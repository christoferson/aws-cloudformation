> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-ephemeralstorage.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition EphemeralStorage

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate. For more information, see Using data volumes in tasks in the Amazon ECS Developer Guide;.Note

For tasks using the Fargate launch type, the task requires the following platforms: 
Linux platform version `1.4.0` or later. 
Windows platform version `1.0.0` or later. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "SizeInGiB" : Integer
}

```

### YAML

```
  SizeInGiB: Integer

```

## Properties

**`SizeInGiB`** 

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB. 

Required: No

Type: Integer

Update requires: Replacement
