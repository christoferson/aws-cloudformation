> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-readondemandthroughputsettings.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReadOnDemandThroughputSettings

Sets the read request settings for a replica table or a replica global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MaxReadRequestUnits" : Integer
}

```

### YAML

```
  MaxReadRequestUnits: Integer

```

## Properties

**`MaxReadRequestUnits`** 

Maximum number of read request units for the specified replica of a global table. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption
