> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-targetfiltersitems.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook TargetFiltersItems

Specifies the resource types, actions, and invocation points to target for the `TargetFilters` property type.

For more information, see CloudFormation Hook target filters.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Actions" : [ String, ... ],
  "InvocationPoints" : [ String, ... ],
  "TargetNames" : [ String, ... ]
}

```

### YAML

```
  Actions: 
    - String
  InvocationPoints: 
    - String
  TargetNames: 
    - String

```

## Properties

**`Actions`** 

The actions to target. For `CHANGE_SET` Hook targets, you can only target `CREATE` actions. 

Valid values: `CREATE` | `UPDATE` | `DELETE` 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`InvocationPoints`** 

The invocation points to target. The only valid value is `PRE_PROVISION`. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`TargetNames`** 

The resource types to target, such as `AWS::S3::Bucket` or `AWS::DynamoDB::Table`. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption
