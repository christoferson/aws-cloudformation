
## AWS Health (EventBridge) - Local Documentation Snapshot

Offline copies of the AWS docs used to build [eventbridge/eventbridge-health](../../eventbridge/eventbridge-health/), converted from HTML to Markdown.
Downloaded 2026-10-27. Each file starts with its source URL. Check the live page if something looks off.

### AWS Health User Guide

| File | Topic |
|---|---|
| [ug-cloudwatch-events-health.md](ug-cloudwatch-events-health.md) | Monitoring Health events with EventBridge (at-least-once, targets) |
| [ug-choosing-a-region.md](ug-choosing-a-region.md) | **Region coverage**: backup Regions (us-west-2 for all, us-east-1 for us-west-2), HA setup, **simplified integration** (one rule in us-west-2), global events (us-east-1) |
| [ug-about-public-events.md](ug-about-public-events.md) | Account-specific vs public events, backup rules, de-duplication (`eventArn` + `communicationId`) |
| [ug-aws-health-events-eventbridge-schema.md](ug-aws-health-events-eventbridge-schema.md) | Event schema (`eventRegion`, `eventScopeCode`, `backupEvent`, `actionability`, `personas`, `page`, ...) and example events |
| [ug-pagnation-of-health-events.md](ug-pagnation-of-health-events.md) | Paginated events (> 256 KB), filter on `detail.page` |
| [ug-aggregating-health-events.md](ug-aggregating-health-events.md) | Organizational view and delegated administrator for EventBridge |
| [ug-enable-organizational-view.md](ug-enable-organizational-view.md) | Enabling organizational view |
| [ug-delegated-administrator-organizational-view.md](ug-delegated-administrator-organizational-view.md) | Delegated administrator |
| [ug-creating-event-bridge-events-rule-for-aws-health.md](ug-creating-event-bridge-events-rule-for-aws-health.md) | Creating a rule for Health events |
| [ug-cloud-watch-events-integration.md](ug-cloud-watch-events-integration.md) | Configuring EventBridge (getting started) |
| [ug-aws-health-concepts-and-terms.md](ug-aws-health-concepts-and-terms.md) | Concepts: event, event type, category, account-specific / public |
| [ug-doc-history.md](ug-doc-history.md) | Document history |

### Amazon EventBridge User Guide

| File | Topic |
|---|---|
| [eb-transform-target-input.md](eb-transform-target-input.md) | Input transformer (JSON paths incl. array indices, string / JSON templates) |
| [eb-rule-dlq.md](eb-rule-dlq.md) | Rule target dead-letter queues and their SQS permissions |
