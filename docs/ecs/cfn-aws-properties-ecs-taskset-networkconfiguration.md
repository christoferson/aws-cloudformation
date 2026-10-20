> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskset-networkconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskSet NetworkConfiguration

The network configuration for a task or service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AwsVpcConfiguration" : AwsVpcConfiguration
}

```

### YAML

```
  AwsVpcConfiguration: 
    AwsVpcConfiguration

```

## Properties

**`AwsVpcConfiguration`** 

The VPC subnets and security groups that are associated with a task. Note

All specified subnets and security groups must be from the same VPC. 

Required: No

Type: AwsVpcConfiguration

Update requires: Replacement
