## CodeDeploy Cloudformation Templates


https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html

LoadBalancer
For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.


### CodeDeploy - EC2

[code-codedeploy](code-codedeploy.yaml)




#### Errors

- For ECS deployment, the deployment type must be BLUE_GREEN, and deployment option must be WITH_TRAFFIC_CONTROL. (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidDeploymentStyleException; Request ID: yyy; Proxy: null)

- For ECS deployment group, loadBalancerInfo must be specified (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidLoadBalancerInfoException; Request ID: xxx)

- 	For ECS deployment group, blueGreenDeploymentConfiguration must be specified (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidBlueGreenDeploymentConfigurationException; Request ID: zzz; Proxy: null)

- Could not load ECS service information for cluster: ecsdev-cluster, service: ecsdev-service. Cause: User: arn:aws:sts::xxx:assumed-role/code-codedeploy-ecs-CodeDeployServiceRole-yyy/xxx is not authorized to perform: ecs:DescribeServices

- Deployment group's ECS service must be configured for a CODE_DEPLOY deployment controller. 

- For ECS deployment group, loadBalancerInfo must not contain elbInfo list (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidLoadBalancerInfoException; Request ID: xxx; Proxy: null)

- For ECS deployment group, loadBalancerInfo must not contain targetGroupInfo list (Service: AmazonCodeDeploy; Status Code: 400; Error Code: InvalidLoadBalancerInfoException; Request ID: xxx; Proxy: null)
  https://repost.aws/questions/QU4L0zR3OYTwSEKKfMUrX6YA/questions/QU4L0zR3OYTwSEKKfMUrX6YA/can-t-create-ecs-deployment-group-using-cloudformation-loadbalancerinfo-error?
