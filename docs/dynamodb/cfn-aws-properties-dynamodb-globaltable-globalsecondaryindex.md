> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-globalsecondaryindex.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable GlobalSecondaryIndex

Allows you to specify a global secondary index for the global table. The index will be defined on all replicas.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "IndexName" : String,
  "KeySchema" : [ KeySchema, ... ],
  "Projection" : Projection,
  "ReadOnDemandThroughputSettings" : ReadOnDemandThroughputSettings,
  "ReadProvisionedThroughputSettings" : GlobalReadProvisionedThroughputSettings,
  "WarmThroughput" : WarmThroughput,
  "WriteOnDemandThroughputSettings" : WriteOnDemandThroughputSettings,
  "WriteProvisionedThroughputSettings" : WriteProvisionedThroughputSettings
}

```

### YAML

```
  IndexName: String
  KeySchema: 
    - KeySchema
  Projection: 
    Projection
  ReadOnDemandThroughputSettings: 
    ReadOnDemandThroughputSettings
  ReadProvisionedThroughputSettings: 
    GlobalReadProvisionedThroughputSettings
  WarmThroughput: 
    WarmThroughput
  WriteOnDemandThroughputSettings: 
    WriteOnDemandThroughputSettings
  WriteProvisionedThroughputSettings: 
    WriteProvisionedThroughputSettings

```

## Properties

**`IndexName`** 

The name of the global secondary index. The name must be unique among all other indexes on this table. 

Required: Yes

Type: String

Minimum: `3`

Maximum: `255`

Update requires: Updates are not supported.

**`KeySchema`** 

The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:  
`HASH` - partition key 
`RANGE` - sort key 
 Note

The partition key of an item is also known as its hash attribute. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.

The sort key of an item is also known as its range attribute. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value. 

Required: Yes

Type: Array of KeySchema

Minimum: `1`

Maximum: `8`

Update requires: Updates are not supported.

**`Projection`** 

Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. 

Required: Yes

Type: Projection

Update requires: Updates are not supported.

**`ReadOnDemandThroughputSettings`** 

Sets read capacity settings for the global secondary index of the global table, which applies to all replicas. This can only be applied for multi-account global tables. 

Required: No

Type: ReadOnDemandThroughputSettings

Update requires: No interruption

**`ReadProvisionedThroughputSettings`** 

Sets the read request settings for the global secondary index of the global table, which applies to all replicas. This can only be applied for multi-account global tables. 

Required: No

Type: GlobalReadProvisionedThroughputSettings

Update requires: No interruption

**`WarmThroughput`** 

Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond`, `WriteUnitsPerSecond`, or both. 

Required: No

Type: WarmThroughput

Update requires: No interruption

**`WriteOnDemandThroughputSettings`** 

Sets the write request settings for a global table or a global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`. 

Required: No

Type: WriteOnDemandThroughputSettings

Update requires: No interruption

**`WriteProvisionedThroughputSettings`** 

Defines write capacity settings for the global secondary index. You must specify a value for this property if the table's `BillingMode` is `PROVISIONED`. All replicas will have the same write capacity settings for this global secondary index. 

Required: No

Type: WriteProvisionedThroughputSettings

Update requires: No interruption
