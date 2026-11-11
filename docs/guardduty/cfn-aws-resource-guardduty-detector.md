<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-detector.html -->
<!-- Downloaded: 2026-10-28 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector

The `AWS::GuardDuty::Detector` resource specifies a new GuardDuty detector. A detector is an object that represents the GuardDuty service. A detector is required for GuardDuty to become operational.

Make sure you use either `DataSources` or `Features` in a one request, and not both.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::GuardDuty::Detector",
  "Properties" : {
      "[DataSources](#cfn-guardduty-detector-datasources)" : [CFNDataSourceConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfndatasourceconfigurations.html),
      "[Enable](#cfn-guardduty-detector-enable)" : Boolean,
      "[Features](#cfn-guardduty-detector-features)" : [ [CFNFeatureConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureconfiguration.html), ... ],
      "[FindingPublishingFrequency](#cfn-guardduty-detector-findingpublishingfrequency)" : String,
      "[Tags](#cfn-guardduty-detector-tags)" : [ [TagItem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-tagitem.html), ... ]
    }
}

```

### YAML

```
Type: AWS::GuardDuty::Detector
Properties:
  [DataSources](#cfn-guardduty-detector-datasources):
    [CFNDataSourceConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
  [Enable](#cfn-guardduty-detector-enable): Boolean
  [Features](#cfn-guardduty-detector-features):
    - [CFNFeatureConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureconfiguration.html)
  [FindingPublishingFrequency](#cfn-guardduty-detector-findingpublishingfrequency): String
  [Tags](#cfn-guardduty-detector-tags):
    - [TagItem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-tagitem.html)

```

## Properties

**`DataSources`**

Describes which data sources will be enabled for the detector.

*Required*: No

*Type*: [CFNDataSourceConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Enable`**

Specifies whether the detector is to be enabled on creation.

*Required*: Yes

*Type*: Boolean

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Features`**

A list of features that will be configured for the detector.

*Required*: No

*Type*: Array of [CFNFeatureConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureconfiguration.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`FindingPublishingFrequency`**

Specifies how frequently updated findings are exported.

*Required*: No

*Type*: String

*Allowed values*: `FIFTEEN_MINUTES | ONE_HOUR | SIX_HOURS`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`Tags`**

Specifies tags added to a new detector resource. Each tag consists of a key and an optional value, both of which you define.

Currently, support is available only for creating and deleting a tag. No support exists for updating the tags.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

*Required*: No

*Type*: Array of [TagItem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-tagitem.html)

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID of the detector.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####

**`Id`**

The unique ID of the detector.

## Examples

### Declare a Detector Resource

The following example shows how to declare a GuardDuty`Detector` resource:

#### JSON

```
"mydetector": {
    "Type" : "AWS::GuardDuty::Detector",
    "Properties" : {
        "Enable" : True,
        "FindingPublishingFrequency" : "FIFTEEN_MINUTES"
    }
}
```

#### YAML

```
mydetector:
    Type: AWS::GuardDuty::Detector
    Properties:
        Enable: True
        FindingPublishingFrequency: FIFTEEN_MINUTES
```
