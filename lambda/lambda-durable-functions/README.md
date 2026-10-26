
## Lambda durable functions vs Step Functions - the same order workflow, both ways

### What durable functions are

A **durable function** is a normal Lambda function with `DurableConfig`. The **Durable Execution SDK** (Python, Node.js / TypeScript, Java, .NET) lets you write a multi-step workflow as **ordinary sequential code**:
- **Steps** are checkpointed and retried.
- **Waits** let the workflow pause for a timer or an external **callback** for up to **1 year**, while the function isn't running and isn't billed for compute.

**How it works: checkpoint and replay.** After a wait or a failure, Lambda invokes the handler **from the top again**, and the SDK **replays** the checkpoint log. Completed steps return their stored result instantly instead of running again.

```
 invocation 1:  reserve ✔(checkpoint) ─ wait_for_callback ─► suspend (no compute)
                                        ... hours / days ... SendDurableExecutionCallbackSuccess
 invocation 2:  reserve ↺(replayed) ─ approval ↺ ─ charge ✔ ─ wait(60s) ─► suspend
 invocation 3:  reserve ↺ ─ approval ↺ ─ charge ↺ ─ wait ↺ ─ ship ✔ ─► SUCCEEDED
```

### The exam answer is still Step Functions

For *"orchestrate several steps / services, human approval, long-running, visual, auditable"*, the expected answer is **AWS Step Functions** (Standard workflow, `.waitForTaskToken` for callbacks, `Wait` state for timers). Durable functions are the newer, **code-first alternative inside Lambda**. Recognize them, but don't pick them over Step Functions unless the question is clearly about keeping workflow logic in Lambda code.

| Template | Built with |
|---|---|
| [lambda-durable-order-approval.yaml](lambda-durable-order-approval.yaml) | **Lambda durable function**: one Python function, `context.step`, `context.wait_for_callback`, `context.wait` |
| [stepfunctions-order-approval.yaml](stepfunctions-order-approval.yaml) | **Step Functions Standard**: no Lambda at all, direct DynamoDB integrations, `.waitForTaskToken`, `Wait` state, `Choice`, `Catch` |

Both run the same workflow and write the order status to DynamoDB:

```
 reserve ─► wait for approval (callback, timeout 1 day) ─┬─ approved ─► charge ─► wait 60 s ─► ship
                                                          └─ rejected / timed out ─► release
```

Offline docs: [../../docs/lambda/README.md](../../docs/lambda/README.md)

----------------------------------------------------------------------------------

## Side by side

| | Lambda durable functions | Step Functions (Standard) |
|---|---|---|
| Workflow defined in | Your code (Python, JS/TS, Java, .NET) | Amazon States Language (JSON/YAML) or the visual designer |
| Runs in | Lambda (`DurableConfig` on the function) | Its own service. Calls 220+ services directly, no code needed |
| Max duration | 1 year (`ExecutionTimeout`). Each invocation is still limited by the function timeout | 1 year (Express: 5 minutes) |
| Step semantics | **At least once**: a step can run again if it fails or the invocation is interrupted, so make steps idempotent | **Exactly once** per state unless you add `Retry` |
| Timer | `context.wait(Duration...)` | `Wait` state |
| Human approval / external system | `wait_for_callback` → callback ID → `SendDurableExecutionCallbackSuccess/Failure` | `.waitForTaskToken` → `$$.Task.Token` → `SendTaskSuccess/Failure` |
| Retries | Step retry strategy in code | `Retry` / `Catch` in ASL |
| Versioning | Executions are **pinned to the function version** that started them (invoke a version or alias) | Executions run on the definition they started with |
| Visibility | `get-durable-execution-history`, CloudWatch | Visual execution graph, full history |
| Pay while waiting | No compute charge during waits | Charged per state transition, not for waiting |
| Rules | Deterministic code outside steps. Durable execution can only be enabled at **creation** | — |
| Best for (AWS) | Lambda-centric app logic, distributed transactions, AI workflows written in code | Cross-service orchestration, business processes, visual / auditable workflows |

AWS's own guidance:
- **Durable functions:** your team wants standard languages and the logic lives mostly in Lambda.
- **Step Functions:** you orchestrate many AWS services, need a visual workflow for other teams, or want zero maintenance (no runtime or SDK updates).
- **Hybrid:** Step Functions for the high-level flow, durable functions inside Lambda-heavy steps.

### Things that trip people up (durable)

- **Qualified invocation:** invoke a **version, alias or `$LATEST`**. An unqualified function name is rejected. `$LATEST` executions resume on whatever code is current, so use versions or aliases in production.
- **IAM uses qualified ARNs:** permissions are checked against the *durable execution* ARN (`function:<name>:<version>/durable-execution/...`), so use `function:<name>:*` in policies. The execution role needs `lambda:CheckpointDurableExecution` and `lambda:GetDurableExecutionState`, which come with the managed policy `AWSLambdaBasicDurableExecutionRolePolicy`.
- **Replay determinism:** code outside steps runs on **every replay**. Never put `random`, `datetime.now()` or API calls there; put them in a step.
- **Don't catch `BaseException`:** the SDK suspends by raising `SuspendExecution` (a `BaseException`). Catch specific errors such as `CallbackError`.
- **Callback result:** it arrives as the **raw string** you sent, and the template parses it with `json.loads`.
- **Error handling:** dead-letter queues are supported, Lambda destinations are not. Event source mappings start a new execution per invocation (no idempotency there), so use an execution name for idempotent starts.

----------------------------------------------------------------------------------

## Deploy and try it

### Durable function

```bash
aws cloudformation create-stack --stack-name myapp-dev-durable-orders \
  --template-body file://lambda-durable-order-approval.yaml --capabilities CAPABILITY_NAMED_IAM

ALIAS=$(aws cloudformation describe-stacks --stack-name myapp-dev-durable-orders \
  --query "Stacks[0].Outputs[?OutputKey=='OrderWorkflowAliasArn'].OutputValue" --output text)

# Asynchronous: returns immediately; the execution can run for days (synchronous is capped at 15 minutes)
aws lambda invoke --function-name $ALIAS --invocation-type Event \
  --cli-binary-format raw-in-base64-out --payload '{"orderId":"o-1001","amount":42}' /dev/null

aws dynamodb get-item --table-name myapp-dev-durable-orders --key '{"orderId":{"S":"o-1001"}}'
# status AWAITING_APPROVAL, callbackId ...   <- the function is suspended now

CB=$(aws dynamodb get-item --table-name myapp-dev-durable-orders --key '{"orderId":{"S":"o-1001"}}' \
  --query "Item.callbackId.S" --output text)
aws lambda send-durable-execution-callback-success --callback-id "$CB" \
  --cli-binary-format raw-in-base64-out --result '{"approved": true}'
# reject: aws lambda send-durable-execution-callback-failure --callback-id "$CB" ...

# CHARGED, then SHIPPED after ShippingDelaySeconds
aws lambda list-durable-executions-by-function --function-name myapp-dev-order-workflow:live
aws lambda get-durable-execution-history --durable-execution-arn <arn from the list>
```

### Step Functions

```bash
aws cloudformation create-stack --stack-name myapp-dev-sfn-orders \
  --template-body file://stepfunctions-order-approval.yaml --capabilities CAPABILITY_NAMED_IAM

SM=$(aws cloudformation describe-stacks --stack-name myapp-dev-sfn-orders \
  --query "Stacks[0].Outputs[?OutputKey=='OrderWorkflowStateMachineArn'].OutputValue" --output text)
aws stepfunctions start-execution --state-machine-arn $SM --name o-2001 --input '{"orderId":"o-2001","amount":42}'

TOKEN=$(aws dynamodb get-item --table-name myapp-dev-sfn-orders --key '{"orderId":{"S":"o-2001"}}' \
  --query "Item.taskToken.S" --output text)
aws stepfunctions send-task-success --task-token "$TOKEN" --task-output '{"approved": true}'
# reject: aws stepfunctions send-task-failure --task-token "$TOKEN" --error Rejected
```

The execution name (`--name o-2001`) makes the start idempotent: a second start with the same name fails instead of running the order twice.

## Notes

- **SDK packaging:** the durable template uses the SDK **bundled in the `python3.13` runtime**, so inline `ZipFile` code works. AWS recommends packaging the SDK with the function in production (`pip install aws-durable-execution-sdk-python`) to pin its version. The Java and .NET runtimes don't bundle it.
- **New code needs a new version:** `AWS::Lambda::Version` is published once. To deploy new code, change its logical ID (or use SAM `AutoPublishAlias`). Running executions keep replaying on their original version.
- **Approver policies:** both templates create a managed policy for approvers. The durable one allows `lambda:SendDurableExecutionCallback*` on `function:<name>:*`, and the Step Functions one allows `states:SendTask*` on the state machine. Task tokens must be sent from the same account.
- **Other callback targets:** besides the AWS SDK DynamoDB call used here, `.waitForTaskToken` works with the optimized Lambda, SQS, SNS, ECS, EventBridge and API Gateway integrations, among others. Lambda, SQS and SNS are the classic exam examples.

## Docs

- [../../docs/lambda/ug-durable-functions.md](../../docs/lambda/ug-durable-functions.md), [ug-durable-basic-concepts.md](../../docs/lambda/ug-durable-basic-concepts.md) (checkpoint / replay, `DurableConfig`)
- [../../docs/lambda/ug-durable-step-functions.md](../../docs/lambda/ug-durable-step-functions.md) (durable functions or Step Functions)
- [../../docs/lambda/ug-durable-invoking.md](../../docs/lambda/ug-durable-invoking.md) (qualified ARNs, version pinning)
- [../../docs/lambda/ug-durable-security.md](../../docs/lambda/ug-durable-security.md) (execution ARN, callback permissions)
- [../../docs/lambda/ug-durable-execution-idempotency.md](../../docs/lambda/ug-durable-execution-idempotency.md)
- [../../docs/lambda/sfn-connect-to-resource.md](../../docs/lambda/sfn-connect-to-resource.md) (`.waitForTaskToken`)
- [../../docs/lambda/sfn-choosing-workflow-type.md](../../docs/lambda/sfn-choosing-workflow-type.md) (Standard vs Express, exactly-once)
