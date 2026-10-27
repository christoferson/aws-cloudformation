> Source: https://docs.aws.amazon.com/health/latest/ug/aws-health-events-eventbridge-schema.html
> Downloaded: 2026-10-27

# Reference: AWS Health events Amazon EventBridge schema

The following is the schema for AWS Health events. The contents of the details parameter follows in a second table. Sample payloads ares provided after the schema tables. 

## AWS Health event schema AWS Health event schema 
|  Parameter |  Description |  Required |    
|  version |  EventBridge version, currently "0". |  Yes |   
|  id |  The unique identifier for the EventBridge event. |  Yes |   
|  detail-type |  The type of detail. For AWS Health events, supported values are `&AWS Health Event` and `AWS Health Abuse Event` |   Yes |   
|  source |   

The event bus source. For AWS Health events, the supported value is `aws.health`  |  Yes |   
|  account |  The account ID to which the AWS Health event was sent .Note

For organizational views this is a different account than the affected account if it's received in the management account or delegated administrator account. |  Yes |   
|  time |  The time at which the notification was sent to EventBridge. Format: `yyyy-mm-ddThh:mm:ssZ`. |  Yes |   
|  region |  The AWS Region that the notification was delivered to.Note

This field doesn't indicate the impacted Region for this AWS Health event. That information is reported in `detail.eventRegion`. |  Yes |   
|  resources |   

Describes the list of affected resources, if any, within an account. 

This field is empty if there are no resources referenced.  |  No |   
|  detail |  

The section containing details of the AWS Health event, as described in the table immediately following this one. |  Yes |    

### Schema content of the 'details' parameter 

The following table documents the content of the detail parameter in the AWS Health event schema. AWS Health event schema: detail parameter content 
|  'detail' parameter content |  Description |  Required |    
|  eventArn |  The unique identifier for the AWS Health event for the specific Region, including the Region and event ID.Note

An event ARN isn't unique to a specific AWS account or Region. |  Yes |   
|  service |  The AWS service affected by the AWS Health event. For example, Amazon EC2, Amazon Simple Storage Service, Amazon Redshift, or Amazon Relational Database Service.  |  Yes |   
|  eventTypeCode |  The unique identifier for the event type. For example: `AWS_EC2_INSTANCE_NETWORK_MAINTENANCE_SCHEDULED` and `AWS_EC2_INSTANCE_REBOOT_MAINTENANCE_SCHEDULED`. Events that include `MAINTENANCE_SCHEDULED` are generally pushed out approximately two weeks before the start time.Note

All new planned lifecycle events have the event type `AWS_{SERVICE}_PLANNED_LIFECYCLE_EVENT`. |  Yes |   
|  eventTypeCategory |  The category code of the event. The supported values include `issue`, `accountNotification`, `investigation`, and `scheduledChange`. |  Yes |   
|  eventScopeCode |  Indicates whether the AWS Health event is account-specific or public. Supported values are `ACCOUNT_SPECIFIC` or `PUBLIC`. |  Yes |   
|  communicationId |   

A unique identifier for this communication for the AWS Health event. 

Messages with the same communication ID might be backup messages or pages of a single AWS Health event. This identifier can be used with the account ID to help de-duplicate messages. 

With the AWS Health event pagination support, the communication ID includes the page number to keep the communication ID unique across pages, for example, 12345678910-1. For more information, see Viewing paginated lists of AWS Health events on EventBridge.  |  Yes |   
|  startTime |  The start time of the AWS Health event, in the format `DoW, DD, MMM, YYYY, HH:MM:SS TZ`. 

The start time can be in the future for scheduled events.  |  Yes |   
|  endTime |  The end time of the AWS Health event, in the format:`DoW, DD MMM YYYY HH:MM:SS TZ`. 

The end time can't be provided for events scheduled for a future time.  |  No |   
|  lastUpdatedTime |  The last update time for the AWS Health event, in the format `DoW, DD MMM YYYY HH:MM:SS TZ`. |  Yes |   
|  statusCode |   

The status of the AWS Health event. 

Supported values include `open`, `closed`, and `upcoming`.  |  Yes |   
|  eventRegion |  The impacted Region described by this AWS Health event. |  Yes |   
|  eventDescription |   

A section that describes the AWS Health event. This includes fields for language and text to describe the event.  
language – The code for the language used in the AWS Health event. This is typically determined by the Region that the event is published to. For example, in the `us-east-1` Region, this is typically `en_US`. 
latestDescription – Describes the AWS Health event as it is rendered from the AWS Health API and typically appears on the the AWS Health dashboard. Note

For public events, this contains only the latest update and not the entire history of the event. 
  |  Yes |   
|  eventMetadata |   

Additional event metadata that can be provided for the AWS Health event.  
<metadata key 1> – Metadata key-value pair strings: "keystring1": "keyvalue1" 

The key-value pairs for event metadata are determined by the service that sent the AWS Health event. 
  |  No |   
|  affectedEntities |   

An array that describes the resource value and status of affected resources within the AWS Health event.  
entityValue – The resource/entity ID. 
lastUpdatedtime – The time when this resource/entity status was last updated, in the format `DoW, DD MMM YYYY HH:MM:SS TZ`. 
status – The status of the affected resource/entity. Supported values include `IMPAIRED`, `UNIMPAIRED`, `PENDING`, `RESOLVED`, and `UNKNOWN`. 
 Note

For planned lifecycle events, resource state updates are performed asynchronously and periodically, and can have a delay of up to 72 hours in rare occasions. For more information, see What should I expect when I receive a planned lifecycle event notification?.  |  No |   
|  page |  

The page this message represents. For more information, see Viewing paginated lists of AWS Health events on EventBridge.Note

Pagination occurs only on resources. If the 256KB size limit is exceeded for another reason, the communication to fail. |  Yes |   
|  totalPages |  

The total number of pages for this health event. For more information, see Viewing paginated lists of AWS Health events on EventBridge. 

You can use this value to determine whether you received all of the pages of a multi-page communication for an account.  |  Yes |   
|  backupEvent |  This flag filters out backup events in the designated backup region within a partition if customers don't want to leverage redundancy. This value can be true or false. |  Yes |   
|  affectedAccount |  

The account ID of the impacted account. 

This may be different from the value in the `account` field if this health event is sent to an account that is part of an AWS Organizations and is received in the management account or delegated administrator account.  |  Yes |   
|  actionability |  Metadata to activate programmatic determination of which events require action without manual inspection. Possible (single) value can be `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED`, or `INFORMATIONAL`. |  No |   
|  personas |  This list of metadata activates programmatic determination of which stakeholder to route the event to. Possible (multiple) values are `OPERATIONAL`, `SECURITY`, and `BILLING`. |  No |    

## Public Health Event - Amazon EC2 operational issue 

```
{
    "version": "0",
    "id": "7bf73129-1428-4cd3-a780-95db273d1602",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-01-27T09:01:22Z",
    "region": "af-south-1",
    "resources": [],
    "detail": {
        "eventArn": "arn:aws:health:af-south-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_7f35c8ae-af1f-54e6-a526-d0179ed6d68f",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
        "eventTypeCategory": "issue",
        "eventScopeCode": "PUBLIC",
        "communicationId": "01b0993207d81a09dcd552ebd1e633e36cf1f09a-1",
        "startTime": "Fri, 27 Jan 2023 06:02:51 GMT",
        "endTime": "Fri, 27 Jan 2023 09:01:22 GMT",
        "lastUpdatedTime": "Fri, 27 Jan 2023 09:01:22 GMT",
        "statusCode": "open",
        "eventRegion": "af-south-1",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "Current severity level: Operating normally\n\n[RESOLVED] \n\n [03:15 PM PST] We continue see recovery \n\nThe following AWS services were previously impacted but are now operating normally: APPSYNC, BACKUP, EVENTS."
        }],
        "affectedEntities": [],
        "page": "1",
        "totalPages": "1",
        "backupEvent": "false",
        "affectedAccount": "123456789012",
        "personas": ["OPERATIONS"]
    }
}
```
 

## Account-specific AWS Health Event - Elastic Load Balancing API Issue 

```
{
    "version": "0",
    "id": "121345678-1234-1234-1234-123456789012",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2022-06-10T06:27:57Z",
    "region": "ap-southeast-2",
    "resources": [],
    "detail": {
        "eventArn": "arn:aws:health:ap-southeast-2::event/AWS_ELASTICLOADBALANCING_API_ISSUE_90353408594353980",
        "service": "ELASTICLOADBALANCING",
        "eventTypeCode": "AWS_ELASTICLOADBALANCING_API_ISSUE",
        "eventTypeCategory": "issue",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "01b0993207d81a09dcd552ebd1e633e36cf1f09a-1",
        "startTime": "Fri, 10 Jun 2022 05:01:10 GMT",
        "endTime": "Fri, 10 Jun 2022 05:30:57 GMT",
        "statusCode": "open",
        "eventRegion": "ap-southeast-2",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "A description of the event will be provided here"
        }],
        "page": "1",
        "totalPages": "1",
        "backupEvent": "false",
        "affectedAccount": "123456789012",
        "personas": ["OPERATIONS"]
    }
}
```
 

## Account-specific AWS Health Event - backup event for Amazon EC2 Instance Store Drive Performance Degraded 

```
{
    "version": "0",
    "id": "121345678-1234-1234-1234-123456789012",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2022-06-03T06:27:57Z",
    "region": "us-west-2",
    "resources": [
        "i-abcd1111"
    ],
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED_90353408594353980",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED",
        "eventTypeCategory": "issue",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "01b0993207d81a09dcd552ebd1e633e36cf1f09a-1",
        "startTime": "Fri, 3 Jun 2022 05:01:10 GMT",
        "endTime": "Fri, 3 Jun 2022 05:30:57 GMT",
        "statusCode": "open",
        "eventRegion": "us-east-1",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "A description of the event will be provided here"
        }],
        "affectedEntities": [{
            "entityValue": "i-abcd1111"
        }],
        "page": "1",
        "totalPages": "1",
        "backupEvent": "true",
        "affectedAccount": "123456789012",
        "personas": ["OPERATIONS"]
    }
}
```
 

## Account-specific AWS Health Event - Amazon EC2 Instance Retirement 

```
{
    "version": "0",
    "id": "7bf73129-1428-4cd3-a780-95db273d1602",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2026-01-27T01:43:21Z",
    "region": "us-east-1",
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/AWS_EC2_INSTANCE_RETIREMENT_SCHEDULED_90353408594353983",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_INSTANCE_RETIREMENT_SCHEDULED",
        "eventTypeCategory": "scheduledChange",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "1234abc01232a4012345678-1",
        "startTime": "Thu, 27 Aug 2026 13:19:03 GMT",
        "lastUpdatedTime": "Thu, 27 Jan 2026 13:44:13 GMT",
        "statusCode": "open",
        "eventRegion": "us-east-1",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "A description of the event will be provided here"
        }],
        "eventMetadata": {
            "keystring1": "valuestring1",
            "keystring2": "valuestring2",
            "keystring3": "valuestring3",
            "keystring4": "valuestring4",
            "truncated": "true"
        },
        "affectedEntities": [{
            "entityValue": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
            "lastUpdatedTime": "Thu, 26 Jan 2026 19:01:55 GMT",
            "status": "PENDING"
        }],
        "affectedAccount": "123456789012",
        "page": "1",
        "totalPages": "1",
        "backupEvent": "false",
        "personas": ["OPERATIONS"],
        "actionability": "ACTION_REQUIRED"
    }
}
```
 

## Account-specific AWS Health Event - Lambda Planned Lifecycle Event 

```
{
    "version": "0",
    "id": "7bf73129-1428-4cd3-a780-95db273d1602",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-01-27T01:43:21Z",
    "region": "us-west-2",
    "resources": ["arn:lambda-1-101002929", "arn:lambda-1-101002930", "arn:lambda-1-101002931", "arn:lambda-1-101002932"],
    "detail": {
        "eventArn": "arn:aws:health:us-west-2::event/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_90353408594353980",
        "service": "LAMBDA",
        "eventTypeCode": "AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT",
        "eventTypeCategory": "scheduledChange",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "1234abc01232a4012345678-1",
        "startTime": "Thu, 27 Aug 2026 13:19:03 GMT",
        "lastUpdatedTime": "Thu, 27 Jan 2026 13:44:13 GMT",
        "statusCode": "open",
        "eventRegion": "us-west-2",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "A description of the event will be provided here"
        }],
        "eventMetadata": {
            "keystring1": "valuestring1",
            "keystring2": "valuestring2",
            "keystring3": "valuestring3",
            "keystring4": "valuestring4",
            "truncated": "true"
        },
        "affectedEntities": [{
            "entityValue": "arn:lambda-1-101002929",
            "lastUpdatedTime": "Thu, 26 Jan 2026 19:01:55 GMT",
            "status": "PENDING"
        }, {
            "entityValue": "arn:lambda-1-101002930",
            "lastUpdatedTime": "Thu, 26 Jan 2026 19:05:12 GMT",
            "status": "PENDING"
        }, {
            "entityValue": "arn:lambda-1-101002931",
            "lastUpdatedTime": "Thu, 26 Jan 2026 19:07:13 GMT",
            "status": "PENDING"
        }, {
            "entityValue": "arn:lambda-1-101002932",
            "lastUpdatedTime": "Thu, 26 Jan 2026 19:10:59 GMT",
            "status": "RESOLVED"
        }],
        "affectedAccount": "123456789012",
        "page": "1",
        "totalPages": "10",
        "backupEvent": "false",
        "personas": ["OPERATIONS"],
        "actionability": "ACTION_REQUIRED"
    }
}
```
