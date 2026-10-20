
## ECS Native Linear and Canary Deployments

Two templates that use the newer Amazon ECS traffic-shifting strategies, available since October 2025. They work like [native blue/green](../ecs-blue-green/README.md): ECS starts the new (green) revision next to the current (blue) one and moves listener-rule weights between two target groups. The difference is **how** production traffic moves:

| Strategy | Traffic shift | CloudFormation |
|---|---|---|
| `BLUE_GREEN` | 0% → 100% in one step | [../ecs-blue-green/ecs-fargate-alb-blue-green.yaml](../ecs-blue-green/ecs-fargate-alb-blue-green.yaml) |
| `LINEAR` | Equal steps of `StepPercent`, `StepBakeTimeInMinutes` between steps | [ecs-fargate-alb-linear.yaml](ecs-fargate-alb-linear.yaml) |
| `CANARY` | `CanaryPercent` first, wait `CanaryBakeTimeInMinutes`, then the rest at once | [ecs-fargate-alb-canary.yaml](ecs-fargate-alb-canary.yaml) |

After 100%, all three wait `BakeTimeInMinutes` with blue still running, then stop blue. A CloudWatch alarm (`DeploymentConfiguration.Alarms`) can roll back at any point until then, moving the weights back to blue.

Offline docs: [../../docs/ecs/README.md](../../docs/ecs/README.md)

----------------------------------------------------------------------------------

## What's in the templates

```yaml
DeploymentController:
  Type: ECS
DeploymentConfiguration:
  Strategy: LINEAR                 # or CANARY
  LinearConfiguration:             # only with LINEAR
    StepPercent: 25                # 3.0-100.0, multiples of 0.1 (ECS default 10.0)
    StepBakeTimeInMinutes: 2       # 0-1440 (default 6); not applied after the last step
  # CanaryConfiguration:           # only with CANARY
  #   CanaryPercent: 10            # 0.1-100.0, multiples of 0.1 (ECS default 5.0)
  #   CanaryBakeTimeInMinutes: 5   # 0-1440 (default 10)
  BakeTimeInMinutes: 5             # after 100%, before blue stops (default 15)
  Alarms: { Enable: true, Rollback: true, AlarmNames: [ <5xx alarm> ] }
LoadBalancers:
  - TargetGroupArn: <primary>
    AdvancedConfiguration:         # same as BLUE_GREEN
      AlternateTargetGroupArn: <alternate>
      ProductionListenerRule: <rule forwarding to both target groups, weights 1 / 0>
      RoleArn: <role with AmazonECSInfrastructureRolePolicyForLoadBalancers>
```

Linear with `StepPercent: 25` shifts production 25% → 50% → 75% → 100%, with `StepBakeTimeInMinutes` after each step except the last. Canary with `CanaryPercent: 10` shifts 10% → 100%.

| Resource | Purpose |
|---|---|
| ALB + listener `:80` | Default action is a fixed 404. A catch-all `/*` **rule** carries the weighted forward, because ECS changes the rule, not the default action |
| `PrimaryTargetGroup` / `AlternateTargetGroup` | ECS alternates which one is production on every deployment |
| `LoadBalancerInfrastructureRole` | ECS assumes it to change rule weights and register targets |
| `LoadBalancerTarget5xxAlarm` | Rolls the deployment back when target 5XX ≥ 5 in a minute |

The test listener and Lambda / pause lifecycle hooks work the same as for blue/green, so they aren't repeated here; see [../ecs-blue-green/](../ecs-blue-green/README.md). For linear and canary, hooks at `PRE_PRODUCTION_TRAFFIC_SHIFT` and `PRODUCTION_TRAFFIC_SHIFT` run at **every** traffic-shift step.

----------------------------------------------------------------------------------

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-ecs-linear \
  --template-body file://ecs-fargate-alb-linear.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx \
               ParameterKey=VpcSubnetList,ParameterValue='subnet-aaaa\,subnet-bbbb'
```

(Use `ecs-fargate-alb-canary.yaml` and a different stack name for canary.)

## Trigger a deployment and watch the weights

```bash
aws cloudformation update-stack --stack-name myapp-dev-ecs-linear \
  --use-previous-template --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=ContainerImageName,ParameterValue=public.ecr.aws/docker/library/nginx:1.28 \
               ParameterKey=VpcId,UsePreviousValue=true ParameterKey=VpcSubnetList,UsePreviousValue=true

# rule weights move step by step
watch -n 10 "aws elbv2 describe-rules --listener-arn <listener-arn> \
  --query 'Rules[?Priority==\`1\`].Actions[0].ForwardConfig.TargetGroups[].Weight'"

# which nginx version answers (mix during the shift)
for i in $(seq 1 20); do curl -sI http://<lb-dns>/ | grep Server; done | sort | uniq -c
```

The stack update completes only when the ECS deployment finishes, including all steps and the bake time. With the defaults, linear takes about 3 steps × 2 min + 5 min, and canary about 5 min + 5 min, plus task start-up.

## Notes

- **33-hour limit:** CloudFormation rejects linear or canary deployments whose calculated time exceeds **33 hours** (its operations time out at 36 h). For linear that's `BakeTimeInMinutes + StepBakeTimeInMinutes × steps`, where steps is `100 / StepPercent − 1` if it divides evenly, otherwise the floor. For canary it's `BakeTimeInMinutes + CanaryBakeTimeInMinutes`. These templates cap the bake parameters at 60 minutes.
- **No circuit breaker:** `DeploymentCircuitBreaker` is rolling-only. Use alarms and hooks for rollback.
- **Capacity:** during a deployment, blue and green each run `TaskDesiredCount` tasks.
- **Rule weights:** after an even number of deployments production may be on `AlternateTargetGroup`. Don't edit the rule weights by hand.

## Docs

- [../../docs/ecs/ug-deployment-type-linear.md](../../docs/ecs/ug-deployment-type-linear.md)
- [../../docs/ecs/ug-canary-deployment.md](../../docs/ecs/ug-canary-deployment.md)
- [../../docs/ecs/cfn-aws-properties-ecs-service-linearconfiguration.md](../../docs/ecs/cfn-aws-properties-ecs-service-linearconfiguration.md)
- [../../docs/ecs/cfn-aws-properties-ecs-service-canaryconfiguration.md](../../docs/ecs/cfn-aws-properties-ecs-service-canaryconfiguration.md)
- [../../docs/ecs/ug-alb-resources-for-blue-green.md](../../docs/ecs/ug-alb-resources-for-blue-green.md) (ALB resources for blue/green, linear and canary)
