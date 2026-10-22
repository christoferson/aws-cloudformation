
## ECS - Local Documentation Snapshot

Offline copies of the AWS docs used to build the templates in [ecs/ecs-blue-green](../../ecs/ecs-blue-green/), [ecs/ecs-linear-canary](../../ecs/ecs-linear-canary/), [ecs/ecs-rolling-deployment](../../ecs/ecs-rolling-deployment/) and [ecs/ecs-gateway](../../ecs/ecs-gateway/), converted from HTML to Markdown.
Downloaded 2026-10-18 (blue/green) and 2026-10-20 (everything else). Each file starts with its source URL. Check the live page if something looks off.

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

### Developer Guide — What's new

| File | Topic |
|---|---|
| [ug-document-history.md](ug-document-history.md) | ECS document history: dated list of feature launches (used to pick what's new) |

### Developer Guide — Deployments and resilience

| File | Topic |
|---|---|
| [ug-deployment-type-linear.md](ug-deployment-type-linear.md) | Linear deployments: step percent, step bake time, lifecycle stages |
| [ug-canary-deployment.md](ug-canary-deployment.md) | Canary deployments: canary percent, canary bake time, lifecycle stages |
| [ug-service-connect-blue-green.md](ug-service-connect-blue-green.md) | Service Connect resources for blue/green, linear and canary |
| [ug-deployment-type-ecs.md](ug-deployment-type-ecs.md) | Rolling deployments (task replacement), minimum healthy / maximum percent |
| [ug-early-success-criteria.md](ug-early-success-criteria.md) | Early success criteria: healthy percent, BLOCKING / DEFERRED cleanup |
| [ug-deployment-circuit-breaker.md](ug-deployment-circuit-breaker.md) | Circuit breaker: threshold, resetOnHealthyTask, rollback |
| [ug-container-restart-policy.md](ug-container-restart-policy.md) | Container restart policies |
| [ug-service-rebalancing.md](ug-service-rebalancing.md) | Availability Zone rebalancing (on by default since 2025-09-05) |

### Developer Guide — ECS Gateway

Used by [ecs/ecs-gateway](../../ecs/ecs-gateway/). Downloaded 2026-10-21.

| File | Topic |
|---|---|
| [ug-gateway-overview.md](ug-gateway-overview.md) | Concepts (gateway, association, connector, route), shared vs service-specific infrastructure, quotas, constraints |
| [ug-gateway-managing.md](ug-gateway-managing.md) | Infrastructure role, create / update / delete a gateway, inbound security group, WAF, access logs, MaxAlbCount, associations |
| [ug-gateway-connect-service.md](ug-gateway-connect-service.md) | Gateway connector, access type filters, health checks, test traffic, service URL, disconnect |
| [ug-gateway-troubleshooting.md](ug-gateway-troubleshooting.md) | Connection, provisioning and update failures |

| File | Type |
|---|---|
| [cfn-aws-resource-ecs-gateway.md](cfn-aws-resource-ecs-gateway.md) | `AWS::ECS::Gateway` |
| [cfn-aws-properties-ecs-gateway-gatewayconfiguration.md](cfn-aws-properties-ecs-gateway-gatewayconfiguration.md) | GatewayConfiguration |
| [cfn-aws-properties-ecs-gateway-hostsharedalbconfiguration.md](cfn-aws-properties-ecs-gateway-hostsharedalbconfiguration.md) | HostSharedAlbConfiguration |
| [cfn-aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.md](cfn-aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.md) | GatewayElbNetworkConfiguration |
| [cfn-aws-properties-ecs-gateway-gatewayalbtesttrafficrules.md](cfn-aws-properties-ecs-gateway-gatewayalbtesttrafficrules.md) | GatewayAlbTestTrafficRules |
| [cfn-aws-properties-ecs-gateway-gatewaytesttrafficheader.md](cfn-aws-properties-ecs-gateway-gatewaytesttrafficheader.md) | GatewayTestTrafficHeader |
| [cfn-aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.md](cfn-aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.md) | GatewayElbAccessLogConfiguration |
| [cfn-aws-properties-ecs-gateway-gatewayelbaccesslogdestination.md](cfn-aws-properties-ecs-gateway-gatewayelbaccesslogdestination.md) | GatewayElbAccessLogDestination |
| [cfn-aws-properties-ecs-gateway-gatewayelbaccesslogs3destination.md](cfn-aws-properties-ecs-gateway-gatewayelbaccesslogs3destination.md) | GatewayElbAccessLogS3Destination |
| [cfn-aws-properties-ecs-gateway-tag.md](cfn-aws-properties-ecs-gateway-tag.md) | Tag |
| [cfn-aws-resource-ecs-gatewayclusterassociations.md](cfn-aws-resource-ecs-gatewayclusterassociations.md) | `AWS::ECS::GatewayClusterAssociations` |
| [cfn-aws-properties-ecs-service-gatewayconnector.md](cfn-aws-properties-ecs-service-gatewayconnector.md) | Service GatewayConnector |
| [cfn-aws-properties-ecs-service-gatewayconnectorfilters.md](cfn-aws-properties-ecs-service-gatewayconnectorfilters.md) | GatewayConnectorFilters (AccessTypes) |
| [cfn-aws-properties-ecs-service-gatewayconnectorhealthcheck.md](cfn-aws-properties-ecs-service-gatewayconnectorhealthcheck.md) | GatewayConnectorHealthCheck |
| [cfn-aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.md](cfn-aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.md) | GatewayConnectorHealthCheckMatcher |

### Developer Guide — Other features reviewed (no template yet)

| File | Topic |
|---|---|
| [ug-managed-daemons.md](ug-managed-daemons.md) | Managed Daemons on ECS Managed Instances |
| [ug-managed-daemons-task-definitions.md](ug-managed-daemons-task-definitions.md) | Daemon task definitions (`daemon_bridge` network, host bind mounts, privileged) |
| [ug-managed-daemons-create-manage.md](ug-managed-daemons-create-manage.md) | Creating and managing daemons |
| [ug-ebs-volumes.md](ug-ebs-volumes.md) | Service-managed EBS volumes |
| [ug-fault-injection.md](ug-fault-injection.md) | Fault injection (`enableFaultInjection`) |
| [ug-service-connect-tls.md](ug-service-connect-tls.md) | Service Connect TLS |

### CloudFormation Template Reference — all `AWS::ECS::*` resources

| File | Resource |
|---|---|
| [cfn-aws-resource-ecs-cluster.md](cfn-aws-resource-ecs-cluster.md) | `AWS::ECS::Cluster` |
| [cfn-aws-resource-ecs-capacityprovider.md](cfn-aws-resource-ecs-capacityprovider.md) | `AWS::ECS::CapacityProvider` (Auto Scaling group and Managed Instances providers) |
| [cfn-aws-resource-ecs-clustercapacityproviderassociations.md](cfn-aws-resource-ecs-clustercapacityproviderassociations.md) | `AWS::ECS::ClusterCapacityProviderAssociations` |
| [cfn-aws-resource-ecs-taskdefinition.md](cfn-aws-resource-ecs-taskdefinition.md) | `AWS::ECS::TaskDefinition` |
| [cfn-aws-resource-ecs-service.md](cfn-aws-resource-ecs-service.md) | `AWS::ECS::Service` |
| [cfn-aws-resource-ecs-taskset.md](cfn-aws-resource-ecs-taskset.md) | `AWS::ECS::TaskSet` |
| [cfn-aws-resource-ecs-primarytaskset.md](cfn-aws-resource-ecs-primarytaskset.md) | `AWS::ECS::PrimaryTaskSet` |
| [cfn-aws-resource-ecs-expressgatewayservice.md](cfn-aws-resource-ecs-expressgatewayservice.md) | `AWS::ECS::ExpressGatewayService` |
| [cfn-aws-resource-ecs-daemontaskdefinition.md](cfn-aws-resource-ecs-daemontaskdefinition.md) | `AWS::ECS::DaemonTaskDefinition` |
| [cfn-aws-resource-ecs-daemon.md](cfn-aws-resource-ecs-daemon.md) | `AWS::ECS::Daemon` |

Every property type of these resources is saved too, as `cfn-aws-properties-ecs-<resource>-<propertytype>.md`, 149 pages in all. The ones used by the new templates:

| File | Property type |
|---|---|
| [cfn-aws-properties-ecs-service-linearconfiguration.md](cfn-aws-properties-ecs-service-linearconfiguration.md) | LinearConfiguration |
| [cfn-aws-properties-ecs-service-canaryconfiguration.md](cfn-aws-properties-ecs-service-canaryconfiguration.md) | CanaryConfiguration |
| [cfn-aws-properties-ecs-service-deploymentearlysuccesscriteria.md](cfn-aws-properties-ecs-service-deploymentearlysuccesscriteria.md) | DeploymentEarlySuccessCriteria |
| [cfn-aws-properties-ecs-service-thresholdconfiguration.md](cfn-aws-properties-ecs-service-thresholdconfiguration.md) | ThresholdConfiguration (circuit breaker) |
| [cfn-aws-properties-ecs-service-monitoringconfiguration.md](cfn-aws-properties-ecs-service-monitoringconfiguration.md) | MonitoringConfiguration |
| [cfn-aws-properties-ecs-service-metricconfiguration.md](cfn-aws-properties-ecs-service-metricconfiguration.md) | MetricConfiguration |
| [cfn-aws-properties-ecs-taskdefinition-restartpolicy.md](cfn-aws-properties-ecs-taskdefinition-restartpolicy.md) | RestartPolicy |
