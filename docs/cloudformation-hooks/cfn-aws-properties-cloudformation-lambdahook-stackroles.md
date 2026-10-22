> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-lambdahook-stackroles.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::LambdaHook StackRoles

Specifies the stack roles for the `StackFilters` property type to include or exclude specific stacks from Hook invocations based on their associated IAM roles.

For more information, see CloudFormation Hooks stack level filters.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Exclude" : [ String, ... ],
  "Include" : [ String, ... ]
}

```

### YAML

```
  Exclude: 
    - String
  Include: 
    - String

```

## Properties

**`Exclude`** 

The IAM role ARNs for stacks you want to exclude. The Hook will be invoked on all stacks except those initiated by the specified roles. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`Include`** 

The IAM role ARNs to target stacks associated with these roles. Only stack operations initiated by these roles will invoke the Hook. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption
