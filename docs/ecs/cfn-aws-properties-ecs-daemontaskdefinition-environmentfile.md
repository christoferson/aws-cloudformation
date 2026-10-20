> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-environmentfile.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition EnvironmentFile

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored.

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they're processed from the top down. We recommend that you use unique variable names. For more information, see Use a file to pass environment variables to a container in the Amazon Elastic Container Service Developer Guide.

Environment variable files are objects in Amazon S3 and all Amazon S3 security considerations apply. 

You must use the following platforms for the Fargate launch type: 
Linux platform version `1.4.0` or later. 
Windows platform version `1.0.0` or later. 

Consider the following when using the Fargate launch type: 
The file is handled like a native Docker env-file. 
There is no support for shell escape handling. 
The container entry point interperts the `VARIABLE` values. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : String,
  "Value" : String
}

```

### YAML

```
  Type: String
  Value: String

```

## Properties

**`Type`** 

The file type to use. Environment files are objects in Amazon S3. The only supported value is `s3`. 

Required: No

Type: String

Allowed values: `s3`

Update requires: Replacement

**`Value`** 

The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file. 

Required: No

Type: String

Update requires: Replacement
