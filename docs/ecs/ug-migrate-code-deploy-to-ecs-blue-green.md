> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-code-deploy-to-ecs-blue-green.html
> Downloaded: 2026-10-18

# Migrating from a CodeDeploy blue/green to an Amazon ECS blue/green service deployment

 By using Amazon ECS blue/green deployments, you can make and test service changes before implementing them in a production environment. 

You must create new lifecycle hooks for your Amazon ECS blue/green deployment. 

## Prerequisites 

Perform the following operations before you start a blue/green deployment.  
Replace the Amazon ECS CodeDeploy IAM role with the following permissions.  
For information about Elastic Load Balancing permissions, see Amazon ECS infrastructure IAM role for load balancers. 
For information about Lambda permissions, see Permissions required for Lambda functions in Amazon ECS blue/green deployments. 
Turn off CodeDeploy automation. For more information, see Working with deployment groups in CodeDeploy in the CodeDeploy User Guide.  
Make sure that you have the following information from your CodeDeploy blue/green deployment. You can reuse this information for the Amazon ECS blue/green deployment:  
The production target group 
The production listener 
The production rule 
The test target group 

This is the target group for the green service revision, 
Ensure that your Application Load Balancer target groups are properly associated with listener rules:  
If you are not using test listeners, both target groups (production and test) must be associated with production listener rules. 
If you are using test listeners, one target group must be linked to production listener rules and the other target group must be linked to test listener rules. 
 

If this requirement is not met, the service deployment will fail with the following error: `Service deployment rolled back because of invalid networking configuration. Both targetGroup and alternateTargetGroup must be associated with the productionListenerRule or testListenerRule.` 
Verify that there are no ongoing service deployments for the service. For more information, see View service history using Amazon ECS service deployments. 
Amazon ECS blue/green deployments require your service to use one of the following features: Configure the appropriate resources.  
Application Load Balancer - For more information, see Application Load Balancer resources for blue/green, linear, and canary deployments. 
Network Load Balancer - For more information, see Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments. 
Service Connect - For more information, see Service Connect resources for Amazon ECS blue/green, linear, and canary deployments. 
VPC Lattice - For more information, see VPC Lattice resources for blue/green, linear, and canary deployments. 
Decide if you want to run Lambda functions for the lifecycle stages for the stages in the Amazon ECS blue/green deployment.  
Pre scale up 
After scale up 
Test traffic shift 
After test traffic shift 
Production traffic shift 
After production traffic shift 
 

Create Lambda functions for each lifecycle stage. For more information, see Create a Lambda function with the console in the AWS Lambda Developer Guide. 
 

For more information about updating a service's deployment controller, see Update Amazon ECS service parameters. 

## Procedure 
Open the console at https://console.aws.amazon.com/ecs/v2.
On the Clusters page, choose the cluster. 

The cluster details page displays. 
From the Services tab, choose the service. 

The service details page displays. 
In the banner, choose Update deployment controller type. 

The Migrate deployment controller type page displays. 
Expand New, and then specify the following parameters. 
For Deployment controller type, choose ECS. 
For Deployment strategy, choose Blue/green. 
For Bake time, enter the time that both the blue and green service revisions run. 
To run Lambda functions for a lifecycle stage, under Deployment lifecycle hooks do the following for each unique Lambda function: 
Choose Add. 

Repeat for every unique function you want to run. 
For Lambda function, enter the function name. 
For Role, choose the role that you created in the prerequisites with the blue/green permissions. 

For more information, see Permissions required for Lambda functions in Amazon ECS blue/green deployments. 
For Lifecycle stages, select the stages the Lambda function runs. 
 (Optional) For Hook details, enter a key-value pair that provides information about the hook. 
Expand Load Balancing, and the configure the following: 
For Role, choose the role that you created in the prerequisites with the blue/green permissions. 

For more information, see Permissions required for Lambda functions in Amazon ECS blue/green deployments. 
For Listener, choose the production listener from your CodeDeploy blue/green deployment. 
For Production rule, choose the production rule from your CodeDeploy blue/green deployment. 
For Test rule, choose the test rule from your CodeDeploy blue/green deployment. 
For Target group, choose the production target group from your CodeDeploy blue/green deployment. 
For Alternate target group, choose the test target group from your CodeDeploy blue/green deployment. 
Choose Update. 
 

## Next steps  
Update the service to start the deployment. For more information, see Updating an Amazon ECS service. 
Monitor the deployment process to ensure it follows the blue/green pattern:  
The green service revision is created and scaled up 
Test traffic is routed to the green revision (if configured) 
Production traffic is shifted to the green revision 
After the bake time, the blue revision is terminated
