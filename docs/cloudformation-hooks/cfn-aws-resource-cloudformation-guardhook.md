> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-guardhook.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook

The `AWS::CloudFormation::GuardHook` resource creates and activates a Guard Hook. Using the Guard domain specific language (DSL), you can author Guard Hooks to evaluate your resources before allowing stack operations.

For more information, see Guard Hooks in the CloudFormation Hooks User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::CloudFormation::GuardHook",
  "Properties" : {
      "Alias" : String,
      "ExecutionRole" : String,
      "FailureMode" : String,
      "HookStatus" : String,
      "LogBucket" : String,
      "Options" : Options,
      "RuleLocation" : S3Location,
      "StackFilters" : StackFilters,
      "TargetFilters" : TargetFilters,
      "TargetOperations" : [ String, ... ]
    }
}

```

### YAML

```
Type: AWS::CloudFormation::GuardHook
Properties:
  Alias: String
  ExecutionRole: String
  FailureMode: String
  HookStatus: String
  LogBucket: String
  Options: 
    Options
  RuleLocation: 
    S3Location
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

The alias must be in the form `Name1::Name2::Name3` and must not begin with `AWS`. For example, `Private::Guard::MyTestHook`. 

Required: Yes

Type: String

Pattern: `^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`

Update requires: Replacement

**`ExecutionRole`** 

The IAM role that the Hook assumes to retrieve your Guard rules from S3 and optionally write a detailed Guard output report back. 

Required: Yes

Type: String

Pattern: `arn:.+:iam::[0-9]{12}:role/.+`

Maximum: `256`

Update requires: Replacement

**`FailureMode`** 

Specifies how the Hook responds when rules fail their evaluation.  
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

**`LogBucket`** 

Specifies the name of an S3 bucket to store the Guard output report. This report contains the results of your Guard rule validations. 

Required: No

Type: String

Update requires: No interruption

**`Options`** 

Specifies the S3 location of your input parameters. 

Required: No

Type: Options

Update requires: No interruption

**`RuleLocation`** 

Specifies the S3 location of your Guard rules. 

Required: Yes

Type: S3Location

Update requires: No interruption

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Hook Amazon Resource Name (ARN). For example: `arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyGuardHook`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`HookArn`** 

Returns the ARN of a Guard Hook. 

## Examples

 

### Creating a Guard Hook in a template

The following example demonstrates how to create a Guard Hook in a template.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Create a Guard Hook",
    "Parameters": {
        "GuardRulesS3Bucket": {
            "Description": "S3 bucket where your rules are",
            "Type": "String"
        },
        "GuardRulesS3Path": {
            "Description": "Location within GuardRulesS3Bucket where your Guard rules are",
            "Type": "String"
        },
        "GuardOutputBucket": {
            "Description": "S3 bucket to put Guard output",
            "Type": "String"
        },
        "HookName": {
            "Description": "The name of your Hook",
            "Type": "String",
            "Default": "Test::Guard::Hook",
            "AllowedPattern": "^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$"
        }
    },
    "Resources": {
        "GuardHookRole": {
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
                        "PolicyName": "root",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject",
                                        "s3:GetObjectVersion",
                                        "s3:ListBucket"
                                    ],
                                    "Resource": [
                                        {"Fn::Sub": "arn:aws:s3:::${GuardRulesS3Bucket}"},
                                        {"Fn::Sub": "arn:aws:s3:::${GuardRulesS3Bucket}/*"}
                                    ]
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": ["s3:PutObject"],
                                    "Resource": [{"Fn::Sub": "arn:aws:s3:::${GuardOutputBucket}/*"}]
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "GuardHook": {
            "Type": "AWS::CloudFormation::GuardHook",
            "Properties": {
                "TargetOperations": [
                    "RESOURCE",
                    "STACK"
                ],
                "Alias": {"Ref": "HookName"},
                "ExecutionRole": {
                    "Fn::GetAtt": [
                        "GuardHookRole",
                        "Arn"
                    ]
                },
                "FailureMode": "WARN",
                "HookStatus": "ENABLED",
                "LogBucket": {"Ref": "GuardOutputBucket"},
                "RuleLocation": {
                    "Uri": {"Fn::Sub": "s3://${GuardRulesS3Bucket}/${GuardRulesS3Path}"}
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
                        "Exclude": [{"Ref": "AWS::StackName"}]
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
Description: Create a Guard Hook
Parameters:
  GuardRulesS3Bucket:
    Description: S3 bucket where your rules are
    Type: String
  GuardRulesS3Path:
    Description: Location within GuardRulesS3Bucket where your Guard rules are
    Type: String
  GuardOutputBucket:
    Description: S3 bucket to put Guard output
    Type: String
  HookName:
    Description: The name of your Hook
    Type: String
    Default: 'Test::Guard::Hook'
    AllowedPattern: '^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$'
Resources:
  GuardHookRole:
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
        - PolicyName: root
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetObjectVersion
                  - s3:ListBucket
                Resource:
                  - !Sub arn:aws:s3:::${GuardRulesS3Bucket}
                  - !Sub arn:aws:s3:::${GuardRulesS3Bucket}/*
              - Effect: Allow
                Action:
                  - s3:PutObject
                Resource:
                  - !Sub arn:aws:s3:::${GuardOutputBucket}/*
  GuardHook:
    Type: AWS::CloudFormation::GuardHook
    Properties:
      TargetOperations:
        - RESOURCE
        - STACK
      Alias: !Ref HookName
      ExecutionRole: !GetAtt GuardHookRole.Arn
      FailureMode: WARN
      HookStatus: ENABLED
      LogBucket: !Ref GuardOutputBucket
      RuleLocation:
        Uri: !Sub s3://${GuardRulesS3Bucket}/${GuardRulesS3Path}
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
