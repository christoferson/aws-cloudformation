> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-environmentvariable.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline EnvironmentVariable

The environment variables for the action.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "Type" : String,
  "Value" : String
}

```

### YAML

```
  Name: String
  Type: String
  Value: String

```

## Properties

**`Name`**
 

The environment variable name in the key-value pair. 

Required: Yes

Type: String

Pattern: `[A-Za-z0-9_]+`

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`Type`**
 

Specifies the type of use for the environment variable value. The value can be either `PLAINTEXT` or `SECRETS_MANAGER`. If the value is `SECRETS_MANAGER`, provide the Secrets reference in the EnvironmentVariable value. 

Required: No

Type: String

Allowed values: `PLAINTEXT | SECRETS_MANAGER`

Update requires: No interruption

**`Value`**
 

The environment variable value in the key-value pair. 

Required: Yes

Type: String

Pattern: `.*`

Minimum: `1`

Maximum: `2000`

Update requires: No interruption

