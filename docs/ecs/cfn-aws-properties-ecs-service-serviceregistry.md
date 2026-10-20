> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceregistry.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceRegistry

The details for the service registry.

Each service may be associated with one service registry. Multiple service registries for each service are not supported.

When you add, update, or remove the service registries configuration, Amazon ECS starts a new deployment. New tasks are registered and deregistered to the updated service registry configuration.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContainerName" : String,
  "ContainerPort" : Integer,
  "Port" : Integer,
  "RegistryArn" : String
}

```

### YAML

```
  ContainerName: String
  ContainerPort: Integer
  Port: Integer
  RegistryArn: String

```

## Properties

**`ContainerName`** 

The container name value to be used for your service discovery service. It's already specified in the task definition. If the task definition that your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition that your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you can't specify both. 

Required: No

Type: String

Update requires: No interruption

**`ContainerPort`** 

The port value to be used for your service discovery service. It's already specified in the task definition. If the task definition your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you can't specify both. 

Required: No

Type: Integer

Update requires: No interruption

**`Port`** 

The port value used if your service discovery service specified an SRV record. This field might be used if both the `awsvpc` network mode and SRV records are used. 

Required: No

Type: Integer

Update requires: No interruption

**`RegistryArn`** 

The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see CreateService. 

Required: No

Type: String

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
