> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extension-parameter.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Extension Parameter

A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked. Parameter values are specified in an extension association. For more information about extensions, see Extending workflows in the AWS AppConfig User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Description" : String,
  "Dynamic" : Boolean,
  "Required" : Boolean
}

```

### YAML

```
  Description: String
  Dynamic: Boolean
  Required: Boolean

```

## Properties

**`Description`** 

Information about the parameter. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`Dynamic`** 

Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association. Dynamic parameters can't be marked `Required`. 

Required: No

Type: Boolean

Update requires: No interruption

**`Required`** 

A parameter value must be specified in the extension association. 

Required: Yes

Type: Boolean

Update requires: No interruption
