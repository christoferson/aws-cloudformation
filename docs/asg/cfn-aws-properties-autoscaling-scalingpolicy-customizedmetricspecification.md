> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy CustomizedMetricSpecification

Contains customized metric specification information for a target tracking scaling policy for Amazon EC2 Auto Scaling.

To create your customized metric specification: 
Add values for each required property from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see Publish Custom Metrics in the Amazon CloudWatch User Guide. 
Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases. 

For more information about CloudWatch, see Amazon CloudWatch Concepts.

`CustomizedMetricSpecification` is a property of the AWS::AutoScaling::ScalingPolicy TargetTrackingConfiguration property type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Dimensions" : [ MetricDimension, ... ],
  "MetricName" : String,
  "Metrics" : [ TargetTrackingMetricDataQuery, ... ],
  "Namespace" : String,
  "Period" : Integer,
  "Statistic" : String,
  "Unit" : String
}

```

### YAML

```
  Dimensions: 
    - MetricDimension
  MetricName: String
  Metrics: 
    - TargetTrackingMetricDataQuery
  Namespace: String
  Period: Integer
  Statistic: String
  Unit: String

```

## Properties

**`Dimensions`** 

The dimensions of the metric. 

Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy. 

Required: No

Type: Array of MetricDimension

Update requires: No interruption

**`MetricName`** 

The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the Metric object that is returned by a call to ListMetrics. 

Required: No

Type: String

Update requires: No interruption

**`Metrics`** 

The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions. 

Required: No

Type: Array of TargetTrackingMetricDataQuery

Update requires: No interruption

**`Namespace`** 

The namespace of the metric. 

Required: No

Type: String

Update requires: No interruption

**`Period`** 

 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see Create a target tracking policy using high-resolution metrics for faster response.  

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`Statistic`** 

The statistic of the metric. 

Required: No

Type: String

Allowed values: `Average | Minimum | Maximum | SampleCount | Sum`

Update requires: No interruption

**`Unit`** 

The unit of the metric. For a complete list of the units that CloudWatch supports, see the MetricDatum data type in the Amazon CloudWatch API Reference. 

Required: No

Type: String

Update requires: No interruption
