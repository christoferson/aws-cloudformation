> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/global-tables-billing.html
> Downloaded: 2026-10-24

# Understanding Amazon DynamoDB billing for global tables

This guide describes how DynamoDB billing works for global tables, identifying the components that contribute to the cost of global tables, including a practical example. 

Amazon DynamoDB global tables is a fully managed, serverless, multi-Region, and multi-active database. Global tables are designed for 99.999% availability, delivering increased application resiliency, and improved business continuity. Global tables replicate your DynamoDB tables automatically across your choice of AWS Regions so you can achieve fast, local read and write performance.  

## How it works 

The billing model for global tables differs from single-Region DynamoDB tables. Write operations for single-Region DynamoDB tables are billed using the following units:  
Write Request Units (WRUs) for on-demand capacity mode, where one WRU is charged for each write up to 1KB 
Write Capacity Units (WCUs) for provisioned capacity mode, where one WCU provides one write per second for up to 1 KB 
 

When you create a global table by adding a replica table to an existing single-Region table, that single-Region table becomes a replica table, which means the units used to bill for writes to the table also change. Write operations to replica tables are billed using the following units:   
Replicated Write Request Units (rWRUs) for on-demand capacity mode, where one rWRU per replica table is charged for each write up to 1KB 
Replicated Write Capacity Units (rWCUs) for provisioned capacity mode, where one WCU per replica table provides one write per second for up to 1 KB 
 

Updates to Global Secondary Indexes (GSIs) are billed using the same units as single-Region DynamoDB tables, even if the base table for the GSI is a replica table. Update operations for GSIs are billed using the following units:  
Write Request Units (WRUs) for on-demand capacity mode, where one WRU is charged for each write up to 1KB 
Write Capacity Units (WCUs) for provisioned capacity mode, where one WCU provides one write per second for up to 1 KB 
 

Replicated write units (rWCUs and rWRUs) are priced the same as single-Region write units (WCUs and WRUs). Replicated write (rWCU or rWRU) charges are incurred in every Region containing a replica table for the global table. DynamoDB does not charge cross-Region data transfer fees for replicating data between the Regions of a global table. 

Read operations from single-Region tables and from replica tables use the following units::  
Read Request Units (RRUs) for on-demand capacity mode, where one RRU is charged for each strongly consistent read up to 4KB 
Read Capacity Units (RCUs) for provisioned tables, where one RCU provides one strongly consistent read per second for up to 4KB 
 

## Consistency modes and billing 

The replicated write units (rWCUs and rWRUs) used to bill for write operations are identical for both multi-Region strong consistency (MRSC) and multi-Region eventual consistency (MREC) modes. Global tables using multi-Region strong consistency (MRSC) mode configured with a witness don't incur replicated write unit costs (rWCUs and rWRUs), storage costs, or data transfer costs for replication to the witness. 

## DynamoDB global tables billing example 

Let's walk through a multi-day example scenario to see how global table write request billing works in practice (note that this example only considers write requests, and does not include the table restore charges that would be incurred when adding a replica in the example): 

Day 1 - Single-Region table: You have a single-Region on-demand DynamoDB table named Table_A in the us-west-2 Region. You write 100 1KB items to Table_A. For these single-Region write operations, you are charged 1 write request unit (WRU) per 1KB written. Your day 1 charges are:  
100 WRUs in the us-west-2 Region for single-Region writes 
 

The total request units charged on day 1: 100 WRUs. 

Day 2 - Creating a global table: You create a global table by adding a replica to Table_A in the us-east-2 Region. Table_A is now a global table with two replica tables; one in the us-west-2 Region, and one in the us-east-2 Region. You write 150 1KB items to the replica table in the us-west-2 Region. Your day 2 charges are:  
150 rWRUs in the us-west-2 Region for replicated writes 
150 rWRUs in the us-east-2 Region for replicated writes 
 

The total request units charged on day 2: 300 rWRUs. 

Day 3 - Adding a Global Secondary Index: You add a global secondary index (GSI) to the replica table in the us-east-2 Region that projects all attributes from the base (replica) table. The global table automatically creates the GSI on the replica table in the us-west-2 Region for you. You write 200 new 1KB records to the replica table in the us-west-2 Region. Your day 3 charges are:  
• 200 rWRUs in the us-west-2 Region for replicated writes 
• 200 WRUs in the us-west-2 Region for GSI updates 
• 200 rWRUs in the us-east-2 Region for replicated writes 
• 200 WRUs in the us-east-2 Region for GSI updates 
 

The total write request units charged on day 3: 400 WRUs and 400 rWRUs. 

The total write unit charges for all three days are 500WRUs (100 WRU on day 1 + 400 WRUs on day 3) and 700 rWRUs (300 rWRUs on Day2 + 400 rWRUs on Day 3). 

In summary, replica table write operations are billed in replicated write units in all Regions that contain a replica table. If you have global secondary indexes, you are charged write units for updates to GSIs in all regions that contain a GSI (which in a global table is all Regions that contain a replica table).
