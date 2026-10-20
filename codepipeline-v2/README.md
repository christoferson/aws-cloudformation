
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
| **Invoke another pipeline** (pass revisions + variables) | – | **Yes** | `ActionTypeId: { Category: Invoke, Provider: CodePipeline }` |
| **New action types**: ECRBuildAndPublish, EC2 deploy, Lambda deploy, EKS deploy | – | **Yes** | See "Other V2-only actions" below |

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

### 5. Stage conditions — `BeforeEntry` / `OnFailure.Conditions` / `OnSuccess`

A **condition** attaches **rules** to a stage at one of three points. If any rule in the condition fails, the configured **result** is applied.

| Point | CloudFormation | Runs | Results |
|---|---|---|---|
| Entry | `BeforeEntry` | Before the stage starts | `FAIL`, `SKIP` (`SKIP` only with `LambdaInvoke` / `VariableCheck` rules) |
| On Success | `OnSuccess` | After all actions succeeded | `ROLLBACK`, `FAIL` |
| On Failure | `OnFailure.Conditions` | After the stage failed | `ROLLBACK` (can't be combined with automatic `RETRY`) |

Rules: `CloudWatchAlarm`, `DeploymentWindow`, `LambdaInvoke`, `VariableCheck`, `Commands`, `CodeBuild` (references in `docs/codepipeline/ug-rule-reference-*.md`).
A condition holds up to 5 rules, and each `BeforeEntry` / `OnSuccess` / `OnFailure` takes one condition.

**Stage rollback** re-runs the stage with the **artifacts and variables of the last execution that succeeded in that stage**, as a new execution of type **"rollback"**. Limits:
- That execution must be in the **current pipeline structure version**, so there's nothing to roll back to on the first run or right after a pipeline update.
- You can't roll back to an execution that was itself a rollback.
- Rollback isn't available in `PARALLEL` mode.

#### Use case: "the deployment succeeded" is not "the release is healthy"

> *After each production deployment, if the error-rate alarm fires, automatically return production to the previous version.*
>
> Answer: an **On Success** condition on the deploy stage, with a **`CloudWatchAlarm`** rule and result **`ROLLBACK`**.

The deploy action can succeed while users see errors. So the pipeline checks health **after** the stage and undoes the release without a human. The `CloudWatchAlarm` rule checks the alarm you name, and an alarm in `ALARM` makes the rule fail.

```yaml
- Name: Deploy
  Actions: [ ... ECS deploy ... ]
  OnSuccess:
    Conditions:
      - Result: ROLLBACK
        Rules:
          - Name: ErrorRateAlarm
            RuleTypeId: { Category: Rule, Owner: AWS, Provider: CloudWatchAlarm, Version: "1" }
            Configuration:
              AlarmName: myapp-dev-target-5xx
              WaitTime: "1"            # minutes to let an alarm already in ALARM recover
```

> **Timing gotcha.** The console guide says that if the alarm is **OK when the rule is first checked, the rule succeeds immediately**, and `WaitTime` only applies when it's already in ALARM. Elsewhere, the same guide describes a 60-minute wait as watching for ALARM within 60 minutes. The two statements conflict. Right after a deploy, the alarm usually hasn't seen the new version's errors yet. So the alarm-rollback and all-features templates add a **bake** step (a Commands action that waits N minutes after the ECS deploy) before the On Success check runs. See [docs/codepipeline/ug-rule-reference-cloudwatch-alarm.md](../docs/codepipeline/ug-rule-reference-cloudwatch-alarm.md) and [docs/codepipeline/ug-stage-conditions.md](../docs/codepipeline/ug-stage-conditions.md).

Implemented in [codepipeline-v2-feature-alarm-rollback.yaml](codepipeline-v2-feature-alarm-rollback.yaml) and the [Docker series](#codepipeline-v2---docker-series) all-features template.

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

### 8. Invoke another pipeline — `Category: Invoke`, `Provider: CodePipeline`

One pipeline starts another and hands it **source revisions** and **pipeline variables**.
This is the V2 way to chain "build once → deploy" or "service → shared release pipeline".
In V1 you needed a Lambda, EventBridge glue or a custom action, and the downstream pipeline would just fetch the branch head.

```yaml
- Name: InvokeDeployPipeline
  ActionTypeId: { Category: Invoke, Owner: AWS, Provider: CodePipeline, Version: "1" }
  Configuration:
    PipelineName: !Ref DeployPipeline          # the TARGET pipeline
    # JSON strings, not YAML lists
    SourceRevisions: '[{"actionName":"Source","revisionType":"COMMIT_ID","revisionValue":"#{SourceVariables.CommitId}"}]'
    Variables: '[{"name":"ReleaseVersion","value":"#{BuildVariables.RELEASE_VERSION}"}]'
```

- No input or output artifacts. Only the revision and the variables cross over; the target fetches its own source at the pinned revision.
- `SourceRevisions[].actionName` = the **target's** source action `Name`. `revisionType` is one of the four types in section 7.
- Every name in `Variables` must be **declared** in the target's `Variables`. Values must match `[A-Za-z0-9@\-_]+`, so no dots: use `20261018-ab12cd3`, not `1.2.3`.
- The invoking pipeline's role needs `codepipeline:StartPipelineExecution` on the target pipeline ARN.
- Both pipelines must be V2.

See [docs/codepipeline/ug-action-reference-pipeline-invoke.md](../docs/codepipeline/ug-action-reference-pipeline-invoke.md).

### Other V2-only actions (candidates for future templates)

| Action | Category / Provider | What it replaces |
|---|---|---|
| ECR build and publish | `Build` / `ECRBuildAndPublish` | CodeBuild project + buildspec that only runs `docker build && docker push`. **Builds a Dockerfile and pushes to ECR** using managed CodeBuild compute (billed as CodeBuild). The **repository must already exist** (`ECRRepositoryName`). Optional `DockerFilePath` (default: repo root), `ImageTags` (comma-delimited, default `latest`), `RegistryType` (`private` / `public`). **Output variables `ECRImageDigestId`** (`sha256` manifest digest) and `ECRRepositoryName`, for pinning the deploy to the exact image. One input artifact, no output artifact |
| EC2 deploy | `Deploy` / `EC2` | CodeDeploy agent + AppSpec. Deploys to instances selected by **tag** (`InstanceTagKey` / `InstanceTagValue`), using the **SSM agent** instead of the CodeDeploy agent. Linux only, up to 500 instances. `MaxBatch` / `MaxError` control rollout. With `TargetGroupNameList`, instances are deregistered during their deploy and re-registered after. Accepts an existing AppSpec as the deploy spec (unsupported fields ignored, `hooks` mapped best-effort) |
| Lambda deploy | `Deploy` / `Lambda` | CodeDeploy for Lambda. **Publishes a version and shifts alias traffic** with `DeployStrategy`: `AllAtOnce` (default), `Canary<N>Percent<M>Minutes` or `Linear<N>PercentEvery<M>Minute(s)`, maximum total wait 2 days. Shifting **requires `FunctionAlias`**, which must already point to a version (the rollback target). Without an alias it deploys to `$LATEST` and publishes a version. Up to **10 CloudWatch alarms**: the action fails if one goes to ALARM. Can also promote an existing version via `PublishedTargetVersion`. Output variable `FunctionVersion` |
| EKS deploy | `Deploy` / `EKS` | CodeBuild running `kubectl` / `helm`. Takes a manifest or Helm chart, works with public and private clusters |

Related managed-compute action (the docs **don't** mark it V2-only, but it pairs naturally with ECRBuildAndPublish):

| Action | Category / Provider | What it does |
|---|---|---|
| Inspector scan | `Invoke` / `InspectorScan` | **Scans source code or an ECR image** with Amazon Inspector. `InspectorRunMode`: `SourceCodeScan` (input artifact = source) or `ECRImageScan` (`ECRRepositoryName` + `ImageTag`, no input artifact). **Fails when findings exceed** `CriticalThreshold` / `HighThreshold` / `MediumThreshold` / `LowThreshold`. **Output artifact: an SBOM.** Output variable `HighestScannedSeverity` (`medium` / `high` / `critical`). Needs `inspector-scan:ScanSbom` (and ECR pull permissions for image scans). Runs on managed CodeBuild compute |

Docs: [InspectorScan](../docs/codepipeline/ug-action-reference-inspector-scan.md), [ECRBuildAndPublish](../docs/codepipeline/ug-action-reference-ecr-build-and-publish.md), [EC2Deploy](../docs/codepipeline/ug-action-reference-ec2-deploy.md), [LambdaDeploy](../docs/codepipeline/ug-action-reference-lambda-deploy.md), [EKS](../docs/codepipeline/ug-action-reference-eks.md).

----------------------------------------------------------------------------------

## Templates

File names follow `codepipeline-v2-<group>-<topic>.yaml`:

| Group | Shows | Templates |
|---|---|---|
| `source-` | How to connect one source provider | `source-codecommit`, `source-s3`, `source-ecr`, `source-github` |
| `feature-` | One V2 feature | `feature-stage-retry-rollback`, `feature-pipeline-variables`, `feature-git-triggers`, `feature-invoke-pipeline`, `feature-inspector-scan`, `feature-deployment-window`, `feature-alarm-rollback` |
| `docker-` | Docker build → ECS, end to end | `docker-ecs-deploy`, `docker-all-features` |

### Source providers

Each `source-` template is the minimum: Source → one Commands step that prints that provider's output variables.

| Template | Provider (`ActionTypeId.Provider`) | Change detection | Pipeline role needs | Output variables |
|---|---|---|---|---|
| [codepipeline-v2-source-codecommit.yaml](codepipeline-v2-source-codecommit.yaml) | `CodeCommit` | EventBridge rule on `CodeCommit Repository State Change` + `PollForSourceChanges: false` | `codecommit:GetBranch`, `GetCommit`, `GetRepository`, `UploadArchive`, `GetUploadArchiveStatus`, `CancelUploadArchive` | `CommitId`, `BranchName`, `RepositoryName`, `CommitMessage`, `AuthorDate`, `CommitterDate` |
| [codepipeline-v2-source-s3.yaml](codepipeline-v2-source-s3.yaml) | `S3` | Bucket with EventBridge notifications + rule on `Object Created` (no CloudTrail trail) + `PollForSourceChanges: false` | `s3:GetObject`, `GetObjectVersion`, `GetBucketVersioning`, `GetBucketAcl`, `GetBucketLocation`, `GetObjectTagging`, `GetObjectVersionTagging` | `BucketName`, `ObjectKey`, `ETag`, `VersionId` |
| [codepipeline-v2-source-ecr.yaml](codepipeline-v2-source-ecr.yaml) | `ECR` | EventBridge rule on `ECR Image Action`, `PUSH`, `SUCCESS`, repository + tag (the action has no polling setting) | `ecr:DescribeImages` | `RegistryId`, `RepositoryName`, `ImageTag`, `ImageDigest`, `ImageURI` |
| [codepipeline-v2-source-github.yaml](codepipeline-v2-source-github.yaml) | `CodeStarSourceConnection` | The connection's GitHub App webhook (`DetectChanges: "true"`); no EventBridge rule | `codeconnections:UseConnection` + `codestar-connections:UseConnection` | `CommitId`, `BranchName`, `FullRepositoryName`, `CommitMessage`, `AuthorDate`, `ConnectionArn` |

Notes:
- **Source artifacts:** CodeCommit and GitHub output the commit as a zip (`CODE_ZIP`), S3 outputs the object itself, and ECR outputs `imageDetail.json` with the pushed image's URI.
- **ECR `ImageTag`:** this output variable isn't produced when the source revision is overridden (`IMAGE_DIGEST`). The ECR template doesn't use it.
- **S3 `AllowOverrideForS3ObjectKey: true`:** lets a manual run use another object key: `--source-revisions actionName=Source,revisionType=S3_OBJECT_KEY,revisionValue=<key>`. Omitted, it defaults to `false`.
- **GitHub:** the `GitHub` connection provider type covers GitHub.com and GitHub Enterprise Cloud. The connection must be `AVAILABLE`: one console handshake installs the AWS Connector app, and you must be the organization owner, or the repository owner outside an organization. See [Pre-requisite: an AVAILABLE connection](#pre-requisite-an-available-connection).
- **GitHub Enterprise Server and GitLab self-managed:** separate provider types (`GitHubEnterpriseServer`, `GitLabSelfManaged`) that also need a connections **host** (`HostArn`). They aren't covered here.

```bash
# CodeCommit
aws cloudformation create-stack --stack-name myapp-dev-source-codecommit \
  --template-body file://codepipeline-v2-source-codecommit.yaml --capabilities CAPABILITY_IAM
git clone codecommit::<region>://myapp-dev-source-codecommit   # push to main to start it

# S3
aws cloudformation create-stack --stack-name myapp-dev-source-s3 \
  --template-body file://codepipeline-v2-source-s3.yaml --capabilities CAPABILITY_IAM
aws s3 cp source.zip s3://<SourceBucketName>/source.zip

# ECR
aws cloudformation create-stack --stack-name myapp-dev-source-ecr \
  --template-body file://codepipeline-v2-source-ecr.yaml --capabilities CAPABILITY_IAM
aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
docker tag myimage <ContainerImageRepositoryUri>:latest && docker push <ContainerImageRepositoryUri>:latest

# GitHub (connection must already be AVAILABLE)
aws cloudformation create-stack --stack-name myapp-dev-source-github \
  --template-body file://codepipeline-v2-source-github.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=ConnectionArn,ParameterValue=<connection-arn> \
               ParameterKey=FullRepositoryId,ParameterValue=<owner>/<repo>
```

The CodeCommit, S3 and ECR stacks fail their first run at Source because nothing has been pushed or uploaded yet. This is expected.

### CodePipeline V2 - Basic (S3 Source → Commands Build → Commands Release)

[codepipeline-v2-feature-stage-retry-rollback.yaml](codepipeline-v2-feature-stage-retry-rollback.yaml)

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
  --template-body file://codepipeline-v2-feature-stage-retry-rollback.yaml \
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

[codepipeline-v2-feature-git-triggers.yaml](codepipeline-v2-feature-git-triggers.yaml)

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
  --template-body file://codepipeline-v2-feature-git-triggers.yaml \
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

### CodePipeline V2 - Invoke Pipeline (build → deploy, CodeCommit)

[codepipeline-v2-feature-invoke-pipeline.yaml](codepipeline-v2-feature-invoke-pipeline.yaml)

Two pipelines in one stack, chained with the invoke action. The deploy pipeline deploys **exactly the commit** the build pipeline built, along with the version the build produced.

```
 git push main ──(EventBridge)──► BUILD pipeline (V2, QUEUED)
   Source  : CodeCommit          namespace SourceVariables → CommitId
   Build   : Commands            exports RELEASE_VERSION = <utc timestamp>-<short sha>
   Release : Invoke (CodePipeline) ──────────────────────────────────────┐
               SourceRevisions  Source = COMMIT_ID #{SourceVariables.CommitId}
               Variables        ReleaseVersion, UpstreamExecutionId      │
                                                                         ▼
                                  DEPLOY pipeline (V2, QUEUED, no trigger of its own)
   Variables : ReleaseVersion (default "manual"), UpstreamExecutionId (default "none")
   Source    : CodeCommit  "Source"  ← pinned to the passed commit
   Deploy    : Commands    prints release + commit + upstream execution
```

V2 features covered (marked `[V2]` in the template):
- Invoke action (`Category: Invoke`, `Provider: CodePipeline`)
- Passing `SourceRevisions` (`COMMIT_ID`) and `Variables` to the target
- Target pipeline-level `Variables` with defaults for manual runs
- A Commands `OutputVariables` value (`RELEASE_VERSION`) feeding the invoke action
- `QUEUED` on deploy, so invoked releases deploy in order and none is superseded

Why pin the commit? If two pushes land close together, a deploy pipeline without the override would fetch the **branch head**. It could then deploy a commit the build pipeline never built or tested. The override makes "what was built" and "what is deployed" the same commit.

| V1 approach | V2 invoke action |
|---|---|
| Single long pipeline, or a Lambda / EventBridge glue step calling `StartPipelineExecution` | Built-in `Invoke` action, no code |
| Downstream fetches the branch head | Downstream pinned to the upstream `CommitId` |
| Data passed through artifacts or SSM parameters | `Variables` passed directly into the target's pipeline variables |

**Source.** CodeCommit, always created by the stack as `<Application>-<Environment>-invoke-demo` (`myapp-dev-invoke-demo`). The repository has `DeletionPolicy: Retain`, so deleting the stack keeps your code; delete it by hand before re-creating a stack with the same name. For GitHub, swap both source actions for `CodeStarSourceConnection`, as in the triggers template. The invoke action is the same.

#### Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-invoke-pipeline \
  --template-body file://codepipeline-v2-feature-invoke-pipeline.yaml \
  --capabilities CAPABILITY_IAM
```

Both pipelines run once at creation and **fail at Source**, because the new repository is empty. This is expected.

#### Run

```bash
pip install git-remote-codecommit                       # or use the HTTPS URL with Git credentials
git clone codecommit::<region>://myapp-dev-invoke-demo && cd myapp-dev-invoke-demo
git switch -c main
echo "hello invoke" > index.html && git add . && git commit -m "first" && git push -u origin main
# -> build pipeline starts -> Release stage invokes the deploy pipeline
```

Check that deploy received the same commit and the variables:

```bash
aws codepipeline list-pipeline-executions --pipeline-name myapp-dev-deploy-pipeline \
  --query "pipelineExecutionSummaries[0].{trigger:trigger,rev:sourceRevisions[0].revisionId}"
aws codepipeline get-pipeline-execution --pipeline-name myapp-dev-deploy-pipeline \
  --pipeline-execution-id <id> --query "pipelineExecution.variables"
```

The deploy pipeline's trigger should show the build pipeline as the starter, and `rev` should equal the build run's `CommitId`.

Run deploy manually, for example to redeploy an old commit with a label:

```bash
aws codepipeline start-pipeline-execution --name myapp-dev-deploy-pipeline \
  --source-revisions actionName=Source,revisionType=COMMIT_ID,revisionValue=<sha> \
  --variables name=ReleaseVersion,value=hotfix-1
```

#### Delete

```bash
aws s3 rm s3://<artifact-bucket> --recursive
aws cloudformation delete-stack --stack-name myapp-dev-invoke-pipeline
aws codecommit delete-repository --repository-name myapp-dev-invoke-demo   # only if you want the code gone
```

### CodePipeline V2 - Docker Series

Each template builds a Dockerfile with **`ECRBuildAndPublish`** (no CodeBuild project, no buildspec, no `docker login` / `docker push` script) from a CodeCommit repository the stack creates. Each one then showcases **one feature**. The all-features template combines them, and nothing is optional: no `!If` conditions.

| Template | Feature | Pipeline |
|---|---|---|
| [codepipeline-v2-docker-ecs-deploy.yaml](codepipeline-v2-docker-ecs-deploy.yaml) | ECS deploy, digest-pinned | Source → Build → Verify → Deploy |
| [codepipeline-v2-feature-inspector-scan.yaml](codepipeline-v2-feature-inspector-scan.yaml) | Inspector scan gate + SBOM | Source → Build → Scan |
| [codepipeline-v2-feature-alarm-rollback.yaml](codepipeline-v2-feature-alarm-rollback.yaml) | **[V2]** On Success alarm → ROLLBACK | Source → Build → Verify → Deploy + Bake |
| [codepipeline-v2-feature-deployment-window.yaml](codepipeline-v2-feature-deployment-window.yaml) | **[V2]** Entry DeploymentWindow → FAIL | Source → Build → Verify → Deploy |
| [codepipeline-v2-feature-pipeline-variables.yaml](codepipeline-v2-feature-pipeline-variables.yaml) | **[V2]** pipeline variables + Entry VariableCheck → SKIP | Source → Build → SmokeTest |
| [codepipeline-v2-docker-all-features.yaml](codepipeline-v2-docker-all-features.yaml) | All of the above + **[V2]** automatic retry | Source → Build → Scan → Verify → Deploy + Bake |

All-features pipeline:

```
 git push main ──(EventBridge)──► Pipeline (V2, QUEUED)
   Source : CodeCommit            namespace SourceVariables → CommitId
   Build  : ECRBuildAndPublish    tags #{variables.ImageTag} + <commit sha>
              outputs #{BuildVariables.ECRImageDigestId}, #{BuildVariables.ECRRepositoryName}
            OnFailure: RETRY (FAILED_ACTIONS, one attempt)
   Scan   : InspectorScan         ECRImageScan of <repo>:<commit sha>, thresholds, SBOM artifact
            Entry: VariableCheck #{variables.RunImageScan} EQ true, else SKIP
   Verify : Commands              imagedefinitions.json → [{"name":"<ContainerName>","imageUri":"<repo>@sha256:..."}]
   Deploy : ECS standard action   + Bake (Commands, DeployBakeTimeInMinutes)
            Entry: DeploymentWindow (cron), else FAIL
            On Success: CloudWatchAlarm in ALARM → ROLLBACK to the last good imagedefinitions.json
```

Each stack names its CodeCommit and ECR repositories `<Application>-<Environment>-<feature>`, so you can deploy several side by side. For example, `myapp-dev-ecs-deploy` and `myapp-dev-all-features`.

#### V2 feature coverage

Mapped to the V1 / V2 table in [../docs/codepipeline/pipeline-types-planning.md](../docs/codepipeline/pipeline-types-planning.md):

| V2 feature | Showcased in |
|---|---|
| QUEUED execution mode | all Docker-series templates, [feature-stage-retry-rollback](codepipeline-v2-feature-stage-retry-rollback.yaml), [feature-invoke-pipeline](codepipeline-v2-feature-invoke-pipeline.yaml) |
| PARALLEL execution mode | [feature-git-triggers](codepipeline-v2-feature-git-triggers.yaml) (can't be combined with ROLLBACK, so it's not in all-features) |
| Pipeline-level variables | [feature-pipeline-variables](codepipeline-v2-feature-pipeline-variables.yaml), all-features, basic, invoke |
| Rollback for pipeline stages | [feature-alarm-rollback](codepipeline-v2-feature-alarm-rollback.yaml) (On Success), all-features, basic (On Failure) |
| Stage conditions | alarm-rollback (On Success), [feature-deployment-window](codepipeline-v2-feature-deployment-window.yaml) (Entry), pipeline-variables (Entry), all-features |
| Entry conditions with Skip result | pipeline-variables (`RunSmokeTest`), all-features (`RunImageScan`) |
| Automatic retry on failure | all-features (Build), basic (Build) |
| Commands action | all |
| Source revision overrides | invoke (invoke action), plus `start-pipeline-execution --source-revisions` (section 7) |
| Triggers and Git filtering | github-triggers (needs a CodeConnections source) |

`ECRBuildAndPublish` is V2-only. The ECS deploy action and `InspectorScan` aren't marked V2-only in their action references.

#### V1 way vs V2 way

| Step | V1 (e.g. [../codepipeline/code-codepipeline-ecs.yaml](../codepipeline/code-codepipeline-ecs.yaml)) | V2 (Docker series) |
|---|---|---|
| Build resource | `AWS::CodeBuild::Project` + its own service role | Nothing. `ECRBuildAndPublish` runs as the pipeline role |
| Build script | `buildspec.yml` with `aws ecr get-login-password \| docker login`, `docker build`, `docker tag`, `docker push` | `ECRRepositoryName` (+ optional `ImageTags`) |
| Privileged mode | Must enable `PrivilegedMode: true` on the project for Docker | Handled by the action |
| Tag per commit | `IMAGE_TAG=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION \| cut -c1-7)` in the buildspec | `ImageTags: "latest,#{SourceVariables.CommitId}"` |
| Vulnerability gate | Extra CodeBuild step installing and running a scanner | `InspectorScan` action with severity thresholds + SBOM artifact |
| Image reference passed to deploy | `imagedefinitions.json` written by the buildspec, usually `:latest` | Output variable `ECRImageDigestId` → `repo@sha256:...` |
| Deploy gating / health | Manual approval, or custom Lambda | Entry `DeploymentWindow`, On Success `CloudWatchAlarm` → ROLLBACK |

#### Why pin by digest?

Tags are mutable, and `latest` moves on every build. A digest names exactly one image. Verify writes `repo@sha256:<digest>` into `imagedefinitions.json`, so the image that was built **and scanned** is the one ECS deploys, even if another build moves `latest` in between. It also makes rollback exact: re-running Deploy with the last good artifact redeploys the previous digest. You don't need a hand-maintained `imagedefinitions.json` in the repo, which is what the AWS console tutorial uses.

> The `imagedefinitions.json` reference only shows `repo:tag` examples. A digest URI is a valid image reference, but confirm it on your first deploy.

#### Inspector scan ([feature-inspector-scan](codepipeline-v2-feature-inspector-scan.yaml), all-features)

- **Setup:** the only documented account setup is the IAM permission `inspector-scan:ScanSbom`, which the templates add. There's no "activate Inspector" step. Scans are billed by Inspector, plus CodeBuild minutes for the managed compute.
- **Thresholds:** the action fails when the count at a severity is **above** its threshold, so `0` means "fail on any". The template defaults are Critical `0`, High `0`, Medium `10` and Low `50`. These are the templates' choice; AWS doesn't recommend values.
- **Scan by tag:** `ImageTag` takes a tag, not a digest, so the scan uses the `<commit sha>` tag that Build pushed. If you change `ImageTags`, keep the commit tag.
- **Output:** the SBOM is kept as `ImageSbomArtifact` in the artifact bucket (30-day lifecycle). The output variable `HighestScannedSeverity` is `medium`, `high` or `critical`.
- **Other mode:** `SourceCodeScan` scans the repository instead of the image. Use `InputArtifacts: SourceArtifact` and leave out `ECRRepositoryName` / `ImageTag`.

To see the gate fail, set `ImageScanLowThreshold=0`, or use an old base image such as `FROM public.ecr.aws/docker/library/python:3.8` (likely to have known HIGH findings), then push again.

Docs: [../docs/codepipeline/ug-action-reference-inspector-scan.md](../docs/codepipeline/ug-action-reference-inspector-scan.md), [../docs/codepipeline/inspector-configure-cicd-account.md](../docs/codepipeline/inspector-configure-cicd-account.md).

#### ECS deploy ([docker-ecs-deploy](codepipeline-v2-docker-ecs-deploy.yaml), and every template with a Deploy stage)

- **Required parameters:** `ContainerClusterName`, `ContainerServiceName`, `ContainerName`. The `ecs/` folder templates can create a cluster and service, for example [../ecs-managed-instance/](../ecs-managed-instance/) or the [blue/green example](../ecs/ecs-blue-green/README.md).
- **Container name:** the service's task definition must have a container named `ContainerName`. The action registers a new task definition revision with only that container's image replaced, then updates the service.
- **IAM:** the action reference's minimum: `ecs:RegisterTaskDefinition` / `ecs:DescribeTaskDefinition`, `ecs:UpdateService` / `ecs:DescribeServices` on that service, `ecs:TagResource` for new task definitions, and `iam:PassRole` for ECS. `PassRole` is on `*`, limited to `ecs` / `ecs-tasks`, so scope it to your task and execution role ARNs for production.

Docs: [../docs/codepipeline/ug-action-reference-ecs.md](../docs/codepipeline/ug-action-reference-ecs.md), [../docs/codepipeline/ug-file-reference.md](../docs/codepipeline/ug-file-reference.md).

#### Alarm rollback ([feature-alarm-rollback](codepipeline-v2-feature-alarm-rollback.yaml), all-features)

```
 Deploy stage
   1. DeployToContainerService   ECS: new task def revision with repo@sha256:<new> → service steady
   2. BakeAndWatchAlarm          wait DeployBakeTimeInMinutes, print alarm state each minute
 stage SUCCEEDED → On Success condition
   CloudWatchAlarm rule  AlarmName = DeployRollbackAlarmName
     OK / INSUFFICIENT_DATA → rule succeeds → release stays
     ALARM                  → (WaitTime) → rule fails → ROLLBACK
              new execution, type "rollback": re-runs Deploy with the last good
              execution's ImageDefinitionsArtifact → repo@sha256:<previous> → ECS
```

- **Bring your own alarm** (`DeployRollbackAlarmName`, required). A typical error-rate alarm for an ALB-backed service:

  ```bash
  # LoadBalancer dimension = the part of the ALB ARN after "loadbalancer/", e.g. app/myapp-dev-alb/0123456789abcdef
  aws cloudwatch put-metric-alarm --alarm-name myapp-dev-target-5xx \
    --namespace AWS/ApplicationELB --metric-name HTTPCode_Target_5XX_Count \
    --dimensions Name=LoadBalancer,Value=app/<alb-name>/<id> \
    --statistic Sum --period 60 --evaluation-periods 1 --threshold 5 \
    --comparison-operator GreaterThanOrEqualToThreshold --treat-missing-data notBreaching
  ```

- **Bake:** the rule passes immediately if the alarm is OK when first checked, so the bake (`DeployBakeTimeInMinutes`, 1–50) gives the alarm time to react. Keep the alarm period short (60s) and the bake at least one or two periods.
- **First deploy:** there's no earlier successful Deploy to roll back to. The same applies right after any pipeline update.
- **Mode:** rollback isn't available in `PARALLEL` mode, so these templates use `QUEUED`.
- **Permissions:** the rule runs as the pipeline role. `cloudwatch:DescribeAlarms` on that alarm is inferred, because the rule reference doesn't list permissions.
- **Compared with ECS-native blue/green:** [../ecs/ecs-blue-green/](../ecs/ecs-blue-green/README.md) does this inside ECS by shifting traffic back to blue. The pipeline approach works with any deploy action, but redeploys the previous version instead.

Try it: deploy a healthy image once, then push a change. During the bake, run `aws cloudwatch set-alarm-state --alarm-name myapp-dev-target-5xx --state-value ALARM --state-reason test`. Then look for the rollback execution:

```bash
aws codepipeline list-pipeline-executions --pipeline-name myapp-dev-alarm-rollback-pipeline \
  --query "pipelineExecutionSummaries[0:3].{id:pipelineExecutionId,type:executionType,status:status,rollback:rollbackMetadata}"
```

#### Deployment window ([feature-deployment-window](codepipeline-v2-feature-deployment-window.yaml), all-features)

```yaml
- Name: Deploy
  BeforeEntry:
    Conditions:
      - Result: FAIL
        Rules:
          - Name: BusinessHoursWindow
            RuleTypeId: { Category: Rule, Owner: AWS, Provider: DeploymentWindow, Version: "1" }
            Configuration:
              Cron: "0 0 9-17 ? * MON-FRI *"   # AWS example: 09:00-17:59 Mon-Fri
              TimeZone: UTC
```

- **What it does:** the rule succeeds when the current time matches the cron. Build and Verify run on every push. Outside the window, the Deploy stage isn't entered and the `FAIL` result is applied. The docs don't describe the rule waiting for the window, so release the change again (or retry the stage) inside the window.
- **Cron fields:** `Seconds Minutes Hours Day-of-month Month Day-of-week [Year]`. Use `?` in one of the two day fields.
- **TimeZone:** `Region/City` (`Europe/Berlin`), `UTC[+-HH:MM]`, or an abbreviation (`EST`). UTC is the default format.
- **Why FAIL and not SKIP:** Entry `SKIP` only works with the `LambdaInvoke` and `VariableCheck` rules.

Docs: [../docs/codepipeline/ug-rule-reference-deployment-window.md](../docs/codepipeline/ug-rule-reference-deployment-window.md).

#### Pipeline variables + SKIP ([feature-pipeline-variables](codepipeline-v2-feature-pipeline-variables.yaml), all-features)

- **`ImageTag`:** default from `ImageTagDefault`, used in `ImageTags: "#{variables.ImageTag},#{SourceVariables.CommitId}"`.
- **`RunSmokeTest`** (all-features: **`RunImageScan`**): an Entry condition with a `VariableCheck` rule (`EQ "true"`) and result **`SKIP`**. Any other value skips the stage: its status is Skipped and its actions show "Didn't Run". A skipped stage can't be retried or rolled back to, and a `SKIP` condition can't be overridden.
- **Value format:** values must match `[A-Za-z0-9@\-_]+`, so use `v1-2-0`, not `v1.2.0`. Pipeline variables can't be used in Source actions.

```bash
aws codepipeline start-pipeline-execution --name myapp-dev-pipeline-variables-pipeline \
  --variables name=ImageTag,value=v1-2-0 name=RunSmokeTest,value=false
```

Docs: [../docs/codepipeline/ug-rule-reference-variable-check.md](../docs/codepipeline/ug-rule-reference-variable-check.md), [../docs/codepipeline/ug-reference-variables.md](../docs/codepipeline/ug-reference-variables.md).

#### Deploy

```bash
# Build + scan only (no ECS needed)
aws cloudformation create-stack --stack-name myapp-dev-inspector-scan \
  --template-body file://codepipeline-v2-feature-inspector-scan.yaml --capabilities CAPABILITY_IAM

# Everything (needs an ECS service and an alarm)
aws cloudformation create-stack --stack-name myapp-dev-all-features \
  --template-body file://codepipeline-v2-docker-all-features.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=ContainerClusterName,ParameterValue=myapp-dev \
               ParameterKey=ContainerServiceName,ParameterValue=myapp-dev-service \
               ParameterKey=ContainerName,ParameterValue=myapp-dev-container \
               ParameterKey=DeployRollbackAlarmName,ParameterValue=myapp-dev-target-5xx
```

The first run fails at Source, because the repository is empty. This is expected.

#### Run

Push a Dockerfile to the repository root (sample from the AWS tutorial, [../docs/codepipeline/ug-tutorials-ecr-build-publish.md](../docs/codepipeline/ug-tutorials-ecr-build-publish.md)). Use the `CodeCommitCloneUrlGrc` stack output:

```bash
git clone codecommit::<region>://myapp-dev-all-features && cd myapp-dev-all-features && git switch -c main
cat > Dockerfile <<'EOF'
FROM public.ecr.aws/amazonlinux/amazonlinux:latest
RUN yum update -y && yum install -y httpd && echo 'Hello World!' > /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EOF
git add Dockerfile && git commit -m "Add Dockerfile" && git push -u origin main
```

Check the result:

```bash
aws ecr describe-images --repository-name myapp-dev-all-features \
  --query "sort_by(imageDetails,&imagePushedAt)[-1].{digest:imageDigest,tags:imageTags}"
aws codepipeline list-action-executions --pipeline-name myapp-dev-all-features-pipeline \
  --query "actionExecutionDetails[].{action:actionName,status:status,vars:output.outputVariables}"
```

Logs for each stack are in `/aws/codepipeline/<pipeline-name>`.

#### Delete

```bash
aws s3 rm s3://<artifact-bucket> --recursive
aws cloudformation delete-stack --stack-name myapp-dev-all-features    # ECR repo is emptied (EmptyOnDelete)
aws codecommit delete-repository --repository-name myapp-dev-all-features   # retained by the stack; delete to reuse the name
```

----------------------------------------------------------------------------------

## Migrating a V1 template to V2

1. Add `PipelineType: V2`. The pipeline updates in place, keeping its name and history.
2. Optionally set `ExecutionMode: QUEUED` (or `PARALLEL`, which can't be used with rollback).
3. Add `Variables` and use `#{variables.X}` in action configuration. Don't use them in Source actions.
4. Replace small CodeBuild projects with the Commands action, and add the `/aws/codepipeline/<name>` logs permission to the pipeline role.
5. Add `OnFailure` (RETRY or ROLLBACK) to deploy stages.
6. For GitHub sources, add `Triggers` with tag, branch or path filters. Remember that this turns off default change detection.
7. Replace Lambda or EventBridge "start the next pipeline" glue with the invoke action, and pin the commit with `SourceRevisions`.

----------------------------------------------------------------------------------

## Errors

##### cfn-lint: `Invalid Property ... ExecutionMode / Commands / OnFailure`, `Category (Compute)` not valid

Your cfn-lint is older than these V2 properties (seen with 0.85.x). Upgrade to cfn-lint v1. cfn-lint 1.26.1 still flags `EnvironmentVariables` on actions until you refresh its schemas with `cfn-lint --update-specs`. Both templates lint clean after that.

##### Pipeline doesn't start on push / tag / PR

- The connection is `PENDING`. Complete it in the console (see the GitHub Triggers pre-requisite).
- The push matched no filter. Remember that defining `Triggers` turns off "any push to `BranchName`".
- The commit changed only excluded paths, or it was the first push of a new branch (file path filters can't be evaluated yet).
- `SourceActionName` in the trigger doesn't match the source action's `Name`.
- The Region doesn't support connection triggers (see [docs/codepipeline/ug-action-reference-codestar-connection-source.md](../docs/codepipeline/ug-action-reference-codestar-connection-source.md)).

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

##### Invoke action fails, or the target starts without the commit or variables

- The invoking role lacks `codepipeline:StartPipelineExecution` on the **target** pipeline ARN.
- `SourceRevisions[].actionName` doesn't match the target's source action `Name` (this template uses `Source` in both).
- A passed variable isn't declared in the target's `Variables`, or its value has characters outside `[A-Za-z0-9@\-_]` (for example a dot in `1.2.3`).
- `SourceRevisions` or `Variables` was written as a YAML list. Both must be **JSON strings**.

##### CodeCommit push doesn't start the build pipeline

Check the EventBridge rule. It must match `referenceName` = your branch and `resources` = the repository ARN. Also keep `PollForSourceChanges: false`, or you'll get duplicate runs.

----------------------------------------------------------------------------------

## Roadmap (next V2 templates)

- `codepipeline-v2-lambda-deploy.yaml`: Lambda deploy action with traffic shifting and no CodeDeploy
- ~~`codepipeline-v2-feature-git-triggers.yaml`~~: done. It also covers PARALLEL mode for PR / feature-branch runs.
- ~~`codepipeline-v2-feature-invoke-pipeline.yaml`~~: done. Build pipeline invokes deploy pipeline with a pinned commit and variables.
- ~~Docker series~~: done. `codepipeline-v2-feature-*.yaml` + `codepipeline-v2-docker-*.yaml`: ECS deploy, Inspector scan, alarm rollback, deployment window, pipeline variables + SKIP, all-features.

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
- https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-PipelineInvoke.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeCommit.html
