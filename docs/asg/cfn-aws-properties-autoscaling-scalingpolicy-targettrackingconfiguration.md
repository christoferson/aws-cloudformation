> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy TargetTrackingConfiguration

`TargetTrackingConfiguration` is a property of the AWS::AutoScaling::ScalingPolicy resource that specifies a target tracking scaling policy configuration for Amazon EC2 Auto Scaling. 

For more information about scaling policies, see Dynamic scaling in the Amazon EC2 Auto Scaling User Guide. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CustomizedMetricSpecification" : CustomizedMetricSpecification,
  "DisableScaleIn" : Boolean,
  "PredefinedMetricSpecification" : PredefinedMetricSpecification,
  "TargetValue" : Number
}

```

### YAML

```
  CustomizedMetricSpecification: 
    CustomizedMetricSpecification
  DisableScaleIn: Boolean
  PredefinedMetricSpecification: 
    PredefinedMetricSpecification
  TargetValue: Number

```

## Properties

**`CustomizedMetricSpecification`** 

A customized metric. You must specify either a predefined metric or a customized metric. 

Required: Conditional

Type: CustomizedMetricSpecification

Update requires: No interruption

**`DisableScaleIn`** 

Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is `false`. 

Required: No

Type: Boolean

Update requires: No interruption

**`PredefinedMetricSpecification`** 

A predefined metric. You must specify either a predefined metric or a customized metric. 

Required: Conditional

Type: PredefinedMetricSpecification

Update requires: No interruption

**`TargetValue`** 

The target value for the metric. Note

Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval.  

Required: Yes

Type: Number

Update requires: No interruption
