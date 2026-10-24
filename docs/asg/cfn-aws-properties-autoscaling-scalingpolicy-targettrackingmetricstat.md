> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-targettrackingmetricstat.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy TargetTrackingMetricStat

This structure defines the CloudWatch metric to return, along with the statistic and unit.

`TargetTrackingMetricStat` is a property of the TargetTrackingMetricDataQuery object.

For more information about the CloudWatch terminology below, see Amazon CloudWatch concepts in the Amazon CloudWatch User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Metric" : Metric,
  "Period" : Integer,
  "Stat" : String,
  "Unit" : String
}

```

### YAML

```
  Metric: 
    Metric
  Period: Integer
  Stat: String
  Unit: String

```

## Properties

**`Metric`** 

The metric to use. 

Required: Yes

Type: Metric

Update requires: No interruption

**`Period`** 

 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see Create a target tracking policy using high-resolution metrics for faster response.  

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`Stat`** 

The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in Statistics in the Amazon CloudWatch User Guide. 

The most commonly used metric for scaling is `Average`. 

Required: Yes

Type: String

Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

**`Unit`** 

The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the MetricDatum data type in the Amazon CloudWatch API Reference. 

Required: No

Type: String

Update requires: No interruption
