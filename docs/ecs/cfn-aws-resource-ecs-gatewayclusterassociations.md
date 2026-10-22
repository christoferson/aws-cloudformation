> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-gatewayclusterassociations.html
> Downloaded: 2026-10-21

# AWS::ECS::GatewayClusterAssociations

The `AWS::ECS::GatewayClusterAssociations` resource Property description not available. for ECS.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::GatewayClusterAssociations",
  "Properties" : {
      "Cluster" : String,
      "Gateway" : String
    }
}

```

### YAML

```
Type: AWS::ECS::GatewayClusterAssociations
Properties:
  Cluster: String
  Gateway: String

```

## Properties

**`Cluster`** 

A regional grouping of one or more container instances where you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously. 

Required: Yes

Type: String

Update requires: Replacement

**`Gateway`** 

The details of a gateway, including its configuration, status, and the infrastructure settings for its type. 

Required: Yes

Type: String

Update requires: Replacement

## Return values

### Ref

### Fn::GetAtt

#### 

**`ClusterArn`**

Property description not available.

**`GatewayArn`**

Property description not available.

**`Status`**

Property description not available.
