> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-authorizationconfig.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition AuthorizationConfig

The authorization configuration details for the Amazon EFS file system.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AccessPointId" : String,
  "IAM" : String
}

```

### YAML

```
  AccessPointId: String
  IAM: String

```

## Properties

**`AccessPointId`** 

The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which will enforce the path set on the EFS access point. If an access point is used, transit encryption must be on in the `EFSVolumeConfiguration`. For more information, see Working with Amazon EFS access points in the Amazon Elastic File System User Guide. 

Required: No

Type: String

Update requires: Replacement

**`IAM`** 

Determines whether to use the Amazon ECS task role defined in a task definition when mounting the Amazon EFS file system. If it is turned on, transit encryption must be turned on in the `EFSVolumeConfiguration`. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see Using Amazon EFS access points in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: Replacement
