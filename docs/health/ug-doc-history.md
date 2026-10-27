> Source: https://docs.aws.amazon.com/health/latest/ug/doc-history.html
> Downloaded: 2026-10-27

# Document history for AWS Health

The following table describes the documentation for this release of AWS Health. 
API version: 2016-08-04 

The following table describes important updates to the AWS Health documentation, beginning in August 28, 2020. You can subscribe to the RSS feed to receive notifications about the updates.
| Change | Description | Date | 
| 

Added FAQ page for supported protocols | 

Added a new FAQ page with answers to common questions about the AWS JSON and Smithy RPC v2 CBOR wire protocols. For more information, see  FAQs on supported protocols. | 

October 6, 2026 | 
| 

Added the version catalog | 

Added a new page that describes the version catalog for AWS Health, which provides a service-wide view of supported versions and their timelines. For more information, see Version catalog for AWS Health. | 

October 2, 2026 | 
| 

Clarified that public events aren't available through AWS User Notifications | 

Added callouts to clarify that public events aren't available through AWS managed notifications in AWS User Notifications. To receive public events, you must create an Amazon EventBridge rule or a User-configured notification (UCN). For more information, see Public event. | 

August 26, 2026 | 
| 

Added a note about resource state update timing for planned lifecycle events | 

Added a note to clarify that resource state updates for planned lifecycle events are performed asynchronously and can have a delay of up to 72 hours in rare occasions. For more information, see Reference: AWS Health events Amazon EventBridge schema. | 

August 26, 2026 | 
| 

Clarified Region coverage for simplified integration | 

Updated the simplified integration section to clarify that a single-Region rule aggregates only account-specific events, not public events. Public events are delivered only to the impacted Region and its backup Region. For more information, see Simplified integration. | 

July 2, 2026 | 
| 

Added end of support notice for AWS Service Management Connector | 

Added an end of support notice to the Service Management Connector integration section. AWS will end support for AWS Service Management Connector on March 31, 2027. For more information, see AWS Service Management Connector end of support. | 

April 28, 2026 | 
| 

Updated Configuring an EventBridge rule to send notifications about events in AWS Health | 

Simplified the procedure for creating EventBridge rules by linking to the Amazon EventBridge User Guide for general rule creation steps. The topic now focuses on AWS Health-specific filtering and use cases. For more information, see Configuring an EventBridge rule to send notifications about events in AWS Health. | 

March 13, 2026 | 
| 

Updated AWS Health events Amazon EventBridge schema examples | 

Updated the schema examples to include personas and actionability fields. Examples include Public Health Event for Amazon EC2 operational issue, Account-specific events for Elastic Load Balancing API Issue and Amazon EC2 Instance Store Drive Performance Degraded backup event, and Lambda Planned Lifecycle Event. For more information, see Reference: AWS Health events Amazon EventBridge schema. | 

March 13, 2026 | 
| 

Updated Manage AWS Health notifications in AWS User Notifications | 

Updated information to this section to reflect the migration of AWS Health events to AWS User Notifications. For more information, see Manage AWS Health notifications in AWS User Notifications. | 

December 22, 2025 | 
| 

Updated Monitoring account-specific and public events for AWS Health | 

Added information to this section detailing backup rule behavior for public events and account-specific events. For more information, see Backup rules for AWS Health events. | 

December 11, 2025 | 
| 

Added information about the Actionability and Personas fields for Health events | 

Added information for the Actionability and Personas fields in the Concepts for AWS Health section and the Schema content of the 'details' parameter in the Reference: AWS Health events Amazon EventBridge schema section. For more information, see Concepts for AWS Health and Reference: AWS Health events Amazon EventBridge schema. | 

November 20, 2025 | 
| 

Updated section: Creating EventBridge rules for AWS Region coverage | 

Updated information to create EventBridge rules. For more information, see Creating EventBridge rules for AWS Region coverage. | 

November 3, 2025 | 
| 

Updated section: Manage AWS Health notifications in AWS User Notifications | 

Updated information for the steps to Configure your AWS managed notifications subscription for AWS Health events . For more information, see Manage AWS Health notifications in AWS User Notifications. | 

September 16, 2025 | 
| 

Updated section: Monitoring events in AWS Health with Amazon EventBridge | 

Updated information in note for AWS Health delivers events to EventBridge. For more information, see Monitoring events in AWS Health with Amazon EventBridge. | 

September 15, 2025 | 
| 

Updated section: AWS Health Dashboard | 

Removed optional steps to subscribe to RSS feed for health events. Added note that to receive notifications for health events, customers can use EventBridge. For more information, see AWS Health Dashboard . | 

August 15, 2025 | 
| 

Updated section: Monitoring events in AWS Health with Amazon EventBridge | 

Removed the topic, Installing a service-linked role to use AWS Incident Detection and Response in Monitoring events in AWS Health with Amazon EventBridge  | 

August 8, 2025 | 
| 

Updated section: Monitoring events in AWS Health with Amazon EventBridge | 

Added information to the Notes section indicating that there might be a lag of up to one hour before you start to receive notifications for Public Health Events. For more information, see Monitoring events in AWS Health with Amazon EventBridge | 

July 22, 2025 | 
| 

Updated section: Enabling organizational view | 

Added information to the Notes section indicating that AWS Health automatically aggregates all historical health events across your organization when you enable organizational view. Historical events might take up to 24 hours to appear in your organizational view. For more information, see Enabling organizational view | 

June 27, 2025 | 
| 

Updated section: Aggregating AWS Health events across accounts | 

Removed note that AWS Health doesn't show events that occurred before you enabled organizational view. For more information, see Aggregating AWS Health events across accounts | 

June 27, 2025 | 
| 

WorkDocs deprecated | 

Removed references to deprecated WorkDocs in Planned lifecycle events for AWS Health. | 

June 19, 2025 | 
| 

Added note for AWS managed notifications migration timeline | 

Added a note regarding key dates for the email migration to AWS managed notifications in AWS User Notifications. For more information, see Manage AWS Health notifications in AWS User Notifications. | 

April 28, 2025 | 
| 

Updated planned lifecycle events | 

Updated planned lifecycle events to indicate that AWS Health events remain open for 4 years rather than 90 days for unresolved resources. For more information, see the What should I expect when I receive a planned lifecycle event notification? section in Planned lifecycle events for AWS Health. | 

April 18, 2025 | 
| 

Updated the description of the Affected resources list for planned lifecycle events | 

The Affected resources list for planned lifecycle events usually refreshes once every 24 hours, but might take up to 72 hours to reflect the current resource status. For more information, see the Event details section in Viewing your account events in the AWS Health Dashboard. | 

April 7, 2025 | 
| 

Added an FAQ for managing AWS Health notifications in AWS User Notifications | 

For more information, see Manage notifications in AWS User Notifications FAQ. | 

February 18, 2025 | 
| 

Added information regarding IPv6-only requests to endpoints. | 

For more information, see Choosing endpoints for AWS Health API requests. | 

January 28, 2025 | 
| 

Manage AWS Health notifications in AWS User Notifications | 

For more information, see Manage notifications in AWS User Notifications. | 

January 16, 2025 | 
| 

Corrected JSON in Monitoring AWS Health events with Amazon EventBridge | 

For more information, see Monitoring AWS Health events with Amazon EventBridge. | 

September 3, 2024 | 
| 

Updated information on downloading affected resources | 

For more information, see Affected resources view. | 

July 27, 2024 | 
| 

Removed Internetwork traffic privacy from the Security section AWS Health documentation | 

For more information, see Security in AWS Health. | 

March 27, 2024 | 
| 

Updated the AWS Health Dashboard – Service health and Planned lifecycle events for AWS Health documentation. | 

For more information, see AWS Health Dashboard – Service health and Planned lifecycle events for AWS Health. | 

February 15, 2024 | 
| 

Removed a duplicate bullet point in Creating an EventBridge rule for AWS Health | 

Removed a duplicate bullet point in Creating an EventBridge rule for AWS Health. | 

December 4, 2023 | 
| 

Added documentation for Planned Lifecycle Events | 

For more information, see Planned Lifecycle Events for AWS Health. | 

October 31, 2023 | 
| 

Updated documentation for AWSHealthFullAccess | 

You can now use the `AWSHealthFullAccess` managed policy in the AWS GovCloud (US) Regions. See AWS managed policies for AWS Health. | 

October 16, 2023 | 
| 

Added documentation for configuring AWS User Notifications in AWS Health. | 

You can now configure AWS User Notifications in AWS Health. For more information, see Configure AWS User Notifications for AWS Health. | 

August 30, 2023 | 
| 

Added documentation for the delegated administrator feature to the Aggregating AWS Health events section. | 

For more information, see Delegated administrator organizational view. | 

July 27, 2023 | 
| 

SLR policy update | 

Update to AWS managed policy: Health_OrganizationsServiceRolePolicy. For more information, see AWS managed policies for AWS Health. | 

July 19, 2023 | 
| 

AWS Health schema now supports event metadata | 

You can now receive event metadata from AWS Health events. For more information, see Monitoring AWS Health events with Amazon EventBridge. | 

June 20, 2023 | 
| 

Updated documentation for Amazon EventBridge | 

You can now use an Amazon EventBridge rule to monitor both account-specific and public events. For more information, see Monitoring AWS Health events with Amazon EventBridge. | 

May 2, 2023 | 
| 

Added documentation for AWS managed policies | 

Added documentation for the AWS managed policies for AWS Health and Using service-linked roles for AWS Health. | 

January 18, 2023 | 
| 

Added time zone setting documentation | 

Use the new time zone feature to view the AWS Health Dashboard in your local time zone or in UTC. For more information, see Getting started with your AWS Health Dashboard – Your account health and the AWS Health Dashboard – Service health. | 

September 21, 2022 | 
| 

Updated documentation | 

Added documentation for AWS Health Aware. For more information, see AWS Health Aware. | 

May 25, 2022 | 
| 

Updated documentation | 

The Service Health Dashboard and the AWS Personal Health Dashboard have been rebranded to the AWS Health Dashboard.

For more information, see Getting started with your AWS Health Dashboard – Your account health and the AWS Health Dashboard – Service health. | 

February 28, 2022 | 
| 

Updated documentation for Amazon EventBridge | 

New topic for AWS Health to use Amazon EventBridge to monitor for Health events. For more information, see Monitoring AWS Health events with Amazon EventBridge. | 

February 3, 2022 | 
| 

Updated documentation | 

If you have an Enterprise On-Ramp Support plan, you can use the AWS Health API. | 

November 24, 2021 | 
| 

Added documentation | 

New topic for AWS Health concepts. For more information, see Concepts for AWS Health. | 

July 29, 2021 | 
| 

Updated documentation for CloudWatch Events | 

Added a section about how to create a rule for multiple services and event type categories. For more information, see Creating a rule for multiple services and categories. | 

May 7, 2021 | 
| 

Updated documentation for CloudWatch Events | 

Updated the section to automate AWS Systems Manager actions for Amazon CloudWatch Events rules. For more information, see Automating actions for Amazon EC2 instances. | 

April 28, 2021 | 
| 

Updated documentation for CloudWatch Events | 

Added a section to receive AWS Health events in your chat client. For more information, see Receiving AWS Health events with Amazon Q Developer in chat applications. | 

March 16, 2021 | 
| 

Updated documentation | 

The following topics are updated: 
Updated the Aggregating AWS Health events topic 
Reorganized and updated the Monitor for AWS Health events with Amazon CloudWatch Events topic 
Updated the Resource- and action-based conditions section 
 | 

January 29, 2021 | 
| 

Added the AWS Health Dashboard for organizational view in the AWS Health console | 

You can use the AWS Health console to enable the organizational view feature. You can then view health events for member accounts in your AWS organization. | 

December 14, 2020 | 
| 

High availability endpoint demo | 

You can use the example code to determine the active regional endpoint and signing AWS Region for AWS Health. | 

October 22, 2020 | 
| 

Updates to the AWS Health User Guide | 

Organization updates and added an RSS feed so that you can subscribe for the latest updates to the AWS Health documentation. | 

August 28, 2020 |  

## Earlier updates  
|  Change |  Description |  Date |    
|  Updated the organizational view topic to include examples. |  See Aggregating AWS Health events across accounts. |  June 3, 2020 |   
|  Security and AWS Health |  Added information about security considerations when using AWS Health. See Security in AWS Health. |  May 5, 2020 |   
|  Added new section to explain how to use organizational view to events aggregated across all accounts in AWS Organizations. |  See Aggregating AWS Health events across accounts. |  December 18, 2019 |   
|  Added new section "Resource- and Action-based Conditions" to explain Events restrictions vended by the AWS Health API. |  See Identity and access management for AWS Health. |  August 2, 2018 |   
|  Added a note about the visibility of AWS Health information. |  See Identity and access management for AWS Health. |  August 16, 2017 |   
|  Service release. |  AWS Health released. |  December 1, 2016 |
