> Source: https://docs.aws.amazon.com/step-functions/latest/dg/document-history.html
> Downloaded: 2026-10-26

# Document history

This section lists major changes to the AWS Step Functions Developer Guide. 
|  Change |  Description |  Date changed |    
|  New feature |   

Step Functions now supports additional data sources and observability metrics for Distributed Map. 

Step Functions supports additional data sources and new observability metrics for Distributed Map. With this update, Distributed Map now supports additional data inputs, so you can orchestrate large-scale analytics and ETL workflows. You can now process Athena data manifest and Parquet files directly, iterate over Amazon S3 objects under a specified prefix using `S3ListObjectsV2`, read from JSON objects and natively extract array data from JSON object from Amazon S3 or state input, eliminating the need for custom pre-processing. You also now get visibility into your Distributed Map usage with new metrics, including: Approximate Open Map Runs Count, Open Map Run Limit, and Approximate Map Runs Backlog Size. To learn more, see ItemReader (Map) and Monitoring Step Functions metrics using Amazon CloudWatch.  |  Sep 18, 2025 |   
|  Documentation-only update |   

Simplified and re-organized the integrating services topics based on customer feedback. To see the updates, check out the Integrating services with Step Functions chapter.  |  Sep 4, 2025 |   
|  Updates |   

Step Functions will now auto-create roles and policy for optimized integrations with MediaConvert. 

For integrations with MediaConvert, Step Functions will now automatically create the necessary roles and policies required by your state machine. To learn more, see Create an AWS Elemental MediaConvert job with Step Functions and Integrating optimized services with Step Functions.  |  March 14, 2025 |   
|  New feature |   

Step Functions expands data source and output options for Distributed Map. 

Distributed map can process data from JSON Lines (JSONL) and a broader range of delimited file formats, such as semicolon-delimited files and tab-delimited files. Additionally, Distributed Map offers output transformations for greater control over result formatting. To learn more, ItemReader (Map) and ResultWriter (Map).  |  February 7, 2025 |   
|  Documentation-only update |  

Replaced the Getting started tutorial with content from workshop presented at re:Invent 2024.  |  Dec 23, 2024 |   
|  New feature |  

Manage state and transform data with Step Functions workflow variables and JSONata. 

With variables, you can pass data between the steps of your workflows. With JSONata, you gain an open source query and expression language to select and transform data in your workflows. To learn more, see Passing data between states with variables and Transforming data with JSONata in Step Functions.  |  November 22, 2024 |   
|  New feature |  

Step Functions adds Infrastructure as Code (IaC) template generation 

The AWS Step Functions console provides the ability to export and download saved workflows as AWS CloudFormation or AWS SAM (SAM) templates. For AWS Regions that support AWS Infrastructure Composer, it additionally provides the ability to export your workflows to Infrastructure Composer and navigates to the Infrastructure Composer console, where you can continue to work with the newly generated template. To learn more, see Exporting your workflow to IaC templates.  |  November 14, 2024 |   
|  New feature |  

Step Functions adds the option to use AWS KMS and customer managed keys to encrypt your data 

You can add another layer of security by choosing a customer managed key to encrypt workflows, activities, and logs. To learn more, see Data at rest encryption in Step Functions.  |  July 25, 2024 |   
|  Updates |  

Document structure update 

With page view data and depth analysis, documentation sections were restructured to increase visibility of important topics. The navigation was updated to reduce overall depth. Related topics were consolidated. Redirects were added so that bookmarks should lead to the updated locations. Send feedback if you notice errors or omissions after this massive update. Thank you!  |  July 24, 2024 |   
|  Updates |  

 AWS managed policy updates - new permission: `states:ValidateStateMachineDefinition`  

Added information about new permission to check the syntax of a state machine that you provide. To learn more, see AWS managed policies for AWS Step Functions.  |  April 29, 2024 |   
|  New feature |  

Step Functions adds optimized integration for AWS Elemental MediaConvert 

AWS Elemental MediaConvert provides broadcast-grade video and audio file transcoding, which customers can automate with code to suit their media workflows. With the optimized integration for AWS Step Functions in MediaConvert, it is now possible to orchestrate using the low-code visual tool Workflow Studio. To learn more, see the documentation to Manage AWS Elemental MediaConvert with Step Functions.  |  April 12, 2024 |   
|  Updates |  

 AWS managed policy updates - Update to an existing policy: `AWSStepFunctionsReadOnlyAccess`  

Added information about new read-only permissions for tags, distributed maps, and versions and aliases. To learn more, see AWS managed policies for AWS Step Functions.   |  April 02, 2024 |   
|  Updates |  

 Step Functions adds support for Open Workflow metrics  

With open workflow metrics, you now have account-level visibility into the number of standard workflows in progress as well as your open workflow limit. You can manage workloads across all workflows, regardless of how they're started, to ensure smooth workflow operations. You can set CloudWatch alarms to monitor your workflows and proactively receive alerts as you approach your limits. Once alerted, you can effectively manage your workflows by taking actions such as stopping specific workflows or requesting a limit increase.  

Open workflow metrics is available to use in CloudWatch for standard workflows with no additional configuration required. To learn more, see Execution Metrics.   |  February 29, 2024 |   
|  Updates |  

Service integration additions and updates. For the list of new and updated AWS SDK integrations, see Learning to use AWS service SDK integrations in Step Functions. For the full list of services, see Supported AWS SDK service integrations.  |  January 18, 2024 |   
|  New feature |  

Use Workflow Studio in Infrastructure Composer to build serverless workflows using AWS CloudFormation templates. For more information, see Using Workflow Studio in Infrastructure Composer to build Step Functions workflows. |  November 27, 2023 |   
|  New feature |  

Step Functions now lets you directly invoke public HTTPS endpoints and test individual states using a new Test State API. For more information, see:  
Call HTTPS APIs in Step Functions workflows 
Testing state machines with TestState API 
  |  November 26, 2023 |   
|  New feature |  Step Functions now integrates with Amazon Bedrock. For more information, see the following topics:  
Invoke and customize Amazon Bedrock models with Step Functions 
IAM permissions for Amazon Bedrock 
Perform AI prompt-chaining with Amazon Bedrock 
Integrating services with Step Functions 
  |  November 26, 2023 |   
|  New feature |  Step Functions now lets you redrive workflow executions of type Standard from their point of failure. For more information, see Restarting state machine executions with redrive in Step Functions and Redriving Map Runs in Step Functions executions. |  November 15, 2023 |   
|  Documentation-only update |   

Published a new topic that explains how to run state machines on a schedule using Amazon EventBridge Scheduler. For more information, see Using Amazon EventBridge Scheduler to start a Step Functions state machine execution. |  October 16, 2023 |   
|  New feature |  Step Functions now integrates with Amazon EMR Serverless. For more information, see the following topics:  
Create and manage Amazon EMR Serverless applications with Step Functions 
Run an EMR Serverless job 
Integrating services with Step Functions 
Integrating services with Step Functions 
  |  October 12, 2023 |   
|  Documentation-only update |  Added information about running state machines on a schedule using Amazon EventBridge Scheduler. For more information, see Using EventBridge Scheduler. |  October 05, 2023 |   
|  Update |   

Reorganized and updated the Distributed Map state topics for clarity, brevity, and establishing a clear journey map for new users. For more information, see Using Map state in Distributed mode for large-scale parallel workloads in Step Functions.  |  October 6, 2023 |   
|  Fixes |  Fixed code samples in a tutorial to use AWS CDK v2. For more information, see Using AWS CDK to create a Standard workflow in Step Functions. |  September 19, 2023 |   
|  Update |  Added information about the enhanced error handling capabilities that Step Functions has introduced to identify errors clearly and implement retries with greater control. For more information, see Fail workflow state and Retrying after an error. |  September 07, 2023 |   
|  Update |  Step Functions has added enhancements to Workflow Studio for streamlining workflow authoring experience. For more information, see Developing workflows in Step Functions Workflow Studio. |  August 31, 2023 |   
|  Documentation-only update |  Added information about twice the actual metric count reported for the `ExecutionsStarted` metric. For more information, see Metrics that report a count. |  July 25, 2023 |   
|  Documentation-only update |  Step Functions has added two new sample projects that demonstrate the following common use cases for the Distributed Map state:  
Processing a CSV file 
Processing data in an Amazon S3 bucket 
  |  July 17, 2023 |   
|  Documentation-only update |   

Published a new topic about deploying state machines using Terraform. For more information, see Using Terraform to deploy state machines in Step Functions.  |  July 5, 2023 |   
|  Documentation-only update |   

Updated the following procedures to match changes to the Amazon EventBridge interface.  
Automate event delivery 
Starting a Step Functions workflow in response to events 
  |  June 26, 2023 |   
|  New feature |  Step Functions now provides the ability to create multiple state machine versions and aliases for improved resiliency while deploying serverless workflows. For more information, see Manage continuous deployments with versions and aliases in Step Functions. |  June 22, 2023 |   
|  Documentation-only update |   

Improved the description of `TimeoutSeconds` and `HeartbeatSeconds` fields to describe how they're different from each other. For more information, see Task state fields.  |  June 22, 2023 |   
|  Documentation-only update |   

Published a new section that describes how to flatten an array of arrays typically returned as result for Parallel and Map states. For more information, see Flattening an array of arrays.  |  June 20, 2023 |   
|   

Update  |   

Step Functions has expanded support for AWS SDK integrations by adding seven AWS services and 468 new API actions. For more information, see Supported AWS SDK service integrations and Learning to use AWS service SDK integrations in Step Functions. |  June 16, 2023 |   
|  Documentation-only update |  Published a new topic that lists the AWS Regions in which recently launched Step Functions features are available. For more information, see Recent feature launches. |  June 16, 2023 |   
|   

Documentation-only update  |  Step Functions now includes a section about AWS User Notifications, an AWS service that acts as a central location for your AWS notifications in the AWS Management Console. For more information, see Events using User Notifications. |  May 4, 2023 |   
|  Documentation-only update |   

Added a new section that explains about the permissions needed to write child workflow execution results to an Amazon S3 bucket encrypted with an AWS Key Management Service (AWS KMS) key. For more information, see IAM permissions for AWS KMS key encrypted Amazon S3 bucket.  |  April 29, 2023 |   
|  Documentation-only update |   

Added a new topic that explains about the  Data flow simulator feature. For more information, see Data flow simulator (unsupported).  |  April 14, 2023 |   
|  Quota update |   

Added information about default quota of 1000 for open Map Runs in each account. For more information, see Quotas related to accounts. |  April 05, 2023 |   
|  Documentation-only update |   

Added a Note about unavailability of X-Ray tracing for the Distributed Map state. For more information, see Trace Step Functions request data in AWS X-Ray.  |  March 21, 2023 |   
|  Documentation-only update |   

Added information about how Step Functions handles tag-based authorization. For more information, see Tagging state machines and activities in Step Functions and Creating tag-based IAM policies in Step Functions.  |  March 15, 2023 |   
|  Documentation-only update |   

Added information about how Step Functions parses CSV files used as input in Distributed Map state. For more information, see CSV file in an Amazon S3 bucket.  |  March 14, 2023 |   
|  Documentation-only update |   

Added information about how Step Functions handles cross-account invocations for the Run a Job (.sync) pattern. For more information, see Run a Job (.sync).  |  March 01, 2023 |   
|  Documentation-only update |   

Reduce the history retention period of your completed workflow executions from 90 days to 30 days. For more information about adjusting the retention period, see Execution guarantees in Step Functions workflows and Quotas related to state machine executions.  |  February 21, 2023 |   
|  Update |   

Step Functions has expanded support for AWS SDK integrations by adding 35 AWS services and 1100 new API actions. For more information, see Supported AWS SDK service integrations and Learning to use AWS service SDK integrations in Step Functions.  |  February 17, 2023 |   
|  Documentation-only update |   

Published a Getting Started tutorial series that walks you through the process of creating a workflow for credit card application using Step Functions. For more information, see Learn how to get started with Step Functions.  |  December 30, 2022 |   
|  New feature |  

Step Functions adds support to orchestrate large-scale parallel workflows for data processing using a new Distributed mode for `Map` state. For more information, see Using Map state in Distributed mode for large-scale parallel workloads in Step Functions.  |  December 01, 2022 |   
|  New feature |  Step Functions now supports access to cross-account AWS resources configured in other accounts. For more information, see  
Accessing resources in other AWS accounts in Step Functions 
Accessing cross-account AWS resources in Step Functions 
Task state 
 |  November 18, 2022 |   
|  Update |   

Step Functions now provides a new console experience for viewing and debugging Express workflow executions. For more information see:  
Standard and Express console experience differences 
Viewing execution details in the Step Functions console 
  |  October 18, 2022 |   
|  Update |   

Added support to optionally specify the `ExecutionRoleArn` parameter while using the `addStep` and `addStep.sync` APIs for the Amazon EMR optimized service integration. For more information, see Create and manage Amazon EMR clusters with Step Functions.  |  September 20, 2022 |   
|  Documentation-only update |   

Added a new topic that provides recommendations about optimizing cost while building serverless workflows using Step Functions. For more information, see Optimizing costs using Express Workflows.  |  September 15, 2022 |   
|   

Update  |   

Step Functions adds support for 14 new intrinsic functions for performing data processing tasks, such as array manipulations, data encoding and decoding, hash calculations, JSON data manipulation, math function operations, and unique identifier generation. Documentation-only update: 

Grouped all the existing and newly introduced intrinsic functions into the following categories based on the type of data processing task they help you perform:  
Intrinsics for arrays 
Intrinsics for data encoding and decoding 
Intrinsic for hash calculation 
Intrinsics for JSON data manipulation 
Intrinsics for Math operations 
Intrinsic for String operation 
Intrinsic for unique identifier generation 
Intrinsic for generic operation 
 

For more information, see Intrinsic functions for JSONPath states in Step Functions.  |   

August 31, 2022  |   
|  Update |   

Step Functions has expanded support for AWS SDK integrations by adding three more AWS services – AWS Billing Conductor, Amazon GameSparks, and Amazon Pinpoint SMS and Voice V2. For more information, see Learning to use AWS service SDK integrations in Step Functions. |  July 26, 2022 |   
|  Documentation-only update |   

Added a new topic to include a summary of all the updates made to AWS SDK integrations supported by Step Functions. For more information, see Learning to use AWS service SDK integrations in Step Functions |  July 26, 2022 |   
|  Documentation-only update |   

AWS Step Functions Developer Guide now includes details about the execution metrics that are emitted specifically for Express Workflows. For more information, see Execution metrics for Express Workflows. |  June 09, 2022 |   
|  Update |   Step Functions console enhancements 

The console now features a redesigned Execution Details page that includes the following enhancements:  
Ability to identify the reason for a failed execution at a glance. 
Two new modes of visualizations for your state machine – Table view and Event view. These views also provide you the ability to apply filters to only view the information of interest. In addition, you can sort the Event view contents based on the event timestamps. 
Switch between the different iterations of `Map` state in the Graph view mode using a dropdown list or in the Table view mode's tree view for `Map` states. 
View in-depth information about each state in the workflow, including the complete input and output data transfer path and retry attempts for `Task` or `Parallel` states. 
Miscellaneous enhancements including the option to copy the state machine's execution Amazon Resource Name, view the count of total state machine transitions, and export the execution details in JSON format. 
 Documentation-only updates 

Added a new topic to explain the various types of information displayed in the Execution Details page. Also, added a tutorial to show how to examine this information. For more information, see:  
Viewing execution details in the Step Functions console 
Examining state machine executions in Step Functions 
  |  May 09, 2022 |   
|   

Update  |   

Step Functions now provides a workaround to prevent the confused deputy security issue, which arises when an entity (a service or an account) is coerced by a different entity to perform an action. For more information, see:  
Prevent cross-service confused deputy issue 
  |   

May 02, 2022  |   
|   

Update  |    
Step Functions has expanded support for AWS SDK integrations by adding 21 more AWS services. For more information, see: Supported AWS SDK service integrations. 
Documentation-only updates:  
Added a list of all the exception prefixes present in the exceptions that are generated when you erroneously perform an AWS SDK service integration with Step Functions. For more information, see: Supported AWS SDK service integrations. 
 
  |   

April 19, 2022  |   
|   

New feature  |   

Step Functions Local now supports AWS SDK integration and mocking of service integrations. For more information, see:  
Using mocked service integrations for testing in Step Functions Local 
  |   

January 28, 2022  |   
|   

New feature  |   

AWS Step Functions now supports creating an Amazon API Gateway REST API with synchronous express state machine as backend integration using the AWS Cloud Development Kit (AWS CDK). For more information, see:  
Using AWS CDK to create an Express workflow in Step Functions 
  |   

December 10, 2021  |   
|   

Update  |   

Step Functions has added three new sample projects that demonstrate the integration of Step Functions and Amazon Athena's upgraded console. For more information, see:  
Execute queries in sequence and parallel using Athena 
Query large datasets using an AWS Glue crawler 
Keep data in a target table updated with AWS Glue and Athena 
  |   

November 22, 2021  |   
|   

New feature  |   

Step Functions has added Amazon VPC endpoints support for Synchronous Express Workflows. For more information, see:  
Creating Amazon VPC endpoints for Step Functions 
  |   

November 15, 2021  |   
|   

Update  |   

AWS Step Functions has added three new sample projects that demonstrate how to use the Step Functions AWS Batch integration. For more information, see:  
Fan out batch jobs with Map state 
Run an AWS Batch job with Lambda 
Manage a batch job with AWS Batch and Amazon SNS 
  |   

October 14, 2021  |   
|   

New feature  |   

AWS Step Functions has added AWS SDK integrations, letting you use the API actions for all of the more than two hundred AWS services. For more information, see:  
Learning to use AWS service SDK integrations in Step Functions 
 Gather Amazon S3 bucket info using AWS SDK service integrations  
  |   

September 30, 2021  |   
|   

New feature  |   

AWS Step Functions has added a visual workflow designer, the AWS Step Functions Workflow Studio. For more information, see:  
Developing workflows in Step Functions Workflow Studio 
  |   

June 17, 2021  |   
|   

Update  |   

AWS Step Functions has added four new APIs, `StartBuildBatch`, `StopBuildBatch`, `RetryBuildBatch` and `DeleteBuildBatch`, to the CodeBuild integration. For more information, see:  
Manage AWS CodeBuild builds with Step Functions 
  |   

June 4, 2021  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon EventBridge. For more information, see:  
Add EventBridge events with Step Functions 
IAM policies for Step Functions and IAM policies for calling EventBridge 
A sample project that shows how to Send a custom event to an EventBridge event bus 
  |   

May 14, 2021  |   
|   

Update  |   

AWS Step Functions has added a new sample project that shows how to use Step Functions and the Amazon Redshift Data API to run an ETL/ELT workflow. For more information, see:  
Run an ETL/ELT workflow using Step Functions and the Amazon Redshift API 
  |   

April 16, 2021  |   
|   

New feature  |   

AWS Step Functions has a new data flow simulator in the console. For more information, see:  
Data flow simulator (unsupported) 
  |   

April 8, 2021  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon EMR on EKS. For more information, see:  
Create and manage Amazon EMR clusters on EKS with AWS Step Functions 
  |   

March 29, 2021  |   
|   

Update  |   

YAML support for state machine definitions has been added to AWS Toolkit for Visual Studio Code and CloudFormation. For more information, see:  
AWS Toolkit for Visual Studio Code 
  |   

March 4, 2021  |   
|   

New feature  |   

AWS Step Functions now integrates with AWS Glue DataBrew. For more information, see:  
Start AWS Glue DataBrew jobs with Step Functions 
What is AWS Glue DataBrew? in the DataBrew developer guide. 
  |   

January 6, 2021  |   
|   

New feature  |   

AWS Step Functions Synchronous Express Workflows are now available, giving you an easy way to orchestrate microservices. For more information, see:  
Synchronous and Asynchronous Express Workflows in Step Functions 
A sample project that shows how to Invoke Synchronous Express Workflows through API Gateway 
The StartSyncExecution API documentation. 
  |   

November 24, 2020  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon API Gateway. For more information, see:  
Create API Gateway REST APIs with Step Functions 
IAM policies for Step Functions and IAM policies for calls to Amazon API Gateway 
A sample project that shows how to Interact with an API managed by API Gateway 
  |   

November 17, 2020  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon Elastic Kubernetes Service. For more information, see:  
Create and manage Amazon EKS clusters with Step Functions 
IAM policies for Step Functions and IAM policies for calling Amazon EKS 
A sample project that shows how to Create and manage an Amazon EKS cluster with a node group 
  |   

November 16, 2020  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon Athena. For more information, see:  
Run Athena queries with Step Functions 
IAM policies for Step Functions and IAM policies for calling Amazon Athena 
A sample project that shows how to Start an Athena query and send a results notification 
  |   

October 22, 2020  |   
|   

New feature  |   

AWS Step Functions now supports tracing end-to-end workflows with AWS X-Ray, giving you full visibility across state machine executions and making it easier to analyze and debug your distributed applications. For more information, see:  
Trace Step Functions request data in AWS X-Ray 
IAM policies for Step Functions and IAM policies using AWS X-Ray in Step Functions 
AWS Step Functions API Reference 
TracingConfiguration 
 
  |   

September 14, 2020  |   
|  Update |  

AWS Step Functions now supports payload sizes up to 256 KiB of data as a UTF-8 encoded string. This lets you process larger payloads in both Standard and Express workflows. 

Your existing state machines do not need to be changed in order to use the larger payloads. However, you will need to update to the latest versions of the Step Functions SDK and Local Runner to use the updated APIs. For more information, see: 
Step Functions service quotas 
Using Amazon S3 ARNs instead of passing large payloads in Step Functions 
States.DataLimitExceeded 
 CloudWatch Logs payloads  
AWS Step Functions API Reference 
CloudWatchEventsExecutionDataDetails 
HistoryEventExecutionDataDetails 
GetExecutionHistory 
ActivityScheduledEventDetails 
ActivitySucceededEventDetails 
CloudWatchEventsExecutionDataDetails 
ExecutionSucceededEventDetails 
LambdaFunctionScheduledEventDetails 
ExecutionSucceededEventDetails 
StateEnteredEventDetails 
StateExitedEventDetails 
TaskSubmittedEventDetails 
TaskSucceededEventDetails 
 
 |  September 3, 2020 |   
|   

Update  |   

The Amazon States Language has been updated as follows:  
Choice Rules (JSONata) has added  
A null comparison operator, `IsNull`. `IsNull` tests against the JSON null value, and can be used to detect if the output of a previous state is null or not. 
Four other new operators have been added, IsBoolean, IsNumeric, IsString and IsTimestamp.  
A test for the existence or non-existence of a field using the `IsPresent` operator. `IsPresent` can be used to prevent `States.Runtime` errors when there is an attempt to access a non-existent key.  
Wildcard pattern matching to support string comparison against patterns with one or more wildcards. 
Comparison between two variables for supported comparison operators. 
Timeout and heartbeat values in a `Task` state can now be provided dynamically from the state input instead of a fixed value using the `TimeoutSecondsPath` and `HeartbeatSecondsPath` fields. See the Task workflow state state for more information. 
The new ResultSelector field provides a way to manipulate a state’s result before `ResultPath` is applied. The `ResultSelector` field is an optional field in the Map workflow state, Parallel workflow state, and Task workflow state states. 
Intrinsic functions for JSONPath states in Step Functions have been added to allow basic operations without `Task` states. Intrinsic functions can be used within the `Parameters` and `ResultSelector` fields.  
  |   

August 13, 2020  |   
|  Update |  

AWS Step Functions now supports the Amazon SageMaker AI `CreateProcessingJob` API call. For more information, see:  
Create and manage Amazon SageMaker AI jobs with Step Functions 
Preprocess data and train a machine learning model with Amazon SageMaker AI, a sample project that demonstrates `CreateProcessingJob`. 
  |  August 4, 2020 |   
|   

New feature  |   

AWS Step Functions is now supported by AWS Serverless Application Model, making it easier to integrate workflow orchestration into your serverless applications. For more information, see:  
Using AWS SAM to build Step Functions workflows 
AWS::Serverless::StateMachine 
AWS SAM Policy Templates 
  |   

May 27, 2020  |   
|  New feature |  AWS Step Functions has introduced a new synchronous invocation for nesting Step Functions executions. The new invocation, `arn:aws:states:::states:startExecution.sync:2`, returns a JSON object. The original invocation, `arn:aws:states:::states:startExecution.sync`, continues to be supported, and returns a JSON-escaped string. For more information, see:  
Start a new AWS Step Functions state machine from a running execution 
  |  May 19, 2020 |   
|   

New feature  |   

AWS Step Functions now integrates with AWS CodeBuild. For more information, see:  
Integrating services with Step Functions 
Manage AWS CodeBuild builds with Step Functions 
Integrating services with Step Functions 
  |   

May 5, 2020  |   
|  New feature |  

Step Functions is now supported in AWS Toolkit for Visual Studio Code, making it easier to create and visualize state machine based workflows without leaving your code editor. |  March 31, 2020 |   
|   

Update  |   

You can now configure logging to Amazon CloudWatch Logs for Standard workflows. For more information, see:  
Using CloudWatch Logs to log execution history in Step Functions 
  |   

February 25, 2020  |   
|   

New feature  |   

AWS Step Functions can now be accessed without requiring a public IP address, directly from Amazon Virtual Private Cloud (VPC). For more information, see:  
Creating Amazon VPC endpoints for Step Functions 
  |   

December 23, 2019  |   
|   

New feature  |   

Express Workflows are a new workflow type, suitable for high-volume event processing workloads such as IoT data ingestion, streaming data processing and transformation, and mobile application backends. 

For more information, review the following new and updated topics.  
Choosing workflow type in Step Functions  
Execution guarantees in Step Functions workflows 
Integrating services with Step Functions  
Integrating services with Step Functions 
Process high-volume messages from Amazon SQS with Step Functions Express workflows 
Perform selective checkpointing using Standard and Express workflows 
Step Functions service quotas  
Step Functions service quotas 
Using CloudWatch Logs to log execution history in Step Functions 
AWS Step Functions API Reference  
CreateStateMachine 
UpdateStateMachine 
DescribeStateMachine 
DescribeStateMachineForExecution 
StopExecution 
DescribeExecution 
GetExecutionHistory 
ListExecutions 
ListStateMachines 
StartExecution 
CloudWatchLogsLogGroup 
LogDestination 
LoggingConfiguration 
 
  |   

December 3, 2019  |   
|   

New feature  |   

AWS Step Functions now integrates with Amazon EMR. For more information, see:  
Integrating services with Step Functions 
Create and manage Amazon EMR clusters with Step Functions 
Integrating services with Step Functions 
  |   

November 19, 2019  |   
|   

Update  |   

AWS Step Functions has released the AWS Step Functions Data Science SDK. For more information, see the following.  
Project on Github 
SDK Documentation 
The following Example Notebooks, which are available in the SageMaker AI console and the related GitHub project.  
`hello_world_workflow.ipynb` 
`machine_learning_workflow_abalone.ipynb` 
`training_pipeline_pytorch_mnist.ipynb` 
 
  |   

November 7, 2019  |   
|   

Update  |   

Step Functions now supports more API actions for Amazon SageMaker AI, and includes two new sample projects to demonstrate the functionality. For more information, see the following.  
Create and manage Amazon SageMaker AI jobs with Step Functions 
Integrating services with Step Functions 
Train a machine learning model using Amazon SageMaker AI 
Tune the hyperparameters of a machine learning model in SageMaker AI 
  |   

October 3, 2019  |   
|  New feature |  

Step Functions supports starting new workflow executions by calling `StartExecution` as an integrated service API. See:  
Start workflow executions from a task state in Step Functions 
Start a new AWS Step Functions state machine from a running execution 
Integrating services with Step Functions 
IAM Policies for Starting Step Functions Workflow Executions 
  |  August 12, 2019 |   
|  New feature |  

Step Functions includes the ability to pass a task token to integrated services, and pause the execution until that task token is returned with `SendTaskSuccess` or `SendTaskFailure`. See:  
Discover service integration patterns in Step Functions 
Wait for a Callback with Task Token 
Create a callback pattern example with Amazon SQS, Amazon SNS, and Lambda 
Integrating services with Step Functions 
Deploying a workflow that waits for human approval in Step Functions 
Service Integration Metrics 
 

Step Functions now provides a way to access dynamic information about your current execution directly in the `"Parameters"` field of a state definition. See:  
Accessing execution data from the Context object in Step Functions 
Pass Context object nodes as parameters 
  |  May 23, 2019 |   
|  New feature |  

Step Functions supports CloudWatch Events for execution status changes, see:  
Automating Step Functions event delivery with EventBridge 
 |  May 8, 2019 |   
|  New feature |  

Step Functions supports IAM permissions using tags. For more information, see:  
Tagging state machines and activities in Step Functions 
Creating tag-based IAM policies in Step Functions 
 |  March 5, 2019 |   
|  New feature |  

Step Functions Local is now available. You can run Step Functions on your local machine for testing and development. Step Functions Local is available for download as either a Java application, or as a Docker image. See Testing state machines with Step Functions Local (unsupported). |  February 4, 2019 |   
|  New feature |   

AWS Step Functions is now available in the Beijing and Ningxia regions.  |  January 15, 2018 |   
|  New feature |  

Step Functions supports resource tagging to help track your cost allocation. You can tag state machines on the Details page, or through API actions. See Tagging state machines and activities in Step Functions. |  January 7, 2019 |   
|  New feature |   

AWS Step Functions is now available in the Europe (Paris), and South America (São Paulo) regions.  |  December 13, 2018 |   
|  New feature |   

AWS Step Functions is now available the Europe (Stockholm) region.  |  December 12, 2018 |   
|   

New feature  |   

Step Functions now integrates with some AWS services. You can now directly call and pass parameters to the API of these integrated services from a task state in the Amazon States Language. For more information, see:  
Integrating services with Step Functions 
Passing parameters to a service API in Step Functions 
Integrating services with Step Functions 
  |   

November 29, 2018  |   
|   

Update  |   

Improved the description of `TimeoutSeconds` and `HeartbeatSeconds` in the documentation for task states. See Task workflow state.  |   

October 24, 2018  |   
|   

Update  |   

Improved the description for the Maximum execution history size limit and provided a link to the related best practices topic.  
Quotas related to state machine executions 
Starting new executions to avoid reaching the history quota in Step Functions 
  |   

October 17, 2018  |   
|   

Update  |   

Added a new tutorial to the AWS Step Functions documentation: See Starting a Step Functions workflow in response to events.  |   

September 25, 2018  |   
|   

Update  |   

Removed the entry Maximum executions displayed in Step Functions console from the limits documentation. See Step Functions service quotas.  |   

September 13, 2018  |   
|   

Update  |   

Added a best practices topic to the AWS Step Functions documentation on improving latency when polling for activity tasks. See Avoiding latency when polling for activity tasks.  |   

August 30, 2018  |   
|   

Update  |   

Improved the AWS Step Functions topic on activities and activity workers. See Learn about Activities in Step Functions.  |   

August 29, 2018  |   
|   

Update  |   

Improved the AWS Step Functions topic on CloudTrail integration. See Recording Step Functions API calls with AWS CloudTrail.  |   

August 7, 2018  |   
|   

Update  |   

Added JSON examples to CloudFormation tutorial. See Using CloudFormation to create a workflow in Step Functions.  |   

June 23, 2018  |   
|   

Update  |   

Added a new topic on handling Lambda service errors. See Handle transient Lambda service exceptions.  |   

June 20, 2018  |   
|  New feature |   

AWS Step Functions is now available the Asia Pacific (Mumbai) region.  |  June 28, 2018 |   
|  New feature |   

AWS Step Functions is now available the AWS GovCloud (US-West) region. For information about using Step Functions in the AWS GovCloud (US-West) Region, see AWS GovCloud (US).  |  June 28, 2018 |   
|   

Update  |   

Improved documentation on error handling for `Parallel` states. See Error Handling.  |   

June 20, 2018  |   
|   

Update  |   

Improved documentation about Input and Output processing in Step Functions. Learn how to use `InputPath`, `ResultPath`, and `OutputPath` to control the flow of JSON through your workflows, states, and tasks. See:  
Processing input and output in Step Functions 
Specifying state output using ResultPath in Step Functions 
  |   

June 7, 2018  |   
|   

Update  |   

Improved code examples for parallel states. See Parallel workflow state.  |   

June 4, 2018  |   
|   

New feature  |   

You can now monitor API and Service metrics in CloudWatch. See Monitoring Step Functions metrics using Amazon CloudWatch.  |   

May 25, 2018  |   
|  Update |   `StartExecution`, `StopExecution`, and `StateTransition` now have increased throttling limits in the following regions:  
US East (N. Virginia) 
US West (Oregon) 
Europe (Ireland) 
 For more information see Step Functions service quotas.  |  May 16, 2018 |   
|  New feature |   

AWS Step Functions is now available the US West (N. California) and Asia Pacific (Seoul) regions. See AWS Services by Region for a list of supported regions.  |  May 5, 2018 |   
|  Update |   

Updated procedures and images to match changes to the interface.  |  April 25, 2018 |   
|  Update |   

Added a new tutorial that shows how to start a new execution to continue your work. See Continue long-running workflows using Step Functions API (recommended). This tutorial describes a design pattern that can help avoid some service limitations. See Starting new executions to avoid reaching the history quota in Step Functions.  |  April 19, 2018 |   
|  Update |   

Improved introduction to states documentation by adding conceptual information about state machines. See Discovering workflow states to use in Step Functions.  |  March 9, 2018 |   
|  New feature |    
When you create a new state machine, you must acknowledge that AWS Step Functions will create an IAM role which allows access to your Lambda functions. 
Updated the following tutorials to reflect the minor changes in the state machine creation workflow:  
Creating a Step Functions state machine that uses Lambda 
Creating an Activity state machine using Step Functions 
Handling error conditions in a Step Functions state machine 
Iterate a loop with a Lambda function in Step Functions 
 
  |  February 19, 2018 |   
|  Update |  Added a topic that describes an example activity worker written in Ruby. This implementation can be used to create a Ruby activity worker directly, or as a design pattern for creating an activity worker in another language.

See Example: Activity Worker in Ruby. |  February 6, 2018 |   
|  Update |  Added a new tutorial describing a design pattern that uses a Lambda function to iterate a count.

See Creating a Step Functions state machine that uses Lambda. |  January 31, 2018 |   
|  Update |  Updated content on IAM permissions to include `DescribeStateMachineForExecution` and `UpdateStateMachine` APIs.

See Creating granular permissions for non-admin users in Step Functions. |  January 26, 2018 |   
|  Update |  Added newly available regions: Canada (Central), Asia Pacific (Singapore). |  January 25, 2018 |   
|  Update |  Updated tutorials and procedures to reflect that IAM allows you to select Step Functions as a role. |  January 24, 2018 |   
|  Update |  Added a new Best Practices topic that suggests not passing large payloads between states. 

See Using Amazon S3 ARNs instead of passing large payloads in Step Functions. |  January 23, 2018 |   
|  Update |  Corrected procedures to match updated interface for creating a state machine:  
Creating a Step Functions state machine that uses Lambda 
Creating an Activity state machine using Step Functions 
Handling error conditions in a Step Functions state machine 
 |  January 17, 2018 |   
|  New Feature |  You can use Sample Projects to quickly provision state machines and all related AWS resources. See Deploy a state machine using a starter template for Step Functions, 

Available sample projects include: 
Poll for job status with Lambda and AWS Batch 
Create a task timer with Lambda and Amazon SNS 
Note

These sample projects and related documentation replace tutorials that described implementing the same functionality. |  January 11, 2018 |   
|  Update |  Added a Best Practices section that includes information on avoiding stuck executions. See Best practices for Step Functions. |  January 5, 2018 |   
|  Update |  Added a note on how retries can affect pricing: Note

Retries are treated as state transitions. For information about how state transitions affect billing, see Step Functions Pricing.  |  December 8, 2017 |   
|  Update |  Added information related to resource names: Note

Step Functions accepts names for state machines, executions, activities, and labels that contain non-ASCII characters. Because such characters will prevent Amazon CloudWatch from logging data, we recommend using only ASCII characters so you can track Step Functions metrics. |  December 6, 2017 |   
|  Update |  Improved security overview information and added a topic on granular IAM permissions. See Security in AWS Step Functions and Creating granular permissions for non-admin users in Step Functions. |  November 27, 2017 |   
|  Update |    
Added new screenshots for state machine execution results to reflect changes in the Step Functions console. Rewrote the Lambda instructions in the following tutorials to reflect changes in the Lambda console:  
Creating a Step Functions state machine that uses Lambda 
Creating a Job Status Poller 
Creating a Task Timer 
Handling error conditions in a Step Functions state machine 
Corrected and clarified information about creating state machines in the following sections:  
Creating an Activity state machine using Step Functions 
 
  |  October 6, 2017 |   
|  Update |   

Rewrote the IAM instructions in the following sections to reflect changes in the IAM console:  
Creating an IAM role for your state machine in Step Functions 
Creating a Step Functions state machine that uses Lambda 
Creating a Job Status Poller 
Creating a Task Timer 
Handling error conditions in a Step Functions state machine 
Creating a Step Functions API using API Gateway 
  |  October 5, 2017 |   
|  Update |   

Rewrote the State Machine Data section.  |  September 28, 2017 |   
|  New feature |   

The limits related to API action throttling are increased for all regions where Step Functions is available.  |   

September 18, 2017  |   
|  Update |    
Corrected and clarified information about starting new executions in all tutorials. 
Corrected and clarified information in the Quotas related to accounts section. 
  |   

September 14, 2017  |   
|  Update |   

Rewrote the following tutorials to reflect changes in the Lambda console:  
Creating a Step Functions state machine that uses Lambda 
Handling error conditions in a Step Functions state machine 
Creating a Job Status Poller 
  |   

August 28, 2017  |   
|  New feature |   

Step Functions is available in Europe (London).  |   

August 23, 2017  |   
|  New feature |   

The visual workflows of state machines let you zoom in, zoom out, and center the graph.  |   

August 21, 2017  |   
|   

New feature  |   Important

An execution can't use the name of another execution for 90 days. 

When you make multiple `StartExecution` calls with the same name, the new execution doesn't run. 

For more information, see the `name` request parameter of the `StartExecution` API action in the AWS Step Functions API Reference.  |  August 18, 2017 |   
|  Update |   

Added information about an alternative way of passing the state machine ARN to the Creating a Step Functions API using API Gateway tutorial.  |   

August 17, 2017  |   
|  Update |  Added the new Creating a Job Status Poller tutorial. |   

August 10, 2017  |   
|   

New feature  |    
Step Functions emits the `ExecutionThrottled` CloudWatch metric. For more information, see Monitoring Step Functions metrics using Amazon CloudWatch. 
Added the Quotas related to state throttling section. 
  |  August 3, 2017 |   
|   

Update  |   

Updated the instructions in the Step 1: Create an IAM Role for API Gateway section.  |   

July 18, 2017  |   
|   

Update  |   

Corrected and clarified information in the Choice workflow state section.  |  June 23, 2017 |   
|   

Update  |   

Added information about using resources under other AWS accounts to the following tutorials:  
Creating a Step Functions state machine that uses Lambda 
Using CloudFormation to create a workflow in Step Functions 
Creating an Activity state machine using Step Functions 
Handling error conditions in a Step Functions state machine 
  |   

June 22, 2017  |   
|   

Update  |   

Corrected and clarified information in the following sections:  
Handling error conditions in a Step Functions state machine  
Discovering workflow states to use in Step Functions 
Handling errors in Step Functions workflows 
  |   

June 21, 2017  |   
|   

Update  |   

Rewrote all tutorials to match the Step Functions console refresh.  |  June 12, 2017 |   
|   

New feature  |   

Step Functions is available in Asia Pacific (Sydney).  |   

June 8, 2017  |   
|   

Update  |   

Restructured the Using Amazon States Language to define Step Functions workflows section.  |   

June 7, 2017  |   
|   

Update  |   

Corrected and clarified information in the Creating an Activity state machine using Step Functions section.  |   

June 6, 2017  |   
|   

Update  |   

Corrected the code examples in the State machine examples using Retry and Catch section.  |   

June 5, 2017  |   
|   

Update  |   

Restructured this guide using AWS documentation standards.  |   

May 31, 2017  |   
|   

Update  |   

Corrected and clarified information in the Parallel workflow state section.  |   

May 25, 2017  |   
|   

Update  |   

Merged the Paths and Filters sections into the Processing input and output in Step Functions section.  |   

May 24, 2017  |   
|   

Update  |   

Corrected and clarified information in the Monitoring Step Functions metrics using Amazon CloudWatch section.  |   

May 15, 2017  |   
|   

Update  |   

Updated the `GreeterActivities.java` worker code in the Creating an Activity state machine using Step Functions tutorial.  |   

May 9, 2017  |   
|   

Update  |   

Added an introductory video to the What is Step Functions? section.  |   

April 19, 2017  |   
|   

Update  |   

Corrected and clarified information in the following tutorials:  
Creating a Step Functions state machine that uses Lambda 
Creating an Activity state machine using Step Functions 
Handling error conditions in a Step Functions state machine 
  |   

April 19, 2017  |   
|   

Update  |   

Added information about Lambda templates to the Creating a Step Functions state machine that uses Lambda and Handling error conditions in a Step Functions state machine tutorials.  |   

April 6, 2017  |   
|   

Update  |   

Changed the "Maximum input or result data size" limit to "Maximum input or result data size for a task, state, or execution" (32,768 characters). For more information, see Quotas related to task executions.  |   

March 31, 2017  |   
|   

New feature  |    
Step Functions supports executing state machines by setting Step Functions as Amazon CloudWatch Events targets. 
  |   

March 21, 2017  |   
|   

New feature  |    
Step Functions allows Lambda function error handling as the preferred error handling method. 
Updated the Handling error conditions in a Step Functions state machine tutorial and the Handling errors in Step Functions workflows section. 
  |   

March 16, 2017  |   
|   

New feature  |   

Step Functions is available in Europe (Frankfurt).  |   

March 7, 2017  |   
|   

Update  |   

Reorganized the topics in the table of contents and updated the following tutorials:  
Creating a Step Functions state machine that uses Lambda 
Creating an Activity state machine using Step Functions 
Handling error conditions in a Step Functions state machine 
  |   

February 23, 2017  |   
|   

New feature  |    
The State Machines page of the Step Functions console includes the Copy to New and Delete buttons. 
Updated the screenshots to match the console changes. 
  |   

February 23, 2017  |   
|   

New feature  |    
Step Functions supports creating APIs using API Gateway. 
Added the Creating a Step Functions API using API Gateway tutorial. 
  |   

February 14, 2017  |   
|   

New feature  |    
Step Functions supports integration with CloudFormation. 
Added the Using CloudFormation to create a workflow in Step Functions tutorial. 
  |   

February 10, 2017  |   
|   

Update  |   

Clarified the current behavior of the `ResultPath` and `OutputPath` fields in relation to `Parallel` states.  |   

February 6, 2017  |   
|   

Update  |    
Clarified state machine naming restrictions in tutorials. 
Corrected some code examples. 
  |   

January 5, 2017  |   
|   

Update  |   

Updated Lambda function examples to use the latest programming model.  |   

December 9, 2016  |   
|   

Initial release  |   

Initial release of AWS Step Functions.  |   

December 1, 2016  |
