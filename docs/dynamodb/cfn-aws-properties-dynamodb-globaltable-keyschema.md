> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-keyschema.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable KeySchema

Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

A `KeySchemaElement` represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one `KeySchemaElement` (for the partition key). A composite primary key would require one `KeySchemaElement` for the partition key, and another `KeySchemaElement` for the sort key.

A `KeySchemaElement` must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeName" : String,
  "KeyType" : String
}

```

### YAML

```
  AttributeName: String
  KeyType: String

```

## Properties

**`AttributeName`** 

The name of a key attribute. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `255`

Update requires: Replacement

**`KeyType`** 

The role that this key attribute will assume:  
`HASH` - partition key 
`RANGE` - sort key 
 Note

The partition key of an item is also known as its hash attribute. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its range attribute. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value. 

Required: Yes

Type: String

Allowed values: `HASH | RANGE`

Update requires: Replacement
