
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
| [ug-action-reference-commands.md](ug-action-reference-commands.md) | Commands action (V2 only) |
| [ug-stage-retry.md](ug-stage-retry.md) | Manual and automatic stage retry |
| [ug-stage-conditions.md](ug-stage-conditions.md) | Entry / OnFailure / OnSuccess conditions and rules |
| [ug-rule-reference.md](ug-rule-reference.md) | Rule providers for conditions (index only) |
| [ug-pipelines-filter.md](ug-pipelines-filter.md) | Triggers: Git tag / branch / file path / pull request filters |
| [ug-pipelines-triggers.md](ug-pipelines-triggers.md) | Triggers: valid filter combinations, OR/AND logic, PR events by provider, examples |
| [ug-pipelines-filter-cli.md](ug-pipelines-filter-cli.md) | Triggers: CLI walkthrough |
| [ug-pipelines-trigger-source-repo-changes-cli.md](ug-pipelines-trigger-source-repo-changes-cli.md) | Change detection for source repos (CLI) |
| [ug-syntax-glob.md](ug-syntax-glob.md) | Glob pattern syntax for trigger filters |
| [ug-pipelines-trigger-source-overrides.md](ug-pipelines-trigger-source-overrides.md) | Source revision override at start |
| [ug-action-reference-codestar-connection-source.md](ug-action-reference-codestar-connection-source.md) | CodeConnections source action (GitHub / GitLab / Bitbucket) |
| [ug-connections-github.md](ug-connections-github.md) | Creating a GitHub connection |
| [ug-tutorials-github-gitclone.md](ug-tutorials-github-gitclone.md) | Tutorial: full clone (`CODEBUILD_CLONE_REF`) |
| [ug-pipeline-requirements.md](ug-pipeline-requirements.md) | Pipeline structure reference (field definitions) |
| [ug-action-reference-pipeline-invoke.md](ug-action-reference-pipeline-invoke.md) | Invoke action: start another pipeline with source revisions + variables (V2) |
| [ug-action-reference-codecommit.md](ug-action-reference-codecommit.md) | CodeCommit source action, output variables, permissions |
| [ug-action-reference-ecr-build-and-publish.md](ug-action-reference-ecr-build-and-publish.md) | ECRBuildAndPublish build action (V2) |
| [ug-action-reference-ec2-deploy.md](ug-action-reference-ec2-deploy.md) | EC2 deploy action (V2) |
| [ug-action-reference-lambda-deploy.md](ug-action-reference-lambda-deploy.md) | Lambda deploy action (V2) |
| [ug-action-reference-eks.md](ug-action-reference-eks.md) | EKS deploy action (V2) |

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
| [cfn-pipeline-gitpullrequestfilter.md](cfn-pipeline-gitpullrequestfilter.md) | GitPullRequestFilter |
| [cfn-pipeline-gitbranchfiltercriteria.md](cfn-pipeline-gitbranchfiltercriteria.md) | GitBranchFilterCriteria |
| [cfn-pipeline-gitfilepathfiltercriteria.md](cfn-pipeline-gitfilepathfiltercriteria.md) | GitFilePathFilterCriteria |
| [cfn-pipeline-gittagfiltercriteria.md](cfn-pipeline-gittagfiltercriteria.md) | GitTagFilterCriteria |

### CloudFormation Template Reference — Connections

| File | Resource |
|---|---|
| [cfn-codestarconnections-connection.md](cfn-codestarconnections-connection.md) | `AWS::CodeStarConnections::Connection` |
