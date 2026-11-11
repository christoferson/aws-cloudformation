<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Logging

Configuration for MicroVM logging output. Specify exactly one: cloudWatch to enable CloudWatch logging, or disabled to turn off logging.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[CloudWatch](#cfn-lambda-microvmimage-logging-cloudwatch)" : [CloudWatchLogging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cloudwatchlogging.html),
  "[Disabled](#cfn-lambda-microvmimage-logging-disabled)" : Boolean
}

```

### YAML

```
  [CloudWatch](#cfn-lambda-microvmimage-logging-cloudwatch):
    [CloudWatchLogging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cloudwatchlogging.html)
  [Disabled](#cfn-lambda-microvmimage-logging-disabled): Boolean

```

## Properties

**`CloudWatch`**

Configuration for sending logs to Amazon CloudWatch Logs.

*Required*: No

*Type*: [CloudWatchLogging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cloudwatchlogging.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Disabled`**

Specifies that logging is disabled for the MicroVM.

*Required*: No

*Type*: Boolean

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
