> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-keyvaluepair.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService KeyValuePair

A key-value pair object.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "Value" : String
}

```

### YAML

```
  Name: String
  Value: String

```

## Properties

**`Name`** 

The name of the key-value pair. For environment variables, this is the name of the environment variable. 

Required: Yes

Type: String

Update requires: No interruption

**`Value`** 

The value of the key-value pair. For environment variables, this is the value of the environment variable. 

Required: Yes

Type: String

Update requires: No interruption
