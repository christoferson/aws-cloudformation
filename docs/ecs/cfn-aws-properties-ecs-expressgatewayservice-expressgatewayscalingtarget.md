> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayScalingTarget

Defines the auto-scaling configuration for an Express service. This determines how the service automatically adjusts the number of running tasks based on demand metrics such as CPU utilization, memory utilization, or request count per target.

Auto-scaling helps ensure your application can handle varying levels of traffic while optimizing costs by scaling down during low-demand periods. You can specify the minimum and maximum number of tasks, the scaling metric, and the target value for that metric.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AutoScalingMetric" : String,
  "AutoScalingTargetValue" : Integer,
  "MaxTaskCount" : Integer,
  "MinTaskCount" : Integer
}

```

### YAML

```
  AutoScalingMetric: String
  AutoScalingTargetValue: Integer
  MaxTaskCount: Integer
  MinTaskCount: Integer

```

## Properties

**`AutoScalingMetric`** 

The metric used for auto-scaling decisions. The default metric used for an Express service is `CPUUtilization`. 

Required: No

Type: String

Allowed values: `AVERAGE_CPU | AVERAGE_MEMORY | REQUEST_COUNT_PER_TARGET`

Update requires: No interruption

**`AutoScalingTargetValue`** 

The target value for the auto-scaling metric. The default value for an Express service is 60. 

Required: No

Type: Integer

Update requires: No interruption

**`MaxTaskCount`** 

The maximum number of tasks to run in the Express service. 

Required: No

Type: Integer

Update requires: No interruption

**`MinTaskCount`** 

The minimum number of tasks to run in the Express service. 

Required: No

Type: Integer

Update requires: No interruption
