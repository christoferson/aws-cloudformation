> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-clusterconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Cluster ClusterConfiguration

The execute command and managed storage configuration for the cluster.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ExecuteCommandConfiguration" : ExecuteCommandConfiguration,
  "ManagedStorageConfiguration" : ManagedStorageConfiguration
}

```

### YAML

```
  ExecuteCommandConfiguration: 
    ExecuteCommandConfiguration
  ManagedStorageConfiguration: 
    ManagedStorageConfiguration

```

## Properties

**`ExecuteCommandConfiguration`** 

The details of the execute command configuration. 

Required: No

Type: ExecuteCommandConfiguration

Update requires: No interruption

**`ManagedStorageConfiguration`** 

The details of the managed storage configuration. 

Required: No

Type: ManagedStorageConfiguration

Update requires: No interruption

## See also 
  Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined
