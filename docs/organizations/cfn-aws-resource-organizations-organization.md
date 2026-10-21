> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-organizations-organization.html
> Downloaded: 2026-10-20

# AWS::Organizations::Organization

Creates an AWS organization. The account whose user is calling the `CreateOrganization` operation automatically becomes the management account of the new organization.

This operation must be called using credentials from the account that is to become the new organization's management account. The principal must also have the relevant IAM permissions.Important 
If you delete an organization, you can't recover it. If you created any policies inside of the organization, they're also deleted and you can't recover them. 
You can delete an organization only after you remove all member accounts from the organization. If you created some of your member accounts using AWS Organizations, you might be blocked from removing those accounts. You can remove a member account only if it has all the information that's required to operate as a standalone AWS account. For more information about how to provide that information and then remove the account, see Leave an organization from your member account in the AWS Organizations User Guide. 
If you closed a member account before you remove it from the organization, it enters a 'suspended' state for a period of time and you can't remove the account from the organization until it is finally closed. This can take up to 90 days and can prevent you from deleting the organization until all member accounts are completely closed. 

For more information, see Deleting an organization in the AWS Organizations User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Organizations::Organization",
  "Properties" : {
      "FeatureSet" : String
    }
}

```

### YAML

```
Type: AWS::Organizations::Organization
Properties:
  FeatureSet: String

```

## Properties

**`FeatureSet`** 

Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.  
`ALL`– In addition to all the features supported by the consolidated billing feature set, the management account gains access to advanced features that give you more control over accounts in your organization. For more information, see All features in the AWS Organizations User Guide. 
`CONSOLIDATED_BILLING`– All member accounts have their bills consolidated to and paid by the management account. For more information, see Consolidated billing in the AWS Organizations User Guide.  Note

The consolidated billing feature feature set isn't available for organizations in the AWS GovCloud (US) Region. 
 

If you don't specify this property, the default value is `ALL`. 

Required: No

Type: String

Allowed values: `ALL | CONSOLIDATED_BILLING`

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AccountId`. For example: `123456789012`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The Amazon Resource Name (ARN) of an organization. 

  

**`Id`** 

The unique identifier (ID) of an organization. 

  

**`ManagementAccountArn`** 

The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization. 

  

**`ManagementAccountEmail`** 

The email address that is associated with the AWS account that is designated as the management account for the organization. 

**`ManagementAccountId`** 

The unique identifier (ID) of the management account of an organization. 

  

**`RootId`** 

The unique identifier (ID) for the root. 

  

## Examples
Organization FeatureSet specified as ALL
Organization FeatureSet specified as CONSOLIDATED_BILLING
 

### Organization FeatureSet specified as ALL

This example illustrates how to specify the organization feature set as `ALL` in `AWS::Organizations::Organization`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "OrganizationTemplateExample": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Organization",
      "Properties": {
        "FeatureSet": "ALL"
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
  OrganizationTemplateExample:
    DeletionPolicy: Retain
    Type: 'AWS::Organizations::Organization'
    Properties:
      FeatureSet: ALL

```
 

### Organization FeatureSet specified as CONSOLIDATED_BILLING

This example illustrates how to specify the organization feature set as `CONSOLIDATED_BILLING` in `AWS::Organizations::Organization`.

#### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS CloudFormation Organizations Template Example",
  "Resources": {
    "OrganizationTemplateExample": {
      "DeletionPolicy": "Retain",
      "Type": "AWS::Organizations::Organization",
      "Properties": {
        "FeatureSet": "CONSOLIDATED_BILLING"
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
  OrganizationTemplateExample:
    DeletionPolicy: Retain
    Type: 'AWS::Organizations::Organization'
    Properties:
      FeatureSet: CONSOLIDATED_BILLING

```
 

## See also 
Creating an organization in the AWS Organizations User Guide. 
CreateOrganization in the AWS Organizations API Reference Guide.
