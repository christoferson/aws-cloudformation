> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-ebstagspecification.html
> Downloaded: 2026-10-20

# AWS::ECS::Service EBSTagSpecification

The tag specifications of an Amazon EBS volume.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "PropagateTags" : String,
  "ResourceType" : String,
  "Tags" : [ Tag, ... ]
}

```

### YAML

```
  PropagateTags: String
  ResourceType: String
  Tags: 
    - Tag

```

## Properties

**`PropagateTags`** 

Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a `SERVICE` specified in `ServiceVolumeConfiguration`. If no value is specified, the tags aren't propagated. 

Required: No

Type: String

Allowed values: `SERVICE | TASK_DEFINITION`

Update requires: No interruption

**`ResourceType`** 

The type of volume resource. 

Required: Yes

Type: String

Allowed values: `volume`

Update requires: No interruption

**`Tags`** 

The tags applied to this Amazon EBS volume. `AmazonECSCreated` and `AmazonECSManaged` are reserved tags that can't be used. 

Required: No

Type: Array of Tag

Minimum: `0`

Maximum: `50`

Update requires: No interruption
