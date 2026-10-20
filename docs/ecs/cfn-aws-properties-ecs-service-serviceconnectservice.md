> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectservice.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceConnectService

The Service Connect service object configuration. For more information, see Service Connect in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ClientAliases" : [ ServiceConnectClientAlias, ... ],
  "DiscoveryName" : String,
  "IngressPortOverride" : Integer,
  "PortName" : String,
  "Timeout" : TimeoutConfiguration,
  "Tls" : ServiceConnectTlsConfiguration
}

```

### YAML

```
  ClientAliases: 
    - ServiceConnectClientAlias
  DiscoveryName: String
  IngressPortOverride: Integer
  PortName: String
  Timeout: 
    TimeoutConfiguration
  Tls: 
    ServiceConnectTlsConfiguration

```

## Properties

**`ClientAliases`** 

The list of client aliases for this Service Connect service. You use these to assign names that can be used by client applications. The maximum number of client aliases that you can have in this list is 1. 

Each alias ("endpoint") is a fully-qualified name and port number that other Amazon ECS tasks ("clients") can use to connect to this service. 

Each name and port mapping must be unique within the namespace. 

For each `ServiceConnectService`, you must provide at least one `clientAlias` with one `port`. 

Required: No

Type: Array of ServiceConnectClientAlias

Update requires: No interruption

**`DiscoveryName`** 

The `discoveryName` is the name of the new AWS Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the AWS Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name can't start with a hyphen. 

If the `discoveryName` isn't specified, the port mapping name from the task definition is used in `portName.namespace`. 

Required: No

Type: String

Update requires: No interruption

**`IngressPortOverride`** 

The port number for the Service Connect proxy to listen on. 

Use the value of this field to bypass the proxy for traffic on the port number specified in the named `portMapping` in the task definition of this application, and then use it in your VPC security groups to allow traffic into the proxy for this Amazon ECS service. 

In `awsvpc` mode and Fargate, the default value is the container port number. The container port number is in the `portMapping` in the task definition. In bridge mode, the default value is the ephemeral port of the Service Connect proxy. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `65535`

Update requires: No interruption

**`PortName`** 

The `portName` must match the name of one of the `portMappings` from all the containers in the task definition of this Amazon ECS service. 

Required: Yes

Type: String

Update requires: No interruption

**`Timeout`** 

A reference to an object that represents the configured timeouts for Service Connect. 

Required: No

Type: TimeoutConfiguration

Update requires: No interruption

**`Tls`** 

A reference to an object that represents a Transport Layer Security (TLS) configuration. 

Required: No

Type: ServiceConnectTlsConfiguration

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
