> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider ManagedInstancesStorageConfiguration

The storage configuration for Amazon ECS Managed Instances. This defines the data volume configuration for the instances.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "StorageSizeGiB" : Integer
}

```

### YAML

```
  StorageSizeGiB: Integer

```

## Properties

**`StorageSizeGiB`** 

The size of the data volume. 

Required: Yes

Type: Integer

Minimum: `1`

Update requires: No interruption
