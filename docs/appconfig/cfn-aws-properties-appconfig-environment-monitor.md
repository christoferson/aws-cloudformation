> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-environment-monitor.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Environment Monitor

Amazon CloudWatch alarms to monitor during the deployment process.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlarmArn" : String,
  "AlarmRoleArn" : String
}

```

### YAML

```
  AlarmArn: String
  AlarmRoleArn: String

```

## Properties

**`AlarmArn`** 

Amazon Resource Name (ARN) of the Amazon CloudWatch alarm. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: No interruption

**`AlarmRoleArn`** 

ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor `AlarmArn`. 

Required: No

Type: String

Minimum: `20`

Maximum: `2048`

Update requires: No interruption
