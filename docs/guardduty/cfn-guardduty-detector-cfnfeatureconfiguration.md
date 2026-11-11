<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureconfiguration.html -->
<!-- Downloaded: 2026-10-28 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNFeatureConfiguration

Information about the configuration of a feature in your account.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[AdditionalConfiguration](#cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration)" : [ [CFNFeatureAdditionalConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html), ... ],
  "[Name](#cfn-guardduty-detector-cfnfeatureconfiguration-name)" : String,
  "[Status](#cfn-guardduty-detector-cfnfeatureconfiguration-status)" : String
}

```

### YAML

```
  [AdditionalConfiguration](#cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration):
    - [CFNFeatureAdditionalConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html)
  [Name](#cfn-guardduty-detector-cfnfeatureconfiguration-name): String
  [Status](#cfn-guardduty-detector-cfnfeatureconfiguration-status): String

```

## Properties

**`AdditionalConfiguration`**

Information about the additional configuration of a feature in your account.

*Required*: No

*Type*: Array of [CFNFeatureAdditionalConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Name`**

Name of the feature. For a list of allowed values, see [DetectorFeatureConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfiguration.html#guardduty-Type-DetectorFeatureConfiguration-name) in the *GuardDuty API Reference*.

*Required*: Yes

*Type*: String

*Maximum*: `128`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Status`**

Status of the feature configuration.

*Required*: Yes

*Type*: String

*Allowed values*: `ENABLED | DISABLED`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
