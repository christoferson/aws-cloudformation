> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-tmpfs.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition Tmpfs

The container path, mount options, and size of the tmpfs mount.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ContainerPath" : String,
  "MountOptions" : [ String, ... ],
  "Size" : Integer
}

```

### YAML

```
  ContainerPath: String
  MountOptions: 
    - String
  Size: Integer

```

## Properties

**`ContainerPath`** 

The absolute file path where the tmpfs volume is to be mounted. 

Required: No

Type: String

Update requires: Replacement

**`MountOptions`** 

The list of tmpfs volume mount options. 

Valid values: `"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"` 

Required: No

Type: Array of String

Update requires: Replacement

**`Size`** 

The maximum size (in MiB) of the tmpfs volume. 

Required: Yes

Type: Integer

Update requires: Replacement
