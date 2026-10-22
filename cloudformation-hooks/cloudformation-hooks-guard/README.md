
## CloudFormation Guard Hook - stack and change set targets

[cloudformation-hooks-guard.yaml](cloudformation-hooks-guard.yaml) · [hook-rules.guard](hook-rules.guard)

A Guard Hook evaluates **Guard rules stored in S3** before CloudFormation provisions anything. This one targets `STACK` and `CHANGE_SET`, and runs only for stack `hooks-demo`. For concepts and the test flow, see [../README.md](../README.md).

```
 create-stack / update-stack ──► STACK input       ┐
 create-change-set           ──► CHANGE_SET input  ┴► GuardHook ── reads ──► s3://<rules-bucket>/hook-rules.guard
                                                        │  role: hooks.cloudformation.amazonaws.com
                                                        ├─ FAIL / WARN back to CloudFormation
                                                        └─ report ──► s3://<reports-bucket>/
```

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-guard-hook \
  --template-body file://cloudformation-hooks-guard.yaml --capabilities CAPABILITY_IAM

BUCKET=$(aws cloudformation describe-stacks --stack-name myapp-dev-guard-hook \
  --query "Stacks[0].Outputs[?OutputKey=='GuardRulesBucketName'].OutputValue" --output text)
aws s3 cp hook-rules.guard s3://$BUCKET/hook-rules.guard
```

The Hook downloads the rules **on every invocation**, so changing them is just another `aws s3 cp`. To stop a bucket change from silently altering the rules, set `RuleLocation.VersionId`, since the bucket is versioned.

## What the rules see

For `STACK` and `CHANGE_SET` targets, the **proposed template sits at the root**, so the rules look like ordinary template rules:

```
HookContext: { AWSAccountID, StackId, HookTypeName, InvocationPoint, TargetName, TargetType, ChangeSetId, ... }
AWSTemplateFormatVersion / Description / Parameters / Resources / ...    # proposed template (as submitted)
Previous: { ...last deployed template... }                              # empty on create
Changes: [ { logicalResourceId, resourceType, action, lineNumber,       # CHANGE_SET only
             beforeContext, afterContext } ]                            # JSON strings -> json_parse()
```

| Rule | Gate | Fails when |
|---|---|---|
| `TEMPLATE_HAS_DESCRIPTION` | `when Resources exists` (skips delete-stack input, which has no template) | No `Description` |
| `TEMPLATE_HAS_APPLICATION_ENVIRONMENT_PARAMETERS` | `when Resources exists` | `Parameters.Application` or `Parameters.Environment` is missing |
| `TEMPLATE_HAS_NO_IAM_USERS` | `when %iam_users !empty` | Any `AWS::IAM::User` |
| `CHANGE_SET_HAS_NO_STATEFUL_DELETES` | `when %stateful_deletes !empty` (only CHANGE_SET input has `Changes`) | A `DELETE` of a protected resource type |

The `when %x !empty { %x empty }` pattern means "fail if anything matches". Each rule's `<< Violation / Fix >>` text appears in the Hook result and in the S3 report.

The template rules can be tested locally, because a template file has the same shape as the STACK input:

```bash
cfn-guard validate --rules hook-rules.guard --data ../test-templates/hooks-demo-noncompliant.yaml   # 3 failures
cfn-guard validate --rules hook-rules.guard --data ../test-templates/hooks-demo-compliant.yaml      # pass
```

## Notes

- **Raw template:** the STACK and CHANGE_SET template is the string you submitted. `!Ref` and `!Sub` are not resolved, and parameters are not substituted. Check resolved property values with a `RESOURCE` target instead.
- **Input parameters:** `Options.InputParams` points to up to 10 YAML or JSON files in S3 that hold data for the rules. Their top-level keys must be unique across files.
- **IAM:** the execution role needs `s3:GetObject`, `s3:GetObjectVersion` and `s3:ListBucket` on the rules bucket, and `s3:PutObject` on the report bucket. It is trusted by `hooks.cloudformation.amazonaws.com`.
- **Cleanup:** empty both buckets (including all object versions in the rules bucket) before deleting the stack.

## Docs

- [../../docs/cloudformation-hooks/ug-guard-hooks-write-rules.md](../../docs/cloudformation-hooks/ug-guard-hooks-write-rules.md) (resource, stack and change set input)
- [../../docs/cloudformation-hooks/ug-guard-hooks-prepare-to-create-hook.md](../../docs/cloudformation-hooks/ug-guard-hooks-prepare-to-create-hook.md) (execution role)
- [../../docs/cloudformation-hooks/ug-guard-hooks-activate-hooks.md](../../docs/cloudformation-hooks/ug-guard-hooks-activate-hooks.md)
- [../../docs/cloudformation-hooks/cfn-aws-resource-cloudformation-guardhook.md](../../docs/cloudformation-hooks/cfn-aws-resource-cloudformation-guardhook.md)
