> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html
> Downloaded: 2026-10-18

# CodeDeploy blue/green deployments for Amazon ECS

We recommend that you use the Amazon ECS blue/green deployment. For more information, see Creating an Amazon ECS blue/green deployment.

The blue/green deployment type uses the blue/green deployment model controlled by CodeDeploy. Use this deployment type to verify a new deployment of a service before sending production traffic to it. For more information, see What Is CodeDeploy in the AWS CodeDeploy User Guide.Validate the state of an Amazon ECS service before deployment

There are three ways traffic can shift during a blue/green deployment: 
Canary — Traffic is shifted in two increments. You can choose from predeﬁned canary options that specify the percentage of traﬃc shifted to your updated task set in the ﬁrst increment and the interval, in minutes, before the remaining traﬃc is shifted in the second increment. 
Linear — Traffic is shifted in equal increments with an equal number of minutes between each increment. You can choose from predeﬁned linear options that specify the percentage of traﬃc shifted in each increment and the number of minutes between each increment. 
All-at-once — All traffic is shifted from the original task set to the updated task set all at once. 

The following are components of CodeDeploy that Amazon ECS uses when a service uses the blue/green deployment type:  

**CodeDeploy application**  

A collection of CodeDeploy resources. This consists of one or more deployment groups.  

**CodeDeploy deployment group**  

The deployment settings. This consists of the following:  
Amazon ECS cluster and service 
Load balancer target group and listener information 
Deployment roll back strategy 
Traffic rerouting settings 
Original revision termination settings 
Deployment configuration 
CloudWatch alarms configuration that can be set up to stop deployments 
SNS or CloudWatch Events settings for notifications 
 

For more information, see Working with Deployment Groups in the AWS CodeDeploy User Guide.  

**CodeDeploy deployment configuration**  

Specifies how CodeDeploy routes production traffic to your replacement task set during a deployment. The following pre-defined linear and canary deployment configuration are available. You can also create custom defined linear and canary deployments as well. For more information, see Working with Deployment Configurations in the AWS CodeDeploy User Guide.  
CodeDeployDefault.ECSAllAtOnce: Shifts all traffic to the updated Amazon ECS container at once 
CodeDeployDefault.ECSLinear10PercentEvery1Minutes: Shifts 10 percent of traffic every minute until all traffic is shifted. 
CodeDeployDefault.ECSLinear10PercentEvery3Minutes: Shifts 10 percent of traffic every 3 minutes until all traffic is shifted. 
CodeDeployDefault.ECSCanary10Percent5Minutes: Shifts 10 percent of traffic in the first increment. The remaining 90 percent is deployed five minutes later. 
CodeDeployDefault.ECSCanary10Percent15Minutes: Shifts 10 percent of traffic in the first increment. The remaining 90 percent is deployed 15 minutes later. 
  

**Revision**  

A revision is the CodeDeploy application specification file (AppSpec file). In the AppSpec file, you specify the full ARN of the task definition and the container and port of your replacement task set where traffic is to be routed when a new deployment is created. The container name must be one of the container names referenced in your task definition. If the network configuration or platform version has been updated in the service definition, you must also specify those details in the AppSpec file. You can also specify the Lambda functions to run during the deployment lifecycle events. The Lambda functions allow you to run tests and return metrics during the deployment. For more information, see AppSpec File Reference in the AWS CodeDeploy User Guide.   

## Considerations 

Consider the following when using the blue/green deployment type:  
When an Amazon ECS service using the blue/green deployment type is initially created, an Amazon ECS task set is created. 
You must configure the service to use either an Application Load Balancer or Network Load Balancer. The following are the load balancer requirements:  
You must add a production listener to the load balancer, which is used to route production traffic. 
An optional test listener can be added to the load balancer, which is used to route test traffic. If you specify a test listener, CodeDeploy routes your test traffic to the replacement task set during a deployment. 
Both the production and test listeners must belong to the same load balancer. 
You must define a target group for the load balancer. The target group routes traffic to the original task set in a service through the production listener. 
When a Network Load Balancer is used, only the `CodeDeployDefault.ECSAllAtOnce` deployment configuration is supported. 
For services configured to use service auto scaling and the blue/green deployment type, auto scaling is not blocked during a deployment but the deployment may fail under some circumstances. The following describes this behavior in more detail.  
If a service is scaling and a deployment starts, the green task set is created and CodeDeploy will wait up to an hour for the green task set to reach steady state and won't shift any traffic until it does. 
If a service is in the process of a blue/green deployment and a scaling event occurs, traffic will continue to shift for 5 minutes. If the service doesn't reach steady state within 5 minutes, CodeDeploy will stop the deployment and mark it as failed. 
Tasks using Fargate or the `CODE_DEPLOY` deployment controller types don't support the `DAEMON` scheduling strategy. 
When you initially create a CodeDeploy application and deployment group, you must specify the following:  
You must define two target groups for the load balancer. One target group should be the initial target group defined for the load balancer when the Amazon ECS service was created. The second target group's only requirement is that it can't be associated with a different load balancer than the one the service uses. 
When you create a CodeDeploy deployment for an Amazon ECS service, CodeDeploy creates a replacement task set (or green task set) in the deployment. If you added a test listener to the load balancer, CodeDeploy routes your test traffic to the replacement task set. This is when you can run any validation tests. Then CodeDeploy reroutes the production traffic from the original task set to the replacement task set according to the traffic rerouting settings for the deployment group. 
 

## Required IAM permissions 

Blue/green deployments are made possible by a combination of the Amazon ECS and CodeDeploy APIs. Users must have the appropriate permissions for these services before they can use Amazon ECS blue/green deployments in the AWS Management Console or with the AWS CLI or SDKs.  

In addition to the standard IAM permissions for creating and updating services, Amazon ECS requires the following permissions. These permissions have been added to the `AmazonECS_FullAccess` IAM policy. For more information, see AmazonECS_FullAccess.  
`codedeploy:CreateApplication`
`codedeploy:CreateDeployment`
`codedeploy:CreateDeploymentGroup`
`codedeploy:GetApplication`
`codedeploy:GetDeployment`
`codedeploy:GetDeploymentGroup`
`codedeploy:ListApplications`
`codedeploy:ListDeploymentGroups`
`codedeploy:ListDeployments`
`codedeploy:StopDeployment`
`codedeploy:GetDeploymentTarget`
`codedeploy:ListDeploymentTargets`
`codedeploy:GetDeploymentConfig`
`codedeploy:GetApplicationRevision`
`codedeploy:RegisterApplicationRevision`
`codedeploy:BatchGetApplicationRevisions`
`codedeploy:BatchGetDeploymentGroups`
`codedeploy:BatchGetDeployments`
`codedeploy:BatchGetApplications`
`codedeploy:ListApplicationRevisions`
`codedeploy:ListDeploymentConfigs`
`codedeploy:ContinueDeployment`
`sns:ListTopics`
`cloudwatch:DescribeAlarms`
`lambda:ListFunctions`
 Note

In addition to the standard Amazon ECS permissions required to run tasks and services, users also require `iam:PassRole` permissions to use IAM roles for tasks. 

CodeDeploy needs permissions to call Amazon ECS APIs, modify your Elastic Load Balancing, invoke Lambda functions, and describe CloudWatch alarms, as well as permissions to modify your service's desired count on your behalf. Before creating an Amazon ECS service that uses the blue/green deployment type, you must create an IAM role (`ecsCodeDeployRole`). For more information, see Amazon ECS CodeDeploy IAM Role.
