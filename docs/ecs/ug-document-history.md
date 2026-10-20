> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
> Downloaded: 2026-10-20

# Document history

The following table describes the major updates and new features for the Amazon Elastic Container Service Developer Guide. We also update the documentation frequently to address the feedback that you send us. 
|   

Change  |   

Description  |   

Date  |    
|   

Add permissions to AmazonECS_FullAccess managed policy.  |   

The `AmazonECS_FullAccess` managed IAM policy was updated to include the `cloudformation:TagResource` and `cloudformation:UntagResource` permissions. These permissions allow tags to be added to CloudFormation stacks when a stack is created or updated.  |  September 2, 2026 |   
|   

Add permissions to AmazonECSServiceRolePolicy managed policy.  |   

The `AmazonECSServiceRolePolicy` managed IAM policy was updated to include the `autoscaling:TerminateInstanceInAutoScalingGroup` permission. This permission allows Amazon ECS to terminate Amazon EC2 instances in customer ASGs that fail to register with the Amazon ECS cluster.  |  April 24, 2026 |   
|   

Update permissions to `AmazonECSInfrastructureRolePolicyForManagedInstances`.  |   

The permissions were updated to maintain consistency of the EC2 service name across partitions. This update does not change the existing permission model or grant additional access.  |  February 26, 2026 |   
|   

 Update permissions to `AmazonECSInfrastructureRolePolicyForManagedInstances`.   |   

The `AmazonECSInfrastructureRolePolicyForManagedInstances` policy has been updated to support Capacity Reservations on Amazon ECS Managed Instances by adding the following permissions:  
`resource-groups:ListGroupResources` permission has been added to allow Amazon ECS to fetch a grouping of capacity reservations. To run this command, the following permissions are also required: `cloudformation:DescribeStacks`, `cloudformation:ListStackResources`, `tag:GetResources`  
`ec2:DescribeCapacityReservations` permission has been added to allow Amazon ECS to gather details about capacity reservations necessary to integrate with Amazon ECS Managed Instances. 
`ec2:RunInstances` permission has been modified to include Amazon ResourceGroups group resources for Amazon ECS to provision targeted Amazon EC2 capacity reservations. 
  |  February 24, 2026 |   
|   

Add permissions to AmazonECSServiceRolePolicy managed policy.  |   

The `AmazonECSServiceRolePolicy` managed IAM policy was updated to include the `ssmmessages:OpenDataChannel` permission. This permission allows Amazon ECS to open data channels for ECS Exec sessions.  |  January 20, 2026 |   
|   

 Update permissions to `AmazonECSInfrastructureRolePolicyForManagedInstances`.   |   

The `AmazonECSInfrastructureRolePolicyForManagedInstances` policy has been updated to modify the `CreateFleet` permissions. The resource-based conditions for subnets, security groups and EC2 images have been removed because:  
Subnets and security groups are not created or managed by Amazon ECS, so they do not contain the required `AmazonECSManaged` tags. 
While Amazon ECS owns and manages EC2 images, the tags are not visible to customers, preventing the application of resource-based policies. 

 This change ensures that the policy functions correctly with resources that lack the expected ECS management tags.   |  December 15, 2025 |   
|   

Correct managed instances lifetime policy  |   

Updated managed instances documentation to clarify instance lifetime terminology and extend maximum instance lifetime from 14 days to 21 days.  |  December 11, 2025 |   
|   

Add permissions to AmazonECSServiceRolePolicy managed policy.  |   

The `AmazonECSServiceRolePolicy` managed IAM policy was updated to include the `ec2:DescribeInstanceEventWindows` permission. This permission allows Amazon ECS to fetch Amazon EC2 Event Windows for services and clusters associated with Event Windows.  |  November 20, 2025 |   
|   

Add permissions to `AmazonECSServiceRolePolicy`.  |  The `AmazonECSServiceRolePolicy` was updated to include the `ec2:AssociateTrunkInterface` and `ec2:DisassociateTrunkInterface` permissions to enable Amazon ECSto provision and de-provision the Task ENI. |  November 14, 2025 |   
|   

Update AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity policy  |   

Updated AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity policy to allow Amazon ECS to monitor lifecycle of Amazon ECS created secrets.  |   

November 13, 2025  |   
|   

Amazon ECS canary deployments  |  Amazon ECS canary deployments enable you to test new application versions by routing a small percentage of traffic to the new version while maintaining the majority on the stable version. For more information, see Amazon ECS canary deployments. |  October 28, 2025 |   
|   

Amazon ECS linear deployments  |  Amazon ECS linear deployments enable you to gradually shift traffic from the current service revision to a new revision in equal percentage increments, providing controlled deployment with monitoring at each step. For more information, see Amazon ECS linear deployments. |  October 28, 2025 |   
|   

Amazon ECS Managed Instances Regions  |  Amazon ECS Managed Instances is now available in additional Regions. For more information, see Architect for Amazon ECS Managed Instances. |  October 27, 2025 |   
|   

AWS for Fluent Bit version 3.0.0  |  AWS for Fluent Bit version `3.0.0` is now available, based on Fluent Bit version `4.1.1` and AL2023. For more information, see AWS for Fluent Bit image repositories for Amazon ECS. |  October 14, 2025 |   
|   

FireLens container non-root user support  |  Amazon ECS supports running the FireLens container as a non-root user. For more information, see Send Amazon ECS logs to an AWS service or AWS Partner. |  October 13, 2025 |   
|   

Amazon ECS event capture in the console  |  The Amazon ECS console provides event capture functionality that stores Amazon ECS-generated events, such as service actions and task state changes, to CloudWatch Logs through EventBridge. For more information, see Task lifecycle events. |  October 2, 2025 |   
|   

Amazon ECS supports Amazon ECS Managed Instances for running containerized workloads  |  Amazon ECS supports Amazon ECS Managed Instances for running containerized workloads. For more information, see Amazon ECS Amazon ECS Managed Instances. |  September 30, 2025 |   
|   

Add new AmazonECSInstanceRolePolicyForManagedInstances  |  Added new AmazonECSInstanceRolePolicyForManagedInstances policy that provides permissions for Amazon ECS managed instances to register with Amazon ECS clusters. |  September 30, 2025 |   
|   

Add new AmazonECSInfrastructureRolePolicyForManagedInstances  |  Added new AmazonECSInfrastructureRolePolicyForManagedInstances policy that provides Amazon ECS access to create and manage Amazon EC2 managed resources. |  September 30, 2025 |   
|   

Support for running Amazon ECS workloads in an IPv6-only configuration  |   

Amazon ECS workloads can now be run in an IPv6-only configuration that allows tasks to communicate exclusively over IPv6. For more information, see Amazon ECS task networking options for the EC2 launch type and Amazon ECS task networking options for the Fargate launch type.  |  September 29, 2025 |   
|   

Support for Amazon ECS Service Connect using shared AWS Cloud Map namespaces  |   

Amazon ECS Service Connect now supports the use of shared AWS Cloud Map namespaces for cross-account service-to-service communication. For more information, see Amazon ECS Service Connect with shared AWS Cloud Map namespaces.  |  September 12, 2025 |   
|   

Amazon ECS enhances task definition editing in the AWS console with Amazon Q  |   

For more information, see Using Amazon Qto provide task definition recommendations in the Amazon ECS console  |  September 10, 2025 |   
|  

Support for running ECS Exec commands from the console |   

You can now run ECS Exec commands directly from the Amazon ECS console. For more information, see Running ECS Exec commands from the console.  |  September 4, 2025 |   
|   

Add new AmazonECSInfrastructureRolePolicyForManagedInstances  |  Added new AmazonECSInfrastructureRolePolicyForManagedInstances policy that provides Amazon ECS access to create and manage Amazon EC2 managed resources. |  August 31, 2025 |   
|   

Add permissions to AmazonEC2ContainerServiceforEC2Role managed policy.  |   

The `AmazonEC2ContainerServiceforEC2Role` managed IAM policy was updated to include the `ecs:ListTagsForResource` permission. This permission allows the Amazon ECS agent to retrieve task and container instance tags through the task metadata endpoint (`${ECS_CONTAINER_METADATA_URI_V4}/taskWithTags`). For more information, see AmazonEC2ContainerServiceforEC2Role.  |  August 4, 2025 |   
|   

Add permissions to AmazonECSInfrastructureRolePolicyForLoadBalancers.  |   

The `AmazonECSInfrastructureRolePolicyForLoadBalancers` managed IAM policy was updated with new permissions for describing, deregistering and registering target groups.  |  July 25, 2025 |   
|   

Support for updating a service deployment controller  |   

Amazon ECS supports updating a service deployment controller, allowing you to change between different deployment types for an existing service. For more information, see Update Amazon ECS service parameters.  |  July 15, 2025 |   
|   

Amazon ECS native blue/green deployments  |   

Amazon ECS supports native blue/green deployments, allowing you to validate new service revisions before directing production traffic to them. For more information, see Amazon ECS blue/green deployments.  |  July 15, 2025 |   
|   

Add new AmazonECSInfrastructureRolePolicyForLoadBalancers managed policy.  |   

This policy provides access to other AWS service resources required to manage load balancers associated with Amazon ECS workloads on your behalf. For more information, see AmazonECSInfrastructureRolePolicyForLoadBalancers.  |  July 15, 2025 |   
|   

SOCI index manifest v2 support  |   

Fargate customers looking to use SOCI will only be able to use the SOCI index manifest v2. Existing customers that have previously used SOCI on Fargate can continue to use the SOCI index manifest v1, however we strongly advise those customers migrate to SOCI index manifest v2. For more information, see Lazy loading container images using Seekable OCI (SOCI).  |  July 2, 2025 |   
|   

Added the task ID in service action events generated due to health failures.  |   

For more information, see Amazon ECS service unhealthy event messages.  |  June 30, 2025 |   
|   

Update to default log driver mode.  |   

The default logging mode for Amazon ECS has been updated from `blocking` to `non-blocking`. You can override this default mode by specifying a `mode` in your container definition's `logConfiguration` or configure your own default by setting the `defaultLogDriverMode` account setting using the Amazon ECS console or the AWS CLI. For more information, see Default log driver mode.  |  June 25, 2025 |   
|   

Add permissions to AmazonECSServiceRolePolicy.  |   

The `AmazonECSServiceRolePolicy` managed IAM policy was updated with new AWS Cloud Map permissions which Amazon ECS can update AWS Cloud Map service attributes for services that Amazon ECS manages.  |  June 24, 2025 |   
|   

Support for the Amazon ECS-optimized Windows Server 2025 Full AMI and Amazon ECS-optimized Windows Server 2025 Core AMI.  |   

For more information, see Amazon ECS-optimized Windows AMIs.  |  June 20, 2025 |   
|   

Support for updating a service capacity provider strategy.  |   

You can now update a service capacity provider strategy. For more information, see Update service parameters.  |  June 12, 2025 |   
|   

Add permissions to AmazonECSInfrastructureRolePolicyForVolumes  |  The `AmazonECSInfrastructureRolePolicyForVolumes` policy has been updated to add the `ec2:DescribeInstances` permission. The permission helps prevent device name collision for Amazon EBS volumes that are attached to Amazon ECS tasks that run on the same container instance. |  June 2, 2025 |   
|   

Support for volume initialization rate for Amazon EBS volumes attached to Amazon ECS tasks.  |  You can now set a `volumeIntiializationRate` to determine the rate, in MiB/s, at which data is fetched from a snapshot of an existing Amazon EBS volume to create new volumes for attachment to Amazon ECS tasks. For more information, see volumeInitializationRate.  |  May 13, 2025 |   
|   

Support for stopping a service deployment.  |  You can now stop a service deployment. For more information, see Stopping Amazon ECS service deployments.  |  May 2, 2025 |   
|   

Support for Amazon ECS dual-stack endpoints.  |  You can now use dual-stack endpoints to interact with Amazon ECS. Dual-stack endpoints support requests to Amazon ECS over both Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). For more information, see Using Amazon ECS dual-stack endpoints.  |  April 30, 2025 |   
|   

Support for configuring a default log driver mode at the account level in an AWS Region.  |  You can now configure a default delivery mode of log messages from a container to the log driver that you specify in your `logConfiguration` using the `defaultLogDriverMode` account setting. For more information, see Default log driver mode.  |  April 17, 2025 |   
|   

Support for migrating a service with a short ARN format to the long ARN format.  |  You can now migrate a service with a short ARN format to the long ARN formatk packet. For more information, see  Migrate an Amazon ECS short service ARN to a long ARN.  |  February 13, 2025 |   
|   

Support for three types of fault injection on Amazon ECS and Fargate.  |  You can now use network blackhole port, network latency, and network packet loss fault injection with Amazon ECS and Fargate. For more information, see  Use AWS Fault Injection Service to test your Amazon ECS workloads.  |  December 19, 2024 |   
|   

Support for CloudWatch Container Insights with enhanced observability.  |  You can use CloudWatch Container Insights with enhanced observability. For more information, see  Monitor Amazon ECS containers using Container Insights with enhanced observability.  |  December 2, 2024 |   
|   

Support for predictive scaling.  |  You can use predictive scaling to anticipate future needs and proactively increase tasks in your service as needed. For more information, see  Use historical patterns to scale CloudWatch services with predictive scaling.  |  November 21, 2024 |   
|   

Support for service-rebalancing.  |   

You can now have Amazon ECS automatically balance your service tasks across Availability Zones. For more information, see Balancing an Amazon ECS service across Availability Zones.  |  November 19, 2024 |   
|   

Support for configuring resolution of container image tags to image digests.  |   

You can now configure the resolution of container image tags to digests for each container in tasks that are part of a service. For more information, see Container image resolution and versionConsistency.  |  November 19, 2024 |   
|   

Add new `AmazonECSInfrastructureRolePolicyForVpcLattice` IAM policy  |   The `AmazonECSInfrastructureRolePolicyForVpcLattice` policy provides access to other AWS service resources required to manage VPC Lattice feature in Amazon ECS workloads on your behalf.  |  November 18, 2024 |   
|   

VPC Lattice is now available for Amazon ECS services.  |   You can now use VPC Lattice to standardize your service-to-service connectivity, security, and observability. For more information, see Use Amazon VPC Lattice to connect, observe, and secure your Amazon ECS services.  |  November 18, 2024 |   
|   

Support for service history using service deployments and service revisions.  |  You can use service deployments and service revisions to view deployment history. For more information, see View service history using Amazon ECS service deployments and Amazon ECS service revisions.  |  October 30, 2024 |   
|   

Support for Amazon EBS volumes for the EC2 launch type using the Windows operating system.  |  Amazon ECS support Amazon EBS volumes attached to tasks running on EC2 instances with the Windows operating system. For more information, see Use Amazon EBS volumes with Amazon ECS.  |  October 24, 2024 |   
|   

Add permissions to AmazonECSInfrastructureRolePolicyForVolumes.  |   The `AmazonECSInfrastructureRolePolicyForVolumes` policy has been updated to allow customers to create an Amazon EBS volume from a snapshot. For more information, see AmazonECSInfrastructureRolePolicyForVolumes.  |  October 10, 2024 |   
|   

Fargate Spot is available for Linux ARM.  |   Support for Fargate Spot on Linux ARM was added to Amazon ECS.  |  September 6, 2024 |   
|   

Container restart policy for individual containers in Amazon ECS tasks.  |   You can enable restart policies for essential and non-essential containers defined in your task definition to overcome transient failures faster and maintain task availability. For more information, see Restart individual containers in Amazon ECS tasks with container restart policies.  |  August 15, 2024 |   
|   

Added permissions to AmazonECS_FullAccess  |   The `AmazonECS_FullAccess` policy was updated to add `iam:PassRole` permissions for IAM roles for a role named `ecsInfrastructureRole`. This is the default IAM role created by the AWS Management Console that is intended to be used as an ECS infrastructure role that allows Amazon ECS to manage Amazon EBS volumes attached to ECS tasks.  |  August 13, 2024 |   
|   

Amazon Linux 2023, CentOS Stream 9, Fedora 40, and Ubuntu 24 support added for ECS Anywhere  |   

Support for the Amazon Linux 2023, CentOS Stream 9, Fedora 40, and Ubuntu 24 operating systems was added to ECS Anywhere. For more information, see Supported operating systems and system architectures.  |   

July 23, 2024  |   
|   

Container image resolution for services that use the rolling update (ECS) deployment type.  |   

To ensure that all tasks in a service that uses the rolling update deployment controller use the same container image, Amazon ECS resolves container image names and any image tags specified in the task definition to container image digests. For more information, see Container image resolution.  |   

July 10, 2024  |   
|   

Debian 11 and Debian 12 support added for ECS Anywhere  |   

Support for the Debian 11 and Debian 12 operating systems was added to ECS Anywhere. For more information, see Supported operating systems and system architectures.  |   

March 28, 2024  |   
|   

gMSA for Linux Containers on Fargate support  |   

Amazon ECS supports Active Directory authentication for Linux containers on Fargate through a special kind of service account called a group Managed Service Account (gMSA). For more information, see Using gMSA for Linux containers on Fargate.  |   

March 5, 2024  |   
|   

CloudWatch metrics added for Amazon EBS volumes attached to tasks  |   

Amazon ECS now publishes CloudWatch metrics for the Amazon EBS storage utilization for tasks that have an Amazon EBS volume attached. For more information, see Amazon ECS CloudWatch metrics.  |   

February 8, 2024  |   
|   

Service Connect TLS  |   

You can now use TLS with Service Connect.  |   

January 22, 2024  |   
|   

Service Connect TLS managed policy  |   

Added new AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity policy.  |   

January 22, 2024  |   
|   

Service Connect timeout configuration update  |   

Service Connect timeout configuration can now be updated and includes two optional parameters - `idleTimeout` and `perRequestTimeout`.  |   

January 22, 2024  |   
|   

Amazon ECS managed instance draining  |  You can use Amazon ECS managed instance draining to facilitate graceful termination of Amazon ECS instances. |  January 19, 2024 |   
|   

Ubuntu 22 support added for ECS Anywhere  |  Support for the Ubuntu 22 operating system was added to ECS Anywhere. For more information, see Supported operating systems and system architectures. |  January 16, 2024 |   
|   

Add `AmazonECSInfrastructureRolePolicyForVolumes` IAM policy  |   

The `AmazonECSInfrastructureolePolicyForVolumes` was added. The policy grants the permissions that are needed by Amazon ECS to make AWS API calls to manage Amazon EBS volumes associated with Amazon ECS workloads.  |   

January 11, 2024  |   
|   

Amazon EBS data volume for Amazon ECS task  |   

You can configure 1 Amazon EBS data volume per task during deployment for attachment to standalone Amazon ECS tasks or tasks managed by an ECS service. Configuring a volume at deployment allows you to create resuable task definitions not constrained to specific volume types or settings. Amazon EBS volumes provide a highly available, cost-effective, durable, high-performance block storage for data intensive containerized workloads.  |   

January 11, 2024  |   
|   

Amazon ECS classic console reached end of life  |  The Amazon ECS console has reached the end of life. |  December 4, 2023 |   
|   

Updated policy  |  The AmazonECSServiceRolePolicy managed IAM policy was updated with new `events` permissions and additional `autoscaling` and `autoscaling-plans` permissions. |  December 4, 2023 |   
|   

Runtime Monitoring support  |   

You can use Runtime Monitoring to monitor your Amazon ECS workloads to identify malicious or unauthorized behavior. For more information, see Runtime Monitoring.  |   

November 26, 2023  |   
|   

Updated policy  |   

The `AmazonECSServiceRolePolicy` managed IAM policy was updated to allow access to the AWS Cloud Map `DiscoverInstancesRevision` API.  |   

October 4, 2023  |   
|   

AWS Fargate task retirement configuration  |   

You can configure the wait period before Fargate tasks are retired For more information, see AWS Fargate task maintenance.  |   

September 5, 2023  |   
|   

Additional task definition parameters in AWS Fargate  |   

AWS Fargate adds support for `pidMode` and `systemControls` in Linux platform version `1.4.0`. For more information, see Task definitions.  |   

August 9, 2023  |   
|   

Amazon ECS console task definition page redesign  |   

The task definition page in the Amazon ECS console has been redesigned and contains additional options. For more information, see Creating a task definition using the console.  |   

 July 26, 2023  |   
|   

Fargate supports lazy loading with Seekable OCI indexes  |   

AWS Fargate is introducing Seekable OCI (SOCI) indexes. With SOCI, containers only spend a few seconds on the image pull before they can start, providing time for environment setup and application instantiation while the image is downloaded in the background. For more information, see Lazy loading container images using Seekable OCI (SOCI).  |   

 July 17, 2023  |   
|   

Improved support for gMSA on Linux and Windows  |   

The task definition has a new `credentialSpecs` field for gMSA for Linux and Windows. A new complete tutorial for domainless gMSA on Windows has been added, see Tutorial: Using Windows Containers with Domainless gMSA using the AWS CLI. For more information, see Using gMSAs for Linux Containers and Using gMSAs for Windows Containers.  |   

 July 14, 2023  |   
|   

Improved ECS Agent versions documentation  |   

The documentation for the Amazon ECS Agent versions has been updated. We recommend that you use the `v20.10.13` version or newer of Docker with the latest version of the Amazon ECS container agent. The released versions and changes to the agent are available on GitHub. For more information, see Amazon ECS Linux container agent versions.  |   

 June 20, 2023  |   
|   

Updated Region availability for Fargate ARM64 support  |   

The Region availability for Fargate ARM64 support has been updated. For more information, see Considerations.  |   

 June 19, 2023  |   
|   

Improve cluster auto scaling documentation  |   

The documentation for Amazon ECS scaling of Amazon EC2 Auto Scaling has significant improvements in accuracy and readability. For more information, see Amazon ECS cluster auto scaling.  |   

 May 4, 2023  |   
|   

Tagging authorization for resource creation.  |   

Users must have permissions for actions that create the resource, such as `ecsCreateCluster`. When you create a resource and specify tags for that resource, AWS performs additional authorization to verify that there are permissions to create tags. For more information, see Tagging authorization and Grant permission to tag resources on creation.  |   

 April 18, 2023  |   
|   

Support for gMSA for Linux containers on EC2  |   

You can use gMSA to authenticate to Active Directory for Linux containers on EC2. For more information, see Using gMSAs for Linux Containers.  |   

April 14, 2023  |   
|   

Support for ephemeral storage for Windows containers on AWS Fargate  |   

You can use ephemeral storage for Windows containers on AWS Fargate. For more information, see Fargate task storage.  |   

April 14, 2023  |   
|  

AWS Cost Management support for task-level CUR data |   

You can turn on task-level cost and resource usage in the Cost and Usage Reports. This adds Split Cost Allocation Data for tasks that run on AWS Fargate and EC2. For more information, see Task-level Cost and Usage Reports.  |   

 April 12, 2023  |   
|   

Amazon Linux 2023 Amazon ECS-optimized AMI  |   

You can deploy workloads on the Amazon Linux 2023 Amazon ECS-optimized AMI. For more information, see Amazon ECS-optimized Linux AMIs.  |   

April 10, 2023  |   
|   

AWS Fargate Federal Information Processing Standard (FIPS) 140  |   

You can deploy workloads on Amazon ECS on AWS Fargate in a manner compliant with Federal Information Processing Standard (FIPS) 140. For more information, see AWS Fargate Federal Information Processing Standard (FIPS-140).  |   

April 10, 2023  |   
|   

Task definition deletion  |   

You can delete a task definition using the Amazon ECS console, SDK, and AWS CLI. For more information, see Deleting a task definition revision using the console and Task definitions.  |   

 February 24, 2023  |   
|   

AWS Fargate service recommendations in Compute Optimizer  |   

AWS Compute Optimizer generates task and container size recommendations based on the utilization of running tasks in Amazon ECS services on AWS Fargate. For more information, see Viewing recommendations for Amazon ECS services on Fargate.  |   

January 27, 2023  |   
|   

Amazon ECS console  |   

The new Amazon ECS console is now the default console. For more information, see New Amazon ECS console.  |   

 January 19, 2023  |   
|   

Updated `AmazonECS_FullAccess` IAM policy  |   

The `AmazonECS_FullAccess` IAM policy is updated to include permissions to add tags to load balancers during creation. For more information, see AmazonECS_FullAccess.  |   

January 4, 2023  |   
|   

Use CloudWatch alarms to detect Amazon ECS service deployment failures  |   

You can configure Amazon ECS to set the deployment to failed when it detects that a specified CloudWatch alarm has gone into the ALARM state. For more information, see Deploy Amazon ECS services by replacing tasks.  |   

December 19, 2022  |   
|   

Support for container port mapping  |   

You can set a port number range on the container that's bound to the dynamically mapped host port range. For more information, see Port mappings.  |   

 December 15, 2022  |   
|   

General availability of Amazon ECS Service Connect  |   

This feature adds service discovery and service mesh that is controlled by Amazon ECS service deployments. For more information, see Use Service Connect to connect Amazon ECS services with short names.  |   

November 27, 2022  |   
|   

The new Amazon ECS console experience for task definitions is updated  |   

The new Amazon ECS console experience now contains a JSON editor for task defintions. For more information, see Creating an Amazon ECS task definition using the console.  |   

 October 27, 2022  |   
|   

The new Amazon ECS console experience for task definitions is updated  |   

The new Amazon ECS console experience now contains a JSON editor for task defintions. For more information, see Creating an Amazon ECS task definition using the console.  |   

October 27, 2022  |   
|   

The new Amazon ECS console experience is updated  |   

The new Amazon ECS console experience has been updated with additional service and task parameters. For more information, see Creating an Amazon ECS rolling update deployment and Running an application as an Amazon ECS task.  |   

October 7, 2022  |   
|   

New information in task metadata endpoint version 4  |   

The task metadata endpoint version 4 now invludes the VPC ID and the service name. For more information, see Amazon ECS task metadata endpoint version 4.  |   

October 7, 2022  |   
|   

New task definition sizes  |   

Amazon ECS on Fargate now supports the 8 vCPU and 16 vCPU task sizes. For more information, see Task size.  |   

 September 16, 2022  |   
|   

ECS CLI pages archived  |   

The ECS CLI documentation has been archived. We recommend using AWS Copilot for your command line tool needs. For more information, see Creating Amazon ECS resources using the AWS Copilot command line interface.  |   

September 15, 2022  |   
|   

New Fargate quotas  |   

Fargate is transitioning from task count-based quotas to vCPU-based quotas. For more information, see Amazon ECS endpoints and quotas.  |   

 September 8, 2022  |   
|   

Support for Amazon EC2 Auto Scaling warm pools.  |   

You can now use Amazon EC2 Auto Scaling warm pools to scale out your applications faster and save costs. For more information, see Configuring pre-initialized instances for your Amazon ECS Auto Scaling group.  |   

 March 23, 2022  |   
|   

Support for Windows instances in ECS Anywhere.  |   

ECS Anywhere now supports Windows instances. For more information, see Amazon ECS clusters for external instances.  |   

March 3, 2022  |   
|   

Added ECS Exec support for external instances  |   

ECS Exec is now supported for external instances. For more information, see Monitor Amazon ECS containers with ECS Exec.  |   

January 24, 2022  |   
|   

The new Amazon ECS console experience updated  |   

The new Amazon ECS console experience supports creating and deleting a cluster, updating a task definition, and deregistering a task definition. For more information, see Creating an Amazon ECS cluster for Fargate workloads, Deleting an Amazon ECS cluster, Updating an Amazon ECS task definition using the console, and Deregistering an Amazon ECS task definition revision using the console.  |   

December 8, 2021  |   
|   

The new Amazon ECS console experience updated  |   

The new Amazon ECS console experience supports creating a task definition. For more information, see Creating an Amazon ECS task definition using the console.  |   

 November 23, 2021  |   
|   

Amazon ECS supports the 64-bit ARM architecture for Linux.  |   

Amazon ECS supports the 64-bit ARM CPU architecture for the Linux operating system. For more information, see Amazon ECS task definitions for 64-bit ARM workloads.  |   

November 23, 2021  |   
|   

Amazon ECS support for the fluentd log-driver-buffer-limit option  |   

Amazon ECS supports the fluentd `log-driver-buffer-limit` option. For more information, see Send Amazon ECS logs to an AWS service or AWS Partner.  |   

November 22, 2021  |   
|   

Amazon ECS-optimized Linux AMI build script  |   

Amazon ECS has open-sourced the build scripts that are used to build the Linux variants of the Amazon ECS-optimized AMI. For more information, see Amazon ECS-optimized Linux AMI build script.  |   

 November 19, 2021  |   
|   

Container instance health  |   

Amazon ECS adds support for container instance health monitoring. For more information, see Monitor Amazon ECS container instance health.  |   

 November 10, 2021  |   
|   

Support for Windows Amazon ECS Exec  |   

Amazon ECS Exec supports Windows. For more information, see Monitor Amazon ECS containers with ECS Exec.  |   

November 1, 2021  |   
|   

Support for Windows containers on Fargate.  |   

Amazon ECS supports Windows containers on Fargate. For more information, see Fargate Windows platform version change log.  |   

October 28, 2021  |   
|   

GPU support for external instances on Amazon ECS Anywhere  |   

Amazon ECS supports specifying GPU requirements in the task definition for tasks run on external instances. For more information, see Amazon ECS task definitions for GPU workloads and Registering an external instance to an Amazon ECS cluster.  |   

October 8, 2021  |   
|   

Support of `awsvpc` network mode on Windows  |   

Amazon ECS supports `awsvpc` network mode on Windows. For more information, see Allocate a network interface for an Amazon ECS task.  |   

July 15, 2021  |   
|   

General availability of Bottlerocket  |   

Amazon ECS supports an Amazon ECS-optimized AMI variant of the Bottlerocket operating system is available as an AMI. For more information, see Amazon ECS-optimized Bottlerocket AMIs.  |   

June 30, 2021  |   
|   

Amazon ECS scheduled tasks update  |   

Amazon EventBridge added support for additional parameters when creating rules that trigger Amazon ECS scheduled tasks.   |   

June 25, 2021  |   
|   

AWS managed policies for Amazon ECS  |   

Amazon ECS added documentation of AWS managed policies for service-linked roles. For more information, see AWS managed policies for Amazon Elastic Container Service.  |   

 June 8, 2021  |   
|   

Getting started with the AWS CDK  |   

Added a getting started guide for using the AWS CDK with Amazon ECS. For more information, see Creating Amazon ECS resources using the AWS CDK.  |   

May 27, 2021  |   
|   

Amazon ECS Anywhere  |   

Amazon ECS has added support for registering an on-premise server or virtual machine (VM) with your cluster. For more information, see Amazon ECS clusters for external instances.  |   

May 25, 2021  |   
|   

Amazon ECS-optimized Windows Server 20H2 Core AMI  |   

Amazon ECS has added support for a new Windows Amazon ECS-optimized AMI variant for Windows Server 20H2 Core. For more information, see Amazon ECS-optimized Linux AMIs.  |   

April 19, 2021  |   
|   

Amazon ECS Exec  |   

Amazon ECS has released a new debugging tool called ECS Exec. For more information, see Monitor Amazon ECS containers with ECS Exec.  |   

March 15, 2021  |   
|   

VPC endpoint policy support  |   

Amazon ECS now supports VPC endpoint policies. For more information, see Creating a VPC endpoint policy for Amazon ECS.  |   

January 11, 2021  |   
|   

New console experience  |   

Amazon ECS has released a new console experience which supports creating or updating a service or running a standalone task. For more information, see Creating an Amazon ECS rolling update deployment and Running an application as an Amazon ECS task.  |   

 December 28, 2020  |   
|   

Capacity provider update  |   

Amazon ECS added support for updating an existing Auto Scaling group capacity provider.   |   

November 23, 2020  |   
|   

ECS now supporting Amazon FSx for Windows File Server for Windows tasks  |   

Amazon ECS added support for specifying Amazon FSx for Windows File Server volumes in Windows task definitions. For more information, see Use FSx for Windows File Server volumes with Amazon ECS.  |   

November 11, 2020  |   
|   

VPC dual-stack mode support added  |   

Amazon ECS added support for using a VPC in dual-stack mode with tasks using the `awsvpc` network mode, which provides support for IPv6 addresses. For more information, see Using a VPC in dual-stack mode.  |   

November 5, 2020  |   
|   

Task metadata endpoint v4 update  |   

Amazon ECS added additional metadata to the task metadata endpoint v4 output. For more information, see Amazon ECS task metadata endpoint version 4.  |   

 November 5, 2020  |   
|   

Support for Local Zones and Wavelength Zones  |   

Amazon ECS added support for workloads in Local Zones and Wavelength Zones. For more information, see Amazon ECS applications in shared subnets, Local Zones, and Wavelength Zones.  |   

 September 4, 2020  |   
|   

Amazon ECS variant of Bottlerocket AMI  |   

Bottlerocket is a Linux-based open source operating system that is purpose-built by AWS for running containers. An Amazon ECS-optimized AMI variant of the Bottlerocket operating system is available as an AMI you can use when launching Amazon ECS container instances. For more information, see Amazon ECS-optimized Bottlerocket AMIs.  |   

 August 31, 2020  |   
|   

Task metadata endpoint version 4 updated for network rate stats  |   

The task metadata endpoint version 4 has been updated to provide network rate stats for Amazon ECS tasks that use the `awsvpc` or `bridge` network modes hosted on Amazon EC2 instances running at least version `1.43.0` of the container agent. For more information, see Amazon ECS task metadata endpoint version 4.  |   

August 10, 2020  |   
|   

Fargate usage metrics  |   

AWS Fargate provides CloudWatch usage metrics which provide visibility into your accounts usage of Fargate On-Demand and Fargate Spot resources. For more information, see Usage metrics.  |   

August 3, 2020  |   
|   

AWS Copilot version 0.1.0  |   

The new AWS Copilot CLI launched, providing high-level commands to simplify modeling, creating, releasing, and managing containerized applications on Amazon ECS from a local development environment. For more information, see Creating Amazon ECS resources using the AWS Copilot command line interface.  |   

July 9, 2020  |   
|   

AWS Fargate platform versions deprecation schedule  |   

The Fargate platform version deprecation schedule has been added. For more information, see AWS Fargate Linux platform version deprecation.  |   

July 8, 2020  |   
|   

AWS Fargate Region expansion  |   

Amazon ECS on AWS Fargate has expanded to the Europe (Milan) Region.  |   

June 25, 2020  |   
|   

Amazon ECS optimized Amazon Linux 2 (Neuron) AMI released  |   

Amazon ECS released an Amazon ECS optimized Amazon Linux 2 (Neuron) AMI for inferential workloads. 

For more information, see Amazon ECS-optimized Linux AMIs.  |   

June 24, 2020  |   
|   

Added support for deleting capacity providers  |   

Amazon ECS added support for deleting Auto Scaling group capacity providers.  |   

June 11, 2020  |   
|   

AWS Fargate platform version 1.4.0 update  |   

Beginning on May 28, 2020, any new Fargate task that is launched using platform version 1.4.0 will have its 20 GB ephemeral storage encrypted with an AES-256 encryption algorithm using an AWS Fargate-managed encryption key. For more information, see Fargate task ephemeral storage for Amazon ECS.  |   

May 28, 2020  |   
|   

Environment variable file support  |   

Added support for specifying environment variable files in a task definition, which enables you to bulk add environment variables to your containers. For more information, see Pass an individual environment variable to an Amazon ECS container.  |   

May 18, 2020  |   
|   

AWS Fargate Region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Africa (Cape Town) Region.  |   

May 11, 2020  |   
|   

Service quota updated  |   

The following service quota was updated:  
Clusters per account was raised from `2,000` to `10,000`. 
 

For more information, see Amazon ECS endpoints and quotas.  |   

April 17, 2020  |   
|   

AWS Fargate platform version 1.4.0  |   

AWS Fargate platform version 1.4.0 is released, which contains the following features:  
Added support for using Amazon EFS file system volumes for persistent task storage. For more information, see Use Amazon EFS volumes with Amazon ECS. 
The ephemeral task storage has been increased to 20 GB. For more information, see Fargate task ephemeral storage for Amazon ECS. 
The network traffic behavior to and from tasks has been updated. Starting with platform version 1.4, all Fargate tasks receive a single elastic network interface (referred to as the task ENI) and all network traffic flows through that ENI within your VPC and will be visible to you through your VPC flow logs. For more information, see Amazon ECS task networking options for the Fargate launch type. 
Task ENIs add support for jumbo frames. Network interfaces are configured with a maximum transmission unit (MTU), which is the size of the largest payload that fits within a single frame. The larger the MTU, the more application payload can fit within a single frame, which reduces per-frame overhead and increases efficiency. Supporting jumbo frames will reduce overhead when the network path between your task and the destination supports jumbo frames, such as all traffic that remains within your VPC. 
CloudWatch Container Insights will include network performance metrics for Fargate tasks. For more information, see Monitor Amazon ECS containers using Container Insights with enhanced observability. 
Added support for the task metadata endpoint v4 which provides additional information for your Fargate tasks, including network stats for the task and which Availability Zone the task is running in. For more information, see Amazon ECS task metadata endpoint version 4. 
Added support for the `SYS_PTRACE` Linux parameter in container definitions. For more information, see Linux parameters. 
The Fargate container agent replaces the use of the Amazon ECS container agent for all Fargate tasks. This change should not have an effect on how your tasks run. 
The container runtime is now using Containerd instead of Docker. This change should not have an effect on how your tasks run. You will notice that some error messages that originate with the container runtime will change from mentioning Docker to more general errors. 
 

For more information, see Fargate platform versions for Amazon ECS.  |   

April 8, 2020  |   
|   

Amazon EFS file system support for task volumes  |   

Amazon EFS file systems can be used as data volumes for both your Amazon ECS and Fargate tasks. For more information, see Use Amazon EFS volumes with Amazon ECS.  |   

April 8, 2020  |   
|   

Amazon ECS Task Metadata Endpoint version 4  |   

Beginning with Amazon ECS container agent version 1.39.0 and Fargate platform version 1.4.0, an environment variable named `ECS_CONTAINER_METADATA_URI_V4` is injected into each container in a task. When you query the task metadata version 4 endpoint, various task metadata and Docker stats are available to tasks. For more information, see Amazon ECS task metadata endpoint version 4.  |   

April 8, 2020  |   
|   

Support for specific versions of Secrets Manager secrets to be injected as environment variables  |   

Added support for specifying sensitive data using specific versions of Secrets Manager secrets. For more information, see Pass sensitive data to an Amazon ECS container.  |   

February 24, 2020  |   
|   

Added additional CodeDeploy deployment configuration options for blue/green deployments  |   

The CodeDeploy service added new canary and linear deployment configurations for the Amazon ECS deployment type. The ability to define custom deployment configurations is also available. For more information, see CodeDeploy blue/green deployments for Amazon ECS.  |   

February 6, 2020  |   
|   

Added the efsVolumeConfiguration task definition parameter  |   

The `efsVolumeConfiguration` task definition parameter is in public preview, which makes it easier to use Amazon EFS file systems with your Amazon ECS tasks. For more information, see Use Amazon EFS volumes with Amazon ECS.  |   

January 17, 2020  |   
|   

Amazon ECS container agent logging behavior updated  |   

The Amazon ECS container agent logging locations and rotation behavior has been updated. For more information, see Amazon ECS container agent log configuration parameters.  |   

January 13, 2020  |   
|   

Fargate Spot  |   

Amazon ECS added support for running tasks using Fargate Spot. For more information, see Amazon ECS clusters for Fargate.  |   

December 3, 2019  |   
|   

Cluster Auto Scaling  |   

Amazon ECS cluster auto scaling enables you to have more control over how you scale tasks within a cluster. For more information, see Automatically manage Amazon ECS capacity with cluster auto scaling.  |   

December 3, 2019  |   
|   

Cluster Capacity Providers  |   

Amazon ECS cluster capacity providers determine the infrastructure to use for your tasks. For more information, see Amazon ECS clusters.  |   

December 3, 2019  |   
|   

Creating a cluster on an AWS Outposts  |   

Amazon ECS now supports creating clusters on an AWS Outposts. For more information, see Amazon Elastic Container Service on AWS Outposts.  |   

December 3, 2019  |   
|   

Service Action Events  |   

Amazon ECS now sends events to Amazon EventBridge when certain service actions occur. For more information, see Amazon ECS service action events.  |   

November 25, 2019  |   
|   

Amazon ECS GPU-optimized AMI Supports G4 Instances  |   

Amazon ECS added support for the g4 instance type family when using the Amazon ECS GPU-optimized AMI. For more information, see Amazon ECS task definitions for GPU workloads.  |   

October 8, 2019  |   
|   

FireLens for Amazon ECS  |   

FireLens for Amazon ECS is in general availability. FireLens for Amazon ECS enables you to use task definition parameters to route logs to an AWS service or partner destination for log storage and analytics. For more information, see Send Amazon ECS logs to an AWS service or AWS Partner.  |   

September 30, 2019  |   
|   

AWS Fargate region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Europe (Paris), Europe (Stockholm), and Middle East (Bahrain) regions.  |   

September 30, 2019  |   
|   

Deep Learning Containers with Elastic Inference on Amazon ECS  |   

Amazon ECS supports attaching Amazon Elastic Inference accelerators to your containers to make running deep learning inference workloads more efficient.   |   

September 3, 2019  |   
|   

FireLens for Amazon ECS  |   

FireLens for Amazon ECS is in public preview. FireLens for Amazon ECS enables you to use task definition parameters to route logs to an AWS service or partner destination for log storage and analytics. For more information, see Send Amazon ECS logs to an AWS service or AWS Partner.  |   

August 30, 2019  |   
|   

CloudWatch Container Insights  |   

CloudWatch Container Insights is now generally available. It enables you to collect, aggregate, and summarize metrics and logs from your containerized applications and microservices. For more information, see Monitor Amazon ECS containers using Container Insights with enhanced observability.  |   

August 30, 2019  |   
|   

Container Level Swap Configuration  |   

Amazon ECS added support for controlling the usage of swap memory space on your Linux container instances at the container level. Using a per-container swap configuration, each container within a task definition can have swap enabled or disabled, and for those that have it enabled, the maximum amount of swap space used can be limited. For more information, see Managing container swap memory space on Amazon ECS.  |   

August 16, 2019  |   
|   

AWS Fargate region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Asia Pacific (Hong Kong) Region.  |   

August 6, 2019  |   
|   

Elastic Network Interface Trunking  |   

Added additional supported Amazon EC2 instance types for ENI trunking feature. For more information, see Supported instances for increased Amazon ECS container network interfaces.  |   

August 1, 2019  |   
|   

Registering Multiple Target Groups with a Service  |   

Added support for specifying multiple target groups in a service definition. For more information, see Registering multiple target groups with an Amazon ECS service.  |   

July 30, 2019  |   
|   

Specifying Sensitive Data Using Secrets Manager Secrets  |   

Added tutorial for specifying sensitive data using Secrets Manager secrets. For more information, see Specifying sensitive data using Secrets Manager secrets in Amazon ECS.  |   

July 20, 2019  |   
|   

CloudWatch Container Insights  |   

Amazon ECS has added support for CloudWatch Container Insights. For more information, see Monitor Amazon ECS containers using Container Insights with enhanced observability.  |   

July 9, 2019  |   
|   

Resource-level permissions for Amazon ECS services and tasksets  |   

Amazon ECS has expanded resource-level permissions support for Amazon ECS services and tasks. For more information, see How Amazon Elastic Container Service works with IAM.  |   

June 27, 2019  |   
|   

New Amazon ECS-optimized AMI patched for AWS-2019-005  |   

Amazon ECS has updated the Amazon ECS-optimized AMI to address the vulnerabilities described in AWS-2019-005.  |   

June 17, 2019  |   
|   

Elastic Network Interface Trunking  |   

Amazon ECS introduces support for launching container instances using supported Amazon EC2 instance types that have increased elastic network interface (ENI) density. Using these instance types and opting in to the `awsvpcTrunking` account setting provides increased ENI density on newly launched container instances which allows you to place more tasks on each container instance. For more information, see Increasing Amazon ECS Linux container instance network interfaces.  |   

June 6, 2019  |   
|   

AWS Fargate platform version 1.3.0 update  |   

Beginning on May 1, 2019, any new Fargate task that is launched supports the `splunk` log driver in addition to the `awslogs` log driver. For more information, see Storage and logging.  |   

May 1, 2019  |   
|   

AWS Fargate platform version 1.3.0 update  |   

Beginning on May 1, 2019, any new Fargate task that is launched supports referencing sensitive data in the log configuration of a container using the `secretOptions` container definition parameter. For more information, see Pass sensitive data to an Amazon ECS container.  |   

May 1, 2019  |   
|   

AWS Fargate platform version 1.3.0 update  |   

Beginning on April 2, 2019, any new Fargate task that is launched supports injecting sensitive data into your containers by storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters and then referencing them in your container definition. For more information, see Pass sensitive data to an Amazon ECS container.  |   

Apr 2, 2019  |   
|   

AWS Fargate platform version 1.3.0 update  |   

Beginning on March 27, 2019, any new Fargate task launched can use additional task definition parameters that enable you to define a proxy configuration, dependencies for container startup and shutdown as well as a per-container start and stop timeout value. For more information, see Proxy configuration, Container dependency, and Container timeouts.  |   

March 27, 2019  |   
|   

Amazon ECS introduces the external deployment type  |   

The external deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service. For more information, see Deploy Amazon ECS services using a third-party controller.  |   

March 27, 2019  |   
|   

AWS Deep Learning Containers on Amazon ECS  |   

AWS Deep Learning Containers are a set of Docker images for training and serving models in TensorFlow on Amazon Elastic Container Service (Amazon ECS). Deep Learning Containers provide optimized environments with TensorFlow, Nvidia CUDA (for GPU instances), and Intel MKL (for CPU instances) libraries and are available in Amazon ECR. For more information, see Using AWS Deep Learning Containers on Amazon ECS.  |   

March 27, 2019  |   
|   

Amazon ECS introduces enhanced container dependency management  |   

Amazon ECS introduces additional task definition parameters that enable you to define dependencies for container startup and shutdown as well as a per-container start and stop timeout value. For more information, see Container dependency.  |   

March 7, 2019  |   
|   

Amazon ECS introduces the `PutAccountSettingDefault` API  |   

Amazon ECS introduces the `PutAccountSettingDefault` API that allows a user to set the default ARN/ID format opt in status for all the users and roles on the account. Previously, setting the account's default opt in status required the use of the account owner. 

For more information, see Amazon Resource Names (ARNs) and IDs.  |   

February 8, 2019  |   
|   

Amazon ECS supports GPU workloads  |   

Amazon ECS introduces support for GPU workloads by enabling you to create clusters with GPU-enabled container instances. In a task definition you can specify the number of required GPUs and the ECS agent will pin the physical GPUs to the container. 

For more information, see Amazon ECS task definitions for GPU workloads.  |   

February 4, 2019  |   
|   

Amazon ECS expanded secrets support  |   

Amazon ECS expanded support for using AWS Secrets Manager secrets directly in your task definitions to inject sensitive data into your containers. 

For more information, see Pass sensitive data to an Amazon ECS container.  |   

January 21, 2019  |   
|   

Interface VPC Endpoints (AWS PrivateLink)  |   

Added support for configuring interface VPC endpoints powered by AWS PrivateLink. This allows you to create a private connection between your VPC and Amazon ECS without requiring access over the Internet, through a NAT instance, a VPN connection, or Direct Connect. 

For more information, see Interface VPC Endpoints (AWS PrivateLink).  |   

December 26, 2018  |   
|   

AWS Fargate platform version 1.3.0  |   

New AWS Fargate platform version released, which contains:  
Added support for using AWS Systems Manager Parameter Store parameters to inject sensitive data into your containers. 

For more information, see Pass sensitive data to an Amazon ECS container. 
Added task recycling for Fargate tasks, which is the process of refreshing tasks that are a part of an Amazon ECS service. 

For more information, see Task retirement and maintenance for AWS Fargate on Amazon ECS. 
 

For more information, see Fargate platform versions for Amazon ECS.  |   

December 17, 2018  |   
|   

Service limits updated  |   

The following service limits were updated:  
Number of clusters per Region, per account was raised from `1000` to `2000`. 
Number of container instances per cluster was raised from `1000` to `2000`. 
Number of services per cluster was raised from `500` to `1000`. 
 

For more information, see Amazon ECS service quotas.  |   

December 14, 2018  |   
|   

AWS Fargate region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Asia Pacific (Mumbai) and Canada (Central) Regions. 

For more information, see Supported Regions for Amazon ECS on AWS Fargate.  |   

December 7, 2018  |   
|   

Amazon ECS blue/green deployments  |   

Amazon ECS added support for blue/green deployments using CodeDeploy. This deployment type allows you to verify a new deployment of a service before sending production traffic to it. 

For more information, see CodeDeploy blue/green deployments for Amazon ECS.  |   

November 27, 2018  |   
|   

Amazon ECS-optimized Amazon Linux 2 (arm64) AMI released  |   

Amazon ECS released an Amazon ECS-optimized Amazon Linux 2 AMIs for arm64 architecture. 

For more information, see Amazon ECS-optimized Linux AMIs.  |   

November 26, 2018  |   
|   

Added support for additional Docker flags in task definitions  |   

Amazon ECS introduced support for the following Docker flags in task definitions:  
IPC mode 
PID mode 
  |   

November 16, 2018  |   
|   

Amazon ECS secrets support  |   

Amazon ECS added support for using AWS Systems Manager Parameter Store parameters to inject sensitive data into your containers. 

For more information, see Pass sensitive data to an Amazon ECS container.  |   

November 15, 2018  |   
|   

Resource tagging  |   

Amazon ECS added support for adding metadata tags to your services, task definitions, tasks, clusters, and container instances. 

For more information, see Tagging Amazon ECS resources.  |   

November 15, 2018  |   
|   

AWS Fargate Region expansion  |   

AWS Fargate with Amazon ECS has expanded to the US West (N. California) and Asia Pacific (Seoul) Regions. 

For more information, see Architect for AWS Fargate for Amazon ECS.  |   

November 7, 2018  |   
|   

Service limits updated  |   

The following service limits were updated:  
Number of tasks using the Fargate launch type, per Region, per account was raised from `20` to `50`. 
Number of public IP addresses for tasks using the Fargate launch type was raised from `20` to `50`. 
 

For more information, see Amazon ECS service quotas.  |   

October 31, 2018  |   
|   

AWS Fargate Region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Europe (London) Region. 

For more information, see Architect for AWS Fargate for Amazon ECS.  |   

October 26, 2018  |   
|   

Amazon ECS-optimized Amazon Linux 2 AMI Released  |   

Amazon ECS vends Linux AMIs that are optimized for the service in two variants. The latest and recommended version is based on x;. Amazon ECS also vends AMIs that are based on the , but we recommend that you migrate your workloads to the Amazon Linux 2 variant, as support for the Amazon Linux AMI will end no later than June 30, 2020. 

For more information, see Amazon ECS-optimized Linux AMIs.  |   

October 18, 2018  |   
|   

Amazon ECS Task Metadata Endpoint version 3  |   

Beginning with version 1.21.0 of the Amazon ECS container agent, the agent injects an environment variable called `ECS_CONTAINER_METADATA_URI` into each container in a task. When you query the task metadata version 3 endpoint, various task metadata and Docker stats are available to tasks that use the `awsvpc` network mode at an HTTP endpoint that is provided by the Amazon ECS container agent. For more information, see Monitor workloads using Amazon ECS metadata.  |   

October 18, 2018  |   
|   

Amazon ECS service discovery Region expansion  |   

Amazon ECS service discovery has expanded support to the Canada (Central), South America (São Paulo), Asia Pacific (Seoul), Asia Pacific (Mumbai), and Europe (Paris) Regions. 

For more information, see Use service discovery to connect Amazon ECS services with DNS names.  |   

September 27, 2018  |   
|   

Added support for additional Docker flags in container definitions  |   

Amazon ECS introduced support for the following Docker flags in container definitions:  
System controls 
Interactive 
Pseudo terminal 
  |   

September 17, 2018  |   
|   

Private registry authentication support for Amazon ECS using AWS Fargate tasks  |   

Amazon ECS introduced support for Fargate tasks using private registry authentication using AWS Secrets Manager. This feature enables you to store your credentials securely and then reference them in your container definition, which allows your tasks to use private images. 

For more information, see Using non-AWS container images in Amazon ECS.  |   

September 10, 2018  |   
|   

Amazon ECS service discovery Region expansion  |   

Amazon ECS service discovery has expanded support to the Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), EU (Frankfurt), and Europe (London) Regions. 

For more information, see Use service discovery to connect Amazon ECS services with DNS names.  |   

August 30, 2018  |   
|   

Scheduled tasks with Fargate tasks support  |   

Amazon ECS introduced support for scheduled tasks for the Fargate launch type.  |   

August 28, 2018  |   
|   

Private registry authentication using AWS Secrets Manager support  |   

Amazon ECS introduced support for private registry authentication using AWS Secrets Manager. This feature enables you to store your credentials securely and then reference them in your container definition, which allows your tasks to use private images. 

For more information, see Using non-AWS container images in Amazon ECS.  |   

August 16, 2018  |   
|   

Docker volume support added  |   

Amazon ECS introduced support for Docker volumes. 

For more information, see Storage options for Amazon ECS tasks.  |   

August 9, 2018  |   
|   

AWS Fargate Region expansion  |   

AWS Fargate with Amazon ECS has expanded to the Europe (Frankfurt), Asia Pacific (Singapore), and Asia Pacific (Sydney) Regions. 

For more information, see Architect for AWS Fargate for Amazon ECS.  |   

July 19, 2018  |   
|   

Amazon ECS service scheduler strategies added  |  Amazon ECS introduced the concept of service scheduler strategies. 

There are two service scheduler strategies available:  
`REPLICA`—The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see Replica scheduling strategy. 
`DAEMON`—The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see Daemon scheduling strategy. Note

Fargate tasks do not support the `DAEMON` scheduling strategy. 
. |   

June 12, 2018  |   
|   

Amazon ECS container agent v1.18.0  |   

New version of the Amazon ECS container agent released, which added the following functionality:  
Added support for customizing the container agent image pull behavior using the `ECS_IMAGE_PULL_BEHAVIOR` parameter. For more information, see Amazon ECS container agent configuration. 
 

For more information, see amazon-ecs-agent github.  |   

May 24, 2018  |   
|   

Added Support for `bridge` and `host` Network Modes When Configuring Service Discovery  |   

Added support for configuring service discovery for Amazon ECS services using task definitions that specify the `bridge` or `host` network modes. For more information, see Use service discovery to connect Amazon ECS services with DNS names.  |   

May 22, 2018  |   
|   

Added support for additional Amazon ECS-optimized AMI metadata parameters  |   

Added subparameters that allow you to programatically retrieve the Amazon ECS-optimized AMI ID, image name, operating system, container agent version, and runtime version. Query the metadata using the Systems Manager Parameter Store API. For more information, see Retrieving Amazon ECS-optimized Linux AMI metadata.  |   

May 9, 2018  |   
|   

AWS Fargate Region expansion  |   

AWS Fargate with Amazon ECS has expanded to the US East (Ohio), US West (Oregon), and EU West (Ireland) Regions. 

For more information, see Architect for AWS Fargate for Amazon ECS.  |   

April 26, 2018  |   
|   

Amazon ECS-optimized AMI Metadata Retrieval  |   

Added ability to programatically retrieve Amazon ECS-optimized AMI metadata using the Systems Manager Parameter Store API. For more information, see Retrieving Amazon ECS-optimized Linux AMI metadata.  |   

April 10, 2018  |   
|   

AWS Fargate platform version  |   

New AWS Fargate platform version released, which contains:  
Added support for Monitor workloads using Amazon ECS metadata. 
Added support for Health check. 
Added support for Use service discovery to connect Amazon ECS services with DNS names 
 

For more information, see Fargate platform versions for Amazon ECS.  |   

March 26, 2018  |   
|   

Amazon ECS Service Discovery  |   

Added integration with Route 53 to support Amazon ECS service discovery. For more information, see Use service discovery to connect Amazon ECS services with DNS names.  |   

March 22, 2018  |   
|   

Docker shm-size and tmpfs support  |  Added support for the Docker shm-size and tmpfs parameters in Amazon ECS task definitions.

For more information about the updated ECS CLI syntax, see Linux parameters. |   

March 20, 2018  |   
|   

Container Health Checks  |   

Added support for Docker health checks in container definitions. For more information, see Health check.  |   

March 8, 2018  |   
|   

AWS Fargate  |   

Added overview for Amazon ECS with AWS Fargate. For more information, see Architect for AWS Fargate for Amazon ECS.  |   

February 22, 2018  |   
|   

Amazon ECS Task Metadata Endpoint  |   

Beginning with version 1.17.0 of the Amazon ECS container agent, various task metadata and Docker stats are available to tasks that use the `awsvpc` network mode at an HTTP endpoint that is provided by the Amazon ECS container agent. For more information, see Monitor workloads using Amazon ECS metadata.  |   

February 8, 2018  |   
|   

Amazon ECS Service Auto Scaling using target tracking policies  |   

Added support for ECS Service Auto Scaling using target tracking policies in the Amazon ECS console. For more information, see Use a target metric to scale Amazon ECS services. 

Removed the previous tutorial for step scaling in the ECS first run wizard. This was replaced with the new tutorial for target tracking.  |   

February 8, 2018  |   
|   

Docker 17.09 support  |   

Added support for Docker 17.09. For more information, see Amazon ECS-optimized Linux AMIs.  |   

January 18, 2018  |   
|   

New service scheduler behavior  |   

Updated information about the behavior for service tasks that fail to launch. Documented new service event message that triggers when a service task has consecutive failures. .  |   

January 11, 2018  |   
|   

Elastic Load Balancing health check initialization wait period  |   

Added ability to specify a wait period for health checks.  |   

December 27, 2017  |   
|   

Task-level CPU and memory  |   

Added support for specifying CPU and memory at the task-level in task definitions. For more information, see TaskDefinition.  |   

December 12, 2017  |   
|   

Task execution role   |   

The Amazon ECS container agent makes calls to the Amazon ECS API actions on your behalf, so it requires an IAM policy and role for the service to know that the agent belongs to you. The following actions are covered by the task execution role:  
Calls to Amazon ECR to pull the container image 
Calls to CloudWatch to store container application logs 
 

For more information, see Amazon ECS task execution IAM role.  |   

December 7, 2017  |   
|   

Windows containers support GA  |   

Added support for Windows Server 2016 containers. For more information, see Amazon ECS-optimized AMI variants.  |   

December 5, 2017  |   
|   

AWS Fargate GA  |   

Added support for launching Amazon ECS services using the Fargate launch type. For more information, see Architect your solution for Amazon ECS.  |   

November 29, 2017  |   
|   

Amazon ECS name change  |   

Amazon Elastic Container Service is renamed (previously Amazon EC2 Container Service).  |   

November 21, 2017  |   
|   

Task networking  |   

The task networking features provided by the awsvpc network mode give Amazon ECS tasks the same networking properties as Amazon EC2 instances. When you use the awsvpc network mode in your task definitions, every task that is launched from that task definition gets its own elastic network interface, a primary private IP address, and an internal DNS hostname. The task networking feature simplifies container networking and gives you more control over how containerized applications communicate with each other and other services within your VPCs. For more information, see Amazon ECS task networking options for EC2.  |   

November 14, 2017  |   
|   

Amazon ECS container metadata  |   

Amazon ECS containers are now able to access metadata such as their Docker container or image ID, networking configuration, or Amazon ARNs. For more information, see Amazon ECS container metadata file.  |   

November 2, 2017  |   
|   

Docker 17.06 support  |   

Added support for Docker 17.06. For more information, see Amazon ECS-optimized Linux AMIs.  |   

November 2, 2017  |   
|   

Support for Docker flags: device and init  |   

Added support for Docker's device and init features in task definitions using the `LinuxParameters` parameter (`devices` and `initProcessEnabled`). For more information, see LinuxParameters.  |   

November 2, 2017  |   
|   

Support for Docker flags: cap-add and cap-drop  |   

Added support for Docker's cap-add and cap-drop features in task definitions using the `LinuxParameters` parameter (`capabilities`). For more information, see LinuxParameters.  |   

September 22, 2017  |   
|   

Network Load Balancer support  |   

Amazon ECS added support for Network Load Balancers in the Amazon ECS console.  |   

September 7, 2017  |   
|   

RunTask overrides  |   

Added support for task definition overrides when running a task. This allows you to run a task while changing a task definition without the need to create a new task definition revision. For more information, see Running an application as an Amazon ECS task.  |   

June 27, 2017  |   
|   

Amazon ECS scheduled tasks  |   

Added support for scheduling tasks using cron.  |   

June 7, 2017  |   
|   

Spot Instances in the Amazon ECS console  |   

Added support for creating Spot Fleet container instances within the Amazon ECS console. For more information, see Launching an Amazon ECS Linux container instance.  |   

June 6, 2017  |   
|   

Amazon SNS notification for new Amazon ECS-optimized AMI releases  |   

Added ability to subscribe to SNS notifications about new Amazon ECS-optimized AMI releases.  |   

March 23, 2017  |   
|   

Microservices and batch jobs  |   

Added documentation for two common use cases for Amazon ECS: microservices and batch jobs.   |   

February 2017  |   
|   

Container instance draining  |   

Added support for container instance draining, which provides a method for removing container instances from a cluster. For more information, see Draining Amazon ECS container instances.  |   

January 24, 2017  |   
|   

Docker 1.12 support  |   

Added support for Docker 1.12. For more information, see Amazon ECS-optimized Linux AMIs.  |   

January 24, 2017  |   
|   

New task placement strategies  |   

Added support for task placement strategies: attribute-based placement, bin pack, Availability Zone spread, and one per host. For more information, see Use strategies to define Amazon ECS task placement.  |   

December 29, 2016  |   
|   

Windows container support in beta  |   

Added support for Windows Server 2016 containers (beta). For more information, see Amazon ECS-optimized AMI variants.  |   

December 20, 2016  |   
|   

Blox OSS support  |   

Added support for Blox OSS, which allows for custom task schedulers. For more information, see Schedule your containers on Amazon ECS.  |   

December 1, 2016  |   
|   

Amazon ECS event stream for CloudWatch Events  |   

Amazon ECS now sends container instance and task state changes to CloudWatch Events. For more information, see Automate responses to Amazon ECS errors using EventBridge.  |   

November 21, 2016  |   
|   

Amazon ECS container logging to CloudWatch Logs  |   

Added support for the awslogs driver to send container log streams to CloudWatch Logs. For more information, see Send Amazon ECS logs to CloudWatch.  |   

September 12, 2016  |   
|   

Amazon ECS services with Elastic Load Balancing support for dynamic ports  |   

Added support for a load balancer to support multiple instance:port combinations per listener, which increases flexibility for containers. Now you can let Docker dynamically define the container's host port and the ECS scheduler registers the instance:port with the load balancer. For more information, see Use load balancing to distribute Amazon ECS service traffic.  |   

August 11, 2016  |   
|   

IAM roles for Amazon ECS tasks  |   

Added support for associating IAM roles with a task. This provides finer-grained permissions to containers as opposed to a single role for an entire container instance. For more information, see Amazon ECS task IAM role.  |   

July 13, 2016  |   
|   

Docker 1.11 support  |   

Added support for Docker 1.11. For more information, see Amazon ECS-optimized Linux AMIs.  |   

May 31, 2016  |   
|   

Task automatic scaling  |   

Amazon ECS added support for automatically scaling your tasks run by a service. For more information, see Automatically scale your Amazon ECS service.  |   

May 18, 2016  |   
|   

Task definition filtering on task family  |   

Added support for filtering a list of task definition based on the task definition family. For more information, see ListTaskDefinitions.  |   

May 17, 2016  |   
|   

Docker container and Amazon ECS agent logging  |   

Amazon ECS added ability to send ECS agent and Docker container logs from container instances to CloudWatch Logs to simplify troubleshooting issues.  |   

May 5, 2016  |   
|   

ECS-optimized AMI now supports Amazon Linux 2016.03.  |   

The ECS-optimized AMI added support for Amazon Linux 2016.03. For more information, see Amazon ECS-optimized Linux AMIs.  |   

April 5, 2016  |   
|   

Docker 1.9 support  |   

Added support for Docker 1.9. For more information, see Amazon ECS-optimized Linux AMIs.  |   

December 22, 2015  |   
|   

CloudWatch metrics for cluster CPU and memory reservation  |   

Amazon ECS added custom CloudWatch metrics for CPU and memory reservation.  |   

December 22, 2015  |   
|   

New Amazon ECS first-run experience  |   

The Amazon ECS console first-run experience added zero-click role creation.  |   

November 23, 2015  |   
|   

Task placement across Availability Zones  |   

The Amazon ECS service scheduler added support for task placement across Availability Zones.   |   

October 8, 2015  |   
|   

CloudWatch metrics for Amazon ECS clusters and services  |   

Amazon ECS added custom CloudWatch metrics for CPU and memory utilization for each container instance, service, and task definition family in a cluster. These new metrics can be used to scale container instances in a cluster using Auto Scaling groups or to create custom CloudWatch alarms.  |   

August 17, 2015  |   
|   

UDP port support  |   

Added support for UDP ports in task definitions.  |   

July 7, 2015  |   
|   

Environment variable overrides  |   

Added support for deregisterTaskDefinition and environment variable overrides for runTask.  |   

June 18, 2015  |   
|   

Automated Amazon ECS agent updates  |   

Added ability to see the ECS agent version that is running on a container instance. Also able to update the ECS agent from the AWS Management Console, AWS CLI, and SDK.  |   

June 11, 2015  |   
|   

Amazon ECS service scheduler and Elastic Load Balancing integration  |   

Added ability to define a service and associate that service with an Elastic Load Balancing load balancer.  |   

April 9, 2015  |   
|   

Amazon ECS GA  |   

Amazon ECS general availability in the US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland) Regions.  |   

April 9, 2015  |
