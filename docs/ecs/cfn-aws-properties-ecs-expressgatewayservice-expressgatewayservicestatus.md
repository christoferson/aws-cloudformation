> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayservicestatus.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceStatus

An object that defines the status of Express service creation and information about the status of the service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "StatusCode" : String
}

```

### YAML

```
  StatusCode: String

```

## Properties

**`StatusCode`** 

The status of the Express service. 

Required: No

Type: String

Allowed values: `ACTIVE | DRAINING | INACTIVE`

Update requires: No interruption
