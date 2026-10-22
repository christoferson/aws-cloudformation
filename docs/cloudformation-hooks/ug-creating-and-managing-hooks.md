> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/creating-and-managing-hooks.html
> Downloaded: 2026-10-22

# Creating and managing CloudFormation Hooks

CloudFormation Hooks provide a mechanism to evaluate your CloudFormation resources before allowing stack creation, modification, or deletion. This feature helps you ensure that your CloudFormation resources comply with your organization's security, operational, and cost optimization best practices.

To create a Hook, you have four options. 
Proactive controls as Hooks – Evaluates resources using proactive controls from the AWS Control Tower Control Catalog. 
Guard Hook – Evaluates resources using an AWS CloudFormation Guard rule. 
Lambda Hook – Forwards requests for resource evaluation to an AWS Lambda function. 
Custom Hook – Uses a custom Hook handler that you manually develop.  
 

**Proactive controls as Hooks** 

To create a Hook from proactive controls, follow these steps: 
Navigate to the CloudFormation console and begin creating a Hook. 
Choose specific controls from the Control Catalog that you want your Hook to evaluate resources against. 

These controls will automatically apply whenever specified resources are created or updated. Your selection determines which resource types the Hook will evaluate. 
Set the Hook mode to either warn users about non-compliance or prevent non-compliant operations. 
Configure optional filters to include or exclude stacks by stack name or stack role. 
After completing the configuration, activate the Hook to begin enforcement. 
  

**Guard Hook** 

To create a Guard Hook, follow these steps: 
Write your resource evaluation logic as a Guard policy rule using the Guard domain-specific language (DSL). 
Store the Guard policy rule in an Amazon S3 bucket. 
Navigate to the CloudFormation console and begin creating a Guard Hook. 
Provide the Amazon S3 path to your Guard rule. 
Choose the specific target types that the Hook will evaluate.   
CloudFormation resources (`RESOURCE`) 
Entire stack templates (`STACK`) 
Change sets (`CHANGE_SET`) 
Cloud Control API resources (`CLOUD_CONTROL`) 
Choose the deployment actions (create, update, delete) that will invoke your Hook. 
Choose how the Hook responds when it fails evaluation. 
Configure optional filters to specify which resource types the Hook should evaluate 
Configure optional filters to include or exclude stacks by stack name or stack role. 
After completing the configuration, activate the Hook to begin enforcement. 
  

**Lambda Hook** 

To create a Lambda Hook, follow these steps: 
Write your resource evaluation logic as a Lambda function. 
Navigate to the CloudFormation console and begin creating a Lambda Hook. 
Provide the Amazon Resource Name (ARN) for your Lambda function. 
Choose the specific target types that the Hook will evaluate.   
CloudFormation resources (`RESOURCE`) 
Entire stack templates (`STACK`) 
Change sets (`CHANGE_SET`) 
Cloud Control API resources (`CLOUD_CONTROL`) 
Choose the deployment actions (create, update, delete) that will invoke your Hook. 
Choose how the Hook responds when it fails evaluation. 
Configure optional filters to specify which resource types the Hook should evaluate 
Configure optional filters to include or exclude stacks by stack name or stack role. 
After completing the configuration, activate the Hook to begin enforcement. 
  

**Custom Hook** 

Custom Hooks are extensions that you register in the CloudFormation registry using the CloudFormation Command Line Interface (CFN-CLI). 

To create a custom Hook, follow these main steps: 
Initiate the project – Generate the files needed to develop a custom Hook. 
Model the Hook – Write a schema that defines the Hook and the handlers that specify the operations that can invoke the Hook. 
Register and activate the Hook – After you have created a Hook, you need to register it in the account and Region where you want to use it and this activates it. 
  

The following topics provide more information for creating and managing Hooks.Topics
Concepts
Proactive controls as Hooks
Guard Hooks
Lambda Hooks
Custom Hooks
