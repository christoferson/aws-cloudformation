> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider BaselineEbsBandwidthMbpsRequest

The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps) for instance type selection. This is important for workloads with high storage I/O requirements.

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

The maximum baseline Amazon EBS bandwidth in Mbps. Instance types with higher Amazon EBS bandwidth are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum baseline Amazon EBS bandwidth in Mbps. Instance types with lower Amazon EBS bandwidth are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption
