> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-executecommandconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Cluster ExecuteCommandConfiguration

The details of the execute command configuration.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "KmsKeyId" : String,
  "LogConfiguration" : ExecuteCommandLogConfiguration,
  "Logging" : String
}

```

### YAML

```
  KmsKeyId: String
  LogConfiguration: 
    ExecuteCommandLogConfiguration
  Logging: String

```

## Properties

**`KmsKeyId`** 

Specify an AWS Key Management Service key ID to encrypt the data between the local client and the container. 

Required: No

Type: String

Update requires: No interruption

**`LogConfiguration`** 

The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket. When `logging=OVERRIDE` is specified, a `logConfiguration` must be provided. 

Required: No

Type: ExecuteCommandLogConfiguration

Update requires: No interruption

**`Logging`** 

The log setting to use for redirecting logs for your execute command results. The following log settings are available.  
`NONE`: The execute command session is not logged. 
`DEFAULT`: The `awslogs` configuration in the task definition is used. If no logging parameter is specified, it defaults to this value. If no `awslogs` log driver is configured in the task definition, the output won't be logged. 
`OVERRIDE`: Specify the logging details as a part of `logConfiguration`. If the `OVERRIDE` logging option is specified, the `logConfiguration` is required. 
 

Required: No

Type: String

Allowed values: `NONE | DEFAULT | OVERRIDE`

Update requires: No interruption

## See also 
  Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined
