> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-metric.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy Metric

Represents a specific metric. 

`Metric` is a property of the AWS::AutoScaling::ScalingPolicy MetricStat property type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Dimensions" : [ MetricDimension, ... ],
  "MetricName" : String,
  "Namespace" : String
}

```

### YAML

```
  Dimensions: 
    - MetricDimension
  MetricName: String
  Namespace: String

```

## Properties

**`Dimensions`** 

The dimensions for the metric. For the list of available dimensions, see the AWS documentation available from the table in AWS services that publish CloudWatch metrics  in the Amazon CloudWatch User Guide.  

Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy. 

Required: No

Type: Array of MetricDimension

Update requires: No interruption

**`MetricName`** 

The name of the metric. 

Required: Yes

Type: String

Update requires: No interruption

**`Namespace`** 

The namespace of the metric. For more information, see the table in AWS services that publish CloudWatch metrics  in the Amazon CloudWatch User Guide. 

Required: Yes

Type: String

Update requires: No interruption
