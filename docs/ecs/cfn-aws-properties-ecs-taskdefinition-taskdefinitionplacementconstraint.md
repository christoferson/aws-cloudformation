> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition TaskDefinitionPlacementConstraint

The constraint on task placement in the task definition. For more information, see Task placement constraints in the Amazon Elastic Container Service Developer Guide.Note

Task placement constraints aren't supported for tasks run on AWS Fargate.

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

A cluster query language expression to apply to the constraint. For more information, see Cluster query language in the Amazon Elastic Container Service Developer Guide. 

Required: No

Type: String

Update requires: Replacement

**`Type`** 

The type of constraint. The `MemberOf` constraint restricts selection to be from a group of valid candidates. 

Required: Yes

Type: String

Allowed values: `memberOf`

Update requires: Replacement
