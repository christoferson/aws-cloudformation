> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-timetolivespecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table TimeToLiveSpecification

Represents the settings used to enable or disable Time to Live (TTL) for the specified table.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AttributeName" : String,
  "Enabled" : Boolean
}

```

### YAML

```
  AttributeName: String
  Enabled: Boolean

```

## Properties

**`AttributeName`** 

The name of the TTL attribute used to store the expiration time for items in the table. Note 
The `AttributeName` property is required when enabling the TTL, or when TTL is already enabled. 
To update this property, you must first disable TTL and then enable TTL with the new attribute name. 
 

Required: Conditional

Type: String

Minimum: `1`

Maximum: `255`

Update requires: No interruption

**`Enabled`** 

Indicates whether TTL is to be enabled (true) or disabled (false) on the table. 

Required: Yes

Type: Boolean

Update requires: No interruption
