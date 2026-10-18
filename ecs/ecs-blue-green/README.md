
## ECS Native Blue/Green Deployments

Templates for the **Amazon ECS blue/green deployment strategy**, where ECS itself runs the blue/green rollout.
This replaces the older CodeDeploy-driven ECS blue/green (`DeploymentController: CODE_DEPLOY`).

Offline AWS docs used to build these: [../docs/ecs/README.md](../../docs/ecs/README.md)

----------------------------------------------------------------------------------

## CodeDeploy blue/green vs ECS native blue/green

| | CodeDeploy blue/green (old) | ECS native blue/green (new) |
|---|---|---|
| Deployment controller | `CODE_DEPLOY` (or `EXTERNAL` + CFN `AWS::CodeDeployBlueGreen` transform) | **`ECS`** |
| Strategy | Set in the CodeDeploy deployment config | **`DeploymentConfiguration.Strategy: BLUE_GREEN`** (also `LINEAR`, `CANARY`) |
| Extra resources | CodeDeploy application + deployment group + `ecsCodeDeployRole` | **None.** You add an infrastructure role for load balancers |
| How to deploy | `codedeploy create-deployment` + AppSpec | **`ecs update-service`** (or a CFN stack update) |
| Underlying construct | Task sets (older) | **Service revisions + service deployments** |
| Target groups | Configured in the deployment group | `LoadBalancers[].TargetGroupArn` + `AdvancedConfiguration.AlternateTargetGroupArn` |
| Listener setup | Single default rule → one target group | **Rule forwarding to BOTH target groups, weights 1 / 0** |
| Traffic shift | CodeDeploy rewrites the listener | ECS flips the listener **rule** weights |
| Hooks | Defined in the AppSpec, which can change per deployment | `DeploymentConfiguration.LifecycleHooks`, defined on the service |
| Hook Lambda result | Lambda must call `PutLifecycleEventHookExecutionStatus` | **Lambda's return value** is the hook status |
| Hook can poll | No (one call, 1 h max) | **Yes**: return `IN_PROGRESS` and ECS calls it again |
| Manual approval | Wait time in the deployment group | **`PAUSE` hook** + `ecs continue-service-deployment` |
| Bake time | Original task set termination wait | `BakeTimeInMinutes` (default 15) |
| Alarm rollback | Deployment group alarms | `DeploymentConfiguration.Alarms` |

Source: [../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen.md](../../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen.md)

### Deployment lifecycle

```
RECONCILE_SERVICE        (only when more than 1 revision is ACTIVE)
PRE_SCALE_UP             blue = 100% prod, green not started
POST_SCALE_UP            green tasks healthy, no traffic yet
TEST_TRAFFIC_SHIFT       test listener rule  -> green          (Lambda hooks only)
POST_TEST_TRAFFIC_SHIFT  green = 100% test traffic             <- Lambda hook in this template
PRE_PRODUCTION_TRAFFIC_SHIFT                                   <- optional PAUSE hook in this template
PRODUCTION_TRAFFIC_SHIFT prod listener rule  -> green          (Lambda hooks only)
POST_PRODUCTION_TRAFFIC_SHIFT
  bake time (BakeTimeInMinutes): blue still running, alarm can still roll back
  blue tasks stopped -> deployment complete
```

- Lambda hooks return `SUCCEEDED`, `FAILED` (rolls back) or `IN_PROGRESS`. With `IN_PROGRESS`, ECS calls the hook again after `callBackDelay` (default 30s), and can pass `hookDetails` state along.
- Pause hooks aren't allowed at `TEST_TRAFFIC_SHIFT` or `PRODUCTION_TRAFFIC_SHIFT`, because those stages also run during rollback.
- Limits: up to 10 Lambda hooks and 10 pause hooks per service. Hook timeout `ROLLBACK` (default) or `CONTINUE`.

Source: [../docs/ecs/ug-deployment-lifecycle-hooks.md](../../docs/ecs/ug-deployment-lifecycle-hooks.md)

----------------------------------------------------------------------------------

## Templates

### ECS Fargate + ALB + Blue/Green (Lambda test hook, optional pause, alarm rollback)

[ecs-fargate-alb-blue-green.yaml](ecs-fargate-alb-blue-green.yaml)

A self-contained stack. You only need a VPC with two public subnets.

```
                     ┌─ :80   ProductionListener ── ProductionListenerRule (/*) ─┐  weights flipped by ECS
Internet ── ALB ─────┤                                                           ├─► PrimaryTargetGroup   (blue|green)
                     └─ :8080 TestListener ─────── TestListenerRule (/*) ────────┘   AlternateTargetGroup (green|blue)

ContainerService  DeploymentController: ECS
                  Strategy: BLUE_GREEN, BakeTimeInMinutes, Alarms (rollback)
                  LifecycleHooks: Lambda @ POST_TEST_TRAFFIC_SHIFT, [PAUSE @ PRE_PRODUCTION_TRAFFIC_SHIFT]
                  AdvancedConfiguration: AlternateTargetGroupArn, ProductionListenerRule, TestListenerRule, RoleArn
```

The key parts, which differ from a rolling-update ECS service:

```yaml
ProductionListenerRule:              # a rule, not the listener default action
  Type: AWS::ElasticLoadBalancingV2::ListenerRule
  Properties:
    Actions:
      - Type: forward
        ForwardConfig:
          TargetGroups:
            - { TargetGroupArn: !Ref PrimaryTargetGroup,   Weight: 1 }
            - { TargetGroupArn: !Ref AlternateTargetGroup, Weight: 0 }

ContainerService:
  Properties:
    DeploymentController:
      Type: ECS
    DeploymentConfiguration:
      Strategy: BLUE_GREEN
      BakeTimeInMinutes: 5
      Alarms: { Enable: true, Rollback: true, AlarmNames: [...] }
      LifecycleHooks:
        - TargetType: AWS_LAMBDA
          HookTargetArn: !GetAtt TestTrafficHookLambdaFunction.Arn
          RoleArn: !GetAtt DeploymentHookInvokeRole.Arn      # ecs.amazonaws.com -> lambda:InvokeFunction
          LifecycleStages: [POST_TEST_TRAFFIC_SHIFT]
    LoadBalancers:
      - TargetGroupArn: !Ref PrimaryTargetGroup
        AdvancedConfiguration:
          AlternateTargetGroupArn: !Ref AlternateTargetGroup
          ProductionListenerRule: !Ref ProductionListenerRule
          TestListenerRule: !Ref TestListenerRule
          RoleArn: !GetAtt LoadBalancerInfrastructureRole.Arn  # AmazonECSInfrastructureRolePolicyForLoadBalancers
```

IAM roles in this template:

| Role | Trusted by | Purpose |
|---|---|---|
| `ContainerTaskExecutionRole` | `ecs-tasks` | Pull the image, write logs |
| `LoadBalancerInfrastructureRole` | `ecs` | ECS changes listener rules and target groups. Replaces `ecsCodeDeployRole` |
| `DeploymentHookInvokeRole` | `ecs` | ECS invokes the Lambda hook (`lambda:InvokeFunction`) |
| `TestTrafficHookLambdaExecutionRole` | `lambda` | Hook writes its logs |

#### Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-ecs-bluegreen \
  --template-body file://ecs-fargate-alb-blue-green.yaml \
  --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx \
               ParameterKey=VpcSubnetList,ParameterValue='subnet-aaaa\,subnet-bbbb'

curl -sI http://<ProductionUrl>/ | grep Server      # Server: nginx/1.27.x
```

#### Trigger a blue/green deployment

Change the image and update the stack. The stack update waits until the ECS deployment finishes, including the bake time.

```bash
aws cloudformation update-stack --stack-name myapp-dev-ecs-bluegreen \
  --use-previous-template --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=ContainerImageName,ParameterValue=public.ecr.aws/docker/library/nginx:1.28 \
               ParameterKey=VpcId,UsePreviousValue=true ParameterKey=VpcSubnetList,UsePreviousValue=true
```

Watch it (in a second terminal):

```bash
# test listener serves green first, production stays on blue
watch -n 2 'curl -sI http://<lb-dns>:8080/ | grep Server; curl -sI http://<lb-dns>/ | grep Server'

aws ecs list-service-deployments --cluster myapp-dev --service myapp-dev-service
aws ecs describe-service-deployments --service-deployment-arns <arn> \
  --query "serviceDeployments[0].{status:status,stage:lifecycleStage,hooks:lifecycleHookDetails}"
```

Outside CloudFormation (for example from a CI pipeline), the trigger is just `aws ecs update-service --task-definition <new-revision>`. There's no CodeDeploy call.

#### Manual approval (pause hook)

Set `DeploymentPauseHookEnabled=true`. Each deployment then stops before the production shift, with hook status `AWAITING_ACTION`. ECS also emits an EventBridge `ECS Hook State Change` event.

```bash
HOOK=$(aws ecs describe-service-deployments --service-deployment-arns <arn> \
  --query "serviceDeployments[0].lifecycleHookDetails[?targetType=='PAUSE'].hookId" --output text)
aws ecs continue-service-deployment --hook-id $HOOK --action CONTINUE   # or ROLLBACK
```

If no one continues within 60 minutes, the deployment rolls back (`TimeoutConfiguration`).
> Enable the pause hook with a stack **update**, after the service exists. If it's on at create time, the initial deployment may wait for a continue, which blocks stack creation.

#### Test the rollback

- **Hook failure:** change the hook's `TEST_URL` to a path nginx doesn't serve (for example `http://<lb-dns>:8080/missing`, which returns 404), then deploy a new image. The hook returns `FAILED` after 5 attempts, ECS rolls back, and production never shifts.
- **Unhealthy green:** deploy an image that doesn't serve on the container port (for example `public.ecr.aws/docker/library/busybox`, which exits immediately). Green never becomes healthy, so the deployment fails and blue keeps production.
- **Alarm:** during the bake time, push target 5XX errors above the threshold (5 per minute). ECS flips the weights back to blue.

#### Delete

```bash
aws cloudformation delete-stack --stack-name myapp-dev-ecs-bluegreen
```

----------------------------------------------------------------------------------

## Migrating a CodeDeploy blue/green template

Based on the "reuse the same ELB resources" approach in [../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.md](../../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.md):

1. Remove the `AWS::CodeDeployBlueGreen` transform and the `AWS::CodeDeploy::BlueGreen` hook.
2. Remove `GreenTaskDefinition`, `GreenTaskSet`, `BlueTaskSet` and `PrimaryTaskSet`. Give the service `TaskDefinition`, `LaunchType` and `NetworkConfiguration` directly.
3. Change the listener (or rule) forward action to include **both** target groups with weights 1 / 0.
4. Set `DeploymentController.Type: ECS` and `DeploymentConfiguration.Strategy: BLUE_GREEN`, plus `BakeTimeInMinutes`.
5. Add `LoadBalancers[].AdvancedConfiguration` (alternate target group, production/test listener rule, role).
6. Add a role trusted by `ecs.amazonaws.com` with `AmazonECSInfrastructureRolePolicyForLoadBalancers`.
7. Rewrite AppSpec Lambda hooks so they **return** `hookStatus` instead of calling `PutLifecycleEventHookExecutionStatus`.
8. Delete the CodeDeploy application and deployment group. CI/CD calls `ecs update-service` instead of `codedeploy create-deployment`.

The other two approaches (a new service on the existing LB with a port swap, or a new LB behind Route 53 or CloudFront) are lower risk. They're described in [../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen.md](../../docs/ecs/ug-migrate-codedeploy-to-ecs-bluegreen.md).

----------------------------------------------------------------------------------

## Notes / Errors

##### `DeploymentCircuitBreaker` with BLUE_GREEN

AWS's migration example sets the circuit breaker alongside `BLUE_GREEN`. The CloudFormation reference says it only applies to rolling updates. This template uses `Alarms` and hooks for rollback instead.

##### Listener default action vs rule

`ProductionListenerRule` must be a **listener rule ARN** for an ALB. A listener ARN is only valid for an NLB. CloudFormation doesn't expose the default rule's ARN, so the template uses an explicit `/*` rule at priority 1. The listener's default action is a fixed 404.

##### Rule weights drift

ECS changes the rule weights on every deployment, so after an even number of deployments, production may be on `AlternateTargetGroup`. A later stack update that touches the rules resets the weights in the template. Avoid editing the listener rules while the service is in use.

##### cfn-lint `Additional properties are not allowed ('Strategy' | 'LifecycleHooks' | 'AdvancedConfiguration')`

Your cfn-lint's bundled schemas are out of date. Run `cfn-lint --update-specs`, or upgrade it.

##### Capacity

During a deployment, blue and green each run `TaskDesiredCount` tasks (2× capacity), so check your Fargate quotas.

----------------------------------------------------------------------------------

## Roadmap

- `ecs-fargate-alb-linear.yaml` / `ecs-fargate-alb-canary.yaml`: `Strategy: LINEAR | CANARY` with `LinearConfiguration` / `CanaryConfiguration`
- NLB variant (`ProductionListenerRule` = listener ARN)
- Private subnets + CloudFront VPC origin (Security Hub ECS.2)

## Resources

- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-codedeploy-to-ecs-bluegreen.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb-resources-for-blue-green.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-lifecycle-hooks.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentconfiguration.html
