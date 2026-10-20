> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-managedstorageconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Cluster ManagedStorageConfiguration

The managed storage configuration for the cluster.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "FargateEphemeralStorageKmsKeyId" : String,
  "KmsKeyId" : String
}

```

### YAML

```
  FargateEphemeralStorageKmsKeyId: String
  KmsKeyId: String

```

## Properties

**`FargateEphemeralStorageKmsKeyId`** 

Specify the AWS Key Management Service key ID for Fargate ephemeral storage. 

When you specify a `fargateEphemeralStorageKmsKeyId`, AWS Fargate uses the key to encrypt data at rest in ephemeral storage. For more information about Fargate ephemeral storage encryption, see Customer managed keys for AWS Fargate ephemeral storage for Amazon ECS in the Amazon Elastic Container Service Developer Guide. 

The key must be a single Region key. 

Required: No

Type: String

Update requires: No interruption

**`KmsKeyId`** 

Specify a AWS Key Management Service key ID to encrypt Amazon ECS managed storage. 

 When you specify a `kmsKeyId`, Amazon ECS uses the key to encrypt data volumes managed by Amazon ECS that are attached to tasks in the cluster. The following data volumes are managed by Amazon ECS: Amazon EBS. For more information about encryption of Amazon EBS volumes attached to Amazon ECS tasks, see Encrypt data stored in Amazon EBS volumes for Amazon ECS in the Amazon Elastic Container Service Developer Guide. 

The key must be a single Region key. 

Required: No

Type: String

Update requires: No interruption
