> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayrepositorycredentials.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService ExpressGatewayRepositoryCredentials

The repository credentials for private registry authentication to pass to the container.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CredentialsParameter" : String
}

```

### YAML

```
  CredentialsParameter: String

```

## Properties

**`CredentialsParameter`** 

The Amazon Resource Name (ARN) of the secret containing the private repository credentials. 

Required: Yes

Type: String

Update requires: No interruption
