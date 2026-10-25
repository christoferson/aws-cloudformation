> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html
> Downloaded: 2026-10-24

# Document history for DynamoDB

The following table describes the important changes in each release of the DynamoDB Developer Guide from July 3, 2018 onward. For notification about updates to this documentation, you can subscribe to the RSS feed (at the top left corner of this page).
| Change | Description | Date | 
| 

Disassociate a global table replica | 

Added instructions for disassociating an MREC global table replica while retaining its regional table and data. The procedure applies to same-account and multi-account global tables. For more information, see Disassociating a global table replica. | 

October 20, 2026 | 
| 

DynamoDB export to Amazon S3 now supports filtered export | 

You can now export a subset of your DynamoDB table data to Amazon S3 instead of the entire table. To do this, provide key condition, filter, and projection expressions on your export request. Filtered export works with both full exports and incremental exports. For more information, see DynamoDB data export to Amazon S3: how it works. | 

October 1, 2026 | 
| 

Expanded agentic AI documentation with vector search guidance and AI framework connectors | 

Refreshed the agentic AI chapter with vector search guidance for RAG and agent memory, and added deep-dive topics for the Strands Agents, LangChain, and LangGraph connectors, covering session persistence, chat history, long-term agent memory, and semantic search. For more information, see Using agentic AI with DynamoDB. | 

August 31, 2026 | 
| 

DAX now supports AWS PrivateLink in commercial and China Regions | 

Added guidance for using AWS PrivateLink with DynamoDB Accelerator (DAX) to help users establish private, secure connectivity to DAX control plane endpoints within the same AWS Region. For more information, see Generate infrastructure code for Amazon DynamoDB using Console-to-Code. | 

October 30, 2025 | 
| 

DynamoDB now supports Internet Protocol version 6 (IPv6) | 

DynamoDB now supports Internet Protocol version 6 (IPv6) addresses in your Amazon VPC when you connect to DynamoDB tables, streams, and DAX, including with AWS PrivateLink Gateway and Interface endpoints. You can use IPv6 to simplify your network stack and meet compliance requirements with a network that supports both IPv4 and IPv6. | 

October 3, 2025 | 
| 

Added documentation for the new Console-to-Code feature for DynamoDB | 

Console-to-Code transforms manual DynamoDB table creation steps in the AWS Management Console into automated, reproducible infrastructure code across multiple formats like AWS CDK and CloudFormation. For more information, see Generate infrastructure code for Amazon DynamoDB using Console-to-Code. | 

September 23, 2025 | 
| 

Released DynamoDB Local version 3.1.0 | 

This update improves performance for PartiQL queries, including Joda-time dependency. | 

September 14, 2025 | 
| 

DynamoDB has enhanced its throttling diagnostics capabilities with a new CloudWatch Contributor Insights mode, added throttling exception details, and targeted CloudWatch metrics | 

DynamoDB provides enhanced throttling diagnostics with a new `Throttled keys` only mode in CloudWatch Contributor Insights that specifically tracks the most throttled partition keys, more detailed throttling exceptions that include structured `ThrottlingReason` fields, providing specific reason codes and resource ARNs to help identify exactly what resource is throttled and why, and 16 new targeted CloudWatch metrics that correspond to different throttling scenario, for precise monitoring of specific throttling events. For more information, see Troubleshooting throttling in DynamoDB. | 

August 14, 2025 | 
| 

Increased limit for switching between capacity modes | 

Increased the limit for switching a table from provisioned to on-demand capacity mode from once every 24 hours to four times every 24 hours. This change provides more flexibility for workloads that require loading large volumes of data multiple times per day or need to accommodate unexpected traffic increases. For more information, see  Considerations when switching capacity modes in DynamoDB. | 

August 12, 2025 | 
| 

Released DynamoDB Local version 3.0, which migrates from AWS SDK for Java V1 to V2 | 

This update removes the V1 dependency, improves performance, and aligns with the AWS SDK V2 package structure. | 

July 17, 2025 | 
| 

Added support for optimized shard discovery in DynamoDB Streams | 

The new shard discovery mechanism reduces initial discovery time, improves steady-state processing performance, provides visibility into processing status, and maintains consistent p100 latency across large-scale operations. For more information, see AWS PrivateLink for Amazon DynamoDB Streams. | 

July 17, 2025 | 
| 

Added Multi-Region Strong Consistency (MRSC) support for DynamoDB global tables | 

DynamoDB now supports Multi-Region Strong Consistency (MRSC) for global tables with optional witness Region. MRSC allows strongly consistent reads across Regions with a Recovery Point Objective (RPO) of zero during regional failures. MRSC global tables must be deployed in exactly three Regions, with either three replicas or two replicas and one witness. For more information and available Regions, see Multi-Region strong consistency (MRSC). | 

June 30, 2025 | 
| 

Amazon DynamoDB Streams Kinesis Client Library (KCL) 2.x adapter | 

DynamoDB now supports an upgraded DynamoDB Streams adapter compatible with KCL 2.x and AWS SDK v2. For more information, see Migrating from KCL1.x to KCL 3.x. | 

June 11, 2025 | 
| 

Added support for running DynamoDB local in AWS CloudShell | 

You can now run DynamoDB local directly in your browser through the AWS Management Console without downloading or installing software. For more information, see Deploying DynamoDB locally on your computer. | 

May 19, 2025 | 
| 

Added support for r7i instance types in DAX | 

Expanded instance type options for DAX to provide more flexibility in performance and capacity. For more details about the new r7i instance types and their capabilities, see  DAX encryption at rest. | 

April 29, 2025 | 
| 

New scoped-down full access policy AmazonDynamoDBFullAccess_v2 replaces AmazonDynamoDBFullAccess. | 

Effective April 25, 2025, DynamoDB has deprecated the `AmazonDynamoDBFullAccess` policy and replaced it with a scoped-down policy named `AmazonDynamoDBFullAccess_v2`. For more information, see AWS managed policy: AmazonDynamoDBFullAccess_v2. | 

April 28, 2025 | 
| 

DynamoDB introduces AWS PrivateLink support for DynamoDB Streams | 

AWS added AWS PrivateLink support for DynamoDB Streams, enabling customers to invoke DynamoDB Streams APIs from within Amazon Virtual Private Cloud (VPC) using private network connectivity. This feature allows simplified private network access without traversing the public internet, supporting compliance and security requirements for DynamoDB workloads. For more information, see AWS PrivateLink for Amazon DynamoDB Streams. | 

March 26, 2025 | 
| 

DAX SDK For JS 3.x and Go 2.x is now available | 

DynamoDB Accelerator (DAX) SDK for JS 3.x is now available and is compatible with the AWS SDK for Java 3.x. | 

March 17, 2025 | 
| 

NoSQL Workbench 3.13.5 on-demand capacity mode for default table settings release | 

When you create a table with default settings, DynamoDB creates a table that uses on-demand capacity mode instead of provisioned capacity mode. | 

February 24, 2025 | 
| 

New best practice for configuring your DAX client | 

Published a new DAX prescriptive guidance best practices topic for configuring your DAX client. For more information, see  Configuring your DAX client. | 

February 17, 2025 | 
| 

New best practices for bulk data operations | 

Published new best practices topics for working with complex data models in DynamoDB. For more information, see  Best practices for using bulk data operations in DynamoDB. | 

January 9, 2025 | 
| 

Amazon DynamoDB now supports configurable point-in-time recovery (PITR) | 

DynamoDB now supports configurable recovery periods for PITR. You can now set the PITR period for each table to between 1 and 35 days. For more information, see Point-in-time backups for DynamoDB. | 

January 7, 2025 | 
| 

Published new topic on integrating Amazon Managed Streaming for Apache Kafka with Amazon DynamoDB | 

Learn how Amazon Managed Streaming for Apache Kafka integrates with Amazon DynamoDB by reading data from Apache Kafka topics and storing it in DynamoDB. For more information, see Integrating DynamoDB with Amazon Managed Streaming for Apache Kafka. | 

December 26, 2024 | 
| 

DynamoDB introduces support for a zero-ETL integration with SageMaker AI Lakehouse | 

DynamoDB introduces a zero-ETL integration that automates the extracting and loading of data from Amazon DynamoDB into a customer's data lake. For more information, see DynamoDB zero-ETL integration with SageMaker AI Lakehouse. | 

December 3, 2024 | 
| 

DynamoDB global tables now supports multi-Region strong consistency | 

With multi-Region strong consistency, you can build highly available multi-Region applications with a recovery point objective (RPO) of zero, achieving the highest level of resilience. For more information, see Global tables with multi-Region strong consistency. | 

December 3, 2024 | 
| 

DynamoDB managed policy update | 

Added two new permissions to the `AmazonDynamoDBReadOnlyAccess` managed policy: `dynamodb:GetAbacStatus` and `dynamodb:UpdateAbacStatus`. These permissions allow you to view the ABAC status and enable ABAC for your AWS account in the current Region. For more information, see AWS managed policy: AmazonDynamoDBReadOnlyAccess. | 

November 18, 2024 | 
| 

DynamoDB introduces support for attribute-based access control (ABAC) | 

ABAC is an authorization strategy that lets you define access permissions based on tags attached to users, roles, and AWS resources. ABAC uses tag-based conditions in your AWS Identity and Access Management (IAM) policies or other policies to allow or deny specific actions on your tables or indexes when IAM principals’ tags match the tags for the tables. For more information, see Using attribute-based access control with DynamoDB. | 

November 18, 2024 | 
| 

DynamoDB introduces warm throughput for on-demand and provisioned tables | 

DynamoDB now supports warm throughput. Warm throughput provides visibility into the number of read and write operations your DynamoDB table can instantaneously support as well as the ability to pre-warm your DynamoDB tables. For more information, see DynamoDB warm throughput. | 

November 13, 2024 | 
| 

Ability to consume Amazon DynamoDB Streams records with Apache Flink | 

You can now consume Amazon DynamoDB Streams records with Apache Flink and leverage the Amazon Managed Service for Apache Flink to quickly build and manage end-to-end stream processing applications. For more information, see DynamoDB Streams and Apache Flink. | 

November 12, 2024 | 
| 

Published new billing topics for global tables and backups | 

Published two new topics regarding billing for global tables and billing for backups. For more information, see Understanding Amazon DynamoDB billing for global tables and Understanding Amazon DynamoDB billing for backups. | 

October 16, 2024 | 
| 

Amazon DynamoDB zero-ETL integration with Amazon Redshift | 

Amazon DynamoDB zero-ETL integration with Amazon Redshift provides a no-code, fully managed ETL pipeline with replication from DynamoDB to Amazon Redshift. For more information, see Amazon DynamoDB zero-ETL integration with Amazon Redshift. | 

October 15, 2024 | 
| 

Documentation-only update to add a topic about using generative AI with DynamoDB | 

Published a new topic that provides information about using generative AI with DynamoDB, including examples of gen AI use cases for DynamoDB. For more information, see Using generative AI with DynamoDB. | 

October 11, 2024 | 
| 

SDK now supports AWS account-based endpoints | 

Added documentation for account-based endpoints and the `ACCOUNT_ID_ENDPOINT_MODE` setting for SDK clients. For more information, see SDK support of AWS account-based endpoints. | 

September 3, 2024 | 
| 

Redesigned the getting started experience | 

Redesigned the getting started experience to consolidate information and get you started with quicker onboarding. For more information, see Getting started with DynamoDB. | 

August 1, 2024 | 
| 

DAX expansion to new Regions for Spain and Sweden | 

DAX is now available in Spain and Sweden Regions. For more information, see DAX cluster components. | 

July 30, 2024 | 
| 

Restructured and consolidated the DynamoDB backup and restore documentation | 

The DynamoDB Developer Guide has a new structure for backing up and restoring. For more information, see Backup and restore for DynamoDB. | 

July 2, 2024 | 
| 

What is Amazon DynamoDB? topic rewrite | 

Published a revised and updated version of the What is Amazon DynamoDB? topic. For more information, see What is Amazon DynamoDB?. | 

June 21, 2024 | 
| 

Integrate DynamoDB Streams with EventBridge | 

Published a new topic on integrating DynamoDB Streams with EventBridge. For more information, see Integrating with EventBridge. | 

June 21, 2024 | 
| 

DAX prescriptive guidance | 

Published a new best practices topic that provides you comprehensive insights for using DynamoDB Accelerator effectively. This topic covers performance optimization, cost management, and operational best practices. For more information, see DAX prescriptive guidance.  | 

June 3, 2024 | 
| 

Migrating a DynamoDB table from one account to another | 

Added a new topic on migrating DynamoDB tables from one account to another. For more information, see Migrating a DynamoDB table from one account to another. | 

May 29, 2024 | 
| 

Restructured and consolidated the DynamoDB monitoring and logging documentation | 

A new structure for monitoring and logging in DynamoDB includes three concise chapters for metrics, logging operations, and contributor insights. | 

May 3, 2024 | 
| 

Restructured and consolidated the DynamoDB capacity mode documentation | 

DynamoDB guide now includes a new chapter that contains all information about the DynamoDB capacity modes – on-demand and provisioned. With this update, the Considerations when changing read/write Capacity Mode topic has been moved inside the Best practices chapter. This topic is now renamed as Considerations when switching capacity modes and includes elaborate information about the best practices when switching between the capacity modes. In addition, the guide now features a new chapter that includes all information about DynamoDB reads and writes, and capacity units consumptions for read and write operations. For more information, see DynamoDB throughput capacity, Considerations when switching capacity modes, and DynamoDB reads and writes. | 

May 1, 2024 | 
| 

Maximum number of on-demand requests | 

You can now specify the maximum number of on-demand requests that an individual table, index, or both, can perform. Specifying the maximum on-demand throughput will help keep your table-level usage and costs bounded and protect against inadvertent surge in consumed resources. For more information, see Maximum throughput for on-demand tables. | 

May 1, 2024 | 
| 

NoSQL Workbench operation builder improvements | 

NoSQL Workbench now includes native support for dark mode. Improved table and item operations in the operations builder. Item results and operation builder request information is available in JSON format. For more information, see NoSQL Workbench operation builder. | 

April 24, 2024 | 
| 

Resource-based policies for Amazon DynamoDB resources | 

DynamoDB now supports resource-based policies for tables, indexes, and streams. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource. For more information, see Using resource-based policies for DynamoDB. | 

March 20, 2024 | 
| 

DynamoDB managed policy update | 

Added a new permission `dynamodb:GetResourcePolicy` to the `AmazonDynamoDBReadOnlyAccess` managed policy. This permission provides access to read resource-based policies attached to DynamoDB resources. For more information, see AWS managed policy: AmazonDynamoDBReadOnlyAccess. | 

March 20, 2024 | 
| 

AWS PrivateLink for Amazon DynamoDB | 

Amazon DynamoDB now supports AWS PrivateLink. With AWS PrivateLink, you can simplify private network connectivity between virtual private clouds (VPCs), DynamoDB, and your on-premises data centers using interface VPC endpoints and private IP addresses. For more information, see AWS PrivateLink for DynamoDB. | 

March 19, 2024 | 
| 

Programming with JavaScript guide | 

Amazon DynamoDB presents a programming guide for AWS SDK for JavaScript. Learn about the AWS SDK for JavaScript, abstraction layers, configuring connection, handling errors, defining retry policies, managing keep-alive, and more. For more information, see Programming with JavaScript. | 

March 6, 2024 | 
| 

Programming with AWS SDK for Java 2.x guide | 

Created a new programming guide that goes in depth about high-level, low-level, and document interfaces, HTTP clients and their configuration, error handling, and addresses the most common configuration settings that you should consider when using the SDK for Java 2.x. For more information, see Programming Amazon DynamoDB with AWS SDK for Java 2.x. | 

March 5, 2024 | 
| 

Clone tables with NoSQL Workbench | 

Allow developers to use NoSQL Workbench to copy or clone tables between development environments and regions (DynamoDB Local and DynamoDB web). For more information, see Cloning tables with NoSQL Workbench. | 

February 26, 2024 | 
| 

Programming with Python guide | 

Created a new guide that goes in depth about both high level and low level libraries and addresses the most common configuration settings that one should consider when using the Python SDK. For more information, see Programming with Python. | 

January 5, 2024 | 
| 

Time to live (TTL) topic rewrite | 

Completely rewrote the TTL section of the guide. The new guide helps you get started with TTL by providing ready-to-use code snippets along the way. The current code snippets provided are in Python and Javascript. For more information, see TTL. | 

December 20, 2023 | 
| 

Best Practices for Understanding your AWS Billing and Usage Reports | 

Added a new section that clarifies various usage types and the charges for those usage types in DynamoDB. For more information, see  Billing and usage reports. | 

December 15, 2023 | 
| 

Amazon DynamoDB zero-ETL integration with Amazon OpenSearch Service | 

Amazon DynamoDB now supports zero-ETL integration with Amazon OpenSearch Service, which lets you perform a search on your DynamoDB data by automatically replicating and transforming it without custom code or infrastructure. For more information, see  DynamoDB zero-ETL integration with Amazon OpenSearch Service. | 

November 28, 2023 | 
| 

Migrating to DynamoDB from a relational database | 

Created a  migration guide to help users understsand how to migrate to DynamoDB from a relational database. | 

November 27, 2023 | 
| 

Generate sample data with NoSQL Workbench | 

NoSQL Workbench for Amazon DynamoDB now supports creating data models directly from  sample data model templates to help you design data schemas for your workloads. You can use this feature to get familiar with NoSQL data modeling best practices when building your applications on DynamoDB. | 

September 28, 2023 | 
| 

Incremental Export to S3 | 

You can now export data that was inserted, updated or deleted, in small increments. With  incremental export, you can export changed data ranging from a few megabytes to terabytes with a few clicks in the AWS Management Console, an API call, or the AWS Command Line Interface. | 

September 26, 2023 | 
| 

Data modeling for DynamoDB | 

You can now learn more about  data modeling with DynamoDB examples that focus on specific use cases, their access patterns, and step-by-step guidance in realizing those access patterns. | 

July 14, 2023 | 
| 

Troubleshooting section | 

You can now find  troubleshooting content for latency and throttling issues that might occur in your DynamoDB tables. | 

March 13, 2023 | 
| 

Deletion protection for Amazon DynamoDB | 

Deletion protection is now available for Amazon DynamoDB tables in all AWS Regions. DynamoDB now makes it possible for you to protect your tables from accidental deletion when performing regular table management operations. | 

March 8, 2023 | 
| 

CloudFormation support for KDSD in global tables | 

Amazon Kinesis Data Streams for DynamoDB now supports CloudFormation for DynamoDB global tables, which means you can enable streaming to an Amazon Kinesis Data Streams on your DynamoDB global tables with CloudFormation templates. | 

February 15, 2023 | 
| 

DynamoDB local supports 100 actions per transaction | 

You can now perform up to 100 actions in a single transaction on DynamoDB local. | 

February 9, 2023 | 
| 

Using the DynamoDB Well-Architected Lens to optimize your DynamoDB workload | 

You can now use the DynamoDB Well-Architected Lens, a collection of design principles and guidance that you can use for designing well-architected DynamoDB workloads. | 

February 3, 2023 | 
| 

PartiQL GovGloud availability | 

PartiQL—a SQL-compatible query language for Amazon DynamoDB is now supported in AWS GovCloud (US-East) and AWS GovCloud (US-West). | 

December 21, 2022 | 
| 

Single installation suite for NoSQL Workbench and DynamoDB local | 

NoSQL Workbench for DynamoDB now includes a guided DynamoDB local installation process to streamline setting up your DynamoDB local development environment. | 

December 6, 2022 | 
| 

Bulk import from S3 | 

Amazon DynamoDB now makes it easier for you to migrate and load data into new DynamoDB tables by supporting bulk data imports from Amazon S3. | 

August 18, 2022 | 
| 

Enhanced integration with Service Quotas | 

Service Quotas now enables you to proactively manage your account and table quotas. You can view current values, set alarms for when your utilization of a quota exceeds a configurable threshold, and more. | 

June 15, 2022 | 
| 

NoSQL Workbench adds table and GSI support | 

You can now use NoSQL Workbench for table and global secondary index (GSI) control plane operations such as CreateTable, UpdateTable, and DeleteTable. | 

June 2, 2022 | 
| 

Standard-infrequent access table class now available in China | 

Amazon DynamoDB Standard-Infrequent Access table class is available in China Regions. Reduce your DynamoDB costs by up to 60 percent, by using this new table class for tables that store infrequently accessed data.  | 

April 18, 2022 | 
| 

Increase in default service quotas and table management operations | 

DynamoDB increased the default quota for the number of tables per account and Region from 256 to 2,500 tables, and increased the number of concurrent table management operations from 50 to 500. | 

March 9, 2022 | 
| 

Optional limiting of items with PartiQL for DynamoDB | 

DynamoDB can limit the number of items processed in PartiQL for DynamoDB operations as an optional parameter on each request.  | 

March 8, 2022 | 
| 

AWS Backup integration available in China (Beijing and Ningxia) Regions | 

AWS Backup now integrates with DynamoDB in the China (Beijing and Ningxia) Regions. You can meet compliance and business continuity requirements more easily through enhanced backup features in AWS Backup, such as cross-account and cross-Region backups. | 

January 26, 2022 | 
| 

Throughput capacity information through PartiQL API calls | 

DynamoDB can return the throughput capacity consumed by PartiQL API calls to help you optimize your queries and throughput costs. | 

January 18, 2022 | 
| 

AWS Backup integration | 

DynamoDB now helps you meet compliance and business continuity requirements more easily through enhanced backup features in AWS Backup, such as cross-account and cross-Region backups. | 

November 24, 2021 | 
| 

NoSQL Workbench import/export datasets in CSV | 

NoSQL Workbench for Amazon DynamoDB now enables you to import and automatically populate sample data to help build and visualize your data models. | 

October 11, 2021 | 
| 

Filter and retrieve Amazon DynamoDB Streams data-plane activity with AWS CloudTrail | 

Amazon DynamoDB now provides you more granular control of audit logging by enabling you to filter Streams data-plane API activity in AWS CloudTrail. | 

September 22, 2021 | 
| 

Updated console | 

The DynamoDB console is now your default console to help you manage data more easily, simplify your common tasks, and give you faster access to resources and features. | 

August 25, 2021 | 
| 

DAX SDK For Java 2.x is now available | 

DynamoDB Accelerator (DAX) SDK for Java 2.x is now available and is compatible with the AWS SDK for Java 2.x. You can benefit from the latest features, including non-blocking I/O. | 

July 29, 2021 | 
| 

NoSQL Workbench feature updates including control plane operations | 

NoSQL Workbench for Amazon DynamoDB now helps you run frequent operations more easily to modify and access table data. | 

July 28, 2021 | 
| 

DynamoDB global tables are now available in the Asia Pacific Region | 

DynamoDB global tables are now available in the Asia Pacific (Osaka) Region. Replicate your DynamoDB tables automatically across your choice of 22 AWS Regions. | 

July 28, 2021 | 
| 

DAX is now available in China | 

DynamoDB Accelerator (DAX) is now available in the China (Beijing) Region, operated by Sinnet. | 

July 28, 2021 | 
| 

DAX encryption in transit | 

DynamoDB Accelerator (DAX) now supports encryption in transit of data between your applications and DAX clusters, and between the nodes within a DAX cluster. | 

July 24, 2021 | 
| 

CloudFormation and CloudTrail integration | 

Integration with AWS CloudFormation and security enhancements with CloudFormation data-plane logging. | 

June 18, 2021 | 
| 

CloudFormation now supported for global tables | 

Amazon DynamoDB global tables now support AWS CloudFormation, which means you can create global tables and manage their settings with CloudFormation templates. | 

May 14, 2021 | 
| 

Amazon DynamoDB local support for Java 2.x | 

You now can use the AWS SDK for Java 2.x with DynamoDB local, the downloadable version of Amazon DynamoDB. With DynamoDB local, you can develop and test applications by using a version of DynamoDB running in your local development environment without incurring any additional costs. | 

May 3, 2021 | 
| 

NoSQL Workbench now supports AWS CloudFormation | 

NoSQL Workbench for Amazon DynamoDB now supports AWS CloudFormation, so you can manage and modify DynamoDB data models with CloudFormation templates. In addition, you now can configure table capacity settings in NoSQL Workbench. | 

April 22, 2021 | 
| 

DynamoDB and AWS Amplify now feature integration | 

AWS Amplify now orchestrates multiple DynamoDB global secondary index updates in a single deployment. | 

April 20, 2021 | 
| 

AWS CloudTrail to log Amazon DynamoDB Streams data-plane APIs | 

You now can use AWS CloudTrail to log Amazon DynamoDB Streams data-plane API activity, and monitor and investigate item-level changes in your DynamoDB tables. | 

April 20, 2021 | 
| 

Amazon Kinesis Data Streams for Amazon DynamoDB now supports AWS CloudFormation | 

Amazon Kinesis Data Streams for Amazon DynamoDBnow supports AWS CloudFormation, which means you can enable streaming to an Amazon Kinesis data stream on your DynamoDB tables with CloudFormation templates. By streaming your DynamoDB data changes to a Kinesis data stream, you can build advanced streaming applications with AAmazon Kinesis services. | 

April 12, 2021 | 
| 

Amazon Keyspaces now offers FIPS 140-2 compliant endpoints | 

Amazon Keyspaces (for Apache Cassandra) now offers Federal Information Processing Standards (FIPS) 140-2 compliant endpoints to help you run highly regulated workloads more easily. FIPS 140-2 is a US and Canadian government standard that specifies the security requirements for cryptographic modules that protect sensitive information. | 

April 8, 2021 | 
| 

Amazon EC2 T3 instances for DAX | 

DAX now supports Amazon EC2 T3 instance types, which provide a baseline level of CPU performance with the ability to burst above the baseline when needed. | 

February 15, 2021 | 
| 

NoSQL Workbench for Amazon DynamoDB support for PartiQL | 

You now can use the NoSQL Workbench for DynamoDB to build PartiQL statements for DynamoDB. | 

December 4, 2020 | 
| 

PartiQL for DynamoDB | 

You now can use PartiQL for DynamoDB—a SQL-compatible query language—to interact with DynamoDB tables and run ad hoc queries by using the AWS Management Console, AWS Command Line Interface, and DynamoDB APIs for PartiQL. | 

November 23, 2020 | 
| 

Amazon Kinesis Data Streams for Amazon DynamoDB | 

You now can use Amazon Kinesis Data Streams for Amazon DynamoDB with your DynamoDB tables to capture item-level changes and replicate them to a Kinesis data stream. | 

November 23, 2020 | 
| 

DynamoDB table export | 

You can now export your DynamoDB tables to Amazon S3, enabling you to perform analytics and complex queries on your data with services like Athena, AWS Glue, and Lake Formation. | 

November 9, 2020 | 
| 

Support for empty values | 

DynamoDB now supports empty values for non-key String and Binary attributes in DynamoDB tables. Empty value support gives you greater flexibility to use attributes for a broader set of use cases without having to transform such attributes before sending them to DynamoDB. List, Map, and Set data types also support empty String and Binary values. | 

May 18, 2020 | 
| 

NoSQL Workbench for Amazon DynamoDB support for Linux | 

NoSQL Workbench for Amazon DynamoDB is now supported on Linux- Ubuntu , Fedora and Debian. | 

May 4, 2020 | 
| 

CloudWatch Contributor Insights for DynamoDB – GA | 

CloudWatch Contributor Insights for DynamoDB is generally available. CloudWatch Contributor Insights for DynamoDB is a diagnostic tool that provides an at-a-glance view of your DynamoDB table's traffic trends and helps you identify your table's most frequently accessed keys (also known as hot keys). | 

April 2, 2020 | 
| 

Upgrading global tables | 

You now can update your global tables from version 2017.11.29 to the latest version of global tables (2019.11.21), with a few clicks in the DynamoDB Console. By upgrading the version of your global tables, you can increase the availability of your DynamoDB tables easily by extending your existing tables into additional AWS Regions, with no table rebuilds required.  | 

March 16, 2020 | 
| 

NoSQL Workbench for Amazon DynamoDB – GA | 

NoSQL Workbench for Amazon DynamoDB is generally available. Use the NoSQL Workbench to design, create, query, and manage DynamoDB tables. | 

March 2, 2020 | 
| 

DAX cache cluster metrics | 

DAX support for new CloudWatch metrics, that allow you to better understand your DAX cluster's performance.  | 

February 6, 2020 | 
| 

CloudWatch Contributor Insights for DynamoDB – Preview | 

CloudWatch Contributor Insights for DynamoDB is a diagnostic tool that provides an at-a-glance view of your DynamoDB table's traffic trends and helps you identify your table's most frequently accessed keys (also known as hot keys). | 

November 26, 2019 | 
| 

Adaptive capacity support for imbalanced workload | 

Amazon DynamoDB adaptive capacity now handles imbalanced workloads better by isolating frequently accessed items automatically. If your application drives disproportionately high traffic to one or more items, DynamoDB will rebalance your partitions such that frequently accessed items do not reside on the same partition. | 

November 26, 2019 | 
| 

Support for customer managed keys | 

DynamoDB now supports customer managed keys, which means you can have full control over how you encrypt and manage the security of your DynamoDB data. | 

November 25, 2019 | 
| 

NoSQL Workbench support for DynamoDB local (Downloadable Version) | 

The NoSQL Workbench now supports connecting to DynamoDB local (Downloadable Version) to design, create, query, and manage DynamoDB tables. | 

November 8, 2019 | 
| 

NoSQL Workbench - Preview | 

This is the initial release of NoSQL Workbench for DynamoDB. Use NoSQL Workbench to design, create, query, and manage DynamoDB tables. For more information, see NoSQL Workbench for Amazon DynamoDB (Preview). | 

September 16, 2019 | 
| 

DAX adds support for transactional operations using Python and .NET | 

DAX supports the `TransactWriteItems` and `TransactGetItems` APIs for applications written in Go, Java, .NET, Node.js, and Python. For more information, see In-Memory Acceleration with DAX. | 

February 14, 2019 | 
| 

Amazon DynamoDB local (Downloadable Version) Updates | 

DynamoDB local (Downloadable Version) now supports transactional APIs, on-demand read/write capacity, capacity reporting for read and write operations, and 20 global secondary indexes. For more information, see Differences Between Downloadable DynamoDB and the DynamoDB Web Service. | 

February 4, 2019 | 
| 

Amazon DynamoDB On-Demand | 

DynamoDB on-demand is a flexible billing option capable of serving thousands of requests per second without capacity planning. DynamoDB on-demand offers pay-per-request pricing for read and write requests so that you pay only for what you use. For more information, see DynamoDB throughput capacity. | 

November 28, 2018 | 
| 

Amazon DynamoDB Transactions | 

DynamoDB transactions make coordinated, all-or-nothing changes to multiple items both within and across tables, providing atomicity, consistency, isolation, and durability (ACID) in DynamoDB. For more information, see Amazon DynamoDB Transactions. | 

November 27, 2018 | 
| 

Amazon DynamoDB encrypts all customer data at rest | 

DynamoDB encryption at rest provides an additional layer of data protection by securing your data in the encrypted table, including its primary key, local and global secondary indexes, streams, global tables, backups, and DAX clusters whenever the data is stored in durable media. For more information, see Amazon DynamoDB Encryption at Rest. | 

November 15, 2018 | 
| 

Use Amazon DynamoDB Local More Easily with the New Docker Image | 

Now, it’s easier to use DynamoDB local, the downloadable version of DynamoDB, to help you develop and test your DynamoDB applications by using the new DynamoDB local Docker image. For more information, see DynamoDB (Downloadable Version) and Docker. | 

August 22, 2018 | 
| 

DynamoDB Accelerator (DAX) Adds Support for Encryption at Rest | 

DynamoDB Accelerator (DAX) now supports encryption at rest for new DAX clusters to help you accelerate reads from Amazon DynamoDB tables in security-sensitive applications that are subject to strict compliance and regulatory requirements. For more information, see DAX Encryption at Rest. | 

August 9, 2018 | 
| 

DynamoDB point-in-time recovery (PITR) adds support for restoring deleted tables | 

If you delete a table with point-in-time recovery enabled, a system backup is automatically created and is retained for 35 days (at no additional cost). For more information, see Before You Begin Using Point In Time Recovery. | 

August 7, 2018 | 
| 

Updates now available over RSS | 

You can now subscribe to the RSS feed (at the top left corner of this page) to receive notifications about updates to the Amazon DynamoDB Developer Guide. | 

July 3, 2018 |  

## Earlier updates 

The following table describes important changes of the DynamoDB Developer Guide before July 3, 2018.  
|  Change |  Description |  Date Changed |    
|  Go support for DAX |   

Now, you can enable microsecond read performance for Amazon DynamoDB tables in your applications written in the Go programming language by using the new DynamoDB Accelerator (DAX) SDK for Go. For more information, see DAX SDK for Go.  |  June 26, 2018 |   
|  DynamoDB announces SLA |   

DynamoDB has released a public availability SLA. For more information, see Amazon DynamoDB Service Level Agreement.  |  June 19, 2018 |   
|  DynamoDB continuous backups and Point-In-Time Recovery (PITR)  |   

Point-in-time recovery helps protect your Amazon DynamoDB tables from accidental write or delete operations. With point in time recovery, you don't have to worry about creating, maintaining, or scheduling on-demand backups. For example, suppose that a test script writes accidentally to a production DynamoDB table. With point-in-time recovery, you can restore that table to any point in time during the last 35 days. DynamoDB maintains incremental backups of your table. For more information, see Point-in-time backups for DynamoDB.  |  April 25, 2018 |   
|  Encryption at rest for DynamoDB |   

DynamoDB encryption at rest, available for new DynamoDB tables, helps you secure your application data in Amazon DynamoDB tables by using AWS-managed encryption keys stored in AWS Key Management Service. For more information, see DynamoDB encryption at rest.  |  February 8, 2018 |   
|  DynamoDB Backup and restore |   

On-Demand Backup allows you to create full backups of your DynamoDB tables data for data archival, helping you meet your corporate and governmental regulatory requirements. You can backup tables from a few megabytes to hundreds of terabytes of data, with no impact on performance and availability to your production applications. For more information, see Backup and restore for DynamoDB.  |  November 29, 2017 |   
|  DynamoDB Global tables |   

Global Tables builds upon DynamoDB’s global footprint to provide you with a fully managed, multi-region, and multi-active database that provides fast, local, read and write performance for massively scaled, global applications. Global Tables replicates your Amazon DynamoDB tables automatically across your choice of AWS regions. For more information, see Global tables - multi-active, multi-Region replication.  |  November 29, 2017 |   
|  Node.js support for DAX |   

Node.js developers can leverage DynamoDB Accelerator (DAX), using the DAX client for Node.js. For more information, see In-memory acceleration with DynamoDB Accelerator (DAX).  |  October 5, 2017 |   
|  VPC Endpoints for DynamoDB |   

DynamoDB endpoints allow Amazon EC2 instances in your Amazon VPC to access DynamoDB, without exposure to the public Internet. Network traffic between your VPC and DynamoDB does not leave the Amazon network. For more information, see Using Amazon VPC endpoints to access DynamoDB.  |  August 16, 2017 |   
|  Auto Scaling for DynamoDB |   

DynamoDB auto scaling eliminates the need for manually defining or adjust provisioned throughput settings. Instead, DynamoDB auto scaling dynamically adjusts read and write capacity in response to actual traffic patterns. This allows a table or a global secondary index to increase its provisioned read and write capacity to handle sudden increases in traffic, without throttling. When the workload decreases, DynamoDB auto scaling decreases the provisioned capacity. For more information, see Managing throughput capacity automatically with DynamoDB auto scaling.  |  June 14, 2017 |   
|  DynamoDB Accelerator (DAX) |   

DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance improvement – from milliseconds to microseconds – even at millions of requests per second. For more information, see In-memory acceleration with DynamoDB Accelerator (DAX).  |  April 19, 2017 |   
|  DynamoDB now supports automatic item expiration with Time to Live (TTL) |   

 Amazon DynamoDB Time to Live (TTL) enables you to automatically delete expired items from your tables, at no additional cost. For more information, see Using time to live (TTL) in DynamoDB.  |  Feb 27, 2017 |   
|  DynamoDB now supports Cost Allocation Tags |   

 You can now add tags to your Amazon DynamoDB tables for improved usage categorization and more granular cost reporting. For more information, see Adding tags and labels to resources in DynamoDB.  |  Jan 19, 2017 |   
|  New DynamoDB `DescribeLimits` API |   

The `DescribeLimits` API returns the current provisioned capacity limits for your AWS account in a region, both for the region as a whole and for any one DynamoDB table that you create there. It lets you determine what your current account-level limits are so that you can compare them to the provisioned capacity that you are currently using, and have plenty of time to apply for an increase before you hit a limit. For more information, see Quotas in Amazon DynamoDB and the DescribeLimits in the Amazon DynamoDB API Reference.  |  March 1, 2016 |   
|  DynamoDB Console Update and New Terminology for Primary Key Attributes |   

The DynamoDB management console has been redesigned to be more intuitive and easy to use. As part of this update, we are introducing new terminology for primary key attributes:  
Partition Key—also known as a hash attribute. 
Sort Key—also known as a range attribute. 
 

Only the names have changed; the functionality remains the same. 

When you create a table or a secondary index, you can choose either a simple primary key (partition key only), or a composite primary key (partition key and sort key). The DynamoDB documentation has been updated to reflect these changes. |  November 12, 2015 |   
|  Amazon DynamoDB Storage Backend for Titan |  

The DynamoDB Storage Backend for Titan is a storage backend for the Titan graph database implemented on top of Amazon DynamoDB. When using the DynamoDB Storage Backend for Titan, your data benefits from the protection of DynamoDB, which runs across Amazon’s high-availability data centers. The plugin is available for Titan version 0.4.4 (primarily for compatibility with existing applications) and Titan version 0.5.4 (recommended for new applications). Like other storage backends for Titan, this plugin supports the Tinkerpop stack (versions 2.4 and 2.5), including the Blueprints API and the Gremlin shell. |  August 20, 2015 |   
|  DynamoDB Streams, Cross-Region Replication, and Scan with Strongly Consistent Reads |  DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table, and stores this information in a log for up to 24 hours. Applications can access this log and view the data items as they appeared before and after they were modified, in near real time. For more information, see Change data capture for DynamoDB Streams and the DynamoDB Streams API Reference. 

DynamoDB cross-region replication is a client-side solution for maintaining identical copies of DynamoDB tables across different AWS regions, in near real time. You can use cross region replication to back up DynamoDB tables, or to provide low-latency access to data where users are geographically distributed. 

The DynamoDB `Scan` operation uses eventually consistent reads, by default. You can use strongly consistent reads instead by setting the `ConsistentRead` parameter to true. For more information, see Read consistency for scan and Scan in the Amazon DynamoDB API Reference. |  July 16, 2015 |   
|  AWS CloudTrail support for Amazon DynamoDB |  DynamoDB is now integrated with CloudTrail. CloudTrail captures API calls made from the DynamoDB console or from the DynamoDB API and tracks them in log files. For more information, see Logging DynamoDB operations by using AWS CloudTrail and the AWS CloudTrail User Guide. |  May 28, 2015 |   
|  Improved support for Query expressions |  This release adds a new `KeyConditionExpression` parameter to the `Query` API. A `Query` reads items from a table or an index using primary key values. The `KeyConditionExpression` parameter is a string that identifies primary key names, and conditions to be applied to the key values; the `Query` retrieves only those items that satisfy the expression. The syntax of `KeyConditionExpression` is similar to that of other expression parameters in DynamoDB, and allows you to define substitution variables for names and values within the expression. For more information, see Querying tables in DynamoDB. |  April 27, 2015 |   
|  New comparison functions for conditional writes |  In DynamoDB, the `ConditionExpression` parameter determines whether a `PutItem`, `UpdateItem`, or `DeleteItem` succeeds: The item is written only if the condition evaluates to true. This release adds two new functions, `attribute_type` and `size`, for use with`ConditionExpression`. These functions allow you to perform a conditional writes based on the data type or size of an attribute in a table. For more information, see DynamoDB condition expression CLI example. |  April 27, 2015 |   
|  Scan API for secondary indexes |  In DynamoDB, a `Scan` operation reads all of the items in a table, applies user-defined filtering criteria, and returns the selected data items to the application. This same capability is now available for secondary indexes too. To scan a local secondary index or a global secondary index, you specify the index name and the name of its parent table. By default, an index `Scan` returns all of the data in the index; you can use a filter expression to narrow the results that are returned to the application. For more information, see Scanning tables in DynamoDB. |  February 10, 2015 |   
|  Online operations for global secondary indexes |  Online indexing lets you add or remove global secondary indexes on existing tables. With online indexing, you do not need to define all of a table's indexes when you create a table; instead, you can add a new index at any time. Similarly, if you decide you no longer need an index, you can remove it at any time. Online indexing operations are non-blocking, so that the table remains available for read and write activity while indexes are being added or removed. For more information, see Managing Global Secondary Indexes in DynamoDB. |  January 27, 2015 |   
|  Document model support with JSON |  DynamoDB allows you to store and retrieve documents with full support for document models. New data types are fully compatible with the JSON standard and allow you to nest document elements within one another. You can use document path dereference operators to read and write individual elements, without having to retrieve the entire document. This release also introduces new expression parameters for specifying projections, conditions and update actions when reading or writing data items. To learn more about document model support with JSON, see Data types and Using expressions in DynamoDB. |  October 7, 2014 |   
|  Flexible scaling |  For tables and global secondary indexes, you can increase provisioned read and write throughput capacity by any amount, provided that you stay within your per-table and per-account limits. For more information, see Quotas in Amazon DynamoDB. |  October 7, 2014 |   
|  Larger item sizes |  The maximum item size in DynamoDB has increased from 64 KB to 400 KB. For more information, see Quotas in Amazon DynamoDB.  |  October 7, 2014 |   
|  Improved conditional expressions |  DynamoDB expands the operators that are available for conditional expressions, giving you additional flexibility for conditional puts, updates, and deletes. The newly available operators let you check whether an attribute does or does not exist, is greater than or less than a particular value, is between two values, begins with certain characters, and much more. DynamoDB also provides an optional OR operator for evaluating multiple conditions. By default, multiple conditions in an expression are ANDed together, so the expression is true only if all of its conditions are true. If you specify OR instead, the expression is true if one or more one conditions are true. For more information, see Working with items and attributes in DynamoDB. |  April 24, 2014 |   
|  Query filter |  The DynamoDB `Query` API supports a new `QueryFilter` option. By default, a `Query` finds items that match a specific partition key value and an optional sort key condition. A `Query` filter applies conditional expressions to other, non-key attributes; if a `Query` filter is present, then items that do not match the filter conditions are discarded before the `Query` results are returned to the application. For more information, see Querying tables in DynamoDB. |  April 24, 2014 |   
|  Data export and import using the AWS Management Console |  The DynamoDB console has been enhanced to simplify exports and imports of data in DynamoDB tables. With just a few clicks, you can set up an AWS Data Pipeline to orchestrate the workflow, and an Amazon Elastic MapReduce cluster to copy data from DynamoDB tables to an Amazon S3 bucket, or vice-versa. You can perform an export or import one time only, or set up a daily export job. You can even perform cross-region exports and imports, copying DynamoDB data from a table in one AWS region to a table in another AWS region.  |  March 6, 2014 |   
|  Reorganized higher-level API documentation |  Information about the following APIs is now easier to find:  
Java: DynamoDBMappper 
.NET: Document model and object-persistence model 
These higher-level APIs are now documented here: Higher-level programming interfaces for DynamoDB. |  January 20, 2014 |   
|  Global secondary indexes |  DynamoDB adds support for global secondary indexes. As with a local secondary index, you define a global secondary index by using an alternate key from a table and then issuing Query requests on the index. Unlike a local secondary index, the partition key for the global secondary index does not have to be the same as that of the table; it can be any scalar attribute from the table. The sort key is optional and can also be any scalar table attribute. A global secondary index also has its own provisioned throughput settings, which are separate from those of the parent table. For more information, see Improving data access with secondary indexes in DynamoDB and Using Global Secondary Indexes in DynamoDB. |  December 12, 2013 |   
|  Fine-grained access control |  DynamoDB adds support for fine-grained access control. This feature allows customers to specify which principals (users, groups, or roles) can access individual items and attributes in a DynamoDB table or secondary index. Applications can also leverage web identity federation to offload the task of user authentication to a third-party identity provider, such as Facebook, Google, or Login with Amazon. In this way, applications (including mobile apps) can handle very large numbers of users, while ensuring that no one can access DynamoDB data items unless they are authorized to do so. For more information, see Using IAM policy conditions for fine-grained access control. |  October 29, 2013 |   
|  4 KB read capacity unit size |  The capacity unit size for reads has increased from 1 KB to 4 KB. This enhancement can reduce the number of provisioned read capacity units required for many applications. For example, prior to this release, reading a 10 KB item would consume 10 read capacity units; now that same 10 KB read would consume only 3 units (10 KB / 4 KB, rounded up to the next 4 KB boundary). For more information, see DynamoDB throughput capacity. |  May 14, 2013 |   
|  Parallel scans |  DynamoDB adds support for parallel Scan operations. Applications can now divide a table into logical segments and scan all of the segments simultaneously. This feature reduces the time required for a Scan to complete, and fully utilizes a table's provisioned read capacity. For more information, see Scanning tables in DynamoDB. |  May 14, 2013 |   
|  Local secondary indexes |  DynamoDB adds support for local secondary indexes. You can define sort key indexes on non-key attributes, and then use these indexes in Query requests. With local secondary indexes, applications can efficiently retrieve data items across multiple dimensions. For more information, see Local secondary indexes. |  April 18, 2013 |   
|  New API version |  With this release, DynamoDB introduces a new API version (2012-08-10). The previous API version (2011-12-05) is still supported for backward compatibility with existing applications. New applications should use the new API version 2012-08-10. We recommend that you migrate your existing applications to API version 2012-08-10, since new DynamoDB features (such as local secondary indexes) will not be backported to the previous API version. For more information on API version 2012-08-10, see the Amazon DynamoDB API Reference. |  April 18, 2013 |   
|  IAM policy variable support |   

The IAM access policy language now supports variables. When a policy is evaluated, any policy variables are replaced with values that are supplied by context-based information from the authenticated user's session. You can use policy variables to define general purpose policies without explicitly listing all the components of the policy. For more information about policy variables, go to Policy Variables in the AWS Identity and Access Management Using IAM guide.  

For examples of policy variables in DynamoDB, see Identity and Access Management for Amazon DynamoDB.   |  April 4, 2013  |   
|  PHP code examples updated for AWS SDK for PHP version 2 |  Version 2 of the AWS SDK for PHP is now available. The PHP code examples in the Amazon DynamoDB Developer Guide have been updated to use this new SDK. For more information on Version 2 of the SDK, see AWS SDK for PHP. |  January 23, 2013 |   
|  New endpoint |  DynamoDB expands to the AWS GovCloud (US-West) region. For the current list of service endpoints and protocols, see Regions and Endpoints. |  December 3, 2012 |   
|  New endpoint |  DynamoDB expands to the South America (São Paulo) region. For the current list of supported endpoints, see Regions and Endpoints. |  December 3, 2012 |   
|  New endpoint |  DynamoDB expands to the Asia Pacific (Sydney) region. For the current list of supported endpoints, see Regions and Endpoints. |  November 13, 2012 |   
|   

DynamoDB implements support for CRC32 checksums, supports strongly consistent batch gets, and removes restrictions on concurrent table updates.  |    
DynamoDB calculates a CRC32 checksum of the HTTP payload and returns this checksum in a new header, `x-amz-crc32`. For more information, see DynamoDB low-level API. 
By default, read operations performed by the `BatchGetItem` API are eventually consistent. A new `ConsistentRead` parameter in `BatchGetItem` lets you choose strong read consistency instead, for any table(s) in the request. For more information, see Description. 
This release removes some restrictions when updating many tables simultaneously. The total number of tables that can be updated at once is still 10; however, these tables can now be any combination of `CREATING`, `UPDATING` or `DELETING` status. Additionally, there is no longer any minimum amount for increasing or reducing the ReadCapacityUnits or WriteCapacityUnits for a table. For more information, see Quotas in Amazon DynamoDB. 
  |   

November 2, 2012  |   
|   

Best practices documentation  |   

The Amazon DynamoDB Developer Guide identifies best practices for working with tables and items, along with recommendations for query and scan operations.  |   

September 28, 2012  |   
|   

Support for binary data type  |   

In addition to the Number and String types, DynamoDB now supports Binary data type.  

Prior to this release, to store binary data, you converted your binary data into string format and stored it in DynamoDB. In addition to the required conversion work on the client-side, the conversion often increased the size of the data item requiring more storage and potentially additional provisioned throughput capacity.  

With the binary type attributes you can now store any binary data, for example compressed data, encrypted data, and images. For more information see Data types. For working examples of handling binary type data using the AWS SDKs, see the following sections:  
Example: Handling binary type attributes using the AWS SDK for Java document API 
Example: Handling binary type attributes using the AWS SDK for .NET low-level API 
 

For the added binary data type support in the AWS SDKs, you will need to download the latest SDKs and you might also need to update any existing applications. For information about downloading the AWS SDKs, see .NET code examples.  |   

August 21, 2012  |   
|   

DynamoDB table items can be updated and copied using the DynamoDB console  |   

DynamoDB users can now update and copy table items using the DynamoDB Console, in addition to being able to add and delete items. This new functionality simplifies making changes to individual items through the Console.  |   

August 14, 2012  |   
|   

DynamoDB lowers minimum table throughput requirements  |   

DynamoDB now supports lower minimum table throughput requirements, specifically 1 write capacity unit and 1 read capacity unit. For more information, see the Quotas in Amazon DynamoDB topic in the Amazon DynamoDB Developer Guide.  |   

August 9, 2012  |   
|   

Signature Version 4 support  |   

 DynamoDB now supports Signature Version 4 for authenticating requests.  |   

July 5, 2012  |   
|  

Table explorer support in DynamoDB Console |  

The DynamoDB Console now supports a table explorer that enables you to browse and query the data in your tables. You can also insert new items or delete existing items. The `SampleData` and Using the console sections have been updated for these features. |  

May 22, 2012 |   
|  

New endpoints |  

DynamoDB availability expands with new endpoints in the US West (N. California) region, US West (Oregon) region, and the Asia Pacific (Singapore) region. 

For the current list of supported endpoints, go to Regions and Endpoints. |  

April 24, 2012 |   
|  

BatchWriteItem API support |  

DynamoDB now supports a batch write API that enables you to put and delete several items from one or more tables in a single API call. For more information about the DynamoDB batch write API, see BatchWriteItem. 

For information about working with items and using batch write feature using AWS SDKs, see Working with items and attributes in DynamoDB and .NET code examples. |  

April 19, 2012 |   
|  

Documented more error codes |  

For more information, see Error handling with DynamoDB. |  

April 5, 2012 |   
|  

New endpoint |  

DynamoDB expands to the Asia Pacific (Tokyo) region. For the current list of supported endpoints, see Regions and Endpoints. |  

February 29, 2012 |   
|  

`ReturnedItemCount` metric added |  

A new metric, `ReturnedItemCount`, provides the number of items returned in the response of a Query or Scan operation for DynamoDB is available for monitoring through CloudWatch. |  

February 24, 2012 |   
|  

Added examples for incrementing values |  

DynamoDB supports incrementing and decrementing existing numeric values. Examples show adding to existing values in the "Updating an Item" sections at: 

Working with items: Java. 

Working with items: .NET.  |  

January 25, 2012 |   
|  

Initial product release |  

DynamoDB is introduced as a new service in Beta release. |  

January 18, 2012 |
