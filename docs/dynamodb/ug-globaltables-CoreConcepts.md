> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-CoreConcepts.html
> Downloaded: 2026-10-24

# Global tables core concepts

The following sections describe the concepts and behaviors of global tables in Amazon DynamoDB 

## Concepts 

Global tables is a DynamoDB feature that replicates table data across AWS Regions. 

A replica table (or replica) is a DynamoDB table that functions as part of a global table. A global table consists of two or more replica tables across different AWS Regions. Each global table can have only one replica per AWS Region. All replicas in a global table share the same table name, primary key schema, and item data. 

When an application writes data to a replica in one Region, DynamoDB automatically replicates the write to all other replicas in the global table. For more information about how to get started with global tables, see Tutorials: Creating global tables or Tutorials: Creating multi-account global tables. 

## Versions 

There are two versions of DynamoDB global tables available: Global Tables version 2019.11.21 (Current) and Global tables version 2017.11.29 (Legacy). You should use Global Tables version 2019.11.21 (Current) whenever possible. The information in this documentation section is for Version 2019.11.21 (Current). For more information, see Determining the version of a global table Determining the version of a global table. 

## Availability 

Global tables help improve your business continuity by making it easier to implement a multi-Region high availability architecture. If a workload in a single AWS Region becomes impaired, you can shift application traffic to a different Region and perform reads and writes to a different replica table in the same global table. 

Each replica table in a global table provides the same durability and availability as a single-Region DynamoDB table. Global tables offer a 99.999% availability Service Level Agreement (SLA), compared to 99.99% for single-Region tables. 

## Fault injection testing 

Both MREC and MRSC global tables integrate with AWS Fault Injection Service (AWS FIS), a fully managed service for running controlled fault injection experiments to improve an application's resilience. Using AWS FIS, you can:  
Create experiment templates that define specific failure scenarios. 
Inject failures to validate application resilience by simulating Region isolation (that is, pausing replication to and from a selected replica) to test error handling, recovery mechanisms, and multi-Region traffic shift behavior when one AWS Region experiences disruption. 
 

For example, in a global table with replicas in US East (N. Virginia), US East (Ohio), and US West (Oregon), you can run an experiment in US East (Ohio) to test region isolation there while US East (N. Virginia) and US West (Oregon) continue normal operations. This controlled testing helps you identify and resolve potential issues before they affect production workloads.  

See  Action targets in the AWS FIS user guide for a complete list of AWS FIS supported actions and  Cross-Region Connectivity to pause DynamoDB replication between regions. 

For information about Amazon DynamoDB global table actions available in AWS FIS, see DynamoDB global tables actions reference in the AWS FIS User Guide. 

To get started running fault injection experiments, see Planning your AWS FIS experiments in the AWS FIS user guide. Note

During AWS FIS experiments in MRSC, eventually consistent reads are permitted, but table setting updates - such as changing billing mode or configuring table throughput - are not allowed, similar to MREC. Please check the CloudWatch metric FaultInjectionServiceInducedErrors for additional details regarding the error code. 

## Time To Live (TTL) 

Global tables configured for MREC support configuring Time To Live (TTL) deletion. TTL settings are automatically synchronized for all replicas in a global table. When TTL deletes an item from a replica in a Region, the delete is replicated to all other replicas in the global table. TTL does not consume write capacity, so you are not charged for the TTL delete in the Region where the delete occurred. However, you are charged for the replicated delete in each other region with a replica in the global table. 

TTL delete replication consumes write capacity on the replicas to which the delete is being replicated. Replicas configured for provisioned capacity might throttle requests if the combination of write throughput and TTL delete throughput is higher than the provisioned write capacity. 

Global tables configured for multi-Region strong consistency (MRSC) do not support configuring Time To Live (TTL) deletion. 

## Streams 

Global tables configured for multi-Region eventual consistency (MREC) replicate changes by reading those changes from a DynamoDB Stream on a replica table and applying that change to all other replica tables. Streams are therefore enabled by default on all replicas in an MREC global table, and cannot be disabled on those replicas. The MREC replication process might combine multiple changes in a short period of time into a single replicated write, resulting in each replica's Stream containing slightly different records. Streams records on MREC replicas maintain ordering for all changes to the same item, but the relative ordering of changes to different items might vary across replicas. 

If you want to write an application that processes Streams records for changes that occurred in a particular Region but not other Regions in a global table, you can add an attribute to each item that defines in which Region the change for that item occurred. You can use this attribute to filter Streams records for changes that occurred in other Regions, including the use of Lambda event filters to only invoke Lambda functions for changes in a specific Region. 

Global tables configured for multi-Region strong consistency (MRSC) do not use DynamoDB Streams for replication, so Streams are not enabled by default on MRSC replicas. You can enable Streams on an MRSC replica. Streams records on MRSC replicas are identical for every replica, including Stream record ordering. 

## Transactions 

On a global table configured for MREC, DynamoDB transaction operations ( `TransactWriteItems` and `TransactGetItems`) are only atomic within the Region where the operation was invoked. Transactional writes are not replicated as a unit across Regions, meaning only some of the writes in a transaction might be returned by read operations in other replicas at a given point in time. 

For example, if you have a global table with replicas in the US East (Ohio) and US West (Oregon) Regions and perform a `TransactWriteItems` operation in the US East (Ohio) Region, you might observe partially completed transactions in the US West (Oregon) Region as changes are replicated. Changes will only be replicated to other Regions after they've been committed in the source Region. 

Global tables configured for multi-Region strong consistency (MRSC) do not support transaction operations, and will return an error if those operations are invoked on an MRSC replica. 

## Read and write throughput 

### Provisioned mode 

Replication consumes write capacity. Replicas configured for provisioned capacity might throttle requests if the combination of application write throughput and replication write throughput exceeds the provisioned write capacity. For global tables using provisioned mode, auto scaling settings for both read and write capacities are synchronized between replicas. 

You can independently configure read capacity settings for each replica in a global table by using the `ProvisionedThroughputOverride` parameter at the replica level. By default, changes to provisioned read capacity are applied to all replicas in the global table. When adding a new replica to a global table, the read capacity of the source table or replica is used as the initial value unless a replica-level override is explicitly specified. 

### On-demand mode 

For global tables configured for on-demand mode, write capacity is automatically synchronized across all replicas. DynamoDB automatically adjusts capacity based on traffic, and there are no replica-specific read or write capacity settings to manage. 

## Monitoring global tables 

Global tables configured for multi-Region eventual consistency (MREC) publish the ReplicationLatency metric to CloudWatch. This metric tracks the elapsed time between when an item is written to a replica table, and when that item appears in another replica in the global table. `ReplicationLatency` is expressed in milliseconds and is emitted for every source and destination Region pair in a global table.  

Typical `ReplicationLatency` values depends on the distance between your chosen AWS Regions, as well as other variables like workload type and throughput. For example, a source replica in the US West (N. California) (us-west-1) Region has lower `ReplicationLatency` to the US West (Oregon) (us-west-2) Region compared to the Africa (Cape Town) (af-south-1) Region. 

An increasing value for `ReplicationLatency` could indicate that updates from one replica are not propagating to other replica tables in a timely manner. In this case, you can temporarily redirect your application's read and write activity to a different AWS Region. 

Global tables configured for multi-Region strong consistency (MRSC) do not publish a `ReplicationLatency` metric. 

## Considerations for managing global tables 

You can't delete a table used to add a new global table replica until 24 hours have elapsed since the new replica was created. 

If you disable an AWS Region that contains global table replicas, those replicas are permanently converted to single-Region tables 20 hours after the Region is disabled.
