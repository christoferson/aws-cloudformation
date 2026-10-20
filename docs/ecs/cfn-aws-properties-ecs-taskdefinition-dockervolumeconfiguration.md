> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition DockerVolumeConfiguration

The `DockerVolumeConfiguration` property specifies a Docker volume configuration and is used when you use Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the `local` driver. To use bind mounts, specify a `host` instead.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Autoprovision" : Boolean,
  "Driver" : String,
  "DriverOpts" : {Key: Value, ...},
  "Labels" : {Key: Value, ...},
  "Scope" : String
}

```

### YAML

```
  Autoprovision: Boolean
  Driver: String
  DriverOpts: 
    Key: Value
  Labels: 
    Key: Value
  Scope: String

```

## Properties

**`Autoprovision`** 

If this value is `true`, the Docker volume is created if it doesn't already exist. Note

This field is only used if the `scope` is `shared`. 

Required: No

Type: Boolean

Update requires: Replacement

**`Driver`** 

The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use `docker plugin ls` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. This parameter maps to `Driver` in the docker container create command and the `xxdriver` option to docker volume create. 

Required: No

Type: String

Update requires: Replacement

**`DriverOpts`** 

A map of Docker driver-specific options passed through. This parameter maps to `DriverOpts` in the docker create-volume command and the `xxopt` option to docker volume create. 

Required: No

Type: Object of String

Pattern: `.{1,}`

Update requires: Replacement

**`Labels`** 

Custom metadata to add to your Docker volume. This parameter maps to `Labels` in the docker container create command and the `xxlabel` option to docker volume create. 

Required: No

Type: Object of String

Pattern: `.{1,}`

Update requires: Replacement

**`Scope`** 

The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as `shared` persist after the task stops. 

Required: No

Type: String

Allowed values: `task | shared`

Update requires: Replacement
