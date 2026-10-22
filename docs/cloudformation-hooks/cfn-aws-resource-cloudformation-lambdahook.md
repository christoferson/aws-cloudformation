> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-lambdahook.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::LambdaHook

The `AWS::CloudFormation::LambdaHook` resource creates and activates a Lambda Hook. You can use a Lambda Hook to evaluate your resources before allowing stack operations. This resource forwards requests for resource evaluation to a Lambda function.

For more information, see Lambda Hooks in the CloudFormation Hooks User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::CloudFormation::LambdaHook",
  "Properties" : {
      "Alias" : String,
      "AutoUpdate" : Boolean,
      "ExecutionRole" : String,
      "FailureMode" : String,
      "HookStatus" : String,
      "LambdaFunction" : String,
      "LoggingConfig" : LoggingConfig,
      "StackFilters" : StackFilters,
      "TargetFilters" : TargetFilters,
      "TargetOperations" : [ String, ... ]
    }
}

```

### YAML

```
Type: AWS::CloudFormation::LambdaHook
Properties:
  Alias: String
  AutoUpdate: Boolean
  ExecutionRole: String
  FailureMode: String
  HookStatus: String
  LambdaFunction: String
  LoggingConfig: 
    LoggingConfig
  StackFilters: 
    StackFilters
  TargetFilters: 
    TargetFilters
  TargetOperations: 
    - String

```

## Properties

**`Alias`** 

The type name alias for the Hook. This alias must be unique per account and Region.  

The alias must be in the form `Name1::Name2::Name3` and must not begin with `AWS`. For example, `Private::Lambda::MyTestHook`. 

Required: Yes

Type: String

Pattern: `^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`

Update requires: Replacement

**`AutoUpdate`**

Property description not available.

Required: No

Type: Boolean

Update requires: Replacement

**`ExecutionRole`** 

The IAM role that the Hook assumes to invoke your Lambda function. 

Required: Yes

Type: String

Pattern: `arn:.+:iam::[0-9]{12}:role/.+`

Maximum: `256`

Update requires: No interruption

**`FailureMode`** 

Specifies how the Hook responds when the Lambda function invoked by the Hook returns a `FAILED` response.  
`FAIL`: Prevents the action from proceeding. This is helpful for enforcing strict compliance or security policies. 
`WARN`: Issues warnings to users but allows actions to continue. This is useful for non-critical validations or informational checks. 
 

Required: Yes

Type: String

Allowed values: `FAIL | WARN`

Update requires: No interruption

**`HookStatus`** 

Specifies if the Hook is `ENABLED` or `DISABLED`. 

Required: Yes

Type: String

Allowed values: `ENABLED | DISABLED`

Update requires: No interruption

**`LambdaFunction`** 

Specifies the Lambda function for the Hook. You can use:  
The full Amazon Resource Name (ARN) without a suffix. 
A qualified ARN with a version or alias suffix. 
 

Required: Yes

Type: String

Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?(-iso([a-z])?)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`

Minimum: `1`

Maximum: `170`

Update requires: No interruption

**`LoggingConfig`** 

Contains logging configuration information for an extension. 

Required: No

Type: LoggingConfig

Update requires: Replacement

**`StackFilters`** 

Specifies the stack level filters for the Hook. 

Example stack level filter in JSON: 

```
"StackFilters": {"FilteringCriteria": "ALL", "StackNames": {"Exclude": [ "stack-1", "stack-2"]}}
```
 

Example stack level filter in YAML: 

```
StackFilters:
  FilteringCriteria: ALL
  StackNames:
    Exclude:
      - stack-1
      - stack-2
```
 

Required: No

Type: StackFilters

Update requires: No interruption

**`TargetFilters`** 

Specifies the target filters for the Hook. 

Example target filter in JSON: 

```
"TargetFilters": {"Actions": [ "CREATE", "UPDATE", "DELETE" ]}
```
 

Example target filter in YAML: 

```
TargetFilters:
  Actions:
    - CREATE
    - UPDATE
    - DELETE
```
 

Required: No

Type: TargetFilters

Update requires: No interruption

**`TargetOperations`** 

Specifies the list of operations the Hook is run against. For more information, see Hook targets in the CloudFormation Hooks User Guide. 

Valid values: `STACK` | `RESOURCE` | `CHANGE_SET` | `CLOUD_CONTROL` 

Required: Yes

Type: Array of String

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Hook Amazon Resource Name (ARN). For example: `arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyLambdaHook`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`HookArn`** 

Returns the ARN of a Lambda Hook. 

## Examples

 

### Creating a Lambda Hook in a template

The following example demonstrates how to create a Lambda Hook in a template.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Create a Lambda Hook",
    "Parameters": {
        "HookFunctionArn": {
            "Description": "Hook Lambda Function ARN",
            "Type": "String"
        },
        "HookName": {
            "Description": "The name of your Hook",
            "Type": "String",
            "Default": "Test::Lambda::Hook",
            "AllowedPattern": "^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$"
        }
    },
    "Resources": {
        "LambdaInvokerHookRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": ["hooks.cloudformation.amazonaws.com"]
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "LambdaInvokerHookPolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": ["lambda:InvokeFunction"],
                                    "Resource": {"Ref" : "HookFunctionArn"}
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "MyLambdaHook": {
            "Type": "AWS::CloudFormation::LambdaHook",
            "Properties": {
                "LambdaFunction": {"Ref" : "HookFunctionArn"},
                "HookStatus": "ENABLED",
                "TargetOperations": [
                    "RESOURCE",
                    "STACK"
                ],
                "FailureMode": "WARN",
                "Alias": {"Ref" : "HookName"},
                "ExecutionRole": {
                    "Fn::GetAtt": [
                        "LambdaInvokerHookRole",
                        "Arn"
                    ]
                },
                "TargetFilters": {
                    "Actions": [
                        "CREATE",
                        "UPDATE",
                        "DELETE"
                    ]
                },
                "StackFilters": {
                    "FilteringCriteria": "ALL",
                    "StackNames": {
                        "Exclude": [{"Ref" : "AWS::StackName"}]
                    }
                }
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: Create a Lambda Hook
Parameters:
  HookFunctionArn:
    Description: Hook Lambda Function ARN
    Type: String
  HookName:
    Description: The name of your Hook
    Type: String
    Default: 'Test::Lambda::Hook'
    AllowedPattern: '^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$'
Resources:
  LambdaInvokerHookRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - hooks.cloudformation.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: LambdaInvokerHookPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 'lambda:InvokeFunction'
                Resource: !Ref HookFunctionArn
  MyLambdaHook:
    Type: AWS::CloudFormation::LambdaHook
    Properties:
      LambdaFunction: !Ref HookFunctionArn
      HookStatus: ENABLED
      TargetOperations:
        - RESOURCE
        - STACK
      FailureMode: WARN
      Alias: !Ref HookName
      ExecutionRole: !GetAtt LambdaInvokerHookRole.Arn
      TargetFilters:
        Actions:
          - CREATE
          - UPDATE
          - DELETE
      StackFilters:
        FilteringCriteria: ALL
        StackNames:
          Exclude:
            - !Ref AWS::StackName
```
