> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_TableCapacityMode.html
> Downloaded: 2026-10-24

# Evaluate your DynamoDB table's capacity mode

This section provides an overview of how to select the appropriate capacity mode for your DynamoDB table. Each mode is tuned to meet the needs of a different workload in terms of responsiveness to change in throughput, as well as how that usage is billed. You must balance these factors when making your decision.Topics
What table capacity modes are available
When to select on-demand capacity mode
When to select provisioned capacity mode
Additional factors to consider when choosing a table capacity mode
 

## What table capacity modes are available 

When you create a DynamoDB table, you must select either on-demand or provisioned capacity mode.  

You can switch tables from provisioned capacity mode to on-demand mode up to four times in a 24-hour rolling window. You can switch tables from on-demand mode to provisioned capacity mode at any time.  On-demand capacity mode 

The on-demand capacity mode is designed to eliminate the need to plan or provision the capacity of your DynamoDB table. In this mode, your table will instantly accommodate requests to your table without the need to scale any resources up or down (up to twice the previous peak throughput of the table). 

DynamoDB on-demand offers pay-per-request pricing for read and write requests so that you only pay for what you use. Provisioned capacity mode 

The provisioned capacity mode is a more traditional model where you must define how much capacity the table has available for requests either directly or with the assistance of auto scaling. Because a specific capacity is provisioned for the table at any given time, billing is based off of the total capacity provisioned rather than the number of requests consumed. Going over the allocated capacity can also cause the table to reject requests and reduce the experience of your applications users. 

Provisioned capacity mode requires constant monitoring to find a balance between not over-provisioning or under-provisioning the table to keep both throttling low and costs tuned. 

## When to select on-demand capacity mode 

When optimizing for cost, on-demand mode is your best choice when you have a workload similar to the following graphs. 

The following factors contribute to this type of workload:  
Traffic pattern that evolves over time  
Variable volume of requests (resulting from batch workloads) 
Unpredictable request timing (resulting in traffic spikes) 
Drops to zero or below 30% of the peak for a given hour  
     

For workloads with the above factors, using auto scaling to maintain enough capacity on the table to respond to spikes in traffic will likely lead to the table being overprovisioned and costing more than necessary or the table being under provisioned and requests being unnecessarily throttled. On-demand capacity mode is the better choice because it can handle fluctuating traffic without requiring you to predict or adjust capacity. 

With on-demand mode’s pay-per-request pricing model, you don’t have to worry about idle capacity because you only pay for the throughput you actually use. You are billed per read or write request consumed, so your costs directly reflect your actual usage, making it easy to balance costs and performance. Optionally, you can also configure maximum read or write (or both) throughput per second for individual on-demand tables and global secondary indexes to help keep costs and usage bounded. For more information, see maximum throughput for on-demand tables . 

## When to select provisioned capacity mode 

An ideal workload for provisioned capacity mode is one with a more steady and predictable usage pattern like the graph below. Note

We recommend reviewing metrics at a fine-grained period, such as 14 days, before taking action on your provisioned capacity. 

The following factors contribute to this type of workload:  
Steady, predictable and cyclical traffic for a given hour or day 
Limited short-term bursts of traffic 
    

Since the traffic volumes within a given hour or day are more stable, you can set the provisioned capacity of the table relatively close to the actual consumed capacity of the table. Cost optimizing a provisioned capacity table is ultimately an exercise in getting the provisioned capacity (blue line) as close to the consumed capacity (orange line) as possible without increasing `ThrottledRequests` on the table. The space between the two lines is both wasted capacity as well as insurance against a bad user experience due to throttling. If you can predict your application’s throughput requirements and you prefer the cost predictability of controlling read and write capacity, then you might want to continue using provisioned tables. 

DynamoDB provides auto scaling for provisioned capacity tables which will automatically balance this on your behalf. This lets you track your consumed capacity throughout the day and set the capacity of the table based on a handful of variables. When using auto scaling, your table will be over-provisioned and you need to fine tune the ratio between number of throttles versus over-provisioned capacity units to match your workload needs.    Minimum capacity units 

You can set the minimum capacity of a table to limit throttling, but it will not reduce the cost of the table. If your table has periods of low usage follow by a sudden burst of high usage, setting the minimum can prevent auto scaling from setting the table capacity too low. Maximum capacity units 

You can set the maximum capacity of a table to limit a table scaling higher than intended. Consider applying a maximum for Dev or Test tables where large-scale load testing is not desired. You can set a maximum for any table, but be sure to regularly evaluate this setting against the table baseline when using it in Production to prevent accidental throttling. Target utilization 

Setting the target utilization of the table is the primary means of cost optimization for a provisioned capacity table. Setting a lower percent value here will increase how much the table is overprovisioned, increasing cost, but reducing the risk of throttling. Setting a higher percent value will decrease how much the table is overprovisioned, but increase the risk of throttling. 

## Additional factors to consider when choosing a table capacity mode 

When deciding between the two modes, there are some additional factors worth considering. Provisioned capacity utilization 

To determine when on-demand mode would cost less than provisioned capacity, it's helpful to look at your provisioned capacity utilization, which refers to how efficiently the allocated (or “provisioned) resources are being used. On-demand mode costs less for workloads with average provisioned capacity utilization below 35%. In many cases, even for workloads with provisioned capacity utilization higher than 35%, it can be more cost-effective to use on-demand mode especially if the workload has periods of low activity mixed with occasional peaks. Reserved capacity 

For provisioned capacity tables, DynamoDB offers the ability to purchase reserved capacity for your read and write capacity (replicated write capacity units (rWCU) and Standard-IA tables are currently not eligible). Reserved capacity offers significant discounts over standard provisioned capacity pricing. 

 When deciding between the two table modes, consider how much this additional discount will affect the cost of the table. In some cases, it might cost less to run a relatively unpredictable workload can be cheaper to run on an overprovisioned provisioned capacity table with reserved capacity.  Improving predictability of your workload 

In some situations, a workload might seemingly have both a predictable and unpredictable pattern. While this can be easily supported with an on-demand table, costs will likely be better if the unpredictable patterns in the workload can be improved. 

One of the most common causes of these patterns is batch imports. This type of traffic can often exceed the baseline capacity of the table to such a degree that throttling would occur if it were to run. To keep a workload like this running on a provisioned capacity table, consider the following options:  
If the batch occurs at scheduled times, you can schedule an increase to your auto- scaling capacity before it runs 
If the batch occurs randomly, consider trying to extend the time it runs rather than executing as fast as possible 
Add a ramp up period to the import where the velocity of the import starts small but is slowly increased over a few minutes until auto scaling has had the opportunity to start adjusting table capacity
