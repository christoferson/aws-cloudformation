> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-clustercapacityproviderassociations.html
> Downloaded: 2026-10-20

# AWS::ECS::ClusterCapacityProviderAssociations

The `AWS::ECS::ClusterCapacityProviderAssociations` resource associates one or more capacity providers and a default capacity provider strategy with a cluster.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::ClusterCapacityProviderAssociations",
  "Properties" : {
      "CapacityProviders" : [ String, ... ],
      "Cluster" : String,
      "DefaultCapacityProviderStrategy" : [ CapacityProviderStrategy, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::ClusterCapacityProviderAssociations
Properties:
  CapacityProviders: 
    - String
  Cluster: String
  DefaultCapacityProviderStrategy: 
    - CapacityProviderStrategy

```

## Properties

**`CapacityProviders`** 

The capacity providers to associate with the cluster. 

Required: No

Type: Array of String

Update requires: No interruption

**`Cluster`** 

The cluster the capacity provider association is the target of. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`DefaultCapacityProviderStrategy`** 

The default capacity provider strategy to associate with the cluster. 

Required: Yes

Type: Array of CapacityProviderStrategy

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the cluster name.
