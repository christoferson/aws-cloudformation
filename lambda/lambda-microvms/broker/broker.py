import json
import os
import re
import time

import boto3
from botocore.exceptions import ClientError

microvms = boto3.client("lambda-microvms")
table = boto3.resource("dynamodb").Table(os.environ["SESSION_TABLE"])

IMAGE_ARN = os.environ["IMAGE_ARN"]
EXECUTION_ROLE_ARN = os.environ["EXECUTION_ROLE_ARN"]
LOG_GROUP = os.environ["LOG_GROUP"]
INGRESS_CONNECTORS = os.environ["INGRESS_CONNECTORS"].split(",")
# Empty = the default, public internet egress. Set a VPC egress connector ARN to lock it down
EGRESS_CONNECTORS = [arn for arn in os.environ.get("EGRESS_CONNECTORS", "").split(",") if arn]
TENANT_PORT = int(os.environ["TENANT_PORT"])
TOKEN_MINUTES = int(os.environ["TOKEN_MINUTES"])
MAX_IDLE_SECONDS = int(os.environ["MAX_IDLE_SECONDS"])
SUSPENDED_SECONDS = int(os.environ["SUSPENDED_SECONDS"])
MAX_DURATION_SECONDS = int(os.environ["MAX_DURATION_SECONDS"])

TENANT_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")
GONE_STATES = {"TERMINATING", "TERMINATED"}


def handler(event, context):
    action = event.get("action")
    tenant_id = event.get("tenantId", "")
    if not TENANT_ID_PATTERN.match(tenant_id):
        return {"error": "tenantId must be 2-63 chars of a-z, 0-9 and '-'"}
    if action == "open":
        return open_session(tenant_id)
    if action == "close":
        return close_session(tenant_id)
    if action == "status":
        item = table.get_item(Key={"tenantId": tenant_id}).get("Item")
        if not item:
            return {"tenantId": tenant_id, "state": "NONE"}
        vm = describe(item["microvmId"])
        return {"tenantId": tenant_id, "microvmId": item["microvmId"], "state": vm["state"] if vm else "TERMINATED"}
    return {"error": "action must be open, close or status"}


def open_session(tenant_id):
    """Return a connection for this tenant, reusing its MicroVM if one is still alive."""
    for _ in range(3):
        item = table.get_item(Key={"tenantId": tenant_id}, ConsistentRead=True).get("Item")
        if item:
            vm = describe(item["microvmId"])
            if vm and vm["state"] not in GONE_STATES:
                # A SUSPENDED MicroVM needs nothing here: autoResumeEnabled wakes it
                # on the first request, with memory and /workspace intact
                return connection(tenant_id, wait_until_running(vm), reused=True)
        generation = int(item["generation"]) + 1 if item else 1
        try:
            vm = launch(tenant_id, generation, item)
        except ClientError as error:
            if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
                continue  # A concurrent call for the same tenant won; read its MicroVM
            raise
        return connection(tenant_id, wait_until_running(vm), reused=False)
    return {"error": "could not open a session for %s, retry" % tenant_id}


def launch(tenant_id, generation, previous):
    network = {"ingressNetworkConnectors": INGRESS_CONNECTORS}
    if EGRESS_CONNECTORS:
        network["egressNetworkConnectors"] = EGRESS_CONNECTORS
    vm = microvms.run_microvm(
        imageIdentifier=IMAGE_ARN,
        executionRoleArn=EXECUTION_ROLE_ARN,
        **network,
        idlePolicy={
            "autoResumeEnabled": True,
            "maxIdleDurationSeconds": MAX_IDLE_SECONDS,
            "suspendedDurationSeconds": SUSPENDED_SECONDS,
        },
        maximumDurationInSeconds=MAX_DURATION_SECONDS,
        # Delivered to the /run hook inside the MicroVM, unique per MicroVM
        runHookPayload=json.dumps({"tenantId": tenant_id}),
        logging={"cloudWatch": {"logGroup": LOG_GROUP, "logStream": "tenant/%s/%d" % (tenant_id, generation)}},
        # Same tenant + generation = same request, so a Lambda retry cannot start a second MicroVM
        clientToken="%s-%d" % (tenant_id, generation),
    )
    condition = "attribute_not_exists(tenantId)" if previous is None else "generation = :previous"
    values = {":previous": previous["generation"]} if previous else {}
    try:
        table.put_item(
            Item={
                "tenantId": tenant_id,
                "microvmId": vm["microvmId"],
                "endpoint": vm["endpoint"],
                "generation": generation,
                "launchedAt": int(time.time()),
                # Matches maximumDurationInSeconds: Lambda has terminated it by then
                "expiresAt": int(time.time()) + MAX_DURATION_SECONDS,
            },
            ConditionExpression=condition,
            **({"ExpressionAttributeValues": values} if values else {}),
        )
    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            # Lost the race after launching: do not leave an orphan MicroVM running
            microvms.terminate_microvm(microvmIdentifier=vm["microvmId"])
        raise
    return vm


def wait_until_running(vm, timeout_seconds=60):
    deadline = time.time() + timeout_seconds
    while vm["state"] == "PENDING" and time.time() < deadline:
        time.sleep(1)
        vm = microvms.get_microvm(microvmIdentifier=vm["microvmId"])
    return vm


def connection(tenant_id, vm, reused):
    if vm["state"] in GONE_STATES or vm["state"] == "PENDING":
        return {"error": "MicroVM %s is %s" % (vm["microvmId"], vm["state"]), "stateReason": vm.get("stateReason")}
    token = microvms.create_microvm_auth_token(
        microvmIdentifier=vm["microvmId"],
        expirationInMinutes=TOKEN_MINUTES,
        # Only the tenant API port. The hook listener on its own port stays unreachable from outside
        allowedPorts=[{"port": TENANT_PORT}],
    )
    return {
        "tenantId": tenant_id,
        "microvmId": vm["microvmId"],
        "state": vm["state"],
        "reused": reused,
        "url": "https://" + vm["endpoint"],
        # A map of header name -> value; send all of them on every request
        "headers": token["authToken"],
        "expiresInMinutes": TOKEN_MINUTES,
    }


def close_session(tenant_id):
    item = table.get_item(Key={"tenantId": tenant_id}, ConsistentRead=True).get("Item")
    if not item:
        return {"tenantId": tenant_id, "closed": False}
    try:
        microvms.terminate_microvm(microvmIdentifier=item["microvmId"])
    except microvms.exceptions.ResourceNotFoundException:
        pass
    table.delete_item(Key={"tenantId": tenant_id})
    return {"tenantId": tenant_id, "microvmId": item["microvmId"], "closed": True}


def describe(microvm_id):
    try:
        return microvms.get_microvm(microvmIdentifier=microvm_id)
    except microvms.exceptions.ResourceNotFoundException:
        return None
