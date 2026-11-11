<!-- Source: https://docs.aws.amazon.com/lambda/latest/dg/web-functions-networking.html -->
<!-- Downloaded: 2026-11-12 -->

# Configuring networking for AWS Lambda Web Functions

A Web Function accepts requests from clients. It can also reach other resources to do its work, such as a database in your VPC, an internal API, or a service on the public internet. You configure these two directions independently. You can expose an endpoint to callers without granting it VPC access, or give a function private outbound access without changing who can invoke it.

Inbound traffic reaches a Web Function through an endpoint. The endpoint defines its domain name, endpoint type, Regions, and authorization configuration. Outbound traffic is configured on a revision. A revision with no egress network connector reaches public `IPv4` destinations directly. A revision that references a connector sends its outbound traffic through your VPC. A Web Function runs on infrastructure that Lambda owns and manages, not inside your VPC. An egress network connector adds outbound VPC access only. It doesn't change how clients reach the endpoint or who is allowed to invoke it.

###### Note

Web Function endpoint domain names are reachable from the public internet. AWS PrivateLink interface endpoints aren't available for Web Function endpoint domain names. Use the endpoint's authorization configuration to control access.

## Inbound connectivity

Clients invoke a Web Function through a Lambda-managed public HTTPS endpoint. Lambda terminates TLS and forwards the request to your application's HTTP server. The managed endpoint supports HTTP/1.1. It does not expose a private VPC address or accept direct connections to the execution environment.

`IamAuth` controls who can invoke an endpoint, but it does not make the endpoint private at the network layer. For authorization options, see [Lambda Web Function endpoint access control](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-endpoint-access-control.html).

The endpoint controls request routing, authorization, throttling, and scaling. Its endpoint type and Region set are fixed when you create it. To change either property, create a new endpoint and move clients to its new domain name.

Endpoint configuration is independent of VPC egress. Adding an egress network connector to a revision doesn't make the endpoint private and doesn't restrict inbound requests.

###### Important

You can use egress network connectors only with `HomeRegion` endpoints. Lambda rejects attempts to route a `MultiRegion` or `PerRegion` endpoint to a revision that references an egress network connector.

When revision weights split traffic between revisions with different connector configurations, requests use different network paths. When you diagnose intermittent connectivity, check the endpoint's auto-deployment mode and revision weights first. For how they route requests to revisions, see [Deployment patterns](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-deployment.html).

### Add an HTTP front door in front of an endpoint

A front door is a service that receives client requests and forwards them to your endpoint. It adds capabilities such as a custom domain, caching, or web application firewall protection. Web Function endpoints do not support custom domain names or direct AWS WAF association. Use Amazon CloudFront in front of the endpoint when you need a custom domain, edge caching, HTTP/2 or HTTP/3 between the viewer and the edge, response compression, or AWS WAF controls.

The following diagram shows a production front door. A client connects to a CloudFront custom domain protected by AWS WAF. CloudFront sends the request to a protected Web Function endpoint, which routes it to an execution environment. Without an egress network connector, the application can call public AWS service or internet endpoints. It can't reach resources that have only private VPC addresses. To reach those resources, see [Connecting a Web Function to your VPC](#web-functions-networking-vpc). With `IamAuth`, CloudFront signs each origin request, and Lambda authorizes the request before invoking your function. Lambda preserves the viewer's original `Authorization` header and forwards it to your function. The Lambda-provided domain accepts only signed requests from principals with permission to invoke it, and rejects unsigned direct requests, such as a browser calling the domain directly. To ensure the endpoint accepts calls only from your distribution, add a resource-based policy that grants invoke permission to the CloudFront service principal and scopes it to your distribution's Amazon Resource Name (ARN) with a source ARN condition. With `ApplicationManaged`, the endpoint is public, and direct requests bypass CloudFront and AWS WAF.

1.

Configure the Web Function domain as an HTTPS custom origin.
2.

Attach the certificate and alternate domain name to the distribution, and point your Domain Name System (DNS) records to the distribution.
3.

Forward only the headers, cookies, and query strings that the application needs. Don't forward the viewer's `Host` header, because Lambda routes on `Host` and returns HTTP 404 when it isn't the endpoint domain. If you use a managed origin request policy that forwards all viewer headers, choose `AllViewerExceptHostHeader`. The endpoint header limits include forwarded headers.
4.

(Optional) Attach an AWS WAF web ACL when you need IP, bot, rate-based, or managed-rule inspection.
5.

Protect the origin so that clients cannot bypass the distribution. For an IAM-authorized endpoint, grant access only to the intended front-door identity. For application-managed authorization, require and validate an origin secret or other application-level proof that the request came through the distribution.

For the CloudFront authorization procedure, see [CloudFront integration](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-endpoint-access-control.html#web-functions-endpoint-access-control-cloudfront).

### Browser access and CORS

Lambda does not add Cross-Origin Resource Sharing (CORS) headers for Web Functions. Your application or front door must handle preflight and actual requests.

-

Return the allowed origin instead of reflecting every `Origin` value.
-

Allow only the methods and request headers that the application uses.
-

When browsers send credentials, use an explicit origin and return `Access-Control-Allow-Credentials: true`. Do not combine credentials with a wildcard origin.
-

Test `OPTIONS` preflight requests separately from the application method.
-

Authenticate and authorize every protected request. CORS is not an authentication control.

### Streaming and protocol limitations

Web Functions stream request bodies to your application as they arrive and stream responses back to the client over HTTP/1.1. The request path is half-duplex: Lambda forwards the full request body before it delivers your application's response. Read the request body completely before you write the response. Set `timeoutSeconds` to cover streaming in both directions: receiving the request body and sending the response. When the timeout elapses, Lambda ends the response. The client receives the status code already sent, with a truncated body. Stop upstream work when the client disconnects.

Lambda does not support WebSocket upgrades. Lambda removes connection-specific upgrade headers before forwarding the request. Use server-sent events when one-way server-to-client streaming is sufficient.

For the complete header and method contract, see [HTTP requests and responses](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-http.html).

## Outbound connectivity

You choose the outbound network path for each revision.

-

Without an egress network connector – The revision reaches public `IPv4` destinations directly without traversing your VPC. The source address is Lambda-managed, isn't stable, and isn't suitable for an allow list. The revision has no route to private resources in your VPC.
-

With an egress network connector – The revision sends outbound traffic through elastic network interfaces in the connector's subnets. Your VPC route tables, security groups, and network access control lists (ACLs) apply. Use this option to reach private VPC resources, on-premises networks connected through Direct Connect or VPN, or destinations that require traffic from your address space.

Referencing a connector replaces the default outbound path. A connector places traffic in your VPC, but it doesn't provide internet access. To reach public `IPv4` destinations, the connector subnets need a route to a NAT gateway. To reach public `IPv6` destinations, they need a route to an egress-only internet gateway.

There is no stable source IP address for connector traffic. Configure destination security groups to allow the connector's security groups. If a destination doesn't support security-group references, allow the connector subnet CIDR blocks instead of an individual address.

Lambda runs connector operations asynchronously. A connector reports `PENDING` while Lambda creates its network interfaces, and `ACTIVE` when revisions can reference it. Other states include `INACTIVE`, `FAILED`, `DELETING`, and `DELETE_FAILED`.

After an update, check `LastUpdateStatus` for `InProgress`, `Successful`, or `Failed`. If an operation fails, use its state reason and reason code to identify the affected subnet, security group, permissions, or IP address capacity.

### DNS resolution

For private DNS names, enable DNS support and DNS hostnames in the connector's VPC. Associate any required Route 53 private hosted zones with that VPC.

Each execution environment caches DNS answers. After changing a DNS record, existing environments continue using the old answer until the cached value expires or Lambda replaces the environment. To force a clean rollout, create a new revision and shift endpoint traffic to it.

When troubleshooting, test name resolution and network reachability separately. Connect to a destination by IP address to verify the network path, then test its DNS name.

## Connecting a Web Function to your VPC

An egress network connector is a reusable Lambda resource. You create the connector once and reference a published connector version from each Web Function revision that needs VPC access.

For Web Functions, the connector reference has the following properties:

-

A revision references zero or one connector.
-

The connector ARN must include a version qualifier.
-

The connector must be in the same AWS account and Region as the Web Function.
-

The connector must have `WebFunction` as its associated compute resource type.
-

Only a `HomeRegion` endpoint supports revisions that reference an egress network connector.
-

You can't change the reference after you set it. To add, change, or remove it, create a new revision.

### Prerequisites

Before you create the connector:

-

Choose at least two subnets in different Availability Zones with available IP addresses.
-

Choose security groups that allow the required outbound traffic.
-

Allow inbound traffic from the connector's security groups on each destination.
-

Configure routes from the connector subnets to the required private, on-premises, or public destinations.
-

Create an operator role that grants Lambda permission to manage network interfaces.
-

Make sure that the identity that creates the connector and the revision has the permissions in [Permissions for configuring networking](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-permissions.html#web-functions-permissions-networking), including `lambda:PassNetworkConnector` on the connector and `iam:PassRole` on the operator role.

The connector's operator role and the revision's execution role serve different purposes. The operator role manages network interfaces in your VPC. The execution role grants your application permission to call AWS APIs. You don't add connector network-interface permissions to the execution role.

### Operator role permissions

Lambda assumes the connector's operator role to manage the connector's network interfaces. The role's trust policy must allow the Lambda service principal, `lambda.amazonaws.com`, to assume it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Attach a permissions policy like the following to the connector's operator role. This policy allows Lambda to create and tag the connector's network interfaces:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateENI",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterface",
      "Resource": [
        "arn:aws:ec2:*:*:network-interface/*",
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
      ]
    },
    {
      "Sid": "TagENI",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": "arn:aws:ec2:*:*:network-interface/*",
      "Condition": {
        "StringEquals": {
          "ec2:ManagedResourceOperator": "network-connectors.lambda.amazonaws.com"
        }
      }
    }
  ]
}
```

### Create a connector

The following AWS CLI command creates an `IPv4` connector for Web Functions. Replace the connector name, subnet IDs, security group ID, and operator role ARN with your own values.

```
aws lambda-core create-network-connector \
  --name my-connector \
  --configuration '{
    "VpcEgressConfiguration": {
      "SubnetIds": [
        "subnet-0ab1c2d3e4f5a6b78",
        "subnet-1bc2d3e4f5a6b7c89"
      ],
      "SecurityGroupIds": ["sg-0123456789abcdef0"],
      "NetworkProtocol": "IPv4",
      "AssociatedComputeResourceTypes": ["WebFunction"]
    }
  }' \
  --operator-role arn:aws:iam::123456789012:role/NetworkConnectorOperatorRole
```

A connector supports one compute resource type. A connector for Web Functions doesn't support another Lambda compute type, and its compute resource type is immutable.

Lambda creates the connector asynchronously. Use `get-network-connector` to wait until its `State` is `ACTIVE`, and note the current version number.

### Reference the connector from a revision

Set `serviceConfig.egressNetworkConnectorArn` when you create the Web Function's first revision or a later revision. Use a version-qualified ARN:

```
arn:aws:lambda:us-east-1:123456789012:network-connector:nc-0a1b2c3d4e5f6a7b8:4
```

The following AWS CLI command creates a revision that references connector version 4. Replace the function name, execution role ARN, connector ARN, and Region with your own values.

```
aws lambda-web create-web-function-revision \
  --function-name my-web-function \
  --build-config file://build-config.json \
  --service-config '{
    "executionRoleArn": "arn:aws:iam::123456789012:role/WebFunctionExecutionRole",
    "timeoutSeconds": 30,
    "egressNetworkConnectorArn": "arn:aws:lambda:us-east-1:123456789012:network-connector:nc-0a1b2c3d4e5f6a7b8:4"
  }' \
  --region us-east-1
```

An unqualified ARN, connector name, or connector ID isn't accepted on a revision. After creating the revision:

-

Wait until the revision's state is `Active`.
-

Read the revision and confirm that `egressNetworkConnectorArn` contains the expected connector version.
-

Confirm that the endpoint routes traffic to the revision. A `HomeRegion` endpoint in `LatestRevision` mode picks up the latest active revision automatically. For an endpoint in `Disabled` mode, update its revision weights.
-

Test a VPC destination and confirm the traffic with VPC Flow Logs.

The endpoint's automatic deployment mode determines whether creating an active revision updates routing automatically. In all modes, confirm which revision is serving before testing its connector.

## Updating or removing VPC connectivity

Updating a connector publishes a new version. Existing revisions remain pinned to the version in their connector ARN.

To roll out a connector change:

-

Update the connector with `update-network-connector`. The connector must be `ACTIVE`. Provide the complete `VpcEgressConfiguration`, including every subnet ID and security group ID that you want to keep, because the update replaces the existing configuration.
-

Wait for the connector's `LastUpdateStatus` to become `Successful`.
-

Get the new connector version.
-

Create a revision that references the new version-qualified ARN.
-

For a `HomeRegion` endpoint in `LatestRevision` mode, confirm that it picked up the new active revision. For an endpoint in `Disabled` mode, shift traffic by updating its revision weights.

Updating the connector without creating a revision that references its new version doesn't change the network configuration of running Web Functions.

To remove VPC connectivity, create a revision without `egressNetworkConnectorArn`. A `HomeRegion` endpoint in `LatestRevision` mode picks it up when it becomes active. For an endpoint in `Disabled` mode, shift traffic by updating its revision weights. The new revision uses Lambda-managed public `IPv4` egress and no longer has private VPC access.

###### Note

Before deleting an egress network connector, shift endpoint traffic away from every Web Function revision that references any version of the connector, and then delete those revisions. Deleting a connector while an active revision still references it interrupts network connectivity for both existing and new execution environments serving that revision.

## IPv6 support

The default outbound path and an `IPv4` connector support `IPv4` only. To use `IPv6`, configure the connector with `NetworkProtocol` set to `DualStack`.

For dual-stack connectivity:

-

The VPC and connector subnets must have `IPv6` CIDR blocks.
-

Route tables must contain routes for the required `IPv6` destinations.
-

Security groups and network ACLs must allow `IPv6` traffic.
-

Public `IPv6` access requires a ::/0 route to an egress-only internet gateway.
-

Reference the connector version that was created when you updated the connector to `DualStack`.

Don't determine `IPv6` availability by inspecting interfaces inside an execution environment. Verify it by making an `IPv6` connection from application code and checking VPC Flow Logs.
