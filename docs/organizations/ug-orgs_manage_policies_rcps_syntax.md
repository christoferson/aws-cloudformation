> Source: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_syntax.html
> Downloaded: 2026-10-20

# RCP syntax

Resource control policies (RCPs) use a similar syntax to that used by resource-based policies. For more information about IAM policies and their syntax, see Overview of IAM Policies in the IAM User Guide.

An RCP is structured according to the rules of JSON. It uses the elements that are described in this topic.Note

All characters in your RCP count against its maximum size. The examples in this guide show the RCPs formatted with extra white space to improve their readability. However, to save space if your policy size approaches the maximum size, you can delete any white space, such as space characters and line breaks that are outside quotation marks.

For general information about RCPs, see Resource control policies (RCPs). 

## Elements summary 

The following table summarizes the policy elements that you can use in RCPs. Note

The effect of `Allow` is only supported for the `RCPFullAWSAccess` policy

The effect of `Allow` is only supported for the `RCPFullAWSAccess` policy. This policy is automatically attached to the organization root, every OU, and every account in your organization, when you enable resource control policies (RCPs). You cannot detach this policy. This default RCP allows all principals and actions access to pass through RCP evaluation, meaning until you start creating and attaching RCPs, all your existing IAM permissions continue to operate as they did. This does not grant access.  
|  Element |  Purpose |    
|  Version |  Specifies the language syntax rules to use for processing the policy. |   
|  Statement |  Serves as the container for policy elements. You can have multiple statements in RCPs. |   
|  Statement ID (Sid) |  (Optional) Provides a friendly name for the statement. |   
|  Effect |  Defines whether the RCP statement denies access to the resources in an account. |   
|  Principal |  Specifies the principal that is allowed or denied access to resources in an account. |   
|   

Action  |   

Specifies AWS service and actions that the RCP allows or denies.  |   
|  Resource |  Specifies the AWS resources that the RCP applies to. |   
|  NotResource |   

Specifies the AWS resources that are exempt from the RCP. Used instead of the `Resource` element.  |   
|  Condition |  Specifies conditions for when the statement is in effect. |    Topics
Version element
Statement element
Statement ID (Sid) element
Effect element
Principal element
Action element
Resource and NotResource elements
Condition element
Unsupported elements
 

## `Version` element 

Every RCP must include a `Version` element with the value `"2012-10-17"`. This is the same version value as the most recent version of IAM permission policies. 

For more information, see IAM JSON Policy Elements: Version in the IAM User Guide. 

## `Statement` element 

An RCP consists of one or more `Statement` elements. You can have only one `Statement` keyword in a policy, but the value can be a JSON array of statements (surrounded by [ ] characters). 

The following example shows a single statement that consists of single `Effect`, `Principal`, `Action`, and `Resource` elements. 

```
 {
    "Statement": {
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:PutBucketPublicAccessBlock",
        "Resource": "*"
    }
}
```
 

For more information, see IAM JSON Policy Elements: Statement in the IAM User Guide. 

## Statement ID (`Sid`) element 

The `Sid` is an optional identifier that you provide for the policy statement. You can assign a `Sid` value to each statement in a statement array. The following example RCP shows a sample `Sid` statement.  

```
{
    "Statement": {
        "Sid": "DenyBPAConfigurations",
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:PutBucketPublicAccessBlock",
        "Resource": "*"
    }
}
```
 

For more information, see IAM JSON Policy Elements: Sid in the IAM User Guide. 

## `Effect` element 

Each statement must contain one `Effect` element. Using the value of `Deny` in the `Effect` element, you can restrict access to specific resources or define conditions for when RCPs are in effect. For RCPs that you create, the value must be `Deny`. For more information, see RCP evaluation and IAM JSON Policy Elements: Effect in the IAM User Guide. 

## `Principal` element 

Each statement must contain the `Principal` element. You can only specify “`*`” in the `Principal` element of an RCP. Use the `Conditions` element to restrict specific principals. 

For more information, see IAM JSON Policy Elements: Principal in the IAM User Guide. 

## `Action` element 

Each statement must contain the `Action` element. 

The value for the `Action` element is a string or list (a JSON array) of strings that identify AWS services and actions that are allowed or denied by the statement. 

Each string consists of the abbreviation for the service (such as "s3", "sqs", or "sts"), in all lowercase, followed by a colon and then an action from that service. Generally, they are all entered with each word starting with an uppercase letter and the rest lowercase. For example: `"s3:ListAllMyBuckets"`. 

You also can use wildcard characters such as asterisk (*) or question mark (?) in an RCP:  
Use an asterisk (*) as a wildcard to match multiple actions that share part of a name. The value `"s3:*"` means all actions in the Amazon S3 service. The value `"sts:Get*"` matches only the AWS STS actions that begin with "Get". 
Use the question mark (?) wildcard to match a single character.  
 Note

You must specify a service in the Action element of a customer managed RCP

In a customer managed RCP, you can't use `"*"` as the entire `Action` value. This wildcard by itself matches all actions in all services, which is not permitted. You must specify the abbreviation for a service (such as `"s3"`, `"sqs"`, or `"sts"`). After the service, you can use the asterisk (*) wildcard to match actions within that service—for example, `"s3:*"` matches all Amazon S3 actions, and `"s3:Get*"` matches all Amazon S3 actions that begin with "Get." The question mark (?) wildcard matches a single character. 

For a list of the services that support RCPs, see List of AWS services that support RCPs. For a list of the actions an AWS service supports, see Actions, Resources, and Condition Keys for AWS Services in the Service Authorization Reference. 

For more information, see IAM JSON Policy Elements: Action in the IAM User Guide. 

## `Resource` and `NotResource` elements 

Each statement must contain the `Resource` or `NotResource` element. 

You can use wildcard characters such as asterisk (*) or question mark (?) in the resource element:  
Use an asterisk (*) as a wildcard to match multiple resources that share part of a name.  
Use the question mark (?) wildcard to match a single character. 
 

For more information, see IAM JSON Policy Elements: Resource and see IAM JSON Policy Elements: NotResource in the IAM User Guide. 

## `Condition` element 

 You can specify a `Condition` element in deny statements in an RCP.   

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}

```
     

This RCP denies access to Amazon S3 operations and resources unless the request occurs over secure transport (the request was sent over TLS).  

For more information, see IAM JSON Policy Elements: Condition in the IAM User Guide. 

## Unsupported elements 

The following elements are not supported in RCPs:  
`NotPrincipal` 
`NotAction`
