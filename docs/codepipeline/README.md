
## CodePipeline V2 - Local Documentation Snapshot

Offline copies of the AWS docs used to build the templates in [codepipeline-v2](../../codepipeline-v2/), converted from HTML to Markdown.
Downloaded 2026-10-18. Each file starts with its source URL — check the live page if something looks off.

Tables and lists were converted automatically, so some formatting is rough (notably the comparison table in `pipeline-types-planning.md`; a clean version is in [codepipeline-v2/README.md](../../codepipeline-v2/README.md)).

### User Guide

| File | Topic |
|---|---|
| [pipeline-types-planning.md](pipeline-types-planning.md) | V1 vs V2 feature comparison + cost analyzer script |
| [ug-concepts-how-it-works.md](ug-concepts-how-it-works.md) | Execution modes: SUPERSEDED / QUEUED / PARALLEL |
| [ug-reference-variables.md](ug-reference-variables.md) | Variables, namespaces, `#{namespace.key}` syntax |
| [ug-action-reference-Commands.md](ug-action-reference-Commands.md) | Commands action (V2 only) |
| [ug-stage-retry.md](ug-stage-retry.md) | Manual and automatic stage retry |
| [ug-stage-conditions.md](ug-stage-conditions.md) | Entry / OnFailure / OnSuccess conditions and rules |
| [ug-rule-reference.md](ug-rule-reference.md) | Rule providers for conditions (index only) |
| [ug-pipelines-filter.md](ug-pipelines-filter.md) | Triggers: Git tag / branch / file path / pull request filters |

### CloudFormation Template Reference — `AWS::CodePipeline::Pipeline`

| File | Property type |
|---|---|
| [aws-resource-codepipeline-pipeline.md](aws-resource-codepipeline-pipeline.md) | Pipeline resource (PipelineType, ExecutionMode, Triggers, Variables) |
| [cfn-pipeline-stagedeclaration.md](cfn-pipeline-stagedeclaration.md) | StageDeclaration (BeforeEntry, OnFailure, OnSuccess) |
| [cfn-pipeline-actiondeclaration.md](cfn-pipeline-actiondeclaration.md) | ActionDeclaration (Commands, EnvironmentVariables, OutputVariables) |
| [cfn-pipeline-outputartifact.md](cfn-pipeline-outputartifact.md) | OutputArtifact (Files) |
| [cfn-pipeline-environmentvariable.md](cfn-pipeline-environmentvariable.md) | EnvironmentVariable |
| [cfn-pipeline-variabledeclaration.md](cfn-pipeline-variabledeclaration.md) | VariableDeclaration |
| [cfn-pipeline-failureconditions.md](cfn-pipeline-failureconditions.md) | FailureConditions (ROLLBACK / RETRY) |
| [cfn-pipeline-retryconfiguration.md](cfn-pipeline-retryconfiguration.md) | RetryConfiguration |
| [cfn-pipeline-successconditions.md](cfn-pipeline-successconditions.md) | SuccessConditions |
| [cfn-pipeline-beforeentryconditions.md](cfn-pipeline-beforeentryconditions.md) | BeforeEntryConditions |
| [cfn-pipeline-condition.md](cfn-pipeline-condition.md) | Condition |
| [cfn-pipeline-ruledeclaration.md](cfn-pipeline-ruledeclaration.md) | RuleDeclaration |
| [cfn-pipeline-pipelinetriggerdeclaration.md](cfn-pipeline-pipelinetriggerdeclaration.md) | PipelineTriggerDeclaration |
| [cfn-pipeline-gitconfiguration.md](cfn-pipeline-gitconfiguration.md) | GitConfiguration |
| [cfn-pipeline-gitpushfilter.md](cfn-pipeline-gitpushfilter.md) | GitPushFilter |
