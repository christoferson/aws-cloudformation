> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-globalsecondaryindex.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table GlobalSecondaryIndex

Represents the properties of a global secondary index.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContributorInsightsSpecification" : ContributorInsightsSpecification,
  "IndexName" : String,
  "KeySchema" : [ KeySchema, ... ],
  "OnDemandThroughput" : OnDemandThroughput,
  "Projection" : Projection,
  "ProvisionedThroughput" : ProvisionedThroughput,
  "WarmThroughput" : WarmThroughput
}

```

### YAML

```
  ContributorInsightsSpecification: 
    ContributorInsightsSpecification
  IndexName: String
  KeySchema: 
    - KeySchema
  OnDemandThroughput: 
    OnDemandThroughput
  Projection: 
    Projection
  ProvisionedThroughput: 
    ProvisionedThroughput
  WarmThroughput: 
    WarmThroughput

```

## Properties

**`ContributorInsightsSpecification`** 

The settings used to specify whether to enable CloudWatch Contributor Insights for the global table and define which events to monitor. 

Required: No

Type: ContributorInsightsSpecification

Update requires: No interruption

**`IndexName`** 

The name of the global secondary index. The name must be unique among all other indexes on this table. 

Required: Yes

Type: String

Pattern: `[a-zA-Z0-9_.-]+`

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

Update requires: Updates are not supported.

**`OnDemandThroughput`** 

The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode. 

Required: No

Type: OnDemandThroughput

Update requires: No interruption

**`Projection`** 

Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.  

Required: Yes

Type: Projection

Update requires: Updates are not supported.

**`ProvisionedThroughput`** 

Represents the provisioned throughput settings for the specified global secondary index. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode. 

For current minimum and maximum provisioned throughput values, see Service, Account, and Table Quotas in the Amazon DynamoDB Developer Guide. 

Required: No

Type: ProvisionedThroughput

Update requires: No interruption

**`WarmThroughput`** 

Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond`, `WriteUnitsPerSecond`, or both. 

Required: No

Type: WarmThroughput

Update requires: No interruption
