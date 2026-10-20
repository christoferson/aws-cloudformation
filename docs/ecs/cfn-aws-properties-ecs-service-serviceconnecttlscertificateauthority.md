> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttlscertificateauthority.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceConnectTlsCertificateAuthority

The certificate root authority that secures your service.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AwsPcaAuthorityArn" : String
}

```

### YAML

```
  AwsPcaAuthorityArn: String

```

## Properties

**`AwsPcaAuthorityArn`** 

The ARN of the AWS Private Certificate Authority certificate. 

Required: No

Type: String

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
