> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/nlb-resources-for-blue-green.html
> Downloaded: 2026-10-18

# Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments

To use a Network Load Balancer with Amazon ECS blue/green deployments, you need to configure specific resources that enable traffic routing between the blue and green service revisions. This section explains the required components and their configuration.

When your configuration includes a Network Load Balancer, Amazon ECS adds a 10 minute delay to the following lifecycle stages: 
TEST_TRAFFIC_SHIFT 
PRODUCTION_TRAFFIC_SHIFT 

This delay accounts for Network Load Balancer timing issues that can cause a mismatch between the configured traffic weights and the actual traffic routing in the data plane.  

## Target groups 

For blue/green deployments with a Network Load Balancer, you need to create two target groups:  
A primary target group for the blue service revision (current production traffic) 
An alternate target group for the green service revision (new service revision) 
 

Both target groups should be configured with the following settings:  
Target type: `ip` (for Fargate or EC2 with `awsvpc` network mode) 
Protocol: `TCP` (or the protocol your application uses) 
Port: The port your application listens on (typically `80` for HTTP) 
VPC: The same VPC as your Amazon ECS tasks 
Health check settings: Configured to properly check your application's health 

For TCP health checks, the Network Load Balancer establishes a TCP connection with the target. If the connection is successful, the target is considered healthy. 

For HTTP/HTTPS health checks, the Network Load Balancer sends an HTTP/HTTPS request to the target and verifies the response. 
 

During a blue/green deployment, Amazon ECS automatically registers tasks with the appropriate target group based on the deployment stage. Example Creating target groups for a Network Load Balancer

The following AWS CLI commands create two target groups for use with a Network Load Balancer in a blue/green deployment:

```
aws elbv2 create-target-group \
    --name blue-target-group \
    --protocol TCP \
    --port 80 \
    --vpc-id vpc-abcd1234 \
    --target-type ip \
    --health-check-protocol TCP

aws elbv2 create-target-group \
    --name green-target-group \
    --protocol TCP \
    --port 80 \
    --vpc-id vpc-abcd1234 \
    --target-type ip \
    --health-check-protocol TCP
```
 

## Network Load Balancer 

You need to create a Network Load Balancer with the following configuration:  
Scheme: Internet-facing or internal, depending on your requirements 
IP address type: IPv4 
VPC: The same VPC as your Amazon ECS tasks 
Subnets: At least two subnets in different Availability Zones 
 

Unlike Application Load Balancers, Network Load Balancers operate at the transport layer (Layer 4) and do not use security groups. Instead, you need to ensure that the security groups associated with your Amazon ECS tasks allow traffic from the Network Load Balancer on the listener ports. Example Creating a Network Load Balancer

The following AWS CLI command creates a Network Load Balancer for use in a blue/green deployment:

```
aws elbv2 create-load-balancer \
    --name my-network-load-balancer \
    --type network \
    --subnets subnet-12345678 subnet-87654321
```
 

## Considerations for using NLB with blue/green deployments 

When using a Network Load Balancer for blue/green deployments, consider the following:  
Layer 4 operation: Network Load Balancers operate at the transport layer (Layer 4) and do not inspect application layer (Layer 7) content. This means you cannot use HTTP headers or paths for routing decisions. 
Health checks: Network Load Balancer health checks are limited to TCP, HTTP, or HTTPS protocols. For TCP health checks, the Network Load Balancer only verifies that the connection can be established. 
Connection preservation: Network Load Balancers preserve the source IP address of the client, which can be useful for security and logging purposes. 
Static IP addresses: Network Load Balancers provide static IP addresses for each subnet, which can be useful for whitelisting or when clients need to connect to a fixed IP address. 
Test traffic: Since Network Load Balancers do not support content-based routing, test traffic must be sent to a different port than production traffic. 
 

## Listeners and rules 

For blue/green deployments with a Network Load Balancer, you need to configure listeners:  
Production listener: Handles production traffic (typically on port 80 or 443)  
Initially forwards traffic to the primary target group (blue service revision) 
After deployment, forwards traffic to the alternate target group (green service revision) 
Test listener (optional): Handles test traffic to validate the green service revision before shifting production traffic  
Can be configured on a different port (e.g., 8080 or 8443) 
Forwards traffic to the alternate target group (green service revision) during testing 
 
 

Unlike Application Load Balancers, Network Load Balancers do not support content-based routing rules. Instead, traffic is routed based on the listener port and protocol. 

The following AWS CLI commands create production and test listeners for a Network Load Balancer: 

Replace the `user-input` with your values. 

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:region:123456789012:loadbalancer/net/my-network-lb/1234567890123456 \
    --protocol TCP \
    --port 80 \
    --default-actions Type=forward, TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/blue-target-group/1234567890123456

aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:region:123456789012:loadbalancer/net/my-network-lb/1234567890123456 \
    --protocol TCP \
    --port 8080 \
    --default-actions Type=forward, TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/green-target-group/1234567890123456
```
 

## Service configuration 

You must have permissions to allow Amazon ECS to manage load balancer resources in your clusters on your behalf. For more information, see Amazon ECS infrastructure IAM role for load balancers.  

When creating or updating an Amazon ECS service for blue/green deployments with a Network Load Balancer, you need to specify the following configuration: 

Replace the `user-input` with your values. 

The key components in this configuration are:  
`targetGroupArn`: The ARN of the primary target group (blue service revision) 
`alternateTargetGroupArn`: The ARN of the alternate target group (green service revision) 
`productionListenerRule`: The ARN of the listener for production traffic 
`testListenerRule`: (Optional) The ARN of the listener for test traffic 
`roleArn`: The ARN of the role that allows Amazon ECS to manage Network Load Balancer resources 
`strategy`: Set to `BLUE_GREEN` to enable blue/green deployments 
`bakeTimeInMinutes`: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted 
 

```
{
    "loadBalancers": [
        {
            "targetGroupArn": "arn:aws:elasticloadbalancing:region:123456789012:targetgroup/blue-target-group/1234567890123456",
            "containerName": "container-name",
            "containerPort": 80,
            "advancedConfiguration": {
                "alternateTargetGroupArn": "arn:aws:elasticloadbalancing:region:123456789012:targetgroup/green-target-group/1234567890123456",
                "productionListenerRule": "arn:aws:elasticloadbalancing:region:123456789012:listener/net/my-network-lb/1234567890123456/1234567890123456",
                "testListenerRule": "arn:aws:elasticloadbalancing:region:123456789012:listener/net/my-network-lb/1234567890123456/2345678901234567",
                "roleArn": "arn:aws:iam::123456789012:role/ecs-nlb-role"
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

During a blue/green deployment with a Network Load Balancer, traffic flows through the system as follows:  
Initial state: All production traffic is routed to the primary target group (blue service revision). 
Green service revision deployment: Amazon ECS deploys the new tasks and registers them with the alternate target group. 
Test traffic: If a test listener is configured, test traffic is routed to the alternate target group to validate the green service revision. 
Production traffic shift: Amazon ECS updates the production listener to route traffic to the alternate target group (green service revision). 
Bake time: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
Completion: After a successful deployment, the blue service revision is terminated. 
 

If issues are detected during the deployment, Amazon ECS can automatically roll back by routing traffic back to the primary target group (blue service revision).
