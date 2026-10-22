> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-stack-level-filtering.html
> Downloaded: 2026-10-22

# CloudFormation Hooks stack level filters

You can add stack level filters to your CloudFormation Hooks to target specific stacks based on stack names and roles. This is useful in cases where you have multiple stacks with the same resource types, but the Hook is intended for specific stacks.

This section explains how these filters work and provides examples you can follow.

The basic structure of a Hook configuration without stack level filtering looks like this:

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "TargetFilters": {
        "Actions": [
          "CREATE",
          "UPDATE",
          "DELETE"
        ]
      }
    }
  }
}
```

For more information about the `HookConfiguration` syntax, see Hook configuration schema syntax reference.

To use stack level filters, add a `StackFilters` key under `HookConfiguration`. 

The `StackFilters` key has one required member and has two optional members. 
`FilteringCriteria` (required) 
`StackNames` (optional) 
`StackRoles` (optional) 

The `StackNames` or `StackRoles` properties are optional. However, you must specify at least one of these properties.

If you create a Hook that targets Cloud Control API operations, all stack level filters will be ignored. 

## `FilteringCriteria` 

`FilteringCriteria` is a required parameter that specifies the filtering behavior. It can be set to either `ALL` or `ANY`.  
`ALL` invokes the Hook if all the filters are matched. 
`ANY` invokes the Hook if any one filter is matched. 
 

## `StackNames` 

To specify one or more stack names as filters in your Hooks configuration, use the following JSON structure: 

```
"StackNames": {
  "Include": [
    "string"
  ],
  "Exclude": [
    "string"
  ]
}
```
 

You must specify one of the following:  
`Include`: List of stack names to include. Only the stacks specified in this list will invoke the Hook.  
Type: Array of strings 
Max items: 50 
Min items: 1 
`Exclude`: List of stack names to exclude. All stacks except those listed here will invoke the Hook.  
Type: Array of strings 
Max items: 50 
Min items: 1 
 
 

Each stack name in the `Include` and `Exclude` arrays must adhere to the following pattern and length requirements:  
Pattern: `^[a-zA-Z][-a-zA-Z0-9]*$` 
Max length: 128  
 

`StackNames` support concrete stack names and full wildcard matching. To see examples using wildcards, see Using wildcards with Hook target names. 

## `StackRoles` 

To specify one or more IAM roles as filters in your Hook configuration, use the following JSON structure: 

```
"StackRoles": {
  "Include": [
    "string"
  ],
  "Exclude": [
    "string"
  ]
}
```
 

You must specify one of the following:  
`Include`: List of IAM role ARNs to target stacks associated with these roles. Only stack operations initiated by these roles will invoke the Hook.  
Type: Array of strings 
Max items: 50 
Min items: 1 
`Exclude`: List of IAM role ARNs for stacks you want to exclude. The Hook will be invoked on all stacks except those initiated by the specified roles.  
Type: Array of strings 
Max items: 50 
Min items: 1 
 
 

Each stack role in the `Include` and `Exclude` arrays must adhere to the following pattern and length requirements:  
Pattern: `arn:.+:iam::[0-9]{12}:role/.+` 
Max length: 256 
 

`StackRoles` allow wildcard characters in the following ARN syntax sections:  
`partition` 
`account-id` 
`resource-id` 
 

To see examples using wildcards in the ARN syntax sections, see Using wildcards with Hook target names. 

## `Include` and `Exclude` 

Each filter (`StackNames` and `StackRoles`) has an `Include` list and `Exclude` list. Using `StackNames` as an example, the Hook is only invoked on the stacks that are specified in `Include` list. If stack names are only specified in the `Exclude` list, the hook is only invoked on stacks that are not in the `Exclude` list. If both `Include` and `Exclude` are specified, the Hook targets what's in the `Include` list and not what's in the `Exclude` list. 

For example, suppose you have four stacks: A, B, C, and D.  
`"Include": ["A","B"]` The Hook is invoked on A and B. 
`"Exclude": ["B"]` The Hook is invoked on A, C, and D. 
`"Include": ["A","B","C"], "Exclude": ["A","D"]` The Hook is invoked on B and C. 
`"Include": ["A","B","C"], "Exclude": ["A”,"B","C"]` The Hook is not invoked on any stack. 
 

## Examples of stack level filters 

This section provides examples you can follow to create stack level filters for CloudFormation Hooks. 

### Example 1: Include specific stacks 

The following example specifies an `Include` list. The Hook is only invoked on stacks named `stack-test-1`, `stack-test-2` and `stack-test-3`. 

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "StackFilters": {
        "FilteringCriteria": "ALL",
        "StackNames": {
          "Include": [
            "stack-test-1",
            "stack-test-2",
            "stack-test-3"
          ]
        }
      }
    }
  }
}
```
 

### Example 2: Exclude specific stacks 

If the stack names are instead added to the `Exclude` list, the Hook is invoked on any stack that is not named `stack-test-1`, `stack-test-2` or `stack-test-3`. 

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "StackFilters": {
        "FilteringCriteria": "ALL",
        "StackNames": {
          "Exclude": [
            "stack-test-1",
            "stack-test-2",
            "stack-test-3"
          ]
        }
      }
    }
  }
}
```
 

### Example 3: Combining include and exclude 

If `Include` and `Exclude` lists aren't specified, the Hook is only invoked on the stacks in the `Include` that aren't in the `Exclude` list. In the following example, the Hook is only invoked on `stack-test-3`. 

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "StackFilters": {
        "FilteringCriteria": "ALL",
        "StackNames": {
          "Include": [
            "stack-test-1",
            "stack-test-2",
            "stack-test-3"
          ],
          "Exclude": [
            "stack-test-1",
            "stack-test-2"
          ]
        }
      }
    }
  }
}
```
 

### Example 4: Combining stack names and roles with `ALL` criteria 

The following Hook includes three stack names, and one stack role. Because the `FilteringCriteria` is specified as `ALL`, the Hook is only invoked for stack that have both a matching stack name and the matching stack role. 

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "StackFilters": {
        "FilteringCriteria": "ALL",
        "StackNames": {
          "Include": [
            "stack-test-1",
            "stack-test-2",
            "stack-test-3"
          ]
        },
        "StackRoles": {
          "Include": ["arn:aws:iam::123456789012:role/hook-role"]
        }
      }
    }
  }
}
```
 

### Example 5: Combining stack names and roles with `ANY` criteria 

The following Hook includes three stack names, and one stack role. Because the `FilteringCriteria` is specified as `ANY`, the Hook is invoked for stack that have either a matching stack name or the matching stack role. 

```
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "HookInvocationStatus": "ENABLED",
      "TargetOperations": [
        "STACK",
        "RESOURCE"
      ],
      "FailureMode": "WARN",
      "Properties": {},
      "StackFilters": {
        "FilteringCriteria": "ANY",
        "StackNames": {
          "Include": [
            "stack-test-1",
            "stack-test-2",
            "stack-test-3"
          ]
        },
        "StackRoles": {
            "Include": ["arn:aws:iam::123456789012:role/hook-role"]
        }
      }
    }
  }
}
```
