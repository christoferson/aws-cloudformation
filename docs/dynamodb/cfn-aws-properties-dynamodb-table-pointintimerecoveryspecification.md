> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-pointintimerecoveryspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table PointInTimeRecoverySpecification

The settings used to enable point in time recovery.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "PointInTimeRecoveryEnabled" : Boolean,
  "RecoveryPeriodInDays" : Integer
}

```

### YAML

```
  PointInTimeRecoveryEnabled: Boolean
  RecoveryPeriodInDays: Integer

```

## Properties

**`PointInTimeRecoveryEnabled`** 

Indicates whether point in time recovery is enabled (true) or disabled (false) on the table. 

Required: No

Type: Boolean

Update requires: No interruption

**`RecoveryPeriodInDays`** 

The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional. If no value is provided, the value will default to 35. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `35`

Update requires: No interruption

## See also

PointInTimeRecoverySpecification in the Amazon DynamoDB API Reference.
