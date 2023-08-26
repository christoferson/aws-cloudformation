## KMS Cloudformation Template

### Concepts | [doc](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)

#### Key Types

##### Customer managed key

- The KMS keys that you create are customer managed keys. 
- Customer managed keys are KMS keys in your AWS account that you create, own, and manage.

 
##### AWS managed key 

- AWS managed keys are KMS keys in your account that are created, managed, and used on your behalf by an AWS service integrated with AWS KMS.
- You don't have to create or maintain the key or its key policy, and there's never a monthly fee for an AWS managed key.
- you cannot change any properties of AWS managed keys, rotate them, change their key policies, or schedule them for deletion. 
- you cannot use AWS managed keys in cryptographic operations directly; the service that creates them uses them on your behalf. 
- Alias aws/service-name
 
##### AWS owned key

- AWS owned keys are a collection of KMS keys that an AWS service owns and manages for use in multiple AWS accounts. 
- Although AWS owned keys are not in your AWS account, an AWS service can use an AWS owned key to protect the resources in your account.
- AWS owned keys are completely free of charge (no monthly fees or usage fees), they do not count against the AWS KMS quotas for your account, and they're easy to use. 


##### Comparison

<table style="border:1px solid black;border-collapse: collapse;">
  <tr><th>KMS Key Type</th><th>Can view KMS key metadata</th><th>Can manage KMS key</th><th>Used only for my AWS account</th><th>Automatic rotation</th></tr>
  <tr><td>Customer managed key</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Optional. Every year (approximately 365 days)</td></tr>
  <tr><td>AWS managed key</td><td>Yes</td><td>No</td><td>Yes</td><td>Required. Every year (approximately 365 days)</td></tr>
  <tr><td>AWS owned key</td><td>No</td><td>No</td><td>No</td><td>Varies</td></tr>
</table>

 
### Authentication and access control for AWS KMS

- No AWS principal has any permissions to a KMS key unless that permission is provided explicitly and never denied. 
- There are no implicit or automatic permission to use or manage a KMS key. 

- The primary way to manage access to your AWS KMS resources is with policies. 

-  AWS KMS resource policies for KMS keys are called key policies. All KMS keys have a key policy.

- KMS keys belong to the AWS account in which they were created. However, no identity or principal, including the AWS account root user, 
  has permission to use or manage a KMS key unless that permission is explicitly provided in a key policy, IAM policy or grant. 

- The IAM identity who creates a KMS key is not considered to be the key owner and they don't automatically have permission to use or manage the KMS key that they created. 
  Like any other identity, the key creator needs to get permission through a key policy, IAM policy, or grant.

- However, identities who have the kms:CreateKey permission can set the initial key policy and give themselves permission to use or manage the key.

- An AWS KMS key policy is a resource-based policy that controls access to a KMS key. Every KMS key must have a key policy. 

- You can use other authorization mechanism to allow access to the KMS key, but only if the key policy allows it. 
  (You can use an IAM policy to deny access to a KMS key even if the key policy doesn't explicitly permit it.)

- key policies are Regional. A key policy controls access only to a KMS key in the same Region. It has no effect on KMS keys in other Regions.

####  Key policy
– Every KMS key has a key policy. It is the primary mechanism for controlling access to a KMS key. 
You can use the key policy alone to control access, which means the full scope of access to the KMS key is defined in a single document (the key policy).

##### Default key policy when you create a KMS key programmatically

- This default key policy has one policy statement that gives the AWS account that owns the KMS key permission to use IAM policies to allow access to all AWS KMS operations on the KMS key.

##### Default key policy when you create a KMS key with the AWS Management Console

- When you create a KMS key with the AWS Management Console, the key policy begins with the policy statement that allows access to the AWS account and enables IAM policies. The console then adds a key administrators statement, a key users statement, and (for most key types) a statement that allows principals to use the KMS key with other AWS services. 

- Unlike other AWS resource policies, an AWS KMS key policy does not automatically give permission to the account or any of its identities. To give permission to account administrators, the key policy must include an explicit statement that provides this permission, like this one.

- It allows the account to use IAM policies to allow access to the KMS key, in addition to the key policy.
Without this permission, IAM policies that allow access to the key are ineffective, although IAM policies that deny access to the key are still effective.

- It reduces the risk of the key becoming unmanageable by giving access control permission to the account administrators, including the account root user, which cannot be deleted. 

##### Kms Actions [link](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html)

- kms:Create* Allows kms:CreateAlias and kms:CreateGrant. (The kms:CreateKey permission is valid only in an IAM policy.)

- kms:Describe* Allows kms:DescribeKey. The kms:DescribeKey permission is required to view the key details page for a KMS key in the AWS Management Console.

- kms:Enable* Allows kms:EnableKey. For symmetric encryption KMS keys, it also allows kms:EnableKeyRotation.

- kms:List* Allows kms:ListGrants, kms:ListKeyPolicies, and kms:ListResourceTags. (The kms:ListAliases and kms:ListKeys permissions, which are required to view KMS keys in the AWS Management Console, are valid only in IAM policies.)


#### IAM policies 
– You can use IAM policies in combination with the key policy and grants to control access to a KMS key. Controlling access this way enables you to manage all of the permissions for your IAM identities in IAM. To use an IAM policy to allow access to a KMS key, the key policy must explicitly allow it. 


#### Grants 
– You can use grants in combination with the key policy and IAM policies to allow access to a KMS key. Controlling access this way enables you to allow access to the KMS key in the key policy, and to allow identities to delegate their access to others.

### Automatic Key Rotation

- Automatic rotation is optional for customer managed KMS keys.

- When you enable automatic key rotation for a KMS key, AWS KMS generates new cryptographic material for the KMS key every year. 

- AWS KMS supports automatic key rotation only for symmetric encryption KMS keys with key material that AWS KMS creates. 

- AWS KMS always rotates the key material for AWS managed KMS keys every year.

- Rotation of AWS owned KMS keys varies.

- When you use a rotated KMS key to encrypt data, AWS KMS uses the current key material.

- When you use the rotated KMS key to decrypt ciphertext, AWS KMS uses the same version of the key material that was used to encrypt it. You cannot request a particular version of the key material.

- AWS KMS rotates key material one year (approximately 365 days) after rotation is enabled, and then every year (approximately 365 days) thereafter.

#### Customer managed keys

- Because automatic key rotation is optional on customer managed keys and can be enabled and disabled at any time, the rotation date depends on the date that rotation was most recently enabled. 

#### AWS managed keys

- AWS KMS automatically rotates AWS managed keys every year (approximately 365 days). You cannot enable or disable key rotation for AWS managed keys.

- In May 2022, AWS KMS changed the rotation schedule for AWS managed keys from every three years (approximately 1,095 days) to every year (approximately 365 days).

#### AWS owned keys

- You cannot enable or disable key rotation for AWS owned keys. The key rotation strategy for an AWS owned key is determined by the AWS service that creates and manages the key. 

### Manual Key Rotation

When you rotate KMS keys manually, you also need to update references to the KMS key ID or key ARN in your applications. Aliases, which associate a friendly name with a KMS key, can make this process easier. Use an alias to refer to a KMS key in your applications. Then, when you want to change the KMS key that the application uses, instead of editing your application code, change the target KMS key of the alias.

-------------------------------------------------------------------

### KMS - Symmetric

Provision a Symmetric Key with Alias Name. 
Default Key Policy which permits everyone in the account.

[kms-symmetric](kms-symmetric.yaml)

### Resources

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KMS.html
- https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html

- https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html
- https://docs.aws.amazon.com/kms/latest/developerguide/grants.html

### TODO

- Assymetric
- Multi-Region

### TODO (KMS Policy)

- kms default policy
- kms custom policy
- kms kms:CallerAccount
- kms cross account policy - 2nd accountmust have iam policy
- kms:ViaService