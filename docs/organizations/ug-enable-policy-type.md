> Source: https://docs.aws.amazon.com/organizations/latest/userguide/enable-policy-type.html
> Downloaded: 2026-10-20

# Enabling a policy type

Before you can create and attach a policy to your organization, you must enable that policy type for use. Enabling a policy type is a one-time task on the organization root. You can enable a policy type from only the organization's management account or a member account designated as a delegated administrator.Minimum permissions

To enable a policy type, you need permission to run the following actions: 
`organizations:EnablePolicyType` 
`organizations:DescribeOrganization` – required only when using the Organizations console 
`organizations:ListRoots` – required only when using the Organizations console 
 

**AWS Management Console** To enable a policy type
Sign in to the AWS Organizations console. You must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization’s management account. 
On the Policies page, choose the name of the policy type that you want to enable. 
On the policy type page, choose Enable `policy type`. 

The page is replaced by a list of the available policies of the specified type. 
  

**AWS CLI & AWS SDKs** To enable a policy type 

You can use one of the following commands to enable a policy type:  
AWS CLI: enable-policy-type 

The following example shows how to enable backup policies for your organization. Note that you must specify the ID of your organization's root. 

```
$ aws organizations enable-policy-type \
    --root-id r-a1b2 \
    --policy-type BACKUP_POLICY
{
    "Root": {
        "Id": "r-a1b2",
        "Arn": "arn:aws:organizations::123456789012:root/o-aa111bb222/r-a1b2",
        "Name": "Root",
        "PolicyTypes": [
            {
                "Type": "BACKUP_POLICY",
                "Status": "ENABLED"
            }
        ]
    }
}
```
 

The list of `PolicyTypes` in the output now includes the specified policy type with the `Status` of `ENABLED`. 
AWS SDKs: EnablePolicyType
