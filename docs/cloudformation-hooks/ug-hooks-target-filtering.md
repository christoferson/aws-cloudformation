> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-target-filtering.html
> Downloaded: 2026-10-22

# CloudFormation Hooks target filters

This topic provides guidance on configuring target filters for CloudFormation Hooks. You can use target filters for more granular control over when and on which resources your Hook is invoked. You can configure filters ranging from simple resource type targeting to more complex combinations of resource types, actions, and invocation points.

To specify one or more stack names as filters in your Hooks configuration, add a `TargetFilters` key under `HookConfiguration`.

`TargetFilters` supports the following properties.   

**`Actions`**  

A string array that specifies the actions to target. For an example, see Example 1: Basic target filter. 

Valid values: `CREATE` | `UPDATE` | `DELETE` Note

For `RESOURCE`, `STACK`, and `CLOUD_CONTROL` targets, all target actions are applicable. For `CHANGE_SET` targets, only the `CREATE` action is applicable. For more information, see Hook targets.  

**`InvocationPoints`**  

A string array that specifies the invocation points to target. 

Valid values: `PRE_PROVISION`  

**`TargetNames`**  

A string array that specifies the resource type names to target, for example, `AWS::S3::Bucket`.  

Target names support concrete target names and full wildcard matching. For more information, see Using wildcards with Hook target names. 

Pattern: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$` 

Maximum: `50`  

**`Targets`**  

An object array that specifies the list of targets to use for target filtering. 

Each target in the targets array has the following properties.   

**`Actions`**  

The action for the specified target. 

Valid values: `CREATE` | `UPDATE` | `DELETE`  

**`InvocationPoints`**  

The invocation point for the specified target. 

Valid values: `PRE_PROVISION`  

**`TargetNames`**  

The resource type name to target.    Note

You can't include both the `Targets` object array and the `TargetNames`, `Actions`, or `InvocationPoints` arrays at the same time. If you want to use these three items and `Targets`, you must include them within the `Targets` object array. For an example, see Example 2: Using the Targets object array. 

## Examples of target filters 

This section provides examples you can follow to create target filters for CloudFormation Hooks. 

### Example 1: Basic target filter 

To create a basic target filter that focuses on specific resource types, use the `TargetFilters` object with the `Actions` array. The following target filter configuration will invoke the Hook on all `Create`, `Update`, and `Delete` actions for the specified target operations (in this case, both `RESOURCE` and `STACK` operations). 

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
           "Create",
           "Update",
           "Delete"
        ]
      }
    }
  }
}
```
 

### Example 2: Using the `Targets` object array 

For more advanced filters, you can use the `Targets` object array to list specific target, action, and invocation point combinations. This following target filter configuration will invoke the Hook before `CREATE` and `UPDATE` actions on S3 buckets and DynamoDB tables. It applies to both `STACK` and `RESOURCE` operations. 

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
        "Targets": [
          {
             "TargetName": "AWS::S3::Bucket",
             "Action": "CREATE",
             "InvocationPoint": "PRE_PROVISION"
          },
          {
             "TargetName": "AWS::S3::Bucket",
             "Action": "UPDATE",
             "InvocationPoint": "PRE_PROVISION"
          },
          {
             "TargetName": "AWS::DynamoDB::Table",
             "Action": "CREATE",
             "InvocationPoint": "PRE_PROVISION"
          },
          {
             "TargetName": "AWS::DynamoDB::Table",
             "Action": "UPDATE",
             "InvocationPoint": "PRE_PROVISION"
          }
        ]               
      }
    }
  }
}
```
