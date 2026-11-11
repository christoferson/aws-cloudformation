<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cloudwatchlogging.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CloudWatchLogging

Configuration for Amazon CloudWatch Logs logging.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[LogGroup](#cfn-lambda-microvmimage-cloudwatchlogging-loggroup)" : String,
  "[LogStream](#cfn-lambda-microvmimage-cloudwatchlogging-logstream)" : String
}

```

### YAML

```
  [LogGroup](#cfn-lambda-microvmimage-cloudwatchlogging-loggroup): String
  [LogStream](#cfn-lambda-microvmimage-cloudwatchlogging-logstream): String

```

## Properties

**`LogGroup`**

The name of the CloudWatch Logs log group to send logs to.

*Required*: No

*Type*: String

*Pattern*: `^[a-zA-Z0-9_\-/.#]+$`

*Minimum*: `1`

*Maximum*: `512`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`LogStream`**

The name of the CloudWatch Logs log stream within the log group.

*Required*: No

*Type*: String

*Pattern*: `^[^:*]*$`

*Minimum*: `1`

*Maximum*: `512`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
