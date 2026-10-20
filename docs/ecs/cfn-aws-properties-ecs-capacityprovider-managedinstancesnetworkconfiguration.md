> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider ManagedInstancesNetworkConfiguration

The network configuration for Amazon ECS Managed Instances. This specifies the VPC subnets and security groups that instances use for network connectivity. Amazon ECS Managed Instances support multiple network modes including `awsvpc` (instances receive ENIs for task isolation), `host` (instances share network namespace with tasks), and `none` (no external network connectivity), ensuring backward compatibility for migrating workloads from Fargate or Amazon EC2.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "SecurityGroups" : [ String, ... ],
  "Subnets" : [ String, ... ]
}

```

### YAML

```
  SecurityGroups: 
    - String
  Subnets: 
    - String

```

## Properties

**`SecurityGroups`** 

The list of security group IDs to apply to Amazon ECS Managed Instances. These security groups control the network traffic allowed to and from the instances. 

Required: Yes

Type: Array of String

Update requires: No interruption

**`Subnets`** 

The list of subnet IDs where Amazon ECS can launch Amazon ECS Managed Instances. Instances are distributed across the specified subnets for high availability. All subnets must be in the same VPC. 

Required: Yes

Type: Array of String

Update requires: No interruption
