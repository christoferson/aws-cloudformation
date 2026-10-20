> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceConfiguration

Represents a specific configuration revision of an Express service, containing all the settings and parameters for that revision.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Cpu" : String,
  "CreatedAt" : String,
  "ExecutionRoleArn" : String,
  "HealthCheckPath" : String,
  "IngressPaths" : [ IngressPathSummary, ... ],
  "Memory" : String,
  "NetworkConfiguration" : ExpressGatewayServiceNetworkConfiguration,
  "PrimaryContainer" : ExpressGatewayContainer,
  "ScalingTarget" : ExpressGatewayScalingTarget,
  "ServiceRevisionArn" : String,
  "TaskDefinitionArn" : String,
  "TaskRoleArn" : String
}

```

### YAML

```
  Cpu: String
  CreatedAt: String
  ExecutionRoleArn: String
  HealthCheckPath: String
  IngressPaths: 
    - IngressPathSummary
  Memory: String
  NetworkConfiguration: 
    ExpressGatewayServiceNetworkConfiguration
  PrimaryContainer: 
    ExpressGatewayContainer
  ScalingTarget: 
    ExpressGatewayScalingTarget
  ServiceRevisionArn: String
  TaskDefinitionArn: String
  TaskRoleArn: String

```

## Properties

**`Cpu`** 

The CPU allocation for tasks in this service revision. 

Required: No

Type: String

Update requires: No interruption

**`CreatedAt`** 

The Unix timestamp for when this service revision was created. 

Required: No

Type: String

Update requires: No interruption

**`ExecutionRoleArn`** 

The ARN of the task execution role for the service revision. 

Required: No

Type: String

Update requires: No interruption

**`HealthCheckPath`** 

The health check path for this service revision. 

Required: No

Type: String

Update requires: No interruption

**`IngressPaths`** 

The entry point into this service revision. 

Required: No

Type: Array of IngressPathSummary

Update requires: No interruption

**`Memory`** 

The memory allocation for tasks in this service revision. 

Required: No

Type: String

Update requires: No interruption

**`NetworkConfiguration`** 

The network configuration for tasks in this service revision. 

Required: No

Type: ExpressGatewayServiceNetworkConfiguration

Update requires: No interruption

**`PrimaryContainer`** 

The primary container configuration for this service revision. 

Required: No

Type: ExpressGatewayContainer

Update requires: No interruption

**`ScalingTarget`** 

The auto-scaling configuration for this service revision. 

Required: No

Type: ExpressGatewayScalingTarget

Update requires: No interruption

**`ServiceRevisionArn`** 

The ARN of the service revision. 

Required: No

Type: String

Update requires: No interruption

**`TaskDefinitionArn`** 

The ARN of the task definition used by this service revision. This is present for all Express services and reflects the task definition in use, whether managed by Amazon ECS or provided by the customer. 

Required: No

Type: String

Update requires: No interruption

**`TaskRoleArn`** 

The ARN of the task role for the service revision. 

Required: No

Type: String

Update requires: No interruption
