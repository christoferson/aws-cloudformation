> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewaytesttrafficheader.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayTestTrafficHeader

A header-based rule that identifies test traffic for progressive deployments.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "Values" : [ String, ... ]
}

```

### YAML

```
  Name: String
  Values: 
    - String

```

## Properties

**`Name`** 

The name of the header to match for test traffic routing. 

Required: Yes

Type: String

Update requires: No interruption

**`Values`** 

The header values to match for test traffic routing. 

Required: Yes

Type: Array of String

Update requires: No interruption
