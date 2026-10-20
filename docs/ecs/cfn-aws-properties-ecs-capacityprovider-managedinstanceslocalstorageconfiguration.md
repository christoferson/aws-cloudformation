> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider ManagedInstancesLocalStorageConfiguration

The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses and configures instance store volumes available on container instance.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "UseLocalStorage" : Boolean
}

```

### YAML

```
  UseLocalStorage: Boolean

```

## Properties

**`UseLocalStorage`** 

Use instance store volumes for data storage when available. EBS volumes are not provisioned for data storage. If the container instance has multiple instance store volumes, a single data volume is created. Consider defining instance store requirements using the `localStorage`, `localStorageTypes` and `totalLocalStorageGB` properties. 

Required: No

Type: Boolean

Update requires: No interruption
