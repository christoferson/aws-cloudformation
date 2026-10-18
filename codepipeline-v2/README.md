
## CodePipeline V2 CloudFormation Templates

Templates for **V2 type** pipelines. V1 templates live in [../codepipeline/README.md](../codepipeline/README.md).

Offline AWS docs used to build these: [docs/codepipeline/README.md](../docs/codepipeline/README.md)

----------------------------------------------------------------------------------

## V1 vs V2 at a glance

A V2 pipeline has the same structure as V1 (stages → actions → artifacts). V2 adds properties on top.
Switching is one property: `PipelineType: V2`. It updates in place ("Update requires: No interruption"), so the pipeline is **not** replaced.

| Capability | V1 | V2 | CloudFormation property |
|---|---|---|---|
| Action-level variables (`#{Namespace.Key}`) | Yes | Yes | `Actions[].Namespace` |
| SUPERSEDED execution mode (default) | Yes | Yes | `ExecutionMode: SUPERSEDED` |
| **QUEUED execution mode** | – | **Yes** | `ExecutionMode: QUEUED` |
| **PARALLEL execution mode** | – | **Yes** | `ExecutionMode: PARALLEL` |
| **Pipeline-level variables** (override per run) | – | **Yes** | `Variables` |
| **Commands action** (no CodeBuild project) | – | **Yes** | `ActionTypeId.Provider: Commands` + `Commands` |
| **Stage automatic retry on failure** | – | **Yes** | `Stages[].OnFailure.Result: RETRY` |
| **Stage rollback** | – | **Yes** | `Stages[].OnFailure.Result: ROLLBACK` |
| **Stage conditions** (entry / on-failure / on-success rules) | – | **Yes** | `BeforeEntry`, `OnFailure.Conditions`, `OnSuccess` |
| **Entry condition with Skip result** | – | **Yes** | `BeforeEntry.Conditions[].Result: SKIP` |
| **Triggers + filters** (Git tags, branches, file paths, PRs) | – | **Yes** | `Triggers` |
| **Source revision overrides** at start | – | **Yes** | CLI `start-pipeline-execution --source-revisions` |

Source: [docs/codepipeline/pipeline-types-planning.md](../docs/codepipeline/pipeline-types-planning.md)

### Pricing model changes

- **V1**: billed per active pipeline per month.
- **V2**: billed per **action-execution minute**. Manual approval and custom actions aren't billed. An idle V2 pipeline costs nothing; a busy one can cost more than V1.
- **Commands action** is billed separately as CodeBuild compute minutes.
- AWS's planning page includes a script that estimates what a V1 pipeline would cost as V2 (see docs/codepipeline/pipeline-types-planning.md).

> **Heads-up:** any V2-only property in the template (for example `Triggers` or `Variables`) makes the pipeline V2, with V2 billing.

----------------------------------------------------------------------------------

## What's new in V2 — explained

### 1. Execution modes — `ExecutionMode`

How CodePipeline handles a new execution while another one is running.

| Mode | Behavior | Use when |
|---|---|---|
| `SUPERSEDED` (default, V1 + V2) | A newer execution can overtake and replace an older one waiting at a stage boundary | Only the latest commit matters |
| `QUEUED` (V2) | Executions wait their turn and run one at a time, in order | Every change must deploy, in order |
| `PARALLEL` (V2) | Executions run independently, with no queue | Dev / feature-branch pipelines with separate targets |

- PARALLEL **cannot** be combined with stage rollback (`OnFailure.Result: ROLLBACK`).
- In PARALLEL mode, S3 and CodeCommit sources always fetch the **latest** revision, which may not be the one that triggered the run.

```yaml
PipelineType: V2
ExecutionMode: QUEUED
```

### 2. Pipeline-level variables — `Variables`

You declare variables once on the pipeline and give each a default. You can set a different value each time you start the pipeline. This lets one pipeline replace near-duplicate copies (for example, one per version or target).

```yaml
Variables:
  - Name: ReleaseVersion
    DefaultValue: latest
    Description: Version label
```

Reference: `#{variables.ReleaseVersion}`. Override per run:

```bash
aws codepipeline start-pipeline-execution --name <pipeline> \
  --variables name=ReleaseVersion,value=v2
```

- Max 50 variables. Name pattern `[A-Za-z0-9@\-_]+`.
- **Not usable in Source actions.**
- `variables` is a reserved namespace. Don't give an action `Namespace: variables`.

Namespaces in V2:

| Namespace | Example | Available in |
|---|---|---|
| `codepipeline` (reserved) | `#{codepipeline.PipelineExecutionId}` | V1 + V2 |
| `variables` (reserved) | `#{variables.ReleaseVersion}` | V2 |
| Action `Namespace` | `#{SourceVariables.VersionId}` | V1 + V2 |

### 3. Commands action

Run shell commands on CodePipeline-managed CodeBuild compute, **without creating an `AWS::CodeBuild::Project` or a buildspec**.

```yaml
- Name: BuildCommands
  ActionTypeId:
    Category: Compute        # new category
    Owner: AWS
    Provider: Commands
    Version: "1"
  Namespace: BuildVariables
  Configuration:
    EnvironmentType: LINUX_CONTAINER      # or WINDOWS_SERVER_2022_CONTAINER
    ComputeType: BUILD_GENERAL1_SMALL     # SMALL | MEDIUM | LARGE
  EnvironmentVariables:                   # action property, not Configuration
    - Name: RELEASE_VERSION
      Value: "#{variables.ReleaseVersion}"
      Type: PLAINTEXT                     # or SECRETS_MANAGER (Commands only)
  Commands:                               # 1-50 single-line commands
    - "echo $RELEASE_VERSION"
    - "export BUILD_TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)"
  OutputVariables:                        # export shell env vars -> #{BuildVariables.BUILD_TIMESTAMP}
    - BUILD_TIMESTAMP
  InputArtifacts:                         # 1-10 required
    - Name: SourceArtifact
  OutputArtifacts:                        # 0-1
    - Name: BuildArtifact
      Files: ["dist/**/*"]                # Files is used by the Commands action
```

Notes:
- `Commands`, `EnvironmentVariables`, `OutputVariables` and `OutputArtifacts[].Files` sit **on the action**, not under `Configuration`. Other actions don't work this way.
- Commands must be **single-line**. Multi-line YAML blocks are rejected. Chain steps with `&&`.
- **Quote every command that contains `#{...}`**. In YAML, an unquoted ` #` starts a comment.
- 55-minute timeout. Counts toward your CodeBuild concurrent-build quota.
- The pipeline **service role** runs the commands (there's no separate CodeBuild role). It needs `logs:CreateLogGroup/CreateLogStream/PutLogEvents` on `/aws/codepipeline/<pipeline-name>`, plus whatever AWS access your commands use.
- VPC access: set `VpcId`, `Subnets`, `SecurityGroupIds` in `Configuration`.

### 4. Stage retry and rollback — `OnFailure`

```yaml
# Retry once automatically, re-running only the failed actions (or ALL_ACTIONS)
OnFailure:
  Result: RETRY
  RetryConfiguration:
    RetryMode: FAILED_ACTIONS

# Re-run the stage using the artifacts of the last successful execution
OnFailure:
  Result: ROLLBACK
```

- Automatic retry makes **one** attempt only. It can't be combined with `OnFailure.Conditions`.
- Rollback needs a previous successful execution **in the current pipeline structure version**. Right after a pipeline update, there's nothing to roll back to yet.
- Rollback isn't available in PARALLEL mode.
- Manual retry from the CLI: `aws codepipeline retry-stage-execution --retry-mode FAILED_ACTIONS|ALL_ACTIONS ...`

### 5. Stage conditions — `BeforeEntry` / `OnFailure.Conditions` / `OnSuccess` *(next template)*

Gate a stage with **rules**: `CloudWatchAlarm`, `DeploymentWindow`, `LambdaInvoke`, `VariableCheck`, `Commands`, `CodeBuild`.
Possible results: `FAIL` or `SKIP` (entry), `ROLLBACK` (on failure), `FAIL` / `ROLLBACK` (on success).
For example, "skip Deploy outside business hours" or "roll back if this alarm fires within 10 minutes".
See [docs/codepipeline/ug-stage-conditions.md](../docs/codepipeline/ug-stage-conditions.md).

### 6. Triggers and filters — `Triggers`

Start the pipeline on Git **tags**, **branches**, **file paths** or **pull request** events (`OPEN`, `UPDATED`, `CLOSED`), with include/exclude globs.
In V1, a connection source can only start on "any push to the one `BranchName`".

```yaml
Triggers:
  - ProviderType: CodeStarSourceConnection
    GitConfiguration:
      SourceActionName: GitSource          # must match the source action's Name
      Push:                                # up to 3 push filters
        - Tags:     { Includes: ["v*"] }   # tags alone, never with Branches/FilePaths
        - Branches: { Includes: [main] }
          FilePaths: { Includes: ["**"], Excludes: ["*.md", "**/*.md", "docs/**"] }
      PullRequest:                         # up to 3 PR filters
        - Branches: { Includes: [main] }   # destination branch of the PR
          Events: [OPEN, UPDATED]
```

How filters combine:

| Level | Logic |
|---|---|
| Between filters (each `Push[]` / `PullRequest[]` entry) | **OR**: any match starts the pipeline |
| Inside one filter (`Branches` + `FilePaths`) | **AND**: both must match |
| Inside one criteria (`Includes` / `Excludes`) | **Excludes win** |
| File paths in one commit | Each file is checked separately. One included file is enough |

Valid push filters are `Tags`, `Branches`, or `Branches` + `FilePaths`. Valid PR filters are `Branches`, or `Branches` + `FilePaths`. Each criteria list holds up to 8 glob patterns ([docs/codepipeline/ug-syntax-glob.md](../docs/codepipeline/ug-syntax-glob.md)).

- Only for `CodeStarSourceConnection` sources (GitHub, GitLab, Bitbucket via CodeConnections).
- One trigger per source action.
- Once you define `Triggers`, the source action's default change detection is **turned off**. `BranchName` is then used only for manual starts.
- A push trigger runs the pushed (destination) branch's commit. A PR trigger runs the PR's **source**-branch commit.
- Merging a PR can start **two** executions if a `CLOSED` PR filter and a branch push filter both match.
- A `Branches` + `FilePaths` filter doesn't fire on the first push of a new branch, because there's no list of changed files yet.
- See [docs/codepipeline/ug-pipelines-triggers.md](../docs/codepipeline/ug-pipelines-triggers.md) (examples and considerations) and [docs/codepipeline/ug-pipelines-filter.md](../docs/codepipeline/ug-pipelines-filter.md).

### 7. Source revision override

Start a run on a specific commit instead of the head of `BranchName`:

```bash
aws codepipeline start-pipeline-execution --name <pipeline> \
  --source-revisions actionName=GitSource,revisionType=COMMIT_ID,revisionValue=<sha>
```

Revision types are `COMMIT_ID`, `IMAGE_DIGEST` (ECR), `S3_OBJECT_VERSION_ID` and `S3_OBJECT_KEY` (S3 needs `AllowOverrideForS3ObjectKey: true`). See [docs/codepipeline/ug-pipelines-trigger-source-overrides.md](../docs/codepipeline/ug-pipelines-trigger-source-overrides.md).

----------------------------------------------------------------------------------

## Templates

### CodePipeline V2 - Basic (S3 Source → Commands Build → Commands Release)

[codepipeline-v2-basic.yaml](codepipeline-v2-basic.yaml)

A small V2 pipeline that needs nothing set up in advance: **no Git connection, no CodeBuild project, no CodeDeploy**. Upload a zip and the pipeline runs.

```
 S3 source.zip ──(EventBridge Object Created)──► Pipeline (V2, QUEUED)
   Source  : S3                    namespace SourceVariables  → #{SourceVariables.VersionId}
   Build   : Commands              namespace BuildVariables   → exports BUILD_TIMESTAMP
             OnFailure RETRY (FAILED_ACTIONS)
   Release : Commands              uses #{BuildVariables.BUILD_TIMESTAMP}, #{variables.TargetEnvironment}
             OnFailure ROLLBACK
```

V2 features covered (marked `[V2]` in the template):
- `PipelineType: V2`, `ExecutionMode: QUEUED`
- Pipeline-level `Variables` (`ReleaseVersion`, `TargetEnvironment`)
- Commands action with `EnvironmentVariables`, `OutputVariables`, `OutputArtifacts[].Files`
- Passing an output variable from one stage to a later stage
- `OnFailure: RETRY` on Build and `OnFailure: ROLLBACK` on Release

Differences from the V1 basic template ([../codepipeline/code-codepipeline-basic.yaml](../codepipeline/code-codepipeline-basic.yaml)):

| V1 basic | V2 basic |
|---|---|
| CodeCommit source | S3 source with versioning and EventBridge notifications (no CloudTrail trail needed) |
| Separate CodeBuild/CodeDeploy roles and resources | Commands action. The pipeline role is the only compute role |
| No execution mode (SUPERSEDED) | QUEUED |
| No variables | Pipeline-level variables, plus action output variables between stages |
| Manual retry only | Automatic retry and rollback |

#### Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-pipeline-v2 \
  --template-body file://codepipeline-v2-basic.yaml \
  --capabilities CAPABILITY_IAM
```

The execution that starts at stack creation **fails at Source**, because `source.zip` doesn't exist yet. This is expected.

#### Run

```bash
BUCKET=$(aws cloudformation describe-stacks --stack-name myapp-dev-pipeline-v2 \
  --query "Stacks[0].Outputs[?OutputKey=='SourceBucketName'].OutputValue" --output text)

mkdir -p /tmp/src && echo "hello v2" > /tmp/src/index.html
(cd /tmp/src && zip -r ../source.zip .)        # PowerShell: Compress-Archive -Path src\* -DestinationPath source.zip
aws s3 cp /tmp/source.zip s3://$BUCKET/source.zip   # upload -> EventBridge starts the pipeline
```

Start manually with variable overrides (V2):

```bash
aws codepipeline start-pipeline-execution --name myapp-dev-pipeline \
  --variables name=ReleaseVersion,value=v2-0-1 name=TargetEnvironment,value=stg
```

Check the resolved variables and the exported output variable:

```bash
aws codepipeline list-action-executions --pipeline-name myapp-dev-pipeline \
  --query "actionExecutionDetails[].{action:actionName,status:status,vars:output.outputVariables}"
```

Commands logs: CloudWatch log group `/aws/codepipeline/myapp-dev-pipeline`.

#### Try the V2 failure handling

- **Retry:** add a failing command such as `"exit 1"` to `BuildCommands` and update the stack. Build fails, retries once automatically, then fails.
- **Rollback:** first get one fully successful run. Then make `ReleaseCommands` fail and upload a new zip. Release fails, and CodePipeline starts a rollback execution of Release using the last successful artifacts.

#### Delete

Empty both buckets first. The source bucket is versioned, so delete all versions:

```bash
aws s3api delete-objects --bucket $BUCKET --delete "$(aws s3api list-object-versions --bucket $BUCKET \
  --query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}' --output json)"
aws s3 rm s3://<artifact-bucket> --recursive
aws cloudformation delete-stack --stack-name myapp-dev-pipeline-v2
```

### CodePipeline V2 - GitHub Triggers (tags / branch + paths / pull requests)

[codepipeline-v2-github-triggers.yaml](codepipeline-v2-github-triggers.yaml)

A GitHub (or GitLab / Bitbucket) source through CodeConnections. The pipeline starts **only** on filtered Git events:

```
 GitHub ──(CodeConnections webhook)──► Trigger on GitSource   (filters OR'ed)
   1. push tag            v*                                  e.g. git push origin v1.2.0
   2. push branch         main  AND  any file not in *.md, **/*.md, docs/**
   3. pull request        into main, OPEN | UPDATED
 Pipeline (V2, PARALLEL)
   Source : CodeStarSourceConnection   namespace SourceVariables → BranchName, CommitId, ...
   Build  : Commands                   prints branch/commit, runs ci.sh if the repo has one
```

V2 features covered (marked `[V2]` in the template):
- `Triggers` with a tag push filter, a branch + file path push filter, and a pull request filter
- `ExecutionMode: PARALLEL`. Runs for different PRs and branches don't queue or supersede each other.
- Source revision override (see below)

Parameters you'll normally set: `ConnectionArn`, `FullRepositoryId`. The trigger patterns are `CommaDelimitedList` parameters (`TriggerTagIncludeList`, `TriggerBranchIncludeList`, `TriggerFilePathExcludeList`), so you can change them without editing the template.

Differences from a V1 GitHub pipeline (for example [../codepipeline/code-codepipeline-github-ecs.yaml](../codepipeline/code-codepipeline-github-ecs.yaml)):

| V1 | V2 triggers |
|---|---|
| Starts on any push to the one `BranchName` | Starts on tag / branch / path / PR filters. `BranchName` is only for manual starts |
| Docs-only commits still start a full run | Excluded file paths alone don't start a run |
| No PR builds | PR OPEN / UPDATED builds the PR's source branch |
| SUPERSEDED: a newer commit replaces a waiting run | PARALLEL: each PR and branch gets its own run |

#### Pre-requisite: an AVAILABLE connection

A connection created from the CLI or CloudFormation starts as `PENDING`. It must be completed once in the console (installing the AWS Connector GitHub App). A `PENDING` connection never triggers the pipeline.

```bash
aws codeconnections create-connection --provider-type GitHub --connection-name myapp-github
# Console: Developer Tools > Settings > Connections > myapp-github > Update pending connection
aws codeconnections get-connection --connection-arn <arn> --query Connection.ConnectionStatus   # AVAILABLE
```

You need to be the repository owner, or the organization owner if the repository is in an organization.

#### Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-github-pipeline \
  --template-body file://codepipeline-v2-github-triggers.yaml \
  --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=ConnectionArn,ParameterValue=<connection-arn> \
               ParameterKey=FullRepositoryId,ParameterValue=<owner>/<repo>
```

Creating the stack starts one run on `SourceBranchName` (main).

#### Try each trigger

```bash
git commit --allow-empty -m "docs only?" && git push          # no changed files -> no run
echo "x" >> README.md && git commit -am "docs" && git push    # only *.md changed -> no run
echo "echo running ci" > ci.sh && git add ci.sh && git commit -m "ci" && git push   # -> run (branch filter)
git tag v1.0.0 && git push origin v1.0.0                      # -> run (tag filter)
git switch -c feature/x && echo 1 > a.txt && git add a.txt && git commit -m f && git push -u origin feature/x
gh pr create --base main --fill                               # -> run on feature/x commit (PR OPEN)
git commit --allow-empty -m "update" && git push              # -> run (PR UPDATED)
```

See which trigger started each run:

```bash
aws codepipeline list-pipeline-executions --pipeline-name myapp-dev-github-pipeline \
  --query "pipelineExecutionSummaries[].{id:pipelineExecutionId,status:status,trigger:trigger.triggerType,detail:trigger.triggerDetail,rev:sourceRevisions[0].revisionId}"
```

Rebuild a specific commit (source revision override):

```bash
aws codepipeline start-pipeline-execution --name myapp-dev-github-pipeline \
  --source-revisions actionName=GitSource,revisionType=COMMIT_ID,revisionValue=<sha>
```

#### Delete

```bash
aws s3 rm s3://<artifact-bucket> --recursive
aws cloudformation delete-stack --stack-name myapp-dev-github-pipeline
```

The connection isn't part of the stack, so it remains.

----------------------------------------------------------------------------------

## Migrating a V1 template to V2

1. Add `PipelineType: V2`. The pipeline updates in place, keeping its name and history.
2. Optionally set `ExecutionMode: QUEUED` (or `PARALLEL`, which can't be used with rollback).
3. Add `Variables` and use `#{variables.X}` in action configuration. Don't use them in Source actions.
4. Replace small CodeBuild projects with the Commands action, and add the `/aws/codepipeline/<name>` logs permission to the pipeline role.
5. Add `OnFailure` (RETRY or ROLLBACK) to deploy stages.
6. For GitHub sources, add `Triggers` with tag, branch or path filters. Remember that this turns off default change detection.

----------------------------------------------------------------------------------

## Errors

##### cfn-lint: `Invalid Property ... ExecutionMode / Commands / OnFailure`, `Category (Compute)` not valid

Your cfn-lint is older than these V2 properties (seen with 0.85.x). Upgrade to cfn-lint v1. cfn-lint 1.26.1 still flags `EnvironmentVariables` on actions until you refresh its schemas with `cfn-lint --update-specs`. Both templates lint clean after that.

##### Pipeline doesn't start on push / tag / PR

- The connection is `PENDING`. Complete it in the console (see the GitHub Triggers pre-requisite).
- The push matched no filter. Remember that defining `Triggers` turns off "any push to `BranchName`".
- The commit changed only excluded paths, or it was the first push of a new branch (file path filters can't be evaluated yet).
- `SourceActionName` in the trigger doesn't match the source action's `Name`.
- The Region doesn't support connection triggers (see [docs/codepipeline/ug-action-reference-CodestarConnectionSource.md](../docs/codepipeline/ug-action-reference-CodestarConnectionSource.md)).

##### Insufficient permissions: Unable to use Connection

Grant **both** `codeconnections:UseConnection` and `codestar-connections:UseConnection` on the connection ARN. Which one is checked depends on the code path, not on the ARN prefix.

##### Source: Upload to S3 failed / `CODEBUILD_CLONE_REF` with a Commands action

`CODEBUILD_CLONE_REF` (full clone) only works with downstream **CodeBuild** actions. Use `CODE_ZIP` with the Commands action.

##### Commands action: multi-line command rejected

Each item in `Commands` must be one line. Join steps with `&&`, or add more list items.

##### Variable reference shows up literally or the action config looks truncated

An unquoted `#{...}` in YAML is read as a comment from ` #` onward. Wrap the whole value in double quotes.

##### Rollback not available / not triggered

Rollback needs a previous successful execution in the **current pipeline structure version**. It isn't supported with `ExecutionMode: PARALLEL`.

----------------------------------------------------------------------------------

## Roadmap (next V2 templates)

- `codepipeline-v2-stage-conditions.yaml`: `BeforeEntry` DeploymentWindow / CloudWatchAlarm, `OnSuccess` rollback
- ~~`codepipeline-v2-github-triggers.yaml`~~: done. It also covers PARALLEL mode for PR / feature-branch runs.

## Resources

- https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-pipeline.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Commands.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-variables.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-filter.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-triggers.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-overrides.html
