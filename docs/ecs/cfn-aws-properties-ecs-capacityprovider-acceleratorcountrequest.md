> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-acceleratorcountrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider AcceleratorCountRequest

The minimum and maximum number of accelerators (such as GPUs) for instance type selection. This is used for workloads that require specific numbers of accelerators.

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

The maximum number of accelerators. Instance types with more accelerators are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum number of accelerators. Instance types with fewer accelerators are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption
