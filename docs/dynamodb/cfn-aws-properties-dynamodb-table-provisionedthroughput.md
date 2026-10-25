> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-provisionedthroughput.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table ProvisionedThroughput

Throughput for the specified table, which consists of values for `ReadCapacityUnits` and `WriteCapacityUnits`. For more information about the contents of a provisioned throughput structure, see Amazon DynamoDB Table ProvisionedThroughput. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReadCapacityUnits" : Integer,
  "WriteCapacityUnits" : Integer
}

```

### YAML

```
  ReadCapacityUnits: Integer
  WriteCapacityUnits: Integer

```

## Properties

**`ReadCapacityUnits`** 

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide. 

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0. 

Required: Yes

Type: Integer

Update requires: No interruption

**`WriteCapacityUnits`** 

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide. 

If read/write capacity mode is `PAY_PER_REQUEST` the value is set to 0. 

Required: Yes

Type: Integer

Update requires: No interruption
