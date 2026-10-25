> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-searchschemaelement.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table SearchSchemaElement

An element in the search schema of a vector index.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeName" : String,
  "SearchSchemaElementType" : String
}

```

### YAML

```
  AttributeName: String
  SearchSchemaElementType: String

```

## Properties

**`AttributeName`** 

The name of the attribute. This attribute must also be declared in the table's `AttributeDefinitions`. 

Required: Yes

Type: String

Maximum: `65535`

Update requires: Updates are not supported.

**`SearchSchemaElementType`** 

The role of the attribute in the search schema. Valid values:  
`HASH` - A partition key that partitions the vector index for independent scaling. When specified, you must provide this attribute's value in the `SearchConditionExpression`. 
`INLINE_FILTER` - An attribute projected into the vector index for filtering at the storage layer during search. Inline filters are optional in the `SearchConditionExpression`. 
 

Required: Yes

Type: String

Allowed values: `HASH | INLINE_FILTER`

Update requires: Updates are not supported.
