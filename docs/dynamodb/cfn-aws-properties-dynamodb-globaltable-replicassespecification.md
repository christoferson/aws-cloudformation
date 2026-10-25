> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicassespecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReplicaSSESpecification

Allows you to specify a KMS key identifier to be used for server-side encryption. The key can be specified via ARN, key ID, or alias. The key must be created in the same region as the replica.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "KMSMasterKeyId" : String
}

```

### YAML

```
  KMSMasterKeyId: String

```

## Properties

**`KMSMasterKeyId`** 

The AWS KMS key that should be used for the AWS KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb`. 

Required: Yes

Type: String

Update requires: No interruption
