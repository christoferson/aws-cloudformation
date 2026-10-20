> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html
> Downloaded: 2026-10-20

# Balancing an Amazon ECS service across Availability Zones

Starting September 5, 2025, Amazon ECS enables Availability Zone rebalancing for all services that are eligible for the feature. A service is eligible when Availability Zone spread is the first task placement strategy, or when there is no placement strategy.

To help your applications achieve high availability, we recommend configuring your multi-task services to run across multiple Availability Zones. For services that specify their first placement strategy to be Availability Zone spread, AWS makes a best effort to evenly distribute service tasks across the available Availability Zones.

However, there might be times when the number of tasks running in one Availability Zone is not the same as in other Availability Zones, such as after an Availability Zone disruption. To address this task imbalance, you can enable the Availability Zone rebalancing feature.

With Availability Zone rebalancing, Amazon ECS continuously monitors the distribution of tasks across Availability Zones for each of your services. When Amazon ECS detects an uneven task distribution, it automatically takes action to rebalance the workload across Availability Zones. This involves launching new tasks in the Availability Zones with the fewest tasks and terminating tasks in the overloaded Availability Zones.

This redistribution ensures no single Availability Zone becomes a point of failure, helping maintain the overall availability of your containerized applications. The automated rebalancing process eliminates the need for manual intervention, speeding the time to recovery after an event.

The following is an overview of the Availability Zone rebalancing process: 
Amazon ECS starts monitoring a service after it reaches the steady state, and looks at the number of tasks running in each Availability Zone. 
Amazon ECS performs the following operations when it detects an imbalance in the number of tasks running in each Availability Zone:  
Sends a service event indicating that Availability Zone rebalancing is starting. 
Starts tasks in Availability Zones with the fewest number of running tasks 
Stops the tasks in Availability Zones with the largest number of running tasks. 
The scheduler waits for the newly started tasks to be `HEALTHY` and `RUNNING` before stopping the tasks in the over-scaled Availability Zone. 
Sends a service event with the Availability Zone rebalancing outcome. 
 
 

## How Amazon ECS detects uneven task distribution 

Amazon ECS determines an imbalance in the number of tasks running in each Availability Zone by dividing the service's desired task count by the number of configured Availability Zones. If the desired task count doesn't divide evenly, Amazon ECS distributes the remainder of tasks evenly across the configured Availability Zones. Each Availability Zone must have at least one task. 

For example, consider an Amazon ECS service with a desired count of two tasks configured for two Availability Zones. In this scenario, the desired task count divides evenly. A balanced distribution would be one task per Availability Zone. If there are two tasks in Availability Zone 1 and zero tasks in Availability Zone 2, Amazon ECS would initiate rebalancing by starting a task in Availability Zone 2 before stopping a task in Availability Zone 1. 

Now, consider an Amazon ECS service with a desired count of three tasks configured for two Availability Zones. In this scenario, the desired task count does not divide evenly. A balanced distribution would be one task in Availability Zone 1 and two tasks in Availability Zone 2 because each Availability Zone has at least one task and the remainder task is placed in Availability Zone 2. 

Consider an Amazon ECS service that has a desired count of five tasks configured for three Availability Zones. In this scenario, the desired task count does not divide evenly. A balanced distribution would be one task in Availability Zone 1 and two tasks each in Availability Zones 2 and 3. After accounting for every Availability Zone having one task each, the two remainder tasks are distributed evenly across the Availability Zones. 

## Considerations for configuring Availability Zone rebalancing 

Consider the following when you want to configure Availability Zone rebalancing:  
Availability Zone rebalancing supports Fargate and EC2 capacity providers, and is supported on Amazon ECS Managed Instances. For Fargate, Amazon ECS will automatically redistribute tasks across available Availability Zones to maintain balance. For EC2 capacity providers, Amazon ECS rebalances tasks across existing container instances on a best-effort basis, respecting your defined placement strategies and constraints. However, Amazon ECS can't launch new instances in underutilized Availability Zones as part of the rebalancing process, limiting the rebalancing to existing container instances.
Availability Zone rebalancing works in the following configurations:  
Services that use the `Replica` strategy 
Services that specify Availability Zone spread as the first task placement strategy, or do not specify a placement strategy. 
You can't use Availability Zone rebalancing with services that meet any of the following criteria:  
Uses the `Daemon` strategy 
Uses the `EXTERNAL` launch type (ECS Anywhere) 
Uses 100% for the `maximumPercent` value 
Uses a Classic Load Balancer 
Uses the `attribute:ecs.availability-zone` as a task placement constraint 
 
 

## Placement strategies and placement constraints with Availability Zone rebalancing 

Placement strategies determine how Amazon ECS selects container instances and Availability Zones for task placement termination. Task placement constraints are rules that determine whether a task is allowed to run on a specific container instance. 

For EC2, you can use placement strategies and placement constraints in conjunction with Availability Zone rebalancing. However, for Availability Zone rebalancing to work, the Availability Zone spread placement strategy must be the first strategy specified. 

Availability Zone rebalancing is compatible with various placement strategy combinations. For example, you can create a strategy that first distributes tasks evenly across Availability Zones, and then bin packs tasks based on memory within each Availability Zone. In this case, Availability Zone rebalancing works because the Availability Zone spread strategy is specified first. 

It's important to note that Availability Zone rebalancing won't work if the first strategy in the placement strategy array is not an Availability Zone spread component. This requirement ensures that the primary focus of task distribution is maintaining balance across Availability Zones, which is crucial for high availability. 

For more information about task placement strategies and constraints, see How Amazon ECS places tasks on container instances. 

Task placement strategies and constraints aren't supported for tasks using Fargate. Fargate will try its best to spread tasks across accessible Availability Zones. If the capacity provider includes both Fargate and Fargate Spot, the spread behavior is independent for each capacity provider. 

The following example strategy distributes tasks evenly across Availability Zones, and then bin packs tasks based on memory within each Availability Zone. Availability Zone rebalancing is compatible with the service because the `spread` strategy is first. 

```
"placementStrategy": [
    {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
    },
    {
        "field": "memory",
        "type": "binpack"
    }
]
```
 

## Turn on Availability Zone rebalancing 

You need to enable Availability Zone rebalancing for new and existing services. 

You can enable and disable Availability Zone rebalancing using the console, APIs, AWS CLI, and CloudFormation. 

The default behavior of `AvailabilityZoneRebalancing` differs between create and update requests:  
For create service requests, when when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults the value to to `ENABLED`. 
For update service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults to the existing service’s `AvailabilityZoneRebalancing` value. If the service never had an `AvailabilityZoneRebalancing` value set, Amazon ECS treats this as `DISABLED`. 
  
|  Service type |  API |  Console |  CLI |    
|  Existing |  UpdateService |   Updating an Amazon ECS service  |  update-service |   
|  New |  CreateService |   Creating an Amazon ECS rolling update deployment  |  create-service |    

The following example shows how to enable service rebalancing when creating a new service: 

```
aws ecs create-service \
    --cluster my-cluster \
    --service-name my-service \
    --task-definition my-task-definition:1 \
    --desired-count 6 \
    --availability-zone-rebalancing ENABLED
```
 

## Troubleshooting service rebalancing 

If you encounter issues with service rebalancing, consider the following troubleshooting steps:   

**Rebalancing doesn't start**  

Verify that:  
Service rebalancing is enabled for your service 
Your service uses a supported configuration (see Considerations for configuring Availability Zone rebalancing) 
Your service has reached a steady state 
  

**Task placement failures during rebalancing**  

If you see `SERVICE_TASK_PLACEMENT_FAILURE` events:  
For EC2: Check if you have container instances available in the target Availability Zone 
For Fargate: Check if there are resource constraints or service quotas limiting task placement 
Review your task placement constraints to ensure they're not preventing proper task distribution 
  

**Rebalancing stops unexpectedly**  

If you see `SERVICE_REBALANCING_STOPPED` events:  
Check for task protection that might be blocking the operation 
Look for concurrent service deployments that could interrupt rebalancing 
Review service events for additional information about why rebalancing stopped 
   

## Best practices for service rebalancing 

Follow these best practices to get the most out of service rebalancing:  
Monitor rebalancing operations - Set up CloudWatch alarms to monitor service events related to rebalancing to quickly identify any issues. 
Consider performance impact - Be aware that rebalancing operations may temporarily increase resource usage as new tasks are started before old ones are stopped. 
Use task protection strategically - If you have critical tasks that shouldn't be terminated during rebalancing, consider using task protection. 
Plan for EC2 capacity - For EC2, ensure you have sufficient container instances across all Availability Zones to support effective rebalancing. 
Test rebalancing behavior - Before relying on rebalancing in production, test how your services behave during rebalancing operations in a non-production environment.
