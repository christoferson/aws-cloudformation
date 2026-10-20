> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-volumefrom.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition VolumeFrom

Details on a data volume from another container in the same task definition.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReadOnly" : Boolean,
  "SourceContainer" : String
}

```

### YAML

```
  ReadOnly: Boolean
  SourceContainer: String

```

## Properties

**`ReadOnly`** 

If this value is `true`, the container has read-only access to the volume. If this value is `false`, then the container can write to the volume. The default value is `false`. 

Required: No

Type: Boolean

Update requires: Replacement

**`SourceContainer`** 

The name of another container within the same task definition to mount volumes from. 

Required: No

Type: String

Update requires: Replacement
