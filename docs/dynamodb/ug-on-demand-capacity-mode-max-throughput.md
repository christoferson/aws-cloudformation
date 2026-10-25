> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode-max-throughput.html
> Downloaded: 2026-10-24

# DynamoDB maximum throughput for on-demand tables

For on-demand tables, you can optionally specify maximum read or write (or both) throughput per second on individual tables and associated global secondary indexes (GSIs). Specifying a maximum on-demand throughput helps keep table-level usage and costs bounded. By default, maximum throughput settings don’t apply and your on-demand throughput rate is bounded by 40,000 table-level read and write throughput AWS service quota for all tables in the account. If needed, you can request an increase to your service quota.

When you configure maximum throughput for an on-demand table, throughput requests that exceed the maximum amount specified will be throttled. You can modify the table-level throughput settings any time based on your application requirements.

The following are some common use cases that can benefit from using maximum throughput for on-demand tables: 
Throughput cost optimization – Using maximum throughput for on-demand tables provides an additional layer of cost predictability and manageability. Additionally, it offers greater flexibility to use on-demand mode to support workloads with differing traffic patterns and budget. 
Protection against excessive usage – By setting maximum throughput, you can prevent an accidental surge in read or write consumption, which might arise from non-optimized code or rogue processes, against an on-demand table. This table-level setting can protect organizations from consuming excessive resources within a certain time frame. 
Safeguarding downstream services – A customer application can include serverless and non-serverless technologies. The serverless piece of the architecture can scale rapidly to match demand. But downstream components with fixed capacities could be overwhelmed. Implementing maximum throughput settings for on-demand tables can prevent large volume of events from propagating to multiple downstream components with unexpected side effects. 

You can configure maximum throughput for on-demand mode for new and existing single-Region tables and global tables and GSIs. You can also configure maximum throughput during table restore and data import from Amazon S3 workflows.

You can specify maximum throughput settings for an on-demand tables using the DynamoDB console, AWS CLI, AWS CloudFormation, or DynamoDB API.Note

The maximum throughput for an on-demand table is applied on a best-effort basis and should be thought of as targets instead of guaranteed request ceilings. Your workload might temporarily exceed the maximum throughput specified because of burst capacity. In some cases, DynamoDB uses burst capacity to accommodate reads or writes in excess of your table's maximum throughput settings. With burst capacity, unexpected read or write requests can succeed where they otherwise would be throttled.Topics
Considerations when using maximum throughput for on-demand mode
Request throttling and CloudWatch metrics
 

## Considerations when using maximum throughput for on-demand mode 

When you use maximum throughput for tables in on-demand mode, the following considerations apply:  
You can independently set maximum throughput for reads and writes for any on-demand table, or individual global secondary index within that table to fine-tune your approach based on specific requirements. 
You can use Amazon CloudWatch to monitor and understand DynamoDB table-level usage metrics and to determine appropriate maximum throughput settings for on-demand mode. For more information, see DynamoDB Metrics and dimensions. 
When you specify the maximum read or write (or both) throughput settings on one global table replica, the same maximum throughput settings are automatically applied to all replica tables. It's important that the replica tables and secondary indexes in a global table have identical write throughput settings to achieve proper replication of data. For more information, see Best practices for global tables. 
The smallest maximum read or write throughput that you can specify is one request unit per second. 
The maximum throughput you specify must be lower than the default throughput quota that is available for any on-demand table, or individual global secondary index within that table. 
 

## Request throttling and CloudWatch metrics 

If your application exceeds the maximum read or write throughput you've set on your on-demand table, DynamoDB begins to throttle those requests. When DynamoDB throttles a read or write, it returns a `ThrottlingException` to the caller. You can then take appropriate action, if required. For example, you can increase or disable the maximum table throughput setting, or wait for a short interval before retrying the request. 

To simplify monitoring the maximum throughput configured for a table or global secondary index, CloudWatch provides the following metrics: OnDemandMaxReadRequestUnits and OnDemandMaxWriteRequestUnits.
