> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.html
> Downloaded: 2026-10-21

# AWS::ECS::Service GatewayConnectorHealthCheckMatcher

The codes that indicate a successful health check response from a target.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "GrpcCode" : String,
  "HttpCode" : String
}

```

### YAML

```
  GrpcCode: String
  HttpCode: String

```

## Properties

**`GrpcCode`** 

The gRPC codes that indicate a successful response from a target. 

Required: No

Type: String

Update requires: No interruption

**`HttpCode`** 

The HTTP codes that indicate a successful response from a target. 

Required: No

Type: String

Update requires: No interruption
