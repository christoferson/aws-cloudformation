<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html -->
<!-- Downloaded: 2026-10-28 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNFeatureAdditionalConfiguration

Information about the additional configuration of a feature in your account.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[Name](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name)" : String,
  "[Status](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status)" : String
}

```

### YAML

```
  [Name](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name): String
  [Status](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status): String

```

## Properties

**`Name`**

Name of the additional configuration.

*Required*: No

*Type*: String

*Minimum*: `1`

*Maximum*: `256`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Status`**

Status of the additional configuration.

*Required*: No

*Type*: String

*Minimum*: `1`

*Maximum*: `128`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
