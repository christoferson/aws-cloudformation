## ECS Cloudformation



### ECS - Fargate

Example that provisions an ECS Fargate Cluster with Application Load Balancer

[ecs-fargate](ecs-fargate.yaml)


### ECS - Fargate - Autoscaling Step Scaling

Example that provisions an ECS Fargate Cluster with Application Load Balancer + AutoScaling Step Scaling

[ecs-fargate-scale-step](ecs-fargate-scale-step.yaml)

### ECS - Fargate - Autoscaling Target Tracking

Example that provisions an ECS Fargate Cluster with Application Load Balancer + AutoScaling Target Tracking

[ecs-fargate-scale-targettrack](ecs-fargate-scale-targettrack.yaml)


-------------------------------------

### ECS - Fargate Cluster

Cluster Only

[ecs-fargate-cluster](ecs-fargate-cluster.yaml)

### ECS - Fargate Cluster Service

Cluster Service & Task

[ecs-fargate-cluster-service](ecs-fargate-cluster-service.yaml)



------------------------------------

### ECS - Fargate Cluster (Basic)

Provision a Cluster and Service. HTTP Only, No Custom Domain

[ecs-fargate-cluster](ecs-fargate-cluster/10-ecs-fargate-cluster.yaml)

[ecs-fargate-cluster-service](ecs-fargate-cluster/20-ecs-fargate-cluster-service.yaml)

-------------------------------------

### ECS - Native Blue/Green Deployment

Fargate + ALB using `DeploymentController: ECS` + `Strategy: BLUE_GREEN` (no CodeDeploy), with a Lambda test hook, optional pause hook and alarm rollback.

[ecs-blue-green/README.md](ecs-blue-green/README.md)

### ECS - Native Linear and Canary Deployments

Fargate + ALB using `Strategy: LINEAR` (equal traffic steps) and `Strategy: CANARY` (small slice, then the rest), with alarm rollback.

[ecs-linear-canary/README.md](ecs-linear-canary/README.md)

### ECS - Rolling Deployment Controls

Fargate + ALB rolling update with circuit breaker threshold / reset, early success criteria, alarm rollback with bake time, 20-second service metrics, AZ rebalancing and container restart policy.

[ecs-rolling-deployment/README.md](ecs-rolling-deployment/README.md)

### ECS - Gateway (managed shared ALB ingress)

ECS Gateway + cluster association + two Fargate services with gateway connectors. ECS provisions the shared ALB, HTTPS listener, certificates and an `https://<id>.ecs.<region>.on.aws` hostname per service.

[ecs-gateway/README.md](ecs-gateway/README.md)

-------------------------------------

## EC2

By default, your container instance launches into your default cluster. To launch into a non-default cluster, choose the Advanced Details list. Then, paste the following script into the User data field, replacing your_cluster_name with the name of your cluster. [link](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html)

```
#!/bin/bash
echo ECS_CLUSTER=your_cluster_name >> /etc/ecs/ecs.config
```

