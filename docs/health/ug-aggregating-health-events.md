> Source: https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html
> Downloaded: 2026-10-27

# Aggregating AWS Health events using organizational view and delegated administrator access

AWS Health supports organizational view and delegated administrator access for AWS Health events published on Amazon EventBridge. When organizational view is turned on in AWS Health, then the management account or a delegated administrator account receives a single feed of AWS Health events from all accounts within your organization in AWS Organizations.

This feature is designed to provide a centralized view to help manage AWS Health events across your organization. Setting up organizational view and an EventBridge rule in the management account doesn't deactivate EventBridge rules for other accounts in your organization. 

For more information on enabling organizational view and delegated administrator access on AWS Health, see Aggregating AWS Health Events.
