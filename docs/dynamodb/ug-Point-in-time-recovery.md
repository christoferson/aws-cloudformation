> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html
> Downloaded: 2026-10-24

# Point-in-time backups for DynamoDB

Amazon DynamoDB point-in-time recovery (PITR) provides automatic continuous backups of your DynamoDB table data. Point-in-time recovery (PITR) backups are fully managed by DynamoDB and provide up to 35 days of recovery points at a per second granularity. With point-in-time recovery, you don't have to worry about creating, maintaining, or scheduling on-demand backups. This section provides an overview of how the process works in DynamoDB. 

## Before you begin 

Before you enable point-in-time recovery (PITR) on an Amazon DynamoDB table, consider the following:  
Setting the `RecoveryPeriodinDays` allows you to shorten the time period for which continuous backups are taken. By default, your `RecoveryPeriodinDays` is 35. However, you can set it to be any value between 1 and 35. Shortening the `RecoveryPeriodinDays` has no impact on PITR pricing because the price is based on the size of table and local secondary indexes.  
If you disable point-in-time recovery and later re-enable it on a table, you reset the start time for which you can recover that table. As a result, you can only immediately restore that table using the `LatestRestorableDateTime`. 
You can enable point-in-time recovery on each local replica of a global table. When you restore the table, the backup restores to an independent table that is not part of the global table. If you are using Global Tables version 2019.11.21 (Current) of global tables, you can create a new global table from the restored table. For more information, see How DynamoDB global tables work. 
You can also restore your DynamoDB table data across AWS Regions such that the restored table is created in a different Region from where the source table resides. You can do cross-Region restores between AWS commercial Regions, AWS China Regions, and AWS GovCloud (US) Regions. You pay only for the data you transfer out of the source Region and for restoring to a new table in the destination Region. 
AWS CloudTrail logs all console and API actions for point-in-time recovery to enable logging, continuous monitoring, and auditing. For more information, see Logging DynamoDB operations by using AWS CloudTrail. 
 Topics
Enable point-in-time recovery in DynamoDB
