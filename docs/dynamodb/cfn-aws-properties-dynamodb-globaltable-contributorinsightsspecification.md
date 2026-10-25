> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ContributorInsightsSpecification

Configures contributor insights settings for a replica or one of its indexes.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Enabled" : Boolean,
  "Mode" : String
}

```

### YAML

```
  Enabled: Boolean
  Mode: String

```

## Properties

**`Enabled`** 

Indicates whether CloudWatch Contributor Insights are to be enabled (true) or disabled (false). 

Required: Yes

Type: Boolean

Update requires: No interruption

**`Mode`** 

Specifies the CloudWatch Contributor Insights mode for a global table. Valid values are `ACCESSED_AND_THROTTLED_KEYS` (tracks all access and throttled events) or `THROTTLED_KEYS` (tracks only throttled events). This setting determines what type of contributor insights data is collected for the global table. 

Required: No

Type: String

Allowed values: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`

Update requires: No interruption
