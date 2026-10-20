> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemon-daemondeploymentconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Daemon DaemonDeploymentConfiguration

Optional deployment parameters that control how a daemon rolls out updates across container instances.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Alarms" : DaemonAlarmConfiguration,
  "BakeTimeInMinutes" : Integer,
  "DrainPercent" : Number
}

```

### YAML

```
  Alarms: 
    DaemonAlarmConfiguration
  BakeTimeInMinutes: Integer
  DrainPercent: Number

```

## Properties

**`Alarms`** 

The CloudWatch alarm configuration for the daemon deployment. When alarms are triggered during a deployment, the deployment can be automatically rolled back. 

Required: No

Type: DaemonAlarmConfiguration

Update requires: No interruption

**`BakeTimeInMinutes`** 

The amount of time (in minutes) to wait after a successful deployment step before proceeding. This allows time to monitor for issues before continuing. The default value is 0. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `1440`

Update requires: No interruption

**`DrainPercent`** 

The percentage of container instances to drain simultaneously during a daemon deployment. Valid values are between 0.0 and 100.0. 

Required: No

Type: Number

Minimum: `0`

Maximum: `100`

Update requires: No interruption
