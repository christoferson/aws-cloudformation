> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-localsecondaryindex.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable LocalSecondaryIndex

Represents the properties of a local secondary index. A local secondary index can only be created when its parent table is created.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "IndexName" : String,
  "KeySchema" : [ KeySchema, ... ],
  "Projection" : Projection
}

```

### YAML

```
  IndexName: String
  KeySchema: 
    - KeySchema
  Projection: 
    Projection

```

## Properties

**`IndexName`** 

The name of the local secondary index. The name must be unique among all other indexes on this table. 

Required: Yes

Type: String

Minimum: `3`

Maximum: `255`

Update requires: Updates are not supported.

**`KeySchema`** 

The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:  
`HASH` - partition key 
`RANGE` - sort key 
 Note

The partition key of an item is also known as its hash attribute. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its range attribute. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value. 

Required: Yes

Type: Array of KeySchema

Maximum: `2`

Update requires: Updates are not supported.

**`Projection`** 

Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.  

Required: Yes

Type: Projection

Update requires: Updates are not supported.
