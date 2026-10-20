> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskSet

Create a task set in the specified cluster and service. This is used when a service uses the `EXTERNAL` deployment controller type. For more information, see Amazon ECS deployment types in the Amazon Elastic Container Service Developer Guide.Note

On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

For information about the maximum number of task sets and other quotas, see Amazon ECS service quotas in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::TaskSet",
  "Properties" : {
      "CapacityProviderStrategy" : [ CapacityProviderStrategyItem, ... ],
      "Cluster" : String,
      "ExternalId" : String,
      "LaunchType" : String,
      "LoadBalancers" : [ LoadBalancer, ... ],
      "NetworkConfiguration" : NetworkConfiguration,
      "PlatformVersion" : String,
      "Scale" : Scale,
      "Service" : String,
      "ServiceRegistries" : [ ServiceRegistry, ... ],
      "Tags" : [ Tag, ... ],
      "TaskDefinition" : String
    }
}

```

### YAML

```
Type: AWS::ECS::TaskSet
Properties:
  CapacityProviderStrategy: 
    - CapacityProviderStrategyItem
  Cluster: String
  ExternalId: String
  LaunchType: String
  LoadBalancers: 
    - LoadBalancer
  NetworkConfiguration: 
    NetworkConfiguration
  PlatformVersion: String
  Scale: 
    Scale
  Service: String
  ServiceRegistries: 
    - ServiceRegistry
  Tags: 
    - Tag
  TaskDefinition: String

```

## Properties

**`CapacityProviderStrategy`** 

The capacity provider strategy that are associated with the task set. 

Required: No

Type: Array of CapacityProviderStrategyItem

Update requires: Replacement

**`Cluster`** 

The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in. 

Required: Yes

Type: String

Update requires: Replacement

**`ExternalId`** 

An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the `ECS_TASK_SET_EXTERNAL_ID`AWS Cloud Map attribute set to the provided value. 

Required: No

Type: String

Update requires: Replacement

**`LaunchType`** 

The launch type that new tasks in the task set uses. For more information, see Amazon ECS launch types in the Amazon Elastic Container Service Developer Guide. 

If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted. 

Required: No

Type: String

Allowed values: `EC2 | FARGATE`

Update requires: Replacement

**`LoadBalancers`** 

A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer. 

Required: No

Type: Array of LoadBalancer

Update requires: Replacement

**`NetworkConfiguration`** 

The network configuration for the task set. 

Required: No

Type: NetworkConfiguration

Update requires: Replacement

**`PlatformVersion`** 

The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the `LATEST` platform version is used. 

Required: No

Type: String

Update requires: Replacement

**`Scale`** 

A floating-point percentage of your desired number of tasks to place and keep running in the task set. 

Required: No

Type: Scale

Update requires: No interruption

**`Service`** 

The short name or full Amazon Resource Name (ARN) of the service to create the task set in. 

Required: Yes

Type: String

Update requires: Replacement

**`ServiceRegistries`** 

The details of the service discovery registries to assign to this task set. For more information, see Service discovery. 

Required: No

Type: Array of ServiceRegistry

Update requires: Replacement

**`Tags`** 

The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. 

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

The task definition for the tasks in the task set to use. If a revision isn't specified, the latest `ACTIVE` revision is used. 

Required: Yes

Type: String

Update requires: Replacement

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Id`** 

The ID of the task set. 

## Examples

 

### Create an Amazon ECS task set

This template defines a task definition, a cluster, a service, and a task set. The task set uses the specified task definition and is created in the specified cluster and service. Replace the `ExecutionRoleArn`, `SecurityGroups`, and `Subnets` with your own information.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "deployment-cluster"
      }
    },
    "ECSService": {
      "Type": "AWS::ECS::Service",
      "Properties": {
        "ServiceName": "deployment-service",
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "DesiredCount": 2,
        "DeploymentController": {
          "Type": "EXTERNAL"
        }
      }
    },
    "ECSTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ContainerDefinitions": [
          {
            "Command": [
             "/bin/sh -c \"echo '<html> <head> <title>Amazon
              ECS Sample App</title> <style>body {margin-top: 40px;
              background-color: #333;} </style> </head><body>
              <div style=color:white;text-align:center> <h1>Amazon
              ECS Sample App</h1> <h2>Congratulations!</h2>
              <p>Your application is now running on a container in Amazon
              ECS.</p> </div></body></html>'
              >  /usr/local/apache2/htdocs/index.html &&
              httpd-foreground\""
            ],
            "EntryPoint": ["sh", "-c"],
            "Essential": true,
            "Image": "public.ecr.aws/docker/library/httpd:2.4",
            "LogConfiguration": {
              "LogDriver": "awslogs",
              "Options": {
                "awslogs-group": "/ecs/deployment",
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
        "Family": "deployment-task",
        "Memory": 512,
        "NetworkMode": "awsvpc",
        "RequiresCompatibilities": ["FARGATE"],
        "RuntimePlatform": {
          "OperatingSystemFamily": "LINUX"
        }
      }
    },
    "ECSTaskSet": {
      "Type": "AWS::ECS::TaskSet",
      "Properties": {
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "LaunchType": "FARGATE",
        "NetworkConfiguration": {
          "AwsVpcConfiguration": {
            "AssignPublicIp": "ENABLED",
            "SecurityGroups": ["sg-abcdef01234567890"],
            "Subnets": ["subnet-021345abcdef67890"]
          }
        },
        "PlatformVersion": "1.4.0",
        "Scale": {
          "Unit": "PERCENT",
          "Value": 100
        },
        "Service": {
          "Ref": "ECSService"
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
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: deployment-cluster
  ECSService:
    Type: AWS::ECS::Service
    Properties:
      ServiceName: deployment-service
      Cluster:
        Ref: ECSCluster
      DesiredCount: 2
      DeploymentController:
        Type: EXTERNAL
  ECSTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      ContainerDefinitions:
        - Command:
            - "/bin/sh -c \"echo '<html> <head> <title>Amazon
              ECS Sample App</title> <style>body {margin-top: 40px;
              background-color: #333;} </style> </head><body>
              <div style=color:white;text-align:center> <h1>Amazon
              ECS Sample App</h1> <h2>Congratulations!</h2>
              <p>Your application is now running on a container in Amazon
              ECS.</p> </div></body></html>'
              >  /usr/local/apache2/htdocs/index.html &&
              httpd-foreground\""
          EntryPoint:
            - sh
            - -c
          Essential: true
          Image: 'public.ecr.aws/docker/library/httpd:2.4'
          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: /ecs/deployment
              awslogs-region: us-east-1
              awslogs-stream-prefix: ecs
          Name: sample-fargate-app
          PortMappings:
            - ContainerPort: 80
              HostPort: 80
              Protocol: tcp
      Cpu: 256
      ExecutionRoleArn: arn:aws:iam::111122223333:role/ecsTaskExecutionRole
      Family: deployment-task
      Memory: 512
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      RuntimePlatform:
        OperatingSystemFamily: LINUX
  ECSTaskSet:
    Type: AWS::ECS::TaskSet
    Properties:
      Cluster:
        Ref: ECSCluster
      LaunchType: FARGATE
      NetworkConfiguration:
        AwsVpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            - sg-abcdef01234567890
          Subnets:
            - subnet-abcdef01234567890
      PlatformVersion: 1.4.0
      Scale:
        Unit: PERCENT
        Value: 50
      Service:
        Ref: ECSService
      TaskDefinition:
        Ref: ECSTaskDefinition
```
