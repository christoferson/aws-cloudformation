> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-blue-green-service.html
> Downloaded: 2026-10-18

# Creating an Amazon ECS blue/green deployment

 By using Amazon ECS blue/green deployments, you can make and test service changes before implementing them in a production environment.  

## Prerequisites 

Perform the following operations before you start a blue/green deployment.   
Configure the appropriate permissions.  
For information about Elastic Load Balancing permissions, see Amazon ECS infrastructure IAM role for load balancers. 
If you're using VPC Lattice, for information about VPC Lattice permissions, see AmazonECSInfrastructureRolePolicyForVpcLattice. 
For information about Lambda permissions, see Permissions required for Lambda functions in Amazon ECS blue/green deployments 
(Optional) For managed traffic shifting, configure one of the following resources. If your service is headless (no load balancer, Service Connect, or VPC Lattice), you can skip this step. Amazon ECS doesn't manage the traffic shift automatically for headless services.  
Application Load Balancer - For more information, see Application Load Balancer resources for blue/green, linear, and canary deployments. 
Network Load Balancer - For more information, see Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments. 
Service Connect - For more information, see Service Connect resources for Amazon ECS blue/green, linear, and canary deployments. 
VPC Lattice - For more information, see VPC Lattice resources for blue/green, linear, and canary deployments. 
Decide if you want to run Lambda functions for the lifecycle stages.  
PRE_SCALE_UP 
POST_SCALE_UP 
TEST_TRAFFIC_SHIFT 
POST_TEST_TRAFFIC_SHIFT 
PRODUCTION_TRAFFIC_SHIFT 
POST_PRODUCTION_TRAFFIC_SHIFT 
 

For more information, see Create a Lambda function with the console in the AWS Lambda Developer Guide. 
 

## Procedure 

You can use the console or the AWS CLI to create an Amazon ECS blue/green service.  

**Console** 
Open the console at https://console.aws.amazon.com/ecs/v2.
Determine the resource from where you launch the service.  
|  To start a service from |  Steps |    
|   

Clusters  |    
On the Clusters page, select the cluster to create the service in. 

The cluster details page displays. 
On the Services tab, choose Create. 
  |   
|  Task definition |    
On the Task definitions page, select the task definition. 
From the Deploy menu, choose Create service. 
  |    

The Create service page displays. 
Under Service details, do the following: 
For Task definition family, choose the task definition to use. Then, for Task definition revision, enter the revision to use. 
For Service name, enter a name for your service. 
To run the service in an existing cluster, for Existing cluster, choose the cluster. To run the service in a new cluster, choose Create cluster  
Choose how your tasks are distributed across your cluster infrastructure. Under Compute configuration, choose your option.  
|  Compute option |  Steps |    
|   

Capacity provider strategy  |    
Under Compute options, choose Capacity provider strategy. 
Choose a strategy:  
To use the cluster's default capacity provider strategy, choose Use cluster default. 
If your cluster doesn't have a default capacity provider strategy, or to use a custom strategy, choose Use custom, Add capacity provider strategy, and then define your custom capacity provider strategy by specifying a Base, Capacity provider, and Weight. 
 
 Note

To use a capacity provider in a strategy, the capacity provider must be associated with the cluster.   |   
|  Launch type |    
In the Compute options section, select Launch type. 
For Launch type, choose a launch type. 
(Optional) When the Fargate is specified, for Platform version, specify the platform version to use. If a platform version isn't specified, the `LATEST` platform version is used. 
  |    
Under Deployment configuration, do the following: 
For Service type, choose Replica. 
For Desired tasks, enter the number of tasks to launch and maintain in the service. 
To have Amazon ECS monitor the distribution of tasks across Availability Zones, and redistribute them when there is an imbalance, under Availability Zone service rebalancing, select Availability Zone service rebalancing. 
For Health check grace period, enter the amount of time (in seconds) that the service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. 
For Bake time, enter the number of minutes that both the blue and green service revisions will run simultaneously before the blue revision is terminated. This allows time for verification and testing. 
(Optional) Configure lifecycle hooks to run at specific stages of the deployment. Under Deployment lifecycle hooks, choose Add. 

For Lambda hooks:  
For Target type, choose Lambda.
For Lambda function, enter the function name or ARN.
For Role, select the IAM role that has permission to invoke the Lambda function.
For Lifecycle stages, select the stages when the Lambda function should run.
 

For pause hooks:  
For Target type, choose Pause.
For Lifecycle stages, select the stages where the deployment should pause.
(Optional) For Timeout, configure the timeout duration and action.
To configure how Amazon ECS detects and handles deployment failures, expand Deployment failure detection, and then choose your options.  
To stop a deployment when the tasks cannot start, select Use the Amazon ECS deployment circuit breaker. 

To have the software automatically roll back the deployment to the last completed deployment state when the deployment circuit breaker sets the deployment to a failed state, select Rollback on failures. 
To stop a deployment based on application metrics, select Use CloudWatch alarm(s). Then, from CloudWatch alarm name, choose the alarms. To create a new alarm, go to the CloudWatch console. 

To have the software automatically roll back the deployment to the last completed deployment state when a CloudWatch alarm sets the deployment to a failed state, select Rollback on failures. 
(Optional) To interconnect your service using Service Connect, expand Service Connect, and then specify the following: 
 Select Turn on Service Connect. 
Under Service Connect configuration, specify the client mode.  
If your service runs a network client application that only needs to connect to other services in the namespace, choose Client side only. 
If your service runs a network or web service application and needs to provide endpoints for this service, and connects to other services in the namespace, choose Client and server. 
To use a namespace that is not the default cluster namespace, for Namespace, choose the service namespace. This can be a namespace created separately in the same AWS Region in your AWS account or a namespace in the same Region that is shared with your account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see Cross-account AWS Cloud Map namespace sharing in the AWS Cloud Map Developer Guide. 
(Optional) Configure test traffic header rules for blue/green deployments. Under Test traffic routing, specify the following: 
Select Enable test traffic header rules to route specific requests to the green service revision during testing. 
For Header matching rules, configure the criteria for routing test traffic:  
Header name: Enter the name of the HTTP header to match (for example, `X-Test-Version` or `User-Agent`). 
Match type: Choose the matching criteria:  
Exact match: Route requests where the header value exactly matches the specified value 
Header present: Route requests that contain the specified header, regardless of value 
Pattern match: Route requests where the header value matches a specified pattern 
Header value (if using exact match or pattern match): Enter the value or pattern to match against. 
 

You can add multiple header matching rules to create complex routing logic. Requests matching any of the configured rules will be routed to the green service revision for testing. 
Choose Add header rule to configure additional header matching conditions. 
 Note

Test traffic header rules enable you to validate new functionality with controlled traffic before completing the full deployment. This allows you to test the green service revision with specific requests (such as those from internal testing tools or beta users) while maintaining normal traffic flow to the blue service revision. 
(Optional) Specify a log configuration. Select Use log collection. The default option sends container logs to CloudWatch Logs. The other log driver options are configured using AWS FireLens. For more information, see Send Amazon ECS logs to an AWS service or AWS Partner. 

The following describes each container log destination in more detail.  
Amazon CloudWatch – Configure the task to send container logs to CloudWatch Logs. The default log driver options are provided, which create a CloudWatch log group on your behalf. To specify a different log group name, change the driver option values. 
Amazon Data Firehose – Configure the task to send container logs to Firehose. The default log driver options are provided, which send logs to a Firehose delivery stream. To specify a different delivery stream name, change the driver option values. 
Amazon Kinesis Data Streams – Configure the task to send container logs to Kinesis Data Streams. The default log driver options are provided, which send logs to an Kinesis Data Streams stream. To specify a different stream name, change the driver option values. 
Amazon OpenSearch Service – Configure the task to send container logs to an OpenSearch Service domain. The log driver options must be provided.  
Amazon S3 – Configure the task to send container logs to an Amazon S3 bucket. The default log driver options are set by default, but you must specify a valid Amazon S3 bucket name. 
(Optional) Configure Load balancing for blue/green deployment.  
|  Elastic Load Balancing type |  Steps |    
|   

Application Load Balancer  |    
For Load balancer type, choose Application Load Balancer. 
Choose Create a new load balancer to create a new Application Load Balancer or Use an existing load balancer to select an existing Application Load Balancer. 
For Container, choose the container that hosts the service. 
For Load balancer name, enter a unique name. 
For Listener, enter a port and protocol for the Application Load Balancer to listen for connection requests on. By default, the load balancer will be configured to use port 80 and HTTP.  
For Production rule, enter the Evaluation order and Path pattern for the rule. 

This rule is for your production service revision traffic. 
For Test rule, enter the Evaluation order and Path pattern for the rule. 

This rule is for your test service revision traffic. 
For Target group, configure the following:  
For Target group name, enter a name and a protocol for the target group that the Application Load Balancer routes requests to. 
For Protocol, choose the protocol for the target group that the Application Load Balancer routes requests to. By default, the target group routes requests to the first container defined in your task definition. 
For Deregistration delay, enter the number of seconds for the load balancer to change the target state to `UNUSED`. The default is 300 seconds. 
For Health check path, enter an existing path within your container where the Application Load Balancer periodically sends requests to verify the connection health between the Application Load Balancer and the container. The default is the root directory (`/`). 
For Alternate group name, enter the group name for the target group for your test (green) service revision. 
 
  |   
|  Network Load Balancer |    
For Load balancer type, select Network Load Balancer. 
For Load Balancer, choose an existing Network Load Balancer. 
For Choose container to load balance, choose the container that hosts the service. 
For Production listener, choose the Production listener port, and the Production listener protocol. 

This is the listener for your production service revision traffic. 
For Test listener, choose the Test listener port, and the Test listener protocol. 

This is the listener for your test service revision traffic. 
For Target group, configure the following:  
For Target group name, enter a name and a protocol for the target group that the Network Load Balancer routes requests to. 
For Protocol, choose the protocol for the target group that the Network Load Balancer routes requests to. By default, the target group routes requests to the first container defined in your task definition. 
For Deregistration delay, enter the number of seconds for the load balancer to change the target state to `UNUSED`. The default is 300 seconds. 
For Health check path, enter an existing path within your container where the Application Load Balancer periodically sends requests to verify the connection health between the Application Load Balancer and the container. The default is the root directory (`/`). 
For Alternate group name, enter the group name for the target group for your test (green) service revision. 
 
  |    
(Optional) To use VPC Lattice for managed traffic shifting during blue/green deployments, expand VPC Lattice - optional and select Use VPC Lattice, then do the following: 
For VPC, choose the VPC for your VPC Lattice resources. This must be the same VPC as your Fargate service. 
For Infrastructure role, choose the Amazon ECS infrastructure IAM role that Amazon ECS uses to manage your VPC Lattice resources, or choose Create a new infrastructure role. 
For Container port name, choose the port name from the task definition that maps to the container port that receives traffic from VPC Lattice. 
For VPC Lattice service, choose Create a new service or Use an existing service. For Service name, enter a unique name for the service. 
For Listener, choose Create new listener or Use an existing listener. For Port, enter a port from 1 to 65535. For Protocol, choose the protocol (for example, HTTP). 
Under Production listener rule, enter a Name, a Priority from 1 to 100, and a Path pattern (maximum 200 characters). Amazon ECS uses this rule to route production traffic. 
(Optional, recommended) Under Test listener rule, enter a Name, a Priority from 1 to 100, and a Path pattern. Amazon ECS uses this rule to route test traffic to the green service revision. 
For Target groups, choose Create two new target groups, Create green target group, or Use two existing target groups. For a new target group, enter a Target group name, choose a Protocol, enter a Port from 1 to 65535, choose a Health check protocol, and enter a Health check path. For Green target group name, enter a name; the green target group uses the same configuration as the blue target group. 
(Optional) To help identify your service and tasks, expand the Tags section, and then configure your tags. 

To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the task definition tags, select Turn on Amazon ECS managed tags, and then for Propagate tags from, choose Task definitions. 

To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the service tags, select Turn on Amazon ECS managed tags, and then for Propagate tags from, choose Service. 

Add or remove a tag.  
[Add a tag] Choose Add tag, and then do the following:  
For Key, enter the key name. 
For Value, enter the key value. 
[Remove a tag] Next to the tag, choose Remove tag. 
Choose Create. 
  

**AWS CLI** 
Create a file named `service-definition.json` with the following content. 

Replace the `user-input` with your values. 

```
{
  "serviceName": "myBlueGreenService",
  "cluster": "arn:aws:ecs:us-west-2:123456789012:cluster/sample-fargate-cluster",
  "taskDefinition": "sample-fargate:1",
  "desiredCount": 5,
  "launchType": "FARGATE",
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "subnets": [
        "subnet-09ce6e74c116a2299",
        "subnet-00bb3bd7a73526788",
        "subnet-0048a611aaec65477"
      ],
      "securityGroups": [
        "sg-09d45005497daa123"
      ],
      "assignPublicIp": "ENABLED"
    }
  },
  "deploymentController": {
    "type": "ECS"
  },
  "deploymentConfiguration": {
    "strategy": "BLUE_GREEN",
    "maximumPercent": 200,
    "minimumHealthyPercent": 100,
    "bakeTimeInMinutes": 2,
    "alarms": {
      "alarmNames": [
        "myAlarm"
      ],
      "rollback": true,
      "enable": true
    },
    "lifecycleHooks": [
      {
        "hookTargetArn": "arn:aws:lambda:us-west-2:7123456789012:function:checkExample",
        "roleArn": "arn:aws:iam::123456789012:role/ECSLifecycleHookInvoke",
        "lifecycleStages": [
          "PRE_SCALE_UP"
        ],
        "hookDetails": {
          "MY_CONFIG_KEY": "my-config-value"
        }
      }
    ]
  },
  "loadBalancers": [
    {
      "targetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/blue-target-group/54402ff563af1197",
      "containerName": "fargate-app",
      "containerPort": 80,
      "advancedConfiguration": {
        "alternateTargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/green-target-group/cad10a56f5843199",
        "productionListenerRule": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-blue-green-demo/32e0e4f946c3c05b/9cfa8c482e204f7d/831dbaf72edb911",
        "roleArn": "arn:aws:iam::123456789012:role/LoadBalancerManagementforECS"
      }
    }
  ]
}
```
Run `create-service`. 

Replace the `user-input` with your values. 

```
aws ecs create-service --cli-input-json file://service-definition.json
```
 

Alternatively, you can use the following example which creates a blue/green deployment service with a load balancer configuration: 

```
aws ecs create-service \
   --cluster "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster" \
   --service-name "blue-green-example-service" \
   --task-definition "nginxServer:1" \
   --launch-type "FARGATE" \
   --network-configuration "awsvpcConfiguration={subnets=[subnet-12345,subnet-67890,subnet-abcdef,subnet-fedcba],securityGroups=[sg-12345],assignPublicIp=ENABLED}" \
   --desired-count 3 \
   --deployment-controller "type=ECS" \
   --deployment-configuration "strategy=BLUE_GREEN,maximumPercent=200,minimumHealthyPercent=100,bakeTimeInMinutes=0" \
   --load-balancers "targetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/MyBGtg1/abcdef1234567890,containerName=nginx,containerPort=80,advancedConfiguration={alternateTargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/MyBGtg2/0987654321fedcba,productionListenerRule=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/MyLB/1234567890abcdef/1234567890abcdef,roleArn=arn:aws:iam::123456789012:role/ELBManagementRole}"
```
 

Alternatively, you can use the following example which creates a blue/green deployment service with a VPC Lattice configuration: 

```
aws ecs create-service \
   --cluster "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster" \
   --service-name "blue-green-example-service" \
   --task-definition "nginxServer:1" \
   --launch-type "FARGATE" \
   --network-configuration "awsvpcConfiguration={subnets=[subnet-12345,subnet-67890,subnet-abcdef,subnet-fedcba],securityGroups=[sg-12345],assignPublicIp=ENABLED}" \
   --desired-count 3 \
   --deployment-controller "type=ECS" \
   --deployment-configuration "strategy=BLUE_GREEN,maximumPercent=200,minimumHealthyPercent=100,bakeTimeInMinutes=0" \
   --vpc-lattice-configurations "portName=web,roleArn=arn:aws:iam::111122223333:role/ecs-vpc-lattice-role,targetGroupArn=arn:aws:vpc-lattice:us-west-2:111122223333:targetgroup/primary-target-group/abcdef123456,advancedConfiguration={alternateTargetGroupArn=arn:aws:vpc-lattice:us-west-2:111122223333:targetgroup/alternate-target-group/ghijkl789012,productionListenerRule=arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0123456789abcdef0/listener/listener-0123456789abcdef0/rule/rule-0123456789abcdef0,testListenerRule=arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0123456789abcdef0/listener/listener-0123456789abcdef0/rule/rule-abcdef01234567890}"
```
 
   

## Next steps  
Update the service to start the deployment. For more information, see Updating an Amazon ECS service.
Monitor the deployment process to ensure it follows the blue/green pattern:  
The green service revision is created and scaled up 
Test traffic is routed to the green revision (if configured) 
Production traffic is shifted to the green revision 
After the bake time, the blue revision is terminated
