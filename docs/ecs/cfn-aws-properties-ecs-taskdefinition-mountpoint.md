> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-mountpoint.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition MountPoint

The details for a volume mount point that's used in a container definition.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContainerPath" : String,
  "ReadOnly" : Boolean,
  "SourceVolume" : String
}

```

### YAML

```
  ContainerPath: String
  ReadOnly: Boolean
  SourceVolume: String

```

## Properties

**`ContainerPath`** 

The path on the container to mount the host volume at. 

Required: No

Type: String

Update requires: Replacement

**`ReadOnly`** 

If this value is `true`, the container has read-only access to the volume. If this value is `false`, then the container can write to the volume. The default value is `false`. 

Required: No

Type: Boolean

Update requires: Replacement

**`SourceVolume`** 

The name of the volume to mount. Must be a volume name referenced in the `name` parameter of task definition `volume`. 

Required: No

Type: String

Update requires: Replacement
