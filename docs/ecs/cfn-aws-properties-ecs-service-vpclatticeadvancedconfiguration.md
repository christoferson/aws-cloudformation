> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-vpclatticeadvancedconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service VpcLatticeAdvancedConfiguration

The advanced settings for VPC Lattice used in blue/green deployments. Specify the alternate target group and listener rules required for traffic shifting during blue/green deployments. For more information, see Required resources for Amazon ECS blue/green deployments in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlternateTargetGroupArn" : String,
  "ProductionListenerRule" : String,
  "TestListenerRule" : String
}

```

### YAML

```
  AlternateTargetGroupArn: String
  ProductionListenerRule: String
  TestListenerRule: String

```

## Properties

**`AlternateTargetGroupArn`** 

The Amazon Resource Name (ARN) of the alternate target group associated with the VPC Lattice Configuration for Amazon ECS blue/green deployments. 

Required: No

Type: String

Update requires: No interruption

**`ProductionListenerRule`** 

The Amazon Resource Name (ARN) that identifies the production listener rule or listener for routing production traffic. 

Required: No

Type: String

Update requires: No interruption

**`TestListenerRule`** 

The Amazon Resource Name (ARN) that identifies the test listener rule or listener for routing test traffic. 

Required: No

Type: String

Update requires: No interruption
