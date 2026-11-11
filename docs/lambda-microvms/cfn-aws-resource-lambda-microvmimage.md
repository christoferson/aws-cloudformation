<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage

Creates a MicroVM image from the specified code artifact and base image. The build is asynchronous — the image transitions from CREATING to CREATED on success, or CREATE_FAILED on failure. Use GetMicrovmImage to poll for completion.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Lambda::MicrovmImage",
  "Properties" : {
      "[AdditionalOsCapabilities](#cfn-lambda-microvmimage-additionaloscapabilities)" : [ String, ... ],
      "[BaseImageArn](#cfn-lambda-microvmimage-baseimagearn)" : String,
      "[BaseImageVersion](#cfn-lambda-microvmimage-baseimageversion)" : String,
      "[BuildRoleArn](#cfn-lambda-microvmimage-buildrolearn)" : String,
      "[CodeArtifact](#cfn-lambda-microvmimage-codeartifact)" : [CodeArtifact](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-codeartifact.html),
      "[CpuConfigurations](#cfn-lambda-microvmimage-cpuconfigurations)" : [ [CpuConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html), ... ],
      "[Description](#cfn-lambda-microvmimage-description)" : String,
      "[EgressNetworkConnectors](#cfn-lambda-microvmimage-egressnetworkconnectors)" : [ String, ... ],
      "[EnvironmentVariables](#cfn-lambda-microvmimage-environmentvariables)" : [ [EnvironmentVariable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-environmentvariable.html), ... ],
      "[Hooks](#cfn-lambda-microvmimage-hooks)" : [Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html),
      "[KmsKeyIdentifier](#cfn-lambda-microvmimage-kmskeyidentifier)" : String,
      "[Logging](#cfn-lambda-microvmimage-logging)" : [Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html),
      "[Name](#cfn-lambda-microvmimage-name)" : String,
      "[Resources](#cfn-lambda-microvmimage-resources)" : [ [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html), ... ],
      "[Tags](#cfn-lambda-microvmimage-tags)" : [ [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-tag.html), ... ]
    }
}

```

### YAML

```
Type: AWS::Lambda::MicrovmImage
Properties:
  [AdditionalOsCapabilities](#cfn-lambda-microvmimage-additionaloscapabilities):
    - String
  [BaseImageArn](#cfn-lambda-microvmimage-baseimagearn): String
  [BaseImageVersion](#cfn-lambda-microvmimage-baseimageversion): String
  [BuildRoleArn](#cfn-lambda-microvmimage-buildrolearn): String
  [CodeArtifact](#cfn-lambda-microvmimage-codeartifact):
    [CodeArtifact](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-codeartifact.html)
  [CpuConfigurations](#cfn-lambda-microvmimage-cpuconfigurations):
    - [CpuConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html)
  [Description](#cfn-lambda-microvmimage-description): String
  [EgressNetworkConnectors](#cfn-lambda-microvmimage-egressnetworkconnectors):
    - String
  [EnvironmentVariables](#cfn-lambda-microvmimage-environmentvariables):
    - [EnvironmentVariable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-environmentvariable.html)
  [Hooks](#cfn-lambda-microvmimage-hooks):
    [Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html)
  [KmsKeyIdentifier](#cfn-lambda-microvmimage-kmskeyidentifier): String
  [Logging](#cfn-lambda-microvmimage-logging):
    [Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html)
  [Name](#cfn-lambda-microvmimage-name): String
  [Resources](#cfn-lambda-microvmimage-resources):
    - [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html)
  [Tags](#cfn-lambda-microvmimage-tags):
    - [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-tag.html)

```

## Properties

**`AdditionalOsCapabilities`**

Additional OS capabilities granted to the MicroVM runtime environment.

*Required*: Yes

*Type*: Array of String

*Allowed values*: `ALL`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`BaseImageArn`**

The ARN of the base MicroVM image used.

*Required*: Yes

*Type*: String

*Pattern*: `^[^\s]+$`

*Minimum*: `1`

*Maximum*: `2048`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`BaseImageVersion`**

The specific version of the base MicroVM image.

*Required*: Yes

*Type*: String

*Pattern*: `^[^\s]+$`

*Minimum*: `1`

*Maximum*: `2048`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`BuildRoleArn`**

The ARN of the IAM build role.

*Required*: Yes

*Type*: String

*Pattern*: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`CodeArtifact`**

The code artifact for this version.

*Required*: Yes

*Type*: [CodeArtifact](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-codeartifact.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`CpuConfigurations`**

The CPU configurations that the MicroVM image version is built for.

*Required*: Yes

*Type*: Array of [CpuConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Description`**

The description of the version.

*Required*: Yes

*Type*: String

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`EgressNetworkConnectors`**

The list of egress network connectors available to the MicroVM at image build time.

*Required*: Yes

*Type*: Array of String

*Maximum*: `10`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`EnvironmentVariables`**

Environment variables set in the MicroVM runtime environment.

*Required*: Yes

*Type*: Array of [EnvironmentVariable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-environmentvariable.html)

*Maximum*: `50`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Hooks`**

Lifecycle hook configuration for MicroVMs and MicroVM images.

*Required*: Yes

*Type*: [Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`KmsKeyIdentifier`**

Property description not available.

*Required*: No

*Type*: String

*Pattern*: `^(arn:aws[a-z-]*:kms:[a-z0-9-]+:[0-9]{12}:(key|alias)/[a-zA-Z0-9:/_-]+|alias/[a-zA-Z0-9:/_-]+|[a-zA-Z0-9-]+)$`

*Minimum*: `1`

*Maximum*: `2048`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Logging`**

Configuration for MicroVM logging output. Specify exactly one: cloudWatch to enable CloudWatch logging, or disabled to turn off logging.

*Required*: Yes

*Type*: [Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Name`**

The name of the MicroVM image.

*Required*: Yes

*Type*: String

*Pattern*: `^[a-zA-Z0-9-_]+$`

*Minimum*: `1`

*Maximum*: `64`

*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

**`Resources`**

The resource requirements for the MicroVM.

*Required*: Yes

*Type*: [Array](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html) of [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html)

*Maximum*: `1`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Tags`**

Key-value pairs associated with the version.

*Required*: No

*Type*: Array of [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-tag.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the image ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####

**`CreatedAt`**

The timestamp when the version was created.

**`ImageArn`**

The ARN of the MicroVM image.

**`LatestActiveImageVersion`**

The latest active version of the MicroVM image.

**`LatestFailedImageVersion`**

The latest failed version of the MicroVM image, if any.

**`State`**

The current state of the version.

**`UpdatedAt`**

The timestamp when the version was last updated.
