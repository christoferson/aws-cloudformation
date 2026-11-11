<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CpuConfiguration

Configuration for the CPU architecture of a MicroVM.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Architecture](#cfn-lambda-microvmimage-cpuconfiguration-architecture)" : String
}

```

### YAML

```
  [Architecture](#cfn-lambda-microvmimage-cpuconfiguration-architecture): String

```

## Properties

**`Architecture`**

The CPU architecture. Valid values are ARM_64 and X86_64. Your container base image and any prebuilt binaries in your code artifact must be built for this architecture.

*Required*: Yes

*Type*: String

*Allowed values*: `ARM_64 | X86_64`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
