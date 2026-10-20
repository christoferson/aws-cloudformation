> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-memorygibpervcpurequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider MemoryGiBPerVCpuRequest

The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Max" : Number,
  "Min" : Number
}

```

### YAML

```
  Max: Number
  Min: Number

```

## Properties

**`Max`** 

The maximum amount of memory per vCPU in GiB. Instance types with a higher memory-to-vCPU ratio are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption

**`Min`** 

The minimum amount of memory per vCPU in GiB. Instance types with a lower memory-to-vCPU ratio are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption
