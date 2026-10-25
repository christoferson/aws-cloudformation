> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-vectorattribute.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table VectorAttribute

The definition of a vector attribute for a vector index.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeName" : String
}

```

### YAML

```
  AttributeName: String

```

## Properties

**`AttributeName`** 

The name of the vector attribute. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `255`

Update requires: Updates are not supported.
