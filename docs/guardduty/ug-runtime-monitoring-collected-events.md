<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-collected-events.html -->
<!-- Downloaded: 2026-10-28 -->

# Collected runtime event types that GuardDuty uses

The GuardDuty security agent collects the following events types and sends them to the GuardDuty backend for threat detection and analysis. GuardDuty doesn't make these events accessible to you. If GuardDuty detects a potential threat and generates a [Runtime Monitoring finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html), you can view the corresponding finding details.

For information about how GuardDuty uses the collected event types in Runtime Monitoring, see [Opting out of using your data for service improvement](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-opting-out-using-data.html).

## Process events

Process events represent information associated with the processes running on Amazon EC2 instances and container workloads. The following table includes the field names and descriptions of the process events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Process name |

Name of the observed process. |
Process Path |

Absolute path of the process executable. |
Process ID |

The ID assigned to the process by the operating system. |
Namespace PID |

The process ID of the process in a secondary PID namespace other than the host level PID namespace. For processes inside a container, it is the process ID observed inside the container. |
Process User ID |

The unique ID of the user that executed the process. |
Process UUID |

The unique ID assigned to the process by GuardDuty. |
Process GID |

Process ID of the process group. |
Process EGID |

Effective group ID of the process group. |
Process EUID |

Effective user ID of the process. |
Process User Name |

The user name that executed the process. |
Process Start Time |

The time when the process was created. This field is in the UTC date string format (`2023-03-22T19:37:20.168Z`). |
Process Executable SHA-256 |

The `SHA256` hash of the process executable. |
Process Script Path |

Path of the script file that was executed. |
Process Environment Variable |

The environment variable made available to the process. Only `LD_PRELOAD` and `LD_LIBRARY_PATH` get collected.  |
Process Present Working Directory (PWD) |

Present working directory of the process. |
Parent process |

Process details of the parent process. A parent process is a process that created the observed process. |
Command Line Arguments

Presently, this field is limited to specific agent versions corresponding to the resource type:

-

Fargate (Amazon ECS only) with GuardDuty security agent v1.0.0 and above.
-

Amazon EC2 instances with GuardDuty security agent v1.0.0 and above.
-

Amazon EKS clusters with security agent v1.4.0 and above.

For more information, see [GuardDuty security agent release versions](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-release-history.html).  |

Command-line arguments provided at the time of process execution. This field might contain sensitive customer data.  |

## Container events

Container events represent information associated with activities of the container workloads. The following table includes the field names and descriptions of the container workload events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Container Name |

Name of the container.

When available, this field displays the value of the label `io.kubenetes.container.name`.  |
Container UID |

The unique ID of the container assigned by the container runtime. |
Container Runtime |

The container runtime (such as `docker` or `containerd`) used to run the container. |
Container Image ID |

The ID of the container image. |
Container Image Name |

Name of the container image. |

## AWS Fargate (Amazon ECS only) task events

Fargate-Amazon ECS task events represent activities associated with Amazon ECS tasks running on Fargate computes. The following table includes the field names and descriptions of the Amazon ECS-Fargate task events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Task Amazon Resource Name (ARN) |

The ARN of the task. |
Cluster Name |

The name of the Amazon ECS cluster. |
Family Name |

The task definition's family name. The `family` is used as a name for the task definition that is used to launch the task. |
Service Name |

The name of the Amazon ECS service, if the task was launched as part of a service. |
Launch Type |

The infrastructure on which your task runs. For Runtime Monitoring with resource type as `ECSCluster`, the launch type could be either `EC2` or `FARGATE`. |
CPU |

The number of CPU units used by the task as expressed in the task definition. |

## Kubernetes pod events

The following table includes the field names and descriptions of the Kubernetes pod events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Pod ID |

The ID of the Kubernetes pod. |
Pod name |

Name of the Kubernetes pod. |
Pod Namespace |

Name of the Kubernetes namespace to which the Kubernetes workload belongs. |
Kubernetes Cluster Name |

Name of the Kubernetes cluster. |

## Domain Name System (DNS) events

The Domain Name System (DNS) events includes details of the DNS queries made by your resource types and corresponding responses. The following table includes the field names and descriptions of the DNS events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Socket Type |

Type of socket to indicate communication semantics. For example, `SOCK_RAW`. |
Address Family |

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IPv4 protocol. |
Direction ID |

The ID of the connection direction. |
Protocol Number |

The layer 4 protocol number such as 17 for UDP and 6 for TCP. |
DNS Remote Endpoint IP |

The remote IP of the connection. |
DNS Remote Endpoint Port |

The port number of the connection. |
DNS Local Endpoint IP |

The local IP of the connection. |
DNS Local Endpoint Port |

The port number of the connection. |
DNS Payload |

The payload of DNS packets that contains DNS queries and responses. |

## Open events

Open events are associated with file access and modification. The following table includes the field names and descriptions of the open events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Filepath |

Path of the file that is opened in this event. |
Flags |

Describes the file access mode, such as read-only, write-only, and read-write. |

## Load module event

The following table includes the field name and description of the load module event that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Module Name |

Name of the module loaded into the kernel. |

## Mprotect events

Mprotect events provide information about changes to the memory protection settings of the processes running on the monitored systems. The following table includes the field names and descriptions of the Mprotect events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Address Range |

The address range for which the access protections were modified. |
Memory Regions |

Specifies the region of a process's address space such as stack and heap. |
Flags |

Represents options that control the behavior of this event. |

## Mount events

Mount events provide information associated with the mounting and unmounting of file systems on your monitored resource. The following table includes the field names and descriptions of the mount events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Mount Target |

The path where the mount source is mounted. |
Mount Source |

The path on the host that is mounted at the mount target. |
Filesystem Type |

Represents the type of mounted fileSystem. |
Flags |

Represents options that control the behavior of this event. |

## Link events

Link events provide visibility into the file system link management activities in your monitored resources. The following table includes the field names and descriptions of the link events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Link Path |

Path where the hard link gets created. |
Target Path |

Path of the file at which the hard link points. |

## Symlink events

Symlink events provide visibility into the file system symbolic link management activities in your monitored resources. The following table includes the field names and descriptions of the symlink events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Link Path |

Path where the symbolic link is created. |
Target Path |

Path of the file at which the symbolic link points. |

## Dup events

Dup events provide visibility into the duplication of file descriptors by processes running on the monitored resources. The following table includes the field names and descriptions of the dup events that Runtime Monitoring collects to detect potential threats.
Field name |

Description |
|---|---|
Old File Descriptor |

A file descriptor that represents an open file object. |
New File Descriptor |

A new file descriptor that is a duplicate of the old file descriptor. Both the old and new file descriptors represent the same open file object. |
Dup Remote Endpoint IP |

The remote IP address of the network socket represented by the old file descriptor. Only applicable when the old file descriptor represents a network socket. |
Dup Remote Endpoint Port |

The remote port of the network socket represented by the old file descriptor. Only applicable when the old file descriptor represents a network socket. |
Dup Local Endpoint IP |

The local IP address of the network socket represented by the old file descriptor. Only applicable when the old file descriptor represents a network socket. |
Dup Local Endpoint Port |

The local port of the network socket represented by the old file descriptor. Only applicable when the old file descriptor represents a network socket. |

## Memory map event

The following table includes the field name and description of the memory map events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Filepath |

Path of the file to which the memory is mapped. |

## Socket events

Socket events provide information about the network socket connections used in the activities of the monitored resources. The following table includes the field names and descriptions of the socket events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Address family |

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IPv4 protocol. |
Socket Type |

Type of socket to indicate communication semantics. For example, `SOCK_RAW`. |
Protocol number |

Specifies a particular protocol within the address family. Usually there is a single protocol in address families. For example, the address family `AF_INET` only has the IP protocol. |

## Connect events

Connect events provide visibility into the network connections established by the processes on your monitored resources. The following table includes the field names and descriptions of the connect events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Address family |

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IPv4 protocol. |
Socket Type |

Type of socket to indicate communication semantics. For example, `SOCK_RAW`. |
Protocol Number |

Specifies a particular protocol within the address family. Usually there is a single protocol in address families. For example, the address family `AF_INET` only has the IP protocol. |
Filepath |

Path of the socket file if the address family is `AF_UNIX`. |
Remote Endpoint IP |

The remote IP of the connection. |
Remote Endpoint Port |

The port number of the connection. |
Local Endpoint IP |

The local IP of the connection. |
Local Endpoint Port |

The port number of the connection. |

## Process VM Readv events

Process VM readv events provide visibility into the read operations performed by the processes on their own virtual memory regions. The following table includes the field names and descriptions of the process VM readv events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Flags |

Represents options that control the behavior of this event. |
Target PID |

Process ID of the process from which memory is being read. |
Target Process UUID |

The unique ID of the target process. |
Target Executable Path |

The absolute path of the target process executable file. |

## Process VM Writev events

Process VM writev events provide visibility into the write operations performed by the processes on their own virtual memory regions. The following table includes the field names and descriptions of the process VM writev events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Flags |

Represents options that control the behavior of this event. |
Target PID |

Process ID of the process to which memory is being written. |
Target Process UUID |

The unique ID of the target process. |
Target Executable Path |

The absolute path of the target process executable file. |

## Process trace (Ptrace) events

Process trace (Ptrace) system call is a debugging and tracing mechanism that allows one process (tracer) to observe and control the execution of another process (tracee). This provides the tracer with the ability to inspect and modify the target process's memory, registers, and execution flow.

Ptrace events provide visibility into the use of ptrace system call by processes running on the monitored resources. The following table includes the field names and descriptions of the ptrace events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Target PID |

Process ID of the target process. |
Target Process UUID |

The unique ID of the target process. |
Target Executable Path |

The absolute path of the target process executable file. |
Flags |

Represents options that control the behavior of this event. |

## Bind events

Bind events provide visibility into binding of network sockets by processes running on the monitored resources. The following table includes the field names and descriptions of the bind events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Address Family |

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IPv4 protocol. |
Socket type |

Type of socket to indicate communication semantics. For example, `SOCK_RAW`. |
Protocol number |

The layer 4 protocol number such as 17 for UDP and 6 for TCP. |
Local endpoint IP |

The local IP of the connection. |
Local endpoint port |

The port number of the connection. |

## Listen events

Listen events provide visibility into the listening state of network sockets, indicating whether or not a network socket is ready to accept incoming connections. A process running on your monitored resource sets the network socket to a listening state. The following table includes the field names and descriptions of the listen events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Address Family |

Represents the communication protocol associated with the address. For example, the address family `AF_INET` is used for IPv4 protocol. |
Socket type |

Type of socket to indicate communication semantics. For example, `SOCK_RAW`. |
Protocol number |

The layer 4 protocol number such as 17 for UDP and 6 for TCP. |
Local endpoint IP |

The local IP of the connection. |
Local endpoint port |

The port number of the connection. |

## Rename events

Rename events provide information about the renaming of files and directories by processes running on the monitored resources. The following table includes the field names and descriptions of the rename events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Filepath |

Path of the file that is renamed. |
Target |

The new path of the file. |

## Set user ID (UID) events

Set user ID (UID) events provide visibility into the changes made to the user ID (UID) associated with the running processes on your monitored resources. The following table includes the field names and descriptions of the set UID events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
New EUID |

The new effective user ID of the process. |
New UID |

The new user ID of the process. |

## Chmod events

Chmod events provide visibility into the changes in the permissions (mode) of files and directories on the monitored resources. The following table includes the field names and descriptions of the chmod events that Runtime Monitoring collects to detect potential threats.

|  Field name |  Description |
|---|---|
Filepath |

Path of the file that invokes this event. |
Filemode |

The updated access permissions for the associated file. |
