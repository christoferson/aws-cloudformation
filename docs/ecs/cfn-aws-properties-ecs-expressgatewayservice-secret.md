> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-secret.html
> Downloaded: 2026-10-20

# AWS::ECS::ExpressGatewayService Secret

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways: 
To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter. 
To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter. 

For more information, see Specifying sensitive data in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "ValueFrom" : String
}

```

### YAML

```
  Name: String
  ValueFrom: String

```

## Properties

**`Name`** 

The name of the secret. 

Required: Yes

Type: String

Update requires: No interruption

**`ValueFrom`** 

The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store. 

For information about the require AWS Identity and Access Management permissions, see Required IAM permissions for Amazon ECS secrets (for Secrets Manager) or Required IAM permissions for Amazon ECS secrets (for Systems Manager Parameter store) in the Amazon Elastic Container Service Developer Guide. Note

If the SSM Parameter Store parameter exists in the same Region as the task you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified. 

Required: Yes

Type: String

Update requires: No interruption
