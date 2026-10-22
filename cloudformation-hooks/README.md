
## CloudFormation Hooks - stack and change set targets (Guard and Lambda)

A Hook runs your checks **before** CloudFormation provisions anything and can **block** the operation (`FAIL`) or let it continue with a warning (`WARN`). Since November 2024, Hooks can target whole **stacks** and **change sets**, not only individual resources, and you can write them without building a registry extension:

| Hook type | CloudFormation resource | Logic lives in |
|---|---|---|
| **Guard Hook** | `AWS::CloudFormation::GuardHook` | Guard rules (`.guard`) in S3 |
| **Lambda Hook** | `AWS::CloudFormation::LambdaHook` | Your Lambda function |
| Custom Hook (older) | `AWS::CloudFormation::HookVersion` + `HookTypeConfig` | A registered extension (CloudFormation CLI project, Java / Python) |

Creating a `GuardHook` or `LambdaHook` resource **activates** the Hook as a private Hook in the account and Region. Deleting the stack removes it.

| Template | Description |
|---|---|
| [cloudformation-hooks-guard/](cloudformation-hooks-guard/README.md) | Guard Hook: rules in S3, output reports to S3 |
| [cloudformation-hooks-lambda/](cloudformation-hooks-lambda/README.md) | Lambda Hook: Python function, annotations with severity and remediation |
| [test-templates/](test-templates/) | Templates to deploy as stack `hooks-demo` to trigger the Hooks |

Both Hooks enforce **the same policy**, so you can compare the two styles:

| Check | Target |
|---|---|
| The template has a `Description` | STACK (and the template inside a CHANGE_SET) |
| The template declares the `Application` and `Environment` parameters | STACK |
| The template has no `AWS::IAM::User` | STACK |
| The change set deletes no DynamoDB table, S3 bucket, RDS or EFS file system | CHANGE_SET |

Offline docs: [../docs/cloudformation-hooks/README.md](../docs/cloudformation-hooks/README.md)

----------------------------------------------------------------------------------

## Concepts

### Targets (`TargetOperations`)

| Target | Runs before | Input | Actions |
|---|---|---|---|
| `RESOURCE` | Each resource create / update / delete in a stack | One resource's properties (resolved) + previous properties | CREATE, UPDATE, DELETE |
| **`STACK`** | `create-stack` / `update-stack` / `delete-stack` | **The whole proposed template** + the previous template | CREATE, UPDATE, DELETE |
| **`CHANGE_SET`** | `create-change-set` | The template + **the list of resource changes** (action, type, before / after) | CREATE only |
| `CLOUD_CONTROL` | Cloud Control API create / update / delete | One resource's properties | CREATE, UPDATE, DELETE |

What only the stack-level targets can check:
- **STACK:** template-wide rules, such as required `Description` or parameters, denied resource types, or naming. The template is the raw string you submitted. Intrinsic functions are **not** resolved, unlike `RESOURCE` input.
- **CHANGE_SET:** what the change *does*, for example "deletes a table". A `RESOURCE` Hook can't catch this one: removing a resource from the template deletes it during `UPDATE_CLEANUP`, which doesn't invoke Hooks (Hooks concepts page).
- **Delete-stack:** the input has no template, so these examples target only CREATE and UPDATE.

### Filters

| Filter | Fields | Notes |
|---|---|---|
| `TargetFilters` | `Actions`, `TargetNames` (resource types, wildcards `AWS::S3::*`), `InvocationPoints` (`PRE_PROVISION`) | `TargetNames` matter for RESOURCE / CLOUD_CONTROL |
| `StackFilters` | `FilteringCriteria` `ALL` / `ANY`, `StackNames` and `StackRoles` with `Include` / `Exclude` (max 50 each) | Ignored for CLOUD_CONTROL. `Include` + `Exclude` = in Include and not in Exclude |

Hooks apply to **every stack in the account and Region** unless filtered. These examples use `StackNames.Include: [hooks-demo]`, so nothing else is affected.

### Failure mode and limits

- **`FAIL`** stops the operation. **`WARN`** continues and records a warning. On a real account, start in `WARN`, review the results, then switch to `FAIL`.
- **Limits:** 30 seconds per invocation and 3 retries. After that the invocation counts as failed.
- **Results:** stack events (the "Hook invocations" column), the console **Invocation summary** (last 90 days), and the CLI:

```bash
aws cloudformation list-hook-results --type-arn <hook-arn> --status HOOK_COMPLETE_FAILED
aws cloudformation get-hook-result --hook-result-id <id>      # annotations: per-check status, remediation, severity
```

### Guard vs Lambda

| | Guard Hook | Lambda Hook |
|---|---|---|
| Logic | Declarative rules, testable locally with `cfn-guard validate` | Any code. It can call AWS APIs |
| STACK / CHANGE_SET input | Parsed for you: template keys at the root, plus `Changes` | Event with an **S3 presigned URL**. You download it and parse the template string (YAML or JSON) yourself |
| Results | `Violation` / `Fix` messages, full report to S3 (`LogBucket`) | `message` + `annotations` (status, remediation message / link, severity) |
| To run | S3 bucket + role (`s3:GetObject`) | Function + role (`lambda:InvokeFunction`) |

----------------------------------------------------------------------------------

## Try it

Deploy one Hook (or both), then use stack `hooks-demo`:

```bash
cd test-templates

# 1. Fails the STACK target: no Description, no parameters, an IAM user
aws cloudformation create-stack --stack-name hooks-demo --template-body file://hooks-demo-noncompliant.yaml --capabilities CAPABILITY_IAM
aws cloudformation describe-stack-events --stack-name hooks-demo \
  --query "StackEvents[?HookStatus!=null].[HookType,HookStatus,HookStatusReason]" --output table
aws cloudformation delete-stack --stack-name hooks-demo   # the rolled-back stack

# 2. Passes
aws cloudformation create-stack --stack-name hooks-demo --template-body file://hooks-demo-compliant.yaml

# 3. Fails the CHANGE_SET target: the change set deletes DemoTable
aws cloudformation create-change-set --stack-name hooks-demo --change-set-name remove-table \
  --template-body file://hooks-demo-remove-table.yaml
aws cloudformation describe-change-set --stack-name hooks-demo --change-set-name remove-table
aws cloudformation list-hook-results --type-arn <hook-arn> --status HOOK_COMPLETE_FAILED
```

In `WARN` mode the same calls succeed, and the results show warnings.

## Docs

- [../docs/cloudformation-hooks/ug-hooks-concepts.md](../docs/cloudformation-hooks/ug-hooks-concepts.md) (targets, actions, failure mode, timeout)
- [../docs/cloudformation-hooks/ug-hooks-stack-level-filtering.md](../docs/cloudformation-hooks/ug-hooks-stack-level-filtering.md)
- [../docs/cloudformation-hooks/ug-hooks-target-filtering.md](../docs/cloudformation-hooks/ug-hooks-target-filtering.md)
- [../docs/cloudformation-hooks/ug-hooks-view-invocations.md](../docs/cloudformation-hooks/ug-hooks-view-invocations.md)
