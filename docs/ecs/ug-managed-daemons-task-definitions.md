> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-daemons-task-definitions.html
> Downloaded: 2026-10-20

# Daemon task definitions

A daemon task definition is the blueprint for your daemon. Amazon ECS Managed Daemons use a dedicated daemon task definition resource, distinct from standard Amazon ECS task definitions. You register a daemon task definition to specify the container image, resource requirements, and configuration for your daemon. 

## Creating a daemon task definition 

You can create a daemon task definition by using the AWS Management Console or the AWS CLI. 

### Using the AWS Management Console  
Open the Amazon ECS console. In the navigation pane, choose Daemon task definitions. 
Choose Create new daemon task definition. 
For Daemon task definition family, enter a unique name. The name can contain up to 255 alphanumeric characters, hyphens, and underscores. 
(Optional) For Task role, choose an IAM role that grants permissions to the applications running in your containers. Leave this blank if your containers do not call AWS APIs. 
(Optional) For Task execution role, select `ecsTaskExecutionRole`. Amazon ECS requires this role to pull container images and publish logs. 
(Optional) For Task size, specify the CPU and memory to reserve for your daemon. For example, `0.25 vCPU` and `512 MB` memory. 
Configure your container details:  
Container name - Enter a name for your container. The name can contain up to 255 alphanumeric characters, hyphens, and underscores. 
Essential container - Select Yes. Each daemon task definition requires at least one essential container. If an essential container fails, Amazon ECS stops the entire task. 
Image URI - Enter the Docker image URI. You can browse Amazon ECR images or use public images from Docker Hub or other registries. 
(Optional) Configure resource allocation, health check, environment variables, log collection, and tags as needed. 
Review your configuration and choose Create. 
 

### Using the AWS CLI 

Register a daemon task definition by creating a JSON file and using the `register-daemon-task-definition` command. 

The following is an example JSON file: 

```
{
    "family": "my-daemon-task",
    "containerDefinitions": [
        {
            "name": "daemon-container",
            "image": "public.ecr.aws/docker/library/busybox:latest",
            "essential": true,
            "command": ["sh", "-c", "while true; do echo 'Daemon running'; sleep 30; done"],
            "memoryReservation": 512
        }
    ]
}
```
 

Run the following command to register the daemon task definition: 

```
aws ecs register-daemon-task-definition --cli-input-json file://daemon-taskdef.json
```
 

## Daemon task definition parameters 

You can use the following parameters when you register a daemon task definition. 

Required parameters  
`family` - The task definition family name. This groups multiple revisions of the same daemon task definition. 
`containerDefinitions` - An array of `DaemonContainerDefinition` objects that describe the containers in your daemon task. 
 

Optional parameters  
`cpu` - Task-level CPU units as a string (for example, `"256"`). 
`memory` - Task-level memory in MiB as a string (for example, `"512"`). 
`taskRoleArn` - The ARN of the IAM role that grants permissions to the containers in your daemon task. 
`executionRoleArn` - The ARN of the IAM role that the Amazon ECS container agent uses to make AWS API calls on your behalf (for example, pulling images from Amazon ECR). 
`volumes` - An array of `DaemonVolume` objects. Daemon volumes support only bind mounts with `host` and `sourcePath`. Daemon task definitions do not support Amazon EBS, Amazon EFS, FSx for Windows File Server, Docker volumes, or ephemeral storage. 
`tags` - An array of key-value pairs to tag your daemon task definition. 
`pidMode` - Controls the PID namespace mode for the daemon. 
`ipcMode` - Controls the IPC namespace mode for the daemon. 
 

## Network mode 

Daemons use a special `daemon_bridge` network mode that Amazon ECS sets automatically. You cannot specify a network mode in your daemon task definition. All daemons on an instance share a single network namespace and are accessible locally via a static daemon bridge IP address (`169.254.172.2` for IPv4, or `fd00:ec2::172:2` for IPv6). Application tasks (non-daemons) can communicate with daemons at this address without additional network configuration. 

Because daemons run in a separate network namespace from application tasks, non-daemon tasks don't need to worry about port conflicts with daemons. However, since all daemon tasks share the same namespace, daemons on the same instance cannot bind to the same port. When deploying multiple daemons, ensure each daemon uses a unique port. 

## Privileged capabilities 

On Amazon ECS Managed Instances, daemons support privileged Linux capabilities for system-level operations. Security agents, network monitoring tools, and observability agents often require kernel-level access to function correctly. 

You can grant capabilities in two ways: 

Full privileged mode grants all Linux capabilities to the container. Use this when your agent requires broad system access: 

```
{
    "containerDefinitions": [{
        "name": "security-daemon",
        "image": "my-security-agent:latest",
        "privileged": true
    }]
}
```
 

Individual capabilities grant only the permissions your daemon needs, following the principle of least privilege. Use the `linuxParameters.capabilities` field to add individual capabilities such as `SYS_ADMIN`, `NET_ADMIN`, `SYS_PTRACE`, `BPF`, and `PERFMON`: 

```
{
    "containerDefinitions": [{
        "name": "monitoring-daemon",
        "image": "my-monitoring-agent:latest",
        "linuxParameters": {
            "capabilities": {
                "add": ["NET_ADMIN", "SYS_PTRACE"]
            }
        }
    }]
}
```
 

## PID and IPC namespace sharing 

On Amazon ECS Managed Instances, daemons support PID and IPC namespace sharing to enable use cases such as security agents, monitoring tools, and observability daemons that need visibility into application task processes or IPC resources.   

**`pidMode`**  

Type: String 

Required: No 

Valid values: `none` | `shared` 

Default: `none` 

The PID namespace mode for the daemon. If `none` is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use `pidMode: "host"` or other daemons that use `pidMode: "shared"`.  

**`ipcMode`**  

Type: String 

Required: No 

Valid values: `none` | `shared` 

Default: `none` 

The IPC namespace mode for the daemon. If `none` is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use `ipcMode: "host"` or other daemons that use `ipcMode: "shared"`.   

The following example shows a daemon task definition with both PID and IPC namespace sharing enabled: 

```
{
    "family": "my-monitoring-daemon",
    "pidMode": "shared",
    "ipcMode": "shared",
    "containerDefinitions": [
        {
            "name": "monitoring-agent",
            "image": "public.ecr.aws/my-company/monitoring-agent:latest",
            "essential": true
        }
    ]
}
```
 

To share the PID namespace with a daemon that has `pidMode` set to `shared`, a non-daemon task must specify `pidMode: "host"` in its task definition. This allows the task's containers to see the daemon's processes and enables use cases such as process monitoring and signal delivery. 

To share the IPC namespace with a daemon that has `ipcMode` set to `shared`, a non-daemon task must specify `ipcMode: "host"` in its task definition. This allows the task's containers to access the daemon's IPC resources such as shared memory segments and message queues. 

## Volumes 

Managed Daemons support bind mounts using host volumes with a `sourcePath` specification. This allows daemon containers to mount host directories to access logs, metrics, and system information on the underlying Amazon EC2 instance. Log collection agents, metrics exporters, and security scanners commonly use this to gain visibility into host-level data. 

The daemon task definition supports host volume specifications with `sourcePath`. Daemon volumes persist for the lifecycle of the underlying container instance. Note

Amazon EBS volumes, Amazon EFS volumes, FSx for Windows File Server volumes, Docker volumes, and ephemeral storage are not supported in daemon task definitions. Note

Daemons do not support volume sharing between each other. Each daemon operates with its own independent volume configuration. 

The following example shows a log collector daemon with a bind mount: 

```
{
    "containerDefinitions": [{
        "name": "log-collector",
        "image": "fluent/fluentd:latest",
        "mountPoints": [{
            "sourceVolume": "var-log",
            "containerPath": "/var/log"
        }]
    }],
    "volumes": [{
        "name": "var-log",
        "host": {
            "sourcePath": "/var/log"
        }
    }]
}
```
 

## Supported container parameters 

Daemon container definitions support the following parameters:  
`image` (required) - Container image URI 
`name` (required) - Container name 
`cpu` - CPU units reserved for the container 
`memory` / `memoryReservation` - Hard and soft memory limits 
`essential` - Whether the container is essential (default: true) 
`command` / `entryPoint` - Override the container command or entry point 
`environment` / `environmentFiles` / `secrets` - Environment configuration 
`privileged` - Run the container in privileged mode 
`user` - User to run the container as 
`workingDirectory` - Working directory inside the container 
`readonlyRootFilesystem` - Mount the root filesystem as read-only 
`mountPoints` - Volume mount points (bind mounts with host and sourcePath only) 
`logConfiguration` - Logging configuration (supports awslogs, splunk, awsfirelens) 
`healthCheck` - Container health check configuration 
`dependsOn` - Container startup dependencies 
`ulimits` - Resource limits 
`systemControls` - Kernel parameters 
`linuxParameters.capabilities` - Linux capabilities to add or drop 
`linuxParameters.initProcessEnabled` - Run an init process in the container 
`repositoryCredentials` - Credentials for private registries 
`restartPolicy` - Container restart policy
