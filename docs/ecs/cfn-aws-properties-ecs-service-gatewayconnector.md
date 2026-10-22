> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnector.html
> Downloaded: 2026-10-21

# AWS::ECS::Service GatewayConnector

A gateway connector that attaches an Amazon ECS service to a gateway ingress path. The connector specifies the service port that receives gateway-managed ingress traffic, along with the health check and traffic filters that the gateway applies. A service can have at most one gateway connector.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Filters" : GatewayConnectorFilters,
  "HealthCheck" : GatewayConnectorHealthCheck,
  "PortName" : String
}

```

### YAML

```
  Filters: 
    GatewayConnectorFilters
  HealthCheck: 
    GatewayConnectorHealthCheck
  PortName: String

```

## Properties

**`Filters`** 

The filters that control which gateway ingress paths the connector applies to. 

Required: No

Type: GatewayConnectorFilters

Update requires: No interruption

**`HealthCheck`** 

The health check that the gateway uses to determine whether the targets for this connector are healthy. 

Required: No

Type: GatewayConnectorHealthCheck

Update requires: No interruption

**`PortName`** 

The name of the service port that the gateway routes ingress traffic to. 

Required: Yes

Type: String

Update requires: No interruption
