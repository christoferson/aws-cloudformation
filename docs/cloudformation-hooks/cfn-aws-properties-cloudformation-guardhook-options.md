> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-options.html
> Downloaded: 2026-10-22

# AWS::CloudFormation::GuardHook Options

Specifies the input parameters for a Guard Hook.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "InputParams" : S3Location
}

```

### YAML

```
  InputParams: 
    S3Location

```

## Properties

**`InputParams`** 

Specifies the S3 location of input parameter files for your Guard rules. You can specify either a single S3 location or an array of up to 10 S3 locations. 

If you specify multiple input parameter files, each file must contain unique top-level keys. If duplicate top-level keys exist across files, Guard returns a failure status. 

Required: No

Type: S3Location

Update requires: No interruption
