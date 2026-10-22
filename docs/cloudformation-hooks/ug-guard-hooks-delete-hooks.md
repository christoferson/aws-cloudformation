> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-delete-hooks.html
> Downloaded: 2026-10-22

# Delete Guard Hooks in your account

When you no longer need an activated Guard Hook, use the following procedures to delete it in your account.

To temporarily disable a Hook instead of deleting it, see Disable and enable CloudFormation Hooks.Topics
Delete a Guard Hook in your account (console)
Delete a Guard Hook in your account (AWS CLI)
 

## Delete a Guard Hook in your account (console) To delete a Guard Hook in your account
Sign in to the AWS Management Console and open the CloudFormation console at https://console.aws.amazon.com/cloudformation.
On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located. 
From the navigation pane, choose Hooks. 
On the Hooks page, find the Guard Hook you want to delete. 
Select the check box next to your Hook and choose Delete.  
When prompted for confirmation, type out the Hook name to confirm deleting the specified Hook and then choose Delete. 
 

## Delete a Guard Hook in your account (AWS CLI) Note

Before you can delete the Hook, you must first disable it. For more information, see Disable and enable a Hook in your account (AWS CLI). 

Use the following deactivate-type command to deactivate a Hook, which removes it from your account. Replace placeholders with your specific values. 

```
aws cloudformation deactivate-type \
  --type-arn "arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook" \
  --region us-west-2
```
