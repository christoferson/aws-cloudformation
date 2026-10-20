> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-memorymibrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider MemoryMiBRequest

The minimum and maximum amount of memory in mebibytes (MiB) for instance type selection. This ensures that selected instance types have adequate memory for your workloads.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Max" : Integer,
  "Min" : Integer
}

```

### YAML

```
  Max: Integer
  Min: Integer

```

## Properties

**`Max`** 

The maximum amount of memory in MiB. Instance types with more memory than this value are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum amount of memory in MiB. Instance types with less memory than this value are excluded from selection. 

Required: Yes

Type: Integer

Update requires: No interruption
