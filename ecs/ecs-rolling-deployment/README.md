
## ECS Rolling Deployment Controls

[ecs-fargate-alb-rolling-controls.yaml](ecs-fargate-alb-rolling-controls.yaml)

The classic rolling update (`Strategy: ROLLING`, tasks replaced in place behind one target group) with the newer controls added to `AWS::ECS::Service` and `AWS::ECS::TaskDefinition`:

| Feature | CloudFormation | What it does |
|---|---|---|
| Circuit breaker threshold | `DeploymentCircuitBreaker.ThresholdConfiguration` | How many task failures fail the deployment. `COUNT` (an exact number), or `BOUNDED_PERCENT` (default, 50) / `UNBOUNDED_PERCENT` × desired count |
| Circuit breaker reset | `DeploymentCircuitBreaker.ResetOnHealthyTask` | `true` (default): a healthy task resets the failure count. `false`: every failure counts |
| Early success | `DeploymentConfiguration.EarlySuccessCriteria` | Complete the deployment once `HealthyPercent` of desired tasks are healthy on the new revision |
| Old-task cleanup | `EarlySuccessCriteria.SourceServiceRevisionCleanup` | `BLOCKING`: stop old tasks, then complete. `DEFERRED`: complete, then stop old tasks in the background (for up to two weeks) |
| Alarm rollback + bake | `DeploymentConfiguration.Alarms` + `BakeTimeInMinutes` | Roll back if the alarm fires. Bake time only applies with alarm-based rollback |
| 20-second metrics | `Service.Monitoring.MetricConfigurations` | Service `CPUUtilization` / `MemoryUtilization` at 20 s instead of 60 s |
| AZ rebalancing | `Service.AvailabilityZoneRebalancing: ENABLED` | ECS moves tasks to restore an even spread across AZs |
| Container restart | `ContainerDefinitions[].RestartPolicy` | Restart a crashed container inside the running task, without replacing the task |

Offline docs: [../../docs/ecs/README.md](../../docs/ecs/README.md)

----------------------------------------------------------------------------------

## How the deployment completes

With the defaults (`TaskDesiredCount 4`, `MinimumHealthyPercent 50`, `MaximumPercent 200`, `HealthyPercent 75`, cleanup `DEFERRED`, bake 2 min):

```
 update stack (new image)
   ECS starts new tasks (up to 2x desired = 8 total)
   circuit breaker watches: 3 task failures (COUNT 3, no reset) -> FAILED -> roll back to last COMPLETED
   3 of 4 new tasks healthy (75% rounded up)  -> early success reached
   bake 2 min with the 5XX alarm watching     -> ALARM -> roll back
   deployment COMPLETED -> old tasks stopped in the background (DEFERRED)
   the 4th task launches through normal scaling
```

After early success, the circuit breaker and alarm rollback **no longer apply**.

Rules from the docs:
- **Rolling-only:** early success criteria and the circuit breaker only work with `ROLLING`. Linear, canary and blue/green use alarms and hooks instead.
- **Healthy percent:** `HealthyPercent` must be between `MinimumHealthyPercent` and 100. With the common `MinimumHealthyPercent: 100`, early success can't finish any sooner, which is why this template uses 50.
- **First task:** ECS launches at least one new task and waits for it to become healthy before it evaluates the healthy percent.
- **Timeout:** setting a bake time on a rolling deployment raises CloudFormation's handler timeout to 36 hours.

## Container restart policy

```yaml
RestartPolicy:
  Enabled: true             # off by default
  IgnoredExitCodes: [0]     # don't restart a clean exit (max 50 codes)
  RestartAttemptPeriod: 60  # must have run 60s first (60-1800, default 300); at most one restart per period
```

- **What restarts:** ECS restarts the container in the same task, so the task keeps its ENI, IP and target registration. Watch restart counts with the task metadata endpoint or Container Insights.
- **Fargate:** supported on Fargate, but not for Windows containers on Fargate.
- **EC2:** needs container agent 1.86.0+, and the agent itself must be running for restarts to happen.

## AZ rebalancing

Since September 5, 2025, ECS turns on AZ rebalancing for every eligible service, meaning one that has AZ spread as the first placement strategy or has no placement strategy.
- **Create:** when the value isn't set, a create defaults to `ENABLED`.
- **Update:** an update keeps the existing value. A service that never had a value is treated as `DISABLED`.
- **Why set it here:** the template sets it explicitly, so the setting is visible and survives updates.

----------------------------------------------------------------------------------

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-ecs-rolling \
  --template-body file://ecs-fargate-alb-rolling-controls.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx \
               ParameterKey=VpcSubnetList,ParameterValue='subnet-aaaa\,subnet-bbbb'
```

## Try it

- **Normal rollout:** update `ContainerImageName` to `...nginx:1.28`. The stack update finishes when 3 of 4 new tasks are healthy and the 2-minute bake passes. The old tasks stop afterwards.
- **Circuit breaker:** set `ContainerImageName` to an image that exits at start, such as `public.ecr.aws/docker/library/busybox`. After 3 failed tasks, the deployment is `FAILED` and ECS rolls back to the last completed deployment.
- **Watch it:**

  ```bash
  aws ecs list-service-deployments --cluster myapp-dev-rolling --service myapp-dev-rolling-service
  aws ecs describe-service-deployments --service-deployment-arns <arn> \
    --query "serviceDeployments[0].{status:status,reason:statusReason,circuitBreaker:deploymentCircuitBreaker}"
  ```

## Docs

- [../../docs/ecs/ug-deployment-type-ecs.md](../../docs/ecs/ug-deployment-type-ecs.md) (rolling deployments)
- [../../docs/ecs/ug-early-success-criteria.md](../../docs/ecs/ug-early-success-criteria.md)
- [../../docs/ecs/ug-deployment-circuit-breaker.md](../../docs/ecs/ug-deployment-circuit-breaker.md)
- [../../docs/ecs/ug-container-restart-policy.md](../../docs/ecs/ug-container-restart-policy.md)
- [../../docs/ecs/ug-service-rebalancing.md](../../docs/ecs/ug-service-rebalancing.md)
- [../../docs/ecs/cfn-aws-properties-ecs-service-deploymentearlysuccesscriteria.md](../../docs/ecs/cfn-aws-properties-ecs-service-deploymentearlysuccesscriteria.md), [../../docs/ecs/cfn-aws-properties-ecs-service-thresholdconfiguration.md](../../docs/ecs/cfn-aws-properties-ecs-service-thresholdconfiguration.md), [../../docs/ecs/cfn-aws-properties-ecs-service-monitoringconfiguration.md](../../docs/ecs/cfn-aws-properties-ecs-service-monitoringconfiguration.md), [../../docs/ecs/cfn-aws-properties-ecs-taskdefinition-restartpolicy.md](../../docs/ecs/cfn-aws-properties-ecs-taskdefinition-restartpolicy.md)
