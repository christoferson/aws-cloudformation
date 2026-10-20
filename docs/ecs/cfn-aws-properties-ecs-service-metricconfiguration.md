> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-metricconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service MetricConfiguration

The configuration for a specific set of metrics to collect for a service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "MetricNames" : [ String, ... ],
  "ResolutionSeconds" : Integer
}

```

### YAML

```
  MetricNames: 
    - String
  ResolutionSeconds: Integer

```

## Properties

**`MetricNames`** 

The list of metric names to configure. The supported metric names are `CPUUtilization` and `MemoryUtilization`. 

Required: Yes

Type: Array of String

Allowed values: `CPUUtilization | MemoryUtilization`

Minimum: `1`

Maximum: `2`

Update requires: No interruption

**`ResolutionSeconds`** 

The resolution, in seconds, at which to collect the metrics. The valid values are `20` and `60`. 

Required: Yes

Type: Integer

Allowed values: `20 | 60`

Update requires: No interruption
