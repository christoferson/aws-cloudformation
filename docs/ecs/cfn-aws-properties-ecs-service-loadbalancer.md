> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-loadbalancer.html
> Downloaded: 2026-10-18

# AWS::ECS::Service LoadBalancer

The `LoadBalancer` property specifies details on a load balancer that is used with a service.

If the service is using the `CODE_DEPLOY` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a `targetGroupPair`). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.

Services with tasks that use the `awsvpc` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose `ip` as the target type, not `instance`. Tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AdvancedConfiguration" : AdvancedConfiguration,
  "ContainerName" : String,
  "ContainerPort" : Integer,
  "LoadBalancerName" : String,
  "TargetGroupArn" : String
}

```

### YAML

```
  AdvancedConfiguration: 
    AdvancedConfiguration
  ContainerName: String
  ContainerPort: Integer
  LoadBalancerName: String
  TargetGroupArn: String

```

## Properties

**`AdvancedConfiguration`** 

The advanced settings for the load balancer used in blue/green deployments. Specify the alternate target group, listener rules, and IAM role required for traffic shifting during blue/green deployments. 

Required: No

Type: AdvancedConfiguration

Update requires: No interruption

**`ContainerName`** 

The name of the container (as it appears in a container definition) to associate with the load balancer. 

You need to specify the container name when configuring the target group for an Amazon ECS load balancer. 

Required: No

Type: String

Update requires: No interruption

**`ContainerPort`** 

The port on the container to associate with the load balancer. This port must correspond to a `containerPort` in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance they're launched on must allow ingress traffic on the `hostPort` of the port mapping. 

Required: No

Type: Integer

Update requires: No interruption

**`LoadBalancerName`** 

The name of the load balancer to associate with the Amazon ECS service or task set. 

If you are using an Application Load Balancer or a Network Load Balancer the load balancer name parameter should be omitted. 

Required: No

Type: String

Update requires: No interruption

**`TargetGroupArn`** 

The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service or task set. 

A target group ARN is only specified when using an Application Load Balancer or Network Load Balancer.  

For services using the `ECS` deployment controller, you can specify one or multiple target groups. For more information, see Registering multiple target groups with a service in the Amazon Elastic Container Service Developer Guide. 

For services using the `CODE_DEPLOY` deployment controller, you're required to define two target groups for the load balancer. For more information, see Blue/green deployment with CodeDeploy in the Amazon Elastic Container Service Developer Guide. Important

If your service's task definition uses the `awsvpc` network mode, you must choose `ip` as the target type, not `instance`. Do this when creating your target groups because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance. This network mode is required for the Fargate launch type. 

Required: No

Type: String

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
