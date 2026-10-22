> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-activate-hooks.html
> Downloaded: 2026-10-22

# Activate a proactive control-based Hook in your account

The following topic shows you how to activate a proactive control-based Hook in your account, which makes it usable in the account and Region it was activated in.Important

Before you continue, verify that you have the permissions required to work with Hooks and view proactive controls from the CloudFormation console. For more information, see Grant IAM permissions for CloudFormation Hooks.Topics
Activate a proactive control-based Hook (console)
Activate a proactive control-based Hook (AWS CLI)
 

## Activate a proactive control-based Hook (console) To activate a proactive control-based Hook for use in your account
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where you want to create the Hook in. 
In the navigation pane on the left, choose Hooks. 
On the Hooks page, choose Create a Hook, and then choose With the Control Catalog. 
On the Select controls page, for Proactive controls, select one or more proactive controls to use. 

These controls will automatically apply whenever specified resources are created or updated. Your selection determines which resource types the Hook will evaluate. 
Choose Next. 
For Hook name, choose one of the following options:  
Provide a short, descriptive name that will be added after `Private::Controls::`. For example, if you enter ``MyTestHook``, the full Hook name becomes `Private::Controls::`MyTestHook``. 
Provide the full Hook name (also called an alias) using this format: ``Provider`::`ServiceName`::`HookName``. 
For Hook mode, choose how the Hook responds when controls fail their evaluation:  
Warn — Issues warnings to users but allows actions to continue. This is useful for non-critical validations or informational checks. 
Fail — Prevents the action from proceeding. This is helpful for enforcing strict compliance or security policies. 
Choose Next. 
(Optional) For Hook filters, do the following: 
For Filtering criteria, choose the logic for applying stack name and stack role filters:  
All stack names and stack roles – The Hook will only be invoked when all specified filters match. 
Any stack names and stack roles – The Hook will be invoked if at least one of the specified filters match. 
For Stack names, include or exclude specific stacks from Hook invocations.  
For Include, specify the stack names to include. Use this when you have a small set of specific stacks you want to target. Only the stacks specified in this list will invoke the Hook. 
For Exclude, specify the stack names to exclude. Use this when you want to invoke the Hook on most stacks but exclude a few specific ones. All stacks except those listed here will invoke the Hook. 
For Stack roles, include or exclude specific stacks from Hook invocations based on their associated IAM roles.  
For Include, specify one or more IAM role ARNs to target stacks associated with these roles. Only stack operations initiated by these roles will invoke the Hook. 
For Exclude, specify one or more IAM role ARNs for stacks you want to exclude. The Hook will be invoked on all stacks except those initiated by the specified roles. 
Choose Next. 
On the Review and activate page, review your choices. To make changes, choose Edit on the related section. 
When you're ready to proceed, choose Activate Hook. 
 

## Activate a proactive control-based Hook (AWS CLI) 

Before you continue, confirm that you have identified the proactive controls that you'll use with this Hook. For more information, see the AWS Control Tower Control Catalog. To activate a proactive control-based Hook for use in your account (AWS CLI)
To start activating a Hook, use the following activate-type command, replacing the placeholders with your specific values. 

```
aws cloudformation activate-type --type HOOK \
  --type-name AWS::ControlTower::Hook  \
  --publisher-id aws-hooks \
  --type-name-alias MyOrg::Security::ComplianceHook \
  --region us-west-2
```
To finish activating the Hook, you must configure it using a JSON configuration file. 

Use the cat command to create a JSON file with the following structure. For more information, see Hook configuration schema syntax reference. 

This following example configures a Hook that invokes on specific IAM, Amazon EC2, and Amazon S3 resources during `CREATE` and `UPDATE` operations. It applies three proactive controls (`CT.IAM.PR.5`, `CT.EC2.PR.17`, `CT.S3.PR.12`) to validate these resources against compliance standards. The hook operates in `WARN` mode, meaning it will flag non-compliant resources with warnings but won't block deployments. 

```
$ cat > config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": ["RESOURCE"],
      "FailureMode": "WARN",
      "Properties": {
        "ControlsToApply": "CT.IAM.PR.5,CT.EC2.PR.17,CT.S3.PR.12"
      },
      "TargetFilters": {
        "Actions": [
          "CREATE",
          "UPDATE"
        ]
      }
    }
  }
}
```
`HookInvocationStatus`: Set to `ENABLED` to enable the Hook. 
`TargetOperations`: Set to `RESOURCE` as this is the only supported value for a proactive control-based Hook. 
`FailureMode`: Set to either `FAIL` or `WARN`. 
`ControlsToApply`: Specify the control IDs of the proactive controls to use. For more information, see the AWS Control Tower Control Catalog. 
(Optional) `TargetFilters`: For `Actions`, you can specify `CREATE` or `UPDATE`, or both (default), to control when the Hook is invoked. Specifying `CREATE` alone limits the Hook to `CREATE` operations only. Other `TargetFilters` properties have no effect. 
Use the following set-type-configuration command, along with the JSON file you created, to apply the configuration. Replace the placeholders with your specific values. 

```
aws cloudformation set-type-configuration \
  --configuration file://config.json \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook" \
  --region us-west-2
```
