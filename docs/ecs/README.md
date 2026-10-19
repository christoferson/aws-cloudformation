
## ECS - Local Documentation Snapshot

Offline copies of the AWS docs used to build the templates in [ecs/ecs-blue-green](../../ecs/ecs-blue-green/), converted from HTML to Markdown.
Downloaded 2026-10-18. Each file starts with its source URL. Check the live page if something looks off.

### Developer Guide — Blue/Green

| File | Topic |
|---|---|
| [ug-migrate-codedeploy-to-ecs-bluegreen.md](ug-migrate-codedeploy-to-ecs-bluegreen.md) | CodeDeploy vs ECS blue/green, three migration approaches |
| [ug-migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.md](ug-migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.md) | CloudFormation template before / after migration |
| [ug-migrate-code-deploy-to-ecs-blue-green.md](ug-migrate-code-deploy-to-ecs-blue-green.md) | Migration procedure (console / CLI) |
| [ug-blue-green-deployment-implementation.md](ug-blue-green-deployment-implementation.md) | Required resources + best practices |
| [ug-deploy-blue-green-service.md](ug-deploy-blue-green-service.md) | Create a blue/green service (console / CLI) |
| [ug-alb-resources-for-blue-green.md](ug-alb-resources-for-blue-green.md) | ALB target groups, listeners, rules |
| [ug-nlb-resources-for-blue-green.md](ug-nlb-resources-for-blue-green.md) | NLB resources |
| [ug-vpc-lattice-resources-for-blue-green.md](ug-vpc-lattice-resources-for-blue-green.md) | VPC Lattice resources |
| [ug-deployment-lifecycle-hooks.md](ug-deployment-lifecycle-hooks.md) | Lifecycle stages, Lambda vs pause hooks |
| [ug-lambda-lifecycle-hooks.md](ug-lambda-lifecycle-hooks.md) | Lambda hook payloads, `hookStatus`, `hookDetails` |
| [ug-pause-lifecycle-hooks.md](ug-pause-lifecycle-hooks.md) | Pause hooks, `continue-service-deployment` |
| [ug-blue-green-permissions.md](ug-blue-green-permissions.md) | Role for ECS to invoke Lambda hooks |
| [ug-amazon-ecs-infrastructure-role-policy-for-load-balancers.md](ug-amazon-ecs-infrastructure-role-policy-for-load-balancers.md) | Managed policy for the load balancer infrastructure role |
| [ug-deployment-alarm-failure.md](ug-deployment-alarm-failure.md) | CloudWatch alarm based rollback |
| [ug-deployment-type-bluegreen.md](ug-deployment-type-bluegreen.md) | Legacy CodeDeploy blue/green (for comparison) |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-ecs-service.md](cfn-aws-resource-ecs-service.md) | `AWS::ECS::Service` |
| [cfn-aws-properties-ecs-service-deploymentconfiguration.md](cfn-aws-properties-ecs-service-deploymentconfiguration.md) | DeploymentConfiguration (Strategy, BakeTimeInMinutes, LifecycleHooks) |
| [cfn-aws-properties-ecs-service-deploymentlifecyclehook.md](cfn-aws-properties-ecs-service-deploymentlifecyclehook.md) | DeploymentLifecycleHook |
| [cfn-aws-properties-ecs-service-hooktimeoutconfig.md](cfn-aws-properties-ecs-service-hooktimeoutconfig.md) | HookTimeoutConfig |
| [cfn-aws-properties-ecs-service-loadbalancer.md](cfn-aws-properties-ecs-service-loadbalancer.md) | LoadBalancer |
| [cfn-aws-properties-ecs-service-advancedconfiguration.md](cfn-aws-properties-ecs-service-advancedconfiguration.md) | AdvancedConfiguration (alternate TG, listener rules, role) |
| [cfn-aws-properties-ecs-service-deploymentcontroller.md](cfn-aws-properties-ecs-service-deploymentcontroller.md) | DeploymentController |
| [cfn-aws-properties-ecs-service-deploymentalarms.md](cfn-aws-properties-ecs-service-deploymentalarms.md) | DeploymentAlarms |
| [cfn-aws-properties-ecs-service-deploymentcircuitbreaker.md](cfn-aws-properties-ecs-service-deploymentcircuitbreaker.md) | DeploymentCircuitBreaker |
| [cfn-aws-resource-elasticloadbalancingv2-listenerrule.md](cfn-aws-resource-elasticloadbalancingv2-listenerrule.md) | `AWS::ElasticLoadBalancingV2::ListenerRule` |
