> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentdefinition-attributevalue.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExperimentDefinition AttributeValue

A value for a feature flag attribute. Only one of the members can be set.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "BooleanValue" : Boolean,
  "NumberArray" : [ Number, ... ],
  "NumberValue" : Number,
  "StringArray" : [ String, ... ],
  "StringValue" : String
}

```

### YAML

```
  BooleanValue: 
    Boolean
  NumberArray: 
    - Number
  NumberValue: 
    Number
  StringArray: 
    - String
  StringValue: 
    String

```

## Properties

**`BooleanValue`** 

A Boolean value for the attribute. 

Required: No

Type: Boolean

Update requires: No interruption

**`NumberArray`** 

An array of numeric values for the attribute. 

Required: No

Type: Array of Number

Minimum: `0`

Maximum: `25`

Update requires: No interruption

**`NumberValue`** 

A numeric value for the attribute. 

Required: No

Type: Number

Update requires: No interruption

**`StringArray`** 

An array of string values for the attribute. 

Required: No

Type: Array of String

Minimum: `0`

Maximum: `25`

Update requires: No interruption

**`StringValue`** 

A string value for the attribute. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption
