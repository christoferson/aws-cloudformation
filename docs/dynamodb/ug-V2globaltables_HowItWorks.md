> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html
> Downloaded: 2026-10-24

# How DynamoDB global tables work

The following sections describe the concepts and behaviors of global tables in Amazon DynamoDB. 

## Concepts 

Global tables is a DynamoDB feature that replicates table data across AWS Regions.  

A replica table (or replica) is a DynamoDB table that functions as part of a global table. A global table consists of two or more replica tables across different AWS Regions. Each global table can have only one replica per AWS Region. All replicas in a global table share the same table name, primary key schema, and item data. 

When an application writes data to a replica in one Region, DynamoDB automatically replicates the write to all other replicas in the global table. For more information about how to get started with global tables, see Tutorials: Creating global tables. 

## Versions 

There are two versions of DynamoDB global tables available: Version 2019.11.21 (Current) and Version 2017.11.29 (Legacy). You should use Version 2019.11.21 (Current) whenever possible. The information in this documentation section is for Version 2019.11.21 (Current). For more information, see Determining the version of a global table. 

## Availability 

Global tables help improve your business continuity by making it easier to implement a multi-Region high availability architecture. If a workload in a single AWS Region becomes impaired, you can shift application traffic to a different Region and perform reads and writes to a different replica table in the same global table. 

Each replica table in a global table provides the same durability and availability as a single-Region DynamoDB table. Global tables offer a 99.999% availability Service Level Agreement (SLA), compared to 99.99% for single-Region tables. 

## Consistency modes 

When you create a global table, you can configure its consistency mode. Global tables support two consistency modes: multi-Region eventual consistency (MREC), and multi-Region strong consistency (MRSC). 

If you do not specify a consistency mode when creating a global table, the global table defaults to multi-Region eventual consistency (MREC). A global table cannot contain replicas configured with different consistency modes. You cannot change a global table's consistency mode after creation. 

### Multi-Region eventual consistency (MREC) 

Multi-Region eventual consistency (MREC) is the default consistency mode for global tables. Item changes in an MREC global table replica are asynchronously replicated to all other replicas, typically within a second or less. In the unlikely event a replica in a MREC global table becomes isolated or impaired, any data not yet replicated to other Regions will be replicated when the replica becomes healthy. 

If the same item is modified in multiple Regions simultaneously, DynamoDB will resolve the conflict by using the modification with the latest internal timestamp on a per-item basis, referred to as a "last writer wins" conflict resolution method. An item will eventually converge in all replicas to the version created by the last write. 

Strongly consistent read operations return the latest version of an item if that item was last updated in the Region where the read occurred, but may return stale data if the item was last updated in a different Region. Conditional writes evaluate the condition expression against the version of the item in the Region. 

You create a MREC global table by adding a replica to an existing DynamoDB table. Adding a replica has no performance impact on existing single-Region DynamoDB tables or global table replicas. You can add replicas to a MREC global table to expand the number of Regions where data is replicated, or remove replicas from an MREC global table if they are no longer needed. An MREC global table can have a replica in any Region where DynamoDB is available, and can have as many replicas as there are Regions in the AWS partition. 

To stop replicating to an MREC replica and keep its table and data, you can disassociate the replica. It becomes a standalone regional table. For requirements and instructions, see Disassociating a global table replica. 

### Multi-Region strong consistency (MRSC) 

You can configure multi-Region strong consistency (MRSC) mode when you create a global table. Item changes in an MRSC global table replica are synchronously replicated to at least one other Region before the write operation returns a successful response. Strongly consistent read operations on any MRSC replica always return the latest version of an item. Conditional writes always evaluate the condition expression against the latest version of an item. 

A MRSC global table must be deployed in exactly three Regions. You can configure a MRSC global table with three replicas, or with two replicas and one witness. A witness is a component of a MRSC global table that contains data written to global table replicas and provides an optional alternative to a full replica while supporting MRSC's availability architecture. You cannot perform read or write operations on a witness. A witness is located in a different Region than the two replicas. When creating a MRSC global table, you choose the Regions for both your replicas and the witness deployment at MRSC table creation time. You can determine whether and in which Region a MRSC global table has a witness configured from the output of the `DescribeTable` API. The witness is owned and managed by DynamoDB, and the witness will not appear in your AWS account in the Region where it is configured. 

MRSC global tables are available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt), Europe (Stockholm), Europe (Spain), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), and Asia Pacific (Singapore). An MRSC global table can include replicas from any combination of three of these Regions, including Regions on different continents. For MRSC global tables, write and strongly consistent read latencies depend on the Regions you choose because these operations require cross-Region communication. Greater round-trip latency between participating Regions can increase request latency. We recommend that you test your workload in the intended Regions to verify that it meets your application's latency requirements under normal and failover conditions. 

You create a MRSC global table by adding one replica and a witness or two replicas to an existing DynamoDB table that contains no data. When converting an existing single-Region table to a MRSC global table, you must make sure that the table is empty. Converting a single-Region table to a MRSC global table with existing items is not supported. Make sure that no data is written into the table during the conversion process. You cannot add additional replicas to an existing MRSC global table. You cannot delete a single replica or a witness from a MRSC global table. You can delete two replicas or delete one replica and a witness from a MRSC global table, converting the remaining replica to a single-Region DynamoDB table. 

A write operation fails with a `ReplicatedWriteConflictException` when it attempts to modify an item that is already being modified in another Region. Writes that fail with the `ReplicatedWriteConflictException` can be retried and will succeed if the item is no longer being modified in another Region. 

The following considerations apply to MRSC global tables:  
Time to Live (TTL) is not supported for MRSC global tables. 
Local secondary indexes (LSIs) are not supported for MRSC global tables. Global secondary indexes (GSIs) are supported. As with single-Region tables, reads from a GSI are eventually consistent. For more information, see Using Global Secondary Indexes in DynamoDB. 
CloudWatch Contributor Insights information is only reported for the Region in which an operation occurred. 
 

## Choosing a consistency mode 

The key criteria for choosing a multi-Region consistency mode is whether your application prioritizes lower latency writes and strongly consistent reads, or prioritizes global strong consistency. 

MREC global tables will have lower write and strongly consistent read latencies compared to MRSC global tables. MREC global tables have a Recovery Point Objective (RPO) equal to the replication delay between replicas, usually a few seconds depending on the replica Regions. 

You should use the MREC mode when:  
Your application can tolerate stale data returned from strongly consistent read operations if that data was updated in another Region. 
You prioritize lower write and strongly consistent read latencies over multi-Region read consistency. 
Your multi-Region high availability strategy can tolerate an RPO greater than zero. 
 

MRSC global tables will have higher write and strongly consistent read latencies compared to MREC global tables. MRSC global tables support a Recovery Point Objective (RPO) of zero. 

You should use the MRSC mode when:  
You need strongly consistent reads across multiple Regions. 
You prioritize global read consistency over lower write latency. 
Your multi-Region high availability strategy requires an RPO of zero. 
 

## Monitoring global tables 

Global tables configured for multi-Region eventual consistency (MREC) publish the ReplicationLatency metric to CloudWatch. This metric tracks the elapsed time between when an item is written to a replica table, and when that item appears in another replica in the global table. `ReplicationLatency` is expressed in milliseconds and is emitted for every source and destination Region pair in a global table.  

Typical `ReplicationLatency` values depends on the distance between your chosen AWS Regions, as well as other variables like workload type and throughput. For example, a source replica in the US West (N. California) (us-west-1) Region has lower `ReplicationLatency` to the US West (Oregon) (us-west-2) Region compared to the Africa (Cape Town) (af-south-1) Region. 

An increasing value for `ReplicationLatency` could indicate that updates from one replica are not propagating to other replica tables in a timely manner. In this case, you can temporarily redirect your application's read and write activity to a different AWS Region. 

Global tables configured for multi-Region strong consistency (MRSC) do not publish a `ReplicationLatency` metric. 

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

Global tables configured for multi-Region eventual consistency (MREC) replicate changes by reading those changes from a DynamoDB Stream on a replica table and applying that change to all other replica tables. Streams are therefore enabled by default on all replicas in an MREC global table, and cannot be disabled on those replicas. The MREC replication process might combine multiple changes in a short period of time into a single replicated write, resulting in each replica's Stream containing slightly different records. Streams records on MREC replicas are always ordered on a per-item basis, but ordering between items might differ between replicas. 

Global tables configured for multi-Region strong consistency (MRSC) do not use DynamoDB Streams for replication, so Streams are not enabled by default on MRSC replicas. You can enable Streams on an MRSC replica. Streams records on MRSC replicas are identical for every replica, including Stream record ordering. 

If you want to write an application that processes Streams records for changes that occurred in a particular Region but not other Regions in a global table, you can add an attribute to each item that defines in which Region the change for that item occurred. You can use this attribute to filter Streams records for changes that occurred in other Regions, including the use of Lambda event filters to only invoke Lambda functions for changes in a specific Region. 

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

## Settings synchronization 

Settings in DynamoDB global tables are configuration parameters that control various aspects of table behavior and replication. These settings are managed through the DynamoDB control plane APIs and can be configured when creating or modifying global tables. Global tables automatically synchronize certain settings across all replicas to maintain consistency, while allowing flexibility for region-specific optimizations. Understanding which settings synchronize and how they behave helps you configure your global table effectively. The settings fall into three main categories based on how they are synchronized across replicas. 

The following settings are always synchronized between replicas in a global table:  
Capacity mode (provisioned capacity or on-demand) 
Table provisioned write capacity 
Table write auto scaling 
Attribute definition of key schema 
Global Secondary Index (GSI) definition 
GSI provisioned write capacity 
GSI write auto scaling 
Server-side Encryption (SSE) type 
Streams definition in MREC mode 
Time To Live (TTL) 
Warm Throughput 
On-demand maximum write throughput 
 

The following settings are synchronized between replicas, but can be overridden on a per-replica basis:  
Table provisioned read capacity 
Table read auto scaling 
GSI provisioned read capacity 
GSI read auto scaling 
Table Class 
On-demand maximum read throughput 
 Note

Overridable setting values are changed if the setting is modified on any other replica. As an example, you have a MREC global table with replicas in US East (N. Virginia) and US West (Oregon). The US East (N. Virginia) replica has provisioned read throughput set to 200 RCUs. The replica in US West (Oregon) has a provisioned read throughput override set to 100 RCUs. If you update the provisioned read throughput setting on the US East (N. Virginia) replica from 200 RCUs to 300 RCUs, the new provisioned read throughput value will also be applied to the replica in US West (Oregon). This changes the provisioned read throughput setting for the US West (Oregon) replica from the overridden value of 100 RCUs to the new value of 300 RCUs. 

The following settings are never synchronized between replicas:  
Deletion protection 
Point-in-time Recovery 
Tags 
Table CloudWatch Contributor Insights enablement 
GSI CloudWatch Contributor Insights enablement 
Kinesis Data Streams definition 
Resource Policies 
Streams definition in MRSC mode 
 

All other settings are not synchronized between replicas. 

## DynamoDB Accelerator (DAX) 

Writes to global table replicas bypass DynamoDB Accelerator (DAX), updating DynamoDB directly. As a result, DAX caches can become stale as writes are not updating the DAX cache. DAX caches configured for global table replicas will only be refreshed when the cache TTL expires. 

## Considerations for managing global tables 

You can't delete a table used to add a new global table replica until 24 hours have elapsed since the new replica was created. 

If you disable an AWS Region that contains global table replicas, those replicas are permanently converted to single-Region tables 20 hours after the Region is disabled.
