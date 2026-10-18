> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-lifecycle-hooks.html
> Downloaded: 2026-10-18

# Lifecycle hooks for Amazon ECS service deployments

When a deployment starts, it progresses through lifecycle stages. Each stage can be in a state such as `IN_PROGRESS` or `SUCCEEDED`. You can configure lifecycle hooks at specific stages to run custom logic or introduce decision points before the deployment proceeds. Amazon ECS supports two types of lifecycle hooks:  

**Lambda hooks**  

Amazon ECS invokes a Lambda function at specific stages of a deployment. Your function contains your custom logic and must return a JSON object containing a `hookStatus` of `SUCCEEDED`, `FAILED`, or `IN_PROGRESS` to tell Amazon ECS how to proceed. You can use these hooks to run validation tests, enforce governance policies, or implement custom approval steps before the deployment proceeds. For more information, see Lambda hooks for Amazon ECS service deployments.  

**Pause hooks**  

Amazon ECS pauses the deployment at a configured lifecycle stage and waits for you to call the `ContinueServiceDeployment` API to continue or roll back. While paused, you can run your own workflows externally, such as manual approvals, integration tests with existing tools, operational readiness checks, or CI/CD pipeline steps. For more information, see Pause hooks for Amazon ECS service deployments.  

You can configure both Lambda hooks and pause hooks at the same lifecycle stage. Both hooks must complete before the deployment proceeds to the next stage. 

## Lifecycle hook details 

When hooks are active during a deployment, you can view their status by calling `DescribeServiceDeployments`. The response includes a `lifecycleHookDetails` array with the following fields for each active hook:  
|  Field |  Description |    
|  `hookId` |  The unique identifier for this hook execution. Use this value when calling `ContinueServiceDeployment` for pause hooks. |   
|  `targetType` |  The hook type: `AWS_LAMBDA` or `PAUSE`. |   
|  `targetArn` |  The ARN of the hook target. For Lambda hooks, this is the Lambda function ARN. For pause hooks, this field is not set. |   
|  `status` |  The current status of the hook: `AWAITING_ACTION`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, or `TIMED_OUT`. |   
|  `expiresAt` |  The date and time when the hook expires. (Example: 2026-05-06T12:06:49-07:00) |   
|  `timeoutAction` |  The action Amazon ECS takes when the hook times out: `ROLLBACK` or `CONTINUE`. |    

## Lifecycle stage categories 

Lifecycle stages fall into two categories:  
Single invocation stages - Amazon ECS invokes these stages only once during a service deployment:  
`RECONCILE_SERVICE`
`PRE_SCALE_UP`
`POST_SCALE_UP`
`TEST_TRAFFIC_SHIFT`
`POST_TEST_TRAFFIC_SHIFT`
`POST_PRODUCTION_TRAFFIC_SHIFT`
Recurring invocation stages - Amazon ECS can invoke these stages multiple times during a service deployment. For linear and canary deployments, these stages are invoked at each traffic shift step:  
`PRE_PRODUCTION_TRAFFIC_SHIFT`
`PRODUCTION_TRAFFIC_SHIFT`
 
 Note

Pause hooks cannot be configured at `TEST_TRAFFIC_SHIFT` or `PRODUCTION_TRAFFIC_SHIFT` because these stages are also invoked during rollback. Pausing during a rollback would require an additional `ContinueServiceDeployment` call to complete the rollback. 

## Supported stages by hook type  
|  Lifecycle stage |  Lambda hooks |  Pause hooks |    
|  `RECONCILE_SERVICE` |  Yes |  Yes |   
|  `PRE_SCALE_UP` |  Yes |  Yes |   
|  `POST_SCALE_UP` |  Yes |  Yes |   
|  `TEST_TRAFFIC_SHIFT` |  Yes |  No |   
|  `POST_TEST_TRAFFIC_SHIFT` |  Yes |  Yes |   
|  `PRE_PRODUCTION_TRAFFIC_SHIFT` |  Yes |  Yes |   
|  `PRODUCTION_TRAFFIC_SHIFT` |  Yes |  No |   
|  `POST_PRODUCTION_TRAFFIC_SHIFT` |  Yes |  Yes |
