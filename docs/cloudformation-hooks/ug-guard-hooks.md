> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html
> Downloaded: 2026-10-22

# Guard Hooks

To use an AWS CloudFormation Guard Hook in your account, you must activate the Hook for the account and Region where you want to use it. Activating a Hook makes it usable in stack operations in the account and Region where it's activated. 

When you activate a Guard Hook, CloudFormation creates an entry in your account's registry for the activated Hook as a private Hook. This allows you to set any configuration properties the Hook includes. Configuration properties define how the Hook is configured for a given AWS account and Region.Topics
AWS CLI commands for working with Guard Hooks
Write Guard rules to evaluate resources for Guard Hooks
Prepare to create a Guard Hook
Activate a Guard Hook in your account
View logs for the Guard Hooks in your account
Delete Guard Hooks in your account
 

## AWS CLI commands for working with Guard Hooks 

The AWS CLI commands for working with Guard Hooks include:   
activate-type to start the activation process for a Guard Hook. 
set-type-configuration to specify the configuration data for a Hook in your account. 
list-types to list the Hooks in your account. 
describe-type to return detailed information about a specific Hook or specific Hook version, including current configuration data. 
deactivate-type to remove a previously activated Hook from your account.
