> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-warmthroughput.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable WarmThroughput

Provides visibility into the number of read and write operations your table or secondary index can instantaneously support. The settings can be modified using the `UpdateTable` operation to meet the throughput requirements of an upcoming peak event.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReadUnitsPerSecond" : Integer,
  "WriteUnitsPerSecond" : Integer
}

```

### YAML

```
  ReadUnitsPerSecond: Integer
  WriteUnitsPerSecond: Integer

```

## Properties

**`ReadUnitsPerSecond`** 

Represents the number of read operations your base table can instantaneously support. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`WriteUnitsPerSecond`** 

Represents the number of write operations your base table can instantaneously support. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
