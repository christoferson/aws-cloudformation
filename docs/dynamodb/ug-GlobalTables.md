> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
> Downloaded: 2026-10-24

# Global tables - multi-active, multi-Region replication

Amazon DynamoDB global tables is a fully managed, multi-Region, and multi-active database feature that provides easy to use data replication and fast local read and write performance for globally scaled applications.

Global tables automatically replicate your DynamoDB table data across AWS Regions and optionally across AWS accounts without requiring you to build and maintain your own replication solution. Global tables are ideal for applications requiring business continuity and high availability through multi-Region deployment. Any global table replica can serve reads and writes. Applications can achieve high resilience with a low or zero Recovery Point Objective (RPO) by shifting traffic to a different Region if application processing is interrupted in a Region. Global tables are available in all Regions where DynamoDB is available. 

## Consistency modes 

When you create a global table, you can configure its consistency mode. Global tables support two consistency modes: multi-Region eventual consistency (MREC) and multi-Region strong consistency (MRSC). 

If you do not specify a consistency mode when creating a global table, the global table defaults to multi-Region eventual consistency (MREC). A global table cannot contain replicas configured with different consistency modes. You cannot change a global table's consistency mode after creation. 

## Account configurations 

DynamoDB now supports two global tables models, each designed for different architectural patterns:  
Same-account global tables – All replicas are created and managed within a single AWS account. 
Multi-account global tables – Replicas are deployed across multiple AWS accounts while participating in a shared replication group. 
 

Both same-account and multi-account models support multi-Region writes, asynchronous replication, last-writer-wins conflict resolution, and the same billing model. However, they differ in how accounts, permissions, encryption, and table governance are managed. 

Global tables configured for MRSC only support same-account configurations. 

You can configure a global table using the AWS Management Console. Global tables use existing DynamoDB APIs to read and write data to your tables, so no application changes are required. You pay only for the resources you provision or use, with no upfront costs or commitments. Comparison of same-account and multi-account global tables 
|  Properties |  Same-Account global tables |  Multi-account global tables |    
|  Primary use case |  Multi-Region resiliency for applications within a single AWS account |  Multi-Region, multi-account replication for applications owned by different teams, distinct business units, or strong security boundaries across accounts |   
|  Account model |  All replicas created and managed in one AWS account |  Replicas created across multiple AWS accounts within the same deployment |   
|  Resource ownership |  A single account owns the table and all replicas |  Each account owns its local replica; replication group spans accounts |   
|  Version supported |  Global tables version 2019.11.21 (Current) and Version 2017.11.29 (Legacy) |  Global tables version 2019.11.21 (Current) |   
|  Control plane operations |  Create, modify, and delete replicas through the table owner account |  Distributed control-plane operations: accounts join or leave the replication group |   
|  Data plane operations |  Standard DynamoDB endpoints per Region |  Data-plane access per account/Region; routing through replication group |   
|  Security boundary |  A single IAM and KMS boundary |  Distinct IAM, KMS, billing, CloudTrail, and governance per account |   
|  Best fit |  Organizations with centralized ownership of tables |  Organizations with federated teams, governance boundaries, or multi-account setups |   Topics
Global tables core concepts
DynamoDB same-account global table
DynamoDB multi-account global tables
Disassociating a global table replica
Understanding Amazon DynamoDB billing for global tables
DynamoDB global tables versions
Best practices for global tables
