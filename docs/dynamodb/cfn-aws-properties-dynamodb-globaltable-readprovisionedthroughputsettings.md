> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReadProvisionedThroughputSettings

Allows you to specify the read capacity settings for a replica table or a replica global secondary index when the `BillingMode` is set to `PROVISIONED`. You must specify a value for either `ReadCapacityUnits` or `ReadCapacityAutoScalingSettings`, but not both. You can switch between fixed capacity and auto scaling.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReadCapacityAutoScalingSettings" : CapacityAutoScalingSettings,
  "ReadCapacityUnits" : Integer
}

```

### YAML

```
  ReadCapacityAutoScalingSettings: 
    CapacityAutoScalingSettings
  ReadCapacityUnits: Integer

```

## Properties

**`ReadCapacityAutoScalingSettings`** 

Specifies auto scaling settings for the replica table or global secondary index. 

Required: No

Type: CapacityAutoScalingSettings

Update requires: No interruption

**`ReadCapacityUnits`** 

Specifies a fixed read capacity for the replica table or global secondary index. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
