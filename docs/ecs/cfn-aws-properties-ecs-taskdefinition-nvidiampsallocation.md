> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-nvidiampsallocation.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition NvidiaMpsAllocation

The `NvidiaMpsAllocation` property type specifies Property description not available. for an AWS::ECS::TaskDefinition.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MaxComputePercent" : Integer,
  "Memory" : Integer
}

```

### YAML

```
  MaxComputePercent: Integer
  Memory: Integer

```

## Properties

**`MaxComputePercent`**

Property description not available.

Required: No

Type: Integer

Minimum: `1`

Maximum: `100`

Update requires: Replacement

**`Memory`**

Property description not available.

Required: Yes

Type: Integer

Minimum: `1`

Update requires: Replacement
