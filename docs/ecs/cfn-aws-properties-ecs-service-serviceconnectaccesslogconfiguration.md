> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectaccesslogconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceConnectAccessLogConfiguration

Configuration for Service Connect access logging. Access logs provide detailed information about requests made to your service, including request patterns, response codes, and timing data for debugging and monitoring purposes.Note

To enable access logs, you must also specify a `logConfiguration` in the `serviceConnectConfiguration`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Format" : String,
  "IncludeQueryParameters" : String
}

```

### YAML

```
  Format: String
  IncludeQueryParameters: String

```

## Properties

**`Format`** 

The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools. 

Required: Yes

Type: String

Allowed values: `TEXT | JSON`

Update requires: No interruption

**`IncludeQueryParameters`** 

Specifies whether to include query parameters in Service Connect access logs. 

When enabled, query parameters from HTTP requests are included in the access logs. Consider security and privacy implications when enabling this feature, as query parameters may contain sensitive information such as request IDs and tokens. By default, this parameter is `DISABLED`. 

Required: No

Type: String

Allowed values: `DISABLED | ENABLED`

Update requires: No interruption
