> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-executecommandlogconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Cluster ExecuteCommandLogConfiguration

The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CloudWatchEncryptionEnabled" : Boolean,
  "CloudWatchLogGroupName" : String,
  "S3BucketName" : String,
  "S3EncryptionEnabled" : Boolean,
  "S3KeyPrefix" : String
}

```

### YAML

```
  CloudWatchEncryptionEnabled: Boolean
  CloudWatchLogGroupName: String
  S3BucketName: String
  S3EncryptionEnabled: Boolean
  S3KeyPrefix: String

```

## Properties

**`CloudWatchEncryptionEnabled`** 

Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off. 

Required: No

Type: Boolean

Update requires: No interruption

**`CloudWatchLogGroupName`** 

The name of the CloudWatch log group to send logs to. Note

The CloudWatch log group must already be created. 

Required: No

Type: String

Update requires: No interruption

**`S3BucketName`** 

The name of the S3 bucket to send logs to. Note

The S3 bucket must already be created. 

Required: No

Type: String

Update requires: No interruption

**`S3EncryptionEnabled`** 

Determines whether to use encryption on the S3 logs. If not specified, encryption is not used. 

Required: No

Type: Boolean

Update requires: No interruption

**`S3KeyPrefix`** 

An optional folder in the S3 bucket to place logs in. 

Required: No

Type: String

Update requires: No interruption

## See also 
  Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined
