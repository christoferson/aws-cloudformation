<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-environmentvariable.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage EnvironmentVariable

The `EnvironmentVariable` property type specifies Property description not available. for an [AWS::Lambda::MicrovmImage](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html).

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Key](#cfn-lambda-microvmimage-environmentvariable-key)" : String,
  "[Value](#cfn-lambda-microvmimage-environmentvariable-value)" : String
}

```

### YAML

```
  [Key](#cfn-lambda-microvmimage-environmentvariable-key): String
  [Value](#cfn-lambda-microvmimage-environmentvariable-value): String

```

## Properties

**`Key`**

Property description not available.

*Required*: Yes

*Type*: String

*Pattern*: `^[^\s]+$`

*Minimum*: `1`

*Maximum*: `256`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Value`**

Property description not available.

*Required*: Yes

*Type*: String

*Minimum*: `0`

*Maximum*: `4096`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
