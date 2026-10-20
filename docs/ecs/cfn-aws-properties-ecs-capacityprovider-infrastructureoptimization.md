> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-infrastructureoptimization.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider InfrastructureOptimization

The configuration that controls how Amazon ECS optimizes your infrastructure.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ScaleInAfter" : Integer
}

```

### YAML

```
  ScaleInAfter: Integer

```

## Properties

**`ScaleInAfter`** 

This parameter defines the number of seconds Amazon ECS Managed Instances waits before optimizing EC2 instances that have become idle or underutilized. A longer delay increases the likelihood of placing new tasks on idle or underutilized instances instances, reducing startup time. A shorter delay helps reduce infrastructure costs by optimizing idle or underutilized instances,instances more quickly. 

Valid values are:  
`null` - Uses the default optimization behavior. 
`-1` - Disables automatic infrastructure optimization. 
A value between `0` and `3600` (inclusive) - Specifies the number of seconds to wait before optimizing instances. 
 

Required: No

Type: Integer

Minimum: `-1`

Maximum: `3600`

Update requires: No interruption
