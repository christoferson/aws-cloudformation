> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitconfiguration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline GitConfiguration

A type of trigger configuration for Git-based source actions.Note

You can specify the Git configuration trigger type for all third-party Git-based source actions that are supported by the `CodeStarSourceConnection` action type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "PullRequest" : [ GitPullRequestFilter, ... ],
  "Push" : [ GitPushFilter, ... ],
  "SourceActionName" : String
}

```

### YAML

```
  PullRequest: 
    - GitPullRequestFilter
  Push: 
    - GitPushFilter
  SourceActionName: String

```

## Properties

**`PullRequest`**
 

The field where the repository event that will start the pipeline is specified as pull requests. 

Required: No

Type: Array of GitPullRequestFilter

Minimum: `1`

Maximum: `3`

Update requires: No interruption

**`Push`**
 

The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details. 

Required: No

Type: Array of GitPushFilter

Minimum: `1`

Maximum: `3`

Update requires: No interruption

**`SourceActionName`**
 

The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only. Note

You can only specify one trigger configuration per source action. 

Required: Yes

Type: String

Pattern: `[A-Za-z0-9.@\-_]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

