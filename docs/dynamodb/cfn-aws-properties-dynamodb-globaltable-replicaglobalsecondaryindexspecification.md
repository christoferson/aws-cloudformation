> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReplicaGlobalSecondaryIndexSpecification

Represents the properties of a global secondary index that can be set on a per-replica basis.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContributorInsightsSpecification" : ContributorInsightsSpecification,
  "IndexName" : String,
  "ReadOnDemandThroughputSettings" : ReadOnDemandThroughputSettings,
  "ReadProvisionedThroughputSettings" : ReadProvisionedThroughputSettings
}

```

### YAML

```
  ContributorInsightsSpecification: 
    ContributorInsightsSpecification
  IndexName: String
  ReadOnDemandThroughputSettings: 
    ReadOnDemandThroughputSettings
  ReadProvisionedThroughputSettings: 
    ReadProvisionedThroughputSettings

```

## Properties

**`ContributorInsightsSpecification`** 

Updates the status for contributor insights for a specific table or index. CloudWatch Contributor Insights for DynamoDB graphs display the partition key and (if applicable) sort key of frequently accessed items and frequently throttled items in plaintext. If you require the use of AWS Key Management Service (KMS) to encrypt this table’s partition key and sort key data with an AWS managed key or customer managed key, you should not enable CloudWatch Contributor Insights for DynamoDB for this table. 

Required: No

Type: ContributorInsightsSpecification

Update requires: No interruption

**`IndexName`** 

The name of the global secondary index. The name must be unique among all other indexes on this table. 

Required: Yes

Type: String

Minimum: `3`

Maximum: `255`

Update requires: Replacement

**`ReadOnDemandThroughputSettings`** 

Sets the read request settings for a replica global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`. 

Required: No

Type: ReadOnDemandThroughputSettings

Update requires: No interruption

**`ReadProvisionedThroughputSettings`** 

Allows you to specify the read capacity settings for a replica global secondary index when the `BillingMode` is set to `PROVISIONED`. 

Required: No

Type: ReadProvisionedThroughputSettings

Update requires: No interruption
