> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/wildcard-hook-targets.html
> Downloaded: 2026-10-22

# Using wildcards with Hook target names

You can use wildcards as part of the target name. You can use wildcard characters (`*` and `?`) within your Hook target names. The asterisk (`*`) represents any combination of characters. The question mark (`?`) represents any single character. You can use multiple `*` and `?` characters in a target name.Example: Examples of target name wildcards in Hook schemas

The following example targets all resource types supported by Amazon S3.

```
{
...
    "handlers": {
       "preCreate": {
            "targetNames": [
                "AWS::S3::*"
            ],
            "permissions": []
       }
    }
...
}
```

The following example matches all resource types that have "Bucket" in the name.

```
{
...
    "handlers": {
       "preCreate": {
            "targetNames": [
                "AWS::*::Bucket*"
            ],
            "permissions": []
       }
    }
...
}
```

The `AWS::*::Bucket*` might resolve to any of the following concrete resource types: 
`AWS::Lightsail::Bucket` 
`AWS::S3::Bucket` 
`AWS::S3::BucketPolicy` 
`AWS::S3Outpost::Bucket` 
`AWS::S3Outpost::BucketPolicy` 
Example: Examples of target name wildcards in Hook configuration schemas

The following example configuration invokes the Hook for `CREATE` operations on all Amazon S3 resource types, and for `UPDATE` operations on all named table resource types, such as `AWS::DynamobDB::Table` or `AWS::Glue::Table`.

```
{
   "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {},
            "TargetFilters":{
                 "Targets": [
                    {
                        "TargetName": "AWS::S3::*",
                        "Action": "CREATE",
                        "InvocationPoint": "PRE_PROVISION"
                    },
                    {
                        "TargetName": "AWS::*::Table",
                        "Action": "UPDATE",
                        "InvocationPoint": "PRE_PROVISION"
                    }
                 ]               
            }
        }
   }
}
```

The following example configuration invokes the Hook for `CREATE` and `UPDATE` operations on all Amazon S3 resource types, and also for `CREATE` and `UPDATE` operations on all named table resource types, such as `AWS::DynamobDB::Table` or `AWS::Glue::Table`.

```
{
   "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {},
            "TargetFilters":{
                "TargetNames": [
                    "AWS::S3::*",
                    "AWS::*::Table"
                ],
                "Actions": [
                    "CREATE",
                    "UPDATE"
                ],
                "InvocationPoints": [
                    "PRE_PROVISION"
                ]
            }
        }
   }
}
```
Example: `Include` specific stacks

The following examples specifies an `Include` list. The Hook is only invoked if the stack names begins with `stack-test-`.

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
            "stack-test-*"
          ]
        }
      }
    }
  }
}
```
Example: `Exclude` specific stacks

The following examples specifies an `Exclude` list. The Hook is invoked on any stack that does not begin with `stack-test-`.

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
            "stack-test-*"
          ]
        }
      }
    }
  }
}
```
Example: Combining `Include` and `Exclude` for specific stacks

If `Include` and `Exclude` lists are specified, the Hook is only invoked on stacks matching in the `Include` that do not match in the `Exclude` list. In the following example, the Hook is invoked on all stacks that begin with `stack-test-` except for stacks named `stack-test-1`, `stack-test-2`, and `stack-test-3`.

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
            "stack-test-*"
          ],
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
Example: `Include` specific roles

The following example specifies an `Include` list with two wildcard patterns. The first entry will run the Hook for any role that begins with `hook-role` in any `partition` and `account-id`. The second entry will run any for any role in any `partition` that belongs to `account-id` `123456789012`.

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
        "StackRoles": {
          "Include": [
            "arn:*:iam::*:role/hook-role*",
            "arn:*:iam::123456789012:role/*
          ]
        }
      }
    }
  }
}
```
Example: `Exclude` specific roles

The following examples specifies an `Exclude` list with two wildcard patterns. The first entry will skip Hook execution when a role has `exempt` in its name in any `partition` and any `account-id`. The second entry will skip Hook execution when a role belonging to `account-id` `123456789012` is used with the stack operation.

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
        "StackRoles": {
          "Exclude": [
            "arn:*:iam::*:role/*exempt*",
            "arn:*:iam::123456789012:role/*
          ]
        }
      }
    }
  }
}
```
Example: Combining `Include` and `Exclude` for specific role ARN patterns

If `Include` and `Exclude` lists are specified, the Hook is only invoked on stacks used with roles that match those in `Include` that do not match in the `Exclude` list. In the following example, the Hook is invoked on stack operations with any `partition`, `account-id`, and `role` name, except if the role belongs to `account-id` `123456789012`.

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
        "StackRoles": {
          "Include": [
            "arn:*:iam::*:role/*"
          ],
          "Exclude": [
            "arn:*:iam::123456789012:role/*"
          ]
        }
      }
    }
  }
}
```
Example: Combining stack names and roles with all criteria

The following Hook includes one stack name wildcard and one stack role wildcard. Because the `FilteringCriteria` is specified as `ALL`, the Hook is only invoked for stacks that have both, the matching `StackName` and matching `StackRoles`.

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
            "stack-test-*"
          ]
        },
        "StackRoles": {
          "Include": ["arn:*:iam::*:role/hook-role*"]
        }
      }
    }
  }
}
```
Example: Combining `StackNames` and `StackRoles` with any criteria

The following Hook includes one stack name wildcard and one stack role wildcard. Because the `FilteringCriteria` is specified as `ANY`, the Hook is invoked for the stack that have either matching `StackNames` or matching `StackRoles`.

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
            "stack-test-*"
          ]
        },
        "StackRoles": {
            "Include": ["arn:*:iam::*:role/hook-role*"]
        }
      }
    }
  }
}
```
