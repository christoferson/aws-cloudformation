> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-successconditions.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline SuccessConditions

The conditions for making checks that, if met, succeed a stage. For more information about conditions, see Stage conditions and How do stage conditions work?.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Conditions" : [ Condition, ... ]
}

```

### YAML

```
  Conditions: 
    - Condition

```

## Properties

**`Conditions`**
 

The conditions that are success conditions. 

Required: No

Type: Array of Condition

Minimum: `1`

Maximum: `1`

Update requires: No interruption

