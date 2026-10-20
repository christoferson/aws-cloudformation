> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceNetworkConfiguration

The network configuration for an Express service. By default, an Express service utilizes subnets and security groups associated with the default VPC.

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

The IDs of the security groups associated with the Express service. 

Required: No

Type: Array of String

Update requires: No interruption

**`Subnets`** 

The IDs of the subnets associated with the Express service. 

Required: No

Type: Array of String

Update requires: No interruption
