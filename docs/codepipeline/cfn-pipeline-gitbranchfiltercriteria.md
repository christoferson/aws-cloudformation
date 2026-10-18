> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitbranchfiltercriteria.html
> Downloaded: 2026-10-18

# AWS::CodePipeline::Pipeline GitBranchFilterCriteria

The Git repository branches specified as filter criteria to start the pipeline.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Excludes" : [ String, ... ],
  "Includes" : [ String, ... ]
}

```

### YAML

```
  Excludes: 
    - String
  Includes: 
    - String

```

## Properties

**`Excludes`** 

The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `8`

Update requires: No interruption

**`Includes`** 

The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `8`

Update requires: No interruption
