> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-placementstrategy.html
> Downloaded: 2026-10-20

# AWS::ECS::Service PlacementStrategy

The task placement strategy for a task or service. For more information, see Task placement strategies in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Field" : String,
  "Type" : String
}

```

### YAML

```
  Field: String
  Type: String

```

## Properties

**`Field`** 

The field to apply the placement strategy against. For the `spread` placement strategy, valid values are `instanceId` (or `host`, which has the same effect), or any platform or custom attribute that's applied to a container instance, such as `attribute:ecs.availability-zone`. For the `binpack` placement strategy, valid values are `cpu` and `memory`. For the `random` placement strategy, this field is not used. 

Required: No

Type: String

Update requires: No interruption

**`Type`** 

The type of placement strategy. The `random` placement strategy randomly places tasks on available candidates. The `spread` placement strategy spreads placement across available candidates evenly based on the `field` parameter. The `binpack` strategy places tasks on available candidates that have the least available amount of the resource that's specified with the `field` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory but still enough to run the task. 

Required: Yes

Type: String

Allowed values: `binpack | random | spread`

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
