
## AWS Health - one catch-all EventBridge rule in US West (Oregon)

[eventbridge-health-catch-all.yaml](eventbridge-health-catch-all.yaml)

### The problem

AWS Health tells you about things that affect **your** resources: EC2 instance retirements, scheduled maintenance, certificate or engine version end-of-life, and operational issues in a Region where you run something. Health events are **Regional**: an event about `eu-central-1` is published to EventBridge in `eu-central-1`. To catch everything, you used to need **one rule in every Region you use**, typically deployed with StackSets.

### What AWS Health does now

Every event is also sent to a **backup Region**:

| Event Region | Also delivered to |
|---|---|
| Any standard-partition Region | **US West (Oregon) `us-west-2`** |
| US West (Oregon) | US East (N. Virginia) `us-east-1` |

So **one rule in `us-west-2`** receives the **account-specific** events of **all** standard Regions. AWS calls this **simplified integration**. The copy carries `detail.backupEvent: "true"`, while the event for `us-west-2` itself has `"false"`.

```
 eu-central-1 event ─┬─► EventBridge eu-central-1 (no rule needed)
                     └─► EventBridge us-west-2  ──► catch-all rules ──► SNS email / SQS
 ap-northeast-1 event ┴─► ...                 ──┘
```

Offline docs: [../../docs/health/README.md](../../docs/health/README.md)

----------------------------------------------------------------------------------

## What one Oregon rule covers, and what it doesn't

| Event type | One rule in us-west-2? | What to do |
|---|---|---|
| **Account-specific** events (`eventScopeCode: ACCOUNT_SPECIFIC`), any Region | **Yes** | This template |
| **Public** events (`PUBLIC`, AWS Health Dashboard service issues) | **No**. A public event goes to the backup Region **only if a rule exists in the impacted Region** | A rule in each Region you care about |
| **Global** events (not Region-specific, for example IAM) | **No** | A rule in **us-east-1** |
| **High availability** (keep working if us-west-2's EventBridge has a problem) | **No**. us-west-2's own backup is us-east-1 | Rules in the event Region **and** the backup Region, plus **de-duplication** |
| Events of **other accounts** in the organization | **No**, a rule only sees its own account | Organizational view in the management or **Health delegated administrator** account, then deploy this stack there |

AWS recommends simplified integration for **action-required account events**. That's exactly what operations teams usually want routed to email, chat or tickets.

### De-duplication

When you combine rules (HA, or a Regional rule plus Oregon), the same message arrives more than once:
- **Dedupe key:** `detail.eventArn` + `detail.communicationId`. Both stay the same across the primary and backup copies.
- **Ignore backups:** to not receive backup copies in a Region at all, filter `detail.backupEvent: ["false"]`.
- **At least once:** Health delivers at least once anyway, so make consumers idempotent.

----------------------------------------------------------------------------------

## What the template creates

| Resource | Purpose |
|---|---|
| `HealthNotifyRule` → SNS email | `source: aws.health` (exact value, wildcards don't match), `detail-type: AWS Health Event`, `eventScopeCode: ACCOUNT_SPECIFIC`, **`page: "1"`**. An input transformer turns the event into one readable line: service, event type, **Region**, category, status, actionability, backup flag, description |
| `HealthRecordRule` → SQS (+ DLQ) | Same events, **all pages**, full JSON. Events with very long `affectedEntities` / `resources` lists are split into pages (same `eventArn` / `communicationId`, `page` / `totalPages`). The rule has a retry policy and a dead-letter queue |
| Topic and queue policies | `events.amazonaws.com`, limited to each rule with `aws:SourceArn` |

### Useful event fields (`detail`)

| Field | Values |
|---|---|
| `eventRegion` | The **impacted** Region (the event's `region` is where it was delivered) |
| `eventTypeCategory` | `issue`, `scheduledChange`, `accountNotification`, `investigation` |
| `statusCode` | `open`, `upcoming`, `closed` |
| `actionability` | `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED`, `INFORMATIONAL` (optional field). Good for routing |
| `backupEvent` | `"true"` = backup copy |
| `affectedAccount`, `affectedEntities`, `service`, `eventTypeCode` | — |

To email only what needs action, add `actionability: ["ACTION_REQUIRED", "ACTION_MAY_BE_REQUIRED"]` to the notify rule's `detail` pattern.

## Deploy

```bash
aws cloudformation create-stack --region us-west-2 --stack-name myapp-dev-health \
  --template-body file://eventbridge-health-catch-all.yaml \
  --parameters ParameterKey=NotificationEmail,ParameterValue=ops@example.com
# confirm the SNS subscription email
```

**Region matters:** in any Region other than us-west-2, the rules only see that Region's own events. You can't send a real Health event to test it. Instead, check the patterns with `aws events test-event-pattern` against the example events in the schema reference ([../../docs/health/ug-aws-health-events-eventbridge-schema.md](../../docs/health/ug-aws-health-events-eventbridge-schema.md)).

The older single-Region example [../eventbridge-rule-health.yaml](../eventbridge-rule-health.yaml) matches only `issue` events, in the Region where it's deployed.

## Docs

- [../../docs/health/ug-choosing-a-region.md](../../docs/health/ug-choosing-a-region.md) (backup Regions, simplified integration, HA, global events)
- [../../docs/health/ug-about-public-events.md](../../docs/health/ug-about-public-events.md) (account-specific vs public, backup rules, de-duplication)
- [../../docs/health/ug-aws-health-events-eventbridge-schema.md](../../docs/health/ug-aws-health-events-eventbridge-schema.md) (all fields, example events)
- [../../docs/health/ug-pagnation-of-health-events.md](../../docs/health/ug-pagnation-of-health-events.md) (pages)
- [../../docs/health/ug-aggregating-health-events.md](../../docs/health/ug-aggregating-health-events.md) (organizational view, delegated administrator)
