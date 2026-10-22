> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-prepare-to-create-hook.html
> Downloaded: 2026-10-22

# Prepare to create a Lambda Hook

Before you create a Lambda Hook, you must complete the following prerequisites: 
You must have already created a Lambda function. For more information, see the Create Lambda functions for Hooks. 
The user or role that creates the Hook must have sufficient permissions to activate Hooks. For more information, see Grant IAM permissions for CloudFormation Hooks. 
To use the AWS CLI or an SDK to create a Lambda Hook, you must manually create an execution role with IAM permissions and a trust policy to allow CloudFormation to invoke a Lambda Hook.  
 

## Create an execution role for a Lambda Hook 

A Hook uses an execution role for the permissions that it requires to invoke that Hook in your AWS account. 

This role can be created automatically if you create a Lambda Hook from the AWS Management Console; otherwise, you must create this role yourself. 

The following section shows you how to set up permissions to create your Lambda Hook.  

### Required permissions 

Follow the guidance at Create a role using custom trust policies in the IAM User Guide to create a role with a custom trust policy. 

Then, complete the following steps to set up your permissions: 
Attach the following minimum privilege policy to the IAM role you want to use to create the Lambda Hook.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
    }
  ]
}

```
Give your Hook permission to assume the role by adding a trust policy to the role. The following shows an example trust policy you can use.  

**JSON**   

****  

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "hooks.cloudformation.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

```
