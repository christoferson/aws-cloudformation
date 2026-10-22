> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-activate-hooks.html
> Downloaded: 2026-10-22

# Activate a Lambda Hook in your account

The following topic shows you how to activate a Lambda Hook in your account, which makes it usable in the account and Region it was activated in.Topics
Activate a Lambda Hook (console)
Activate a Lambda Hook (AWS CLI)
Related resources
 

## Activate a Lambda Hook (console) To activate a Lambda Hook for use in your account
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where you want to create the Hook in. 
If you haven't created a Lambda function for the Hook, do the following:  
Open the Functions page on the Lambda console. 
Create the Lambda function that you'll use with this Hook, and then return to this procedure. For more information, see Create Lambda functions to evaluate resources for Lambda Hooks.  
 

If you have already created your Lambda function, proceed to the next step.  
In the navigation pane on the left, choose Hooks. 
On the Hooks page, choose Create a Hook, and then choose With Lambda. 
For Hook name, choose one of the following options:  
Provide a short, descriptive name that will be added after `Private::Lambda::`. For example, if you enter ``MyTestHook``, the full Hook name becomes `Private::Lambda::`MyTestHook``. 
Provide the full Hook name (also called an alias) using this format: ``Provider`::`ServiceName`::`HookName``  
For Lambda function, provide the Lambda function to be used with this Hook. You can use:   
The full Amazon Resource Name (ARN) without a suffix. 
A qualified ARN with a version or alias suffix. 
For Hook targets, choose what to evaluate:  
Stacks — Evaluates stack templates when users create, update, or delete stacks. 
Resources — Evaluates individual resource changes when users update stacks. 
Change sets — Evaluates planned updates when users create change sets. 
Cloud Control API — Evaluates create, update or delete operations initiated by the Cloud Control API. 
For Actions, choose which actions (create, update, delete) will invoke your Hook. 
For Hook mode, choose how the Hook responds when the Lambda function invoked by the Hook returns a `FAILED` response:  
Warn — Issues warnings to users but allows actions to continue. This is useful for non-critical validations or informational checks. 
Fail — Prevents the action from proceeding. This is helpful for enforcing strict compliance or security policies. 
For Execution role, choose the IAM role that the Hook assumes to invoke your Lambda function. You can either allow CloudFormation to automatically create an execution role for you or you can specify a role that you've created.  
Choose Next. 
(Optional) For Hook filters, do the following: 
For Resource filter, specify which resource types can invoke the Hook. This ensures that the Hook is only invoked for relevant resources. 
For Filtering criteria, choose the logic for applying stack name and stack role filters:  
All stack names and stack roles – The Hook will only be invoked when all specified filters match. 
Any stack names and stack roles – The Hook will be invoked if at least one of the specified filters match. 
 Note

For Cloud Control API operations, all Stack names and Stack roles filters are ignored. 
For Stack names, include or exclude specific stacks from Hook invocations.  
For Include, specify the stack names to include. Use this when you have a small set of specific stacks you want to target. Only the stacks specified in this list will invoke the Hook. 
For Exclude, specify the stack names to exclude. Use this when you want to invoke the Hook on most stacks but exclude a few specific ones. All stacks except those listed here will invoke the Hook. 
For Stack roles, include or exclude specific stacks from Hook invocations based on their associated IAM roles.  
For Include, specify one or more IAM role ARNs to target stacks associated with these roles. Only stack operations initiated by these roles will invoke the Hook. 
For Exclude, specify one or more IAM role ARNs for stacks you want to exclude. The Hook will be invoked on all stacks except those initiated by the specified roles. 
Choose Next. 
On the Review and activate page, review your choices. To make changes, choose Edit on the related section. 
When you're ready to proceed, choose Activate Hook. 
 

## Activate a Lambda Hook (AWS CLI) 

Before you continue, confirm that you have created the Lambda function and the execution role that you'll use with this Hook. For more information, see Create Lambda functions to evaluate resources for Lambda Hooks and Create an execution role for a Lambda Hook. To activate a Lambda Hook for use in your account (AWS CLI)
To start activating a Hook, use the following activate-type command, replacing the placeholders with your specific values. This command authorizes the Hook to use a specified execution role from your AWS account. 

```
aws cloudformation activate-type --type HOOK \
  --type-name AWS::Hooks::LambdaHook \
  --publisher-id aws-hooks \
  --execution-role-arn arn:aws:iam::123456789012:role/my-execution-role \
  --type-name-alias Private::Lambda::MyTestHook \
  --region us-west-2
```
To finish activating the Hook, you must configure it using a JSON configuration file. 

Use the cat command to create a JSON file with the following structure. For more information, see Hook configuration schema syntax reference. 

```
$ cat > config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "CLOUD_CONTROL"
      ],
      "FailureMode": "WARN",
      "Properties": {
        "LambdaFunction": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
      },
      "TargetFilters": {
        "Actions": [
          "CREATE",
          "UPDATE",
          "DELETE"
        ]
      }
    }
  }
}
```
`HookInvocationStatus`: Set to `ENABLED` to enable the Hook. 
`TargetOperations`: Specify the operations that the Hook will evaluate. 
`FailureMode`: Set to either `FAIL` or `WARN`. 
`LambdaFunction`: Specify the ARN of the Lambda function. 
`TargetFilters`: Specify the types of actions that will invoke the Hook. 
Use the following set-type-configuration command, along with the JSON file you created, to apply the configuration. Replace the placeholders with your specific values. 

```
aws cloudformation set-type-configuration \
  --configuration file://config.json \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook" \
  --region us-west-2
```
 
 

## Related resources 

We provide template examples that you can use to understand how to declare a Lambda Hook in a CloudFormation stack template. For more information, see AWS::CloudFormation::LambdaHook in the AWS CloudFormation User Guide.
