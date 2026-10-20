> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceAwsLogsConfiguration

Specifies the Amazon CloudWatch Logs configuration for the Express service container.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "LogGroup" : String,
  "LogStreamPrefix" : String
}

```

### YAML

```
  LogGroup: String
  LogStreamPrefix: String

```

## Properties

**`LogGroup`** 

The name of the CloudWatch Logs log group to send container logs to. 

Required: Yes

Type: String

Update requires: No interruption

**`LogStreamPrefix`** 

The prefix for the CloudWatch Logs log stream names. The default for an Express service is `ecs`. 

Required: Yes

Type: String

Update requires: No interruption
