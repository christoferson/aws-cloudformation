> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-kernelcapabilities.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition KernelCapabilities

The Linux capabilities to add or remove from the default Docker configuration for a container defined in the task definition. For more detailed information about these Linux capabilities, see the capabilities(7) Linux manual page.

The following describes how Docker processes the Linux capabilities specified in the `add` and `drop` request parameters. For information about the latest behavior, see Docker Compose: order of cap_drop and cap_add in the Docker Community Forum. 
When the container is a privleged container, the container capabilities are all of the default Docker capabilities. The capabilities specified in the `add` request parameter, and the `drop` request parameter are ignored. 
When the `add` request parameter is set to ALL, the container capabilities are all of the default Docker capabilities, excluding those specified in the `drop` request parameter. 
When the `drop` request parameter is set to ALL, the container capabilities are the capabilities specified in the `add` request parameter. 
When the `add` request parameter and the `drop` request parameter are both empty, the capabilities the container capabilities are all of the default Docker capabilities. 
The default is to first drop the capabilities specified in the `drop` request parameter, and then add the capabilities specified in the `add` request parameter. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Add" : [ String, ... ],
  "Drop" : [ String, ... ]
}

```

### YAML

```
  Add: 
    - String
  Drop: 
    - String

```

## Properties

**`Add`** 

The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to `CapAdd` in the docker container create command and the `--cap-add` option to docker run. Note

Tasks launched on AWS Fargate only support adding the `SYS_PTRACE` kernel capability. 

Valid values: `"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"` 

Required: No

Type: Array of String

Update requires: Replacement

**`Drop`** 

The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to `CapDrop` in the docker container create command and the `--cap-drop` option to docker run. 

Valid values: `"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"` 

Required: No

Type: Array of String

Update requires: Replacement
