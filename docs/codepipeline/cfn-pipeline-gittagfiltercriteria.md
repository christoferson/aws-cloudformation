> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gittagfiltercriteria.html
> Downloaded: 2026-10-18

# AWS::CodePipeline::Pipeline GitTagFilterCriteria

The Git tags specified as filter criteria for whether a Git tag repository event will start the pipeline.

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

The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `8`

Update requires: No interruption

**`Includes`** 

The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `8`

Update requires: No interruption
