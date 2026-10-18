> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-failureconditions.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline FailureConditions

The configuration that specifies the result, such as rollback, to occur upon stage failure. For more information about conditions, see Stage conditions and How do stage conditions work?.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Conditions" : [ Condition, ... ],
  "Result" : String,
  "RetryConfiguration" : RetryConfiguration
}

```

### YAML

```
  Conditions: 
    - Condition
  Result: String
  RetryConfiguration: 
    RetryConfiguration

```

## Properties

**`Conditions`**
 

The conditions that are configured as failure conditions. For more information about conditions, see Stage conditions and How do stage conditions work?. 

Required: No

Type: Array of Condition

Minimum: `1`

Maximum: `1`

Update requires: No interruption

**`Result`**
 

The specified result for when the failure conditions are met, such as rolling back the stage. 

Required: No

Type: String

Allowed values: `ROLLBACK | RETRY`

Update requires: No interruption

**`RetryConfiguration`**
 

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode. 

Required: No

Type: RetryConfiguration

Update requires: No interruption

