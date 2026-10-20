> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition

Registers a new task definition from the supplied `family` and `containerDefinitions`. Optionally, you can add data volumes to your containers with the `volumes` parameter. For more information about task definition parameters and defaults, see Amazon ECS Task Definitions in the Amazon Elastic Container Service Developer Guide.

You can specify a role for your task with the `taskRoleArn` parameter. When you specify a role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide.

You can specify a Docker networking mode for the containers in your task definition with the `networkMode` parameter. If you specify the `awsvpc` network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::TaskDefinition",
  "Properties" : {
      "ContainerDefinitions" : [ ContainerDefinition, ... ],
      "Cpu" : String,
      "EnableFaultInjection" : Boolean,
      "EphemeralStorage" : EphemeralStorage,
      "ExecutionRoleArn" : String,
      "Family" : String,
      "IpcMode" : String,
      "Memory" : String,
      "NetworkMode" : String,
      "PidMode" : String,
      "PlacementConstraints" : [ TaskDefinitionPlacementConstraint, ... ],
      "ProxyConfiguration" : ProxyConfiguration,
      "RequiresCompatibilities" : [ String, ... ],
      "RuntimePlatform" : RuntimePlatform,
      "Tags" : [ Tag, ... ],
      "TaskRoleArn" : String,
      "Volumes" : [ Volume, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::TaskDefinition
Properties:
  ContainerDefinitions: 
    - ContainerDefinition
  Cpu: String
  EnableFaultInjection: Boolean
  EphemeralStorage: 
    EphemeralStorage
  ExecutionRoleArn: String
  Family: String
  IpcMode: String
  Memory: String
  NetworkMode: String
  PidMode: String
  PlacementConstraints: 
    - TaskDefinitionPlacementConstraint
  ProxyConfiguration: 
    ProxyConfiguration
  RequiresCompatibilities: 
    - String
  RuntimePlatform: 
    RuntimePlatform
  Tags: 
    - Tag
  TaskRoleArn: String
  Volumes: 
    - Volume

```

## Properties

**`ContainerDefinitions`** 

A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see Amazon ECS Task Definitions in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: Array of ContainerDefinition

Update requires: Replacement

**`Cpu`** 

The number of `cpu` units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the `memory` parameter. 

If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs).  

This field is required for Fargate. For information about the valid values, see Task size in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Update requires: Replacement

**`EnableFaultInjection`** 

Enables fault injection and allows for fault injection requests to be accepted from the task's containers. The default value is `false`. 

Required: No

Type: Boolean

Update requires: Replacement

**`EphemeralStorage`** 

The ephemeral storage settings to use for tasks run with the task definition. 

Required: No

Type: EphemeralStorage

Update requires: Replacement

**`ExecutionRoleArn`** 

The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see IAM roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Update requires: Replacement

**`Family`** 

The name of a family that this task definition is registered to. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. 

A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add. Note

To use revision numbers when you update a task definition, specify this property. If you don't specify a value, AWS CloudFormation generates a new task definition each time that you update it. 

Required: No

Type: String

Update requires: Replacement

**`IpcMode`** 

The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`. If `host` is specified, then all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If `task` is specified, all containers within the specified task share the same IPC resources. If `none` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. 

If the `host` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. 

If you are setting namespaced kernel parameters using `systemControls` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see System Controls in the Amazon Elastic Container Service Developer Guide.  
For tasks that use the `host` IPC mode, IPC namespace related `systemControls` are not supported. 
For tasks that use the `task` IPC mode, IPC namespace related `systemControls` will apply to all containers within a task. 
 Note

This parameter is not supported for Windows containers or tasks run on AWS Fargate. 

Required: No

Type: String

Allowed values: `host | task | none`

Update requires: Replacement

**`Memory`** 

The amount (in MiB) of memory used by the task. 

If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see ContainerDefinition. 

If your tasks runs on AWS Fargate, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the `cpu` parameter.  
512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU) 
1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU) 
2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU) 
Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU) 
Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU) 
Between 16 GB and 60 GB in 4 GB increments - Available `cpu` values: 8192 (8 vCPU) 

This option requires Linux platform `1.4.0` or later. 
Between 32GB and 120 GB in 8 GB increments - Available `cpu` values: 16384 (16 vCPU) 

This option requires Linux platform `1.4.0` or later. 
 

Required: No

Type: String

Update requires: Replacement

**`NetworkMode`** 

The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`. If no network mode is specified, the default is `bridge`. 

For Amazon ECS tasks on Fargate, the `awsvpc` network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, `<default>` or `awsvpc` can be used. If the network mode is set to `none`, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The `host` and `awsvpc` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the `bridge` mode. 

With the `host` and `awsvpc` network modes, exposed container ports are mapped directly to the corresponding host port (for the `host` network mode) or the attached elastic network interface port (for the `awsvpc` network mode), so you cannot take advantage of dynamic host port mappings.  Important

When using the `host` network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user. 

If the network mode is `awsvpc`, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide. 

If the network mode is `host`, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used. 

Required: No

Type: String

Allowed values: `bridge | host | awsvpc | none`

Update requires: Replacement

**`PidMode`** 

The process namespace to use for the containers in the task. The valid values are `host` or `task`. On Fargate for Linux containers, the only valid value is `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task. 

If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance. 

If `task` is specified, all containers within the specified task share the same process namespace. 

If no value is specified, the The default is a private namespace for each container. 

If the `host` PID mode is used, there's a heightened risk of undesired process namespace exposure. Note

This parameter is not supported for Windows containers. Note

This parameter is only supported for tasks that are hosted on AWS Fargate if the tasks are using platform version `1.4.0` or later (Linux). This isn't supported for Windows containers on Fargate. 

Required: No

Type: String

Allowed values: `host | task`

Update requires: Replacement

**`PlacementConstraints`** 

An array of placement constraint objects to use for tasks. Note

This parameter isn't supported for tasks run on AWS Fargate. 

Required: No

Type: Array of TaskDefinitionPlacementConstraint

Update requires: Replacement

**`ProxyConfiguration`** 

The configuration details for the App Mesh proxy. 

Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the `ecs-init` package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version `20190301` or later, they contain the required versions of the container agent and `ecs-init`. For more information, see Amazon ECS-optimized Linux AMI in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: ProxyConfiguration

Update requires: Replacement

**`RequiresCompatibilities`** 

The task launch types the task definition was validated against. The valid values are `MANAGED_INSTANCES`, `EC2`, `FARGATE`, and `EXTERNAL`. For more information, see Amazon ECS launch types in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: Array of String

Update requires: Replacement

**`RuntimePlatform`** 

The operating system that your tasks definitions run on. 

Required: No

Type: RuntimePlatform

Update requires: Replacement

**`Tags`** 

The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them. 

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

**`TaskRoleArn`** 

The short name or full Amazon Resource Name (ARN) of the AWS Identity and Access Management role that grants containers in the task permission to call AWS APIs on your behalf. For more information, see Amazon ECS Task Role in the Amazon Elastic Container Service Developer Guide. 

IAM roles for tasks on Windows require that the `-EnableTaskIAMRole` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code to use the feature. For more information, see Windows IAM roles for tasks in the Amazon Elastic Container Service Developer Guide. Note

String validation is done on the ECS side. If an invalid string value is given for `TaskRoleArn`, it may cause the Cloudformation job to hang. 

Required: No

Type: String

Update requires: Replacement

**`Volumes`** 

The list of data volume definitions for the task. For more information, see Using data volumes in tasks in the Amazon Elastic Container Service Developer Guide. Note

The `host` and `sourcePath` parameters aren't supported for tasks run on AWS Fargate.  

Required: No

Type: Array of Volume

Update requires: Replacement

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN).

In the following example, the `Ref` function returns the ARN of the `MyTaskDefinition` task definition, such as `arn:aws:ecs:us-west-2:123456789012:task-definition/TaskDefinitionFamily:1`.

 `{ "Ref": "MyTaskDefinition" }` 

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

#### 

**`TaskDefinitionArn`** 

The ARN of the task definition. 

## Examples
Create a task definition with 2 containers
Create a task definition that can be used for both the Fargate and the EC2 launch types
Create an Amazon ECS task definition with an Amazon EFS volume
 

### Create a task definition with 2 containers

The following example defines an Amazon ECS task definition, which includes two container definitions and one volume definition.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "taskdefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ContainerDefinitions": [
          {
            "Name": "AppName",
            "MountPoints": [
              {
                "SourceVolume": "my-vol",
                "ContainerPath": "/var/www/my-vol"
              }
            ],
            "Image": "amazon/amazon-ecs-sample",
            "Cpu": 256,
            "PortMappings": [
              {
                "ContainerPort": 80,
                "HostPort": 80,
                "Protocol": "tcp"
              }
            ],
            "EntryPoint": ["/usr/sbin/apache2", "-D", "FOREGROUND"],
            "Memory": 512,
            "Essential": true
          },
          {
            "Name": "busybox",
            "Image": "busybox",
            "Cpu": 256,
            "EntryPoint": ["sh", "-c"],
            "Memory": 512,
            "Command": [
              "/bin/sh -c \"while true; do /bin/date > /var/www/my-vol/date; sleep 1; done\""
            ],
            "Essential": false,
            "VolumesFrom": [
              {
                "SourceContainer": "AppName"
              }
            ]
          }
        ],
        "Volumes": [
          {
            "Host": {
              "SourcePath": "/var/lib/docker/vfs/dir/"
            },
            "Name": "my-vol"
          }
        ]
      }
    }
  }
}

```

#### YAML

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  taskdefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      ContainerDefinitions:
        - Name: AppName
          MountPoints:
            - SourceVolume: my-vol
              ContainerPath: "/var/www/my-vol"
          Image: amazon/amazon-ecs-sample
          Cpu: 256
          PortMappings:
            - ContainerPort: 80
              HostPort: 80
              Protocol: tcp
          EntryPoint:
            - "/usr/sbin/apache2"
            - "-D"
            - FOREGROUND
          Memory: 512
          Essential: true
        - Name: busybox
          Image: busybox
          Cpu: 256
          EntryPoint:
            - sh
            - "-c"
          Memory: 512
          Command:
            - "/bin/sh"
            - "-c"
            - "while true; do /bin/date > /var/www/my-vol/date; sleep 1; done"
          Essential: false
          VolumesFrom:
            - SourceContainer: AppName
      Volumes:
        - Host:
            SourcePath: "/var/lib/docker/vfs/dir/"
          Name: my-vol

```
 

### Create a task definition that can be used for both the Fargate and the EC2 launch types

The following is an example task definition using a Linux container that sets up a web server and is tagged with the key `environment` and the value `webserver`. This task definition is compatible across both the Fargate and EC2 launch types.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Create a task definition for a web server.",
  "Resources": {
    "ECSTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ContainerDefinitions": [
          {
            "Name": "first-run-task",
            "Image": "public.ecr.aws/docker/library/httpd:2.4",
            "Essential": true,
            "PortMappings": [
              {
                "ContainerPort": 80,
                "Protocol": "tcp"
              }
            ],
             "EntryPoint": ["sh", "-c"],
             "Command":[
              "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
            ]
          }
        ],
        "Family": "first-run-task",
        "Cpu": "1 vCPU",
        "Memory": "3 GB",
        "NetworkMode": "awsvpc",
        "RequiresCompatibilities": ["EC2","FARGATE"],
         "Tags": [
            {
                "Key": "environment",
                "Value": "webserver"
            }
        ]
      }
    }
  },
  "Outputs": {
    "ECSTaskDefinition": {
      "Description": "The created Taskdefinition.",
      "Value": {
        "Ref": "ECSTaskDefinition"
      }
    }
  }
}          
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: Create a task definition for a web server.
Resources:
  ECSTaskDefinition:
    Type: 'AWS::ECS::TaskDefinition'
    Properties:
      ContainerDefinitions:
        - Name: first-run-task
          Image: 'public.ecr.aws/docker/library/httpd:2.4'
          Essential: true
          PortMappings:
            - ContainerPort: 80
              Protocol: tcp
          EntryPoint:
            - sh
            - -c
          Command:
            -   "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample
                App</title> <style>body {margin-top: 40px; background-color:
                #333;} </style> </head><body> <div
                style=color:white;text-align:center> <h1>Amazon ECS Sample
                App</h1> <h2>Congratulations!</h2> <p>Your application is now
                running on a container in Amazon ECS.</p> </div></body></html>'
                >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
      Family: first-run-task
      Cpu: 1 vCPU
      Memory: 3 GB
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - EC2
        - FARGATE
      Tags:
        - Key: environment
          Value: webserver
Outputs:
  ECSTaskDefinition:
    Description: The created Taskdefinition.
    Value: !Ref ECSTaskDefinition        
```
 

### Create an Amazon ECS task definition with an Amazon EFS volume

The following example defines an Amazon ECS task definition that uses an Amazon EFS volume. Replace the `ExecutionRoleArn` and `FileSystemId` with your own values. For more information about using Amazon EFS volumes with Amazon ECS, see Use Amazon EFS volumes with Amazon ECS in the Amazon ECS Developer Guide.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Create a task definition for a web server.",
    "Resources": {
      "ECSTaskDefinition": {
        "Type": "AWS::ECS::TaskDefinition",
        "Properties": {
          "ExecutionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
          "NetworkMode": "awsvpc",
          "RequiresCompatibilities": ["FARGATE"],
          "Family": "my-ecs-task",
          "Cpu": "256",
          "Memory": "512",
          "ContainerDefinitions": [
            {
              "Name": "nginx",
              "Image": "public.ecr.aws/nginx/nginx:latest",
              "Essential": true,
              "PortMappings": [
                {
                  "ContainerPort": 80,
                  "Protocol": "tcp"
                }
              ],
              "LinuxParameters": {
                "InitProcessEnabled": true
              },
              "MountPoints": [
                {
                  "SourceVolume": "efs-volume",
                  "ContainerPath": "/usr/share/nginx/html"
                }
            ],
                "LogConfiguration": {
                  "LogDriver": "awslogs",
                    "Options": {
                      "mode": "non-blocking",
                      "max-buffer-size": "25m",
                      "awslogs-group": "LogGroup",
                      "awslogs-region": "us-east-1",
                      "awslogs-create-group": "true",
                      "awslogs-stream-prefix": "efs-task"
                    }
                }
            }
        ],
          "Volumes": [
            {
              "Name": "efs-volume",
              "EFSVolumeConfiguration": {
                "FilesystemId": "fs-1234567890abcdef0",
                "RootDirectory": "/",
                "TransitEncryption": "ENABLED"
              }
          }
        ]
        }
      }
    }
  }
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: Create a task definition for a web server.
Resources:
  ECSTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      ExecutionRoleArn: arn:aws:iam::123456789012:role/ecsTaskExecutionRole
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      Family: my-ecs-task
      Cpu: "256"
      Memory: "512"
      ContainerDefinitions:
        - Name: nginx
          Image: public.ecr.aws/nginx/nginx:latest
          Essential: true
          PortMappings:
            - ContainerPort: 80
              Protocol: tcp
          LinuxParameters:
            InitProcessEnabled: true
          MountPoints:
            - SourceVolume: efs-volume
              ContainerPath: /usr/share/nginx/html
          LogConfiguration:
            LogDriver: awslogs
            Options:
              mode: non-blocking
              max-buffer-size: 25m
              awslogs-group: LogGroup
              awslogs-region: us-east-1
              awslogs-create-group: "true"
              awslogs-stream-prefix: efs-task
      Volumes:
        - Name: efs-volume
          EFSVolumeConfiguration:
            FilesystemId: fs-1234567890abcdef0
            RootDirectory: /
            TransitEncryption: ENABLED

```
