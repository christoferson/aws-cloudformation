> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider AutoScalingGroupProvider

The details of the Auto Scaling group for the capacity provider.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AutoScalingGroupArn" : String,
  "ManagedDraining" : String,
  "ManagedScaling" : ManagedScaling,
  "ManagedTerminationProtection" : String
}

```

### YAML

```
  AutoScalingGroupArn: String
  ManagedDraining: String
  ManagedScaling: 
    ManagedScaling
  ManagedTerminationProtection: String

```

## Properties

**`AutoScalingGroupArn`** 

The Amazon Resource Name (ARN) that identifies the Auto Scaling group, or the Auto Scaling group name. 

Required: Yes

Type: String

Update requires: Replacement

**`ManagedDraining`** 

The managed draining option for the Auto Scaling group capacity provider. When you enable this, Amazon ECS manages and gracefully drains the EC2 container instances that are in the Auto Scaling group capacity provider. 

Required: No

Type: String

Allowed values: `DISABLED | ENABLED`

Update requires: No interruption

**`ManagedScaling`** 

The managed scaling settings for the Auto Scaling group capacity provider. 

Required: No

Type: ManagedScaling

Update requires: No interruption

**`ManagedTerminationProtection`** 

The managed termination protection setting to use for the Auto Scaling group capacity provider. This determines whether the Auto Scaling group has managed termination protection. The default is off. Important

When using managed termination protection, managed scaling must also be used otherwise managed termination protection doesn't work. 

When managed termination protection is on, Amazon ECS prevents the Amazon EC2 instances in an Auto Scaling group that contain tasks from being terminated during a scale-in action. The Auto Scaling group and each instance in the Auto Scaling group must have instance protection from scale-in actions on as well. For more information, see Instance Protection in the AWS Auto Scaling User Guide. 

When managed termination protection is off, your Amazon EC2 instances aren't protected from termination when the Auto Scaling group scales in. 

Required: No

Type: String

Allowed values: `DISABLED | ENABLED`

Update requires: No interruption

## See also 
  Defining an Amazon ECS capacity provider
