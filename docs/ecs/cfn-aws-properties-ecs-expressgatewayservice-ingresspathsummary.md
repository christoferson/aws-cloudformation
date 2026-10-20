> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-ingresspathsummary.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService IngressPathSummary

The entry point into an Express service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AccessType" : String,
  "Endpoint" : String
}

```

### YAML

```
  AccessType: String
  Endpoint: String

```

## Properties

**`AccessType`** 

The type of access to the endpoint for the Express service. 

Required: No

Type: String

Allowed values: `PUBLIC | PRIVATE`

Update requires: No interruption

**`Endpoint`** 

The endpoint for access to the service. 

Required: No

Type: String

Update requires: No interruption
