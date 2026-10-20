> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider AcceleratorTotalMemoryMiBRequest

The minimum and maximum total accelerator memory in mebibytes (MiB) for instance type selection. This is important for GPU workloads that require specific amounts of video memory.

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

The maximum total accelerator memory in MiB. Instance types with more accelerator memory are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum total accelerator memory in MiB. Instance types with less accelerator memory are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption
