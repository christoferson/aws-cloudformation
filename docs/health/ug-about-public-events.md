> Source: https://docs.aws.amazon.com/health/latest/ug/about-public-events.html
> Downloaded: 2026-10-27

# Monitoring account-specific and public events for AWS Health

When you create an EventBridge rule to monitor events from AWS Health, the rule delivers both account-specific events and public events: 
Account-specific events affect your account and resources, such as an event that tells you about a required update to an Amazon EC2 instance or other scheduled change events. 
Public events appear on the AWS Health Dashboard – Service health. Public events aren't specific to AWS accounts and provide public information about the Regional availability of a service. 
Important

To receive both event types, your rule must use the `"source": [ "aws.health"]` value. Wildcards, such as `"source": [ "aws.health*"]` won't match the pattern to monitor for any events.

You can identify if an event is public or account-specific in EventBridge, by using the eventScopeCode parameter. Events can have the `PUBLIC` or `ACCOUNT_SPECIFIC`. You can also filter your rule on this parameter.

To view an example public event for Amazon Elastic Compute Cloud, see Public Health Event - Amazon EC2 operational issue. 

## Backup rules for AWS Health events 

If you're monitoring public events from an AWS Region, we recommend that you create a back up rule. Public events for AWS Health are sent simultaneously to both the impacted Region and to the backup Region when a valid rule is set in the impacted Region. Important

If you don't have a rule in the impacted Region, the backup Region will not automatically send out the public event as a backup. You must have a valid rule in the impacted Region for public events to be delivered to the backup Region. 

AWS Health sends account-specific events to both the impacted Region and to the backup Region, regardless of any rules configured in the impacted Region. 

We recommend that you deduplicate AWS Health events using `eventARN` and `communicationId` because these values remain consistent for AWS Health messages that are sent to the backup Region.
