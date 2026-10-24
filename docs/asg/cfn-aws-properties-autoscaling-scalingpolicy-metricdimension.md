> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-metricdimension.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy MetricDimension

`MetricDimension` specifies a name/value pair that is part of the identity of a CloudWatch metric for the `Dimensions` property of the AWS::AutoScaling::ScalingPolicy CustomizedMetricSpecification property type. Duplicate dimensions are not allowed. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "Value" : String
}

```

### YAML

```
  Name: String
  Value: String

```

## Properties

**`Name`** 

The name of the dimension. 

Required: Yes

Type: String

Update requires: No interruption

**`Value`** 

The value of the dimension. 

Required: Yes

Type: String

Update requires: No interruption
