> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition S3FilesVolumeConfiguration

This parameter is specified when you're using an Amazon S3 Files file system for task storage. For more information, see Amazon S3 Files volumes in the Amazon Elastic Container Service Developer Guide.Important

Your task definition must include a Task IAM Role. See  IAM role for attaching your file system to AWS compute resources for required permissions.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AccessPointArn" : String,
  "FileSystemArn" : String,
  "RootDirectory" : String,
  "TransitEncryptionPort" : Integer
}

```

### YAML

```
  AccessPointArn: String
  FileSystemArn: String
  RootDirectory: String
  TransitEncryptionPort: Integer

```

## Properties

**`AccessPointArn`** 

The full ARN of the S3 Files access point to use. If an access point is specified, the root directory value specified in the `S3FilesVolumeConfiguration` must either be omitted or set to `/` which will enforce the path set on the S3 Files access point. For more information, see Creating S3 Files access points. 

Required: No

Type: String

Update requires: Replacement

**`FileSystemArn`** 

The full ARN of the S3 Files file system to mount. 

Required: Yes

Type: String

Update requires: Replacement

**`RootDirectory`** 

The directory within the Amazon S3 Files file system to mount as the root directory. If this parameter is omitted, the root of the Amazon S3 Files file system will be used. Specifying `/` will have the same effect as omitting this parameter. Important

If a S3 Files access point is specified in the `accessPointArn`, the root directory parameter must either be omitted or set to `/` which will enforce the path set on the S3 Files access point. 

Required: No

Type: String

Update requires: Replacement

**`TransitEncryptionPort`** 

The port to use for sending encrypted data between the ECS host and the S3 Files file system. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon S3 Files mount helper uses. For more information, see S3 Files mount helper. 

Required: No

Type: Integer

Update requires: Replacement
