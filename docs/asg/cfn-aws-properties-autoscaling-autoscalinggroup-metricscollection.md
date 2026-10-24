> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-metricscollection.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::AutoScalingGroup MetricsCollection

`MetricsCollection` is a property of the AWS::AutoScaling::AutoScalingGroup resource that describes the group metrics that an Amazon EC2 Auto Scaling group sends to Amazon CloudWatch. These metrics describe the group rather than any of its instances. 

For more information, see Monitor CloudWatch metrics for your Auto Scaling groups and instances in the Amazon EC2 Auto Scaling User Guide. You can find a sample template snippet in the Examples section of the `AWS::AutoScaling::AutoScalingGroup` resource.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Granularity" : String,
  "Metrics" : [ String, ... ]
}

```

### YAML

```
  Granularity: String
  Metrics: 
    - String

```

## Properties

**`Granularity`** 

The frequency at which Amazon EC2 Auto Scaling sends aggregated data to CloudWatch. The only valid value is `1Minute`. 

Required: Yes

Type: String

Update requires: No interruption

**`Metrics`** 

Identifies the metrics to enable. 

You can specify one or more of the following metrics:  
 `GroupMinSize`  
 `GroupMaxSize`  
 `GroupDesiredCapacity`  
 `GroupInServiceInstances`  
 `GroupPendingInstances`  
 `GroupStandbyInstances`  
 `GroupTerminatingInstances`  
 `GroupTotalInstances`  
 `GroupInServiceCapacity`  
 `GroupPendingCapacity`  
 `GroupStandbyCapacity`  
 `GroupTerminatingCapacity`  
 `GroupTotalCapacity`  
 `WarmPoolDesiredCapacity`  
 `WarmPoolWarmedCapacity`  
 `WarmPoolPendingCapacity`  
 `WarmPoolTerminatingCapacity`  
 `WarmPoolTotalCapacity`  
 `GroupAndWarmPoolDesiredCapacity`  
 `GroupAndWarmPoolTotalCapacity`  
 

If you specify `Granularity` and don't specify any metrics, all metrics are enabled. 

For more information, see Amazon CloudWatch metrics for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Array of String

Update requires: No interruption
