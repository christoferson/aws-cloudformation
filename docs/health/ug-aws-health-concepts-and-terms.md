> Source: https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html
> Downloaded: 2026-10-27

# Concepts for AWS Health

Learn about AWS Health concepts and understand how you can use the service to maintain the health of your applications, services, and resources in your AWS account.Topics
AWS Health event
AWS Health Dashboard
Event type code
Event type categories
Event status
Actionability
Personas
Affected entities
AWS Health events on Amazon EventBridge
AWS Health API
Organizational view
AWS User Notifications
 

## AWS Health event 

AWS Health events, also known as Health events, are notifications that AWS Health sends on behalf of other AWS services. You can use these events to learn about upcoming or scheduled changes that might affect your account. For example, AWS Health can send an event if AWS Identity and Access Management (IAM) plans to deprecate a managed policy or AWS Config plans to deprecate a managed rule. AWS Health also sends events when there are service availability issues in an AWS Region. You can review the event description to understand the issue, identify any affected resources, and take any recommended actions. 

There are two types of Health events: Contents
Account-specific event
Public event
 

### Account-specific event 

Account-specific events are local to either your AWS account or an account in your AWS organization. For example, if there's an issue with an Amazon Elastic Compute Cloud (Amazon EC2) instance type in a Region that you use, AWS Health provides information about the event and the name of the affected resources.  

You can find account-specific events from your AWS Health Dashboard, the AWS Health API, or use Amazon EventBridge or AWS User Notifications to receive notifications. 

### Public event 

Public events are reported service events that aren't specific to an account. For example, if there's a service issue for Amazon Simple Storage Service (Amazon S3) in the US East (Ohio) Region, AWS Health provides information about the event, even if you don't use that service or have S3 buckets in that Region. We recommend that you review public notifications before you take action on them. 

You can find public events from your AWS Health Dashboard and the AWS Health Dashboard – Service health. Important

Public events are not available through AWS managed notifications in AWS User Notifications. To receive public events, you must create an Amazon EventBridge rule or a User-configured notification (UCN) within AWS User Notifications. For more information, see Monitoring events in AWS Health with Amazon EventBridge and Managing notifications in AWS User Notifications. 

If you have an account, see Getting started with your AWS Health Dashboard. 

If you don't have an account, see AWS Health Dashboard. 

## AWS Health Dashboard 

If you have an AWS account, your AWS Health Dashboard shows both public events and account-specific events. 

We recommend that you use your AWS Health Dashboard to learn about events that provide general awareness, such as an upcoming maintenance issue for a service in a Region. You can also use the AWS Health Dashboard to learn about events that might affect you directly, such as a deprecated resource in your account. 

You can sign in to the AWS Management Console to view your AWS Health Dashboard at https://health.aws.amazon.com/health/home.  

For more information, see Getting started with your AWS Health Dashboard. 

### AWS Health Dashboard – Service health 

If you don't have an account, you can use the AWS Health Dashboard – Service health at https://health.aws.amazon.com/health/status to view public events. Public events are reported service issues for AWS that provide information about service availability. This website only shows public events, which aren’t specific to any account. You don't need to sign in or have an account to view this page. 

For more information, see AWS Health Dashboard. 

## Event type code 

The event type codes shown in a Health event include the affected service and the type of event. For example, if you receive a Health event that has the `AWS_EC2_SYSTEM_MAINTENANCE_EVENT` event type code, this means that the service is scheduling a maintenance event that might affect you. Use this information to plan ahead or take action for your account. 

## Event type categories 

All Health events have an associated event type category. For some events, the event type category might appear in the event type code, such as the `AWS_RDS_MAINTENANCE_SCHEDULED` code. In this example, the category is scheduled. You can use this information to understand event categories at a high level. 

It's a best practice that you monitor all event type categories. Note that each category appears for different types of events. You can also use the DescribeEventTypes API operation to find the event type category.   

**Account notification**  

These events provide information about the administration or security of your accounts and services. These events might be informative, or they might require urgent action from you. We recommend that you pay attention for these types of events and review all recommended actions. 

The following are example event type codes for account notifications:  
`AWS_S3_OPEN_ACCESS_BUCKET_NOTIFICATION` – You have an Amazon S3 bucket that might allow public access. 
`AWS_BILLING_SUSPENSION_NOTICE` – Your account has outstanding charges and has been suspended, or you deactivated your account. 
`AWS_WORKSPACES_OPERATIONAL_NOTIFICATION` – There’s a service issue for Amazon WorkSpaces. 
  

**Issue**  

These events are unexpected events that affect AWS services or resources. Common events in this category include communications about operational issues that are causing service degradation, or localized resource-level issues for your awareness. 

The following are example event type codes for issues:  
`AWS_EC2_OPERATIONAL_ISSUE` – An operational issue for a service, such as delays in using a service. 
`AWS_EC2_API_ISSUE` – An operational issue for a service's API, such as increased latency for an API operation. 
`AWS_EBS_VOLUME_ATTACHMENT_ISSUE` – A localized resource-level issue that might affect your Amazon Elastic Block Store (Amazon EBS) resources. 
`AWS_ABUSE_PII_CONTENT_REMOVAL_REPORT` – This event means that your account might be suspended if you don't take action. 
  

**Scheduled change**  

These events provide information about upcoming changes to your services and resources. These events include planned lifecycle events such as end-of-support notifications and auto-upgrades for different versions. Some events might recommend that you take action to avoid service disruptions, while others will occur automatically without any action on your part. Your resource might be temporarily unavailable during the scheduled change activity. All events in this category are account-specific events. 

The following are example event type codes for scheduled changes:  
`AWS_EC2_INSTANCE_RETIREMENT_SCHEDULED` – An Amazon EC2 instance requires a reboot. 
`AWS_SAGEMAKER_SCHEDULED_MAINTENANCE` – SageMaker AI requires a maintenance event, such as fixing a service issue. 
`AWS_RDS_PLANNED_LIFECYCLE_EVENT` – Amazon RDS is scheduling a planned lifecycle event, such as an end-of-support event for one of its versions, which requires customer action. 
 Tip

If you use the AWS Health API or the AWS Command Line Interface (AWS CLI) to return event details, the `Event` object contains the `eventScopeCode` field with the `ACCOUNT_SPECIFIC` value. For more information, see the AWS Health API Reference.   

## Event status 

The event status tells you if the Health event is open, closed, or upcoming. You can view Health events in the AWS Health Dashboard or the AWS Health API for up to 90 days. 

## Actionability 

Actionability is a field that helps you prioritize Health events based on whether an action is required from you. Health events include an actionability status that indicates if you need to take action to mitigate risks to your AWS resources or if the event is informational in nature. 

The actionability field can contain one of the following values:  
`ACTION_REQUIRED`: Events with this status require action from you to mitigate potential impact related to availability, billing, or security of your AWS resources.
`ACTION_MAY_BE_REQUIRED`: Events with this status communicate changes that require action, based on your specific implementation, dependencies, and workflows. These events require your review to determine if action is needed. 
`INFORMATIONAL`: Events with this status provide ongoing visibility into operational information about the AWS services that you use. No immediate action is expected. 
 Note

Health events related to service issues don't include an actionability label, as the need for recovery actions depends on your specific application architecture. 

## Personas 

The personas field provides a list of contacts that helps you route relevant information to appropriate teams within your organization. Each Health event can include one or more of the following personas:  
`OPERATIONS`: For events related to operational activities and service availability.
`SECURITY`: For events related to security considerations.
`BILLING`: For events with potential cost implications.
 

For example, when AWS sends an event about the end of standard support that converts into extended support, the event includes `BILLING` in addition to `OPERATIONS` within the persona list to help make sure the information reaches teams responsible for cost management. 

## Affected entities 

Affected entities are AWS resources that might be affected by the event. For example, if you receive a scheduled event for Amazon EC2 maintenance for a specific instance type that you're using in your account, you can use the Health event to determine the ID of the affected instances. Use this information to address any potential service issue, such as creating or deprecating resources. 

## AWS Health events on Amazon EventBridge 

You can setup Amazon EventBridge rules for your accounts to automate actions after the appropriate AWS Health event is received by an account. These can be general actions, such as sending all planned lifecycle event messages to a chat interface. Or, they can be specific actions, such as triggering a workflow in an IT service management tool. 

For more information, see Monitoring events in AWS Health with Amazon EventBridge.  

## AWS Health API 

You can use the AWS Health API to programmatically access the information that appears in the AWS Health Dashboard, such as the following:  
Get information about events that might affect your AWS services and resources 
Enable or disable the organizational view feature for your AWS organization 
Filter your events by specific services, event type categories, and event type codes 
 

For more information, see the AWS Health API Reference.  Note

You must have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan from AWS Support to use the AWS Health API. If you call the AWS Health API from an account that doesn't have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, you receive a `SubscriptionRequiredException` error.  

## Organizational view 

You can use this feature to aggregate all health events for AWS accounts in your AWS Organizations into a single view in the AWS Health Dashboard. You can then sign in to the management account of your organization or use the AWS Health API to view all events that might affect the different accounts and resources. You can enable this feature from the AWS Health console or API. For more information, see Aggregating AWS Health events across accounts. 

## AWS User Notifications 

AWS Health integrates with AWS User Notifications so that you can easily receive and control notifications about events affecting your AWS accounts and services. User Notifications offers managed notifications for AWS Health events by default. You can configure these subscriptions to control how often you receive messages through time-based aggregation, what kinds of AWS Health events you get notified about, and where notifications are delivered. To get started, open User Notifications in the AWS Management Console. For more information, see Manage AWS Health notifications in AWS User Notifications
