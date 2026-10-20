> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-firelensconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition FirelensConfiguration

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see Custom log routing in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Options" : {Key: Value, ...},
  "Type" : String
}

```

### YAML

```
  Options: 
    Key: Value
  Type: String

```

## Properties

**`Options`** 

The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}`. For more information, see Creating a task definition that uses a FireLens configuration in the Amazon Elastic Container Service Developer Guide. Note

Tasks hosted on AWS Fargate only support the `file` configuration file type. 

Required: No

Type: Object of String

Pattern: `.{1,}`

Update requires: Replacement

**`Type`** 

The log router to use. The valid values are `fluentd` or `fluentbit`. 

Required: No

Type: String

Allowed values: `fluentd | fluentbit`

Update requires: Replacement
