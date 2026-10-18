> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-hooktimeoutconfig.html
> Downloaded: 2026-10-18

# AWS::ECS::Service HookTimeoutConfig

The `HookTimeoutConfig` property type specifies Property description not available. for an AWS::ECS::Service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Action" : String,
  "TimeoutInMinutes" : Integer
}

```

### YAML

```
  Action: String
  TimeoutInMinutes: Integer

```

## Properties

**`Action`**

Property description not available.

Required: No

Type: String

Allowed values: `ROLLBACK | CONTINUE`

Update requires: No interruption

**`TimeoutInMinutes`**

Property description not available.

Required: No

Type: Integer

Minimum: `1`

Maximum: `20160`

Update requires: No interruption
