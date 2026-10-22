> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayElbNetworkConfiguration

The network configuration for the load balancers that a gateway manages.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "InboundSecurityGroup" : String,
  "IpAddressType" : String,
  "Subnets" : [ String, ... ]
}

```

### YAML

```
  InboundSecurityGroup: String
  IpAddressType: String
  Subnets: 
    - String

```

## Properties

**`InboundSecurityGroup`** 

The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages. 

Required: No

Type: String

Update requires: No interruption

**`IpAddressType`** 

The IP address type for the load balancers that the gateway manages. The default is `dualstack`. 

Required: No

Type: String

Allowed values: `ipv4 | dualstack | dualstack-without-public-ipv4`

Update requires: Replacement

**`Subnets`** 

The subnets for the load balancers that the gateway manages. The default is the subnets in the default VPC. 

Required: No

Type: Array of String

Minimum: `2`

Update requires: Replacement
