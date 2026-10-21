> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-deployment-dynamicextensionparameters.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Deployment DynamicExtensionParameters

A map of dynamic extension parameter names to values to pass to associated extensions with `PRE_START_DEPLOYMENT` actions.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ExtensionReference" : String,
  "ParameterName" : String,
  "ParameterValue" : String
}

```

### YAML

```
  ExtensionReference: String
  ParameterName: String
  ParameterValue: String

```

## Properties

**`ExtensionReference`** 

The ARN or ID of the extension for which you are inserting a dynamic parameter. 

Required: No

Type: String

Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

Minimum: `20`

Maximum: `2048`

Update requires: Replacement

**`ParameterName`** 

The parameter name. 

Required: No

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`ParameterValue`** 

The parameter value. 

Required: No

Type: String

Update requires: Replacement
