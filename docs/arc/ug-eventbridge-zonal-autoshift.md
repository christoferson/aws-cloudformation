> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/eventbridge-zonal-autoshift.html
> Downloaded: 2026-10-24

# Using zonal autoshift with Amazon EventBridge

Using Amazon EventBridge, you can set up event-driven rules that monitor your zonal autoshift resources and initiate target actions that use other AWS services. For example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic when a practice run starts for zonal autoshift.

You can create rules in Amazon EventBridge to act on zonal autoshift. An event for zonal autoshift specifies status information about practice runs or autoshifts, for example, when a practice run is started. You can configure zonal autoshift to notify you about zonal autoshift events for resources that you enable for the service.

You can also choose, in addition to or instead of other notifications, to enable autoshift observer notification, which provides a notification event whenever AWS starts an autoshift for a potentially impaired Availability Zone. Autoshift observer notification is separate from notifications that you receive when the traffic for resources that you have enabled for zonal autoshift is shifted away from an Availability Zone. You don't need to configure any resources with zonal autoshift to enable autoshift observer notification. For more information, see Enabling and working with zonal autoshift. 

To capture specific zonal autoshift events that you're interested in, define event-specific patterns that EventBridge can use to detect the events. Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. 

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time, under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see Events and Event Patterns in EventBridge.  

## Monitor a zonal autoshift resource with EventBridge 

With EventBridge, you can create rules that define actions to take when ARC emits events for its resources. For example, you can create a rule that sends an email message when a practice run starts for zonal autoshift.  

To type or copy and paste an event pattern into the EventBridge console, select to the option to use Enter my own option in the console. To help you determine event patterns that might be useful for you, this topic includes examples of both zonal autoshift event-matching patterns  and zonal autoshift events that you can use.  To create a rule for a resource event
Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
Choose the AWS Region that you want to create the rule in, that is the Region that you're interested in watching events for. 
Choose Create rule. 
Enter a Name for the rule, and, optionally, a description. 
For Event bus, leave the default value, default. 
Choose Next. 
For the Build event pattern step, for Event source, leave the default value, AWS events. 
Under Sample event, choose Enter my own. 
For Sample events, type or copy and paste an event pattern. 
 

## Example zonal autoshift event patterns 

Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. 

You can copy and paste event patterns from this section into EventBridge to create rules that you can use to monitor zonal autoshift actions and resources. 

When you create event patterns for zonal autoshift events, you can specify any of the following for the `detail-type`:  
`Autoshift In Progress`
`Autoshift Completed`
`Practice Run Started`
`Practice Run Succeeded`
`Practice Run Interrupted`
`Practice Run Failed`
`FIS Experiment Autoshift In Progress`
`FIS Experiment Autoshift Completed`
`FIS Experiment Autoshift Canceled`
`Manual Shift Started`
`Manual Shift Updated`
`Manual Shift Canceled`
 

When a practice run is interrupted, for more information about what caused the interruption, see the `additionalFailureInfo` field. 

You can choose to monitor all AWS autoshifts by enabling autoshift observer notifications. After you enable autoshift observer notification, to receive the notifications, choose to be notified for the zonal autoshift detail type `Autoshift In Progress`. To see the steps for enabling autoshift observer notification, see Enabling and working with zonal autoshift. 

For examples, see the Example zonal autoshift events section.  
Select all events from zonal autoshift where an autoshift has started. 

Note the following:  
If you have autoshift observer notification enabled, ARC returns all autoshift events. 
If you do not have autoshift observer notification enabled, ARC returns autoshift events only when a resource that you have configured for zonal autoshift is included in an autoshift.
 

```
{
    "source": [
        "aws.arc-zonal-shift"
    ],
    "detail-type": [
        "Autoshift In Progress"
    ]
}
```
Select all events from zonal autoshift where a practice run has started. 

```
{
    "source": [
        "aws.arc-zonal-shift"
    ],
    "detail-type": [
        "Practice Run Started"
    ]
}
```
Select all events from zonal autoshift where a practice run has failed. 

```
{
    "source": [
        "aws.arc-zonal-shift"
    ],
    "detail-type": [
        "Practice Run Failed"
    ]
}
```
 
 

## Example zonal autoshift events 

This section includes example events for zonal autoshift actions. 

The following is an example event for the `Autoshift In Progress` action, when 1) autoshift observer notification is enabled and 2) you have not configured a resource with zonal autoshift that is included in an autoshift: 

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":"AWS has started an autoshift for an impaired Availability Zone. This notification 
            is separate from autoshift notifications for resources, if any, that you have configured for 
            zonal autoshift. For details, see the Developer Guide."
        }
    }
}
```
 

The following is an example event for the `Autoshift In Progress` action, when 1) autoshift observer notification is disabled and 2) you have configured a resource with zonal autoshift that is included in an autoshift: 

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```
 

The following is an example event for the `Practice Run Interrupted` action: 

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Practice Run Interrupted",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": {
            "additionalFailureInfo": "Practice run interrupted. The blocking alarm entered ALARM state."
        },
        "metadata": {
            "awayFrom": "use1-az2"
        }
    }
}
```
 

The following is an example event for the `FIS Experiment Autoshift In Progress` action: 

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "FIS Experiment Autoshift In Progress",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```
 

The following is an example event for the `Manual Shift Started` action. It is emitted when the `StartZonalShift` API is called on a resource: 

```
{
    "version": "0",
    "id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4",
    "detail-type": "Manual Shift Started",
    "source": "aws.arc-zonal-shift",
    "account": "111122223333",
    "time": "2023-11-16T23:38:14Z",
    "region": "us-east-1",
    "resources": [
        "TEST-EXAMPLE-2023-11-16-23-28-11-5"
    ],
    "detail": {
        "version": "0.0.1",
        "data": "",
        "metadata": {
            "awayFrom": "use1-az2",
            "notes":""
        }
    }
}
```
 

## Specify a CloudWatch log group to use as a target 

When you create an EventBridge rule, you must specify the target where events that are matched to the rule are sent. For a list of available targets for EventBridge, see Targets available in the EventBridge console. One of the targets that you can add to an EventBridge rule is an Amazon CloudWatch log group. This section describes the requirements for adding CloudWatch log groups as targets, and provides a procedure for adding a log group when you create a rule. 

To add a CloudWatch log group as a target, you can do one of the following:  
Create a new log group 
Choose an existing log group
 

If you specify a new log group using the console when you create a rule, EventBridge automatically creates the log group for you. Make sure that the log group that you use as a target for the EventBridge rule starts with `/aws/events`. If you want to choose an existing log group, be aware that only log groups that start with `/aws/events` appear as options in the drop-down menu. For more information, see Create a new log group in the Amazon CloudWatch User Guide. 

If you create or use a CloudWatch log group to use as a target using CloudWatch operations outside of the console, make sure that you set permissions correctly. If you use the console to add a log group to an EventBridge rule, then the resource-based policy for the log group is updated automatically. But, if you use the AWS Command Line Interface or an AWS SDK to specify a log group, then you must update resource-based policy for the log group. The following example policy illustrates the permissions that you must define in a resource-based policy for the log group:  

**JSON**   

****  

```
{
    "Version":"2012-10-17",

    "Statement": [
        {
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "events.amazonaws.com",
                    "delivery.logs.amazonaws.com"
                ]
            },
            "Resource": "arn:aws:logs:us-east-1:222222222222:log-group:/aws/events/*:*",
            "Sid": "TrustEventsToStoreLogEvent"
        }
    ]
}

```
     

You can't configure a resource-based policy for a log group by using the console. To add the required permissions to a resource-based policy, use the CloudWatch PutResourcePolicy API operation. Then, you can use the  describe-resource-policies CLI command to check that your policy was applied correctly. To create a rule for a resource event and specify a CloudWatch log group target
Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
Choose the AWS Region that you want to create the rule in. 
Choose Create rule and then enter any information about that rule, such as the event pattern or schedule details. 

For more information about creating EventBridge rules for ARC, see the sections earlier in this topic. 
On the Select target page, choose CloudWatch as your target.
Choose a CloudWatch log group from the drop-down menu.
