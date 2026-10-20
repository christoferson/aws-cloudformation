> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-resourcerequirement.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition ResourceRequirement

The type and amount of a resource to assign to a container. The supported resource types are GPUs, Neuron devices, and Elastic Inference accelerators. For more information, see Working with GPUs on Amazon ECS or Working with Amazon Elastic Inference on Amazon ECS in the Amazon Elastic Container Service Developer Guide

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "SharingStrategy" : SharingStrategy,
  "Type" : String,
  "Value" : String
}

```

### YAML

```
  SharingStrategy: 
    SharingStrategy
  Type: String
  Value: String

```

## Properties

**`SharingStrategy`**

Property description not available.

Required: No

Type: SharingStrategy

Update requires: Replacement

**`Type`** 

The type of resource to assign to a container.  

Required: Yes

Type: String

Allowed values: `GPU | InferenceAccelerator | NeuronDevice`

Update requires: Replacement

**`Value`** 

The value for the specified resource type. 

When the type is `GPU`, the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. You can also specify `ALL` to allocate all available GPUs on the instance to the container. 

When the type is `NeuronDevice`, the value must be `ALL`. This allocates all available Neuron devices on the instance to the container. Only one container in a task can specify `NeuronDevice` resources. This resource type is only supported on Managed Instances. 

When the type is `InferenceAccelerator`, the `value` matches the `deviceName` for an InferenceAccelerator specified in a task definition. 

Required: No

Type: String

Update requires: Replacement
