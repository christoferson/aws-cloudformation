> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-hooktypeconfig.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::HookTypeConfig

The `AWS::CloudFormation::HookTypeConfig` resource specifies the configuration of an activated Hook.

For information about the CloudFormation registry, see Managing extensions with the CloudFormation registry in the CloudFormation User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::CloudFormation::HookTypeConfig",
  "Properties" : {
      "Configuration" : String,
      "ConfigurationAlias" : String,
      "TypeArn" : String,
      "TypeName" : String
    }
}

```

### YAML

```
Type: AWS::CloudFormation::HookTypeConfig
Properties:
  Configuration: String
  ConfigurationAlias: String
  TypeArn: String
  TypeName: String

```

## Properties

**`Configuration`** 

Specifies the activated Hook type configuration, in this AWS account and AWS Region. 

You must specify either `TypeName` and `Configuration` or `TypeArn` and `Configuration`. 

Required: Conditional

Type: String

Pattern: `[\s\S]+`

Update requires: No interruption

**`ConfigurationAlias`** 

An alias by which to refer to this configuration data. 

Defaults to `default` alias. Hook types currently support default configuration alias. 

Required: No

Type: String

Allowed values: `default`

Pattern: `^[a-zA-Z0-9]{1,256}$`

Update requires: Replacement

**`TypeArn`** 

The Amazon Resource Number (ARN) for the Hook to set `Configuration` for. 

You must specify either `TypeName` and `Configuration` or `TypeArn` and `Configuration`. 

Required: Conditional

Type: String

Pattern: `^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$`

Update requires: No interruption

**`TypeName`** 

The unique name for your Hook. Specifies a three-part namespace for your Hook, with a recommended pattern of `Organization::Service::Hook`. 

You must specify either `TypeName` and `Configuration` or `TypeArn` and `Configuration`. 

Required: Conditional

Type: String

Pattern: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the resource version. For example:

 `arn:aws:cloudformation:us-west-2:123456789012:type-configuration/hook/My-Sample-Hook/default` 

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`ConfigurationArn`** 

The Amazon Resource Number (ARN) of the activated Hook type configuration in this account and Region. 

## Examples
Specifying the configuration of a Hook using TypeName
Specifying the configuration of a Hook using TypeArn
 

### Specifying the configuration of a Hook using TypeName

The following example demonstrates how to specify a new Hook configuration with the `TypeName` property type.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "HookTypeConfig": {
            "Type": "AWS::CloudFormation::HookTypeConfig",
            "Properties": {
                "TypeName": "My::Sample::Hook",
                "Configuration": "{\"CloudFormationConfiguration\":{\"HookConfiguration\":{\"HookInvocationStatus\":\"ENABLED\",\"FailureMode\":\"WARN\",\"Properties\":{\"limitSize\": \"1\",\"encryptionAlgorithm\": \"aws:kms\"}}}}"
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookTypeConfig:
    Type: AWS::CloudFormation::HookTypeConfig
    Properties:
      TypeName: My::Sample::Hook
      Configuration: '{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus":"ENABLED","FailureMode":"WARN","Properties":{"limitSize": "1","encryptionAlgorithm": "aws:kms"}}}}'
```
 

### Specifying the configuration of a Hook using TypeArn

The following example demonstrates how to specify a new Hook configuration with the `TypeArn` property type.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "HookTypeConfig": {
            "Type": "AWS::CloudFormation::HookTypeConfig",
            "Properties": {
                "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/My-Sample-Hook",
                "Configuration": "{\"CloudFormationConfiguration\":{\"HookConfiguration\":{\"HookInvocationStatus\":\"ENABLED\",\"FailureMode\":\"WARN\",\"Properties\":{\"limitSize\": \"1\",\"encryptionAlgorithm\": \"aws:kms\"}}}}"
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookTypeConfig:
    Type: AWS::CloudFormation::HookTypeConfig
    Properties:
      TypeArn: arn:aws:cloudformation:us-west-2:123456789012:type/hook/My-Sample-Hook
      Configuration: '{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus":"ENABLED","FailureMode":"WARN","Properties":{"limitSize": "1","encryptionAlgorithm": "aws:kms"}}}}'
```
