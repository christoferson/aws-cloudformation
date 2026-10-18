> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-variabledeclaration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline VariableDeclaration

A variable declared at the pipeline level.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "DefaultValue" : String,
  "Description" : String,
  "Name" : String
}

```

### YAML

```
  DefaultValue: String
  Description: String
  Name: String

```

## Properties

**`DefaultValue`**
 

The value of a pipeline-level variable. 

Required: No

Type: String

Pattern: `.*`

Minimum: `1`

Maximum: `1000`

Update requires: No interruption

**`Description`**
 

The description of a pipeline-level variable. It's used to add additional context about the variable, and not being used at time when pipeline executes. 

Required: No

Type: String

Pattern: `.*`

Minimum: `0`

Maximum: `200`

Update requires: No interruption

**`Name`**
 

The name of a pipeline-level variable. 

Required: Yes

Type: String

Pattern: `[A-Za-z0-9@\-_]+`

Minimum: `1`

Maximum: `128`

Update requires: No interruption

