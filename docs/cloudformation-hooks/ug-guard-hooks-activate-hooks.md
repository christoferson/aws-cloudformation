> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-activate-hooks.html
> Downloaded: 2026-10-22

# Activate a Guard Hook in your account

The following topic shows you how to activate a Guard Hook in your account, which makes it usable in the account and Region it was activated in.Topics
Activate a Guard Hook (console)
Activate a Guard Hook (AWS CLI)
Related resources
 

## Activate a Guard Hook (console) To activate a Guard Hook for use in your account
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where you want to create the Hook in. 
In the navigation pane on the left, choose Hooks. 
On the Hooks page, choose Create a Hook, and then choose With Guard. 
If you haven't created any Guard rules yet, create your Guard rule, store it in Amazon S3, and then return to this procedure. Refer to the example rules in Write Guard rules to evaluate resources for Guard Hooks to get started. 

If you have already created your Guard rule and stored it in S3, proceed to the next step.  Note

The object stored in S3 must have one of the following file extensions: `.guard`, `.zip`, or `.tar.gz`. 
For Guard Hook source, Store your Guard rules in S3, do the following:  
For S3 URI, specify the S3 path to your rules file or use the Browse S3 button to open a dialog box to browse for and select the S3 object. 
(Optional) For Object version, if your S3 bucket has versioning enabled, you can select a specific version of the S3 object.  

The Guard Hook downloads your rules from S3 every time the Hook is invoked. To prevent accidental changes or deletions, we recommend using a version when configuring your Guard Hook. 
(Optional) For S3 bucket for Guard output report, specify an S3 bucket to store the Guard output report. This report contains the results of your Guard rule validations. 

To configure the output report destination, choose one of the following options:  
Select the Use the same bucket my Guard rules are stored in check box to use the same bucket where your Guard rules are located. 
Choose a different S3 bucket name for storing the Guard output report. 
(Optional) Expand Guard rule input parameters, and then provide the following information under Store your Guard rule input parameters in S3:  
For S3 URI, specify the S3 path to a parameter file or use the Browse S3 button to open a dialog box to browse for and select the S3 object. 
(Optional) For Object version, if your S3 bucket has versioning enabled, you can select a specific version of the S3 object.  
Choose Next. 
For Hook name, choose one of the following options:  
Provide a short, descriptive name that will be added after `Private::Guard::`. For example, if you enter ``MyTestHook``, the full Hook name becomes `Private::Guard::`MyTestHook``. 
Provide the full Hook name (also called an alias) using this format: ``Provider`::`ServiceName`::`HookName``  
For Hook targets, choose what to evaluate:  
Stacks — Evaluates stack templates when users create, update, or delete stacks. 
Resources — Evaluates individual resource changes when users update stacks. 
Change sets — Evaluates planned updates when users create change sets. 
Cloud Control API — Evaluates create, update or delete operations initiated by the Cloud Control API. 
For Actions, choose which actions (create, update, delete) will invoke your Hook. 
For Hook mode, choose how the Hook responds when rules fail their evaluation:  
Warn — Issues warnings to users but allows actions to continue. This is useful for non-critical validations or informational checks. 
Fail — Prevents the action from proceeding. This is helpful for enforcing strict compliance or security policies. 
For Execution role, choose the IAM role that the Hook assumes to retrieve your Guard rules from S3 and optionally write a detailed Guard output report back. You can either allow CloudFormation to automatically create an execution role for you or you can specify a role that you've created.  
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
 

## Activate a Guard Hook (AWS CLI) 

Before you continue, confirm that you have created the Guard rule and the execution role that you'll use with this Hook. For more information, see Write Guard rules to evaluate resources for Guard Hooks and Create an execution role for a Guard Hook. To activate a Guard Hook for use in your account (AWS CLI)
To start activating a Hook, use the following activate-type command, replacing the placeholders with your specific values. This command authorizes the Hook to use a specified execution role from your AWS account. 

```
aws cloudformation activate-type --type HOOK \
  --type-name AWS::Hooks::GuardHook \
  --publisher-id aws-hooks \
  --type-name-alias Private::Guard::MyTestHook \
  --execution-role-arn arn:aws:iam::123456789012:role/my-execution-role \
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
        "STACK",
        "RESOURCE",
        "CHANGE_SET"
      ],
      "FailureMode": "WARN",
      "Properties": {
        "ruleLocation": "s3://amzn-s3-demo-bucket/MyGuardRules.guard",
        "logBucket": "amzn-s3-demo-logging-bucket",
        "options": {
          "inputParams": "s3://amzn-s3-demo-bucket/MyInputParams.json"
        }
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
`ruleLocation`: Replace with the S3 URI where your rule is stored. The object stored in S3 must have one of the following ﬁle extensions: `.guard`, `.zip`, and `.tar.gz`. 
`logBucket`: (Optional) Specify the name of an S3 bucket for Guard JSON reports. 
`options.inputParams`: (Optional) Specify the S3 URI of a JSON or YAML file containing input parameters for your Guard rules. You can specify a single S3 URI or an array of up to 10 S3 URIs. 
`TargetFilters`: Specify the types of actions that will invoke the Hook. 
Use the following set-type-configuration command, along with the JSON file you created, to apply the configuration. Replace the placeholders with your specific values. 

```
aws cloudformation set-type-configuration \
  --configuration file://config.json \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook" \
  --region us-west-2
```
 
 

## Related resources 

We provide template examples that you can use to understand how to declare a Guard Hook in a CloudFormation stack template. For more information, see AWS::CloudFormation::GuardHook in the AWS CloudFormation User Guide.
