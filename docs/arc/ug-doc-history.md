> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/doc-history.html
> Downloaded: 2026-10-24

# Document history for the Amazon Application Recovery Controller (ARC) Developer Guide

The following entries describe important changes made to the Amazon Application Recovery Controller (ARC) documentation. 
Version: latest 
Latest documentation update: September 24th, 2026 
 
|  Change |  Description |  Date |    
|  Zonal shift support for additional Network Load Balancer target group configurations |  

You can now use zonal shift with cross-zone enabled Network Load Balancers that have target groups with connection termination for unhealthy targets enabled, UDP target groups, or Application Load Balancers as targets. 

For more information, see Network Load Balancers.  |  September 24, 2026 |   
|  Readiness check availability change |  

The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. 

For more information, see Amazon Application Recovery Controller (ARC) readiness check availability change.  |  April 30, 2026 |   
|  Readiness check availability change |  

The readiness check feature in Amazon Application Recovery Controller (ARC) will no longer be open to new customers starting April 30, 2026. Existing customers can continue to use the service as normal. 

For more information, see Amazon Application Recovery Controller (ARC) readiness check availability change.  |  March 31, 2026 |   
|  New managed policy for Region switch plan execution |  

Amazon Application Recovery Controller (ARC) released a new managed policy, `AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy`, that grants permissions for Region switch plan execution and evaluation. 

For more information, see Amazon Application Recovery Controller (ARC) updates to AWS managed policies.  |  November 3rd, 2025 |   
|  You can now use AWS PrivateLink between your VPC and Amazon Application Recovery Controller (ARC) zonal shift. |  

You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Application Recovery Controller (ARC) zonal shift. 

For more information, see Access Amazon Application Recovery Controller (ARC) zonal shift using an interface endpoint (AWS PrivateLink).  |  August 11, 2025 |   
|  New Region switch service |  

Region switch enables customers to orchestrate the specific steps, supporting cross-account, that are needed to operate their multi-Region application out of another AWS Region. 

For more information, see Region switch in ARC.  |  August 1, 2025 |   
|  Enhancements to practice runs |  

You can now start on-demand practice runs in ARC. In addition, practice runs now include checks for sufficient capacity in other AZs in the Region. 

For more information, see How it works.  |  June 30, 2025 |   
|  Updates a managed policy |  

Updates the `AWSZonalAutoshiftPracticeRunSLRPolicy` managed policy by adding the policy statement `AutoshiftPracticeCheckPermissions` with the permissions `autoscaling:DescribeAutoScalingGroups`, `ec2:DescribeInstances`, `elasticloadbalancing:DescribeTargetHealth`, and `elasticloadbalancing:DescribeTargetHealth` to support balanced capacity checks. 

For more information, see AWSZonalAutoshiftPracticeRunSLRPolicy managed policy. |  June 30, 2025 |   
|  Updates to exception types for zonal autoshift |  

You can now interact with zonal autoshift on a per-resource basis. 

For more information, see How it works.  |  April 21, 2025 |   
|  Test ARC zonal autoshift with AWS FIS |  

You can use AWS FIS to test how ARC zonal autoshift automatically recovers your application during an AZ power interruption 

For more information, see Testing zonal autoshift with AWS FIS.  |  March 26, 2025 |   
|  ARC now supports IPv6 endpoints for routing controls and zonal shift. |  

ARC now supports IPv6 endpoints for routing controls and zonal shift. 

For more information, see Set up routing control components. |  November 21, 2024 |   
|  Zonal shift capability for Amazon EC2 Auto Scaling groups |  

ARC now supports zonal shift for Amazon EC2 Auto Scaling groups. 

For more information, see Support for Amazon EC2 Auto Scaling groups. |  November 18, 2024 |   
|  Zonal shift capability for Amazon EKS |  

You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to do it for you by enabling zonal autoshift. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. 

For more information, see Support for Amazon Elastic Kubernetes Service. |  October 22, 2024 |   
|  Zonal shift capability for Network Load Balancers |  

ARC now supports zonal shift for Network Load Balancers with cross-zone enabled or cross-zone disabled configurations. 

For more information, see Support for Network Load Balancers. |  October 11, 2024 |   
|  Autoshift observer notifications |  

With autoshift observer notifications, you can configure zonal autoshift to notify you, through Amazon EventBridge, whenever AWS starts an autoshift to shift traffic away from a potentially impaired Availability Zone. You do not have to configure any specific resources with zonal autoshift to enable these separate notifications. 

For more information, see Using zonal autoshift with Amazon EventBridge. |  July 12, 2024 |   
|  Doc reorganization by each capability |  

Reorganizes the developer guide content to be siloed into sub-dev guides. That is, there are now separate sections that contain comprehensive information for each capability in ARC: zonal shift and zonal autoshift for multi-AZ recovery, and routing control and readiness check for multi-Region recovery. 

For more information, see What is Amazon Application Recovery Controller (ARC). |  April 30, 2024 |   
|  Adds zonal autoshift capability |  

Adds a new capability in ARC where you authorize AWS to shift away resource traffic for an application from an Availability Zone, on your behalf, to help reduce time to recovery during events. 

For more information, see Zonal autoshift in Amazon Application Recovery Controller (ARC). |  November 30, 2023 |   
|  Adds new service-linked role |  

Adds a new service-linked role, AWSServiceRoleForZonalAutoshiftPracticeRun, for zonal autoshift practice runs. 

For more information, see Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun. |  November 30, 2023 |   
|  Adds cross-account support for clusters |  

Adds cross-account support for clusters in ARC with AWS Resource Access Manager, so that you can easily and securely use one cluster to host control panels and routing controls owned by several different AWS accounts. 

For more information, see Support cross-account for clusters in ARC. |  October 18, 2023 |   
|  Updates a managed policy |  

Updates the `AmazonRoute53RecoveryControlConfigReadOnly` managed policy to add permissions for `GetResourcePolicy`, to support returning details about AWS Resource Access Manager resource policies for shared resources. 

For more information, see AWS managed policies. |  September 19, 2023 |   
|  Updated service-linked role |  

Added new permissions, `ec2:DescribeVpnGateways` and `ec2:DescribeCustomerGateways`, to the service-linked role for ARC, to support polling Amazon EC2 instances. 

For more information, see Using service-linked roles for ARC. |  February 17, 2023 |   
|  GA release for zonal shift |  

Supports the GA release of zonal shift for ARC, which includes attribute-based access control (ABAC) for managed resources that are registered in ARC for zonal shift. 

For more information, see Attribute-based access control (ABAC) with ARC. |  January 10, 2023 |   
|  Added new multi-AZ zonal shift |  

Added content describing a new service in ARC, zonal shift, for multi-AZ applications. You can start a zonal shift to temporarily move traffic for a load balancer resource away from an Availability Zone. 

For more information, see Zonal shift in ARC. |  November 28, 2022 |   
|  Updated service-linked role |  

Added a new permission, `lambda:ListProvisionedConcurrencyConfigs`, to the service-linked role for ARC to query information about Lambda functions. 

For more information, see Using service-linked roles for ARC. |  August 31, 2022 |   
|  Updated managed policy |  

Updated the `AmazonRoute53RecoveryControlConfigFullAccess` managed policy to remove Amazon Route 53 permissions and list them as optional. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC). |  May 26, 2022 |   
|  Updated managed policy |  

Updated the `AmazonRoute53RecoveryControlConfigFullAccess` managed policy to include required Amazon Route 53 permissions. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC). |  April 15, 2022 |   
|  Added CLI example for the new list routing controls API |  

Added example CLI command and best practices recommendations for the new list routing controls API operation included in the extremely reliable ARC data plane API. 

For more information, see List and update routing controls and states. |  March 31, 2022 |   
|  Added support for overriding safety rules |  

Added support for overriding safety rules, which allows you to bypass routing control safeguards that are enforced with safety rules that you've configured. Safety rule overrides could be required, for example, in a "break glass" scenario during failover for disaster recovery. 

For more information, see Override safety rules to reroute traffic. |  March 2, 2022 |   
|  Added additional tagging support |  

Added support for tagging additional resources in ARC, including clusters, control panels, routing controls, and safety rules. 

For more information, see Tagging in Amazon Application Recovery Controller (ARC). |  December 20, 2021 |   
|  Updated managed policy |  

Updated the `AmazonRoute53RecoveryControlConfigReadOnly` managed policy to add permission to list tags for a resource. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC) |  December 20, 2021 |   
|  Added support for real-time alerts with EventBridge |  

Added support for EventBridge, which means that now you can add rules to get alerts and act on ARC readiness check status changes, for example, when a status changes from READY to NOT READY. 

For more information, see Using ARC with Amazon EventBridge. |  December 20, 2021 |   
|  Added routing control state code samples |  

Added code samples to illustrate trying cluster endpoints in sequence when you use API operations to get or update routing control states. 

For more information, see API examples for Amazon Application Recovery Controller (ARC). |  November 16, 2021 |   
|  Added new permissions to a read-only policy |  

Added two new permissions to the policy `AmazonRoute53RecoveryReadinessReadOnlyAccess`: `route53-recovery-readiness:GetArchitectureRecommendations` and `route53-recovery-readiness:GetCellReadinessSummary`. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC). |  November 9, 2021 |   
|  Added support for Amazon API Gateway resource type |  

Added a new resource type, Amazon API Gateway, and updated the ARC service-linked role permissions so that ARC can audit API Gateway with readiness checks. 

For more information, see  Readiness rules and supported resource types and  Using service-linked roles for ARC. |  October 28, 2021 |   
|  Added support for Lambda functions resource type |  

Added a new resource type, Lambda functions, and updated the ARC service-linked role permissions so that ARC can audit Lambda functions with readiness checks. 

For more information, see  Readiness rules and supported resource types and  Using service-linked roles for ARC. |  October 8, 2021 |   
|  Added links to CloudFormation and Terraform templates |  

Added links to downloadable CloudFormation and Hashicorp Terraform templates to help you quickly get started with using ARC.For more information, see Recovery readiness with a new application.  |  September 13, 2021 |   
|  Added new managed policies |  

Added the following AWS managed policies for ARC: `AmazonRoute53RecoveryReadinessFullAccess`, `AmazonRoute53RecoveryReadinessReadOnlyAccess`, `AmazonRoute53RecoveryClusterFullAccess`, `AmazonRoute53RecoveryClusterReadOnlyAccess`, `AmazonRoute53RecoveryControlConfigFullAccess`, and `AmazonRoute53RecoveryControlConfigReadOnlyAccess`. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC). |  August 18, 2021 |   
|  Started tracking AWS managed policies for Amazon Application Recovery Controller (ARC) |  

Updates for managed policies will be tracked from the initial release date forward. 

For more information, see AWS managed policies for Amazon Application Recovery Controller (ARC). |  July 27, 2021 |   
|  Initial release of Amazon Application Recovery Controller (ARC) |  ARC improves application availability by centrally coordinating failovers within an AWS Region or across multiple Regions. ARC provides readiness checks to ensure that your applications are scaled to handle failover traffic and configured to route around failures. It also provides extremely reliable routing control so that you can recover applications by rerouting traffic, for example, across Availability Zones or Regions. For more information, see  What is ARC?. |  July 27, 2021 |
