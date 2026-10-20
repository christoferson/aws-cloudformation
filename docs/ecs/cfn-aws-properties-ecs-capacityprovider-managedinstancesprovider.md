> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesprovider.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider ManagedInstancesProvider

The configuration for a Amazon ECS Managed Instances provider. Amazon ECS uses this configuration to automatically launch, manage, and terminate Amazon EC2 instances on your behalf. Managed instances provide access to the full range of Amazon EC2 instance types and features while offloading infrastructure management to AWS.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AutoRepairConfiguration" : AutoRepairConfiguration,
  "InfrastructureOptimization" : InfrastructureOptimization,
  "InfrastructureRoleArn" : String,
  "InstanceLaunchTemplate" : InstanceLaunchTemplate,
  "PropagateTags" : String
}

```

### YAML

```
  AutoRepairConfiguration: 
    AutoRepairConfiguration
  InfrastructureOptimization: 
    InfrastructureOptimization
  InfrastructureRoleArn: String
  InstanceLaunchTemplate: 
    InstanceLaunchTemplate
  PropagateTags: String

```

## Properties

**`AutoRepairConfiguration`** 

The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Indicates whether Amazon ECS automatically replaces container instances that are detected as unhealthy. 

Required: No

Type: AutoRepairConfiguration

Update requires: No interruption

**`InfrastructureOptimization`** 

Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Configure it to turn on or off the infrastructure optimization in your capacity provider, and to control the idle or underutilized EC2 instances optimization delay. 

Required: No

Type: InfrastructureOptimization

Update requires: No interruption

**`InfrastructureRoleArn`** 

The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS assumes to manage instances. This role must include permissions for Amazon EC2 instance lifecycle management, networking, and any additional AWS services required for your workloads. 

For more information, see Amazon ECS infrastructure IAM role in the Amazon ECS Developer Guide. 

Required: Yes

Type: String

Update requires: No interruption

**`InstanceLaunchTemplate`** 

The launch template that defines how Amazon ECS launches Amazon ECS Managed Instances. This includes the instance profile for your tasks, network and storage configuration, and instance requirements that determine which Amazon EC2 instance types can be used. 

For more information, see Store instance launch parameters in Amazon EC2 launch templates in the Amazon EC2 User Guide. 

Required: Yes

Type: InstanceLaunchTemplate

Update requires: No interruption

**`PropagateTags`** 

Determines whether tags from the capacity provider are automatically applied to Amazon ECS Managed Instances. This helps with cost allocation and resource management by ensuring consistent tagging across your infrastructure. 

Required: No

Type: String

Allowed values: `CAPACITY_PROVIDER | NONE`

Update requires: No interruption
