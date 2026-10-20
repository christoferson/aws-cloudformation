> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-expressgatewayservice.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService

Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed AWS infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.

Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary AWS resources for traffic distribution, health monitoring, network access control, and capacity management.

Provide an execution role for task operations and an infrastructure role for managing AWS resources on your behalf.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::ExpressGatewayService",
  "Properties" : {
      "Cluster" : String,
      "Cpu" : String,
      "ExecutionRoleArn" : String,
      "HealthCheckPath" : String,
      "InfrastructureRoleArn" : String,
      "Memory" : String,
      "NetworkConfiguration" : ExpressGatewayServiceNetworkConfiguration,
      "PrimaryContainer" : ExpressGatewayContainer,
      "ScalingTarget" : ExpressGatewayScalingTarget,
      "ServiceName" : String,
      "Tags" : [ Tag, ... ],
      "TaskDefinitionArn" : String,
      "TaskRoleArn" : String
    }
}

```

### YAML

```
Type: AWS::ECS::ExpressGatewayService
Properties:
  Cluster: String
  Cpu: String
  ExecutionRoleArn: String
  HealthCheckPath: String
  InfrastructureRoleArn: String
  Memory: String
  NetworkConfiguration: 
    ExpressGatewayServiceNetworkConfiguration
  PrimaryContainer: 
    ExpressGatewayContainer
  ScalingTarget: 
    ExpressGatewayScalingTarget
  ServiceName: String
  Tags: 
    - Tag
  TaskDefinitionArn: String
  TaskRoleArn: String

```

## Properties

**`Cluster`** 

The short name or full ARN of the cluster that hosts the Express service. 

Required: No

Type: String

Update requires: Replacement

**`Cpu`** 

The CPU allocation for tasks in this service revision. 

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

**`InfrastructureRoleArn`** 

The ARN of the infrastructure role that manages AWS resources for the Express service. 

Required: Yes

Type: String

Update requires: Replacement

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

**`ServiceName`** 

The name of the Express service. 

Required: No

Type: String

Update requires: Replacement

**`Tags`** 

The metadata applied to the Express service. 

Required: No

Type: Array of Tag

Minimum: `0`

Maximum: `50`

Update requires: Replacement

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

## Return values

### Ref

### Fn::GetAtt

#### 

**`ActiveConfigurations`** 

The list of active service configurations for the Express service. 

**`CreatedAt`** 

The Unix timestamp for when the Express service was created. 

**`ECSManagedResourceArns.AutoScaling.ApplicationAutoScalingPolicies`** 

The list of Auto Scaling policy ARNs associated with the express service. 

**`ECSManagedResourceArns.AutoScaling.ScalableTarget`** 

The Auto Scaling Scalable Target ARN associated with the express service. 

**`ECSManagedResourceArns.IngressPath.CertificateArn`** 

The Certificate ARN associated with the express service. 

**`ECSManagedResourceArns.IngressPath.ListenerArn`** 

The ARN of the Load Balancer listener associated with the express service. 

**`ECSManagedResourceArns.IngressPath.ListenerRuleArn`** 

The ARN of the Load Balancer listener rule associated with the express service. 

**`ECSManagedResourceArns.IngressPath.LoadBalancerArn`** 

The ARN of the Load Balancer associated with the express service. 

**`ECSManagedResourceArns.IngressPath.LoadBalancerSecurityGroups`** 

The list of Load Balancer Security Group ARNs associated with the express service. 

**`ECSManagedResourceArns.IngressPath.TargetGroupArns`** 

The list of Target Group ARNs associated with the express service. 

**`ECSManagedResourceArns.LogGroups`** 

The list of Log Group ARNs associated with the express service. 

**`ECSManagedResourceArns.MetricAlarms`** 

The list of Metric Alarm ARNs associated with the express service. 

**`ECSManagedResourceArns.ServiceSecurityGroups`** 

The list of Security Group ARNs associated with the express service. 

**`Endpoint`** 

The Endpoint of the express service. 

**`ServiceArn`** 

The ARN that identifies the Express service. 

**`UpdatedAt`** 

The Unix timestamp for when the Express service was last updated.
