<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmimagehooks.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage MicrovmImageHooks

Configuration for hooks invoked during MicroVM image build events such as ready and validate.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Ready](#cfn-lambda-microvmimage-microvmimagehooks-ready)" : String,
  "[ReadyTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-readytimeoutinseconds)" : Integer,
  "[Validate](#cfn-lambda-microvmimage-microvmimagehooks-validate)" : String,
  "[ValidateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-validatetimeoutinseconds)" : Integer
}

```

### YAML

```
  [Ready](#cfn-lambda-microvmimage-microvmimagehooks-ready): String
  [ReadyTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-readytimeoutinseconds): Integer
  [Validate](#cfn-lambda-microvmimage-microvmimagehooks-validate): String
  [ValidateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-validatetimeoutinseconds): Integer

```

## Properties

**`Ready`**

The path of the hook invoked when the MicroVM image build is ready.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`ReadyTimeoutInSeconds`**

The maximum time in seconds for the ready hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `3600`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Validate`**

The path of the hook invoked to validate the MicroVM image build.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`ValidateTimeoutInSeconds`**

The maximum time in seconds for the validate hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `3600`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
