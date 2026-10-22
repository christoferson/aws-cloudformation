> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/doc-history.html
> Downloaded: 2026-10-22

# Document history for the CloudFormation Hooks user guide

The following table describes the important changes to the documentation since the last release of CloudFormation Hooks. For notification about updates to this documentation, you can subscribe to an RSS feed. 
Latest documentation update: September 4, 2025. 

| Change | Description | Date | 
| 

Detailed compliance check results | 

Hooks now support annotations that provide detailed compliance check results and remediation guidance for each evaluated resource. View these detailed validation results through the CloudFormation console or `get-hook-result` CLI command. | 

November 13, 2025 | 
| 

Proactive controls as Hooks | 

You can now activate proactive control-based Hooks through the CloudFormation console or CLI using the `activate-type` and `set-type-configuration` commands. You can configure these Hooks to apply specific AWS Control Tower Control Catalog proactive controls to evaluate resources during `CREATE` and `UPDATE` operations. | 

September 4, 2025 | 
| 

Hooks invocation summary | 

You can now retrieve information about Hook invocations through the CloudFormation console, or use the `list-hook-results` CLI command to programmatically retrieve invocation details. You can also now filter `list-hook-results` results by Hook or invocation status to focus on relevant invocations. | 

September 4, 2025 | 
| 

Stack-level Hooks | 

Hooks are now supported at the stack-level, allowing customers to use CloudFormation Hooks to evaluate new templates and potentially block stack operations from proceeding. | 

November 13, 2024 | 
| 

AWS Cloud Control API Hooks integration | 

Hooks are now integrated with Cloud Control API, allowing customers to use CloudFormation Hooks to proactively inspect the configuration of resources before provisioning. If non-compliant resources are found, the Hook either fails the operation and prevents the resources from being provisioned, or emits a warning and allows the provisioning operation to continue. | 

November 13, 2024 | 
| 

AWS CloudFormation Guard Hooks | 

AWS CloudFormation Guard is an open-source and general purpose domain specific language (DSL) you can use to author policy-as-code. Guard Hooks can evaluate Cloud Control API and CloudFormation operations to inspect the configuration of resources before provisioning. If non-compliant resources are found, the Hook either fails the operation and prevents the resources from being provisioned, or emits a warning and allows the provisioning operation to continue. | 

November 13, 2024 | 
| 

AWS Lambda Hooks | 

AWS CloudFormation Lambda Hooks allow you to evaluate CloudFormation and Cloud Control API operations against custom your own custom code. Your Hook can block an operation from proceeding, or issue a warning to the caller and allow the operation to proceed. | 

November 13, 2024 | 
| 

Hooks User Guide | 

Initial version of the CloudFormation Hooks User Guide. Updates include a new introduction, getting started walkthrough, concepts and terminology, stack level filtering, and updated topics on prerequisites, setup, and CloudFormation Hooks development. | 

December 8, 2023 |
