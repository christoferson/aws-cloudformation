> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemon-daemonalarmconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Daemon DaemonAlarmConfiguration

The CloudWatch alarm configuration for a daemon. When enabled, CloudWatch alarms determine whether a daemon deployment has failed.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlarmNames" : [ String, ... ],
  "Enable" : Boolean
}

```

### YAML

```
  AlarmNames: 
    - String
  Enable: Boolean

```

## Properties

**`AlarmNames`** 

The CloudWatch alarm names to monitor during a daemon deployment. 

Required: No

Type: Array of String

Update requires: No interruption

**`Enable`** 

Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is `false`. 

Required: No

Type: Boolean

Update requires: No interruption
