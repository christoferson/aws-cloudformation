> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorhealthcheck.html
> Downloaded: 2026-10-21

# AWS::ECS::Service GatewayConnectorHealthCheck

The health check configuration that a gateway uses to evaluate the targets associated with a gateway connector.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "HealthCheckIntervalSeconds" : Integer,
  "HealthCheckPath" : String,
  "HealthCheckPort" : Integer,
  "HealthCheckProtocol" : String,
  "HealthCheckTimeoutSeconds" : Integer,
  "HealthyThresholdCount" : Integer,
  "Matcher" : GatewayConnectorHealthCheckMatcher,
  "UnhealthyThresholdCount" : Integer
}

```

### YAML

```
  HealthCheckIntervalSeconds: Integer
  HealthCheckPath: String
  HealthCheckPort: Integer
  HealthCheckProtocol: String
  HealthCheckTimeoutSeconds: Integer
  HealthyThresholdCount: Integer
  Matcher: 
    GatewayConnectorHealthCheckMatcher
  UnhealthyThresholdCount: Integer

```

## Properties

**`HealthCheckIntervalSeconds`** 

The approximate amount of time, in seconds, between health checks of an individual target. 

Required: No

Type: Integer

Update requires: No interruption

**`HealthCheckPath`** 

The destination path for health check requests. 

Required: No

Type: String

Update requires: No interruption

**`HealthCheckPort`** 

The port that the gateway uses to perform health checks on the targets. 

Required: No

Type: Integer

Update requires: No interruption

**`HealthCheckProtocol`** 

The protocol that the gateway uses to perform health checks. 

Valid values:  
`HTTP` - Health checks are performed over HTTP. 
`HTTPS` - Health checks are performed over HTTPS. 
 

Required: No

Type: String

Allowed values: `HTTP | HTTPS`

Update requires: No interruption

**`HealthCheckTimeoutSeconds`** 

The amount of time, in seconds, during which no response from a target means a failed health check. 

Required: No

Type: Integer

Update requires: No interruption

**`HealthyThresholdCount`** 

The number of consecutive successful health checks that a target must pass before the gateway considers it healthy. 

Required: No

Type: Integer

Update requires: No interruption

**`Matcher`** 

The HTTP or gRPC codes that indicate a successful health check response from a target. 

Required: No

Type: GatewayConnectorHealthCheckMatcher

Update requires: No interruption

**`UnhealthyThresholdCount`** 

The number of consecutive failed health checks that a target must fail before the gateway considers it unhealthy. 

Required: No

Type: Integer

Update requires: No interruption
