> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-stacknames.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook StackNames

Specifies the stack names for the `StackFilters` property type to include or exclude specific stacks from Hook invocations.

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

The stack names to exclude. All stacks except those listed here will invoke the Hook. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`Include`** 

The stack names to include. Only the stacks specified in this list will invoke the Hook. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption
