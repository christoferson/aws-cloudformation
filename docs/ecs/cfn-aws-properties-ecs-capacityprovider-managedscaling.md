> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedscaling.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider ManagedScaling

The managed scaling settings for the Auto Scaling group capacity provider.

When managed scaling is turned on, Amazon ECS manages the scale-in and scale-out actions of the Auto Scaling group. Amazon ECS manages a target tracking scaling policy using an Amazon ECS managed CloudWatch metric with the specified `targetCapacity` value as the target value for the metric. For more information, see Using managed scaling in the Amazon Elastic Container Service Developer Guide.

If managed scaling is off, the user must manage the scaling of the Auto Scaling group.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "InstanceWarmupPeriod" : Integer,
  "MaximumScalingStepSize" : Integer,
  "MinimumScalingStepSize" : Integer,
  "Status" : String,
  "TargetCapacity" : Integer
}

```

### YAML

```
  InstanceWarmupPeriod: Integer
  MaximumScalingStepSize: Integer
  MinimumScalingStepSize: Integer
  Status: String
  TargetCapacity: Integer

```

## Properties

**`InstanceWarmupPeriod`** 

The period of time, in seconds, after a newly launched Amazon EC2 instance can contribute to CloudWatch metrics for Auto Scaling group. If this parameter is omitted, the default value of `300` seconds is used. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `10000`

Update requires: No interruption

**`MaximumScalingStepSize`** 

The maximum number of Amazon EC2 instances that Amazon ECS will scale out at one time. If this parameter is omitted, the default value of `10000` is used. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `10000`

Update requires: No interruption

**`MinimumScalingStepSize`** 

The minimum number of Amazon EC2 instances that Amazon ECS will scale out at one time. The scale in process is not affected by this parameter If this parameter is omitted, the default value of `1` is used. 

When additional capacity is required, Amazon ECS will scale up the minimum scaling step size even if the actual demand is less than the minimum scaling step size. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `10000`

Update requires: No interruption

**`Status`** 

Determines whether to use managed scaling for the capacity provider. 

Required: No

Type: String

Allowed values: `DISABLED | ENABLED`

Update requires: No interruption

**`TargetCapacity`** 

The target capacity utilization as a percentage for the capacity provider. The specified value must be greater than `0` and less than or equal to `100`. For example, if you want the capacity provider to maintain 10% spare capacity, then that means the utilization is 90%, so use a `targetCapacity` of `90`. The default value of `100` percent results in the Amazon EC2 instances in your Auto Scaling group being completely used. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `100`

Update requires: No interruption
