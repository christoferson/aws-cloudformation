## KMS Cloudformation Template

### KMS - Symmetric

Provision a Symmetric Key with Alias Name

[kms-symmetric](kms-symmetric.yaml)

### Resources

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KMS.html
- https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html

### TODO

- Assymetric
- Multi-Region

### TODO (KMS Policy)

- kms default policy
- kms custom policy
- kms kms:CallerAccount
- kms cross account policy - 2nd accountmust have iam policy
- kms:ViaService