> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-policy.html
> Downloaded: 2026-10-20

# AWS::Organizations::Policy

Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.

For more information about policies and their use, see Managing AWS Organizations policies.

If the request includes tags, then the requester must have the `organizations:TagResource` permission.

This operation can be called only from the organization's management account or a member account designated as a delegated administrator.Note

Before you can create a policy of a given type, you must first enable that policy type in your organization.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Organizations::Policy",
  "Properties" : {
      "Content" : Json,
      "Description" : String,
      "Name" : String,
      "Tags" : [ Tag, ... ],
      "TargetIds" : [ String, ... ],
      "Type" : String
    }
}

```

### YAML

```
Type: AWS::Organizations::Policy
Properties:
  Content: Json
  Description: String
  Name: String
  Tags: 
    - Tag
  TargetIds: 
    - String
  Type: String

```

## Properties

**`Content`** 

The policy text content. You can specify the policy content as a JSON object or a JSON string. Important

When you specify the policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the policy content as a JSON object instead. 

The text that you supply must adhere to the rules of the policy type you specify in the `Type` parameter. The following AWS Organizations quotas are enforced for the maximum size of a policy document:  
Service control policies: 5,120 characters 
Resource control policies: 5,120 characters 
Declarative policies: 10,000 characters 
Backup policies: 10,000 characters 
Tag policies: 10,000 characters 
Chat applications policies: 10,000 characters 
AI services opt-out policies: 2,500 characters 
Security Hub policies: 10,000 characters 
Amazon Inspector policies: 10,000 characters 
Amazon Bedrock policies: 10,000 characters 
Upgrade rollout policies: 10,000 characters 
 

For more information about Organizations service quotas, see Quotas for AWS Organizations in the AWS Organizations User Guide. 

Required: Yes

Type: Json

Pattern: `[\s\S]*`

Minimum: `1`

Maximum: `1000000`

Update requires: No interruption

**`Description`** 

Human readable description of the policy. 

Required: No

Type: String

Pattern: `[\s\S]*`

Maximum: `512`

Update requires: No interruption

**`Name`** 

Name of the policy. 

The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range. 

Required: Yes

Type: String

Pattern: `[\s\S]*`

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`Tags`** 

A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to `null`. For more information about tagging, see Tagging AWS Organizations resources in the AWS Organizations User Guide. Note

If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created. 

Required: No

Type: Array of Tag

Update requires: No interruption

**`TargetIds`** 

List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the ListRoots, ListOrganizationalUnitsForParent, or ListAccounts operations. If you don't specify this parameter, the policy is created but not attached to any organization resource. 

The regex pattern for a target ID string requires one of the following:  
Root - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. 
Account - A string that consists of exactly 12 digits. 
Organizational unit (OU) - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits. 
 

Required: No

Type: Array of String

Pattern: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`

Maximum: `100`

Update requires: No interruption

**`Type`** 

The type of policy to create. 

Required: Yes

Type: String

Allowed values: `AISERVICES_OPT_OUT_POLICY | BACKUP_POLICY | BEDROCK_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | INSPECTOR_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY | RESOURCE_CONTROL_POLICY | S3_POLICY | SECURITYHUB_POLICY | SERVICE_CONTROL_POLICY | TAG_POLICY | UPGRADE_ROLLOUT_POLICY`

Update requires: Replacement

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Id`. For example: `p-examplepolicyid111`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

Returns the Amazon Resource Name (ARN) of the policy. For example: `arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111`. 

**`AwsManaged`** 

Returns a boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it. For example: `true | false`. 

**`Id`** 

Returns the unique identifier (ID) of the policy. For example: `p-examplepolicyid111`. 

## Examples
Organization Policy Content Specified as a JSON Object
Organization Policy Content Specified as a JSON String
 

### Organization Policy Content Specified as a JSON Object

This example illustrates how to specify the organization policy content as a JSON object in `AWS::Organizations::Policy`. The organization policy is specified inline as a JSON object in the `Content` property of `AWS::Organizations::Policy`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "PolicyTestTemplate": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Policy",
      "Properties": {
        "Type": "SERVICE_CONTROL_POLICY",
        "Name": "SCPDenyLeaveOrganization",
        "Content": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "SCPDenyLeaveOrganization",
              "Effect": "Deny",
              "Action": [
                "organizations:LeaveOrganization"
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
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content:
        Version: 2012-10-17
        Statement:
          - Sid: SCPDenyLeaveOrganization
            Effect: Deny
            Action:
              - 'organizations:LeaveOrganization'
            Resource: '*'

```
 

### Organization Policy Content Specified as a JSON String

This example illustrates how to specify the organization policy content as a JSON string in `AWS::Organizations::Policy`. The organization policy is specified inline as a JSON string in the `Content` property of `AWS::Organizations::Policy`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "PolicyTestTemplate": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Policy",
      "Properties": {
        "Type": "SERVICE_CONTROL_POLICY",
        "Name": "SCPDenyLeaveOrganization",
        "Content": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"SCPDenyLeaveOrganization\",\"Effect\":\"Deny\",\"Action\":[\"organizations:LeaveOrganization\"],\"Resource\":\"*\"}]}"
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
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content: >-
        {"Version":"2012-10-17","Statement":[{"Sid":"SCPDenyLeaveOrganization","Effect":"Deny","Action":["organizations:LeaveOrganization"],"Resource":"*"}]}

```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: AWS CloudFormation Organizations Template Example
Resources:
  PolicyTestTemplate:
    DeletionPolicy: Retain
    Type: AWS::Organizations::Policy
    Properties:
      Type: SERVICE_CONTROL_POLICY
      Name: SCPDenyLeaveOrganization
      Content: >-
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "SCPDenyLeaveOrganization",
              "Effect": "Deny",
              "Action": [
                "organizations:LeaveOrganization"
              ],
              "Resource": "*"
            }
          ]
        }

```
 

## See also 
Managing AWS Organizations policies in the AWS Organizations User Guide. 
CreatePolicy in the AWS Organizations API Reference Guide.
