> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-view-invocations.html
> Downloaded: 2026-10-22

# View invocation results for CloudFormation Hooks

This topic describes how to view invocation results for CloudFormation Hooks. Viewing invocation results can help you understand how Hooks are evaluating your resources and resolve any issues that are detected when Hooks verify a resource.

Invocations are specific instances when your validation logic (whether it's a AWS Control Tower proactive control, Guard rule, or Lambda function) runs during a resource's lifecycle. 

## View invocation results in the console 

You can view invocation results in the console in three ways: through the Invocation summary page, through the invocation histories for individual Hooks, or through individual stack events for stack-specific invocations. 

### View results for all Hooks 

The Invocation summary page provides a comprehensive view of all Hook invocations across your account and Region for the past 90 days. To view results for all Hooks
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where you want to view Hook invocations. 
From the navigation pane, choose Invocation summary. 
The page displays a list of all Hook invocations from the past 90 days, including:  
Invocation ID 
Hook 
Target 
Mode (`Warn` or `Fail`) 
Result (`Warning`, `Pass`, `Failed`, `In progress`) 
Invocation time 
Result message 
You can filter the list using the search bar at the top of the table to find specific invocations. 
Select a specific invocation to view more addition details about the invocation result, including remediation guidance for failed Hook invocations. 
 

### View invocation history for individual Hooks 

You can also view invocation results through the invocation histories for individual Hooks. To view Hook invocations for a specific Hook
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where you want to view Hook invocations. 
From the navigation pane, choose Hooks. 
Choose the Hook you want to view Hook invocations for. 
Select a specific invocation to view more addition details about the invocation result, including remediation guidance for failed Hook invocations. 
 

### View results for stack-specific invocations 

You can also view invocation results for a specific stack through the stack Events page. To view Hook invocations for a specific stack
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where the stack operation occurred. 
From the navigation pane, choose Stacks. 
Select the stack you want to view Hook invocations for. 
Choose the Stack events tab. 
In the events list, look for events with Hook invocations complete in the Status reason column.  
To view specific Hook invocation details, review the Hook invocations column, and choose the underlined text to open a pop-up window with more detailed information. Note

To display hidden columns, choose the gear icon on the top right corner of the section to open the Preferences modal, update the settings as needed, and choose Confirm. 
 

## View invocation results using the AWS CLI 

Use the list-hook-results command to retrieve information about Hook invocations. This command supports the following filtering options:  
Get all Hook invocation results (no parameters required)  
Filter by Hook ARN (use `--type-arn`) 
Filter by Hook ARN and status (use `--type-arn` and `--status`) 
Search for specific targets (use `--target-type` and `--target-id`) 
 Filter results by Hook ARN 

The following command lists all Hook invocation results for a specific Hook. 

```
aws cloudformation list-hook-results \
  --type-arn arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook \
  --region us-west-2
```
 

Example output: 

```
{
  "HookResults": [
    {
      "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook",
      "HookResultId": "59ef501c-0ac4-47c0-a193-e071cabf748d",
      "TypeName": "MyOrg::Security::ComplianceHook",
      "TypeVersionId": "00000001",
      "HookExecutionTarget": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/39f29d10-73ed-11f0-abc1-0affdfe4aebb",
      "InvokedAt": "2025-08-08T00:18:39.651Z",
      "FailureMode": "WARN",
      "HookStatusReason": "...",
      "InvocationPoint": "PRE_PROVISION",
      "Status": "HOOK_COMPLETE_FAILED"
    },
    ...
  ]
}
```
 

For a description of the fields in the response, see HookResultSummary in the AWS CloudFormation API Reference. Filter results by Hook ARN and status 

To filter for a common status among the results, specify the `--status` option in the command. Valid values are:  
`HOOK_IN_PROGRESS`: The Hook is currently running. 
`HOOK_COMPLETE_SUCCEEDED`: The Hook completed successfully. 
`HOOK_COMPLETE_FAILED`: The Hook completed but failed validation. 
`HOOK_FAILED`: The Hook encountered an error during execution. 
 

```
aws cloudformation list-hook-results \
  --type-arn arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook \ 
  --status HOOK_COMPLETE_FAILED \
  --region us-west-2
```
 

Example output: 

```
{
  "HookResults": [
    {
      "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook",
      "HookResultId": "59ef501c-0ac4-47c0-a193-e071cabf748d",
      "TypeName": "MyOrg::Security::ComplianceHook",
      "TypeVersionId": "00000001",
      "HookExecutionTarget": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/39f29d10-73ed-11f0-abc1-0affdfe4aebb",
      "InvokedAt": "2025-08-08T00:18:39.651Z",
      "FailureMode": "WARN",
      "HookStatusReason": "...",
      "InvocationPoint": "PRE_PROVISION",
      "Status": "HOOK_COMPLETE_FAILED"
    },
    ...
  ]
}
```
 

For a description of the fields in the response, see HookResultSummary in the AWS CloudFormation API Reference. Filter results by target type and target ID 

The following command lists all Hook invocation results for a specific Cloud Control API request. 

```
aws cloudformation list-hook-results \
  --target-type CLOUD_CONTROL \
  --target-id d417b05b-9eff-46ef-b164-08c76aec1801 \
  --region us-west-2
```
 

Example output: 

```
{
  "HookResults": [
    {
      "TargetType": "CLOUD_CONTROL",
      "TargetId": "d417b05b-9eff-46ef-b164-08c76aec1801",
      "HookResults": [
        {
          "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook",
          "HookResultId": "4e7f4766-d8fe-44e5-8587-5b327a148abe",
          "TypeName": "MyOrg::Security::ComplianceHook",
          "TypeVersionId": "00000001",
          "FailureMode": "WARN",
          "HookStatusReason": "...",
          "InvocationPoint": "PRE_PROVISION",
          "Status": "HOOK_COMPLETE_FAILED"
        },
        ...
      ]
    }
  ]
}
```
 

For a description of the fields in the response, see HookResultSummary in the AWS CloudFormation API Reference. Get detailed results for a specific invocation 

Use the get-hook-result command to retrieve detailed information about a specific Hook invocation, including annotations with compliance check results and remediation guidance. 

```
aws cloudformation get-hook-result \
  --hook-result-id 59ef501c-0ac4-47c0-a193-e071cabf748d \
  --region us-west-2
```
 

Example output: 

```
{
  "HookResultId": "59ef501c-0ac4-47c0-a193-e071cabf748d",
  "InvocationPoint": "PRE_PROVISION",
  "FailureMode": "WARN",
  "TypeName": "MyOrg::Security::ComplianceHook",
  "TypeVersionId": "00000001",
  "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook",
  "Status": "HOOK_COMPLETE_FAILED",
  "HookStatusReason": "Hook completed with failed validations",
  "InvokedAt": "2025-08-08T00:18:39.651Z",
  "Target": {
    "TargetType": "RESOURCE",
    "TargetTypeName": "AWS::S3::Bucket",
    "TargetId": "my-s3-bucket",
    "Action": "CREATE"
  },
  "Annotations": [
    {
      "AnnotationName": "BlockPublicAccessCheck",
      "Status": "FAILED",
      "StatusMessage": "Bucket does not block public access",
      "RemediationMessage": "Enable block public access settings on the S3 bucket",
      "SeverityLevel": "HIGH"
    },
    {
      "AnnotationName": "BucketEncryptionCheck", 
      "Status": "PASSED",
      "StatusMessage": "Bucket has encryption configured correctly"
    }
  ]
}
```
 

For a description of the fields in the response, see GetHookResult in the AWS CloudFormation API Reference.
