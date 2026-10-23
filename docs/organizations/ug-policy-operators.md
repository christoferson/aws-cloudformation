> Source: https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html
> Downloaded: 2026-10-23

# Inheritance operators

Inheritance operators control how inherited policies and account policies merge into the account's effective policy. These operators include value-setting operators and child control operators. 

When you use the visual editor in the AWS Organizations console, you can use only the `@@assign` operator. Other operators are considered an advanced feature. To use the other operators, you must manually author the JSON policy. Experienced policy authors can use inheritance operators to control what values are applied to the effective policy and limit what changes child policies can make. 

For information about how policy inheritance works in an organization, see Inheritance examples. 

## Value-setting operators 

You can use the following value-setting operators to control how your policy interacts with its parent policies:  
`@@assign` – Overwrites any inherited policy settings with the specified settings. If the specified setting isn't inherited, this operator adds it to the effective policy. This operator can apply to any policy setting of any type.  
For single-valued settings, this operator replaces the inherited value with the specified value. 
For multi-valued settings (JSON arrays), this operator removes any inherited values and replaces them with the values specified by this policy. 
`@@append` – Adds the specified settings (without removing any) to the inherited ones. If the specified setting isn't inherited, this operator adds it to the effective policy. You can use this operator with only multi-valued settings.  
This operator adds the specified values to any values in the inherited array. 
`@@remove` – Removes the specified inherited settings from the effective policy, if they exist. You can use this operator with only multi-valued settings.  
This operator removes only the specified values from the array of values inherited from the parent policies. Other values can continue to exist in the array and can be inherited by child policies. 
 
 

## Child control operators 

Using child control operators is optional. You can use the `@@operators_allowed_for_child_policies` operator to control which value-setting operators child policies can use. You can allow all operators, some specific operators, or no operators. By default, all operators (`@@all`) are allowed.  
`"@@operators_allowed_for_child_policies"`:`["@@all"]` – Child OUs and accounts can use any operator in policies. By default, all operators are allowed in child policies. 
`"@@operators_allowed_for_child_policies"`:`["@@assign", "@@append", "@@remove"]` – Child OUs and accounts can use only the specified operators in child policies. You can specify one or more value-setting operators in this child control operator. 
`"@@operators_allowed_for_child_policies"`:`["@@none"]` – Child OUs and accounts can't use operators in policies. You can use this operator to effectively lock in the values that are defined in a parent policy so that child policies can't add, append, or remove those values. 
 Note

If an inherited child control operator limits the use of an operator, you can't reverse that rule in a child policy. If you include child control operators in a parent policy, they limit the value-setting operators in all child policies.
