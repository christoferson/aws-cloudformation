<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-config.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector Config

Configuration for a VPC egress network connector. Specifies the subnets, security groups, and network protocol for routing outbound traffic through your VPC.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[VpcEgressConfiguration](#cfn-lambda-networkconnector-config-vpcegressconfiguration)" : [VpcEgressConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html)
}

```

### YAML

```
  [VpcEgressConfiguration](#cfn-lambda-networkconnector-config-vpcegressconfiguration):
    [VpcEgressConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html)

```

## Properties

**`VpcEgressConfiguration`**

The VPC egress configuration for the network connector.

*Required*: Yes

*Type*: [VpcEgressConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
