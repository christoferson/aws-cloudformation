> Source: https://docs.aws.amazon.com/inspector/latest/user/configure-cicd-account.html
> Downloaded: 2026-10-19

# Setting up an AWS account to use the Amazon Inspector CI/CD integration

 To use the Amazon Inspector CI/CD integration, you must sign up for an AWS account. The AWS account must have an IAM role that grants your CI/CD pipleline access to the Amazon Inspector Scan API. Complete the tasks in the following topics to sign up for an AWS account, create an administrator user, and configure an IAM role for CI/CD integration. Note

 If you already signed up for an AWS account, you can skip to Configure an IAM role for CI/CD integration. Topics
Sign up for an AWS account
Configure an IAM role for CI/CD integration
 

## Sign up for an AWS account 

To get started with AWS, you need an AWS account. For information about creating an AWS account, see Getting started with an AWS account in the AWS Account Management Reference Guide. 

## Configure an IAM role for CI/CD integration 

To integrate Amazon Inspector scanning into your CI/CD pipeline you need to create an IAM policy that allows access to the Amazon Inspector Scan API that scans the software bill of materials (SBOMs). Then, you can attach that policy to an IAM role that your account can assume to run the Amazon Inspector Scan API. 
Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/. 
In the navigation pane of the IAM console, Policies and then choose Create Policy. 
In Policy Editor select JSON and paste the following statement:  

**JSON**   

****  

```

{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "inspector-scan:ScanSbom",
            "Resource": "*"
        }
    ]
}

```
Choose Next. 
Give the policy a name, for example `InspectorCICDscan-policy`, and add an optional description, then choose Create Policy. This policy will be attached to the role you’ll create in the next steps. 
In the navigation pane of the IAM console, select Roles and then select Create New Role. 
For Trusted entity type choose Custom trust policy and paste the following policy:  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}

```
Choose Next. 
In Add permissions search for and select the policy you created earlier, then choose Next. 
Give the role a name, for example `InspectorCICDscan-role`, and add an optional description, then choose `Create Role`.
