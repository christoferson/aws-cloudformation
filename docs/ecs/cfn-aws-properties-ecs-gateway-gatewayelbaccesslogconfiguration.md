> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayElbAccessLogConfiguration

The access log configuration for the load balancers that a gateway manages.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Destination" : GatewayElbAccessLogDestination
}

```

### YAML

```
  Destination: 
    GatewayElbAccessLogDestination

```

## Properties

**`Destination`** 

The destination where access logs are delivered. 

Required: No

Type: GatewayElbAccessLogDestination

Update requires: No interruption
