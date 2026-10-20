> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-fsxauthorizationconfig.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition FSxAuthorizationConfig

The authorization configuration details for Amazon FSx for Windows File Server file system. See FSxWindowsFileServerVolumeConfiguration in the Amazon ECS API Reference.

For more information and the input format, see Amazon FSx for Windows File Server Volumes in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CredentialsParameter" : String,
  "Domain" : String
}

```

### YAML

```
  CredentialsParameter: String
  Domain: String

```

## Properties

**`CredentialsParameter`** 

The authorization credential option to use. The authorization credential options can be provided using either the Amazon Resource Name (ARN) of an AWS Secrets Manager secret or SSM Parameter Store parameter. The ARN refers to the stored credentials. 

Required: Yes

Type: String

Update requires: Replacement

**`Domain`** 

A fully qualified domain name hosted by an AWS Directory Service Managed Microsoft AD (Active Directory) or self-hosted AD on Amazon EC2. 

Required: Yes

Type: String

Update requires: Replacement
