> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/grant-iam-permissions-for-hooks.html
> Downloaded: 2026-10-22

# Grant IAM permissions for CloudFormation Hooks

By default, a brand new user in your AWS account doesn't have permission to manage Hooks using the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS API. To grant users permission, an IAM administrator can create IAM policies. The administrator can then add the IAM policies to roles, and users can assume the roles.

Use the policy examples in this topic to create your own custom IAM policies to give users permissions to work with Hooks. 

To learn how to create an IAM identity-based policy using these example JSON policy documents, see Define custom IAM permissions with customer managed policies in the IAM User Guide.

This topic covers the permissions that are needed to do the following: 
Manage Hooks – Create, modify, and disable Hooks in your account. 
Publish Hooks publicly – Register, test, and publish your custom Hooks to make them available publicly in the CloudFormation registry. 
View invocation results – Access and query the results of Hook invocations in your account. 
View details for an invocation result – Access detailed information and remediation guidance for a specific Hook invocation result in your account. 

As you create your IAM policies, you can find documentation for all of the actions, resources, and condition keys associated with the `cloudformation` service prefix in the Actions, resources, and condition keys for CloudFormation section of the Service Authorization Reference.Topics
Allow a user to manage Hooks
Allow a user to publish custom Hooks publicly
Allow a user to view Hook invocation results
Allow a user to view detailed Hook invocation results
AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest
 

## Allow a user to manage Hooks 

If you need to allow users to manage extensions, including Hooks, without the ability to make them public in the CloudFormation registry, you can use the following example IAM policy. Important

The `ActivateType` and `SetTypeConfiguration` API calls work together to create Hooks in your account. When you grant a user permission to call the `SetTypeConfiguration` API, you automatically grant them the ability to modify and disable existing Hooks. You can't use resource-level permissions to restrict access to this API call. Therefore, ensure that you grant this permission only to authorized users in your account.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:ActivateType",
                "cloudformation:DescribeType",
                "cloudformation:ListTypes",
                "cloudformation:SetTypeConfiguration"
            ],
            "Resource": "*"
        }
    ]
}

```
     

Users who manage Hooks might need some related permissions, for example:   
To view proactive controls from the Control Catalog in the CloudFormation console, the user must have the `controlcatalog:ListControls` permission in an IAM policy.  
To register custom Hooks as private extensions in the CloudFormation registry, the user must have the `cloudformation:RegisterType` permission in an IAM policy. 
 

## Allow a user to publish custom Hooks publicly 

The following example IAM policy focuses specifically on publishing capabilities. Use this policy if you need to allow users to make extensions, including Hooks, available publicly in the CloudFormation registry. Important

Publishing Hooks publicly makes them available to other AWS accounts. Ensure that only authorized users have these permissions and that published extensions meet your organization's quality and security standards.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:DescribePublisher",
                "cloudformation:DescribeTypeRegistration",
                "cloudformation:ListTypes",
                "cloudformation:ListTypeVersions",
                "cloudformation:PublishType",
                "cloudformation:RegisterPublisher",
                "cloudformation:RegisterType",
                "cloudformation:TestType"
            ],
            "Resource": "*"
        }
    ]
}

```
     

## Allow a user to view Hook invocation results 

The IAM permissions needed to view Hook invocation results change depending on the type of information being requested. 

### List Hook invocation results 

To list Hook invocation results, users need different permissions depending on the API request being made.  
To grant permissions to request all Hook results, results for a specific Hook, or results for a specific Hook and invocation status, you must grant access to the `cloudformation:ListAllHookResults` action. 
To grant permissions to request results by specifying a Hook target, you must grant access to the `cloudformation:ListHookResults` action. This permission allows the API caller to specify the `TargetType` and `TargetId` parameters when calling `ListHookResults`. 
 

The following shows an example of a basic permissions policy for listing Hook invocation results. IAM identities (users or roles) with this policy have permission to request all invocation results using all available parameter combinations.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListAllHookResults",
                "cloudformation:ListHookResults"
            ],
            "Resource": "*"
        }
    ]
}

```
     

#### Control which change sets can be specified 

The following example IAM policy grants permissions to the `cloudformation:ListHookResults` action to request results by specifying the target of the Hook. However, it also denies the action if the target is a change set named `example-changeset`.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListHookResults"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "cloudformation:ListHookResults"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudformation:ChangeSetName": "example-changeset"
                }
            }
        }
    ]
}

```
     

#### Control which Hooks can be specified 

The following example IAM policy grants permissions to the `cloudformation:ListAllHookResults` action to request invocation results only when the Hook's ARN is provided in the request. It denies the action for a specified Hook ARN.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListAllHookResults"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "cloudformation:ListAllHookResults"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "cloudformation:TypeArn": "true"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "cloudformation:ListAllHookResults"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "cloudformation:TypeArn": "arn:aws:cloudformation:us-east-1:123456789012:type/hook/MyCompany-MyHook"
                }
            }
        }
    ]
}

```
     

## Allow a user to view detailed Hook invocation results 

To grant permissions to view the detailed results of a specific Hook invocation, you must grant access to the `cloudformation:GetHookResult` action. This permission allows users to retrieve detailed information and remediation guidance for a specific Hook invocation result. For more information, see GetHookResult in the AWS CloudFormation API Reference. 

The following example IAM policy grants permissions to the `cloudformation:GetHookResult` action.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
       "Action": [
         "cloudformation:GetHookResult"
      ],
      "Resource": "*"
    }
  ]
}

```
     Note

You can configure Hooks to encrypt detailed invocation results stored in the cloud with your own AWS KMS keys. For information about how to set up the key policy and IAM permissions that you need when you use a customer managed key for encryption, see AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest.
