> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogdestination.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway GatewayElbAccessLogDestination

The destination where the access logs for a gateway's load balancers are delivered.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "S3" : GatewayElbAccessLogS3Destination
}

```

### YAML

```
  S3: 
    GatewayElbAccessLogS3Destination

```

## Properties

**`S3`** 

The Amazon S3 destination for access logs. 

Required: No

Type: GatewayElbAccessLogS3Destination

Update requires: No interruption
