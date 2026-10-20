> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition EFSVolumeConfiguration

This parameter is specified when you're using an Amazon Elastic File System file system for task storage. For more information, see Amazon EFS volumes in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AuthorizationConfig" : AuthorizationConfig,
  "FilesystemId" : String,
  "RootDirectory" : String,
  "TransitEncryption" : String,
  "TransitEncryptionPort" : Integer
}

```

### YAML

```
  AuthorizationConfig: 
    AuthorizationConfig
  FilesystemId: String
  RootDirectory: String
  TransitEncryption: String
  TransitEncryptionPort: Integer

```

## Properties

**`AuthorizationConfig`** 

The authorization configuration details for the Amazon EFS file system. 

Required: No

Type: AuthorizationConfig

Update requires: Replacement

**`FilesystemId`** 

The Amazon EFS file system ID to use. 

Required: Yes

Type: String

Update requires: Replacement

**`RootDirectory`** 

The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying `/` will have the same effect as omitting this parameter. Important

If an EFS access point is specified in the `authorizationConfig`, the root directory parameter must either be omitted or set to `/` which will enforce the path set on the EFS access point. 

Required: No

Type: String

Update requires: Replacement

**`TransitEncryption`** 

Determines whether to use encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be turned on if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see Encrypting data in transit in the Amazon Elastic File System User Guide. 

Required: No

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: Replacement

**`TransitEncryptionPort`** 

The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses. For more information, see EFS mount helper in the Amazon Elastic File System User Guide. 

Required: No

Type: Integer

Update requires: Replacement
