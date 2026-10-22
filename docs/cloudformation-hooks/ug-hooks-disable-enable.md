> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html
> Downloaded: 2026-10-22

# Disable and enable CloudFormation Hooks

This topic describes how to disable and then re-enable a Hook to temporarily prevent it from being active in your account. Disabling Hooks can be useful when you need to investigate an issue without interference from Hooks. 

## Disable and enable a Hook in your account (console) To disable a Hook in your account
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located. 
From the navigation pane, choose Hooks. 
Choose the name of the Hook you want to disable. 
On the Hook details page, to the right of the Hook's name, choose the Disable button. 
When prompted for confirmation, choose Disable Hook. 
 To re-enable a previously disabled Hook
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located. 
From the navigation pane, choose Hooks. 
Choose the name of the Hook you want to enable. 
On the Hook details page, to the right of the Hook's name, choose the Enable button. 
When prompted for confirmation, choose Enable Hook. 
 

## Disable and enable a Hook in your account (AWS CLI) Important

The AWS CLI commands for disabling and enabling Hooks replace the entire Hook configuration with the values specified in the `--configuration` option. To avoid unintended changes, you must include all existing settings you wish to keep when running these commands. To view the current configuration data, use the describe-type command. To disable a Hook 

Use the following set-type-configuration command and specify `HookInvocationStatus` as `DISABLED` to disable the Hook. Replace the placeholders with your specific values. 

```
aws cloudformation set-type-configuration \
  --configuration "{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "DISABLED", "FailureMode": "FAIL", "TargetOperations": ["STACK","RESOURCE","CHANGE_SET"], "Properties":{}}}}" \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook" \
  --region us-west-2
```
 To re-enable a previously disabled Hook 

Use the following set-type-configuration command and specify `HookInvocationStatus` as `ENABLED` to re-enable the Hook. Replace the placeholders with your specific values. 

```
aws cloudformation set-type-configuration \
  --configuration "{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "ENABLED", "FailureMode": "FAIL", "TargetOperations": ["STACK","RESOURCE","CHANGE_SET"], "Properties":{}}}}" \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook" \
  --region us-west-2
```
 

For more information, see Hook configuration schema syntax reference.
