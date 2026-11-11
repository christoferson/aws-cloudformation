<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Resources

Resource requirements for a MicroVM.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[MinimumMemoryInMiB](#cfn-lambda-microvmimage-resources-minimummemoryinmib)" : Integer
}

```

### YAML

```
  [MinimumMemoryInMiB](#cfn-lambda-microvmimage-resources-minimummemoryinmib): Integer

```

## Properties

**`MinimumMemoryInMiB`**

The minimum amount of memory in MiB to allocate to the MicroVM.

*Required*: Yes

*Type*: Integer

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
