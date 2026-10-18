> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html
> Downloaded: 2026-10-18

# AWS::ECS::Service

The `AWS::ECS::Service` resource creates an Amazon Elastic Container Service (Amazon ECS) service that runs and maintains the requested number of tasks and associated load balancers.Important

The stack update fails if you change any properties that require replacement and at least one Amazon ECS Service Connect `ServiceConnectConfiguration` property is configured. This is because AWS CloudFormation creates the replacement service first, but each `ServiceConnectService` must have a name that is unique in the namespace.Note

Starting April 15, 2023, AWS; will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service. Important

On June 12, 2025, Amazon ECS launched support for updating capacity provider configuration for Amazon ECS services. With this launch, Amazon ECS also aligned the CloudFormation update behavior for `CapacityProviderStrategy` parameter with the standard practice. For more information, see Amazon ECS adds support for updating capacity provider configuration for ECS services. Previously Amazon ECS ignored the `CapacityProviderStrategy` property if it was set to an empty list for example, `[]` in CloudFormation, because updating capacity provider configuration was not supported. Now, with support for capacity provider updates, customers can remove capacity providers from a service by passing an empty list. When you specify an empty list (`[]`) for the `CapacityProviderStrategy` property in your CloudFormation template, Amazon ECS will remove any capacity providers associated with the service, as follows: 
For services created with a capacity provider strategy after the launch:  
If there's a cluster default strategy set, the service will revert to using that default strategy. 
If no cluster default strategy exists, you will receive the following error: 

No launch type to fall back to for empty capacity provider strategy. Your service was not created with a launch type. 
For services created with a capacity provider strategy prior to the launch:  
If `CapacityProviderStrategy` had `FARGATE_SPOT` or `FARGATE` capacity providers, the launch type will be updated to `FARGATE` and the capacity provider will be removed. 
If the strategy included Auto Scaling group capacity providers, the service will revert to EC2 launch type, and the Auto Scaling group capacity providers will not be used. 
 

Recommended Actions

If you are currently using `CapacityProviderStrategy: []` in your CloudFormation templates, you should take one of the following actions: 
If you do not intend to update the Capacity Provider Strategy:  
Remove the `CapacityProviderStrategy` property entirely from your CloudFormation template 
Alternatively, use `!Ref AWS::NoValue` for the `CapacityProviderStrategy` property in your template 
If you intend to maintain or update the Capacity Provider Strategy, specify the actual Capacity Provider Strategy for the service in your CloudFormation template. 

If your CloudFormation template had an empty list ([]) for `CapacityProviderStrategy` prior to the aforementioned launch on June 12, and you are using the same template with `CapacityProviderStrategy: []`, you might encounter the following error:

 Invalid request provided: When switching from launch type to capacity provider strategy on an existing service, or making a change to a capacity provider strategy on a service that is already using one, you must force a new deployment. (Service: Ecs, Status Code: 400, Request ID: xxx) (SDK Attempt Count: 1)" (RequestToken: xxx HandlerErrorCode: InvalidRequest) 

Note that CloudFormation automatically initiates a new deployment when it detects a parameter change, but customers cannot choose to force a deployment through CloudFormation. This is an invalid input scenario that requires one of the remediation actions listed above.

If you are experiencing active production issues related to this change, contact AWS Support or your Technical Account Manager.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::Service",
  "Properties" : {
      "AvailabilityZoneRebalancing" : String,
      "CapacityProviderStrategy" : [ CapacityProviderStrategyItem, ... ],
      "Cluster" : String,
      "DeploymentConfiguration" : DeploymentConfiguration,
      "DeploymentController" : DeploymentController,
      "DesiredCount" : Integer,
      "EnableECSManagedTags" : Boolean,
      "EnableExecuteCommand" : Boolean,
      "ForceNewDeployment" : ForceNewDeployment,
      "HealthCheckGracePeriodSeconds" : Integer,
      "LaunchType" : String,
      "LoadBalancers" : [ LoadBalancer, ... ],
      "Monitoring" : MonitoringConfiguration,
      "NetworkConfiguration" : NetworkConfiguration,
      "PlacementConstraints" : [ PlacementConstraint, ... ],
      "PlacementStrategies" : [ PlacementStrategy, ... ],
      "PlatformVersion" : String,
      "PropagateTags" : String,
      "Role" : String,
      "SchedulingStrategy" : String,
      "ServiceConnectConfiguration" : ServiceConnectConfiguration,
      "ServiceName" : String,
      "ServiceRegistries" : [ ServiceRegistry, ... ],
      "Tags" : [ Tag, ... ],
      "TaskDefinition" : String,
      "VolumeConfigurations" : [ ServiceVolumeConfiguration, ... ],
      "VpcLatticeConfigurations" : [ VpcLatticeConfiguration, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::Service
Properties:
  AvailabilityZoneRebalancing: String
  CapacityProviderStrategy: 
    - CapacityProviderStrategyItem
  Cluster: String
  DeploymentConfiguration: 
    DeploymentConfiguration
  DeploymentController: 
    DeploymentController
  DesiredCount: Integer
  EnableECSManagedTags: Boolean
  EnableExecuteCommand: Boolean
  ForceNewDeployment: 
    ForceNewDeployment
  HealthCheckGracePeriodSeconds: Integer
  LaunchType: String
  LoadBalancers: 
    - LoadBalancer
  Monitoring: 
    MonitoringConfiguration
  NetworkConfiguration: 
    NetworkConfiguration
  PlacementConstraints: 
    - PlacementConstraint
  PlacementStrategies: 
    - PlacementStrategy
  PlatformVersion: String
  PropagateTags: String
  Role: String
  SchedulingStrategy: String
  ServiceConnectConfiguration: 
    ServiceConnectConfiguration
  ServiceName: String
  ServiceRegistries: 
    - ServiceRegistry
  Tags: 
    - Tag
  TaskDefinition: String
  VolumeConfigurations: 
    - ServiceVolumeConfiguration
  VpcLatticeConfigurations: 
    - VpcLatticeConfiguration

```

## Properties

**`AvailabilityZoneRebalancing`** 

Indicates whether to use Availability Zone rebalancing for the service. 

For more information, see Balancing an Amazon ECS service across Availability Zones in the  Amazon Elastic Container Service Developer Guide . 

The default behavior of `AvailabilityZoneRebalancing` differs between create and update requests:  
For create service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults the value to `ENABLED`. 
For update service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults to the existing service’s `AvailabilityZoneRebalancing` value. If the service never had an `AvailabilityZoneRebalancing` value set, Amazon ECS treats this as `DISABLED`. 
 

Required: No

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: No interruption

**`CapacityProviderStrategy`** 

The capacity provider strategy to use for the service. 

If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or `launchType` is specified, the `defaultCapacityProviderStrategy` for the cluster is used. 

A capacity provider strategy can contain a maximum of 20 capacity providers. Important

To remove this property from your service resource, specify an empty `CapacityProviderStrategyItem` array. 

Required: No

Type: Array of CapacityProviderStrategyItem

Update requires: No interruption

**`Cluster`** 

The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed. 

Required: No

Type: String

Update requires: Replacement

**`DeploymentConfiguration`** 

Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks. 

Required: No

Type: DeploymentConfiguration

Update requires: No interruption

**`DeploymentController`** 

The deployment controller to use for the service.  

Required: No

Type: DeploymentController

Update requires: No interruption

**`DesiredCount`** 

The number of instantiations of the specified task definition to place and keep running in your service. 

For new services, if a desired count is not specified, a default value of `1` is used. When using the `DAEMON` scheduling strategy, the desired count is not required. 

For existing services, if a desired count is not specified, it is omitted from the operation. 

Required: Conditional

Type: Integer

Update requires: No interruption

**`EnableECSManagedTags`** 

Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see Tagging your Amazon ECS resources in the Amazon Elastic Container Service Developer Guide. 

When you use Amazon ECS managed tags, you must set the `propagateTags` request parameter. 

Required: No

Type: Boolean

Update requires: No interruption

**`EnableExecuteCommand`** 

Determines whether the execute command functionality is turned on for the service. If `true`, the execute command functionality is turned on for all containers in tasks as part of the service. 

Required: No

Type: Boolean

Update requires: No interruption

**`ForceNewDeployment`** 

Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version. 

Required: No

Type: ForceNewDeployment

Update requires: No interruption

**`HealthCheckGracePeriodSeconds`** 

The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then `healthCheckGracePeriodSeconds` is unused. 

If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count. 

Required: No

Type: Integer

Update requires: No interruption

**`LaunchType`** 

The launch type on which to run your service. For more information, see Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide. Note

If you want to use Managed Instances, you must use the `capacityProviderStrategy` request parameter 

Required: No

Type: String

Allowed values: `EC2 | FARGATE | EXTERNAL`

Update requires: Some interruptions

**`LoadBalancers`** 

A list of load balancer objects to associate with the service. If you specify the `Role` property, `LoadBalancers` must be specified as well. For information about the number of load balancers that you can specify per service, see Service Load Balancing in the Amazon Elastic Container Service Developer Guide. Important

To remove this property from your service resource, specify an empty `LoadBalancer` array. 

Required: No

Type: Array of LoadBalancer

Update requires: No interruption

**`Monitoring`** 

The optional monitoring configuration for the service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds. 

Required: No

Type: MonitoringConfiguration

Update requires: No interruption

**`NetworkConfiguration`** 

The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide. 

Required: Conditional

Type: NetworkConfiguration

Update requires: No interruption

**`PlacementConstraints`** 

An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime. Important

To remove this property from your service resource, specify an empty `PlacementConstraint` array. 

Required: No

Type: Array of PlacementConstraint

Update requires: No interruption

**`PlacementStrategies`** 

The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service. Important

To remove this property from your service resource, specify an empty `PlacementStrategy` array. 

Required: No

Type: Array of PlacementStrategy

Update requires: No interruption

**`PlatformVersion`** 

The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the `LATEST` platform version is used. For more information, see AWS Fargate platform versions in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Update requires: No interruption

**`PropagateTags`** 

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action. 

You must set this to a value other than `NONE` when you use Cost Explorer. For more information, see Amazon ECS usage reports in the Amazon Elastic Container Service Developer Guide. 

The default is `NONE`. 

Required: No

Type: String

Allowed values: `SERVICE | TASK_DEFINITION`

Update requires: No interruption

**`Role`** 

The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the `awsvpc` network mode. If you specify the `role` parameter, you must also specify a load balancer object with the `loadBalancers` parameter. Important

If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the `awsvpc` network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see Using service-linked roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide. 

If your specified role has a path other than `/`, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name `bar` has a path of `/foo/` then you would specify `/foo/bar` as the role name. For more information, see Friendly names and paths in the IAM User Guide. 

Required: No

Type: String

Update requires: Replacement

**`SchedulingStrategy`** 

The scheduling strategy to use for the service. For more information, see Services. 

There are two service scheduler strategies available:  
`REPLICA`-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the `CODE_DEPLOY` or `EXTERNAL` deployment controller types. 
`DAEMON`-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. Note

Tasks using the Fargate launch type or the `CODE_DEPLOY` or `EXTERNAL` deployment controller types don't support the `DAEMON` scheduling strategy. 
 

Required: No

Type: String

Allowed values: `DAEMON | REPLICA`

Update requires: Replacement

**`ServiceConnectConfiguration`** 

The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace. 

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see Service Connect in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: ServiceConnectConfiguration

Update requires: No interruption

**`ServiceName`** 

The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions. Important

The stack update fails if you change any properties that require replacement and the `ServiceName` is configured. This is because AWS CloudFormation creates the replacement service first, but each `ServiceName` must be unique in the cluster. 

Required: No

Type: String

Update requires: Replacement

**`ServiceRegistries`** 

The details of the service discovery registry to associate with this service. For more information, see Service discovery. Note

Each service may be associated with one service registry. Multiple service registries for each service isn't supported. Important

To remove this property from your service resource, specify an empty `ServiceRegistry` array. 

Required: No

Type: Array of ServiceRegistry

Update requires: No interruption

**`Tags`** 

The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well. 

The following basic restrictions apply to tags:  
Maximum number of tags per resource - 50 
For each resource, each tag key must be unique, and each tag key can have only one value. 
Maximum key length - 128 Unicode characters in UTF-8 
Maximum value length - 256 Unicode characters in UTF-8 
If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @. 
Tag keys and values are case-sensitive. 
Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit. 
 

Required: No

Type: Array of Tag

Minimum: `0`

Maximum: `50`

Update requires: No interruption

**`TaskDefinition`** 

The `family` and `revision` (`family:revision`) or full ARN of the task definition to run in your service. If a `revision` isn't specified, the latest `ACTIVE` revision is used. 

A task definition must be specified if the service uses either the `ECS` or `CODE_DEPLOY` deployment controllers. 

For more information about deployment types, see Amazon ECS deployment types. 

Required: No

Type: String

Update requires: No interruption

**`VolumeConfigurations`** 

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume. Important

To remove this property from your service resource, specify an empty `ServiceVolumeConfiguration` array. 

Required: No

Type: Array of ServiceVolumeConfiguration

Update requires: No interruption

**`VpcLatticeConfigurations`** 

The VPC Lattice configuration for the service being created. 

Required: No

Type: Array of VpcLatticeConfiguration

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN).

In the following example, the `Ref` function returns the ARN of the `MyECSService` service, such as `arn:aws:ecs:us-west-2:123456789012:service/sample-webapp`.

 `{ "Ref": "MyECSService" }` 

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Name`** 

The name of the Amazon ECS service, such as `sample-webapp`. 

**`ServiceArn`** 

The ARN that identifies the service. For more information about the ARN format, see Amazon Resource Name (ARN) in the Amazon ECS Developer Guide. 

## Examples
Create a service that uses a task definition
Create a service with a volume configuration
Associate an Application Load Balancer with a service
 

### Create a service that uses a task definition

The following example template creates a service, a cluster, and a task definition. The cluster contains the service. The service — with a `DesiredCount` of 1 — uses the task definition defined in the template. Replace the `ExecutionRoleArn`, `SecurityGroups`, and `Subnets` with your own information.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ECSCluster": {
            "Type": "AWS::ECS::Cluster",
            "Properties": {
                "ClusterName": "CFNCluster"
            }
        },
        "ECSTaskDefinition": {
            "Type": "AWS::ECS::TaskDefinition",
            "Properties": {
                "ContainerDefinitions": [
                    {
                        "Command": [
                            "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
                        ],
                        "EntryPoint": [
                            "sh",
                            "-c"
                        ],
                        "Essential": true,
                        "Image": "public.ecr.aws/docker/library/httpd:2.4",
                        "LogConfiguration": {
                            "LogDriver": "awslogs",
                            "Options": {
                                "awslogs-group": "/ecs/fargate-task-definition",
                                "awslogs-region": "us-east-1",
                                "awslogs-stream-prefix": "ecs"
                            }
                        },
                        "Name": "sample-fargate-app",
                        "PortMappings": [
                            {
                                "ContainerPort": 80,
                                "HostPort": 80,
                                "Protocol": "tcp"
                            }
                        ]
                    }
                ],
                "Cpu": 256,
                "ExecutionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
                "Family": "task-definition-cfn",
                "Memory": 512,
                "NetworkMode": "awsvpc",
                "RequiresCompatibilities": [
                    "FARGATE"
                ],
                "RuntimePlatform": {
                    "OperatingSystemFamily": "LINUX"
                }
            }
        },
        "ECSService": {
            "Type": "AWS::ECS::Service",
            "Properties": {
                "ServiceName": "cfn-service",
                "Cluster": {
                    "Ref": "ECSCluster"
                },
                "DesiredCount": 1,
                "LaunchType": "FARGATE",
                "NetworkConfiguration": {
                    "AwsvpcConfiguration": {
                        "AssignPublicIp": "ENABLED",
                        "SecurityGroups": [
                            "sg-abcdef01234567890"
                        ],
                        "Subnets": [
                            "subnet-021345abcdef67890"
                        ]
                    }
                },
                "TaskDefinition": {
                    "Ref": "ECSTaskDefinition"
                }
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ECSCluster:
    Type: 'AWS::ECS::Cluster'
    Properties:
      ClusterName: CFNCluster
  ECSTaskDefinition:
    Type: 'AWS::ECS::TaskDefinition'
    Properties:
      ContainerDefinitions:
        - Command:
            - >-
              /bin/sh -c "echo '<html> <head> <title>Amazon ECS Sample
              App</title> <style>body {margin-top: 40px; background-color:
              #333;} </style> </head><body> <div
              style=color:white;text-align:center> <h1>Amazon ECS Sample
              App</h1> <h2>Congratulations!</h2> <p>Your application is now
              running on a container in Amazon ECS.</p> </div></body></html>' > 
              /usr/local/apache2/htdocs/index.html && httpd-foreground"
          EntryPoint:
            - sh
            - '-c'
          Essential: true
          Image: 'public.ecr.aws/docker/library/httpd:2.4'
          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: /ecs/fargate-task-definition
              awslogs-region: us-east-1
              awslogs-stream-prefix: ecs
          Name: sample-fargate-app
          PortMappings:
            - ContainerPort: 80
              HostPort: 80
              Protocol: tcp
      Cpu: 256
      ExecutionRoleArn: 'arn:aws:iam::111122223333:role/ecsTaskExecutionRole'
      Family: task-definition-cfn
      Memory: 512
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      RuntimePlatform:
        OperatingSystemFamily: LINUX
  ECSService:
    Type: 'AWS::ECS::Service'
    Properties:
      ServiceName: cfn-service
      Cluster: !Ref ECSCluster
      DesiredCount: 1
      LaunchType: FARGATE
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            - sg-abcdef01234567890
          Subnets:
            - subnet-021345abcdef67890
      TaskDefinition: !Ref ECSTaskDefinition
```
 

### Create a service with a volume configuration

The following example template creates a service that utilizes a pre-existing task that defers volume configuration to service creation. This example template provides volume configuration that Amazon ECS uses to create and attach an Amazon EBS volume to each task in the service. For more information about defering volume configuration and using Amazon EBS volumes with Amazon ECS, see Use Amazon EBS volumes with Amazon ECS in the Amazon ECS Developer Guide. Replace `SubnetIDs`, `SecurityGroupIDs`, `TaskDefinition`, and `ManagedEBSVolume` with your own information. 

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "The template used to create an ECS Service that includes a volume configuration.",
    "Parameters": {
      "ECSClusterName": {
        "Type": "String",
        "Default": "volume-config-cluster"
      },
      "SecurityGroupIDs": {
        "Type": "CommaDelimitedList",
        "Default": "sg-1234567890abcdef0"
      },
      "SubnetIDs": {
        "Type": "CommaDelimitedList",
        "Default": "subnet-021345abcdef67890,subnet-abcdef01234567890"
      }
    },
    "Resources": {
      "ECSService": {
        "Type": "AWS::ECS::Service",
        "Properties": {
          "Cluster": "endpoint",
          "TaskDefinition": "arn:aws:ecs:us-east-1:111122223333:task-definition/ebs-task-attach-task-def-test:11",
          "LaunchType": "FARGATE",
          "ServiceName": "ebs",
          "SchedulingStrategy": "REPLICA",
          "DesiredCount": 1,
          "NetworkConfiguration": {
            "AwsvpcConfiguration": {
              "AssignPublicIp": "ENABLED",
              "SecurityGroups": {
                "Ref": "SecurityGroupIDs"
              },
              "Subnets": {
                "Ref": "SubnetIDs"
              }
            }
          },
          "PlatformVersion": "LATEST",
          "DeploymentConfiguration": {
            "MaximumPercent": 200,
            "MinimumHealthyPercent": 100,
            "DeploymentCircuitBreaker": {
              "Enable": true,
              "Rollback": true
            }
          },
          "DeploymentController": {
            "Type": "ECS"
          },
          "Tags": [],
          "EnableECSManagedTags": true,
          "VolumeConfigurations": [
            {
              "Name": "ebs-volume",
              "ManagedEBSVolume": {
                "RoleArn": "arn:aws:iam::111122223333:role/ecsInfrastructureRole",
                "VolumeType": "gp3",
                "Iops": "3000",
                "Throughput": "125",
                "SizeInGiB": "10",
                "FilesystemType": "xfs",
                "TagSpecifications": [
                  {
                    "ResourceType": "volume",
                    "PropagateTags": "TASK_DEFINITION"
                  }
                ]
              }
            }
          ]
        }
      }
    },
    "Outputs": {
      "ClusterName": {
        "Description": "The cluster used to create the service.",
        "Value": {
          "Ref": "ECSClusterName"
        }
      },
      "ECSService": {
        "Description": "The created service.",
        "Value": {
          "Ref": "ECSService"
        }
      }
    }
  }
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: The template used to create an ECS Service that includes a volume configuration.
Parameters:
  ECSClusterName:
    Type: String
    Default: volume-config-cluster
  SecurityGroupIDs:
    Type: CommaDelimitedList
    Default: sg-1234567890abcdef0
  SubnetIDs:
    Type: CommaDelimitedList
    Default: subnet-021345abcdef67890,subnet-abcdef01234567890
Resources:
  ECSService:
    Type: AWS::ECS::Service
    Properties:
      Cluster: endpoint
      TaskDefinition: arn:aws:ecs:us-east-1:111122223333:task-definition/ebs-task-attach-task-def-test:11
      LaunchType: FARGATE
      ServiceName: ebs
      SchedulingStrategy: REPLICA
      DesiredCount: 1
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            Ref: SecurityGroupIDs
          Subnets:
            Ref: SubnetIDs
      PlatformVersion: LATEST
      DeploymentConfiguration:
        MaximumPercent: 200
        MinimumHealthyPercent: 100
        DeploymentCircuitBreaker:
          Enable: true
          Rollback: true
      DeploymentController:
        Type: ECS
      Tags: []
      EnableECSManagedTags: true
      VolumeConfigurations:
        - Name: ebs-volume
          ManagedEBSVolume:
            RoleArn: arn:aws:iam::111122223333:role/ecsInfrastructureRole
            VolumeType: gp3
            Iops: "3000"
            Throughput: "125"
            SizeInGiB: "10"
            FilesystemType: xfs
            TagSpecifications:
              - ResourceType: volume
                PropagateTags: TASK_DEFINITION
Outputs:
  ClusterName:
    Description: The cluster used to create the service.
    Value:
      Ref: ECSClusterName
  ECSService:
    Description: The created service.
    Value:
      Ref: ECSService  
```
 

### Associate an Application Load Balancer with a service

The following example associates an Application Load Balancer with an Amazon ECS service by referencing an `AWS::ElasticLoadBalancingV2::TargetGroup` resource. Replace the `SecurityGroupIDs`, `SubnetIDs`, `VpcID`, `Cluster`, and `TaskDefinition` with your own information. For more information about using Application Load Balancers with Amazon ECS, see Use an Application Load Balancer for Amazon ECS in the Amazon ECS Developer Guide.Note

The Amazon ECS service requires an explicit dependency on the Application Load Balancer listener rule and the Application Load Balancer listener. This prevents the service from starting before the listener is ready.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "The template used to create an ECS Service associated with an Application Load Balancer.",
    "Parameters": {
      "SecurityGroupIDs": {
        "Type": "CommaDelimitedList",
        "Default": "sg-1234567890abcdef0,sg-021345abcdef67890"
      },
      "SubnetIDs": {
        "Type": "CommaDelimitedList",
        "Default": "subnet-abcdef01234567890,subnet-fedcba01234567098,subnet-2135647890abcdef0"
      },
      "VpcID": {
        "Type": "String",
        "Default": "vpc-3214789650abcdef0"
      }
    },
    "Resources": {
        "ECSCluster": {
            "Type": "AWS::ECS::Cluster",
            "Properties": {
                "ClusterName": "ALBCluster"
            }
        },
      "ECSService": {
        "Type": "AWS::ECS::Service",
        "Properties": {
          "Cluster": {"Ref":"ECSCluster"},
          "TaskDefinition": "arn:aws:ecs:us-east-1:111122223333:task-definition/first-run-task:7",
          "LaunchType": "FARGATE",
          "ServiceName": "alb",
          "SchedulingStrategy": "REPLICA",
          "DesiredCount": 3,
          "LoadBalancers": [
            {
              "ContainerName": "first-run-task",
              "ContainerPort": 80,
              "LoadBalancerName": {
                "Ref": "AWS::NoValue"
              },
              "TargetGroupArn": {
                "Ref": "TargetGroup"
              }
            }
          ],
          "HealthCheckGracePeriodSeconds": "20",
          "NetworkConfiguration": {
            "AwsvpcConfiguration": {
              "AssignPublicIp": "ENABLED",
              "SecurityGroups": {
                "Ref": "SecurityGroupIDs"
              },
              "Subnets": {
                "Ref": "SubnetIDs"
              }
            }
          },
          "PlatformVersion": "LATEST",
          "DeploymentConfiguration": {
            "MaximumPercent": 200,
            "MinimumHealthyPercent": 100,
            "DeploymentCircuitBreaker": {
              "Enable": true,
              "Rollback": true
            }
          },
          "DeploymentController": {
            "Type": "ECS"
          },
          "ServiceConnectConfiguration": {
            "Enabled": false
          },
          "Tags": [],
          "EnableECSManagedTags": true
        },
        "DependsOn": [
          "Listener"
        ]
      },
      "LoadBalancer": {
        "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "Properties": {
          "Type": "application",
          "Name": "alb-test",
          "SecurityGroups": {
            "Ref": "SecurityGroupIDs"
          },
          "Subnets": {
            "Ref": "SubnetIDs"
          }
        }
      },
      "TargetGroup": {
        "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
        "Properties": {
          "HealthCheckPath": "/",
          "Name": "ecs-task-m-alb",
          "Port": 80,
          "Protocol": "HTTP",
          "TargetType": "ip",
          "HealthCheckProtocol": "HTTP",
          "VpcId": {
            "Ref": "VpcID"
          },
          "TargetGroupAttributes": [
            {
              "Key": "deregistration_delay.timeout_seconds",
              "Value": "300"
            }
          ]
        }
      },
      "Listener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
          "DefaultActions": [
            {
              "Type": "forward",
              "TargetGroupArn": {
                "Ref": "TargetGroup"
              }
            }
          ],
          "LoadBalancerArn": {
            "Ref": "LoadBalancer"
          },
          "Port": 80,
          "Protocol": "HTTP"
        }
      }
    },
    "Outputs": {
      "ClusterName": {
        "Description": "The cluster used to create the service.",
        "Value": {
          "Ref": "ECSCluster"
        }
      },
      "ECSService": {
        "Description": "The created service.",
        "Value": {
          "Ref": "ECSService"
        }
      },
      "LoadBalancer": {
        "Description": "The created load balancer.",
        "Value": {
          "Ref": "LoadBalancer"
        }
      },
      "Listener": {
        "Description": "The created listener.",
        "Value": {
          "Ref": "Listener"
        }
      },
      "TargetGroup": {
        "Description": "The created target group.",
        "Value": {
          "Ref": "TargetGroup"
        }
      }
    }
  }
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: The template used to create an ECS Service associated with an
  Application Load Balancer.
Parameters:
  SecurityGroupIDs:
    Type: CommaDelimitedList
    Default: sg-1234567890abcdef0,sg-021345abcdef67890
  SubnetIDs:
    Type: CommaDelimitedList
    Default: subnet-abcdef01234567890,subnet-fedcba01234567098,subnet-2135647890abcdef0
  VpcID:
    Type: String
    Default: vpc-3214789650abcdef0
Resources:
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: ALBCluster
  ECSService:
    Type: AWS::ECS::Service
    Properties:
      Cluster:
        Ref: ECSCluster
      TaskDefinition: arn:aws:ecs:us-east-1:111122223333:task-definition/first-run-task:7
      LaunchType: FARGATE
      ServiceName: alb
      SchedulingStrategy: REPLICA
      DesiredCount: 3
      LoadBalancers:
        - ContainerName: first-run-task
          ContainerPort: 80
          LoadBalancerName:
            Ref: AWS::NoValue
          TargetGroupArn:
            Ref: TargetGroup
      HealthCheckGracePeriodSeconds: "20"
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            Ref: SecurityGroupIDs
          Subnets:
            Ref: SubnetIDs
      PlatformVersion: LATEST
      DeploymentConfiguration:
        MaximumPercent: 200
        MinimumHealthyPercent: 100
        DeploymentCircuitBreaker:
          Enable: true
          Rollback: true
      DeploymentController:
        Type: ECS
      ServiceConnectConfiguration:
        Enabled: false
      Tags: []
      EnableECSManagedTags: true
    DependsOn:
      - Listener
  LoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Type: application
      Name: alb-test
      SecurityGroups:
        Ref: SecurityGroupIDs
      Subnets:
        Ref: SubnetIDs
  TargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      HealthCheckPath: /
      Name: ecs-task-m-alb
      Port: 80
      Protocol: HTTP
      TargetType: ip
      HealthCheckProtocol: HTTP
      VpcId:
        Ref: VpcID
      TargetGroupAttributes:
        - Key: deregistration_delay.timeout_seconds
          Value: "300"
  Listener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: forward
          TargetGroupArn:
            Ref: TargetGroup
      LoadBalancerArn:
        Ref: LoadBalancer
      Port: 80
      Protocol: HTTP
Outputs:
  ClusterName:
    Description: The cluster used to create the service.
    Value:
      Ref: ECSCluster
  ECSService:
    Description: The created service.
    Value:
      Ref: ECSService
  LoadBalancer:
    Description: The created load balancer.
    Value:
      Ref: LoadBalancer
  Listener:
    Description: The created listener.
    Value:
      Ref: Listener
  TargetGroup:
    Description: The created target group.
    Value:
      Ref: TargetGroup

```
