> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/lambda-lifecycle-hooks.html
> Downloaded: 2026-10-18

# Lambda hooks for Amazon ECS service deployments

Lambda hooks are Lambda functions that Amazon ECS invokes at specific stages of a deployment. You can use hooks to run validation tests, enforce governance policies, or implement custom logic before the deployment proceeds.

When Amazon ECS invokes your hook, your function must return a JSON object containing a `hookStatus` field. You can optionally include `callBackDelay` to control retry timing and `hookDetails` to pass data between invocations. If your function doesn't return a valid `hookStatus`, or if it fails, Amazon ECS rolls back the deployment. 

## hookStatus values 

The following are the valid `hookStatus` values:  
`SUCCEEDED` - The deployment continues to the next lifecycle stage. 
`FAILED` - Amazon ECS rolls back the deployment to the last successful service revision. 
`IN_PROGRESS` - Amazon ECS invokes the function again after a delay. By default, the delay is 30 seconds. You can customize this value by returning a `callBackDelay` alongside the `hookStatus`. 
 

The following example shows how to return a `hookStatus` with a custom callback delay. In this example, Amazon ECS retries the hook after 60 seconds instead of the default 30 seconds: 

```

{
    "hookStatus": "IN_PROGRESS",
    "callBackDelay": 60
}
    
```
 

## Passing state with hookDetails 

The `hookDetails` field is a dictionary that you can use to pass data into your lifecycle hook function. There are two ways to populate `hookDetails`:  
At service creation or update - Define `hookDetails` in the lifecycle hook configuration within your service definition. Amazon ECS passes this data to your function on every invocation. Use this to make your hooks reusable across multiple services by passing in service-specific configuration. 
At runtime via IN_PROGRESS responses - Return `hookDetails` alongside the `IN_PROGRESS` hook status. Amazon ECS passes this data back to your function on the next invocation. Use this to maintain state between invocations without external storage. 
 

The following example shows a lifecycle hook configuration in a service definition that passes an S3 bucket name to the function: 

```

{
    "hookTargetArn": "arn:aws:lambda:us-west-2:123456789012:function:my-approval-hook",
    "roleArn": "arn:aws:iam::123456789012:role/ecs-lambda-invoke-role",
    "lifecycleStages": [
        "POST_TEST_TRAFFIC_SHIFT"
    ],
    "hookDetails": {
        "S3_BUCKET_NAME": "my-approval-bucket"
    }
}
    
```
 

When your function returns `IN_PROGRESS`, you can also include `hookDetails` in the response. Amazon ECS merges this data and passes it back on the next invocation. Common use cases include passing metric counters or ARNs of external resources between invocations. 

```

{
    "hookStatus": "IN_PROGRESS",
    "callBackDelay": 30,
    "hookDetails": {
        "approvalChecked": true,
        "S3_BUCKET_NAME": "my-approval-bucket"
    }
}
    
```
 

On the next invocation, Amazon ECS includes the `hookDetails` in the event payload alongside `executionDetails`: 

```

{
  "executionId": "e8d5a28f-eb01-4f3c-9454-a30ba6dc54bc",
  "lifecycleStage": "POST_TEST_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {}
  },
  "hookDetails": {
    "approvalChecked": true,
    "S3_BUCKET_NAME": "my-approval-bucket"
  }
}
    
```
 

Your function can read `event["hookDetails"]` to access the configuration and state from previous invocations. Note

Data added to `hookDetails` at runtime only persists between invocations of the same hook within a single deployment. Data doesn't carry over between different hooks within the same deployment or the same hook in different deployments. 

## Timeout configuration 

You can configure a timeout for Lambda hooks using `timeoutConfiguration`. If the Lambda function does not return `SUCCEEDED` or `FAILED` before the timeout expires, Amazon ECS takes the configured timeout action.  
|  Field |  Description |    
|  `timeoutConfiguration.timeoutInMinutes` |  How long to wait. Valid range: 1 to 1,440 (24 hours). Default: 1,440 minutes. |   
|  `timeoutConfiguration.action` |  The action to take if the timeout expires. Valid values: `ROLLBACK`, `CONTINUE`. Default: `ROLLBACK`. |    

## Supported lifecycle stages 

You can configure Lambda hooks at the following lifecycle stages:  
`RECONCILE_SERVICE`
`PRE_SCALE_UP`
`POST_SCALE_UP`
`TEST_TRAFFIC_SHIFT`
`POST_TEST_TRAFFIC_SHIFT`
`PRE_PRODUCTION_TRAFFIC_SHIFT`
`PRODUCTION_TRAFFIC_SHIFT`
`POST_PRODUCTION_TRAFFIC_SHIFT`
 

For linear and canary deployments, Lambda hooks configured at `PRODUCTION_TRAFFIC_SHIFT` or `PRE_PRODUCTION_TRAFFIC_SHIFT` are invoked at each traffic shift step. 

For more information about lifecycle stage categories, see Lifecycle hooks for Amazon ECS service deployments. 

## Lifecycle payloads 

### Common payload structure 

When Amazon ECS invokes your lifecycle hook Lambda function, the event payload contains the following top-level fields:  
`executionId` - The unique identifier for this hook execution. 
`lifecycleStage` - The current lifecycle stage (for example, `PRODUCTION_TRAFFIC_SHIFT`). 
`resourceArn` - The ARN of the resource associated with the deployment. 
`executionDetails` - An object containing the deployment-specific information described in the following list. 
 

The `executionDetails` object contains the following fields:  
`serviceArn` - The Amazon Resource Name (ARN) of the service. 
`targetServiceRevisionArn` - The ARN of the target service revision being deployed. 
`testTrafficWeights` - A map of service revision ARNs to their corresponding test traffic weight percentages. 
`productionTrafficWeights` - A map of service revision ARNs to their corresponding production traffic weight percentages. 
 

The following example shows the full event structure that your Lambda function receives: 

```

{
  "executionId": "f4fcae0f-9bec-41c6-ba87-0eaa0cef8af5",
  "lifecycleStage": "PRODUCTION_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900": 100,
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1920498462936580504": 0
    }
  }
}
      
```
 

### Lifecycle stage payloads 

The following sections show example payloads for each lifecycle stage. In these examples, the green service revision (`9313423515462893900`) is the new revision being deployed, and the blue service revision (`1920498462936580504`) is the existing production revision. 

#### PRE_SCALE_UP 

This stage occurs before Amazon ECS launches the green service revision tasks. The green service revision has not started, and no traffic is being routed to it. 

```

{
  "executionId": "e8d5a28f-eb01-4f3c-9454-a30ba6dc54bc",
  "lifecycleStage": "PRE_SCALE_UP",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {}
  }
}
        
```
 

#### POST_SCALE_UP 

This stage occurs after Amazon ECS has launched the green service revision tasks and they are healthy. The green tasks are running but not yet receiving any traffic. 

```

{
  "executionId": "8b095b05-7bb0-4c56-a223-a3f61f4f9295",
  "lifecycleStage": "POST_SCALE_UP",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {}
  }
}
        
```
 

#### TEST_TRAFFIC_SHIFT 

This stage occurs when Amazon ECS shifts test traffic to the green service revision. The `testTrafficWeights` show the green revision receiving 100% of test traffic while the blue revision receives 0%. Production traffic continues to flow to the blue revision. 

```

{
  "executionId": "779085de-ab47-42bc-84ad-41f9914a8643",
  "lifecycleStage": "TEST_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900": 100,
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1920498462936580504": 0
    },
    "productionTrafficWeights": {}
  }
}
        
```
 

#### POST_TEST_TRAFFIC_SHIFT 

This stage occurs after Amazon ECS has completed the test traffic shift. The green service revision is handling 100% of test traffic. 

```

{
  "executionId": "3a0345ba-b029-404b-890d-7da2a4b266aa",
  "lifecycleStage": "POST_TEST_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {}
  }
}
        
```
 

#### PRE_PRODUCTION_TRAFFIC_SHIFT 

This stage occurs before Amazon ECS shifts production traffic to the green service revision. For linear and canary deployments, this stage is invoked before each traffic shift step. 

```

{
  "executionId": "a2b3c4d5-e6f7-8901-abcd-ef1234567890",
  "lifecycleStage": "PRE_PRODUCTION_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900": 0,
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1920498462936580504": 100
    }
  }
}
        
```
 

#### PRODUCTION_TRAFFIC_SHIFT 

This stage occurs when Amazon ECS shifts production traffic to the green service revision. The `productionTrafficWeights` show the green revision receiving 100% of production traffic while the blue revision receives 0%. 

```

{
  "executionId": "f4fcae0f-9bec-41c6-ba87-0eaa0cef8af5",
  "lifecycleStage": "PRODUCTION_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900": 100,
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1920498462936580504": 0
    }
  }
}
        
```
 

#### POST_PRODUCTION_TRAFFIC_SHIFT 

This stage occurs after Amazon ECS has completed the production traffic shift. The green service revision is now handling all production traffic. 

```

{
  "executionId": "5f40ed04-7e54-437d-b95d-98bc872fec49",
  "lifecycleStage": "POST_PRODUCTION_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {}
  }
}
        
```
 

## Lifecycle hooks during rollback 

There is no dedicated `ROLLBACK` lifecycle stage. When a rollback occurs, Amazon ECS re-invokes hooks registered at the `PRODUCTION_TRAFFIC_SHIFT` and `TEST_TRAFFIC_SHIFT` stages (the recurring invocation stages). During a rollback, the `productionTrafficWeights` in the payload show traffic shifting back to the blue revision. 

The `targetServiceRevisionArn` remains the green revision ARN because it is still the target of the original deployment, even though traffic is shifting away from it. 

The following example shows a `PRODUCTION_TRAFFIC_SHIFT` payload during a rollback. Notice that the blue revision (`1920498462936580504`) now receives 100% of production traffic, while the green revision (`9313423515462893900`) receives 0%: 

```

{
  "executionId": "70073435-cb99-457f-b900-6ee1dcad05ec",
  "lifecycleStage": "PRODUCTION_TRAFFIC_SHIFT",
  "resourceArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28",
  "executionDetails": {
    "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
    "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900",
    "testTrafficWeights": {},
    "productionTrafficWeights": {
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/9313423515462893900": 0,
      "arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1920498462936580504": 100
    }
  }
}
    
```
 

To determine whether your hook is being invoked during a rollback, check the `productionTrafficWeights`. If the `targetServiceRevisionArn` (green revision) has a weight of 0% and the other revision has 100%, the deployment is rolling back.
