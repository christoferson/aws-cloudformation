> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-linear.html
> Downloaded: 2026-10-20

# Amazon ECS linear deployments

Linear deployments gradually shift traffic from the old service revision to the new one in equal increments over time, allowing you to monitor each step before proceeding to the next. With Amazon ECS linear deployments, control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic. This approach provides a controlled way to deploy changes with the ability to monitor performance at each increment. 

## Resources involved in a linear deployment 

The following are resources involved in Amazon ECS linear deployments:  
Traffic shift - The process Amazon ECS uses to shift production traffic. For Amazon ECS linear deployments, traffic is shifted in equal percentage increments with configurable wait times between each increment. 
Step percent - The percentage of traffic to shift in each increment during a linear deployment. This field takes Double for value, and valid values are from 3.0 to 100.0. 
Step bake time - The duration to wait between each traffic shift increment during a linear deployment. Valid values are from 0 - 1440 minutes. 
Deployment bake time - The time, in minutes, Amazon ECS waits after shifting all production traffic to the new service revision, before it terminates the old service revision. This is the duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
Lifecycle stages - A series of events in the deployment operation, such as "after production traffic shift". 
Lifecycle hook - A Lambda function or pause point at a specific lifecycle stage. Lambda hooks invoke Lambda functions that you have defined to run custom code. Pause hooks pause the deployment and wait for you to call `ContinueServiceDeployment` to proceed. Hooks configured for `PRODUCTION_TRAFFIC_SHIFT` or `PRE_PRODUCTION_TRAFFIC_SHIFT` are invoked at every production traffic shift step. 
Target group - An Elastic Load Balancing or VPC Lattice resource used to route requests to one or more registered targets (for example, EC2 instances). When you create a listener, you specify a target group for its default action. Traffic is forwarded to the target group specified in the listener rule. 
Listener - An Elastic Load Balancing or VPC Lattice resource that checks for connection requests using the protocol and port that you configure. The rules that you define for a listener determine how Amazon ECS routes requests to its registered targets. 
Rule - An Elastic Load Balancing or VPC Lattice resource associated with a listener. A rule defines how requests are routed and consists of an action, condition, and priority. 
 

## Considerations 

Consider the following when choosing a deployment type:  
Resource usage: Linear deployments temporarily run both the blue and green service revisions simultaneously, which may double your resource usage during deployments. 
Deployment monitoring: Linear deployments provide detailed deployment status information, allowing you to monitor each stage of the deployment process and each traffic shift increment. 
Rollback: Linear deployments make it easier to roll back to the previous version if issues are detected, as the blue revision is kept running until the bake time expires. 
Gradual validation: Linear deployments allow you to validate the new revision with increasing amounts of production traffic, providing more confidence in the deployment. 
Deployment duration: Linear deployments take longer to complete than all-at-once deployments due to the incremental traffic shifting and wait times between steps. 
 

## How Linear deployment works 

The Amazon ECS Linear deployment process follows a structured approach with six distinct phases that ensure safe and reliable application updates. Each phase serves a specific purpose in validating and transitioning your application from the current version (blue) to the new version (green).  
Preparation Phase: Create the green environment alongside the existing blue environment. 
Deployment Phase: Deploy the new service revision to the green environment. Amazon ECS launches new tasks using the updated service revision while the blue environment continues serving production traffic. 
Testing Phase: Validate the green environment using test traffic routing. Your traffic-shifting resource (an Application Load Balancer, Network Load Balancer, Service Connect, or VPC Lattice) directs test requests to the green environment while production traffic remains on blue. 
Linear Traffic Shifting Phase: Gradually shift production traffic from blue to green in equal percentage increments based on your configured deployment strategy. 
Monitoring Phase: Monitor application health, performance metrics, and alarm states during the bake time period. A rollback operation is initiated when issues are detected. 
Completion Phase: Finalize the deployment by terminating the blue environment. 
 

The linear traffic shift phase follows these steps:  
Initial - The deployment begins with 100% of traffic routed to the blue (current) service revision. The green (new) service revision receives test traffic but no production traffic initially. 
Incremental traffic shifting - Traffic is gradually shifted from blue to green in equal percentage increments. For example, with a 10.0% step configuration, traffic shifts occur as follows:  
Step 1: 10.0% to green, 90.0% to blue 
Step 2: 20.0% to green, 80.0% to blue 
Step 3: 30.0% to green, 70.0% to blue 
And so on until 100% reaches green 
Step bake time - Between each traffic shift increment, the deployment waits for a configurable duration (step bake time) to allow monitoring and validation of the new revision's performance with the increased traffic load. Note, that last step bake time is skipped once traffic is shifted 100.0%. 
Lifecycle hooks - Optional Lambda functions or pause hooks can be configured at various lifecycle stages during the deployment to perform automated validation, monitoring, or custom logic. Hooks configured for `PRODUCTION_TRAFFIC_SHIFT` or `PRE_PRODUCTION_TRAFFIC_SHIFT` are invoked at every production traffic shift step. 
 

## Deployment lifecycle stages 

The Linear deployment process progresses through distinct lifecycle stages, each with specific responsibilities and validation checkpoints. Understanding these stages helps you monitor deployment progress and troubleshoot issues effectively. 

Each lifecycle stage can last up to 24 hours and in addition each traffic shift step in PRODUCTION_TRAFFIC_SHIFT can last upto 24 hours. We recommend that the value remains below the 24-hour mark. This is because asynchronous processes need time to trigger the hooks. The system times out, fails the deployment, and then initiates a rollback after a stage reaches 24 hours. 

CloudFormation deployments have additional timeout restrictions. While the 24-hour stage limit remains in effect, CloudFormation enforces a 36-hour limit on the entire deployment. CloudFormation fails the deployment, and then initiates a rollback if the process doesn't complete within 36 hours. 

For pause hooks, you can configure the timeout up to 20,160 minutes (14 days). The overall deployment timeout is 30 days.  
|  Lifecycle stages |  Description |  Lifecycle hook support |    
|  RECONCILE_SERVICE |  This stage only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state. |  Yes |   
|  PRE_SCALE_UP |  The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic. |  Yes |   
|  SCALE_UP |  The time when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point. |  No |   
|  POST_SCALE_UP |  The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic. |  Yes |   
|  TEST_TRAFFIC_SHIFT |  The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic. |  Yes (Lambda only) |   
|  POST_TEST_TRAFFIC_SHIFT |  The test traffic shift is complete. The green service revision handles 100% of the test traffic. |  Yes |   
|  PRE_PRODUCTION_TRAFFIC_SHIFT |  Occurs before each production traffic shift increment. Lifecycle hooks configured for this stage are invoked at every traffic shift step. |  Yes |   
|  PRODUCTION_TRAFFIC_SHIFT |  Traffic is gradually shifted from blue to green in equal percentage increments until green receives 100% of traffic. Each traffic shift invokes lifecycle hook with 24 hours timeout. |  Yes (Lambda only) |   
|  POST_PRODUCTION_TRAFFIC_SHIFT |  The production traffic shift is complete. |  Yes |   
|  BAKE_TIME |  The duration when both blue and green service revisions are running simultaneously. |  No |   
|  CLEAN_UP |  The blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage. |  No |
