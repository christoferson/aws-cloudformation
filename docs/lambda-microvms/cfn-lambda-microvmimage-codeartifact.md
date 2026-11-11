<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-codeartifact.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CodeArtifact

Contains the location of the code artifact for a MicroVM image.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Uri](#cfn-lambda-microvmimage-codeartifact-uri)" : String
}

```

### YAML

```
  [Uri](#cfn-lambda-microvmimage-codeartifact-uri): String

```

## Properties

**`Uri`**

The URI of the code artifact in Amazon S3.

*Required*: Yes

*Type*: String

*Pattern*: `^[^\s]+$`

*Minimum*: `1`

*Maximum*: `2048`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
