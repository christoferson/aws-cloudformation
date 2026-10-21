> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extension-action.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Extension Action

The actions defined in the extension.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Description" : String,
  "Name" : String,
  "RoleArn" : String,
  "Uri" : String
}

```

### YAML

```
  Description: String
  Name: String
  RoleArn: String
  Uri: String

```

## Properties

**`Description`** 

Information about actions defined in the extension. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`Name`** 

The extension name. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`RoleArn`** 

An Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role. 

Required: No

Type: String

Minimum: `20`

Maximum: `2048`

Update requires: No interruption

**`Uri`** 

The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an AWS Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: No interruption
