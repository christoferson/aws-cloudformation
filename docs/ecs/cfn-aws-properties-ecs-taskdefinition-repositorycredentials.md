> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-repositorycredentials.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition RepositoryCredentials

The repository credentials for private registry authentication.

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

The Amazon Resource Name (ARN) of the secret containing the private repository credentials. Note

When you use the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you're launching then you can use either the full ARN or the name of the secret. When you use the AWS Management Console, you must specify the full ARN of the secret. 

Required: No

Type: String

Update requires: Replacement
