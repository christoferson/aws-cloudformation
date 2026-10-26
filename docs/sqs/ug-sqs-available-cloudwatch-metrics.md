> Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html
> Downloaded: 2026-10-27

# Available CloudWatch metrics for Amazon SQS

Amazon SQS sends the following metrics to CloudWatch.Note

For some metrics, the result is approximate because of the distributed architecture of Amazon SQS. In most cases, the count should be close to the actual number of messages in the queue. 

## Amazon SQS metrics 

Amazon SQS automatically publishes operational metrics to Amazon CloudWatch under the `AWS/SQS` namespace. These metrics help you monitor queue health and performance. Due to SQS’s distributed nature, many values are approximate, but accurate enough for most operational decisions. Note 
All metrics emit non-negative values only when the queue is active. 
Some metrics (such as `SentMessageSize`) are not emitted until at least one message is sent. 
  
|  Metric |  Description |  Units |  Reporting behavior |  Key notes |    
|  `ApproximateAgeOfOldestMessage` |  The age of the oldest unprocessed message in the queue. |  

Seconds |  Reported if the queue contains at least one active message. |   
For standard queues, if a message is received three or more times and not deleted, SQS moves it to the back of the queue. The metric then reflects the age of the next message that hasn’t exceeded the receive threshold. This reordering occurs even when a redrive policy is in place. 
Poison-pill messages (those repeatedly received but never deleted) are excluded from this metric until successfully processed. 
When a message is moved to a DLQ after exceeding the `maxReceiveCount`, the age resets. In that case, the DLQ’s metric reflects the time the message was moved—not when it was originally sent. 
FIFO queues don't reorder messages to preserve order. A failed message blocks its message group until it's deleted or expires. If a DLQ is configured, the message is sent there after the receive threshold is met. 
 |   
|  `ApproximateNumberOfGroupsWithInflightMessages` |  For FIFO only. The number of message groups with one or more in-flight messages. |  

Count |  Reported if the FIFO queue is active. |   
A message is considered in-flight after it’s received from the queue by a consumer but not yet deleted or expired. 
This metric helps you troubleshoot and optimize FIFO queue throughput. High values usually indicate strong concurrency. 
If the queue has a large backlog and this value remains low, consider scaling consumers or increasing the number of active message groups. 
For throughput and in-flight limits, see Amazon SQS quotas. 
 |   
|  `ApproximateNumberOfMessagesDelayed` |   

The number of messages in the queue that are delayed and not immediately available for retrieval.  |  

Count |  Reported if delayed messages exist in the queue. |   
Applies to queues configured with a default delay and to individual messages sent with a `DelaySeconds` parameter. 
Delayed messages remain hidden from consumers until their delay period expires, which can affect perceived queue backlog or throughput. 
 |   
|  `ApproximateNumberOfMessagesNotVisible` |  The number of in-flight messages that have been received but not yet deleted or expired. |  

Count |  Reported if in-flight messages exist. |   
Messages enter the in-flight state after being sent to a consumer via the `ReceiveMessage` API. 
These messages are temporarily hidden from other consumers during the visibility timeout window. 
Use this metric to track message processing delays or stuck consumers. 
On rare occasions, one of the servers that Amazon SQS uses to store your messages might be unavailable when Amazon SQS reports queue metrics. When this occurs, this metric might report a non-zero value, including when the queue is otherwise empty or has had no `ReceiveMessage` calls. It typically resolves within minutes, so if you set an alarm for this metric, evaluate multiple consecutive data points rather than a single non-zero value. 
 |   
|  `ApproximateNumberOfMessagesVisible` |  The number of messages currently available for retrieval and processing. |  

Count |  Reported if the queue is active. |   
Reflects the current processing backlog in the queue. 
There's no hard limit on how many messages can accumulate, but they are subject to the queue’s configured retention period. 
A consistently high value may indicate under-provisioned consumers or stuck processing logic. 
 |   
|  `NumberOfEmptyReceives`¹ |  The number of ReceiveMessage API calls that returned no messages. |  

Count |  Reported during receive operations. |   
This metric can help identify inefficiencies in polling behavior or underutilized consumer instances. 
High values may occur when the queue is empty, the consumer uses short polling, or messages are being processed faster than they are produced. 
This isn't a precise indicator of queue state. It reflects service-side behavior and may include retries. 
 |   
|  `NumberOfDeduplicatedSentMessages` |  For FIFO only. The number of sent messages that were deduplicated and not added to the queue. |  

Count |  Reported if duplicate `MessageDeduplicationId` values or content are detected. |   
SQS deduplicates messages based on the `MessageDeduplicationId` or content-based hashing (if enabled). 
A high value may indicate that a producer is repeatedly sending the same message within the 5-minute deduplication window. 
Use this metric to troubleshoot redundant producer logic or confirm that deduplication is functioning as intended. 
 |   
|  `NumberOfMessagesDeleted`¹ |   

The number of messages successfully deleted from the queue.  |  

Count |  Reported for each delete request with a valid receipt handle. |   
This metric counts all successful delete operations—even if the same message is deleted more than once. 
Common reasons for higher-than-expected values include:  
Multiple deletes of the same message using different receipt handles, after visibility timeout expires and the message is received again. 
Duplicate deletes using the same receipt handle, which still return a success status and increment the metric. 
Use this metric to track message processing success, but don't treat it as an exact count of unique deleted messages. 
 |   
|  `NumberOfMessagesReceived`¹ |  The number of messages returned by the ReceiveMessage API. |  

Count |  Reported during receive operations. |    
This includes all messages returned to consumers, including those that are later returned to the queue due to visibility timeout expiration. 
A single message can be received multiple times if it isn’t deleted, which can cause this metric to exceed the number of messages sent. 
Use this to track consumer activity, but don't treat it as a count of unique messages processed. 
  |   
|   `NumberOfMessagesSent`¹ |  The number of messages successfully added to a queue. |  

Count |  Reported for each successful manual send. |   
Manual calls to `SendMessage` or `SendMessageBatch` are counted, including those targeting a DLQ directly. 
Messages that are automatically moved to a DLQ after exceeding the `maxReceiveCount` are not included in this metric. 
As a result, `NumberOfMessagesSent` may be lower than `NumberOfMessagesReceived`—especially if redrive policies are moving many messages to DLQs behind the scenes. 
 |   
|   `SentMessageSize`¹  |   

The size of messages successfully sent to the queue.  |  

Bytes |  Not emitted until at least one message is sent. |   
This metric will not appear in the CloudWatch console until the queue receives its first message. 
Use this metric to track the size of each message in bytes. This is useful for analyzing payload trends or estimating throughput cost. 
The maximum message size for SQS is 1 MiB. 
 |   
|   `ApproximateNumberOfNoisyGroups` |  

The number of message groups that are considered noisy in a fair queue. A noisy message group represents a noisy neighbor tenant of a multi-tenant queue. |  

Count |  A non-negative value is reported if the queue is active. |   
Helps identify potential noisy neighbor problems in multi-tenant environments by tracking message groups consuming disproportionate resources. 
Use this metric to set alarms that trigger when the number of noisy groups exceeds your acceptable threshold, indicating potential queue fairness issues. 
 |   
|   `ApproximateNumberOfMessagesVisibleInQuietGroups` |  

The number of messages visible excluding messages from noisy message groups. |  

Count |  A non-negative value is reported if the queue is active. |   
Provides visibility into the queue backlog for standard-rate message groups, excluding messages from noisy neighbors. 
Helps identify the true processing backlog for typical message groups by filtering out the impact of noisy neighbors. 
 |   
|   `ApproximateNumberOfMessagesNotVisibleInQuietGroups` |  The number of messages in-flight excluding messages from noisy message groups. |  

Count |  A non-negative value is reported if the queue is active. |   
Tracks in-flight messages (being processed but not yet deleted) from well-behaved message groups. 
Use this metric to monitor processing throughput of normal message groups and detect processing bottlenecks that aren't caused by noisy neighbors. 
 |   
|   `ApproximateNumberOfMessagesDelayedInQuietGroups` |  The number of messages excluding messages from noisy message groups that are delayed and not available for reading immediately. Delayed messages occur when the queue is configured as a delay queue or when a message has been sent with a delay parameter. |  

Count |  A non-negative value is reported if the queue is active. |   
Helps monitor the delayed message backlog from message groups with normal or expected throughput patterns (as opposed to high-volume or noisy groups) 
Useful for understanding future processing requirements and capacity planning for typical workloads. 
 |   
|   `ApproximateAgeOfOldestMessageInQuietGroups` |  The age of the oldest non-deleted message in the queue excluding messages from noisy message groups. |  

Seconds |  A non-negative value is reported if the queue is active. |   
Used for monitoring SLA compliance and detecting processing bottlenecks in message groups with normal or expected throughput patterns (as opposed to high-volume or noisy message groups that might otherwise skew the metric). 
Use this metric to set alarms for message processing timeouts that ignore artificially aged messages from noisy neighbors. 
 |    

¹ These metrics reflect system-level activity and may include retries, duplicates, or delayed messages. Don’t use raw counts to estimate real-time queue state without factoring in message lifecycle behavior. 

## Dead-letter queues (DLQs) and CloudWatch metrics 

When working with DLQs, it's important to understand how Amazon SQS metrics behave:  
`NumberOfMessagesSent` – This metric behaves differently for DLQs:  
Manual Sending – Messages manually sent to a DLQ are captured by this metric. 
Automatic Redrive – Messages automatically moved to a DLQ due to processing failures are not captured by this metric. As a result, the `NumberOfMessagesSent` and `NumberOfMessagesReceived` metrics may show discrepancies for DLQs. 
Recommended Metric for DLQs – To monitor the state of a DLQ, use the `ApproximateNumberOfMessagesVisible` metric. This metric indicates the number of messages currently available for processing in the DLQ. 
 

## Fair queues and CloudWatch metrics 

When you use fair queues, Amazon SQS emits the following additional metrics:  
`ApproximateNumberOfNoisyGroups` 
`ApproximateNumberOfMessagesVisibleInQuietGroups` 
`ApproximateNumberOfMessagesNotVisibleInQuietGroups` 
`ApproximateNumberOfMessagesDelayedInQuietGroups` 
`ApproximateAgeOfOldestMessageInQuietGroups` 
 Note

Each `QuietGroup` metric is a subset of the equivalent standard queue-level `Approximate` metric, but excludes messages from noisy neighbor groups.    

**Noisy groups**  

A noisy message group represents a noisy neighbor tenant of a multi-tenant queue.  

**Quiet groups**  

Message groups excluding noisy groups.   

Observing SQS fair queues behavior 

To monitor the effect of Amazon SQS fair queues, you can compare `Approximate..InQuietGroups` metrics with standard queue-level metrics. During traffic surges for a specific tenant, the general queue-level metrics may reveal increasing backlogs or older message ages. However, looking at the quiet groups in isolation, you can identify that most non-noisy message groups or tenants are not impacted, and provide an estimate of the total number of impacted message groups. 

 While these new metrics provide a good overview of Amazon SQS fair queues behavior, it can be beneficial to understand which specific tenant is causing the load. Amazon CloudWatch contributor insights allows you to see metrics about the top-N contributors, the total number of unique contributors, and their usage. This is especially helpful in scenarios where you are dealing with thousands of tenants that would otherwise lead to high-cardinality data (and cost) when emitting traditional metrics.  

 For an example of monitoring configuration for fair queues, see the sample on GitHub.  

## Dimensions for Amazon SQS metrics 

Amazon SQS metrics in CloudWatch use a single dimension: `QueueName`. All metric data is grouped and filtered by the name of the queue. 

## Monitoring tips 

Monitor SQS effectively using key metrics and CloudWatch alarms to detect queue backlogs, optimize performance, and stay within service limits.  
Set CloudWatch alarms based on `ApproximateNumberOfMessagesVisible` to catch backlog growth. 
Monitor `NumberOfEmptyReceives` to tune poll frequency and reduce API cost. 
Use `ApproximateNumberOfGroupsWithInflightMessages` in FIFO queues to diagnose throughput limits. 
Review SQS quotas to understand metric thresholds and service limits.
