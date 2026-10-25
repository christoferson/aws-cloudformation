> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-timetolivespecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable TimeToLiveSpecification

Represents the settings used to enable or disable Time to Live (TTL) for the specified table. All replicas will have the same time to live configuration.

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

The name of the attribute used to store the expiration time for items in the table. 

Currently, you cannot directly change the attribute name used to evaluate time to live. In order to do so, you must first disable time to live, and then re-enable it with the new attribute name. It can take up to one hour for changes to time to live to take effect. If you attempt to modify time to live within that time window, your stack operation might be delayed. 

Required: No

Type: String

Minimum: `1`

Maximum: `255`

Update requires: No interruption

**`Enabled`** 

Indicates whether TTL is to be enabled (true) or disabled (false) on the table. 

Required: Yes

Type: Boolean

Update requires: No interruption
