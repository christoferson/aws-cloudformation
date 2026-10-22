
## CloudFormation Hooks - Local Documentation Snapshot

Offline copies of the AWS docs used to build [cloudformation-hooks](../../cloudformation-hooks/), converted from HTML to Markdown.
Downloaded 2026-10-22. Each file starts with its source URL. Check the live page if something looks off.

### Hooks User Guide — Overview

| File | Topic |
|---|---|
| [ug-what-is-cloudformation-hooks.md](ug-what-is-cloudformation-hooks.md) | What are CloudFormation Hooks |
| [ug-creating-and-managing-hooks.md](ug-creating-and-managing-hooks.md) | Hook types: proactive controls, Guard, Lambda, custom |
| [ug-hooks-concepts.md](ug-hooks-concepts.md) | Targets (RESOURCE / STACK / CHANGE_SET / CLOUD_CONTROL), actions, failure mode, annotations, 30 s timeout |
| [ug-doc-history.md](ug-doc-history.md) | Document history (stack-level, Guard and Lambda Hooks: 2024-11-13; annotations: 2025-11-13) |

### Hooks User Guide — Guard Hooks

| File | Topic |
|---|---|
| [ug-guard-hooks.md](ug-guard-hooks.md) | Overview, CLI commands |
| [ug-guard-hooks-write-rules.md](ug-guard-hooks-write-rules.md) | Resource, **stack** and **change set** input shapes, with example rules |
| [ug-guard-hooks-prepare-to-create-hook.md](ug-guard-hooks-prepare-to-create-hook.md) | Execution role (S3 permissions, trust policy) |
| [ug-guard-hooks-activate-hooks.md](ug-guard-hooks-activate-hooks.md) | Activate (console / CLI), configuration JSON, input parameters |
| [ug-guard-hooks-view-logs.md](ug-guard-hooks-view-logs.md) | Output reports in S3 |
| [ug-guard-hooks-delete-hooks.md](ug-guard-hooks-delete-hooks.md) | Delete |

### Hooks User Guide — Lambda Hooks

| File | Topic |
|---|---|
| [ug-lambda-hooks.md](ug-lambda-hooks.md) | Overview, CLI commands |
| [ug-lambda-hooks-create-lambda-function.md](ug-lambda-hooks-create-lambda-function.md) | Request / response, resource, **stack** and **change set** payloads, sample functions |
| [ug-lambda-hooks-prepare-to-create-hook.md](ug-lambda-hooks-prepare-to-create-hook.md) | Execution role (`lambda:InvokeFunction`, trust policy) |
| [ug-lambda-hooks-activate-hooks.md](ug-lambda-hooks-activate-hooks.md) | Activate (console / CLI) |
| [ug-lambda-hooks-view-logs.md](ug-lambda-hooks-view-logs.md) | Function logs |
| [ug-lambda-hooks-delete-hooks.md](ug-lambda-hooks-delete-hooks.md) | Delete |

### Hooks User Guide — Configuration and operations

| File | Topic |
|---|---|
| [ug-hook-configuration-schema.md](ug-hook-configuration-schema.md) | `HookConfiguration` syntax (set-type-configuration) |
| [ug-hooks-stack-level-filtering.md](ug-hooks-stack-level-filtering.md) | `StackFilters`: StackNames / StackRoles, Include / Exclude, ALL / ANY |
| [ug-hooks-target-filtering.md](ug-hooks-target-filtering.md) | `TargetFilters`: Actions, TargetNames, InvocationPoints, Targets |
| [ug-wildcard-hook-targets.md](ug-wildcard-hook-targets.md) | Wildcards in target names |
| [ug-hooks-disable-enable.md](ug-hooks-disable-enable.md) | Disable / enable |
| [ug-hooks-view-invocations.md](ug-hooks-view-invocations.md) | Invocation summary, `list-hook-results`, `get-hook-result` |
| [ug-grant-iam-permissions-for-hooks.md](ug-grant-iam-permissions-for-hooks.md) | IAM permissions to activate Hooks and read results |
| [ug-hooks-kms-key-policy.md](ug-hooks-kms-key-policy.md) | KMS key for encrypting results |
| [ug-creating-hooks-with-cloudformation.md](ug-creating-hooks-with-cloudformation.md) | Hook-related CloudFormation resource types |

### Hooks User Guide — Other Hook types reviewed (no template yet)

| File | Topic |
|---|---|
| [ug-proactive-controls-hooks.md](ug-proactive-controls-hooks.md) | AWS Control Tower proactive controls as Hooks |
| [ug-proactive-controls-hooks-activate-hooks.md](ug-proactive-controls-hooks-activate-hooks.md) | Activate a proactive control-based Hook |
| [ug-hooks-develop.md](ug-hooks-develop.md) | Custom Hooks with the CloudFormation CLI |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-cloudformation-guardhook.md](cfn-aws-resource-cloudformation-guardhook.md) | `AWS::CloudFormation::GuardHook` |
| [cfn-aws-properties-cloudformation-guardhook-s3location.md](cfn-aws-properties-cloudformation-guardhook-s3location.md) | S3Location (RuleLocation: Uri, VersionId) |
| [cfn-aws-properties-cloudformation-guardhook-options.md](cfn-aws-properties-cloudformation-guardhook-options.md) | Options (InputParams) |
| [cfn-aws-properties-cloudformation-guardhook-stackfilters.md](cfn-aws-properties-cloudformation-guardhook-stackfilters.md) | StackFilters |
| [cfn-aws-properties-cloudformation-guardhook-stacknames.md](cfn-aws-properties-cloudformation-guardhook-stacknames.md) | StackNames |
| [cfn-aws-properties-cloudformation-guardhook-stackroles.md](cfn-aws-properties-cloudformation-guardhook-stackroles.md) | StackRoles |
| [cfn-aws-properties-cloudformation-guardhook-targetfilters.md](cfn-aws-properties-cloudformation-guardhook-targetfilters.md) | TargetFilters |
| [cfn-aws-properties-cloudformation-guardhook-targetfiltersitems.md](cfn-aws-properties-cloudformation-guardhook-targetfiltersitems.md) | TargetFiltersItems |
| [cfn-aws-resource-cloudformation-lambdahook.md](cfn-aws-resource-cloudformation-lambdahook.md) | `AWS::CloudFormation::LambdaHook` |
| [cfn-aws-properties-cloudformation-lambdahook-loggingconfig.md](cfn-aws-properties-cloudformation-lambdahook-loggingconfig.md) | LoggingConfig |
| [cfn-aws-properties-cloudformation-lambdahook-stackfilters.md](cfn-aws-properties-cloudformation-lambdahook-stackfilters.md) | StackFilters |
| [cfn-aws-properties-cloudformation-lambdahook-stacknames.md](cfn-aws-properties-cloudformation-lambdahook-stacknames.md) | StackNames |
| [cfn-aws-properties-cloudformation-lambdahook-stackroles.md](cfn-aws-properties-cloudformation-lambdahook-stackroles.md) | StackRoles |
| [cfn-aws-properties-cloudformation-lambdahook-targetfilters.md](cfn-aws-properties-cloudformation-lambdahook-targetfilters.md) | TargetFilters |
| [cfn-aws-properties-cloudformation-lambdahook-targetfiltersitems.md](cfn-aws-properties-cloudformation-lambdahook-targetfiltersitems.md) | TargetFiltersItems |
| [cfn-aws-resource-cloudformation-hooktypeconfig.md](cfn-aws-resource-cloudformation-hooktypeconfig.md) | `AWS::CloudFormation::HookTypeConfig` (custom / third-party Hooks) |

Note: the reference pages show `TargetFilters` wrapping `TargetFiltersItems`, but their own examples (and the templates here) put `Actions` directly under `TargetFilters`.
