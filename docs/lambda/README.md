
## AWS Lambda durable functions (and Step Functions) - Local Documentation Snapshot

Offline copies of the AWS docs used to build [lambda/lambda-durable-functions](../../lambda/lambda-durable-functions/), converted from HTML to Markdown.
Downloaded 2026-10-25. Each file starts with its source URL. Check the live page if something looks off.

### Lambda Developer Guide — Durable functions

| File | Topic |
|---|---|
| [ug-durable-functions.md](ug-durable-functions.md) | Overview: checkpoint / replay, up to 1 year, when to use, comparison with Step Functions |
| [ug-durable-basic-concepts.md](ug-durable-basic-concepts.md) | Durable execution, replay and determinism, `DurableContext`, `ExecutionTimeout` vs function timeout, retention |
| [ug-durable-getting-started.md](ug-durable-getting-started.md) | Creating durable functions |
| [ug-durable-getting-started-cli.md](ug-durable-getting-started-cli.md) | CLI: create, invoke, list, history, stop |
| [ug-durable-getting-started-iac.md](ug-durable-getting-started-iac.md) | CloudFormation, CDK, SAM, Terraform (version + alias required) |
| [ug-durable-configuration.md](ug-durable-configuration.md) | `DurableConfig`: `ExecutionTimeout`, `RetentionPeriodInDays`, `KMSKeyArn`; only at creation |
| [ug-durable-step-functions.md](ug-durable-step-functions.md) | Durable functions or Step Functions: decision framework, feature table, hybrid |
| [ug-durable-examples.md](ug-durable-examples.md) | Examples: distributed transactions, human approval (`wait_for_callback`), pipelines, map / parallel |
| [ug-durable-security.md](ug-durable-security.md) | Execution ARN, execution role, callback permissions |
| [ug-durable-encryption.md](ug-durable-encryption.md) | Encrypting execution data with a customer managed key |
| [ug-durable-execution-sdk.md](ug-durable-execution-sdk.md) | Durable Execution SDK |
| [ug-durable-supported-runtimes.md](ug-durable-supported-runtimes.md) | Supported runtimes, SDK bundled in Node.js / Python runtimes |
| [ug-durable-invoking.md](ug-durable-invoking.md) | Sync / async invocation, qualified ARNs, version pinning, lifecycle |
| [ug-durable-invoking-esm.md](ug-durable-invoking-esm.md) | Event source mappings with durable functions |
| [ug-durable-execution-sdk-retries.md](ug-durable-execution-sdk-retries.md) | Retries |
| [ug-durable-execution-idempotency.md](ug-durable-execution-idempotency.md) | Execution names, at-least-once steps |
| [ug-durable-testing.md](ug-durable-testing.md) | Testing |
| [ug-durable-monitoring.md](ug-durable-monitoring.md) | Monitoring |
| [ug-durable-best-practices.md](ug-durable-best-practices.md) | Best practices |

### Lambda API Reference

| File | Operation |
|---|---|
| [api-SendDurableExecutionCallbackSuccess.md](api-SendDurableExecutionCallbackSuccess.md) | `SendDurableExecutionCallbackSuccess` (CallbackId, Result up to 1 MB) |
| [api-ListDurableExecutionsByFunction.md](api-ListDurableExecutionsByFunction.md) | `ListDurableExecutionsByFunction` |

### Step Functions Developer Guide (for the comparison template)

| File | Topic |
|---|---|
| [sfn-connect-to-resource.md](sfn-connect-to-resource.md) | Integration patterns: Request Response, `.sync`, `.waitForTaskToken`; AWS SDK integrations |
| [sfn-connect-ddb.md](sfn-connect-ddb.md) | DynamoDB integration |
| [sfn-connect-sqs.md](sfn-connect-sqs.md) | SQS integration |
| [sfn-choosing-workflow-type.md](sfn-choosing-workflow-type.md) | Standard vs Express (1 year vs 5 minutes, exactly-once vs at-least-once) |
| [sfn-service-quotas.md](sfn-service-quotas.md) | Quotas |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-lambda-function.md](cfn-aws-resource-lambda-function.md) | `AWS::Lambda::Function` (`DurableConfig`) |
| [cfn-aws-properties-lambda-function-durableconfig.md](cfn-aws-properties-lambda-function-durableconfig.md) | DurableConfig (`ExecutionTimeout` 1–31622400, `RetentionPeriodInDays` 1–90) |

### SDK source checked

The Python SDK signatures used in the template were checked against https://github.com/aws/aws-durable-execution-sdk-python (`context.py`, `config.py`, `exceptions.py`):
- **`wait_for_callback`:** `submitter(callback_id, wait_context)`, configured with `WaitForCallbackConfig(timeout=Duration)`.
- **`wait`:** takes a `Duration`.
- **Callback results:** pass-through, so the raw string is returned.
- **Suspension:** `SuspendExecution` is a `BaseException`.
