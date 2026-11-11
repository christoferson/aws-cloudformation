<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector

The `AWS::Lambda::NetworkConnector` resource creates a network connector that enables Lambda MicroVMs and WebFunction compute resources to reach resources in a virtual private cloud (VPC). A network connector provisions elastic network interfaces (ENIs) in the subnets you specify, providing a managed network path to private resources such as databases, caches, and internal APIs.

###### Note

Deleting the network connector removes the connector and all of its versions. You can also delete a specific historical version on its own by supplying its version-qualified ARN. You can't delete the latest version individually; to remove it, delete the network connector.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Lambda::NetworkConnector",
  "Properties" : {
      "[Configuration](#cfn-lambda-networkconnector-configuration)" : [Config](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-config.html),
      "[Name](#cfn-lambda-networkconnector-name)" : String,
      "[OperatorRole](#cfn-lambda-networkconnector-operatorrole)" : String,
      "[Tags](#cfn-lambda-networkconnector-tags)" : [ [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-tag.html), ... ]
    }
}

```

### YAML

```
Type: AWS::Lambda::NetworkConnector
Properties:
  [Configuration](#cfn-lambda-networkconnector-configuration):
    [Config](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-config.html)
  [Name](#cfn-lambda-networkconnector-name): String
  [OperatorRole](#cfn-lambda-networkconnector-operatorrole): String
  [Tags](#cfn-lambda-networkconnector-tags):
    - [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-tag.html)

```

## Properties

**`Configuration`**

The network configuration for the connector. Specify a `VpcEgressConfiguration` to enable outbound traffic routing through your VPC.

*Required*: Yes

*Type*: [Config](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-config.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Name`**

A unique name for the network connector within your account and Region. Must be 1 to 64 alphanumeric characters, hyphens, or underscores.

*Required*: No

*Type*: String

*Pattern*: `^(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9][0-9]*)?)|[a-zA-Z0-9_-]{1,64}$`

*Minimum*: `1`

*Maximum*: `140`

*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

**`OperatorRole`**

The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for `ec2:CreateNetworkInterface` and related describe operations.

*Required*: No

*Type*: String

*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

*Minimum*: `0`

*Maximum*: `10000`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Tags`**

A list of tags to apply to the network connector. Use tags to categorize network connectors for cost allocation, access control, or operational management.

*Required*: No

*Type*: Array of [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-tag.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the network connector.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####

**`Arn`**

The Amazon Resource Name (ARN) of the network connector.

**`LatestVersion`**

The version number of the network connector's latest version. Updates to the connector's configuration create a new immutable version, and this attribute exposes the most recent one.

**`LatestVersionArn`**

The qualified Amazon Resource Name (ARN) of the network connector's latest version. This ARN includes the immutable version suffix and can be used to pin to a specific version.

**`State`**

Current state of the network connector. Valid values are `PENDING`, `ACTIVE`, `INACTIVE`, `FAILED`, `DELETING`, and `DELETE_FAILED`.
