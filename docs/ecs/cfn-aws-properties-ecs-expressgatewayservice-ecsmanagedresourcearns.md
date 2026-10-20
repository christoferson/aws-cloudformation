> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ECSManagedResourceArns

The `ECSManagedResourceArns` property type specifies Property description not available. for an AWS::ECS::ExpressGatewayService.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AutoScaling" : AutoScalingArns,
  "IngressPath" : IngressPathArns,
  "LogGroups" : [ String, ... ],
  "MetricAlarms" : [ String, ... ],
  "ServiceSecurityGroups" : [ String, ... ]
}

```

### YAML

```
  AutoScaling: 
    AutoScalingArns
  IngressPath: 
    IngressPathArns
  LogGroups: 
    - String
  MetricAlarms: 
    - String
  ServiceSecurityGroups: 
    - String

```

## Properties

**`AutoScaling`**

Property description not available.

Required: No

Type: AutoScalingArns

Update requires: No interruption

**`IngressPath`**

Property description not available.

Required: No

Type: IngressPathArns

Update requires: No interruption

**`LogGroups`**

Property description not available.

Required: No

Type: Array of String

Update requires: No interruption

**`MetricAlarms`**

Property description not available.

Required: No

Type: Array of String

Update requires: No interruption

**`ServiceSecurityGroups`**

Property description not available.

Required: No

Type: Array of String

Update requires: No interruption
