> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-networkconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service NetworkConfiguration

The network configuration for a task or service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AwsvpcConfiguration" : AwsVpcConfiguration
}

```

### YAML

```
  AwsvpcConfiguration: 
    AwsVpcConfiguration

```

## Properties

**`AwsvpcConfiguration`** 

The VPC subnets and security groups that are associated with a task. Note

All specified subnets and security groups must be from the same VPC. 

Required: No

Type: AwsVpcConfiguration

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
