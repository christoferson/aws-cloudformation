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

[ecs-fargate-cluster](ecs-fargate-cluster/01-ecs-fargate-cluster.yaml)

[ecs-fargate-cluster-service](ecs-fargate-cluster/02-ecs-fargate-cluster-service.yaml)

-------------------------------------

## EC2

By default, your container instance launches into your default cluster. To launch into a non-default cluster, choose the Advanced Details list. Then, paste the following script into the User data field, replacing your_cluster_name with the name of your cluster. [link](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html)

```
#!/bin/bash
echo ECS_CLUSTER=your_cluster_name >> /etc/ecs/ecs.config
```

