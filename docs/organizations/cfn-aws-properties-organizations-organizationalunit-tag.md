> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-organizations-organizationalunit-tag.html
> Downloaded: 2026-10-20

# AWS::Organizations::OrganizationalUnit Tag

A custom key-value pair associated with a resource within your organization.

You can attach tags to any of the following organization resources. 
AWS account 
Organizational unit (OU) 
Organization root 
Policy 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Key" : String,
  "Value" : String
}

```

### YAML

```
  Key: String
  Value: String

```

## Properties

**`Key`** 

The key identifier, or name, of the tag. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`Value`** 

The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. 

Required: Yes

Type: String

Minimum: `0`

Maximum: `256`

Update requires: No interruption
