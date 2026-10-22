> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-kms-key-policy.html
> Downloaded: 2026-10-22

# AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest

This topic describes how to set up the AWS KMS key policy and permissions that you need when you specify a customer managed key for encrypting Hooks annotations data that's available from the GetHookResult API. Note

CloudFormation Hooks doesn't need additional authorization to use the default AWS owned key to encrypt annotations data in your account.Topics
Overview
Using encryption context to control access to your customer managed key
Customer managed KMS key policy
KMS permissions for SetTypeConfiguration API
KMS permissions for GetHookResult API
 

## Overview 

The following AWS KMS keys can be used for encrypting Hook annotations data:  
AWS owned key – By default, CloudFormation uses an AWS owned key to encrypt data. You can't view, manage, or use AWS owned keys, or audit their use. However, you don't have to perform explicit configuration to protect the key that's used to encrypt your data. AWS owned keys are provided free of charge (no monthly fees or usage fees). Unless you are required to audit or control the encryption key that protects your annotations data, an AWS owned key is a good choice. 
Customer managed key – CloudFormation supports the use of a symmetric customer managed key that you create, own, and manage to add a second layer of encryption over the existing AWS owned key. AWS KMS charges apply. For more information, see Creating keys in the AWS Key Management Service Developer Guide. To manage your key, use the AWS Key Management Service (AWS KMS) in the AWS KMS console, the AWS CLI, or the AWS KMS API. For more information, see the AWS Key Management Service Developer Guide. 
 

You can configure customer managed keys when creating and updating Hooks. When you provide your customer managed key, CloudFormation uses this key to encrypt the annotations data before storing it. When the annotations data is later accessed during the `GetHookResult` API operation, CloudFormation automatically decrypts it. For information about configuring your encryption key for Hooks, see Hook configuration schema syntax reference. Important

Note that the `KmsKeyId` option to specify a customer managed key is currently only available when you use the AWS CLI to configure your Hook. 

## Using encryption context to control access to your customer managed key 

CloudFormation Hooks automatically includes encryption context with every annotation storage and retrieval operation. This allows you to set encryption context conditions in your key policy to ensure the key can only be used for specific Hooks:  
`kms:EncryptionContext:aws:cloudformation:hooks:service` – Ensures the key is only used by the CloudFormation Hooks service. 
`kms:EncryptionContext:aws:cloudformation:account-id` – Prevents cross-account key usage by matching your AWS account ID. 
`kms:EncryptionContext:aws:cloudformation:arn` – Restrict usage to specific Hooks using ARN patterns. 
 

These conditions provide additional protection against confused deputy attacks by cryptographically binding the encrypted data to the specific Hook context. 

## Customer managed KMS key policy 

When creating your customer managed key, you must define its key policy to allow the CloudFormation Hooks service to perform AWS KMS operations. To use the following key policy, replace the `placeholder values` with your own information.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "EnableIAMUserDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ExampleRole"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "cloudformation.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "EnableIAMUserGenerateDataKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ExampleRole"
      },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "cloudformation.us-east-1.amazonaws.com",
          "kms:EncryptionContext:aws:cloudformation:hooks:service": "hooks.cloudformation.amazonaws.com",
          "kms:EncryptionContext:aws:cloudformation:123456789012": "123456789012"
        },
        "ArnLike": {
          "kms:EncryptionContext:aws:cloudformation:arn": "arn:aws:cloudformation:*:123456789012:hook/*"
        }
      }
    },
    {
      "Sid": "EnableIAMUserDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ExampleRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "cloudformation.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowHooksServiceDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "hooks.cloudformation.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudformation:*:123456789012:hook/*"
        }
      }
    },
    {
      "Sid": "AllowHooksService",
      "Effect": "Allow",
      "Principal": {
        "Service": "hooks.cloudformation.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012",
          "kms:EncryptionContext:aws:cloudformation:hooks:service": "hooks.cloudformation.amazonaws.com",
          "kms:EncryptionContext:aws:cloudformation:123456789012": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudformation:*:123456789012:hook/*",
          "kms:EncryptionContext:aws:cloudformation:arn": "arn:aws:cloudformation:*:123456789012:hook/*"
        }
      }
    }
  ]
}

```
     

This policy grants permissions to both IAM roles (first three statements) and the CloudFormation Hooks service (last two statements). The `kms:ViaService` condition key ensures the KMS key can only be used through CloudFormation, preventing direct KMS API calls. The key operations are:  
`kms:DescribeKey` – Validates key properties and metadata. This operation is in separate statements because it cannot be used with encryption context conditions. 
`kms:GenerateDataKey` – Generates data encryption keys for encrypting annotations before storage. This operation includes encryption context conditions for scoped access control. 
`kms:Decrypt` – Decrypts previously encrypted annotations data. For IAM roles, this includes the `kms:ViaService` condition. For the service principal, this includes encryption context conditions. 
 

The `aws:SourceAccount` and `aws:SourceArn` condition keys provide the primary protection against confused deputy attacks. The encryption context conditions provide additional validation layers. For more information, see Using aws:SourceArn or aws:SourceAccount condition keys in the AWS Key Management Service Developer Guide. Important

Hook execution roles do not need AWS KMS permissions. The CloudFormation Hooks service principal performs all AWS KMS operations. 

## KMS permissions for `SetTypeConfiguration` API 

During the SetTypeConfiguration API call, CloudFormation validates user permissions to encrypt annotations data with the specified AWS KMS key. Add the following IAM policy to the user or role that will configure encryption using the `SetTypeConfiguration` API. Replace the `placeholder values` with your own information.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudformation:SetTypeConfiguration",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "kms:DescribeKey",
      "Resource": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
    },
    {
      "Effect": "Allow",
      "Action": "kms:GenerateDataKey",
      "Resource": "arn:aws:kms:us-east-1:123456789012:key/abc-123",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:cloudformation:hooks:service": "hooks.cloudformation.amazonaws.com",
          "kms:EncryptionContext:aws:cloudformation:123456789012": "123456789012"
        },
        "ArnLike": {
          "kms:EncryptionContext:aws:cloudformation:arn": "arn:aws:cloudformation:*:123456789012:hook/*"
        }
      }
    }
  ]
}

```
     

## KMS permissions for `GetHookResult` API 

To call GetHookResult for Hooks that use your customer managed key, users must have `kms:Decrypt` permission for that key. Add the following IAM policy to the user or role that will call `GetHookResult`. Replace ``arn:aws:kms:us-east-1:123456789012:key/abc-123`` with the ARN of your customer managed key.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudformation:GetHookResult",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
    }
  ]
}

```
