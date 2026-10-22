> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayconfiguration.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayConfiguration

The type-specific configuration for a gateway that you provide when you create it. Exactly one variant is set, and it determines the gateway type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "HostSharedAlb" : HostSharedAlbConfiguration
}

```

### YAML

```
  HostSharedAlb: 
    HostSharedAlbConfiguration

```

## Properties

**`HostSharedAlb`** 

The configuration for a host-based, shared Application Load Balancer gateway. Each service that uses the gateway is assigned a unique DNS host name. 

Required: Yes

Type: HostSharedAlbConfiguration

Update requires: No interruption
