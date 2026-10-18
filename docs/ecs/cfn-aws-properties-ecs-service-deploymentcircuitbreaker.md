> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentcircuitbreaker.html
> Downloaded: 2026-10-18

# AWS::ECS::Service DeploymentCircuitBreakerNote

The deployment circuit breaker can only be used for services using the rolling update (`ECS`) deployment type.

The deployment circuit breaker determines whether a service deployment will fail if the service can't reach a steady state. If it is turned on, a service deployment will transition to a failed state and stop launching new tasks. You can also configure Amazon ECS to roll back your service to the last completed deployment after a failure. For more information, see Rolling update in the Amazon Elastic Container Service Developer Guide.

For more information about API failure reasons, see API failure reasons in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Enable" : Boolean,
  "ResetOnHealthyTask" : Boolean,
  "Rollback" : Boolean,
  "ThresholdConfiguration" : ThresholdConfiguration
}

```

### YAML

```
  Enable: Boolean
  ResetOnHealthyTask: Boolean
  Rollback: Boolean
  ThresholdConfiguration: 
    ThresholdConfiguration

```

## Properties

**`Enable`** 

Determines whether to use the deployment circuit breaker logic for the service. 

Required: Yes

Type: Boolean

Update requires: No interruption

**`ResetOnHealthyTask`** 

Specifies whether the deployment circuit breaker resets its failure count when a task reaches a healthy state. When set to `true`, a task that reaches a healthy state resets the failure count to `0`. When set to `false`, Amazon ECS does not reset the failure count. The default is `true`. 

Required: No

Type: Boolean

Update requires: No interruption

**`Rollback`** 

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully. 

Required: Yes

Type: Boolean

Update requires: No interruption

**`ThresholdConfiguration`** 

The threshold configuration that controls when the deployment circuit breaker triggers. The `type` and `value` together determine how many task failures are tolerated before the circuit breaker activates. 

Required: No

Type: ThresholdConfiguration

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
