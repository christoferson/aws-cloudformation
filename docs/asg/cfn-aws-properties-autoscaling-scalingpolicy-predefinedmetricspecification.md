> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::ScalingPolicy PredefinedMetricSpecification

Contains predefined metric specification information for a target tracking scaling policy for Amazon EC2 Auto Scaling.

`PredefinedMetricSpecification` is a property of the AWS::AutoScaling::ScalingPolicy TargetTrackingConfiguration property type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "PredefinedMetricType" : String,
  "ResourceLabel" : String
}

```

### YAML

```
  PredefinedMetricType: String
  ResourceLabel: String

```

## Properties

**`PredefinedMetricType`** 

The metric type. The following predefined metrics are available:  
`ASGAverageCPUUtilization` - Average CPU utilization of the Auto Scaling group. 
`ASGAverageNetworkIn` - Average number of bytes received on all network interfaces by the Auto Scaling group. 
`ASGAverageNetworkOut` - Average number of bytes sent out on all network interfaces by the Auto Scaling group. 
`ALBRequestCountPerTarget` - Average Application Load Balancer request count per target for your Auto Scaling group. 
 

Required: Yes

Type: String

Allowed values: `ASGAverageCPUUtilization | ASGAverageNetworkIn | ASGAverageNetworkOut | ALBRequestCountPerTarget`

Update requires: No interruption

**`ResourceLabel`** 

A label that uniquely identifies a specific Application Load Balancer target group from which to determine the average request count served by your Auto Scaling group. You can't specify a resource label unless the target group is attached to the Auto Scaling group. 

You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is: 

`app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`. 

Where:  
app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN 
targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN. 
 

To find the ARN for an Application Load Balancer, use the DescribeLoadBalancers API operation. To find the ARN for the target group, use the DescribeTargetGroups API operation. 

Required: Conditional

Type: String

Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

Minimum: `1`

Maximum: `1023`

Update requires: No interruption
