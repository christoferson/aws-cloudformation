> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-servicevolumeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceVolumeConfiguration

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ManagedEBSVolume" : ServiceManagedEBSVolumeConfiguration,
  "Name" : String
}

```

### YAML

```
  ManagedEBSVolume: 
    ServiceManagedEBSVolumeConfiguration
  Name: String

```

## Properties

**`ManagedEBSVolume`** 

The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task in the service. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created. 

Required: No

Type: ServiceManagedEBSVolumeConfiguration

Update requires: No interruption

**`Name`** 

The name of the volume. This value must match the volume name from the `Volume` object in the task definition. 

Required: Yes

Type: String

Update requires: No interruption
