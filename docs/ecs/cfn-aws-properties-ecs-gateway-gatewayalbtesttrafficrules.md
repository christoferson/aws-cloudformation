> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayalbtesttrafficrules.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayAlbTestTrafficRules

The rules that route test traffic to services behind a gateway during progressive deployments.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Header" : GatewayTestTrafficHeader
}

```

### YAML

```
  Header: 
    GatewayTestTrafficHeader

```

## Properties

**`Header`** 

The header-based rule that identifies test traffic. 

Required: No

Type: GatewayTestTrafficHeader

Update requires: No interruption
