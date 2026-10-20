> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-forcenewdeployment.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ForceNewDeployment

Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "EnableForceNewDeployment" : Boolean,
  "ForceNewDeploymentNonce" : String
}

```

### YAML

```
  EnableForceNewDeployment: Boolean
  ForceNewDeploymentNonce: String

```

## Properties

**`EnableForceNewDeployment`** 

Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version. 

Required: Yes

Type: Boolean

Update requires: No interruption

**`ForceNewDeploymentNonce`** 

When you change the` ForceNewDeploymentNonce` value in your template, it signals Amazon ECS to start a new deployment even though no other service parameters have changed. The value must be a unique, time- varying value like a timestamp, random string, or sequence number. Use this property when you want to ensure your tasks pick up the latest version of a Docker image that uses the same tag but has been updated in the registry.  

Required: No

Type: String

Minimum: `1`

Maximum: `255`

Update requires: No interruption
