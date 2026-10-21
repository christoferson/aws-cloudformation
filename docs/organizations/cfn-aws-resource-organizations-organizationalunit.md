> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-organizationalunit.html
> Downloaded: 2026-10-20

# AWS::Organizations::OrganizationalUnit

Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five.

For more information about OUs, see Managing organizational units (OUs) in the AWS Organizations User Guide.

If the request includes tags, then the requester must have the `organizations:TagResource` permission.

You can only call this operation from the management account.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Organizations::OrganizationalUnit",
  "Properties" : {
      "Name" : String,
      "ParentId" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::Organizations::OrganizationalUnit
Properties:
  Name: String
  ParentId: String
  Tags: 
    - Tag

```

## Properties

**`Name`** 

The friendly name of this OU. 

The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range. 

Required: Yes

Type: String

Pattern: `[\s\S]*`

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`ParentId`** 

The unique identifier (ID) of the parent root or OU that you want to create the new OU in. Important

To update the `ParentId` parameter value, you must first remove all accounts attached to the organizational unit (OU). OUs can't be moved within the organization with accounts still attached. 

The regex pattern for a parent ID string requires one of the following:  
Root - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. 
Organizational unit (OU) - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits. 
 

Required: Yes

Type: String

Pattern: `^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`

Maximum: `100`

Update requires: Replacement

**`Tags`** 

A list of tags that you want to attach to the newly created OU. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to `null`. For more information about tagging, see Tagging AWS Organizations resources in the AWS Organizations User Guide. Note

If any one of the tags is not valid or if you exceed the allowed number of tags for an OU, then the entire request fails and the OU is not created. 

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Id`. For example: `ou-examplerootid111-exampleouid111`.Note

When creating child OUs, we recommend that you use the `Ref` function instead of `Fn::GetAtt`. For example, in the properties for the child OU, use `ParentId: !Ref ParentOU`, instead of `ParentId: !GetAtt 'ParentOU.Id'`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The Amazon Resource Name (ARN) of this OU. For example: `arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111`. 

**`Id`** 

The unique identifier (ID) associated with this OU. For example: `ou-examplerootid111-exampleouid111`. 

**`Path`** 

The path in the organization where this OU exists. 

## Examples
Specify an OU under the root
Specify an OU under a parent OU
 

### Specify an OU under the root

This example illustrates how to specify an OU using `AWS::Organizations::OrganizationalUnit` directly under the root.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Organizations Template Example",
    "Parameters": {
        "OrganizationRootId": {
            "Type": "String"
        }
    },
    "Resources": {
        "TestTemplateOU": {
            "Type": "AWS::Organizations::OrganizationalUnit",
            "Properties": {
                "Name": "TestTemplateOU",
                "ParentId": {
                    "Ref": "OrganizationRootId"
                }
            }
        }
    }
}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Parameters:
  OrganizationRootId:
    Type: String
Resources:
  TestTemplateOU:
    Type: 'AWS::Organizations::OrganizationalUnit'
    Properties:
      Name: TestTemplateOU
      ParentId: !Ref OrganizationRootId

```
 

### Specify an OU under a parent OU

This example illustrates how to specify a nested OU using `AWS::Organizations::OrganizationalUnit` by referencing another OU.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Nested OU Template Example",
    "Parameters": {
        "OrganizationRootId": {
            "Type": "String"
        }
    },
    "Resources": {
        "ParentOU": {
            "Type": "AWS::Organizations::OrganizationalUnit",
            "Properties": {
                "Name": "ParentOU",
                "ParentId": {
                    "Ref": "OrganizationRootId"
                }
            }
        },
        "ChildOU": {
            "Type": "AWS::Organizations::OrganizationalUnit",
            "Properties": {
                "Name": "ChildOU",
                "ParentId": {
                    "Ref": "ParentOU"
                }
            }
        }
    }
}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Nested OU Template Example
Parameters:
  OrganizationRootId:
    Type: String
Resources:
  ParentOU:
    Type: 'AWS::Organizations::OrganizationalUnit'
    Properties:
      Name: ParentOU
      ParentId: !Ref OrganizationRootId
  ChildOU:
    Type: 'AWS::Organizations::OrganizationalUnit'
    Properties:
      Name: ChildOU
      ParentId: !Ref ParentOU

```
 

## See also 
Creating an OU in the AWS Organizations User Guide. 
CreateOrganizationalUnit in the AWS Organizations API Reference Guide.
