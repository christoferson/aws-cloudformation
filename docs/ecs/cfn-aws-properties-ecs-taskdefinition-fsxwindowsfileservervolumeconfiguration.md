> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition FSxWindowsFileServerVolumeConfiguration

This parameter is specified when you're using Amazon FSx for Windows File Server file system for task storage.

For more information and the input format, see Amazon FSx for Windows File Server volumes in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AuthorizationConfig" : FSxAuthorizationConfig,
  "FileSystemId" : String,
  "RootDirectory" : String
}

```

### YAML

```
  AuthorizationConfig: 
    FSxAuthorizationConfig
  FileSystemId: String
  RootDirectory: String

```

## Properties

**`AuthorizationConfig`** 

The authorization configuration details for the Amazon FSx for Windows File Server file system. 

Required: No

Type: FSxAuthorizationConfig

Update requires: Replacement

**`FileSystemId`** 

The Amazon FSx for Windows File Server file system ID to use. 

Required: Yes

Type: String

Update requires: Replacement

**`RootDirectory`** 

The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host. 

Required: Yes

Type: String

Update requires: Replacement
