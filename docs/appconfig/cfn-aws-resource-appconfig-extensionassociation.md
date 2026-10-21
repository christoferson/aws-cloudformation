> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-extensionassociation.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExtensionAssociation

When you create an extension or configure an AWS authored extension, you associate the extension with an AWS AppConfig application, environment, or configuration profile. For example, you can choose to run the `AWS AppConfig deployment events to Amazon SNS`AWS authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AWS AppConfig resource is called an extension association. An extension association is a specified relationship between an extension and an AWS AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see Extending workflows in the AWS AppConfig User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AppConfig::ExtensionAssociation",
  "Properties" : {
      "ExtensionIdentifier" : String,
      "ExtensionVersionNumber" : Integer,
      "Parameters" : {Key: Value, ...},
      "ResourceIdentifier" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::ExtensionAssociation
Properties:
  ExtensionIdentifier: String
  ExtensionVersionNumber: Integer
  Parameters: 
    Key: Value
  ResourceIdentifier: String
  Tags: 
    - Tag

```

## Properties

**`ExtensionIdentifier`** 

The name, the ID, or the Amazon Resource Name (ARN) of the extension. 

Required: No

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`ExtensionVersionNumber`** 

The version number of the extension. If not specified, AWS AppConfig uses the maximum version of the extension. 

Required: No

Type: Integer

Update requires: Replacement

**`Parameters`** 

The parameter names and values defined in the extensions. Extension parameters marked `Required` must be entered for this field. 

Required: No

Type: Object of String

Pattern: `^.+$`

Update requires: No interruption

**`ResourceIdentifier`** 

The ARN of an application, configuration profile, or environment. 

Required: No

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`Tags`** 

Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.  

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns information about the extension association.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The ARN of the extension defined in the association. 

**`ExtensionArn`** 

The ARN of the extension defined in the association. 

**`Id`** 

The system-generated ID for the association. 

**`ResourceArn`** 

The ARNs of applications, configuration profiles, or environments defined in the association. 

## Examples

 

### AWS AppConfig create extension association example

An extension association defines which extension to associate with an AWS AppConfig resource. An extension association is a specified relationship between an extension and an AWS AppConfig resource, such as an application or a configuration profile. The following example creates an extension association between an application called MyDependentApplication and an extension called MyAmazingExtension.

#### JSON

```
{
  "Resources": {
    "BasicExtensionAssociation": {
      "Type": "AWS::AppConfig::ExtensionAssociation",
      "Properties": {
        "ExtensionIdentifier": "MyAmazingExtension",
        "ExtensionVersionNumber": 0,
        "ResourceIdentifier": [
          "/",
          [
            "arn:${AWS::Partition}:appconfig:${AWS::Region}:${AWS::AccountId}:application",
            "MyApplication"
          ]
         ],
        "Parameters": {
          "MyTestParam": "My test parameter value"
        },
        "Tags": [
          {
            "Key": "ExtAssociation",
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
  BasicExtensionAssociation:
    Type: AWS::AppConfig::ExtensionAssociation
    Properties:
      ExtensionIdentifier: !ImportValue MyAmazingExtension
      ExtensionVersionNumber: 0
      ResourceIdentifier: !Join
        - '/'
        - - !Sub 'arn:${AWS::Partition}:appconfig:${AWS::Region}:${AWS::AccountId}:application'
          - !ImportValue MyApplication
      Parameters:
        MyTestParam: "My test parameter value"
      Tags:
        - Key: ExtAssociation
          Value: Test
```
 

## See also 
 AWS AppConfig  
 Working with AWS AppConfig extensions
