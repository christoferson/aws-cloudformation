<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmhooks.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage MicrovmHooks

Configuration for lifecycle hooks invoked during MicroVM events such as run, resume, suspend, and terminate.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Resume](#cfn-lambda-microvmimage-microvmhooks-resume)" : String,
  "[ResumeTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-resumetimeoutinseconds)" : Integer,
  "[Run](#cfn-lambda-microvmimage-microvmhooks-run)" : String,
  "[RunTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-runtimeoutinseconds)" : Integer,
  "[Suspend](#cfn-lambda-microvmimage-microvmhooks-suspend)" : String,
  "[SuspendTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-suspendtimeoutinseconds)" : Integer,
  "[Terminate](#cfn-lambda-microvmimage-microvmhooks-terminate)" : String,
  "[TerminateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-terminatetimeoutinseconds)" : Integer
}

```

### YAML

```
  [Resume](#cfn-lambda-microvmimage-microvmhooks-resume): String
  [ResumeTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-resumetimeoutinseconds): Integer
  [Run](#cfn-lambda-microvmimage-microvmhooks-run): String
  [RunTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-runtimeoutinseconds): Integer
  [Suspend](#cfn-lambda-microvmimage-microvmhooks-suspend): String
  [SuspendTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-suspendtimeoutinseconds): Integer
  [Terminate](#cfn-lambda-microvmimage-microvmhooks-terminate): String
  [TerminateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-terminatetimeoutinseconds): Integer

```

## Properties

**`Resume`**

The path of the hook invoked when the MicroVM resumes from a suspended state.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`ResumeTimeoutInSeconds`**

The maximum time in seconds for the resume hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `60`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Run`**

The path of the hook invoked when the MicroVM starts running.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`RunTimeoutInSeconds`**

The maximum time in seconds for the run hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `60`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Suspend`**

The path of the hook invoked when the MicroVM is suspended.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`SuspendTimeoutInSeconds`**

The maximum time in seconds for the suspend hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `60`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Terminate`**

The path of the hook invoked when the MicroVM is terminated.

*Required*: No

*Type*: String

*Allowed values*: `DISABLED | ENABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`TerminateTimeoutInSeconds`**

The maximum time in seconds for the terminate hook to complete.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `60`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
