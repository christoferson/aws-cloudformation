## CodeDeploy Cloudformation Templates




LoadBalancer
For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.






#### Errors

- For ECS deployment group, loadBalancerInfo must be specified (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidLoadBalancerInfoException; Request ID: xxx)

- 	For ECS deployment group, blueGreenDeploymentConfiguration must be specified (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidBlueGreenDeploymentConfigurationException; Request ID: zzz; Proxy: null)

- Could not load ECS service information for cluster: ecsdev-cluster, service: ecsdev-service. Cause: User: arn:aws:sts::xxx:assumed-role/code-codedeploy-ecs-CodeDeployServiceRole-yyy/xxx is not authorized to perform: ecs:DescribeServices