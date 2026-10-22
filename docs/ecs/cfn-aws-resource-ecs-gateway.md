> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-gateway.html
> Downloaded: 2026-10-21

# AWS::ECS::Gateway

The details of a gateway, including its configuration, status, and the infrastructure settings for its type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::Gateway",
  "Properties" : {
      "Configuration" : GatewayConfiguration,
      "DeletionProtection" : Boolean,
      "GatewayName" : String,
      "InfrastructureRoleArn" : String,
      "PropagateTags" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::Gateway
Properties:
  Configuration: 
    GatewayConfiguration
  DeletionProtection: Boolean
  GatewayName: String
  InfrastructureRoleArn: String
  PropagateTags: String
  Tags: 
    - Tag

```

## Properties

**`Configuration`** 

The type-specific configuration for the gateway. 

Required: Yes

Type: GatewayConfiguration

Update requires: No interruption

**`DeletionProtection`** 

Specifies whether deletion protection is enabled for the gateway. 

Required: No

Type: Boolean

Update requires: No interruption

**`GatewayName`** 

The name of the gateway. 

Required: Yes

Type: String

Pattern: `^[a-zA-Z0-9-]+$`

Minimum: `1`

Maximum: `255`

Update requires: Replacement

**`InfrastructureRoleArn`** 

The Amazon Resource Name (ARN) of the IAM role that the gateway uses to manage infrastructure on your behalf. 

Required: Yes

Type: String

Update requires: No interruption

**`PropagateTags`** 

Specifies whether the gateway propagates its tags to the infrastructure it manages. 

Required: No

Type: String

Allowed values: `NONE | GATEWAY`

Update requires: No interruption

**`Tags`** 

The metadata applied to the gateway. Each tag consists of a key and an optional value. 

Required: No

Type: Array of Tag

Minimum: `0`

Maximum: `50`

Update requires: No interruption

## Return values

### Ref

### Fn::GetAtt

#### 

**`AccessType`** 

Specifies whether the gateway is publicly accessible (`PUBLIC`) or private (`PRIVATE`). The gateway derives this value from its scheme when you create the gateway, and the value is immutable. 

**`Arn`** 

The Amazon Resource Name (ARN) of the security group. 

**`Configuration.HostSharedAlb.CurrentAlbCount`** 

The current number of Application Load Balancers that the gateway has allocated. 

**`CreatedAt`** 

The Unix timestamp for the time when the gateway was created. 

**`Status`** 

The status of the gateway. 

**`UpdatedAt`** 

The Unix timestamp for the time when the gateway was last updated.
