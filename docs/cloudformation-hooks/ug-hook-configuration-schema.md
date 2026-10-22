> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.html
> Downloaded: 2026-10-22

# Hook configuration schema syntax reference

This section outlines the schema syntax used to configure Hooks. CloudFormation uses this configuration schema at runtime when invoking a Hook in an AWS account. 

To enable your Hook to proactively inspect the configuration of your stack, set the `HookInvocationStatus` to `ENABLED` after the Hook has been registered and activated in your account. Topics
Hook configuration schema properties
Hook configuration examples
CloudFormation Hooks stack level filters
CloudFormation Hooks target filters
Using wildcards with Hook target names
Note

The maximum amount of data that a Hook’s configuration can store is 300 KB. This is in addition to all the constraints imposed on `Configuration` request parameter of SetTypeConfiguration operation. 

## Hook configuration schema properties 

The following schema is the structure for a Hook configuration schema. 

```
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "HookInvocationStatus": "ENABLED",
            "TargetOperations": ["STACK"],
            "FailureMode": "FAIL",
            "EncryptionConfiguration": {
                "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
            },
            "Properties": {
                ...
            }
        }
    }
}
```
   

**`HookConfiguration`**  

Hook configuration supports activating or deactivating Hooks at stack level, failure modes, and Hook properties values. 

The Hook configuration supports the following properties.   

**`HookInvocationStatus`**  

Specifies if the Hook is `ENABLED` or `DISABLED`. 

Valid values: `ENABLED` | `DISABLED`  

**`TargetOperations`**  

Specifies the list of operations the Hook is run against. For more information, see Hook targets. 

Valid values: `STACK` | `RESOURCE` | `CHANGE_SET` | `CLOUD_CONTROL`   

**`TargetStacks`**  

Available for backward compatibility. Use `HookInvocationStatus` instead. 

If the mode is set to `ALL`, the Hook applies to all stacks in your account during a `CREATE`, `UPDATE`, or `DELETE` resource operation. 

If the mode is set to `NONE`, the Hook won't apply to stacks in your account. 

Valid values: `ALL` | `NONE`  

**`FailureMode`**  

This field tells the service how to treat Hook failures.  
If the mode is set to `FAIL`, and the Hook fails, then the fail configuration stops provisioning resources and rolls back the stack. 
If the mode is set to `WARN` and the Hook fails, then the warn configuration allows provisioning to continue with a warning message. 
 

Valid values: `FAIL` | `WARN`  

**`EncryptionConfiguration`**  

Specifies encryption settings for Hook annotations data.   

**`KmsKeyId`**  

The alias, alias ARN, key ID, or key ARN of the symmetric encryption AWS KMS key used to encrypt Hook annotations data. For more information, see KeyId in the AWS KMS docs. 

Before you can create Hooks with customer managed AWS KMS keys, your user or role must have AWS KMS permissions to `DescribeKey` and `GenerateDataKey`. For more information, see AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest.     

**`Properties`**  

Specifies Hook runtime properties. These should match the shape of the properties supported by Hooks schema.     

## Hook configuration examples 

For examples of configuring Hooks from the AWS CLI, see the following sections:  
Activate a proactive control-based Hook (AWS CLI) 
Activate a Guard Hook (AWS CLI) 
Activate a Lambda Hook (AWS CLI)
