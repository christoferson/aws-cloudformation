> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-attributedefinition.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable AttributeDefinition

Represents an attribute for describing the schema for the table and indexes.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeName" : String,
  "AttributeType" : String
}

```

### YAML

```
  AttributeName: String
  AttributeType: String

```

## Properties

**`AttributeName`** 

A name for the attribute. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `255`

Update requires: No interruption

**`AttributeType`** 

The data type for the attribute, where:  
`S` - the attribute is of type String 
`N` - the attribute is of type Number 
`B` - the attribute is of type Binary 
 

Required: Yes

Type: String

Allowed values: `S | N | B`

Update requires: No interruption
