> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable TargetTrackingScalingPolicyConfiguration

Defines a target tracking scaling policy.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "DisableScaleIn" : Boolean,
  "ScaleInCooldown" : Integer,
  "ScaleOutCooldown" : Integer,
  "TargetValue" : Number
}

```

### YAML

```
  DisableScaleIn: Boolean
  ScaleInCooldown: Integer
  ScaleOutCooldown: Integer
  TargetValue: Number

```

## Properties

**`DisableScaleIn`** 

Indicates whether scale in by the target tracking scaling policy is disabled. The default value is `false`. 

Required: No

Type: Boolean

Update requires: No interruption

**`ScaleInCooldown`** 

The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. 

Required: No

Type: Integer

Minimum: `0`

Update requires: No interruption

**`ScaleOutCooldown`** 

The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start. 

Required: No

Type: Integer

Minimum: `0`

Update requires: No interruption

**`TargetValue`** 

Defines a target value for the scaling policy. 

Required: Yes

Type: Number

Update requires: No interruption
