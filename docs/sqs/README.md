
## Amazon SQS - Local Documentation Snapshot

Offline copies of the AWS docs used to build [sqs/sqs-fair-queue](../../sqs/sqs-fair-queue/), converted from HTML to Markdown.
Downloaded 2026-10-27. Each file starts with its source URL. Check the live page if something looks off.

### SQS Developer Guide

| File | Topic |
|---|---|
| [ug-sqs-fair-queues.md](ug-sqs-fair-queues.md) | Fair queues: noisy neighbor, dwell time, enabling with `MessageGroupId`, when to use, metrics overview |
| [ug-sqs-fair-queues-detailed.md](ug-sqs-fair-queues-detailed.md) | How fair queues work: tenant identification, detection thresholds (concurrency share, processing-time share), delivery order, recovery, consumer capacity |
| [ug-sqs-available-cloudwatch-metrics.md](ug-sqs-available-cloudwatch-metrics.md) | CloudWatch metrics, including `ApproximateNumberOfNoisyGroups` and the `...InQuietGroups` metrics |
| [ug-sqs-queue-types.md](ug-sqs-queue-types.md) | Standard vs FIFO queues |
| [ug-standard-queues.md](ug-standard-queues.md) | Standard queues |
| [ug-using-messagegroupid-property.md](ug-using-messagegroupid-property.md) | `MessageGroupId` on FIFO queues (ordering) |

### Lambda and CloudFormation

| File | Topic |
|---|---|
| [lambda-with-sqs.md](lambda-with-sqs.md) | Lambda with SQS (event source mapping, batch size, maximum concurrency) |
| [cfn-aws-resource-sqs-queue.md](cfn-aws-resource-sqs-queue.md) | `AWS::SQS::Queue` (fair queues need no property) |
