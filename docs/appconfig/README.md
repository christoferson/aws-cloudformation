
## AWS AppConfig - Local Documentation Snapshot

Offline copies of the AWS docs used to build [appconfig/appconfig-feature-flag-variants](../../appconfig/appconfig-feature-flag-variants/), converted from HTML to Markdown.
Downloaded 2026-10-21. Each file starts with its source URL. Check the live page if something looks off.

### User Guide — What's new

| File | Topic |
|---|---|
| [ug-doc-history.md](ug-doc-history.md) | AppConfig document history (multi-variant flags, deletion protection, entity-based targeting, experimentation, ...) |

### User Guide — Multi-variant feature flags

| File | Topic |
|---|---|
| [ug-appconfig-creating-multi-variant-feature-flags.md](ug-appconfig-creating-multi-variant-feature-flags.md) | Overview |
| [ug-appconfig-creating-multi-variant-feature-flags-concepts.md](ug-appconfig-creating-multi-variant-feature-flags-concepts.md) | Concepts: variant, rule, default variant (last, no rule), context |
| [ug-appconfig-creating-multi-variant-feature-flags-rules.md](ug-appconfig-creating-multi-variant-feature-flags-rules.md) | Rule evaluation order, the `split` operator and `seed` |
| [ug-appconfig-creating-multi-variant-feature-flags-rules-operators.md](ug-appconfig-creating-multi-variant-feature-flags-rules-operators.md) | Operands and operators |
| [ug-appconfig-creating-multi-variant-feature-flags-procedures.md](ug-appconfig-creating-multi-variant-feature-flags-procedures.md) | Creating multi-variant flags (console) |
| [ug-appconfig-type-reference-feature-flags.md](ug-appconfig-type-reference-feature-flags.md) | `AWS.AppConfig.FeatureFlags` JSON schema (`_variants`, attributes, constraints) |
| [ug-appconfig-creating-feature-flag-configuration-commandline.md](ug-appconfig-creating-feature-flag-configuration-commandline.md) | Creating feature flags (CLI) |
| [ug-appconfig-creating-configuration-and-profile.md](ug-appconfig-creating-configuration-and-profile.md) | Creating flags and free-form configuration |

### User Guide — Retrieving flags (AppConfig Agent)

| File | Topic |
|---|---|
| [ug-appconfig-retrieving-simplified-methods.md](ug-appconfig-retrieving-simplified-methods.md) | Retrieval methods |
| [ug-appconfig-integration-retrieving-feature-flags.md](ug-appconfig-integration-retrieving-feature-flags.md) | `?flag=` and the `Context` header, with sample responses (`_variant`) |
| [ug-appconfig-code-samples-agent-read-feature-flag-with-variants.md](ug-appconfig-code-samples-agent-read-feature-flag-with-variants.md) | Java / Python / JavaScript samples |
| [ug-appconfig-agent-how-to-use-additional-features.md](ug-appconfig-agent-how-to-use-additional-features.md) | Additional agent features |
| [ug-appconfig-integration-lambda-extensions.md](ug-appconfig-integration-lambda-extensions.md) | AppConfig Agent Lambda extension |
| [ug-appconfig-integration-lambda-extensions-add.md](ug-appconfig-integration-lambda-extensions-add.md) | Adding the extension, required IAM actions |
| [ug-appconfig-integration-lambda-extensions-config.md](ug-appconfig-integration-lambda-extensions-config.md) | Extension environment variables (`PREFETCH_LIST`, `HTTP_PORT`, ...) |
| [ug-appconfig-integration-lambda-extensions-versions.md](ug-appconfig-integration-lambda-extensions-versions.md) | Layer ARNs and the public SSM parameters for the latest version |

### User Guide — Other features reviewed

| File | Topic |
|---|---|
| [ug-deletion-protection.md](ug-deletion-protection.md) | Deletion protection account setting |
| [ug-appconfig-experimentation.md](ug-appconfig-experimentation.md) | AppConfig experimentation (no template yet) |

### CloudFormation Template Reference — `AWS::AppConfig::*`

| File | Resource |
|---|---|
| [cfn-aws-resource-appconfig-application.md](cfn-aws-resource-appconfig-application.md) | `AWS::AppConfig::Application` |
| [cfn-aws-resource-appconfig-environment.md](cfn-aws-resource-appconfig-environment.md) | `AWS::AppConfig::Environment` (`Monitors`, `DeletionProtectionCheck`) |
| [cfn-aws-resource-appconfig-configurationprofile.md](cfn-aws-resource-appconfig-configurationprofile.md) | `AWS::AppConfig::ConfigurationProfile` |
| [cfn-aws-resource-appconfig-hostedconfigurationversion.md](cfn-aws-resource-appconfig-hostedconfigurationversion.md) | `AWS::AppConfig::HostedConfigurationVersion` |
| [cfn-aws-resource-appconfig-deploymentstrategy.md](cfn-aws-resource-appconfig-deploymentstrategy.md) | `AWS::AppConfig::DeploymentStrategy` |
| [cfn-aws-resource-appconfig-deployment.md](cfn-aws-resource-appconfig-deployment.md) | `AWS::AppConfig::Deployment` |
| [cfn-aws-resource-appconfig-extension.md](cfn-aws-resource-appconfig-extension.md) | `AWS::AppConfig::Extension` |
| [cfn-aws-resource-appconfig-extensionassociation.md](cfn-aws-resource-appconfig-extensionassociation.md) | `AWS::AppConfig::ExtensionAssociation` |
| [cfn-aws-resource-appconfig-experimentdefinition.md](cfn-aws-resource-appconfig-experimentdefinition.md) | `AWS::AppConfig::ExperimentDefinition` |
| [cfn-aws-resource-appconfig-experimentrun.md](cfn-aws-resource-appconfig-experimentrun.md) | `AWS::AppConfig::ExperimentRun` |

Their 17 property types are saved too, as `cfn-aws-properties-appconfig-<resource>-<propertytype>.md`.
