> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-networkinterfacecountrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider NetworkInterfaceCountRequest

The minimum and maximum number of network interfaces for instance type selection. This is useful for workloads that require multiple network interfaces.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Max" : Integer,
  "Min" : Integer
}

```

### YAML

```
  Max: Integer
  Min: Integer

```

## Properties

**`Max`** 

The maximum number of network interfaces. Instance types that support more network interfaces are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption

**`Min`** 

The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection. 

Required: No

Type: Integer

Update requires: No interruption
