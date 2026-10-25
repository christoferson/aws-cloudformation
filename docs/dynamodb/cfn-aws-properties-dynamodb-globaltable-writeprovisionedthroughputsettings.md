> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable WriteProvisionedThroughputSettings

Specifies an auto scaling policy for write capacity. This policy will be applied to all replicas. This setting must be specified if `BillingMode` is set to `PROVISIONED`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "WriteCapacityAutoScalingSettings" : CapacityAutoScalingSettings
}

```

### YAML

```
  WriteCapacityAutoScalingSettings: 
    CapacityAutoScalingSettings

```

## Properties

**`WriteCapacityAutoScalingSettings`** 

Specifies auto scaling settings for the replica table or global secondary index. 

Required: No

Type: CapacityAutoScalingSettings

Update requires: No interruption
