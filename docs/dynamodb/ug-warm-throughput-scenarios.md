> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/warm-throughput-scenarios.html
> Downloaded: 2026-10-24

# Understanding DynamoDB warm throughput in different scenarios

Here are some different scenarios you might encounter when working with DynamoDB warm throughput.Topics
Warm throughput and uneven access patterns
Warm throughput for a provisioned table
Warm throughput for an on-demand table
Warm throughput for an on-demand table with maximum throughput configured
 

## Warm throughput and uneven access patterns 

A table might have a warm throughput of 30,000 read units per second and 10,000 write units per second, but you could still experience throttling on reads or writes before hitting those values. This is likely due to a hot partition. While DynamoDB can keep scaling to support virtually unlimited throughput, each individual partition is limited to 1,000 write units per second and 3,000 read units per second. If your application drives too much traffic to a small portion of the table’s partitions, throttling can occur even before you reach the table's warm throughput values. We recommend following DynamoDB best practices to make sure seamless scalability and avoid hot partitions. 

## Warm throughput for a provisioned table 

Consider a provisioned table that has a warm throughput of 30,000 read units per second and 10,000 write units per second but currently has a provisioned throughput of 4,000 RCU and 8,000 WCU. You can instantly scale the table's provisioned throughput up to 30,000 RCU or 10,000 WCU by updating your provisioned throughput settings. As you increase the provisioned throughput beyond these values, the warm throughput will automatically adjust to the new higher values, because you have established a new peak throughput. For example, if you set the provisioned throughput to 50,000 RCU, the warm throughput will increase to 50,000 read units per second. 

```
"ProvisionedThroughput": 
    {
        "ReadCapacityUnits": 4000,
        "WriteCapacityUnits": 8000 
    }
"WarmThroughput": 
    { 
        "ReadUnitsPerSecond": 30000,
        "WriteUnitsPerSecond": 10000
    }

```
 

## Warm throughput for an on-demand table 

A new on-demand table starts with a warm throughput of 12,000 read units per second and 4,000 write units per second. Your table can instantly accommodate sustained traffic up to these levels. When your requests exceed 12,000 read units per second or 4,000 write units per second, the warm throughput will automatically adjust to higher values. 

```
"WarmThroughput": 
    { 
        "ReadUnitsPerSecond": 12000,
        "WriteUnitsPerSecond": 4000
    }
```
 

## Warm throughput for an on-demand table with maximum throughput configured 

Consider an on-demand table with a warm throughput of 30,000 read units per second but with a maximum throughput configured at 5,000 read request units (RRU). In this scenario, the table's throughput will be limited to the maximum of 5,000 RRU that you set. Any throughput requests exceeding this maximum will be throttled. However, you can modify the table-specific maximum throughput at any time based on your application's needs. 

```
"OnDemandThroughput": 
    {
        "MaxReadRequestUnits": 5000,
        "MaxWriteRequestUnits": 4000
    }
"WarmThroughput": 
    { 
        "ReadUnitsPerSecond": 30000,
        "WriteUnitsPerSecond": 10000
    }
```
