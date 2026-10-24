> Source: https://docs.aws.amazon.com/autoscaling/ec2/userguide/DocumentHistory.html
> Downloaded: 2026-10-24

# Document history

The following table describes important additions to the Amazon EC2 Auto Scaling documentation, beginning in July 2018. For notification about updates to this documentation, you can subscribe to the RSS feed.
| Change | Description | Date | 
| 

Availability Zone distribution: reservations then balanced | 

Auto Scaling now provides a Reservations then balanced Availability Zone distribution strategy that launches instances into your Capacity Reservations first, and then balances any remaining capacity across Availability Zones. For more information, see Auto Scaling group Availability Zone distribution. | 

June 30, 2026 | 
| 

Security IAM update | 

The AutoScalingServiceRolePolicy now includes the `ec2:CreateReplaceRootVolumeTask` permission that allows you to replace root volumes on instances as part of an instance refresh. Additionally, the `events:DescribeRule` permission has been removed from the policy. | 

November 20, 2025 | 
| 

Replace root volumes | 

Root volume replacement updates your instances by replacing only the root EBS volume while keeping the instance running. For more information, see  Replace root volumes during instance refresh. | 

November 20, 2025 | 
| 

Instance lifecycle policies | 

Instance lifecycle policies give you control over what happens when termination lifecycle hooks don't complete successfully. For more information, see  Replace root volumes during instance refresh. | 

November 20, 2025 | 
| 

Synchronous provisioning | 

You can now use the LaunchInstances API to synchronously launch instances with immediate feedback and have precise control over which Availability Zone instances launch in. For more information, see Synchronous provisioning. | 

November 18, 2025 | 
| 

Lambda notification target for lifecycle hooks | 

You can now route lifecycle hook notifications directly to AWS Lambda functions. For more information, see  Route notifications to AWS Lambda directly. | 

July 28, 2025 | 
| 

High-resolution metrics | 

Target tracking now supports high-resolution CloudWatch metrics with seconds-level data points that are published at lower intervals than one minute. For more information, see Create a target tracking policy using high-resolution metrics for faster response. | 

November 22, 2024 | 
| 

Security IAM update | 

The AutoScalingServiceRolePolicy managed policy now grants additional permission to Resource Groups `resource-groups:ListGroupResources`. | 

November 20, 2024 | 
| 

Performance protection | 

When using attribute-based instance type selection for your Auto Scaling group, you can now enable performance protection to ensure that the selected instance types are similar to or exceed a specified performance baseline. For more information, see Create mixed instances group using attribute-based instance type selection. | 

November 20, 2024 | 
| 

Capacity Reservation preference | 

You can now prioritize launching instances into Capacity Reservations. For more information, see Capacity Reservations. | 

November 20, 2024 | 
| 

Zonal shift | 

You can now use zonal shift to recover from application impairments in an Availability Zone. For more information, see Auto Scaling group zonal shift.  | 

November 18, 2024 | 
| 

Availability Zone distribution | 

You can now choose an Availability Zone distribution for your Auto Scaling group. For more information, see Auto Scaling group Availability Zone distribution.  | 

November 7, 2024 | 
| 

Security IAM update | 

The AutoScalingServiceRolePolicy managed policy now grants additional permissions to Amazon EC2 (`ec2:GetSecurityGroupsForVpc` and `ec2:GetInstanceTypesFromInstanceRequirements`). | 

February 29, 2024 | 
| 

Warm pool hibernation supported in additional AWS Regions | 

You can now hibernate instances in a warm pool in two additional Regions: AWS GovCloud (US-East) and AWS GovCloud (US-West). For more information about warm pools, see Warm pools for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

February 26, 2024 | 
| 

Warm pool hibernation supported in additional AWS Regions | 

You can now hibernate instances in a warm pool in two additional Regions: Europe (Zurich) and Middle East (UAE). For more information about warm pools, see Warm pools for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

February 21, 2024 | 
| 

Support for cross-account parameter use | 

You can now use an AWS Systems Manager parameter shared from another AWS account with Amazon EC2 Auto Scaling. For more information, see Use AWS Systems Manager parameters instead of AMI IDs in launch templates in the Amazon EC2 Auto Scaling User Guide. | 

February 21, 2024 | 
| 

New Spot price protection option | 

You can now define your price protection threshold for Spot Instances as a percentage of an On-Demand price when you use attribute-based instance type selection. For more information, see Price protection in the Amazon EC2 Auto Scaling User Guide. | 

January 29, 2024 | 
| 

Instance maintenance policies | 

You can now use an instance maintenance policy to define whether instances are launched before or after existing instances are terminated during events that cause your instances to be replaced, including an instance refresh. For more information, see Instance maintenance policies in the Amazon EC2 Auto Scaling User Guide. | 

November 15, 2023 | 
| 

Capacity Blocks for ML | 

You can now launch instances into a Capacity Block by specifying the Capacity Block reservation ID when you create a launch template. With Capacity Blocks, you can reserve GPU instances on a future date to support your short-duration, machine learning (ML) workloads. For more information, see Use Capacity Blocks for machine learning workloads in the Amazon EC2 Auto Scaling User Guide. | 

October 31, 2023 | 
| 

New instance refresh features | 

You can now configure an instance refresh to set its status to failed and optionally roll back when it detects that a specified CloudWatch alarm has gone into the `ALARM` state. For more information, see Undo changes with a rollback in the Amazon EC2 Auto Scaling User Guide. | 

July 31, 2023 | 
| 

Guide changes | 

A new topic about launching On-Demand Instances into Capacity Reservations has been added to the guide. For more information, see Use On-Demand Capacity Reservations to reserve capacity in specific Availability Zones in the Amazon EC2 Auto Scaling User Guide. | 

July 28, 2023 | 
| 

Guide changes | 

A new topic about migrating your AWS CloudFormation stacks from launch configurations to launch templates has been added to the guide. For more information, see Migrate AWS CloudFormation stacks from launch configurations to launch templates in the Amazon EC2 Auto Scaling User Guide. | 

April 18, 2023 | 
| 

Support for new API operations | 

This release adds three new API operations, `AttachTrafficSources`, `DetachTrafficSources`, and `DescribeTrafficSources`. Also, a new field, `TrafficSources`, has been added to the results of `DescribeAutoScalingGroups` operations. A new activity status, `WaitingForConnectionDraining`, has been added to the results of `DescribeScalingActivities` operations. Amazon EC2 Auto Scaling also supports a new value, `VPC_LATTICE`, for the `HealthCheckType` field in `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, and `DescribeAutoScalingGroups` operations. For more information, see the Amazon EC2 Auto Scaling API Reference. | 

March 31, 2023 | 
| 

Support for Amazon VPC Lattice | 

This is the general availability release of VPC Lattice for Amazon EC2 Auto Scaling. For more information, see Route traffic to your Auto Scaling group with a VPC Lattice target group in the Amazon EC2 Auto Scaling User Guide. | 

March 31, 2023 | 
| 

Guide changes | 

The section with AWS CLI examples for working with Elastic Load Balancing now includes new and updated examples. For more information, see Examples for working with Elastic Load Balancing with the AWS Command Line Interface (AWS CLI) in the Amazon EC2 Auto Scaling User Guide.  | 

March 31, 2023 | 
| 

Support for predictive scaling in additional AWS Regions | 

You can now create predictive scaling policies in the Middle East (UAE) and AWS GovCloud (US-East) Regions. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

March 16, 2023 | 
| 

New instance refresh features | 

You can now choose to terminate or ignore instances on standby and replace or ignore instances protected from scale in, instead of waiting for them to become replaceable. You can also roll back changes from a failed instance refresh. As part of this update, the documentation has been expanded to include topics for rolling back an instance refresh, cancelling an instance refresh, and understanding the default values for the configurable parameters of an instance refresh. For more information, see Replacing Auto Scaling instances based on an instance refresh in the Amazon EC2 Auto Scaling User Guide. | 

February 10, 2023 | 
| 

Support for using an AWS Systems Manager parameter for an AMI ID | 

You can now use a Systems Manager parameter instead of an AMI ID in your launch template. For more information, see Using AWS Systems Manager parameters instead of AMI IDs in launch templates in the Amazon EC2 Auto Scaling User Guide. | 

January 19, 2023 | 
| 

Predictive scaling recommendations | 

You can now get recommendations for evaluating and choosing the right predictive scaling policy from the Amazon EC2 Auto Scaling console. For more information, see Evaluate your predictive scaling policies in the Amazon EC2 Auto Scaling User Guide. | 

January 18, 2023 | 
| 

Predictive scaling forecasts | 

The forecasts generated by predictive scaling now update every six hours instead of daily. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

January 6, 2023 | 
| 

Support for CloudWatch metric math | 

You can now use metric math when you create target tracking scaling policies. With metric math, you can query multiple CloudWatch metrics and use math expressions to create new time series based on these metrics. For more information, see Create a target tracking scaling policy for Amazon EC2 Auto Scaling using metric math in the Amazon EC2 Auto Scaling User Guide. | 

December 8, 2022 | 
| 

Update to IAM service-linked role permissions | 

The `AutoScalingServiceRolePolicy` policy now grants additional permissions to Amazon EC2 Auto Scaling. For more information, see AWS managed policies for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

December 6, 2022 | 
| 

New Spot allocation strategy | 

You can now use the price and capacity optimized allocation strategy to request Spot Instances from the Spot pools that are the least likely to be interrupted and have the lowest possible price. For more information, see Allocation strategies in the Amazon EC2 Auto Scaling User Guide. | 

November 10, 2022 | 
| 

Support for predictive scaling in Asia Pacific (Jakarta) Region | 

You can now create predictive scaling policies in Asia Pacific (Jakarta) Region. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

October 13, 2022 | 
| 

Support for custom metrics for predictive scaling in the console | 

You can now use custom metrics when creating predictive scaling policies from the Amazon EC2 Auto Scaling console. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

October 13, 2022 | 
| 

CloudWatch monitoring for predictive scaling metrics | 

You can now access monitoring data for predictive scaling using CloudWatch. This lets you use metric math to create new time series that display the accuracy of forecast data. For more information, see Monitor predictive scaling metrics with CloudWatch in the Amazon EC2 Auto Scaling User Guide. | 

July 7, 2022 | 
| 

Support for predictive scaling in Asia Pacific (Osaka) Region | 

You can now create predictive scaling policies in Asia Pacific (Osaka) Region. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

July 6, 2022 | 
| 

Warm pool hibernation supported in additional Regions | 

You can now hibernate instances in a warm pool in four additional Regions: Africa (Cape Town), Asia Pacific (Jakarta), Asia Pacific (Osaka), and Europe (Milan). For more information about warm pools, see Warm pools for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

July 5, 2022 | 
| 

Update to health checks | 

When performing health checks, Amazon EC2 Auto Scaling now helps you minimize any downtime that can occur because of temporary issues or misconfigured health checks. For more information, see How Amazon EC2 Auto Scaling minimizes downtime in the Amazon EC2 Auto Scaling User Guide. | 

May 21, 2022 | 
| 

Default instance warmup | 

You can now unify all the warmup and cooldown settings for an Auto Scaling group and optimize the performance of scaling policies that scale continuously by enabling default instance warmup. For more information, see Set the default instance warmup for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. | 

April 19, 2022 | 
| 

Guide changes | 

A new chapter about integrating with other AWS services has been added to the guide. For more information, see AWS services integrated with Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

March 29, 2022 | 
| 

Update to IAM service-linked role permissions | 

The `AutoScalingServiceRolePolicy` policy now grants additional read permissions to Amazon EC2 Auto Scaling. For more information, see AWS managed policies for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

March 28, 2022 | 
| 

Instance metadata provides target lifecycle state | 

You can retrieve an Auto Scaling instance's target lifecycle state from the instance metadata. For more information, see Retrieve the target lifecycle state through instance metadata in the Amazon EC2 Auto Scaling User Guide. | 

March 24, 2022 | 
| 

Support for new warm pool functionality | 

You can now hibernate instances in a warm pool to stop instances without deleting their memory contents (RAM). You can now also return instances to the warm pool on scale in, instead of always terminating instance capacity that you will need later. For more information, see Warm pools for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

February 24, 2022 | 
| 

Guide changes | 

The Amazon EC2 Auto Scaling console has been updated with additional options to help you start an instance refresh with skip matching enabled and a desired configuration specified. For more information, see Start or cancel an instance refresh (console) in the Amazon EC2 Auto Scaling User Guide. | 

February 3, 2022 | 
| 

Custom metrics for predictive scaling policies | 

You can now choose whether to use custom metrics when you create predictive scaling policies. You can also use metric math to further customize the metrics that you include in your policy. For more information, see Advanced predictive scaling policy configurations using custom metrics. | 

November 24, 2021 | 
| 

New On-Demand allocation strategy | 

You can now choose whether to launch On-Demand Instances based on price (lowest priced instance types first) when you create an Auto Scaling group that uses a mixed instances policy. For more information, see Allocation strategies in the Amazon EC2 Auto Scaling User Guide. | 

October 27, 2021 | 
| 

Attribute-based instance type selection | 

Amazon EC2 Auto Scaling adds support for attribute-based instance type selection. Instead of manually choosing instance types, you can express your instance requirements as a set of attributes, such as vCPU, memory, and storage. For more information, see Creating an Auto Scaling group using attribute-based instance type selection in the Amazon EC2 Auto Scaling User Guide. | 

October 27, 2021 | 
| 

Support for filtering groups by tags | 

You can now filter your Auto Scaling groups using tag filters when you retrieve information about your Auto Scaling groups using the `describe-auto-scaling-groups` command. For more information, see Use tags to filter Auto Scaling groups in the Amazon EC2 Auto Scaling User Guide. | 

October 14, 2021 | 
| 

Guide changes | 

The Amazon EC2 Auto Scaling console has been updated to help you create custom termination policies with AWS Lambda. The console documentation has been revised accordingly. For more information, see Using different termination policies (console). | 

October 14, 2021 | 
| 

Support for copying launch configurations to launch templates | 

You can now copy all launch configurations in an AWS Region to new launch templates from the Amazon EC2 Auto Scaling console. | 

August 9, 2021 | 
| 

Expands instance refresh functionality | 

You can now include updates, such as a new version of a launch template, when replacing instances by adding your desired configuration to the `start-instance-refresh` command. You can also skip replacing instances that already have your desired configuration by enabling skip matching. For more information, see Replacing Auto Scaling instances based on an instance refresh in the Amazon EC2 Auto Scaling User Guide. | 

August 5, 2021 | 
| 

Support for custom termination policies | 

You can now create custom termination policies with AWS Lambda. For more information, see Creating a custom termination policy with Lambda. The documentation for specifying termination policies has been updated accordingly. | 

July 29, 2021 | 
| 

Guide changes | 

The Amazon EC2 Auto Scaling console has been updated and enhanced with additional features to help you create scheduled actions with a time zone specified. The documentation for Scheduled scaling has been revised accordingly. | 

June 3, 2021 | 
| 

gp3 volumes in launch configurations | 

You can now specify gp3 volumes in the block device mappings for launch configurations. | 

June 2, 2021 | 
| 

Support for predictive scaling | 

You can now use predictive scaling to proactively scale your Amazon EC2 Auto Scaling groups using a scaling policy. For more information, see Predictive scaling for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. With this update, the AutoScalingServiceRolePolicy managed policy now includes permission to call the `cloudwatch:GetMetricData` API action. | 

May 19, 2021 | 
| 

Guide changes | 

You can now access example templates for lifecycle hooks from GitHub. For more information, see Amazon EC2 Auto Scaling lifecycle hooks in the Amazon EC2 Auto Scaling User Guide. | 

April 9, 2021 | 
| 

Support for warm pools | 

You can now balance performance (minimize cold starts) and cost (stop over-provisioning instance capacity) for applications with long first boot times by adding warm pools to Auto Scaling groups. For more information, see Warm pools for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

April 8, 2021 | 
| 

Support for checkpoints | 

You can now add checkpoints to an instance refresh to replace instances in phases and perform verifications on your instances at specific points. For more information, see Adding checkpoints to an instance refresh in the Amazon EC2 Auto Scaling User Guide. | 

March 18, 2021 | 
| 

Guide changes | 

Improved documentation for using EventBridge with Amazon EC2 Auto Scaling events and lifecycle hooks. For more information, see Using Amazon EC2 Auto Scaling with EventBridge and Tutorial: Configure a lifecycle hook that invokes a Lambda function in the Amazon EC2 Auto Scaling User Guide. | 

March 18, 2021 | 
| 

Support for local time zones | 

You can now create recurring scheduled actions in the local time zone by adding the `--time-zone` option to the put-scheduled-update-group-action command. If your time zone observes Daylight Saving Time (DST), the recurring action automatically adjusts for Daylight Saving Time. For more information, see Scheduled scaling in the Amazon EC2 Auto Scaling User Guide. | 

March 9, 2021 | 
| 

Expands functionality for mixed instances policies | 

You can now prioritize instance types for your Spot capacity when you use a mixed instances policy. Amazon EC2 Auto Scaling attempts to fulfill priorities on a best-effort basis but optimizes for capacity first. For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide. | 

March 8, 2021 | 
| 

Scaling activities for deleted groups | 

You can now view scaling activities for deleted Auto Scaling groups by adding the `--include-deleted-groups` option to the describe-scaling-activities command. For more information, see Troubleshooting Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

February 23, 2021 | 
| 

Console improvements | 

You can now create and attach an Application Load Balancer or Network Load Balancer from the Amazon EC2 Auto Scaling console. For more information, see Create and attach a new Application Load Balancer or Network Load Balancer (console) in the Amazon EC2 Auto Scaling User Guide. | 

November 24, 2020 | 
| 

Multiple network interfaces | 

You can now configure a launch template for an Auto Scaling group that specifies multiple network interfaces. For more information, see Network interfaces in a VPC.  | 

November 23, 2020 | 
| 

Multiple launch templates | 

Multiple launch templates can now be used with Auto Scaling groups. For more information, see Specifying a different launch template for an instance type in the Amazon EC2 Auto Scaling User Guide. | 

November 19, 2020 | 
| 

Gateway Load Balancers | 

Updated guide to show how to attach a Gateway Load Balancer to an Auto Scaling group to ensure that appliance instances launched by Amazon EC2 Auto Scaling are automatically registered and deregistered from the load balancer. For more information, see Elastic Load Balancing types and Attaching a load balancer to your Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. | 

November 10, 2020 | 
| 

Maximum instance lifetime | 

You can now reduce the maximum instance lifetime to one day (86,400 seconds). For more information, see Replacing Auto Scaling instances based on maximum instance lifetime in the Amazon EC2 Auto Scaling User Guide. | 

November 9, 2020 | 
| 

Capacity Rebalancing | 

You can configure your Auto Scaling group to launch a replacement Spot Instance when Amazon EC2 emits a rebalance recommendation. For more information, see Amazon EC2 Auto Scaling Capacity Rebalancing in the Amazon EC2 Auto Scaling User Guide. | 

November 4, 2020 | 
| 

Instance metadata service version 2 | 

You can require the use of Instance Metadata Service Version 2, which is a session-oriented method for requesting instance metadata, when using launch configurations. For more information, see Configuring the instance metadata options in the Amazon EC2 Auto Scaling User Guide. | 

July 28, 2020 | 
| 

Guide changes | 

Various improvements and new console procedures in the Controlling which Auto Scaling instances terminate during scale in, Monitoring your Auto Scaling instances and groups, Launch templates, and Launch configurations sections of the Amazon EC2 Auto Scaling User Guide. | 

July 28, 2020 | 
| 

Instance refresh | 

Start an instance refresh to update all instances in your Auto Scaling group when you make a configuration change. For more information, see Replacing Auto Scaling instances based on an instance refresh in the Amazon EC2 Auto Scaling User Guide. | 

June 16, 2020 | 
| 

Guide changes | 

Various improvements in the Replacing Auto Scaling instances based on maximum instance lifetime, Auto Scaling groups with multiple instance types and purchase options, Scaling based on Amazon SQS, and Tagging Auto Scaling groups and instances sections of the Amazon EC2 Auto Scaling User Guide. | 

May 6, 2020 | 
| 

Guide changes | 

Various improvements to IAM documentation. For more information, see Launch template support and Amazon EC2 Auto Scaling identity-based policy examples in the Amazon EC2 Auto Scaling User Guide. | 

March 4, 2020 | 
| 

Disable scaling policies | 

You can now disable and re-enable scaling policies. This feature allows you to temporarily disable a scaling policy while preserving the configuration details so that you can enable the policy again later. For more information, see Disabling a scaling policy for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. | 

February 18, 2020 | 
| 

Add notification functionality | 

Amazon EC2 Auto Scaling now sends events to your AWS Health Dashboard when your Auto Scaling groups cannot scale out due to a missing security group or launch template. For more information, see Health Dashboard notifications for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

February 12, 2020 | 
| 

Guide changes | 

Various improvements and corrections in the How Amazon EC2 Auto Scaling works with IAM, Amazon EC2 Auto Scaling identity-based policy examples, Required CMK key policy for use with encrypted volumes, and Monitoring your Auto Scaling instances and groups sections of the Amazon EC2 Auto Scaling User Guide. | 

February 10, 2020 | 
| 

Guide changes | 

Improved documentation for Auto Scaling groups that use instance weighting. Learn how to use scaling policies when using "capacity units" to measure desired capacity. For more information, see How scaling policies work and Scaling adjustment types in the Amazon EC2 Auto Scaling User Guide. | 

February 6, 2020 | 
| 

New "Security" chapter | 

A new Security chapter in the Amazon EC2 Auto Scaling User Guide helps you understand how to apply the shared responsibility model when using Amazon EC2 Auto Scaling. As part of this update, the user guide chapter "Controlling Access to Your Amazon EC2 Auto Scaling Resources" has been replaced by a new, more useful section, Identity and access management for Amazon EC2 Auto Scaling. | 

February 4, 2020 | 
| 

Recommendations for instance types | 

AWS Compute Optimizer provides Amazon EC2 instance recommendations to help you improve performance, save money, or both. For more information, see Getting recommendations for an instance type in the Amazon EC2 Auto Scaling User Guide. | 

December 3, 2019 | 
| 

Dedicated Hosts and host resource groups | 

Updated guide to show how to create a launch template that specifies a host resource group. This allows you to create an Auto Scaling group with a launch template that specifies a BYOL AMI to use on Dedicated Hosts. For more information, see Creating a launch template for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. | 

December 3, 2019 | 
| 

Support for Amazon VPC endpoints | 

You can now establish a private connection between your VPC and Amazon EC2 Auto Scaling. For more information, see Amazon EC2 Auto Scaling and interface VPC endpoints in the Amazon EC2 Auto Scaling User Guide. | 

November 22, 2019 | 
| 

Maximum instance lifetime | 

You can now replace instances automatically by specifying the maximum length of time that an instance can be in service. If any instances are approaching this limit, Amazon EC2 Auto Scaling gradually replaces them. For more information, see Replacing Auto Scaling instances based on maximum instance lifetime in the Amazon EC2 Auto Scaling User Guide. | 

November 19, 2019 | 
| 

Instance weighting | 

For Auto Scaling groups with multiple instance types, you can now optionally specify the number of capacity units that each instance type contributes to the capacity of the group. For more information, see Instance weighting for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. | 

November 19, 2019 | 
| 

Minimum number of instance types | 

You no longer have to specify additional instance types for groups of Spot, On-Demand, and Reserved Instances. For all Auto Scaling groups, the minimum is now one instance type. For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide. | 

September 16, 2019 | 
| 

Support for new Spot allocation strategy | 

Amazon EC2 Auto Scaling now supports a new Spot allocation strategy "capacity-optimized" that fulfills your request using Spot Instance pools that are optimally chosen based on the available Spot capacity. For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide. | 

August 12, 2019 | 
| 

Guide changes | 

Improved Amazon EC2 Auto Scaling documentation in the Service-linked roles and Required CMK key policy for use with encrypted volumes topics. | 

August 1, 2019 | 
| 

Support for tagging enhancement | 

Amazon EC2 Auto Scaling now adds tags to Amazon EC2 instances as part of the same API call that launches the instances. For more information, see Tagging Auto Scaling groups and instances. | 

July 26, 2019 | 
| 

Guide changes | 

Improved Amazon EC2 Auto Scaling documentation in the Suspending and resuming scaling processes topic. Updated Customer managed policy examples to include an example policy that allows users to pass only specific custom suffix service-linked roles to Amazon EC2 Auto Scaling. | 

June 13, 2019 | 
| 

Support for new Amazon EBS feature | 

Added support for new Amazon EBS feature in the launch template topic. Change the encryption state of an EBS volume while restoring from a snapshot. For more information, see Creating a launch template for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. | 

May 13, 2019 | 
| 

Guide changes | 

Improved Amazon EC2 Auto Scaling documentation in the following sections: Controlling which Auto Scaling instances terminate during scale in, Auto Scaling groups, Auto Scaling groups with multiple instance types and purchase options, and Dynamic scaling for Amazon EC2 Auto Scaling. | 

March 12, 2019 | 
| 

Support for combining instance types and purchase options | 

Provision and automatically scale instances across purchase options (Spot, On-Demand, and Reserved Instances) and instance types within a single Auto Scaling group. For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide. | 

November 13, 2018 | 
| 

Updated topic for scaling based on Amazon SQS | 

Updated guide to explain how you can use custom metrics to scale an Auto Scaling group in response to changing demand from an Amazon SQS queue. For more information, see Scaling based on Amazon SQS in the Amazon EC2 Auto Scaling User Guide. | 

July 26, 2018 | 

The following table describes important changes to the Amazon EC2 Auto Scaling documentation before July 2018. 
|  Feature |  Description |  Release date |    
|   

Support for target tracking scaling policies  |   

Set up dynamic scaling for your application in just a few steps. For more information, see Target tracking scaling policies for Amazon EC2 Auto Scaling.  |  12 July 2017 |   
|   

Support for resource-level permissions  |   

Create IAM policies to control access at the resource level. For more information, see Controlling access to your Amazon EC2 Auto Scaling resources.  |  15 May 2017 |   
|   

Monitoring improvements  |   

Auto Scaling group metrics no longer require that you enable detailed monitoring. You can now enable group metrics collection and view metrics graphs from the Monitoring tab in the console. For more information, see Monitoring your Auto Scaling groups and instances using Amazon CloudWatch.  |  18 August 2016 |   
|   

Support for Application Load Balancers  |   

Attach one or more target groups to a new or existing Auto Scaling group. For more information, see Attaching a load balancer to your Auto Scaling group.  |  11 August 2016 |   
|   

Events for lifecycle hooks  |   

Amazon EC2 Auto Scaling sends events to EventBridge when it calls lifecycle hooks. For more information, see Getting EventBridge when your Auto Scaling group scales.  |  24 February 2016 |   
|   

Instance protection  |   

Prevent Amazon EC2 Auto Scaling from selecting specific instances for termination when scaling in. For more information, see Instance protection.  |  07 December 2015 |   
|   

Step scaling policies  |   

Create a scaling policy that enables you to scale based on the size of the alarm breach. For more information, see Scaling policy types.  |  06 July 2015 |   
|   

Update load balancer  |   

Attach a load balancer to or detach a load balancer from an existing Auto Scaling group. For more information, see Attaching a load balancer to your Auto Scaling group.  |  11 June 2015 |   
|   

Support for ClassicLink  |   

Link EC2-Classic instances in your Auto Scaling group to a VPC, enabling communication between these linked EC2-Classic instances and instances in the VPC using private IP addresses. For more information, see Linking EC2-Classic instances to a VPC.  |  19 January 2015 |   
|   

Lifecycle hooks  |   

Hold your newly launched or terminating instances in a pending state while you perform actions on them. For more information, see Amazon EC2 Auto Scaling lifecycle hooks.  |  30 July 2014 |   
|   

Detach instances  |   

Detach instances from an Auto Scaling group. For more information, see Detach EC2 instances from your Auto Scaling group.  |  30 July 2014 |   
|   

Put instances into a Standby state  |   

Put instances that are in an `InService` state into a `Standby` state. For more information, see Temporarily removing instances from your Auto Scaling group.  |  30 July 2014 |   
|   

Manage tags  |   

Manage your Auto Scaling groups using the AWS Management Console. For more information, see Tagging Auto Scaling groups and instances.  |  01 May 2014 |   
|   

Support for Dedicated Instances  |   

Launch Dedicated Instances by specifying a placement tenancy attribute when you create a launch configuration. For more information, see Instance placement tenancy.  |  23 April 2014 |   
|   

Create a group or launch configuration from an EC2 instance  |   

Create an Auto Scaling group or a launch configuration using an EC2 instance. For information about creating a launch configuration using an EC2 instance, see Create a launch configuration using an EC2 instance. For information about creating an Auto Scaling group using an EC2 instance, see Creating an Auto Scaling group using an EC2 instance.  |  02 January 2014 |   
|   

Attach instances  |   

Enable automatic scaling for an EC2 instance by attaching the instance to an existing Auto Scaling group. For more information, see Attach EC2 instances to your Auto Scaling group.  |  02 January 2014 |   
|   

View account limits  |   

View the limits on Auto Scaling resources for your account. For more information, see Quotas for Auto Scaling resources and groups.  |  02 January 2014 |   
|   

Console support for Amazon EC2 Auto Scaling  |   

Access Amazon EC2 Auto Scaling using the AWS Management Console. For more information, see Getting started with Amazon EC2 Auto Scaling.   |  10 December 2013 |   
|   

Assign a public IP address  |   

Assign a public IP address to an instance launched into a VPC. For more information, see Launching Auto Scaling instances in a VPC.  |  19 September 2013 |   
|   

Instance termination policy  |   

Specify an instance termination policy for Amazon EC2 Auto Scaling to use when terminating EC2 instances. For more information, see Controlling which Auto Scaling instances terminate during scale in.  |  17 September 2012 |   
|   

Support for IAM roles  |   

Launch EC2 instances with an IAM instance profile. You can use this feature to assign IAM roles to your instances, allowing your applications to access other Amazon Web Services securely. For more information, see Launch Auto Scaling instances with an IAM role.  |  11 June 2012 |   
|   

Support for Spot Instances  |   

Launch Spot Instances with a launch configuration. For more information, see Requesting Spot Instances for fault-tolerant and flexible applications.  |  7 June 2012 |   
|   

Tag groups and instances  |   

Tag Auto Scaling groups and specify that the tag also applies to EC2 instances launched after the tag was created. For more information, see Tagging Auto Scaling groups and instances.  |  26 January 2012 |   
|   

Support for Amazon SNS  |   

Use Amazon SNS to receive notifications whenever Amazon EC2 Auto Scaling launches or terminates EC2 instances. For more information, see Getting SNS notifications when your Auto Scaling group scales. 

Amazon EC2 Auto Scaling also added the following new features:  
The ability to set up recurring scaling activities using cron syntax. For more information, see the `PutScheduledUpdateGroupAction` API operation. 
A new configuration setting that allows you to scale out without adding the launched instance to the load balancer (LoadBalancer). For more information, see the `ProcessType` API data type. 
The `ForceDelete` flag in the `DeleteAutoScalingGroup` operation that tells Amazon EC2 Auto Scaling to delete the Auto Scaling group with the instances associated to it without waiting for the instances to be terminated first. For more information, see the `DeleteAutoScalingGroup` API operation. 
  |  20 July 2011 |   
|   

Scheduled scaling actions  |   

Added support for scheduled scaling actions. For more information, see Scheduled scaling for Amazon EC2 Auto Scaling.  |  2 December 2010 |   
|   

Support for Amazon VPC  |   

Added support for Amazon VPC. For more information, see Launching Auto Scaling instances in a VPC.  |  2 December 2010 |   
|   

Support for HPC clusters  |   

Added support for high performance computing (HPC) clusters.  |  2 December 2010 |   
|   

Support for health checks  |   

Added support for using Elastic Load Balancing health checks with Amazon EC2 Auto Scaling-managed EC2 instances. For more information, see Health checks for instances in an Auto Scaling group.  |  2 December 2010 |   
|   

Support for CloudWatch alarms  |   

Removed the older trigger mechanism and redesigned Amazon EC2 Auto Scaling to use the CloudWatch alarm feature. For more information, see Dynamic scaling for Amazon EC2 Auto Scaling.  |  2 December 2010 |   
|   

Suspend and resume scaling  |   

Added support to suspend and resume scaling processes.  |  2 December 2010 |   
|   

Support for IAM  |   

Added support for IAM. For more information, see Controlling access to your Amazon EC2 Auto Scaling resources.  |  2 December 2010 |
