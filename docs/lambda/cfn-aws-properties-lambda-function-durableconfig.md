> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-durableconfig.html
> Downloaded: 2026-10-25

# AWS::Lambda::Function DurableConfig

Configuration settings for durable functions, including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ExecutionTimeout" : Integer,
  "KMSKeyArn" : String,
  "RetentionPeriodInDays" : Integer
}

```

### YAML

```
  ExecutionTimeout: Integer
  KMSKeyArn: String
  RetentionPeriodInDays: Integer

```

## Properties

**`ExecutionTimeout`** 

The maximum time (in seconds) that a durable execution can run before timing out. This timeout applies to the entire durable execution, not individual function invocations. 

Required: Yes

Type: Integer

Minimum: `1`

Maximum: `31622400`

Update requires: No interruption

**`KMSKeyArn`** 

The ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads. 

Required: No

Type: String

Pattern: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`

Update requires: No interruption

**`RetentionPeriodInDays`** 

The number of days to retain execution history after a durable execution completes. After this period, execution history is no longer available through the GetDurableExecutionHistory API. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `90`

Update requires: No interruption
