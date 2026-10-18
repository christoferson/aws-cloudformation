> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-retryconfiguration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline RetryConfiguration

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "RetryMode" : String
}

```

### YAML

```
  RetryMode: String

```

## Properties

**`RetryMode`**
 

The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage. 

Required: No

Type: String

Allowed values: `ALL_ACTIONS | FAILED_ACTIONS`

Update requires: No interruption

