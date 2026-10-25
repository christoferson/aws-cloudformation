> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-ssespecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable SSESpecification

Represents the settings used to enable server-side encryption.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "SSEEnabled" : Boolean,
  "SSEType" : String
}

```

### YAML

```
  SSEEnabled: Boolean
  SSEType: String

```

## Properties

**`SSEEnabled`** 

Indicates whether server-side encryption is performed using an AWS managed key or an AWS owned key. If enabled (true), server-side encryption type is set to KMS and an AWS managed key is used (AWS KMS charges apply). If disabled (false) or not specified,server-side encryption is set to an AWS owned key. If you choose to use KMS encryption, you can also use customer managed KMS keys by specifying them in the `ReplicaSpecification.SSESpecification` object. You cannot mix AWS managed and customer managed KMS keys. 

Required: Yes

Type: Boolean

Update requires: No interruption

**`SSEType`** 

Server-side encryption type. The only supported value is:  
`KMS` - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply). 
 

Required: No

Type: String

Allowed values: `AES256 | KMS`

Update requires: No interruption
