> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-writeondemandthroughputsettings.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable WriteOnDemandThroughputSettings

Sets the write request settings for a global table or a global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MaxWriteRequestUnits" : Integer
}

```

### YAML

```
  MaxWriteRequestUnits: Integer

```

## Properties

**`MaxWriteRequestUnits`** 

Maximum number of write request settings for the specified replica of a global table. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
