> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicaspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReplicaSpecification

Defines settings specific to a single replica of a global table.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContributorInsightsSpecification" : ContributorInsightsSpecification,
  "DeletionProtectionEnabled" : Boolean,
  "DisassociationProtectionEnabled" : Boolean,
  "GlobalSecondaryIndexes" : [ ReplicaGlobalSecondaryIndexSpecification, ... ],
  "GlobalTableSettingsReplicationMode" : String,
  "KinesisStreamSpecification" : KinesisStreamSpecification,
  "PointInTimeRecoverySpecification" : PointInTimeRecoverySpecification,
  "ReadOnDemandThroughputSettings" : ReadOnDemandThroughputSettings,
  "ReadProvisionedThroughputSettings" : ReadProvisionedThroughputSettings,
  "Region" : String,
  "ReplicaStreamSpecification" : ReplicaStreamSpecification,
  "ResourcePolicy" : ResourcePolicy,
  "SSESpecification" : ReplicaSSESpecification,
  "TableClass" : String,
  "Tags" : [ Tag, ... ]
}

```

### YAML

```
  ContributorInsightsSpecification: 
    ContributorInsightsSpecification
  DeletionProtectionEnabled: Boolean
  DisassociationProtectionEnabled: Boolean
  GlobalSecondaryIndexes: 
    - ReplicaGlobalSecondaryIndexSpecification
  GlobalTableSettingsReplicationMode: String
  KinesisStreamSpecification: 
    KinesisStreamSpecification
  PointInTimeRecoverySpecification: 
    PointInTimeRecoverySpecification
  ReadOnDemandThroughputSettings: 
    ReadOnDemandThroughputSettings
  ReadProvisionedThroughputSettings: 
    ReadProvisionedThroughputSettings
  Region: String
  ReplicaStreamSpecification: 
    ReplicaStreamSpecification
  ResourcePolicy: 
    ResourcePolicy
  SSESpecification: 
    ReplicaSSESpecification
  TableClass: String
  Tags: 
    - Tag

```

## Properties

**`ContributorInsightsSpecification`** 

The settings used to enable or disable CloudWatch Contributor Insights for the specified replica. When not specified, defaults to contributor insights disabled for the replica. 

Required: No

Type: ContributorInsightsSpecification

Update requires: No interruption

**`DeletionProtectionEnabled`** 

Determines if a replica is protected from deletion. When enabled, the table cannot be deleted by any user or process. This setting is disabled by default. For more information, see Using deletion protection in the Amazon DynamoDBDeveloper Guide. 

Required: No

Type: Boolean

Update requires: No interruption

**`DisassociationProtectionEnabled`** 

Protects a global table replica from disassociation. Enabled by default and independent of `DeletionProtectionEnabled`. You manage this setting independently for each replica. 

Set this property to `false` in a separate stack update before you set `TableType` to `Regional`. Remove this property in the disassociation update. The setting applies only while the table is a replica, so a value left in the template is reported as drift after disassociation. In other updates, omitting this property leaves the existing protection setting unchanged. For more information, see the TableType property. 

Required: No

Type: Boolean

Update requires: No interruption

**`GlobalSecondaryIndexes`** 

Defines additional settings for the global secondary indexes of this replica. 

Required: No

Type: Array of ReplicaGlobalSecondaryIndexSpecification

Update requires: No interruption

**`GlobalTableSettingsReplicationMode`** 

The replication mode for global table settings across multiple accounts. In a multi-account global table, you cannot make changes to a synchronized setting using CloudFormation. You need to use console or CLI to make any settings changes. 

Required: No

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: No interruption

**`KinesisStreamSpecification`** 

Defines the Kinesis Data Streams configuration for the specified replica. 

Required: No

Type: KinesisStreamSpecification

Update requires: No interruption

**`PointInTimeRecoverySpecification`** 

The settings used to enable point in time recovery. When not specified, defaults to point in time recovery disabled for the replica. 

Required: No

Type: PointInTimeRecoverySpecification

Update requires: No interruption

**`ReadOnDemandThroughputSettings`** 

Sets read request settings for the replica table. 

Required: No

Type: ReadOnDemandThroughputSettings

Update requires: No interruption

**`ReadProvisionedThroughputSettings`** 

Defines read capacity settings for the replica table. 

Required: No

Type: ReadProvisionedThroughputSettings

Update requires: No interruption

**`Region`** 

The region in which this replica exists. 

Required: Yes

Type: String

Update requires: No interruption

**`ReplicaStreamSpecification`** 

Represents the DynamoDB Streams configuration for a global table replica.  

Required: No

Type: ReplicaStreamSpecification

Update requires: No interruption

**`ResourcePolicy`** 

A resource-based policy document that contains permissions to add to the specified replica of a DynamoDB global table. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource. 

In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see Using resource-based policies for DynamoDB and Resource-based policy examples. 

Required: No

Type: ResourcePolicy

Update requires: No interruption

**`SSESpecification`** 

Allows you to specify a customer-managed key for the replica. When using customer-managed keys for server-side encryption, this property must have a value in all replicas. 

Required: No

Type: ReplicaSSESpecification

Update requires: No interruption

**`TableClass`** 

The table class of the specified table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`. 

Required: No

Type: String

Allowed values: `STANDARD | STANDARD_INFREQUENT_ACCESS`

Update requires: No interruption

**`Tags`** 

An array of key-value pairs to apply to this replica. 

For more information, see Tag. 

Required: No

Type: Array of Tag

Update requires: No interruption
