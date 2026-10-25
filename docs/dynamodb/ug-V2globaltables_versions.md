> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_versions.html
> Downloaded: 2026-10-24

# DynamoDB global tables versions

There are two versions of DynamoDB global tables available: Global Tables version 2019.11.21 (Current) and Global tables version 2017.11.29 (Legacy). We recommend using Global Tables version 2019.11.21 (Current), as it is easier to use, supported in more Regions, and lower cost for most workloads compared to version 2017.11.29 (Legacy). 

## Determining the version of a global table 

### Determining the version using the AWS CLI 

#### Identifying a version 2019.11.21 (Current) global table replica 

To determine if a table is a global tables version 2019.11.21 (Current) replica, invoke the `describe-table` command for the table. If the output contains the `GlobalTableVersion` attribute with a value of "2019.11.21", the table is a version 2019.11.21 (Current) global table replica. 

An example CLI command for `describe-table`: 

```
aws dynamodb describe-table \
--table-name users \
--region us-east-2
```
 

The (abridged) output contains the `GlobalTableVersion` attribute with a value of "2019.11.21", so this table is a version 2019.11.21 (Current) global table replica. 

```
{
    "Table": {
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S"
            },
            {
                "AttributeName": "name",
                "AttributeType": "S"
            }
        ],
        "TableName": "users",
        ...
        "GlobalTableVersion": "2019.11.21",
        "Replicas": [
            {
                "RegionName": "us-west-2",
                "ReplicaStatus": "ACTIVE",
            }
        ],
        ...
    }
}
```
 

#### Identifying a version 2017.11.29 (Legacy) global table replica 

Global tables version 2017.11.29 (Legacy) uses a dedicated set of commands for global table management. To determine if a table is a global tables version 2017.11.29 (Legacy) replica, invoke the `describe-global-table` command for the table. If you receive a successful response, the table is a version 2017.11.29 (Legacy) global table replica. If the `describe-global-table` command returns a `GlobalTableNotFoundException` error, the table is not a version 2017.11.29 (Legacy) replica. 

An example CLI command for `describe-global-table`: 

```
aws dynamodb describe-global-table \
--global-table-name users \
--region us-east-2
```
 

The command returns a successful response, so this table is a version 2017.11.29 (Legacy) global table replica. 

```
{
    "GlobalTableDescription": {
        "ReplicationGroup": [
            {
                "RegionName": "us-west-2"
            },
            {
                "RegionName": "us-east-2"
            }
        ],
        "GlobalTableArn": "arn:aws:dynamodb::123456789012:global-table/users",
        "CreationDateTime": "2025-06-10T13:55:53.630000-04:00",
        "GlobalTableStatus": "ACTIVE",
        "GlobalTableName": "users"
    }
}
```
 

### Determining the version using the DynamoDB Console 

To identify the version of a global table replica, perform the following: 
Open the DynamoDB console at https://console.aws.amazon.com/dynamodb/home. 
In the navigation pane on the left side of the console, choose Tables. 
Choose the table you want to identify the global tables version for. 
Choose the Global Tables tab. 

The Summary section displays the version of global tables in use. 
 

## Differences in behavior between Legacy and Current versions 

The following list describes the differences in behavior between the Legacy and Current versions of global tables.  
version 2019.11.21 (Current) consumes less write capacity for several DynamoDB operations compared to version 2017.11.29 (Legacy), and therefore, is more cost-effective for most customers. The differences for these DynamoDB operations are as follows:  
Invoking PutItem for a 1KB item in a Region and replicating to other Regions requires 2 rWRUs per region for 2017.11.29 (Legacy), but only 1 rWRU for 2019.11.21 (Current). 
Invoking UpdateItem for a 1KB item requires 2 rWRUs in the source Region and 1 rWRU per destination Region for 2017.11.29 (Legacy), but only 1 rWRU for both source and destination Regions for 2019.11.21 (Current). 
Invoking DeleteItem for a 1KB item requires 1 rWRU in the source Region and 2 rWRUs per destination Region for 2017.11.29 (Legacy), but only 1 rWRU for both source or destination Region for 2019.11.21 (Current). 
 

The following table shows the rWRU consumption of 2017.11.29 (Legacy) and 2019.11.21 (Current) tables for a 1KB item in two Regions.  
|  Operation |  2017.11.29 (Legacy) |  2019.11.21 (Current) |  Savings |    
|  PutItem |  4 rWRUs |  2 rWRUs |  50% |   
|  UpdateItem |  3 rWRUs |  2 rWRUs |  33% |   
|  DeleteItem |  3 rWRUs |  2 rWRUs |  33% |    
version 2017.11.29 (Legacy) is available in only 11 AWS Regions. However, version 2019.11.21 (Current) is available in all the AWS Regions. 
You create version 2017.11.29 (Legacy) global tables by first creating a set of empty Regional tables, then invoking the CreateGlobalTable API to form the global table. You create version 2019.11.21 (Current) global tables by invoking the UpdateTable API to add a replica to an existing Regional table. 
version 2017.11.29 (Legacy) requires you to empty all replicas in the table before adding a replica in a new Region (including during creation). version 2019.11.21 (Current) supports you to add and remove replicas to Regions on a table that already contains data. 
version 2017.11.29 (Legacy) uses the following dedicated set of control plane APIs for managing replicas:  
CreateGlobalTable 
DescribeGlobalTable 
DescribeGlobalTableSettings 
ListGlobalTables 
UpdateGlobalTable 
UpdateGlobalTableSettings 
 

version 2019.11.21 (Current) uses the DescribeTable and UpdateTable APIs to manage replicas. 
version 2017.11.29 (Legacy) publishes two DynamoDB Streams records for each write. version 2019.11.21 (Current) only publishes one DynamoDB Streams record for each write. 
version 2017.11.29 (Legacy) populates and updates the `aws:rep:deleting`, `aws:rep:updateregion`, and `aws:rep:updatetime` attributes. version 2019.11.21 (Current) does not populate or update these attributes. 
version 2017.11.29 (Legacy) does not synchronize Using time to live (TTL) in DynamoDB settings across replicas. version 2019.11.21 (Current) synchronizes TTL settings across replicas. 
version 2017.11.29 (Legacy) does not replicate TTL deletes to other replicas. version 2019.11.21 (Current) replicates TTL deletes to all replicas. 
version 2017.11.29 (Legacy) does not synchronize auto scaling settings across replicas. version 2019.11.21 (Current) synchronizes auto scaling settings across replicas. 
version 2017.11.29 (Legacy) does not synchronize global secondary index (GSI) settings across replicas. version 2019.11.21 (Current) synchronizes GSI settings across replicas. 
version 2017.11.29 (Legacy) does not synchronize encryption at rest settings across replicas. version 2019.11.21 (Current) synchronizes encryption at rest settings across replicas. 
version 2017.11.29 (Legacy) publishes the `PendingReplicationCount` metric. version 2019.11.21 (Current) does not publish this metric. 
 

## Upgrading to the current version 

### Required permissions for global tables upgrade 

To upgrade to version 2019.11.21 (Current), you must have `dynamodb:UpdateGlobalTableversion` permissions in all Regions with replicas. These permissions are required in addition to the permissions needed for accessing the DynamoDB console and viewing tables. 

The following IAM policy grants permissions to upgrade any global table to version 2019.11.21 (Current). 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dynamodb:UpdateGlobalTableversion",
            "Resource": "*"
        }
    ]
}
```
 

The following IAM policy grants permissions to upgrade only the `Music` global table with replicas in two Regions to version 2019.11.21 (Current). 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dynamodb:UpdateGlobalTableversion",
            "Resource": [
                "arn:aws:dynamodb::123456789012:global-table/Music",
                "arn:aws:dynamodb:ap-southeast-1:123456789012:table/Music",
                "arn:aws:dynamodb:us-east-2:123456789012:table/Music"
            ]
        }
    ]
}
```
 

### What to expect during the upgrade  
All global table replicas will continue to process read and write traffic while upgrading. 
The upgrade process requires between a few minutes to several hours depending on the table size and number of replicas. 
During the upgrade process, the value of TableStatus will change from `ACTIVE` to `UPDATING`. You can view the status of the table by invoking the DescribeTable API, or with the Tables view in the DynamoDB console. 
Auto scaling will not adjust the provisioned capacity settings for a global table while the table is being upgraded. We strongly recommend that you set the table to on-demand capacity mode during the upgrade. 
If you choose to use provisioned capacity mode with auto scaling during the upgrade, you must increase the minimum read and write throughput on your policies to accommodate any expected increases in traffic to avoid throttling during the upgrade. 
The `ReplicationLatency` metric can temporarily report latency spikes or stop reporting metric data during the upgrade process. See, ReplicationLatency, for more information.  
When the upgrade process is complete, your table status will change to `ACTIVE`. 
 

### DynamoDB Streams behavior before, during, and after upgrade  
|  Operation |  Replica Region |  Behavior before upgrade |  Behavior during upgrade |  Behavior after upgrade |    
|  

Put or Update |  

Source |  Timestamp population happens using UpdateItem. |  Timestamp population happens using PutItem. |  No customer visible timestamp is generated. |   
|  Two Streams records are generated. The first record contains the customer written attributes. The second record contains the `aws:rep:*` attributes. |  Two Streams records are generated. The first record contains the customer written attributes. The second record contains the `aws:rep:*` attributes. |  A single Streams record is generated containing the customer-writen attributes. |   
|  Two rWCUs are consumed for each customer write. |  Two rWCUs are consumed for each customer write. |  One rWCU is consumed for each customer write. |   
|  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` metric is published in CloudWatch. |   
|  

Destination |  Replication happens using PutItem. |  Replication happens using PutItem. |  Replication happens using PutItem. |   
|  A single Streams record is generated, which contains both the customer-written attributes and the `aws:rep:*` attributes. |  A single Streams record is generated, which contains both the customer-written attributes and the `aws:rep:*` attributes. |  A single Streams record is generated, which contains the customer-written attributes only and no replication attributes. |   
|  One rWCU is consumed if the item exists in the destination Region. Two rWCUs are consumed if the item doesn't exist in the destination Region. |  One rWCU is consumed if the item exists in the destination Region. Two rWCUs are consumed if the item doesn't exist in the destination Region. |  One rWCU is consumed for each customer write. |   
|  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` metric is published in CloudWatch. |   
|  

Delete |  

Source |  Delete any item with smaller timestamp using DeleteItem. |  Delete any item with smaller timestamp using DeleteItem. |  Delete any item with smaller timestamp using DeleteItem. |   
|  A single Streams record is generated, which contains both the customer-written attributes and the `aws:rep:*` attributes. |  A single Streams record is generated, which contains both the customer-written attributes and the `aws:rep:*` attributes. |  A single Streams record is generated, which contains the customer-written attributes. |   
|  One rWCU is consumed for each customer delete. |  One rWCU is consumed for each customer delete. |  One rWCU is consumed for each customer delete. |   
|  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` metric is published in CloudWatch. |   
|  

Destination |  

Two-phase deletes take place:  
In Phase 1, UpdateItem sets the deleting flag. 
In Phase 2, DeleteItem deletes the item. 
  |  Deletes the item using DeleteItem. |  Deletes the item using DeleteItem. |   
|  Two Streams records are generated. The first record contains the change to the `aws:rep:deleting` field. The second record contains the customer-written attributes and the `aws:rep:*` attributes. |  A single Stream record is generated, which contains the customer-written attributes. |  A single Stream record is generated, which contains the customer-written attributes. |   
|  Two rWCUs are consumed for each customer delete. |  One rWCU is consumed for each customer delete. |  One rWCU is consumed for each customer delete. |   
|  `ReplicationLatency` and `PendingReplicationCount` metrics are published in CloudWatch. |  `ReplicationLatency` metric is published in CloudWatch. |  `ReplicationLatency` metric is published in CloudWatch. |    

### Upgrading to version 2019.11.21 (Current) 

Perform the following steps to upgrade your version of DynamoDB global tables using the AWS Management Console. To upgrade global tables to version 2019.11.21 (Current)
Open the DynamoDB console at https://console.aws.amazon.com/dynamodb/home.  
In the navigation pane on the left side of the console, choose Tables, and then select the global table that you want to upgrade to version 2019.11.21 (Current).  
Choose the Global Tables tab. 
Choose Update version.    
Read and agree to the new requirements, and then choose Update version. 
After the upgrade process is complete, the global tables version that appears on the console changes to 2019.11.21.
