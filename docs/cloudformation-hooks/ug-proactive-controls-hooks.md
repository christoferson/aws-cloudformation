> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks.html
> Downloaded: 2026-10-22

# AWS Control Tower proactive controls as Hooks

The AWS Control Tower Control Catalog provides pre-built compliance rules (proactive controls) that you can implement as Hooks. This approach saves setup time and helps you validate resource configurations against AWS best practices across your organization without writing code. 

Proactive controls evaluate AWS resources before deployment, preventing non-compliant resources from being created rather than detecting issues later. They check configurations against established security, operational, and governance standards. 

To get started, simply activate proactive control-based Hooks in your desired account and Region. These Hooks will then evaluate specific target types to ensure compliance with your selected controls. 

For more information about available proactive controls, see the AWS Control Tower Control Catalog.Topics
AWS CLI commands for working with Hooks
Activate a proactive control-based Hook in your account
Delete proactive control-based Hooks in your account
 

## AWS CLI commands for working with Hooks 

The AWS CLI commands for working with proactive control-based Hooks include:   
activate-type to start the activation process for a proactive control-based Hook. 
set-type-configuration to specify the controls to apply to a proactive control-based Hook in your account. 
list-types to list the Hooks in your account. 
describe-type to return detailed information about a specific Hook or specific Hook version, including current configuration data. 
deactivate-type to remove a previously activated Hook from your account.
