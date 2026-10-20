> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-daemontaskdefinition.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition

The details of a daemon task definition. A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents independently across your Amazon ECS infrastructure.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::DaemonTaskDefinition",
  "Properties" : {
      "ContainerDefinitions" : [ DaemonContainerDefinition, ... ],
      "Cpu" : String,
      "ExecutionRoleArn" : String,
      "Family" : String,
      "IpcMode" : String,
      "Memory" : String,
      "PidMode" : String,
      "Tags" : [ Tag, ... ],
      "TaskRoleArn" : String,
      "Volumes" : [ Volume, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::DaemonTaskDefinition
Properties:
  ContainerDefinitions: 
    - DaemonContainerDefinition
  Cpu: String
  ExecutionRoleArn: String
  Family: String
  IpcMode: String
  Memory: String
  PidMode: String
  Tags: 
    - Tag
  TaskRoleArn: String
  Volumes: 
    - Volume

```

## Properties

**`ContainerDefinitions`** 

A list of container definitions in JSON format that describe the containers that make up the daemon task. 

Required: No

Type: Array of DaemonContainerDefinition

Update requires: Replacement

**`Cpu`** 

The number of CPU units used by the daemon task. 

Required: No

Type: String

Update requires: Replacement

**`ExecutionRoleArn`** 

The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. 

Required: No

Type: String

Update requires: Replacement

**`Family`** 

The name of a family that this daemon task definition is registered to. 

Required: No

Type: String

Update requires: Replacement

**`IpcMode`** 

The IPC namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`. 

If `none` is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use `ipcMode: "host"` or other daemons that use `ipcMode: "shared"`. 

Required: No

Type: String

Allowed values: `none | shared`

Update requires: Replacement

**`Memory`** 

The amount of memory (in MiB) used by the daemon task. 

Required: No

Type: String

Update requires: Replacement

**`PidMode`** 

The PID namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`. 

If `none` is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use `pidMode: "host"` or other daemons that use `pidMode: "shared"`. 

Required: No

Type: String

Allowed values: `none | shared`

Update requires: Replacement

**`Tags`**

Property description not available.

Required: No

Type: Array of Tag

Update requires: No interruption

**`TaskRoleArn`** 

The short name or full Amazon Resource Name (ARN) of the IAM role that grants containers in the daemon task permission to call Amazon Web Services APIs on your behalf. 

Required: No

Type: String

Update requires: Replacement

**`Volumes`** 

The list of data volume definitions for the daemon task. 

Required: No

Type: Array of Volume

Update requires: Replacement

## Return values

### Ref

### Fn::GetAtt

#### 

**`DaemonTaskDefinitionArn`** 

The full Amazon Resource Name (ARN) of the daemon task definition.
