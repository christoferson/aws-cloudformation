<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Hooks

Lifecycle hook configuration for MicroVMs and MicroVM images.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[MicrovmHooks](#cfn-lambda-microvmimage-hooks-microvmhooks)" : [MicrovmHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmhooks.html),
  "[MicrovmImageHooks](#cfn-lambda-microvmimage-hooks-microvmimagehooks)" : [MicrovmImageHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmimagehooks.html),
  "[Port](#cfn-lambda-microvmimage-hooks-port)" : Integer
}

```

### YAML

```
  [MicrovmHooks](#cfn-lambda-microvmimage-hooks-microvmhooks):
    [MicrovmHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmhooks.html)
  [MicrovmImageHooks](#cfn-lambda-microvmimage-hooks-microvmimagehooks):
    [MicrovmImageHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmimagehooks.html)
  [Port](#cfn-lambda-microvmimage-hooks-port): Integer

```

## Properties

**`MicrovmHooks`**

The lifecycle hooks for MicroVM events.

*Required*: No

*Type*: [MicrovmHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmhooks.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`MicrovmImageHooks`**

The hooks for MicroVM image build events.

*Required*: No

*Type*: [MicrovmImageHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmimagehooks.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Port`**

The port number on which the hooks listener runs.

*Required*: No

*Type*: Integer

*Minimum*: `1`

*Maximum*: `65535`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
