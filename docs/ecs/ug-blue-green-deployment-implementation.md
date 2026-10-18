> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html
> Downloaded: 2026-10-18

# Required resources for Amazon ECS blue/green deployments

You can use Amazon ECS blue/green deployments with or without managed traffic shifting. When your service uses Elastic Load Balancing, Service Connect, or VPC Lattice, Amazon ECS manages the traffic shift between the blue and green service revisions for you. If your service doesn't use a load balancer, Service Connect, or VPC Lattice (headless service), you can still use blue/green deployments for controlled rollouts, but Amazon ECS doesn't manage the traffic shift automatically.

For managed traffic shifting, configure one of the following: 
Elastic Load Balancing 
Service Connect 
VPC Lattice 

The following list provides a high-level overview of what you need to configure for Amazon ECS blue/green deployments: 
If your service uses an Application Load Balancer, Network Load Balancer, Service Connect, or VPC Lattice, configure the appropriate resources for managed traffic shifting.  
Application Load Balancer - For more information, see Application Load Balancer resources for blue/green, linear, and canary deployments. 
Network Load Balancer - For more information, see Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments. 
Service Connect - For more information, see Service Connect resources for Amazon ECS blue/green, linear, and canary deployments. 
VPC Lattice - For more information, see VPC Lattice resources for blue/green, linear, and canary deployments. 
 

If your service is headless (no load balancer, Service Connect, or VPC Lattice), you don't need to configure additional traffic shifting resources. 
Set the service deployment controller to `ECS`. 
Configure the deployment strategy as `blue/green` in your service definition. 
Optionally, configure additional parameters such as:  
Bake time for the new deployment 
CloudWatch alarms for automatic rollback 
Deployment lifecycle hooks (Lambda functions or pause hooks that run at specified deployment stages) 
 
 

## Best practices 

Follow these best practices for successful Amazon ECS blue/green deployments:  
Configure appropriate health checks that accurately reflect your application's health. 
Set a bake time that allows sufficient testing of the green deployment. 
Implement CloudWatch alarms to automatically detect issues and trigger rollbacks. 
Use lifecycle hooks to perform automated testing at each deployment stage. 
Ensure your application can handle both blue and green service revisions running simultaneously. 
Plan for sufficient cluster capacity to handle both service revisions during deployment. 
Test your rollback procedures before implementing them in production.
