> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-timeoutconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service TimeoutConfiguration

An object that represents the timeout configurations for Service Connect.Note

If `idleTimeout` is set to a time that is less than `perRequestTimeout`, the connection will close when the `idleTimeout` is reached and not the `perRequestTimeout`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "IdleTimeoutSeconds" : Integer,
  "PerRequestTimeoutSeconds" : Integer
}

```

### YAML

```
  IdleTimeoutSeconds: Integer
  PerRequestTimeoutSeconds: Integer

```

## Properties

**`IdleTimeoutSeconds`** 

The amount of time in seconds a connection will stay active while idle. A value of `0` can be set to disable `idleTimeout`. 

The `idleTimeout` default for `HTTP`/`HTTP2`/`GRPC` is 5 minutes. 

The `idleTimeout` default for `TCP` is 1 hour. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `2147483647`

Update requires: No interruption

**`PerRequestTimeoutSeconds`** 

The amount of time waiting for the upstream to respond with a complete response per request. A value of `0` can be set to disable `perRequestTimeout`. `perRequestTimeout` can only be set if Service Connect `appProtocol` isn't `TCP`. Only `idleTimeout` is allowed for `TCP``appProtocol`. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `2147483647`

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
