> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskset-scale.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskSet Scale

A floating-point percentage of the desired number of tasks to place and keep running in the task set.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Unit" : String,
  "Value" : Number
}

```

### YAML

```
  Unit: String
  Value: Number

```

## Properties

**`Unit`** 

The unit of measure for the scale value. 

Required: No

Type: String

Allowed values: `PERCENT`

Update requires: No interruption

**`Value`** 

The value, specified as a percent total of a service's `desiredCount`, to scale the task set. Accepted values are numbers between 0 and 100. 

Required: No

Type: Number

Minimum: `0`

Maximum: `100`

Update requires: No interruption
