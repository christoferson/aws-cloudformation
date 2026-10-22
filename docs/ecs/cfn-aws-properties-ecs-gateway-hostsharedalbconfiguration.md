> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-hostsharedalbconfiguration.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway HostSharedAlbConfiguration

The configuration for a gateway that uses shared Application Load Balancers with host-based routing. Where they apply, the field names and values are kept consistent with the Elastic Load Balancing API.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AccessLogs" : GatewayElbAccessLogConfiguration,
  "CurrentAlbCount" : Integer,
  "HttpDesync" : String,
  "MaxAlbCount" : Integer,
  "NetworkConfiguration" : GatewayElbNetworkConfiguration,
  "Port" : Integer,
  "Protocol" : String,
  "Scheme" : String,
  "TestTrafficRules" : GatewayAlbTestTrafficRules,
  "WebACLArn" : String
}

```

### YAML

```
  AccessLogs: 
    GatewayElbAccessLogConfiguration
  CurrentAlbCount: Integer
  HttpDesync: String
  MaxAlbCount: Integer
  NetworkConfiguration: 
    GatewayElbNetworkConfiguration
  Port: Integer
  Protocol: String
  Scheme: String
  TestTrafficRules: 
    GatewayAlbTestTrafficRules
  WebACLArn: String

```

## Properties

**`AccessLogs`** 

The access log configuration for the load balancers that the gateway manages. 

Required: No

Type: GatewayElbAccessLogConfiguration

Update requires: No interruption

**`CurrentAlbCount`**

Property description not available.

Required: No

Type: Integer

Update requires: No interruption

**`HttpDesync`** 

The desync mitigation mode for the load balancers that the gateway manages, which determines how the load balancers handle requests that might pose a security risk. The default is `defensive`. 

Required: No

Type: String

Allowed values: `monitor | defensive | strictest`

Update requires: No interruption

**`MaxAlbCount`** 

The maximum number of Application Load Balancers that the gateway manages. The default is 10. 

Required: No

Type: Integer

Update requires: No interruption

**`NetworkConfiguration`** 

The network configuration for the load balancers that the gateway manages. 

Required: No

Type: GatewayElbNetworkConfiguration

Update requires: No interruption

**`Port`** 

The port that the load balancer listener uses is 443. The gateway supports only HTTPS at port 443. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `65535`

Update requires: Replacement

**`Protocol`** 

The protocol for the load balancer listener is `HTTPS`. No other protocol is supported. 

Required: No

Type: String

Allowed values: `HTTP | HTTPS`

Update requires: Replacement

**`Scheme`** 

Specifies whether the load balancers the gateway manages are `internet-facing` or `internal`. The default is `internet-facing`. 

Required: No

Type: String

Allowed values: `internet-facing | internal`

Update requires: Replacement

**`TestTrafficRules`** 

The rules that route test traffic for progressive deployments. During a progressive deployment, requests whose headers match these rules are routed to the new service revision so that it can be validated before production traffic shifts to it. 

Required: No

Type: GatewayAlbTestTrafficRules

Update requires: No interruption

**`WebACLArn`** 

The Amazon Resource Name (ARN) of the WAF web ACL to associate with the load balancers that the gateway manages. 

Required: No

Type: String

Update requires: No interruption
