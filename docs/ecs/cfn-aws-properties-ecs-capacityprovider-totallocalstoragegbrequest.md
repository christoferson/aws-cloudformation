> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-totallocalstoragegbrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider TotalLocalStorageGBRequest

The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage. This is useful for workloads that require local storage for temporary data or caching.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Max" : Number,
  "Min" : Number
}

```

### YAML

```
  Max: Number
  Min: Number

```

## Properties

**`Max`** 

The maximum total local storage in GB. Instance types with more local storage are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption

**`Min`** 

The minimum total local storage in GB. Instance types with less local storage are excluded from selection. 

Required: No

Type: Number

Update requires: No interruption
