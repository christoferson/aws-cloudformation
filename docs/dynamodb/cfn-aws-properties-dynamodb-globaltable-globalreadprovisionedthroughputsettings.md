> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable GlobalReadProvisionedThroughputSettings

Sets read capacity settings for the multi-account global table or its global secondary index.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReadCapacityUnits" : Integer
}

```

### YAML

```
  ReadCapacityUnits: Integer

```

## Properties

**`ReadCapacityUnits`** 

Sets read capacity settings for the multi-account global table or its global secondary index. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
