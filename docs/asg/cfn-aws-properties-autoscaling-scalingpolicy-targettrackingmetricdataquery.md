> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy TargetTrackingMetricDataQuery

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

You can use `TargetTrackingMetricDataQuery` structures with a PutScalingPolicy operation when you specify a TargetTrackingConfiguration in the request.

You can call for a single metric or perform math expressions on multiple metrics. Any expressions used in a metric specification must eventually return a single time series.

For more information, see the Create a target tracking scaling policy for Amazon EC2 Auto Scaling using metric math in the Amazon EC2 Auto Scaling User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Expression" : String,
  "Id" : String,
  "Label" : String,
  "MetricStat" : TargetTrackingMetricStat,
  "Period" : Integer,
  "ReturnData" : Boolean
}

```

### YAML

```
  Expression: String
  Id: String
  Label: String
  MetricStat: 
    TargetTrackingMetricStat
  Period: Integer
  ReturnData: Boolean

```

## Properties

**`Expression`** 

The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.  

Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both. 

Required: No

Type: String

Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

Minimum: `1`

Maximum: `2047`

Update requires: No interruption

**`Id`** 

A short name that identifies the object's results in the response. This name must be unique among all `TargetTrackingMetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.  

Required: Yes

Type: String

Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

Minimum: `1`

Maximum: `64`

Update requires: No interruption

**`Label`** 

A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents. 

Required: No

Type: String

Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

Maximum: `2047`

Update requires: No interruption

**`MetricStat`** 

Information about the metric data to return. 

Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both. 

Required: No

Type: TargetTrackingMetricStat

Update requires: No interruption

**`Period`** 

 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see Create a target tracking policy using high-resolution metrics for faster response.  

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`ReturnData`** 

Indicates whether to return the timestamps and raw data values of this metric.  

If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification. 

If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData`. This sets it to its default (`true`). 

Required: No

Type: Boolean

Update requires: No interruption
