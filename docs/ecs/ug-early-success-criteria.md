> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/early-success-criteria.html
> Downloaded: 2026-10-20

# Complete Amazon ECS rolling deployments early with early success criteria

When you update a service that uses the rolling deployment strategy, Amazon ECS starts a deployment that replaces the tasks on the source service revision with new tasks on the target service revision. Amazon ECS completes the deployment after all of the following are true: 
The target service revision reaches 100 percent of the desired count, and all of its tasks are running and healthy. 
The deployment circuit breaker or a CloudWatch alarm does not trigger a rollback. 
If you use alarm-based rollback, the bake time elapses. 
The tasks on the source service revision are cleaned up. 

With early success criteria, you configure when Amazon ECS completes a deployment, based on the confidence and operational needs of your workload.

You can use early success criteria in the following scenarios: 
You are confident that a percentage of healthy tasks on the target service revision is enough to complete the deployment, and you want to complete it sooner so that subsequent deployments, CI/CD pipelines, and other dependent operations can proceed. 
Your service runs on specialized or constrained capacity, such as GPU-accelerated inference workloads, where some tasks take longer to launch because of hardware availability. 
Your service has tasks on the source service revision that are slow to drain and would otherwise hold the deployment open, such as tasks with long-lived connections. 
You want the deployment circuit breaker or CloudWatch alarm rollback to protect the deployment until the target service revision reaches a health level that you define, and you do not want a rollback after that point. 

You define the criteria by using the following settings in the deployment configuration. 

## Healthy percent 

The `earlySuccessCriteria.healthyPercent` represents the number of tasks that must be running and healthy on the target service revision before Amazon ECS completes the deployment, as a percent of the desired number of tasks for the service. This value is rounded up. For example, if the healthy percent is 90 and the desired count is 100, Amazon ECS completes the deployment after 90 tasks are healthy. If the healthy percent is 50 and the desired count is 3, Amazon ECS completes the deployment after 2 tasks are healthy. 

A task is healthy when it passes the health checks that you configure for the service. 

Amazon ECS launches any remaining tasks on the target service revision outside of the deployment, through regular service scaling. After Amazon ECS completes the deployment, the deployment circuit breaker and CloudWatch alarm rollback no longer apply. 

The healthy percent must be between the service `minimumHealthyPercent` and 100. 

## Source service revision cleanup 

The `earlySuccessCriteria.sourceServiceRevisionCleanup` determines when Amazon ECS cleans up the tasks from the source service revision. It has two values, `BLOCKING` and `DEFERRED`. 

With `BLOCKING`, the deployment proceeds in the following order:  
The healthy percent of tasks are running and healthy on the target service revision. 
If you use alarm-based rollback, the bake time elapses. 
Amazon ECS cleans up the tasks on the source service revision. 
Amazon ECS completes the deployment. 
 

With `DEFERRED`, the deployment proceeds in the following order:  
The healthy percent of tasks are running and healthy on the target service revision. 
If you use alarm-based rollback, the bake time elapses. 
Amazon ECS completes the deployment. 
Amazon ECS cleans up the tasks on the source service revision, outside of the deployment. 
 

With `DEFERRED`, Amazon ECS tries to clean up the tasks on the source service revision for up to two weeks. 

Use `DEFERRED` for services with long-lived connections or task scale-in protection, where tasks from the source service revision might need to keep running without holding the deployment open. This is useful when draining the source service revision is a long-tail operation and your CI/CD tooling has time limits. Amazon ECS completes the deployment when the healthy percent is met, and the tasks on the source service revision drain outside of the deployment. 

## How Amazon ECS evaluates early success criteria 

Amazon ECS completes a deployment that uses early success criteria after all of the following are true:  
The number of running and healthy tasks on the target service revision is at least the healthy percent of the desired count, rounded up. 
The deployment circuit breaker or a CloudWatch alarm does not trigger a rollback. 
If you use alarm-based rollback, the bake time elapses. 
If source service revision cleanup is `BLOCKING`, the tasks on the source service revision are cleaned up. 
 

Amazon ECS launches at least one task on the target service revision and waits for it to become healthy before it evaluates the healthy percent. Example healthy task counts 
|  Desired count |  Healthy percent |  Required healthy tasks (rounded up) |    
|  2 |  50 |  1 |   
|  3 |  50 |  2 |   
|  10 |  80 |  8 |   
|  100 |  90 |  90 |   
|  10 |  100 |  10 |    

## Configure early success criteria 

You can configure early success criteria for a new or existing service by using the console or the AWS CLI.   

**Console**  

In the create service or update service flow, under Deployment configuration, turn on early success criteria. Enter a value for Healthy percent, and choose a Source service revision cleanup option, either Blocking or Deferred.  

**AWS CLI**  

Set the `earlySuccessCriteria` values in the `--deployment-configuration` parameter when you create or update a service. 

```
aws ecs update-service \
    --cluster MyCluster \
    --service MyService \
    --deployment-configuration '{
        "strategy": "ROLLING",
        "earlySuccessCriteria": {
            "enable": true,
            "healthyPercent": 90,
            "sourceServiceRevisionCleanup": "BLOCKING"
        }
    }'
```
   

## What you observe  
`DescribeServiceDeployments` returns the deployment status and the configured early success criteria. While the deployment is in progress, the task counts are live. After the deployment completes, the task counts are a snapshot from when the deployment completed. This applies to both `BLOCKING` and `DEFERRED`. 
To view live task counts for a service, use `DescribeServices`. 
Deployments that complete early are included when you filter `ListServiceDeployments` by a status of `SUCCESSFUL`. 
Deployment state-change events and AWS CloudTrail records show the standard `IN_PROGRESS` to `SUCCESSFUL` lifecycle. Early success criteria does not add a new deployment status. 
 

## Considerations 

Review the following considerations before you use early success criteria.   

**Rollback monitoring applies during the deployment**  

The deployment circuit breaker and CloudWatch alarm rollback are failure-detection mechanisms for the deployment. They can roll back the deployment while it is in progress. After Amazon ECS completes the deployment, these mechanisms no longer roll back the service, including while Amazon ECS launches any remaining tasks through regular service scaling. You can't stop a deployment after it completes. Set the healthy percent to a percentage at which you are confident that the target service revision is healthy.  

**`DEFERRED` cleanup**  

With `DEFERRED`, Amazon ECS cleans up the tasks on the source service revision after it completes the deployment. If the tasks on the source service revision are protected, by task scale-in protection or another mechanism, for more than two weeks after the deployment, Amazon ECS can't clean them up. Use `DescribeServices` to monitor the tasks on the source service revision.
