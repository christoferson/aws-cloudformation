> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewaycontainer.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayContainer

Defines the configuration for the primary container in an Express service. This container receives traffic from the Application Load Balancer and runs your application code.

The container configuration includes the container image, port mapping, logging settings, environment variables, and secrets. The container image is the only required parameter, with sensible defaults provided for other settings.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AwsLogsConfiguration" : ExpressGatewayServiceAwsLogsConfiguration,
  "Command" : [ String, ... ],
  "ContainerPort" : Integer,
  "Environment" : [ KeyValuePair, ... ],
  "Image" : String,
  "RepositoryCredentials" : ExpressGatewayRepositoryCredentials,
  "Secrets" : [ Secret, ... ]
}

```

### YAML

```
  AwsLogsConfiguration: 
    ExpressGatewayServiceAwsLogsConfiguration
  Command: 
    - String
  ContainerPort: Integer
  Environment: 
    - KeyValuePair
  Image: String
  RepositoryCredentials: 
    ExpressGatewayRepositoryCredentials
  Secrets: 
    - Secret

```

## Properties

**`AwsLogsConfiguration`** 

The log configuration for the container. 

Required: No

Type: ExpressGatewayServiceAwsLogsConfiguration

Update requires: No interruption

**`Command`** 

The command that is passed to the container. 

Required: No

Type: Array of String

Update requires: No interruption

**`ContainerPort`** 

The port number on the container that receives traffic from the load balancer. Default is 80. 

Required: No

Type: Integer

Update requires: No interruption

**`Environment`** 

The environment variables to pass to the container. 

Required: No

Type: Array of KeyValuePair

Update requires: No interruption

**`Image`** 

The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`. 

For Express services, the image typically contains a web application that listens on the specified container port. The image can be stored in Amazon ECR, Docker Hub, or any other container registry accessible to your execution role. 

Required: Yes

Type: String

Update requires: No interruption

**`RepositoryCredentials`** 

The configuration for repository credentials for private registry authentication. 

Required: No

Type: ExpressGatewayRepositoryCredentials

Update requires: No interruption

**`Secrets`** 

The secrets to pass to the container. 

Required: No

Type: Array of Secret

Update requires: No interruption
