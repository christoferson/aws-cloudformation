
## CloudFormation Lambda Hook - stack and change set targets

[cloudformation-hooks-lambda.yaml](cloudformation-hooks-lambda.yaml)

A Lambda Hook calls **your function** before CloudFormation provisions anything. The function returns `SUCCESS` or `FAILED`, plus annotations. This one targets `STACK` and `CHANGE_SET`, runs only for stack `hooks-demo`, and enforces the same policy as the [Guard Hook](../cloudformation-hooks-guard/README.md). For concepts and the test flow, see [../README.md](../README.md).

```
 create-stack / update-stack / create-change-set
   └─► LambdaHook ── role (hooks.cloudformation.amazonaws.com, lambda:InvokeFunction) ──► function
         event.requestData.payload = S3 presigned URL
           STACK       { template, previousTemplate }
           CHANGE_SET  { template, changedResources: [ { action, resourceType, logicalResourceId, beforeContext, afterContext, lineNumber } ] }
         function ── cloudformation:GetTemplateSummary(TemplateBody) ──► Parameters, ResourceTypes, Description
         ◄── { hookStatus, errorCode, message, clientRequestToken, annotations }
```

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-lambda-hook \
  --template-body file://cloudformation-hooks-lambda.yaml --capabilities CAPABILITY_IAM
```

## Request and response

Event, trimmed down:

```json
{
  "clientRequestToken": "f8da6d11-...",
  "stackId": "arn:aws:cloudformation:...:stack/hooks-demo/...",
  "changeSetId": "arn:...:changeSet/remove-table/...",
  "actionInvocationPoint": "CREATE_PRE_PROVISION",
  "requestData": {
    "targetName": "CHANGE_SET", "targetType": "CHANGE_SET",
    "targetLogicalId": "arn:...:changeSet/remove-table/...",
    "payload": "https://s3...."
  },
  "requestContext": { "invocation": 1, "callbackContext": null }
}
```

Response:

```json
{
  "hookStatus": "FAILED",
  "errorCode": "NonCompliant",
  "message": "Change set deletes: DemoTable (AWS::DynamoDB::Table).",
  "clientRequestToken": "f8da6d11-...",
  "annotations": [
    { "annotationName": "ChangeSetHasNoStatefulDeletes", "status": "FAILED",
      "statusMessage": "Change set deletes: DemoTable (AWS::DynamoDB::Table).",
      "remediationMessage": "Keep the resource in the template, ...", "severityLevel": "CRITICAL" }
  ]
}
```

| Field | Values |
|---|---|
| `hookStatus` | `SUCCESS`, `FAILED`, or `IN_PROGRESS`. With `IN_PROGRESS`, the function is invoked again with `callbackContext` after `callbackDelaySeconds`, up to 3 times |
| `errorCode` | Required when the Hook fails. `NonCompliant` = evaluated and rejected. `InternalFailure` = the evaluation itself failed |
| `message` | Truncated to 4096 characters (1024 for Cloud Control API) |
| `annotations[]` | `status` PASSED / FAILED / SKIPPED, `remediationMessage`, `remediationLink`, `severityLevel` INFORMATIONAL … CRITICAL |

`FailureMode` decides what a `FAILED` response does: `FAIL` blocks, and `WARN` continues with a warning.

## Notes

- **Parsing the template:** it comes as the YAML or JSON string you submitted, with nothing resolved. The Python runtime has no YAML library, and CloudFormation short-form tags (`!Ref`) break generic YAML parsers. The function therefore sends the template to `GetTemplateSummary`, which parses it on the CloudFormation side and returns `Parameters`, `ResourceTypes` and `Description`. That API accepts up to 51,200 bytes, so larger templates are reported as `SKIPPED`. To check resource properties, bundle a CloudFormation-aware parser, or use a `RESOURCE` target, which receives resolved properties as JSON.
- **Change set contexts:** `beforeContext` and `afterContext` are JSON strings in which **numbers and booleans are strings** (`"PointInTimeRecoveryEnabled": "false"`). `beforeContext` is null on CREATE, and `afterContext` is null on DELETE.
- **Timeout:** the Hook waits up to 30 seconds. The function timeout is 25 seconds, and the presigned URL download has a 10-second timeout.
- **Invoke permission:** the Hook's execution role grants `lambda:InvokeFunction`, so no Lambda resource-based policy is needed. `LambdaFunction` also accepts a version- or alias-qualified ARN, which lets you pin the evaluated code.
- **Logs:** the function's own log group, `/lambda/<app>/<env>/stack-policy-hook`. The Hook's `LoggingConfig` (CloudFormation's own error logs, with a log role) is not used here.

## Docs

- [../../docs/cloudformation-hooks/ug-lambda-hooks-create-lambda-function.md](../../docs/cloudformation-hooks/ug-lambda-hooks-create-lambda-function.md) (request and response, stack and change set payloads)
- [../../docs/cloudformation-hooks/ug-lambda-hooks-prepare-to-create-hook.md](../../docs/cloudformation-hooks/ug-lambda-hooks-prepare-to-create-hook.md) (execution role)
- [../../docs/cloudformation-hooks/cfn-aws-resource-cloudformation-lambdahook.md](../../docs/cloudformation-hooks/cfn-aws-resource-cloudformation-lambdahook.md)
