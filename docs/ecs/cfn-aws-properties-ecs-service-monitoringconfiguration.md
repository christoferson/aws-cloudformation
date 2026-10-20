> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-monitoringconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service MonitoringConfiguration

The optional monitoring configuration for a service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MetricConfigurations" : [ MetricConfiguration, ... ]
}

```

### YAML

```
  MetricConfigurations: 
    - MetricConfiguration

```

## Properties

**`MetricConfigurations`** 

The list of metric configurations for the service monitoring. 

Required: Yes

Type: Array of MetricConfiguration

Minimum: `1`

Maximum: `2`

Update requires: No interruption
