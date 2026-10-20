> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/canary-deployment.html
> Downloaded: 2026-10-20

# Amazon ECS canary deployments

Canary deployments first route a small percentage of traffic to the new revision for initial testing, then shift all remaining traffic at once after the canary phase completes successfully. With Amazon ECS canary deployments, validate new service revisions with real user traffic while minimizing risk exposure. This approach provides a controlled way to deploy changes with the ability to monitor performance and roll back quickly if issues are detected. 

## Resources involved in a canary deployment 

The following are resources involved in Amazon ECS canary deployments:  
Traffic shift - The process Amazon ECS uses to shift production traffic. For Amazon ECS canary deployments, traffic is shifted in two phases: first to the canary percentage, then to complete the deployment. 
Canary percentage - The percentage of traffic routed to the new version during the evaluation period. 
Canary bake time - The duration to monitor the canary version before proceeding with full deployment. 
Deployment bake time - The time, in minutes, Amazon ECS waits after shifting all production traffic to the new service revision, before it terminates the old service revision. This is the duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
Lifecycle stages - A series of events in the deployment operation, such as "after production traffic shift". 
Lifecycle hook - A Lambda function or pause point at a specific lifecycle stage. Lambda hooks invoke Lambda functions that you have defined to run custom code. Pause hooks pause the deployment and wait for you to call `ContinueServiceDeployment` to proceed. 
Target group - An Elastic Load Balancing or VPC Lattice resource used to route requests to one or more registered targets (for example, EC2 instances). When you create a listener, you specify a target group for its default action. Traffic is forwarded to the target group specified in the listener rule. 
Listener - An Elastic Load Balancing or VPC Lattice resource that checks for connection requests using the protocol and port that you configure. The rules that you define for a listener determine how Amazon ECS routes requests to its registered targets. 
Rule - An Elastic Load Balancing or VPC Lattice resource associated with a listener. A rule defines how requests are routed and consists of an action, condition, and priority. 
 

## Considerations 

Consider the following when choosing a deployment type:  
Resource usage: Canary deployments run both original and canary task sets simultaneously during the evaluation period, increasing resource usage. 
Traffic volume: Ensure the canary percentage generates sufficient traffic for meaningful validation of the new version. 
Monitoring complexity: Canary deployments require monitoring and comparing metrics between two different versions simultaneously. 
Rollback speed: Canary deployments enable quick rollback by shifting traffic back to the original task set. 
Risk mitigation: Canary deployments provide excellent risk mitigation by limiting exposure to a small percentage of users. 
Deployment duration: Canary deployments include evaluation periods that extend the overall deployment time but provide validation opportunities. 
 

## How canary deployments work 

The Amazon ECS Canary deployment process follows a structured approach with six distinct phases that ensure safe and reliable application updates. Each phase serves a specific purpose in validating and transitioning your application from the current version (blue) to the new version (green).  
Preparation Phase: Create the green environment alongside the existing blue environment. 
Deployment Phase: Deploy the new service revision to the green environment. Amazon ECS launches new tasks using the updated service revision while the blue environment continues serving production traffic. 
Testing Phase: Validate the green environment using test traffic routing. The Application Load Balancer directs test requests to the green environment while production traffic remains on blue. 
Canary Traffic Shifting Phase: Shift configured percentage of traffic to the new green service revision during the canary phase, followed by shifting 100.0% of traffic to Green service revision 
Monitoring Phase: Monitor application health, performance metrics, and alarm states during the bake time period. A rollback operation is initiated when issues are detected. 
Completion Phase: Finalize the deployment by terminating the blue environment. 
 

The canary traffic shift phase follows these steps:  
Initial - The deployment begins with 100% of traffic routed to the blue (current) service revision. The green (new) service revision receives test traffic but no production traffic initially. 
Canary traffic shifting - This is a two step traffic shift strategy.  
Step 1: 10.0% to green, 90.0% to blue 
Step 2: 100.0% to green, 0.0% to blue 
Canary bake time - Waits for a configurable duration (canary bake time) after canary traffic shift to allow monitoring and validation of the new revision's performance with the increased traffic load. 
Lifecycle hooks - Optional Lambda functions or pause hooks can be configured at various lifecycle stages during the deployment to perform automated validation, monitoring, or custom logic. Hooks configured for `PRODUCTION_TRAFFIC_SHIFT` or `PRE_PRODUCTION_TRAFFIC_SHIFT` are invoked at every production traffic shift step. 
 

### Deployment lifecycle stages 

The canary deployment process progresses through distinct lifecycle stages, each with specific responsibilities and validation checkpoints. Understanding these stages helps you monitor deployment progress and troubleshoot issues effectively. 

Each lifecycle stage can last up to 24 hours and in addition each traffic shift step in PRODUCTION_TRAFFIC_SHIFT can last upto 24 hours. We recommend that the value remains below the 24-hour mark. This is because asynchronous processes need time to trigger the hooks. The system times out, fails the deployment, and then initiates a rollback after a stage reaches 24 hours. 

CloudFormation deployments have additional timeout restrictions. While the 24-hour stage limit remains in effect, CloudFormation enforces a 36-hour limit on the entire deployment. CloudFormation fails the deployment, and then initiates a rollback if the process doesn't complete within 36 hours. 

For pause hooks, you can configure the timeout up to 20,160 minutes (14 days). The overall deployment timeout is 30 days. Lifecycle stages 
|  Lifecycle stages |  Description |  Lifecycle hook support |    
|  RECONCILE_SERVICE |  This stage only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state. |  Yes |   
|  PRE_SCALE_UP |  The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic. |  Yes |   
|  SCALE_UP |  The time when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point. |  No |   
|  POST_SCALE_UP |  The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic. |  Yes |   
|  TEST_TRAFFIC_SHIFT |  The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic. |  Yes (Lambda only) |   
|  POST_TEST_TRAFFIC_SHIFT |  The test traffic shift is complete. The green service revision handles 100% of the test traffic. |  Yes |   
|  PRE_PRODUCTION_TRAFFIC_SHIFT |  Occurs before each production traffic shift step. For canary, this occurs before the canary traffic shift and before the remaining traffic shift. |  Yes |   
|  PRODUCTION_TRAFFIC_SHIFT |  Canary production traffic is routed to green revision and lifecycle hook is invoked with 24 hours timeout. The second step shifts remaining production traffic to green revision. |  Yes (Lambda only) |   
|  POST_PRODUCTION_TRAFFIC_SHIFT |  The production traffic shift is complete. |  Yes |   
|  BAKE_TIME |  The duration when both blue and green service revisions are running simultaneously. |  No |   
|  CLEAN_UP |  The blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage. |  No |    

### Configuration parameters 

Canary deployments require the following configuration parameters:  
Canary percentage - The percentage of traffic to route to the new service revision during the canary phase. This allows testing with a controlled subset of production traffic. 
Canary bake time - The duration to wait during the canary phase before shifting the remaining traffic to the new service revision. This provides time to monitor and validate the new version. 
 

### Traffic management 

Canary deployments use load balancer target groups to manage traffic distribution:  
Original target group - Contains tasks from the current stable version and receives the majority of traffic. 
Canary target group - Contains tasks from the new version and receives a small percentage of traffic for testing. 
Weighted routing - The load balancer uses weighted routing rules to distribute traffic between the target groups based on the configured canary percentage. 
 

### Monitoring and validation 

Effective canary deployments rely on comprehensive monitoring:  
Health checks - Both task sets must pass health checks before receiving traffic. 
Metrics comparison - Compare key performance indicators between the original and canary versions, such as response time, error rate, and throughput. 
Automated rollback - Configure CloudWatch alarms to automatically trigger rollback if the canary version shows degraded performance. 
Manual validation - Use the evaluation period to manually review logs, metrics, and user feedback before proceeding. 
 

### Best practices for canary deployments 

Follow these best practices to ensure successful canary deployments with services. 

#### Choose appropriate traffic percentages 

Consider these factors when selecting canary traffic percentages:  
Start small - Begin with 5-10% of traffic to minimize impact if issues occur. 
Consider application criticality - Use smaller percentages for mission-critical applications and larger percentages for less critical services. 
Account for traffic volume - Ensure the canary percentage generates sufficient traffic for meaningful validation. 
 

#### Set appropriate evaluation periods 

Configure evaluation periods based on these considerations:  
Allow sufficient time - Set evaluation periods long enough to capture meaningful performance data, typically 10-30 minutes. 
Consider traffic patterns - Account for your application's traffic patterns and peak usage times. 
Balance speed and safety - Longer evaluation periods provide more data but slow deployment velocity. 
 

#### Implement comprehensive monitoring 

Set up monitoring to track canary deployment performance:  
Key metrics - Monitor response time, error rate, throughput, and resource utilization for both task sets. 
Alarm-based rollback - Configure CloudWatch alarms to automatically trigger rollback when metrics exceed thresholds. 
Comparative analysis - Set up dashboards to compare metrics between original and canary versions side-by-side. 
Business metrics - Include business-specific metrics like conversion rates or user engagement alongside technical metrics. 
 

#### Plan rollback strategies 

Prepare for potential rollback scenarios with these strategies:  
Automated rollback - Configure automatic rollback triggers based on health checks and performance metrics. 
Manual rollback procedures - Document clear procedures for manual rollback when automated triggers don't capture all issues. 
Rollback testing - Regularly test rollback procedures to ensure they work correctly when needed. 
 

#### Validate thoroughly before deployment 

Ensure thorough validation before proceeding with canary deployments:  
Pre-deployment testing - Thoroughly test changes in staging environments before canary deployment. 
Health check configuration - Ensure health checks accurately reflect application readiness and functionality. 
Dependency validation - Verify that new versions are compatible with downstream and upstream services. 
Data consistency - Ensure database schema changes and data migrations are backward compatible. 
 

#### Coordinate team involvement 

Ensure effective team coordination during canary deployments:  
Deployment windows - Schedule canary deployments during business hours when teams are available to monitor and respond. 
Communication channels - Establish clear communication channels for deployment status and issue escalation. 
Role assignments - Define roles and responsibilities for monitoring, decision-making, and rollback execution.
