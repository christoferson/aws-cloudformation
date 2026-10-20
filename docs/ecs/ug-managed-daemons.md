> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-daemons.html
> Downloaded: 2026-10-20

# Amazon ECS Managed Daemons

Amazon ECS Managed Daemons enable you to deploy and manage software agents, such as security, observability, and networking agents, across your container infrastructure on Amazon ECS Managed Instances. Managed Daemons decouple daemon lifecycle management from application operations. You can deploy, update, and monitor agents independently, without redeploying workloads or coordinating changes across services. 

## Daemon criticality 

You can configure each managed daemon as critical or non-critical, based on whether a daemon failure should cause Amazon ECS to drain the container instance.  
Critical - The default. Amazon ECS starts the daemon task before it places application tasks on the instance, and if the daemon task stops or becomes unhealthy, Amazon ECS drains and replaces the container instance. 
Non-critical - Set the `critical` parameter to `false`. The daemon task operates independently of container instance health. If a non-critical daemon task fails, stops, or becomes unhealthy, Amazon ECS keeps the container instance active. Existing application tasks keep running, and Amazon ECS keeps placing new application tasks on it. A non-critical daemon never blocks instance registration, so application tasks can be placed immediately even if the daemon fails to start. 
 

## How Managed Daemons work 

To use Managed Daemons, first register a daemon task definition. A daemon task definition is a template that describes the containers that form a daemon. After you register a daemon task definition, create a daemon and associate it with a cluster and one or more Amazon ECS Managed Instances capacity providers. Amazon ECS then ensures that exactly one daemon task runs on every Amazon EC2 instance provisioned through those capacity providers. 

Daemons do not launch instances independently. When you run an application task on a Amazon ECS Managed Instances capacity provider, Amazon ECS provisions an Amazon EC2 instance, starts the daemon task, and only then transitions the application task to `RUNNING`. Amazon ECS uses this ordering for every daemon, regardless of criticality, so that cross-cutting functions like logging, tracing, and metrics collection are operational before your application begins processing requests. 

Criticality controls what Amazon ECS does when a daemon task doesn't start, or stops later. For a critical daemon, a task that fails to start keeps the instance from becoming active. A task that stops or becomes unhealthy after the instance is active causes Amazon ECS to drain and replace the instance. This auto-repair behavior maintains reliable daemon coverage without manual intervention. 

A non-critical daemon never blocks the instance and never triggers a drain. The instance becomes active even if the daemon task fails to start, and stays active if the daemon task stops or becomes unhealthy later. Your application tasks keep running, and Amazon ECS keeps placing new application tasks on the instance. 

When you update a daemon to a new task definition revision, Amazon ECS performs a rolling deployment across all instances in the associated capacity providers. During the deployment, Amazon ECS drains a configurable percentage of instances simultaneously, provisions replacement instances with the updated daemon, and replaces your Amazon ECS service tasks automatically. Amazon ECS provides built-in circuit breaker protection. You can configure a bake time and CloudWatch alarms so that Amazon ECS monitors the deployment after it updates all instances and automatically rolls back if issues arise. Amazon ECS emits an EventBridge event and records a service action log when a daemon task fails to start, for both critical and non-critical daemons. 

## Key benefits  
Decoupled lifecycle management - Update daemons independently from application deployments. 
Guaranteed coverage - Amazon ECS starts the daemon task before application tasks on every instance, so cross-cutting functions are operational before your application begins processing requests. For a critical daemon, a daemon task that fails to start also keeps the instance from registering, so an instance never serves application tasks without its daemon. 
Reliable version updates - When you update a daemon version, Amazon ECS rolls it out across all instances in the associated capacity providers, with built-in circuit breaker protection and automatic rollback to ensure every instance runs the target revision. 
Improved resource utilization - Running a single daemon task per instance eliminates the sidecar-per-task model, reducing resource overhead across your cluster. 
Automatic instance repair - For a critical daemon, if the daemon task stops or becomes unhealthy, Amazon ECS automatically drains and replaces that container instance. This maintains reliable daemon coverage without manual intervention. 
Workload continuity - Non-critical daemons keep your application workloads running uninterrupted, even if a daemon task fails, stops, or becomes unhealthy. 
 Note

Amazon ECS offers a DAEMON scheduling strategy for Amazon ECS services for the Amazon EC2 launch type. Managed Daemons is a new capability built for Amazon ECS Managed Instances to simplify daemon deployments and provide stronger daemon coverage guarantees. 

## Getting started 

To get started, register a daemon task definition specifying your container image, then create a daemon with associated capacity providers in your cluster. You can use the AWS Management Console, AWS CLI, CloudFormation, or AWS SDKs. For step-by-step instructions, see Creating and managing daemons.
