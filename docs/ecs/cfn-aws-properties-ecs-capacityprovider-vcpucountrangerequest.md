> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-vcpucountrangerequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider VCpuCountRangeRequest

The minimum and maximum number of vCPUs for instance type selection. This allows you to specify a range of vCPU counts that meet your workload requirements.

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

The maximum number of vCPUs. Instance types with more vCPUs than this value are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum number of vCPUs. Instance types with fewer vCPUs than this value are excluded from selection. 

Required: Yes

Type: Integer

Update requires: No interruption
