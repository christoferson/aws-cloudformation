> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-stackfilters.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook StackFilters

The `StackFilters` property type specifies stack level filters for a Hook.

The `StackNames` or `StackRoles` properties are optional. However, you must specify at least one of these properties.

For more information, see CloudFormation Hooks stack level filters.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "FilteringCriteria" : String,
  "StackNames" : StackNames,
  "StackRoles" : StackRoles
}

```

### YAML

```
  FilteringCriteria: String
  StackNames: 
    StackNames
  StackRoles: 
    StackRoles

```

## Properties

**`FilteringCriteria`** 

The filtering criteria.  
All stack names and stack roles (`All`): The Hook will only be invoked when all specified filters match. 
Any stack names and stack roles (`Any`): The Hook will be invoked if at least one of the specified filters match. 
 

Required: Yes

Type: String

Allowed values: `ALL | ANY`

Update requires: No interruption

**`StackNames`** 

Includes or excludes specific stacks from Hook invocations. 

Required: No

Type: StackNames

Update requires: No interruption

**`StackRoles`** 

Includes or excludes specific stacks from Hook invocations based on their associated IAM roles. 

Required: No

Type: StackRoles

Update requires: No interruption
