> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-autorepairconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider AutoRepairConfiguration

The auto repair configuration for an Amazon ECS Managed Instances capacity provider. When enabled, Amazon ECS automatically replaces container instances that are detected as unhealthy based on container instance health checks, including accelerated compute device and daemon health checks.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ActionsStatus" : String
}

```

### YAML

```
  ActionsStatus: String

```

## Properties

**`ActionsStatus`** 

The status of auto repair actions for the capacity provider. When set to `ENABLED`, Amazon ECS automatically replaces container instances with an `IMPAIRED` health status. When set to `DISABLED`, Amazon ECS still monitors container instance health but does not automatically replace impaired instances. 

Required: No

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: No interruption
