> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-ondemandthroughput.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table OnDemandThroughput

Sets the maximum number of read and write units for the specified on-demand table. If you use this property, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MaxReadRequestUnits" : Integer,
  "MaxWriteRequestUnits" : Integer
}

```

### YAML

```
  MaxReadRequestUnits: Integer
  MaxWriteRequestUnits: Integer

```

## Properties

**`MaxReadRequestUnits`** 

Maximum number of read request units for the specified table. 

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`MaxWriteRequestUnits`** 

Maximum number of write request units for the specified table. 

To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
