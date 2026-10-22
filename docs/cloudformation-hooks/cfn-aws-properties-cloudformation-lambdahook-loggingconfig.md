> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-loggingconfig.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::LambdaHook LoggingConfig

Contains logging configuration information for an extension.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "LogGroupName" : String,
  "LogRoleArn" : String
}

```

### YAML

```
  LogGroupName: String
  LogRoleArn: String

```

## Properties

**`LogGroupName`** 

The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers. 

Required: Yes

Type: String

Pattern: `^[\.\-_/#A-Za-z0-9]+$`

Minimum: `1`

Maximum: `512`

Update requires: Replacement

**`LogRoleArn`** 

The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs. 

Required: Yes

Type: String

Pattern: `arn:.+:iam::[0-9]{12}:role/.+`

Minimum: `1`

Maximum: `256`

Update requires: Replacement
