## IAM Cloudformation

### Concepts

### IAM - Role

Provision a Role with Role Policy

[iam-role](iam-role.yaml)

### IAM - User Group

Provision a User Group with User Group Policy

[iam-user-group](iam-user-group.yaml)

### IAM - Managed Policy

Provision a custom managed policy

[iam-managed-policy](iam-managed-policy.yaml)

### IAM - Policy Variables

Provision a custom managed policy with Policy Variables.

When using policy variables, you must explicitly specify version 2012-10-17 in the policy. The default version of the IAM policy language, 2008-10-17, does not support policy variables.

- ${!aws:username}

[iam-policy-variable](iam-policy-variable.yaml)

### Errors

- Unresolved resource dependencies [aws:username] in the Resources block of the template
  Use ${!aws:username} instead of ${aws:username} arn:aws:iam::${AWS::AccountId}:user/${!aws:username}

### Resources

https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_IAM.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html

