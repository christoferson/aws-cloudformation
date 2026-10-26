
## SQS fair queues - noisy-neighbor protection on a multi-tenant standard queue

[sqs-fair-queue-multi-tenant.yaml](sqs-fair-queue-multi-tenant.yaml)

### The problem

A SaaS app puts work from **all customers into one queue**. Customer A runs a bulk import and drops 5,000 messages into it. Consumers work through A's backlog, so customers B, C and D wait **minutes** for messages that normally take milliseconds. That's the *noisy neighbor*: one tenant raises the **dwell time** (time from send to processing) for everyone.

Classic fixes:
- **A queue per tenant:** lots of queues to manage, scale and poll.
- **Overprovision consumers:** expensive, and auto scaling still reacts too late.

### Fair queues

| | |
|---|---|
| Enable | Producers set **`MessageGroupId` = tenant ID** on messages sent to a **standard** queue. No queue setting, no consumer change, no throughput limit, no extra latency |
| Detection | SQS tracks each tenant's share of **in-flight** messages (> ~10% and ≥ ~30 messages) and of **processing time** (> ~10%) |
| Effect | While a tenant is "noisy", consumers receive the **quiet tenants' messages first**. The noisy tenant's messages are **not dropped or throttled**; they go out whenever there's spare capacity |
| Back to normal | Once the noisy tenant's backlog is consumed, or it has had nothing in flight for 5 minutes |
| Not ordering | On a standard queue, `MessageGroupId` is **only a tenant ID**. Ordering per group is a **FIFO** queue feature |
| Without a group ID | Each such message counts as its own tenant |

```
                   without fair queues                    with fair queues (A detected as noisy)
 queue:   A A A A A A A A A A A A A A B C D        A A A A A A A A A A A A A A B C D
 receive: A A A A A A A A A A A A A A B C D        B C D A A A A A A A A A A A A A A
 dwell:   B, C, D wait for all of A                B, C, D processed right away; A's dwell time rises
```

### When to use it

Use fair queues when **all** of these apply:
- The queue is **multi-tenant**, and each tenant is identifiable (customer, client app, request type).
- The queue has **high throughput**, so one tenant's burst can build a real backlog.
- **Dwell time** matters to your quality of service.

Offline docs: [../../docs/sqs/README.md](../../docs/sqs/README.md)

----------------------------------------------------------------------------------

## What the template creates

| Resource | Why |
|---|---|
| `TenantMessageQueue` | A **plain standard queue** with a dead-letter queue. There's nothing fairness-specific to configure |
| `ProducerLambdaFunction` | Load generator: a **noisy burst first** (default 5,000 messages for `tenant-a`), then 30 messages each for `tenant-b/c/d`. Every message has `MessageGroupId = tenant` |
| `ConsumerLambdaFunction` + event source mapping | `MaximumConcurrency` 10 × `BatchSize` 10 means up to about 100 messages in flight, so one tenant's share can stand out. It sleeps 0.2 s per message and logs `tenant` and `dwellSeconds` as JSON |
| `QuietTenantMessageAgeAlarm` | SLA on **`ApproximateAgeOfOldestMessageInQuietGroups`**. It only fires if *well-behaved* tenants are delayed, not because the noisy tenant's own backlog is old. In that case, scale the consumers |
| `NoisyTenantAlarm` | `ApproximateNumberOfNoisyGroups` ≥ 1 (informational) |
| `FairQueueDashboard` | Queue-wide metrics **next to** their `...InQuietGroups` versions |

### Fair-queue metrics (AWS/SQS, dimension `QueueName`)

| Metric | Compare with |
|---|---|
| `ApproximateNumberOfNoisyGroups` | — |
| `ApproximateNumberOfMessagesVisibleInQuietGroups` | `ApproximateNumberOfMessagesVisible` |
| `ApproximateNumberOfMessagesNotVisibleInQuietGroups` | `ApproximateNumberOfMessagesNotVisible` |
| `ApproximateNumberOfMessagesDelayedInQuietGroups` | `ApproximateNumberOfMessagesDelayed` |
| `ApproximateAgeOfOldestMessageInQuietGroups` | `ApproximateAgeOfOldestMessage` |

During the burst, the whole-queue backlog and age shoot up, while the quiet-tenant lines stay low. That gap shows fairness working. To see *which* tenant is noisy, AWS points to CloudWatch Contributor Insights, and there's a sample on GitHub (linked from the metrics page).

----------------------------------------------------------------------------------

## Deploy and try it

```bash
aws cloudformation create-stack --stack-name myapp-dev-fair-queue \
  --template-body file://sqs-fair-queue-multi-tenant.yaml --capabilities CAPABILITY_IAM

aws lambda invoke --function-name myapp-dev-tenant-producer --cli-binary-format raw-in-base64-out \
  --payload '{"noisyTenant":"tenant-a","noisyCount":5000,"quietTenants":["tenant-b","tenant-c","tenant-d"],"quietCount":30}' out.json
```

After a few minutes, compare dwell time per tenant in **CloudWatch Logs Insights** (log group `/lambda/myapp/dev/tenant-consumer`):

```
fields tenant, dwellSeconds
| stats avg(dwellSeconds) as avgDwell, max(dwellSeconds) as maxDwell, count(*) as messages by tenant
| sort avgDwell desc
```

Expected result: `tenant-a` has a high dwell time (its backlog is worked off over several minutes), while `tenant-b/c/d` stay at a few seconds, even though they were sent **after** the burst. Then look at the dashboard. For a baseline, rerun without `MessageGroupId`: remove it from the producer, and the quiet tenants wait behind the burst.

## Notes

- **Consumer sizing:** in-flight messages ≈ consumer concurrency × batch size. Too few messages in flight, and the concurrency-share check can't single out a tenant (the processing-time check still works).
- **Choosing the tenant ID:** pick a real entity (customer ID, app ID, request type). There's no limit on the number of tenants.
- **Fair queues vs FIFO:** fair queues keep standard-queue semantics (at-least-once, best-effort ordering, nearly unlimited throughput). If you need **ordering per tenant**, use a FIFO queue with `MessageGroupId`. FIFO already interleaves groups, but has FIFO throughput limits.
- **Cost:** sending thousands of demo messages incurs normal SQS request charges.

## Docs

- [../../docs/sqs/ug-sqs-fair-queues.md](../../docs/sqs/ug-sqs-fair-queues.md) (overview, how to use, when to use)
- [../../docs/sqs/ug-sqs-fair-queues-detailed.md](../../docs/sqs/ug-sqs-fair-queues-detailed.md) (detection thresholds, delivery order, consumer capacity)
- [../../docs/sqs/ug-sqs-available-cloudwatch-metrics.md](../../docs/sqs/ug-sqs-available-cloudwatch-metrics.md) (quiet-group and noisy-group metrics)
- [../../docs/sqs/lambda-with-sqs.md](../../docs/sqs/lambda-with-sqs.md) (Lambda event source mapping, maximum concurrency)
