> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider NetworkBandwidthGbpsRequest

The minimum and maximum network bandwidth in gigabits per second (Gbps) for instance type selection. This is important for network-intensive workloads.

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

The maximum network bandwidth in Gbps. Instance types with higher network bandwidth are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption

**`Min`** 

The minimum network bandwidth in Gbps. Instance types with lower network bandwidth are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption
