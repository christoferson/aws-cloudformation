> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/pause-lifecycle-hooks.html
> Downloaded: 2026-10-18

# Pause hooks for Amazon ECS service deployments

Pause hooks pause an Amazon ECS service deployment at a specific lifecycle stage and wait for you to call `ContinueServiceDeployment` before the deployment proceeds. Use pause hooks when you need manual approval or external validation before a deployment continues. 

## How pause hooks work 

When a deployment reaches a lifecycle stage that has a pause hook configured, the following occurs:  
Amazon ECS generates a unique `hookId` for the pause hook. 
Amazon ECS emits an EventBridge event with the detail-type `ECS Hook State Change` and the event name `HOOK_AWAITING_ACTION`. 
The deployment remains paused until you call `ContinueServiceDeployment` with the `hookId` and an action of `CONTINUE` or `ROLLBACK`, or until the configured timeout is reached. 
 

You can retrieve the `hookId` by calling `DescribeServiceDeployments`. The response includes a `lifecycleHookDetails` array with the hook status: 

```

{
    "serviceDeployments": [
        {
            "lifecycleHookDetails": [
                {
                    "hookId": "ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw",
                    "targetType": "PAUSE",
                    "status": "AWAITING_ACTION",
                    "expiresAt": "2024-01-15T12:00:00Z",
                    "timeoutAction": "ROLLBACK"
                }
            ]
        }
    ]
}
    
```
 

## Configuring pause hooks 

The following example shows a pause hook configuration in a service definition that pauses the deployment after the test traffic shift completes: 

```

{
    "deploymentConfiguration": {
        "strategy": "BLUE_GREEN",
        "lifecycleHooks": [
            {
                "targetType": "PAUSE",
                "lifecycleStages": [
                    "POST_TEST_TRAFFIC_SHIFT"
                ],
                "timeoutConfiguration": {
                    "timeoutInMinutes": 10,
                    "action": "ROLLBACK"
                }
            }
        ]
    }
}
    
```
 

### Configuration fields  
|  Field |  Description |  Valid values |  Required |    
|  `targetType` |  The type of hook. Must be `PAUSE` for pause hooks. |  `PAUSE` |  Yes |   
|  `lifecycleStages` |  The lifecycle stages at which the deployment pauses. |  `RECONCILE_SERVICE`, `PRE_SCALE_UP`, `POST_SCALE_UP`, `POST_TEST_TRAFFIC_SHIFT`, `PRE_PRODUCTION_TRAFFIC_SHIFT`, `POST_PRODUCTION_TRAFFIC_SHIFT` |  Yes |   
|  `timeoutConfiguration.timeoutInMinutes` |  How long to wait before taking the timeout action. Default: 1,440 minutes (24 hours). |  1 - 20,160 (14 days) |  No |   
|  `timeoutConfiguration.action` |  The action to take if the timeout expires. |  `ROLLBACK` (default), `CONTINUE` |  No |    

## Constraints  
You can configure a maximum of 10 pause hooks and 10 Lambda hooks per service. 
Pause hooks do not use `hookTargetArn` or `roleArn`. These fields are only for Lambda hooks. 
Pause hooks cannot be configured at the `TEST_TRAFFIC_SHIFT` or `PRODUCTION_TRAFFIC_SHIFT` stages. 
 

## Continuing a paused deployment 

When a deployment is paused (the pause hook status is `AWAITING_ACTION`), call `ContinueServiceDeployment` with the `hookId` and the action you want to take. 

To continue the deployment: 

```

aws ecs continue-service-deployment \
    --hook-id ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw \
    --action CONTINUE
    
```
 

To roll back the deployment: 

```

aws ecs continue-service-deployment \
    --hook-id ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw \
    --action ROLLBACK
    
```
 

For more information, see Continuing service deployments. 

## Multiple hooks at the same stage 

When multiple hooks are configured at the same lifecycle stage, the deployment stays paused until all hooks at that stage are continued. If any hook triggers a rollback, the entire deployment rolls back regardless of the status of other hooks at that stage. 

This behavior applies when both Lambda hooks and pause hooks are configured at the same lifecycle stage. The deployment proceeds only when all hooks at that stage have completed successfully or been continued. 

All hooks configured at the same lifecycle stage run in parallel. 

## Timeout behavior 

If you do not call `ContinueServiceDeployment` before the timeout expires, Amazon ECS takes the configured timeout action:  
`ROLLBACK` (default) - Amazon ECS rolls back the deployment to the previous service revision. 
`CONTINUE` - Amazon ECS continues the deployment to the next lifecycle stage. 
 

Check the `expiresAt` field in the `lifecycleHookDetails` array of the `DescribeServiceDeployments` response to see when the timeout expires. 

## Pause hooks with linear and canary deployments 

For linear and canary deployments, pause hooks configured at `PRE_PRODUCTION_TRAFFIC_SHIFT` are invoked at each traffic shift step. Each invocation generates a unique `hookId`, and you must call `ContinueServiceDeployment` for each one. 

For example, a linear deployment with 5 traffic shift steps and a pause hook at `PRE_PRODUCTION_TRAFFIC_SHIFT` pauses 5 times - once before each step. Each pause requires a separate call to `ContinueServiceDeployment` with the corresponding `hookId`. 

## EventBridge events 

Amazon ECS emits EventBridge events with the detail-type `ECS Hook State Change` as pause hooks progress through their lifecycle. The following table describes the event names:  
|  Event name |  Description |    
|  `HOOK_AWAITING_ACTION` |  The hook is waiting for you to call `ContinueServiceDeployment`. |   
|  `HOOK_SUCCEEDED` |  The hook completed successfully (you called `ContinueServiceDeployment` with `CONTINUE`). |   
|  `HOOK_FAILED` |  The hook failed (you called `ContinueServiceDeployment` with `ROLLBACK`). |   
|  `HOOK_TIMED_OUT` |  The hook timed out before `ContinueServiceDeployment` was called. |    

The following example shows an EventBridge event emitted when a pause hook is awaiting action: 

```

{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "ECS Hook State Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2024-01-15T10:00:00Z",
    "region": "us-west-2",
    "detail": {
        "eventType": "INFO",
        "eventName": "HOOK_AWAITING_ACTION",
        "hookId": "ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw",
        "hookType": "PAUSE",
        "expiresAt": "2024-01-15T12:00:00Z",
        "lifecycleStage": "POST_TEST_TRAFFIC_SHIFT",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
        "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
        "updatedAt": "2024-01-15T10:00:00Z"
    }
}
    
```
