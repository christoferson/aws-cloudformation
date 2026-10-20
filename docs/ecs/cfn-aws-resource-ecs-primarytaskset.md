> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-primarytaskset.html
> Downloaded: 2026-10-20

# AWS::ECS::PrimaryTaskSet

Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the `EXTERNAL` deployment controller type. For more information, see Amazon ECS Deployment Types in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::PrimaryTaskSet",
  "Properties" : {
      "Cluster" : String,
      "Service" : String,
      "TaskSetId" : String
    }
}

```

### YAML

```
Type: AWS::ECS::PrimaryTaskSet
Properties:
  Cluster: String
  Service: String
  TaskSetId: String

```

## Properties

**`Cluster`** 

The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in. 

Required: Yes

Type: String

Update requires: Replacement

**`Service`** 

The short name or full Amazon Resource Name (ARN) of the service that the task set exists in. 

Required: Yes

Type: String

Update requires: Replacement

**`TaskSetId`** 

The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment. 

Required: Yes

Type: String

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see `Ref`.
