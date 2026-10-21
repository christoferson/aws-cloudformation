> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-configurationprofile-validators.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ConfigurationProfile Validators

A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended. To validate your application configuration data, you provide a schema or an AWS Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid. For more information, see About validators in the AWS AppConfig User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Content" : String,
  "Type" : String
}

```

### YAML

```
  Content: String
  Type: String

```

## Properties

**`Content`** 

Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function. 

Required: No

Type: String

Minimum: `0`

Maximum: `32768`

Update requires: No interruption

**`Type`** 

AWS AppConfig supports validators of type `JSON_SCHEMA` and `LAMBDA` 

Required: No

Type: String

Allowed values: `JSON_SCHEMA | LAMBDA`

Update requires: No interruption
