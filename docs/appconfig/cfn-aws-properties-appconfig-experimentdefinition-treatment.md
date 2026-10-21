> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentdefinition-treatment.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExperimentDefinition Treatment

Describes a treatment in an experiment, including its traffic allocation weight and feature flag value.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeValues" : {Key: Value, ...},
  "Description" : String,
  "Enabled" : Boolean,
  "Key" : String,
  "Weight" : Number
}

```

### YAML

```
  AttributeValues: 
    Key: Value
  Description: String
  Enabled: Boolean
  Key: String
  Weight: Number

```

## Properties

**`AttributeValues`**

Property description not available.

Required: No

Type: Object of AttributeValue

Update requires: No interruption

**`Description`** 

A description of the treatment. 

Required: No

Type: String

Maximum: `1024`

Update requires: No interruption

**`Enabled`**

Property description not available.

Required: Yes

Type: Boolean

Update requires: No interruption

**`Key`** 

The unique key that identifies this treatment. 

Required: No

Type: String

Pattern: `^[a-zA-Z0-9]{1,8}`

Update requires: No interruption

**`Weight`** 

The traffic allocation weight for this treatment. 

Required: Yes

Type: Number

Update requires: No interruption
