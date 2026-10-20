> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-placementconstraint.html
> Downloaded: 2026-10-20

# AWS::ECS::Service PlacementConstraint

An object representing a constraint on task placement. For more information, see Task placement constraints in the Amazon Elastic Container Service Developer Guide.Note

If you're using the Fargate launch type, task placement constraints aren't supported.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Expression" : String,
  "Type" : String
}

```

### YAML

```
  Expression: String
  Type: String

```

## Properties

**`Expression`** 

A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You can't specify an expression if the constraint type is `distinctInstance`. For more information, see Cluster query language in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Update requires: No interruption

**`Type`** 

The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates. 

Required: Yes

Type: String

Allowed values: `distinctInstance | memberOf`

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
