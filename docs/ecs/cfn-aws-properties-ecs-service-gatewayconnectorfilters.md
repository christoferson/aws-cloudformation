> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorfilters.html
> Downloaded: 2026-10-21

# AWS::ECS::Service GatewayConnectorFilters

The filters that determine which gateway ingress paths a connector applies to.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AccessTypes" : [ String, ... ]
}

```

### YAML

```
  AccessTypes: 
    - String

```

## Properties

**`AccessTypes`** 

The access types of the gateway ingress paths that the connector applies to. 

The access type can be one of the following values:  
`PUBLIC` - The ingress path is publicly accessible. 
`PRIVATE` - The ingress path is only accessible privately. 
 

Required: No

Type: Array of String

Allowed values: `PUBLIC | PRIVATE`

Update requires: No interruption
