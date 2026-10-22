> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-concepts.html
> Downloaded: 2026-10-22

# CloudFormation Hooks concepts

The following terminology and concepts are central to your understanding and use of CloudFormation Hooks. 

## Hook 

A Hook contains code that is invoked immediately before CloudFormation creates, updates, or deletes stacks or specific resources. It can also be invoked during a create change set operation. Hooks can inspect the template, resources, or change set that CloudFormation is about to provision. Additionally, Hooks can be invoked immediately before the Cloud Control API creates, update, or deletes specific resources. 

If a Hook identifies any configurations that don't comply with the organizational guidelines defined in your Hook logic, then you may choose to either `WARN` users or `FAIL`, preventing CloudFormation from provisioning the resource. 

Hooks have the following characteristics:  
Proactive validation – Reduces risk, operational overhead, and cost by identifying non-compliant resources before they're created, updated, or deleted. 
Automatic enforcement – Provides enforcement in your AWS account to prevent non-compliant resources from being provisioned by CloudFormation. 
 

## Failure mode 

Your Hook logic can return success or failure. A success response will allow the operation to continue. A failure for non-compliant resources can result in the following:  
`FAIL` – Stops provisioning operation. 
`WARN` – Allows provisioning to continue with a warning message. 
 

Creating Hooks in `WARN` mode is an effective way to monitor Hook behavior without affecting stack operations. First, activate Hooks in `WARN` mode to understand which operations will be impacted. After you have assessed the potential effects, you can switch the Hook to `FAIL` mode to start preventing non-compliant operations. 

## Hook targets 

Hook targets specify the operations that a Hook will evaluate. These can be operations on:  
Resources supported by CloudFormation (`RESOURCE`)  
Stack templates (`STACK`) 
Change sets (`CHANGE_SET`) 
Resources supported by the Cloud Control API (`CLOUD_CONTROL`)  
 

You define one or more targets that specify the broadest operations that the Hook will evaluate. For example, you can author a Hook targeting `RESOURCE` to target all AWS resources and `STACK` to target all stack templates. 

## Target actions 

Target actions define the specific actions (`CREATE`, `UPDATE`, or `DELETE`) that will invoke a Hook. For `RESOURCE`, `STACK`, and `CLOUD_CONTROL` targets, all target actions are applicable. For `CHANGE_SET` targets, only the `CREATE` action is applicable. 

## Annotations 

GetHookResult responses can return annotations that provide detailed compliance check results and remediation guidance for each evaluated resource. For details on the API's annotation structure, see Annotation in the AWS CloudFormation API Reference. For instructions on viewing these validation results, see View invocation results for CloudFormation Hooks. 

You can encrypt annotations as needed for sensitive compliance information by specifying your own KMS key when configuring the Hook. For more information, see Hook configuration schema syntax reference. For information about setting up the key policy that you need when you specify your KMS key for Hooks, see AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest. Important

Note that the `KmsKeyId` option to specify a customer managed key is currently only available when you use the AWS CLI to configure your Hook. 

## Hook handler 

For custom Hooks, this is the code that handles evaluation. It is associated with a target invocation point and a target action that mark an exact point where a Hook runs. You write handlers that host logic for these specific points. For example, a `PRE` target invocation point with `CREATE` target action makes a `preCreate` Hook handler. Code within the Hook handler runs when a matching target invocation point and service are performing an associated target action. 

Valid values: (`preCreate` | `preUpdate` | `preDelete`) Important

Stack operations that result in the status of `UpdateCleanup` do not invoke a Hook. For example, during the following two scenarios, the Hook's `preDelete` handler is not invoked: 
the stack is updated after removing one resource from the template. 
a resource with the update type of replacement is deleted. 
 

## Timeout and retry limits 

Hooks have a 30-second timeout limit per invocation and are limited to 3 retry attempts. If an invocation exceeds the timeout, we return an error message stating that the Hook execution timed out. After the third retry, CloudFormation marks the Hook execution as failed.
