> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-device.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition Device

An object representing a container instance host device.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContainerPath" : String,
  "HostPath" : String,
  "Permissions" : [ String, ... ]
}

```

### YAML

```
  ContainerPath: String
  HostPath: String
  Permissions: 
    - String

```

## Properties

**`ContainerPath`** 

The path inside the container at which to expose the host device. 

Required: No

Type: String

Update requires: Replacement

**`HostPath`** 

The path for the device on the host container instance. 

Required: No

Type: String

Update requires: Replacement

**`Permissions`** 

The explicit permissions to provide to the container for the device. By default, the container has permissions for `read`, `write`, and `mknod` for the device. 

Required: No

Type: Array of String

Update requires: Replacement
