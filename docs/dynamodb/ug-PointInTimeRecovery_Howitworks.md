> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html
> Downloaded: 2026-10-24

# Enable point-in-time recovery in DynamoDB

Amazon DynamoDB point-in-time recovery (PITR) provides automatic backups of your DynamoDB table data. This section provides an overview of how the process works in DynamoDB.Note

DynamoDB charges for PITR based on the size of each DynamoDB table, including table data and local secondary indexes. Changing the recovery window (for example, from 35 days to 1 day) doesn't reduce the price. The cost remains the same regardless of the recovery period you choose. The configured maximum recovery period doesn't impact the price you're charged for turning on PITR. To determine your backup charges, DynamoDB continuously monitors the size of the tables that have PITR turned on. You're billed for PITR usage until you turn off PITR for each table.Topics
Enabling point-in-time recovery
Enable PITR (console)
Enable PITR (AWS CLI)
Enable PITR (CloudFormation)
Enable PITR (API)
Recovery Period
Edit PITR
Delete a table with PITR enabled
 

## Enabling point-in-time recovery 

You can enable point-in-time recovery using the AWS Management Console, AWS Command Line Interface (AWS CLI), or the DynamoDB API. When enabled, point-in-time recovery provides continuous backups until you explicitly turn it off. 

After you enable point-in-time recovery, you can restore to any point in time within `EarliestRestorableDateTime` and `LatestRestorableDateTime`. `LatestRestorableDateTime` is typically five minutes before the current time. For more information, see Restoring a DynamoDB table to a point in time. Note

The point-in-time recovery process always restores to a new table. 

## Enable PITR (console) To enable PITR using the DynamoDB console
Navigate to the DynamoDB console. 
Choose Tables from the left navigation and select your DynamoDB table. 
From the Backups tab, for the Point in Time Recovery option, choose Edit. 
Choose Turn on point-in-time recovery. 
Choose a value between 1 and 35 for your backup recovery period. This indicates the maximum time period for which the continuous backup is recoverable. 
 

## Enable PITR (AWS CLI) Note

If you receive errors when running AWS CLI commands, see Troubleshoot AWS CLI errors. Make sure you're using the most recent AWS CLI version. 

Run the update-continuous-backups command with the point-in-time-recovery-specification setting turned on: 

```
aws dynamodb update-continuous-backups \
--table-name Music \
--point-in-time-recovery-specification PointInTimeRecoveryEnabled=true,RecoveryPeriodInDays=35
```
 

## Enable PITR (CloudFormation) 

Use the AWS::DynamoDB::Table resource with the `PointInTimeRecoverySpecification` property turned on: 

```
Resources:
  iotCatalog:
    Type: AWS::DynamoDB::Table
      Properties:
      ...
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
        RecoveryPeriodInDays: 35
```
 

Request syntax example: 

```
{
   "PointInTimeRecoverySpecification": { 
      "PointInTimeRecoveryEnabled": boolean,
      "RecoveryPeriodInDays: number
   },
   "TableName": "string"
}
```
 

## Enable PITR (API) 

Run the UpdateContinuousBackups API operation with the `PointInTimeRecoverySpecification` parameter turned on. 

Request syntax example: 

```
{
   "PointInTimeRecoverySpecification": { 
      "PointInTimeRecoveryEnabled": boolean,
      "RecoveryPeriodInDays" : number
   },
   "TableName": "string"
}
```
 

Response syntax example: 

```
{
   "ContinuousBackupsDescription": { 
      "ContinuousBackupsStatus": "string",
      "PointInTimeRecoveryDescription": { 
         "PointInTimeRecoveryStatus": "string",
         "EarliestRestorableDateTime": number,
         "RecoveryPeriodInDays": number,
         "LatestRestorableDateTime": number
      }
   }
}
```
 Note

`ContinuousBackupsStatus` is always `ENABLED` for a DynamoDB table and can't be disabled. An `ENABLED` value doesn't mean that point-in-time recovery is turned on. Whether you can restore the table to a point in time is controlled separately by `PointInTimeRecoveryStatus`, which is `DISABLED` by default until you enable PITR. A newly created table therefore reports `ContinuousBackupsStatus` as `ENABLED` together with `PointInTimeRecoveryStatus` as `DISABLED`. 

Python 

```
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.update_continuous_backups(
    TableName=<table_name>,
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True,
        'RecoveryPeriodInDays': 35
    }
)
```
 

## Recovery Period 

You can set the recovery period for continuous backups to be any number between 1 and 35 days. This `RecoveryPeriodInDays` determines the time period for which your continuous backups are maintained. For example, if you set this value to be 30 days, you'll only have the ability to restore your table to any point in time from the past 30 days. Note

DynamoDB charges for PITR based on the size of each DynamoDB table, including table data and local secondary indexes. The configured maximum recovery period doesn't impact the price you're charged for turning on PITR. For details on pricing, see DynamoDB pricing. 

## Edit PITR 

You can edit the PITR setting on your table and change the recovery period. If you change the recovery period and increase it to a value higher than previously set, your `EarliestRestorePoint` will not change immediately. Since the recovery period is a rolling window, DynamoDB will continue to take automatic backups until the new increased period is reached. If you change the recovery period and decrease it to a value lower than previously set, your `EarliestRestorePoint` will immediately decrease to match your recovery period, and any continuous backups that fall outside of the new set value will not be recoverable. 

## Delete a table with PITR enabled 

When you delete a table that has point-in-time recovery enabled, DynamoDB automatically creates a backup snapshot called a system backup and retains it for 35 days (at no additional cost). You can use the system backup to restore the deleted table to the state it was in before deletion. All system backups follow a standard naming convention of `table-name``$DeletedTableBackup`. Note

Once a table with point-in-time recovery enabled is deleted, you can use system backup to restore that table to a single point in time. The system backup will be created upon table deletion, and is a snapshot of the table right before the table is deleted.
