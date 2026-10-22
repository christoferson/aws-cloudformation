> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectcontainerconfiguration.html
> Downloaded: 2026-10-21

# AWS::ECS::Service ServiceConnectContainerConfiguration

Contains a configuration setting for the Service Connect proxy container, such as the log level. Specify exactly one member in each object.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "LogLevel" : String
}

```

### YAML

```
  LogLevel: String

```

## Properties

**`LogLevel`** 

The log level of the Service Connect proxy container. Set the log level to `debug` to collect more detailed proxy logs when you troubleshoot connectivity issues between services, and set it back to `info` when you finish. Debug logging increases the volume of logs that the proxy container writes. If you don't specify a log level, the default is `info`. 

Required: No

Type: String

Allowed values: `debug | info`

Update requires: No interruption
