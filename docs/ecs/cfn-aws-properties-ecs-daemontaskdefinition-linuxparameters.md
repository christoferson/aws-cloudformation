> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-linuxparameters.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition LinuxParameters

The Linux-specific options that are applied to the container, such as Linux KernelCapabilities.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Capabilities" : KernelCapabilities,
  "Devices" : [ Device, ... ],
  "InitProcessEnabled" : Boolean,
  "Tmpfs" : [ Tmpfs, ... ]
}

```

### YAML

```
  Capabilities: 
    KernelCapabilities
  Devices: 
    - Device
  InitProcessEnabled: Boolean
  Tmpfs: 
    - Tmpfs

```

## Properties

**`Capabilities`** 

The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker. Note

For tasks that use the Fargate launch type, `capabilities` is supported for all platform versions but the `add` parameter is only supported if using platform version 1.4.0 or later. 

Required: No

Type: KernelCapabilities

Update requires: Replacement

**`Devices`** 

Any host devices to expose to the container. This parameter maps to `Devices` in the docker container create command and the `--device` option to docker run. Note

If you're using tasks that use the Fargate launch type, the `devices` parameter isn't supported. 

Required: No

Type: Array of Device

Update requires: Replacement

**`InitProcessEnabled`** 

Run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to docker run. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version --format '{{.Server.APIVersion}}'` 

Required: No

Type: Boolean

Update requires: Replacement

**`Tmpfs`** 

The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the `--tmpfs` option to docker run. 

Required: No

Type: Array of Tmpfs

Update requires: Replacement
