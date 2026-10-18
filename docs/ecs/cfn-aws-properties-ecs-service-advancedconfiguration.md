> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-advancedconfiguration.html
> Downloaded: 2026-10-18

# AWS::ECS::Service AdvancedConfiguration

The advanced settings for a load balancer used in blue/green deployments. Specify the alternate target group, listener rules, and IAM role required for traffic shifting during blue/green deployments. For more information, see Required resources for Amazon ECS blue/green deployments in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlternateTargetGroupArn" : String,
  "ProductionListenerRule" : String,
  "RoleArn" : String,
  "TestListenerRule" : String
}

```

### YAML

```
  AlternateTargetGroupArn: String
  ProductionListenerRule: String
  RoleArn: String
  TestListenerRule: String

```

## Properties

**`AlternateTargetGroupArn`** 

The Amazon Resource Name (ARN) of the alternate target group for Amazon ECS blue/green deployments. 

Required: Yes

Type: String

Update requires: No interruption

**`ProductionListenerRule`** 

The Amazon Resource Name (ARN) that that identifies the production listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing production traffic. 

Required: No

Type: String

Update requires: No interruption

**`RoleArn`** 

The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call the Elastic Load Balancing APIs for you. 

Required: No

Type: String

Update requires: No interruption

**`TestListenerRule`** 

The Amazon Resource Name (ARN) that identifies ) that identifies the test listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing test traffic. 

Required: No

Type: String

Update requires: No interruption
