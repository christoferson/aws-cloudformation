> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-resourcepolicy.html
> Downloaded: 2026-10-20

# AWS::Organizations::ResourcePolicy

Creates or updates a resource-based delegation policy that can be used to delegate policy management for AWS Organizations to specified member accounts to perform policy actions that are by default available only to the management account.

For more information about delegated policy management, see Delegated administrator for AWS Organizations in the AWS Organizations User Guide.

You can only call this operation from the organization's management account.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Organizations::ResourcePolicy",
  "Properties" : {
      "Content" : Json,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::Organizations::ResourcePolicy
Properties:
  Content: Json
  Tags: 
    - Tag

```

## Properties

**`Content`** 

The policy text of the organization resource policy. You can specify the resource policy content as a JSON object or a JSON string. Important

When you specify the resource policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the resource policy content as a JSON object instead. 

Required: Yes

Type: Json

Pattern: `[\s\S]*`

Minimum: `1`

Maximum: `40000`

Update requires: No interruption

**`Tags`** 

A list of tags that you want to attach to the newly created resource policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to `null`. For more information about tagging, see Tagging AWS Organizations resources in the AWS Organizations User Guide. Note

If any one of the tags is not valid or if you exceed the allowed number of tags for the resource policy, then the entire request fails and the resource policy is not created. 

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Id`. For example: `rp-examplepolicyid111`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

Returns the Amazon Resource Name (ARN) of the policy. For example: `arn:aws:organizations::111111111111:resourcepolicy/o-exampleorgid/rp-examplepolicyid111`. 

**`Id`** 

Returns the unique identifier (ID) of the resource policy. For example: `rp-examplepolicyid111`. 

## Examples
Organization Resource Policy Content Specified as a JSON Object
Organization Resource Policy Content Specified as a JSON String
 

### Organization Resource Policy Content Specified as a JSON Object

This example illustrates how to specify the organization resource policy content as a JSON object in `AWS::Organizations::ResourcePolicy`. The organization resource policy is specified inline as a JSON object in the `Content` property of `AWS::Organizations::ResourcePolicy`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "ResourcePolicyTestTemplate": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::ResourcePolicy",
      "Properties": {
        "Content": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "AllowDescribeOrganization",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
              },
              "Action": [
                "organizations:DescribeOrganization"
              ],
              "Resource": "*"
            }
          ]
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
Resources:
  ResourcePolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::ResourcePolicy
    Properties:
      Content:
        Version: 2012-10-17
        Statement:
          - Sid: AllowDescribeOrganization
            Effect: Allow
            Principal:
              AWS: 'arn:aws:iam::111122223333:root'
            Action:
              - 'organizations:DescribeOrganization'
            Resource: '*'

```
 

### Organization Resource Policy Content Specified as a JSON String

This example illustrates how to specify the organization resource policy content as a JSON string in `AWS::Organizations::ResourcePolicy`. The organization resource policy is specified inline as a JSON string in the `Content` property of `AWS::Organizations::ResourcePolicy`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "ResourcePolicyExample": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::ResourcePolicy",
      "Properties": {
        "Content": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"AllowDescribeOrganization\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::111122223333:root\"},\"Action\":[\"organizations:DescribeOrganization\"],\"Resource\":\"*\"}]}"
      }
    }
  }
}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  ResourcePolicyExample:
    DeletionPolicy: Retain
    Type: AWS::Organizations::ResourcePolicy
    Properties:
      Content: >-
        {"Version":"2012-10-17","Statement":[{"Sid":"AllowDescribeOrganization","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::111122223333:root"},"Action":["organizations:DescribeOrganization"],"Resource":"*"}]}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  ResourcePolicyExample:
    DeletionPolicy: Retain
    Type: AWS::Organizations::ResourcePolicy
    Properties:
      Content: >-
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "AllowDescribeOrganization",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
              },
              "Action": [
                "organizations:DescribeOrganization"
              ],
              "Resource": "*"
            }
          ]
        }

```
 

## See also 
Delegated administrator for AWS Organizations in the AWS Organizations User Guide. 
PutResourcePolicy in the AWS Organizations API Reference Guide.
