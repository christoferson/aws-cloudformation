> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-s3location.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook S3Location

Specifies the S3 location where your Guard rules or input parameters are located.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Uri" : String,
  "VersionId" : String
}

```

### YAML

```
  Uri: String
  VersionId: String

```

## Properties

**`Uri`** 

Specifies the S3 path to the file that contains your Guard rules or input parameters (in the form `s3://<bucket name>/<file name>`). 

For Guard rules, the object stored in S3 must have one of the following file extensions: `.guard`, `.zip`, or `.tar.gz`. 

For input parameters, the object stored in S3 must have one of the following file extensions: `.yaml`, `.json`, `.zip`, or `.tar.gz`. 

Required: Yes

Type: String

Update requires: No interruption

**`VersionId`** 

For S3 buckets with versioning enabled, specifies the unique ID of the S3 object version to download your Guard rules or input parameters from. 

The Guard Hook downloads files from S3 every time the Hook is invoked. To prevent accidental changes or deletions, we recommend using a version when configuring your Guard Hook. 

Required: No

Type: String

Update requires: No interruption
