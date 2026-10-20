> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition DaemonContainerDefinition

A container definition for a daemon task. Daemon container definitions describe the containers that run as part of a daemon task on container instances managed by capacity providers.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Command" : [ String, ... ],
  "Cpu" : Integer,
  "DependsOn" : [ ContainerDependency, ... ],
  "EntryPoint" : [ String, ... ],
  "Environment" : [ KeyValuePair, ... ],
  "EnvironmentFiles" : [ EnvironmentFile, ... ],
  "Essential" : Boolean,
  "FirelensConfiguration" : FirelensConfiguration,
  "HealthCheck" : HealthCheck,
  "Image" : String,
  "Interactive" : Boolean,
  "LinuxParameters" : LinuxParameters,
  "LogConfiguration" : LogConfiguration,
  "Memory" : Integer,
  "MemoryReservation" : Integer,
  "MountPoints" : [ MountPoint, ... ],
  "Name" : String,
  "Privileged" : Boolean,
  "PseudoTerminal" : Boolean,
  "ReadonlyRootFilesystem" : Boolean,
  "RepositoryCredentials" : RepositoryCredentials,
  "RestartPolicy" : RestartPolicy,
  "Secrets" : [ Secret, ... ],
  "StartTimeout" : Integer,
  "StopTimeout" : Integer,
  "SystemControls" : [ SystemControl, ... ],
  "Ulimits" : [ Ulimit, ... ],
  "User" : String,
  "WorkingDirectory" : String
}

```

### YAML

```
  Command: 
    - String
  Cpu: Integer
  DependsOn: 
    - ContainerDependency
  EntryPoint: 
    - String
  Environment: 
    - KeyValuePair
  EnvironmentFiles: 
    - EnvironmentFile
  Essential: Boolean
  FirelensConfiguration: 
    FirelensConfiguration
  HealthCheck: 
    HealthCheck
  Image: String
  Interactive: Boolean
  LinuxParameters: 
    LinuxParameters
  LogConfiguration: 
    LogConfiguration
  Memory: Integer
  MemoryReservation: Integer
  MountPoints: 
    - MountPoint
  Name: String
  Privileged: Boolean
  PseudoTerminal: Boolean
  ReadonlyRootFilesystem: Boolean
  RepositoryCredentials: 
    RepositoryCredentials
  RestartPolicy: 
    RestartPolicy
  Secrets: 
    - Secret
  StartTimeout: Integer
  StopTimeout: Integer
  SystemControls: 
    - SystemControl
  Ulimits: 
    - Ulimit
  User: String
  WorkingDirectory: String

```

## Properties

**`Command`** 

The command that's passed to the container. 

Required: No

Type: Array of String

Update requires: Replacement

**`Cpu`** 

The number of `cpu` units reserved for the container. 

Required: No

Type: Integer

Update requires: Replacement

**`DependsOn`** 

The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition. 

Required: No

Type: Array of ContainerDependency

Update requires: Replacement

**`EntryPoint`** 

The entry point that's passed to the container. 

Required: No

Type: Array of String

Update requires: Replacement

**`Environment`** 

The environment variables to pass to a container. 

Required: No

Type: Array of KeyValuePair

Update requires: Replacement

**`EnvironmentFiles`** 

A list of files containing the environment variables to pass to a container. 

Required: No

Type: Array of EnvironmentFile

Update requires: Replacement

**`Essential`** 

If the `essential` parameter of a container is marked as `true`, and that container fails or stops for any reason, all other containers that are part of the task are stopped. 

Required: No

Type: Boolean

Update requires: Replacement

**`FirelensConfiguration`** 

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. 

Required: No

Type: FirelensConfiguration

Update requires: Replacement

**`HealthCheck`** 

The container health check command and associated configuration parameters for the container. 

Required: No

Type: HealthCheck

Update requires: Replacement

**`Image`** 

The image used to start the container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`. 

Required: Yes

Type: String

Update requires: Replacement

**`Interactive`** 

When this parameter is `true`, you can deploy containerized applications that require `stdin` or a `tty` to be allocated. 

Required: No

Type: Boolean

Update requires: Replacement

**`LinuxParameters`** 

Linux-specific modifications that are applied to the container configuration, such as Linux kernel capabilities. 

Required: No

Type: LinuxParameters

Update requires: Replacement

**`LogConfiguration`** 

The log configuration specification for the container. 

Required: No

Type: LogConfiguration

Update requires: Replacement

**`Memory`** 

The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is killed. 

Required: No

Type: Integer

Update requires: Replacement

**`MemoryReservation`** 

The soft limit (in MiB) of memory to reserve for the container. 

Required: No

Type: Integer

Update requires: Replacement

**`MountPoints`** 

The mount points for data volumes in your container. 

Required: No

Type: Array of MountPoint

Update requires: Replacement

**`Name`** 

The name of the container. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. 

Required: Yes

Type: String

Update requires: Replacement

**`Privileged`** 

When this parameter is true, the container is given elevated privileges on the host container instance (similar to the `root` user). 

Required: No

Type: Boolean

Update requires: Replacement

**`PseudoTerminal`** 

When this parameter is `true`, a TTY is allocated. 

Required: No

Type: Boolean

Update requires: Replacement

**`ReadonlyRootFilesystem`** 

When this parameter is true, the container is given read-only access to its root file system. 

Required: No

Type: Boolean

Update requires: Replacement

**`RepositoryCredentials`** 

The private repository authentication credentials to use. 

Required: No

Type: RepositoryCredentials

Update requires: Replacement

**`RestartPolicy`** 

The restart policy for the container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task. 

Required: No

Type: RestartPolicy

Update requires: Replacement

**`Secrets`** 

The secrets to pass to the container. 

Required: No

Type: Array of Secret

Update requires: Replacement

**`StartTimeout`** 

Time duration (in seconds) to wait before giving up on resolving dependencies for a container. 

Required: No

Type: Integer

Update requires: Replacement

**`StopTimeout`** 

Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own. 

Required: No

Type: Integer

Update requires: Replacement

**`SystemControls`** 

A list of namespaced kernel parameters to set in the container. 

Required: No

Type: Array of SystemControl

Update requires: Replacement

**`Ulimits`** 

A list of `ulimits` to set in the container. 

Required: No

Type: Array of Ulimit

Update requires: Replacement

**`User`** 

The user to use inside the container. 

Required: No

Type: String

Update requires: Replacement

**`WorkingDirectory`** 

The working directory to run commands inside the container in. 

Required: No

Type: String

Update requires: Replacement
