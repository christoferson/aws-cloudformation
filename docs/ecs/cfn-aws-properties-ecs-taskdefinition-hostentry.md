> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-hostentry.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition HostEntry

The `HostEntry` property specifies a hostname and an IP address that are added to the `/etc/hosts` file of a container through the `extraHosts` parameter of its `ContainerDefinition` resource.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Hostname" : String,
  "IpAddress" : String
}

```

### YAML

```
  Hostname: String
  IpAddress: String

```

## Properties

**`Hostname`** 

The hostname to use in the `/etc/hosts` entry. 

Required: No

Type: String

Update requires: Replacement

**`IpAddress`** 

The IP address to use in the `/etc/hosts` entry. 

Required: No

Type: String

Update requires: Replacement
