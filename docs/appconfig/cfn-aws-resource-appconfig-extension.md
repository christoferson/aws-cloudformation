> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-extension.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Extension

Creates an AWS AppConfig extension. An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration.

You can create your own extensions or use the AWS authored extensions provided by AWS AppConfig. For an AWS AppConfig extension that uses AWS Lambda, you must create a Lambda function to perform any computation and processing defined in the extension. If you plan to create custom versions of the AWS authored notification extensions, you only need to specify an Amazon Resource Name (ARN) in the `Uri` field for the new extension version. 
For a custom EventBridge notification extension, enter the ARN of the EventBridge default events in the `Uri` field. 
For a custom Amazon SNS notification extension, enter the ARN of an Amazon SNS topic in the `Uri` field. 
For a custom Amazon SQS notification extension, enter the ARN of an Amazon SQS message queue in the `Uri` field.  

For more information about extensions, see Extending workflows in the AWS AppConfig User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AppConfig::Extension",
  "Properties" : {
      "Actions" : [ Action, ... ],
      "Description" : String,
      "LatestVersionNumber" : Integer,
      "Name" : String,
      "Parameters" : {Key: Value, ...},
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::Extension
Properties:
  Actions: 
    - Action
  Description: String
  LatestVersionNumber: Integer
  Name: String
  Parameters: 
    Key: Value
  Tags: 
    - Tag

```

## Properties

**`Actions`** 

The actions defined in the extension. 

Required: Yes

Type: Array of Action

Pattern: `^.+$`

Update requires: No interruption

**`Description`** 

Information about the extension. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`LatestVersionNumber`** 

You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. 

Required: No

Type: Integer

Update requires: No interruption

**`Name`** 

A name for the extension. Each extension name in your account must be unique. Extension versions use the same name. 

Required: Yes

Type: String

Pattern: `^[^\/#:\n]{1,64}$`

Update requires: Replacement

**`Parameters`** 

The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the `CreateExtensionAssociation` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object. 

Required: No

Type: Object of Parameter

Update requires: No interruption

**`Tags`** 

Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.  

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns information about the extension.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The system-generated Amazon Resource Name (ARN) for the extension. 

**`Id`** 

The system-generated ID of the extension. 

**`VersionNumber`** 

The extension version number. 

## Examples

 

### AWS AppConfig create extension example

An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration. You can create your own extensions or use the AWS authored extensions provided by AWS AppConfig. The following extension performs an action using AWS Lambda (as defined by the `Uri` field) before a configuration version is created by AWS AppConfig (as defined by the `PRE_CREATE_HOSTED_CONFIGURATION_VERSION` action point).

#### JSON

```
{
  "Resources": {
    "BasicExtension": {
      "Type": "AWS::AppConfig::Extension",
      "Properties": {
        "Name": "My Test Extension",
        "Description": "My test extension",
        "LatestVersionNumber": 0,
        "Actions": {
          "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [
            {
              "Name": "My Test Action",
              "Uri": "DependentLambda.Arn",
              "RoleArn": "DependentRole.Arn",
              "Description": "My test action point"
            }
          ]
        },
        "Parameters": {
          "MyTestParam": {
            "Required": false,
            "Description": "My test parameter"
          }
        },
        "Tags": [
          {
            "Key": "Ext",
            "Value": "Test"
          }
        ]
      }
    }
  }
}
```

#### YAML

```
Resources:
  BasicExtension:
    Type: AWS::AppConfig::Extension
    Properties:
      Name: "My Test Extension"
      Description: "My test extension"
      LatestVersionNumber: 0
      Actions:
        PRE_CREATE_HOSTED_CONFIGURATION_VERSION:
          - Name: "My Test Action"
            Uri: !GetAtt DependentLambda.Arn
            RoleArn: !GetAtt DependentRole.Arn
            Description: "My test action point"
      Parameters:
        MyTestParam:
          Required: false
          Description: "My test parameter"
      Tags:
        - Key: Ext
          Value: Test
```
 

## See also 
 AWS AppConfig  
 Working with AWS AppConfig extensions
