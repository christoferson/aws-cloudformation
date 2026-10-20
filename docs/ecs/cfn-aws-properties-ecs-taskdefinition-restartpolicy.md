> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-restartpolicy.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition RestartPolicy

You can enable a restart policy for each container defined in your task definition, to overcome transient failures faster and maintain task availability. When you enable a restart policy for a container, Amazon ECS can restart the container if it exits, without needing to replace the task. For more information, see Restart individual containers in Amazon ECS tasks with container restart policies in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Enabled" : Boolean,
  "IgnoredExitCodes" : [ Integer, ... ],
  "RestartAttemptPeriod" : Integer
}

```

### YAML

```
  Enabled: Boolean
  IgnoredExitCodes: 
    - Integer
  RestartAttemptPeriod: Integer

```

## Properties

**`Enabled`** 

Specifies whether a restart policy is enabled for the container. 

Required: No

Type: Boolean

Update requires: Replacement

**`IgnoredExitCodes`** 

A list of exit codes that Amazon ECS will ignore and not attempt a restart on. You can specify a maximum of 50 container exit codes. By default, Amazon ECS does not ignore any exit codes. 

Required: No

Type: Array of Integer

Update requires: Replacement

**`RestartAttemptPeriod`** 

A period of time (in seconds) that the container must run for before a restart can be attempted. A container can be restarted only once every `restartAttemptPeriod` seconds. If a container isn't able to run for this time period and exits early, it will not be restarted. You can set a minimum `restartAttemptPeriod` of 60 seconds and a maximum `restartAttemptPeriod` of 1800 seconds. By default, a container must run for 300 seconds before it can be restarted. 

Required: No

Type: Integer

Update requires: Replacement
