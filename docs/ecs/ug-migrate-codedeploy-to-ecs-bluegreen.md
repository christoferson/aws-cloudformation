> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-codedeploy-to-ecs-bluegreen.html
> Downloaded: 2026-10-18

# Migrate CodeDeploy blue/green deployments to Amazon ECS blue/green deployments

CodeDeploy blue/green and Amazon ECS blue/green deployments provide similar functionality, but they differ in how you configure and manage them. 

## CodeDeploy blue/green deployment overview 

When creating an Amazon ECS service using CodeDeploy, you:  
Create a load balancer with a production listener and (optionally) a test listener. Each listener is configured with a single (default) rule that routes all traffic to a single target group (the primary target group). 
Create an Amazon ECS service, configured to use the listener and target group, with `deploymentController` type set to `CODE_DEPLOY`. Service creation results in the creation of a (blue) task set registered with the specified target group. 
Create a CodeDeploy deployment group (as part of a CodeDeploy application), and configure it with details of the Amazon ECS cluster, service name, load balancer listeners, two target groups (the primary target group used in the production listener rule, and a secondary target group to be used for replacement tasks), a service role (to grant CodeDeploy permissions to manipulate Amazon ECS and Elastic Load Balancing resources) and various parameters that control the deployment behavior. 
 

With CodeDeploy, new versions of a service are deployed using `CreateDeployment()`, specifying the CodeDeploy application name, deployment group name, and an AppSpec file which provides details of the new revision and optional lifecycle hooks. The CodeDeploy deployment creates a replacement (green) task set and registers its tasks with the secondary target group. When this becomes healthy, it is available for testing (optional) and for production. In both cases, re-routing is achieved by changing the respective listener rule to point at the secondary target group associated with the green task set. Rollback is achieved by changing the production listener rule back to the primary target group. 

## Amazon ECS blue/green deployment overview 

With Amazon ECS blue/green deployments, The deployment configuration is part of the Amazon ECS service itself:  
You must pre-configure the load balancer production listener with a rule that includes two target groups with weights of 1 and 0. 
You need to specify the following resources, or update the service resources:   
The ARN of this listener rule  
The two target groups 
An IAM role to grant Amazon ECS permission to call the Elastic Load Balancing APIs 
An optional IAM role to run Lambda functions 
Set `deploymentController` type to `ECS` and `deploymentConfiguration.strategy` to `BLUE_GREEN`. This results in the creation of a (blue) service deployment whose tasks are registered with the primary target group. 
 
 

With Amazon ECS blue/green, a new service revision is created by calling Amazon ECS `UpdateService()`, passing details of the new revision. The service deployment creates new (green) service revision tasks and registers them with the secondary target group. Amazon ECS handles re-routing and rollback operations by switching the weights on the listener rule. 

## Key implementation differences 

While both approaches result in the creation of an initial set of tasks, the underlying implementation differs:  
CodeDeploy uses a task set, whereas Amazon ECS uses a service revision. Amazon ECS task sets are an older construct which have been superseded by Amazon ECS service revisions and deployments. The latter offer greater visibility into the deployment process, as well as the service deployment and service revision history. 
With CodeDeploy, lifecycle hooks are specified as part of the AppSpec file that is supplied to `CreateDeployment()`. This means that the hooks can be changed from one deployment to the next. With Amazon ECS blue/green, the hooks are specified as part of the service configuration, and any updates would require an `UpdateService()` call. 
Both CodeDeploy and Amazon ECS blue/green use Lambda for hook implementation, but the expected inputs and outputs differ. 

With CodeDeploy, the function must call `PutLifecycleEventHookExecutionStatus()` to return the hook status, which can either be `SUCCEEDED` or `FAILED`. With Amazon ECS, the Lambda response is used to indicate the hook status. 
CodeDeploy invokes each hook as a one-off call, and expects a final execution status to be returned within one hour. Amazon ECS hooks are more flexible in that they can return an `IN_PROGRESS` indicator, which signals that the hook must be re-invoked repeatedly until it results in `SUCCEEDED` or `FAILED`. For more information, see Lifecycle hooks for Amazon ECS service deployments. 
 

## Migration approaches 

There are three main approaches to migrating from CodeDeploy blue/green to Amazon ECS blue/green deployments. Each approach has different characteristics in terms of complexity, risk, rollback capability, and potential downtime. 

### Reuse the same Elastic Load Balancing resources used for CodeDeploy 

You update the existing Amazon ECS service to use the Amazon ECS deployment controller with blue/green deployment strategy instead of CodeDeploy deployment controller. Consider the following when using this approach:  
The migration procedure is simpler because you are updating the existing Amazon ECS service deployment controller and deployment strategy. 
There is no downtime when correctly configured and migrated. 
A rollback requires that you revert the service revision. 
The risk is high because there is no parallel blue/green configuration. 
 

You use the same load balancer listener and target groups that are used for CodeDeploy. If you are using CloudFormation, see Migrating an CloudFormation CodeDeploy blue/green deployment template to an Amazon ECS blue/green CloudFormation template. 
Modify the default rule of the production/test listeners to include the alternate target group and set the weight of the primary target group to 1 and the alternate target group to 0. 

For CodeDeploy, the listeners of the load balancer attached to the service are configured with a single (default) rule that routes all traffic to a single target group. For Amazon ECS blue/green, the load balancer listeners must be pre-configured with a rule that includes the two target groups with weights. The primary target group must be weighted to 1 and the alternate target group must be weighted to 0. 
Update the existing Amazon ECS service by calling the `UpdateService` API and setting the parameter `deploymentController` to `ECS`, and the parameter `deploymentStrategy` to `BLUE_GREEN`. Specify the ARNs of the target group, the alternative target group, the production listener, and an optional test listener. 
Verify that the service works as expected. 
Delete the CodeDeploy setup for this Amazon ECS service as you are now using Amazon ECS blue/green. 
 

### New service with existing load balancer 

This approach uses the blue/green strategy for the migration. 

Consider the following when using this approach:  
There is minimal disruption. It occurs only during the Elastic Load Balancing port swap. 
A rollback requires that you revert the Elastic Load Balancing port swap. 
The risk is low because there are parallel configurations. Therefore you can test before the traffic shift. 
Leave the listeners, the target groups, and the Amazon ECS service for the CodeDeploy setup intact so you can easily rollback to this setup if needed. 
Create new target groups and new listeners (with different ports from the original listeners) under the existing load balancer. Then, create a new Amazon ECS service that matches the existing Amazon ECS service except that you use `ECS` as deployment controller, `BLUE_GREEN` as a deployment strategy, and pass the ARNs for the new target groups and the new listeners rules. 
Verify the new setup by manually sending HTTP traffic to the service. If everything goes well, swap the ports of the original listeners and the new listeners to route the traffic to the new setup. 
Verify the new setup, and if everything continues to work as expected, delete the CodeDeploy setup. 
 

### New service with a new load balancer 

Like the previous approach, this approach uses the blue/green strategy for the migration. The key difference is that the switch from the CodeDeploy setup to the Amazon ECS blue/green setup happens at a reverse proxy layer above the load balancer. Sample implementations for the reverse proxy layer are Route 53 and CloudFront. 

This approach is suitable for customers who already have this reverse proxy layer, and if all the communication with the service is happening through it (for example, no direct communication at the load balancer level). 

Consider the following when using this approach:  
This requires a reverse proxy layer. 
The migration procedure is more complex because you need to update the existing Amazon ECS service deployment controller and deployment strategy. 
There is minimal disruption. It occurs only during the Elastic Load Balancing port swap. 
A rollback requires that you reverse the proxy configuration changes. 
The risk is low because there are parallel configurations. Therefore you can test before the traffic shift. 
Do not modify the existing CodeDeploy setup intact (load balancer, listeners, target groups, Amazon ECS service, and CodeDeploy deployment group). 
Create a new load balancer, target groups, and listeners configured for Amazon ECS blue/green deployments. 

Configure the appropriate resources.  
Application Load Balancer - For more information, see Application Load Balancer resources for blue/green, linear, and canary deployments. 
Network Load Balancer - For more information, see Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments. 
VPC Lattice - For more information, see VPC Lattice resources for blue/green, linear, and canary deployments. 
Create a new service with `ECS` as deployment controller and `BLUE_GREEN` as deployment strategy, pointing to the new load balancer resources. 
Verify the new setup by testing it through the new load balancer. 
Update the reverse proxy configuration to route traffic to the new load balancer. 
Observe the new service revision, and if everything continues to work as expected, delete the CodeDeploy setup. 
 

## Next steps 

After migrating to Amazon ECS blue/green deployments:  
Update your deployment scripts and CI/CD pipelines to use the Amazon ECS `UpdateService` API instead of the CodeDeploy `CreateDeployment` API. 
Update your monitoring and alerting to track Amazon ECS service deployments instead of CodeDeploy deployments. 
Consider implementing automated testing of your new deployment process to ensure it works as expected.
