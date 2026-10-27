> Source: https://docs.aws.amazon.com/health/latest/ug/choosing-a-region.html
> Downloaded: 2026-10-27

# Creating EventBridge rules for AWS Region coverage

You can create an EventBridge rule for each Region that you want to receive AWS Health events for. For example, to receive events from the Europe (Frankfurt) Region, you can create a rule for this Region.

To enhance the reliability of AWS Health notifications, you can set up rules in the dedicated backup Regions. In the standard AWS partition, the US West (Oregon) Region acts as the backup region for all other Regions, while US East (N. Virginia) Region serves as the backup for the US West (Oregon) Region. When health events occur, they are automatically sent to both the primary Region and its designated backup Region. For example, if you're monitoring events in the Europe (Frankfurt) Region, then any health events are delivered to both the Europe (Frankfurt) Region and the US West (Oregon) Region. This system makes sure you continue to receive health notifications even if your primary Region experiences issues. To create a backup rule, follow the procedure for Configuring an EventBridge rule to send notifications about events in AWS Health.

If you prefer not to use backup functionality, then you must add a filter to your backup region rule. For example, implement a filter for `detail.backupEvent = False`. This prevents you from receiving backup events from other regions.

## High availability setup (optional) 

If you want to create an EventBridge integration with high availability, make sure you have implemented rules in both the relevant and backup Regions, and then implement de-duplication using `detail.communicationId`. This makes sure you receive all events while avoiding duplicates. For more information, see Reference: AWS Health events Amazon EventBridge schema. 

## Simplified integration 

If you want to capture account-specific events from multiple AWS Regions, but prefer to configure only a single rule, then simplified integration is the appropriate option. To receive account-specific AWS Health events from all Regions in the standard AWS partition, you can set up a central rule in the US West (Oregon) Region. This single rule automatically aggregates account-specific events from all standard partition Regions. However, you won't have high availability configuration. Note

Simplified integration doesn't allow you to receive public events that are shown in the AWS Health Dashboard. Simplified integration is only recommended for ingesting action-required AWS Health events. For more information about public and account-specific events, see Monitoring account-specific and public events for AWS Health. 

## Global events 

Some AWS Health events are not Region-specific. Events that aren't specific to a Region are called global events. These include events sent for AWS Identity and Access Management (IAM). To receive global events, you must create a rule for the US East (N. Virginia) Region.
