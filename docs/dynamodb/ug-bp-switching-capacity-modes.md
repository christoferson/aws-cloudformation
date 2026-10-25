> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-switching-capacity-modes.html
> Downloaded: 2026-10-24

# Considerations when switching capacity modes in DynamoDB

When you create a DynamoDB table, you must select either on-demand or provisioned capacity mode.

You can switch tables from provisioned capacity mode to on-demand mode up to four times in a 24-hour rolling window. You can switch tables from on-demand mode to provisioned capacity mode at any time. Topics
Switching from provisioned capacity mode to on-demand capacity mode
Switching from on-demand capacity mode to provisioned capacity mode
 

## Switching from provisioned capacity mode to on-demand capacity mode 

In provisioned mode, you set read and write capacity based on your expected application needs. When you update a table from provisioned to on-demand mode, you don't need to specify how much read and write throughput you expect your application to perform. 

DynamoDB on-demand offers simple pay-per-request pricing for read and write requests so that you only pay for what you use, making it easy to balance costs and performance. 

You can optionally configure maximum read or write (or both) throughput for individual on-demand tables and associated global secondary indexes to help keep costs and usage bounded. For more information about setting maximum throughput for a specific table or index, see DynamoDB maximum throughput for on-demand tables. 

When you switch from provisioned capacity mode to on-demand capacity mode, the process can take several minutes. During the switching period, your table delivers throughput that is consistent with the previously provisioned write capacity unit and read capacity unit amounts. 

### Initial throughput for on-demand capacity mode 

If you recently switched an existing table to on-demand capacity mode for the first time, the table has the following previous peak settings, even though the table has not served traffic previously using on-demand capacity mode. 

Following are examples of possible scenarios:  
Any provisioned table configured below 4000 WCU and 12,000 RCU, that has never been previously provisioned for more. When you switch this table to on-demand for the first time, DynamoDB will make sure it is scaled out to instantly sustain at least 4,000 write units/sec and 12,000 read units/sec. 
A provisioned table configured as 8,000 WCU and 24,000 RCU. When you switch this table to on-demand, it will continue to be able to sustain at least 8,000 write units/sec and 24,000 read units/sec at any time. 
A provisioned table configured with 8,000 WCU and 24,000 RCU, that consumed 6,000 write units/sec and 18,000 read units/sec for a sustained period. When you switch this table to on-demand, it will continue to be able to sustain at least 8,000 write units/sec and 24,000 read units/sec. The previous traffic might further allow the table to sustain much higher levels of traffic without throttling. 
A table previously provisioned with 10,000 WCU and 10,000 RCU, but currently provisioned with 10 RCU and 10 WCU. When you switch this table to on-demand, it will be able to sustain at least 10,000 write units/sec and 10,000 read units/sec. 
 

Warm throughput is the number of read and write operations that your table can instantaneously support. Warm throughput is available by default for all tables and global secondary indexes (GSIs), and represents the level to which they have already scaled based on historical usage. 

When you use on-demand mode, or when you update your provisioned throughput to these values, your application can issue requests up to those values instantly. For more information, see Understanding DynamoDB warm throughput. 

### Auto scaling settings 

When you update a table from provisioned to on-demand mode:  
If you're using the console, all of your auto scaling settings (if any) will be deleted. 
If you're using the AWS CLI or AWS SDK, all of your auto scaling settings will be preserved. These settings can be applied when you update your table to provisioned billing mode again. 
 

### Bulk editing capacity mode in the DynamoDB console 

You can bulk edit multiple tables to switch from provisioned capacity mode to on-demand capacity mode using the DynamoDB console. To bulk edit capacity mode:  
In the DynamoDB console, go to the Tables page. 
Select the checkboxes for the tables you want to update to on-demand capacity mode. 
Choose Actions, and then select Update to on-demand capacity mode. 
 

This bulk operation allows you to efficiently switch multiple tables to on-demand capacity mode without having to update each table individually. 

## Switching from on-demand capacity mode to provisioned capacity mode 

When switching from on-demand capacity mode back to provisioned capacity mode, your table delivers throughput consistent with the previous peak reached when the table was set to on-demand capacity mode. 

### Managing capacity 

Consider the following when you update a table from on-demand to provisioned mode:  
 If you're using the AWS CLI or AWS SDK, choose the right provisioned capacity settings of your table and global secondary indexes by using Amazon CloudWatch to look at your historical consumption (`ConsumedWriteCapacityUnits` and `ConsumedReadCapacityUnits` metrics) to determine the new throughput settings. Note

If you're switching a global table to provisioned mode, look at the maximum consumption across all your regional replicas for base tables and global secondary indexes when determining the new throughput settings.  
If you're switching from on-demand mode back to provisioned mode, make sure to set the initial provisioned units high enough to handle your table or index capacity during the transition. 
 

### Managing auto scaling 

When you update a table from on-demand to provisioned mode:  
If you're using the console, we recommend enabling auto scaling with the following defaults:  
Target utilization: 70% 
Minimum provisioned capacity: 5 units 
Maximum provisioned capacity: The Region maximum 
 If you're using the AWS CLI or SDK, your previous auto scaling settings (if any) are preserved.
