> Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues-detailed.html
> Downloaded: 2026-10-27

# How Amazon SQS fair queues work

 Amazon SQS fair queues automatically mitigate the noisy-neighbor impact in multi-tenant queues by preventing a single tenant from slowing down message processing for other tenants. When fair queues detect that one tenant is using a disproportionate share of the queue's consumer capacity, they prioritize delivery of messages from quiet tenants. 

## Tenant identification 

Fair queues identify tenants by the `MessageGroupId` property on each message. Messages that share the same `MessageGroupId` belong to the same tenant. A fair queue can contain a mix of messages with and without a `MessageGroupId`. Each message without a `MessageGroupId` is treated as belonging to its own distinct tenant. 

We recommend setting a `MessageGroupId` on every message you send to a fair queue, using an identifier that maps to a real entity in your system, such as a customer ID, client application ID, or request type. 

## How detection works 

Amazon SQS detects noisy neighbors using two measures:  
Concurrency share — the tenant's in-flight messages as a fraction of all in-flight messages in the queue. This detects tenants with many messages being processed at once, whether due to high send volume, slow processing, or both. 
Processing time share — the tenant's recent share of total consumer processing time. This detects tenants whose messages are few in number but slow to process, so the tenant occupies significant consumer time without having many messages in flight at once. 
 

A tenant is marked as a noisy neighbor when either of the following is true:  
Concurrency share: the tenant accounts for more than 10% of in-flight messages in the queue and has at least 30 of its own messages in flight. 
Processing time share: the tenant's recent share of total consumer processing time exceeds 10%. 
 

Because Amazon SQS is a distributed system, these thresholds are approximate and detection may not activate at the exact values described. 

## How message delivery order changes 

Once a tenant is detected as a noisy neighbor, Amazon SQS prioritizes delivering messages from quiet tenants. Consumer instances polling for messages receive messages from quiet tenants whenever quiet-tenant messages are available. This prioritization continues until the noisy neighbor's concurrency share and processing time share drop to levels comparable to quiet tenants. 

Noisy neighbor messages are not dropped or throttled. Their dwell time rises while quiet-tenant messages are prioritized, and returns to normal once their backlog clears. When no quiet-tenant messages are waiting, consumer instances receive noisy neighbor messages as usual. 

If multiple tenants are detected as noisy neighbors simultaneously, consumer instances receive messages from the noisy tenant with the fewest in-flight messages first. This helps balance processing time across noisy tenants. 

## When a noisy neighbor becomes quiet 

A tenant is no longer treated as a noisy neighbor when either of the following is true:  
The tenant's backlog has been fully consumed. 
No messages from the tenant have been in flight for a continuous period of 5 minutes. 
 

After that, the tenant's messages are no longer deprioritized and are treated the same as messages from any other quiet tenant. 

## Consumer capacity considerations 

For the concurrency share measure to work effectively, your consumers need to process enough messages concurrently that one tenant's share of in-flight messages can stand out. Take this into account when sizing your consumer fleet. 

When using Lambda as a consumer through event source mapping, the number of in-flight messages depends on both Lambda function concurrency and batch size. Evaluate these settings together when sizing your consumers. 

When the number of in-flight messages is too low for the concurrency share threshold to trigger, the processing time share measure can still detect noisy neighbors. However, fair queues work best when consumers process enough messages concurrently for both measures to be evaluated.
