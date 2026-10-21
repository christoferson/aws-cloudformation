> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extensionassociation-tag.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExtensionAssociation Tag

Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Key" : String,
  "Value" : String
}

```

### YAML

```
  Key: String
  Value: String

```

## Properties

**`Key`** 

A key and optional value to help you categorize resources. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`Value`** 

An optional tag value. 

Required: Yes

Type: String

Minimum: `0`

Maximum: `256`

Update requires: No interruption
