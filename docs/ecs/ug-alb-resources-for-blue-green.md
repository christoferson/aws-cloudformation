> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb-resources-for-blue-green.html
> Downloaded: 2026-10-18

# Application Load Balancer resources for blue/green, linear, and canary deployments

To use Application Load Balancers with Amazon ECS blue/green deployments, you need to configure specific resources that allow traffic routing between the blue and green service revisions.  

## Target groups 

For blue/green deployments with Elastic Load Balancing, you need to create two target groups:  
A primary target group for the blue service revision (current production traffic) 
An alternate target group for the green service revision (new version) 
 

Both target groups should be configured with the following settings:  
Target type: `IP` (for Fargate or EC2 with `awsvpc` network mode) 
Protocol: `HTTP` (or the protocol your application uses) 
Port: The port your application listens on (typically `80` for HTTP) 
VPC: The same VPC as your Amazon ECS tasks 
Health check settings: Configured to properly check your application's health 
 

During a blue/green deployment, Amazon ECS automatically registers tasks with the appropriate target group based on the deployment stage. Example Creating target groups for an Application Load Balancer

The following CLI commands create two target groups for use with an Application Load Balancer in a blue/green deployment:

```
aws elbv2 create-target-group \
    --name blue-target-group \
    --protocol HTTP \
    --port 80 \
    --vpc-id vpc-abcd1234 \
    --target-type ip \
    --health-check-path / \
    --health-check-protocol HTTP \
    --health-check-interval-seconds 30 \
    --health-check-timeout-seconds 5 \
    --healthy-threshold-count 2 \
    --unhealthy-threshold-count 2

aws elbv2 create-target-group \
    --name green-target-group \
    --protocol HTTP \
    --port 80 \
    --vpc-id vpc-abcd1234 \
    --target-type ip \
    --health-check-path / \
    --health-check-protocol HTTP \
    --health-check-interval-seconds 30 \
    --health-check-timeout-seconds 5 \
    --healthy-threshold-count 2 \
    --unhealthy-threshold-count 2
```
 

## Application Load Balancer 

You need to create an Application Load Balancer with the following configuration:  
Scheme: Internet-facing or internal, depending on your requirements 
IP address type: IPv4 
VPC: The same VPC as your Amazon ECS tasks 
Subnets: At least two subnets in different Availability Zones 
Security groups: A security group that allows traffic on the listener ports 
 

The security group attached to the Application Load Balancer must have an outbound rule that allows traffic to the security group attached to your Amazon ECS tasks. Example Creating an Application Load Balancer

The following CLI command creates anApplication Load Balancer for use in a blue/green deployment:

```
aws elbv2 create-load-balancer \
    --name my-application-load-balancer \
    --type application \
    --security-groups sg-abcd1234 \
    --subnets subnet-12345678 subnet-87654321
```
 

## Listeners and rules 

For blue/green deployments, you need to configure listeners on your Application Load Balancer:  
Production listener: Handles production traffic (typically on port 80 or 443)  
Initially forwards traffic to the primary target group (blue service revision) 
After deployment, forwards traffic to the alternate target group (green service revision) 
Test listener (optional): Handles test traffic to validate the green service revision before shifting production traffic  
Can be configured on a different port (for example, 8080 or 8443) 
Forwards traffic to the alternate target group (green service revision) during testing 
 
 

During a blue/green deployment, Amazon ECS automatically updates the listener rules to route traffic to the appropriate target group based on the deployment stage. Example Creating a production listener

The following CLI command creates a production listener on port 80 that forwards traffic to the primary (blue) target group:

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:region:123456789012:loadbalancer/app/my-application-load-balancer/abcdef123456 \
    --protocol HTTP \
    --port 80 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/blue-target-group/abcdef123456
```
 Example Creating a test listener

The following CLI command creates a test listener on port 8080 that forwards traffic to the alternate (green) target group:

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:region:123456789012:loadbalancer/app/my-application-load-balancer/abcdef123456 \
    --protocol HTTP \
    --port 8080 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/green-target-group/ghijkl789012
```
 Example Creating a listener rule for path-based routing

The following CLI command creates a rule that forwards traffic for a specific path to the green target group for testing:

```
aws elbv2 create-rule \
    --listener-arn arn:aws:elasticloadbalancing:region:123456789012:listener/app/my-application-load-balancer/abcdef123456/ghijkl789012 \
    --priority 10 \
    --conditions Field=path-pattern,Values='/test/*' \
    --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/green-target-group/ghijkl789012
```
 Example Creating a listener rule for header-based routing

The following CLI command creates a rule that forwards traffic with a specific header to the green target group for testing:

```
aws elbv2 create-rule \
    --listener-arn arn:aws:elasticloadbalancing:region:123456789012:listener/app/my-application-load-balancer/abcdef123456/ghijkl789012 \
    --priority 20 \
    --conditions Field=http-header,HttpHeaderConfig='{Name=X-Environment,Values=[test]}' \
    --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/green-target-group/ghijkl789012
```
 

## Service configuration 

You must have permissions to allow Amazon ECS to manage load balancer resources in your clusters on your behalf. For more information, see Amazon ECS infrastructure IAM role for load balancers.  

When creating or updating an Amazon ECS service for blue/green deployments with Elastic Load Balancing, you need to specify the following configuration. 

Replace the `user-input` with your values. 

The key components in this configuration are:  
`targetGroupArn`: The ARN of the primary target group (blue service revision). 
`alternateTargetGroupArn`: The ARN of the alternate target group (green service revision). 
`productionListenerRule`: The ARN of the listener rule for production traffic. 
`roleArn`: The ARN of the role that allows Amazon ECS to manage Elastic Load Balancing resources. 
`strategy`: Set to `BLUE_GREEN` to enable blue/green deployments. 
`bakeTimeInMinutes`: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
`TestListenerRule`: The ARN of the listener rule for test traffic. This is an optional parameter. 
 

```
{
    "loadBalancers": [
        {
            "targetGroupArn": "arn:aws:elasticloadbalancing:region:123456789012:targetgroup/primary-target-group/abcdef123456",
            "containerName": "container-name",
            "containerPort": 80,
            "advancedConfiguration": {
                "alternateTargetGroupArn": "arn:aws:elasticloadbalancing:region:account-id:targetgroup/alternate-target-group/ghijkl789012",
                "productionListenerRule": "arn:aws:elasticloadbalancing:region:account-id:listener-rule/app/load-balancer-name/abcdef123456/listener/ghijkl789012/rule/mnopqr345678",
                "roleArn": "arn:aws:iam::123456789012:role/ecs-elb-role"
            }
        }
    ],
    "deploymentConfiguration": {
        "strategy": "BLUE_GREEN",
        "maximumPercent": 200,
        "minimumHealthyPercent": 100,
        "bakeTimeInMinutes": 5
    }
}
```
 

## Traffic flow during deployment 

During a blue/green deployment with Elastic Load Balancing, traffic flows through the system as follows:  
Initial state: All production traffic is routed to the primary target group (blue service revision). 
Green service revision deployment: Amazon ECS deploys the new tasks and registers them with the alternate target group. 
Test traffic: If a test listener is configured, test traffic is routed to the alternate target group to validate the green service revision. 
Production traffic shift: Amazon ECS updates the production listener rule to route traffic to the alternate target group (green service revision). 
Bake time: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
Completion: After a successful deployment, the blue service revision is terminated. 
 

If issues are detected during the deployment, Amazon ECS can automatically roll back by routing traffic back to the primary target group (blue service revision).
