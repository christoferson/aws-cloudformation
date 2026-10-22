> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogs3destination.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayElbAccessLogS3Destination

The Amazon S3 destination for the access logs of a gateway's load balancers.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Bucket" : String,
  "Prefix" : String
}

```

### YAML

```
  Bucket: String
  Prefix: String

```

## Properties

**`Bucket`** 

The name of the Amazon S3 bucket where access logs are delivered. 

Required: Yes

Type: String

Update requires: No interruption

**`Prefix`** 

The object key prefix for the access logs in the Amazon S3 bucket. 

Required: No

Type: String

Update requires: No interruption
