> Source: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies-ec2_getting-started.html
> Downloaded: 2026-10-23

# Getting started with EC2 policies

EC2 policies let you enforce declarative configurations across accounts in your organization. This topic walks you through the steps to enable, create, and attach EC2 policies. 

## Prerequisites 

Before you begin, make sure you have the required permissions to perform declarative policy tasks. For more information, see Prerequisites for managing declarative policies. 

## Procedure 

For all of these steps, you sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization's management account.  
Enable EC2 policies for your organization. Note

Enabling trusted access is required

You must enable trusted access for Amazon EC2. This creates a read-only service-linked role that generates the account status report of the current configuration for accounts in your organization.

Using the console

If you use the Organizations console, enabling trusted access is part of the process for enabling EC2 policies.

Using the AWS CLI

If you use the AWS CLI, use two separate operations: 
EnablePolicyType – Enables EC2 policies. 
EnableAWSServiceAccess – Enables trusted access. 

For more information about how to enable trusted access for a specific service with the AWS CLI, see AWS services that you can use with AWS Organizations. 
Run the account status report. 
Create an EC2 policy. 
Attach the EC2 policy to your organization's root, OU, or account. 
View the combined effective EC2 policy that applies to an account. 
 

## Additional resources  
EC2 policy syntax and examples
