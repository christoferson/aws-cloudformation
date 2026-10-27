> Source: https://docs.aws.amazon.com/health/latest/ug/creating-event-bridge-events-rule-for-aws-health.html
> Downloaded: 2026-10-27

# Configuring an EventBridge rule to send notifications about events in AWS Health

You can create an Amazon EventBridge rule to programmatically integrate AWS Health events with other services, applications, and workloads. EventBridge provides a drag and drop console interface and an API to set up rules that trigger when a matching AWS Health event is created for your account or organization. To learn how to set up a rule in EventBridge to capture AWS Health events, see Creating rules using the Enhanced Builder and Creating rules using the Advanced Builder in the Amazon EventBridge User Guide.

Depending on your integration, EventBridge allows you to add parameters to the EventBridge rule to filter only the AWS Health events that you want to integrate with your use case. For incident response use cases, you might want to focus on the `issue` event category and certain critical services. For change management use cases such as planned lifecycle events, you might want to focus on AWS Health events with `ACTION_REQUIRED` in the Actionability field. For integrating with security use cases, you might want to focus on all AWS Health Abuse events and AWS Health events with the `SECURITY` persona field.

You can use sample use cases to verify that your rule captures the events you need. Sample use cases are available in Reference: AWS Health events Amazon EventBridge schema. You can also find them in the EventBridge console under the Use Sample events provided option in the Test event pattern - optional panel 

## Using the API or AWS Command Line Interface 

For a new or existing rule, use the PutRule API operation or the `aws events put-rule` command to update the event pattern. To view an example AWS CLI command, see put-rule in the AWS CLI Command Reference. Example: Setting up rules for issues for only the Amazon EC2 service

The following event pattern creates a rule to monitor issue events for the Amazon EC2 service.

```
{
  "detail": {
    "eventTypeCategory": [
      "issue"
    ],
    "service": [
      "EC2"
    ]
  },
  "detail-type": [
    "AWS Health Event"
  ],
  "source": [
    "aws.health"
  ]
}
```
 Example: Setting up rules for all action required AWS Health events, including planned lifecycle events

The following event pattern creates a rule to monitor all AWS Health events that require action, including planned lifecycle events.

```
{
  "detail": {
    "eventTypeCategory": [
      "accountNotification",
      "scheduledChange"
    ],
    "actionability": [
      "ACTION_REQUIRED"
    ]
  },
  "detail-type": [
    "AWS Health Event"
  ],
  "source": [
    "aws.health"
  ]
}
```
 Example: Setting up rules for all AWS Health events for multiple services and event type categories

The following event pattern creates a rule to monitor events for the `issue`, `accountNotification`, and `scheduledChange` event type categories for three AWS services: Amazon EC2 Auto Scaling, Amazon VPC, and Amazon EC2.

```
{
  "detail": {
    "eventTypeCategory": [
      "issue",
      "accountNotification",
      "scheduledChange"
    ],
    "service": [
      "AUTOSCALING",
      "VPC",
      "EC2"
    ]
  },
  "detail-type": [
    "AWS Health Event"
  ],
  "source": [
    "aws.health"
  ]
}
```
