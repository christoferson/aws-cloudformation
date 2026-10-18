> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-lattice-resources-for-blue-green.html
> Downloaded: 2026-10-18

# VPC Lattice resources for blue/green, linear, and canary deployments

To use Amazon VPC Lattice with Amazon ECS blue/green, linear, and canary deployments, you configure the following resources: 
A pair of VPC Lattice target groups. 
A VPC Lattice service with a listener. 
The listener rules that route traffic to the target groups. A production listener rule is required, and a test listener rule is optional. 

When your service uses VPC Lattice, Amazon ECS waits at the following deployment lifecycle stages so that target registration and traffic-weight changes can propagate to the VPC Lattice data plane: 
`POST_SCALE_UP` – approximately 3 minutes, so that the new tasks are healthy before Amazon ECS shifts traffic to them. 
`TEST_TRAFFIC_SHIFT`, `PRODUCTION_TRAFFIC_SHIFT`, and `RECONCILE_SERVICE` – approximately 90 seconds after each weight change. Canary deployments change weights twice; linear deployments change weights once per step. 
 

## Target groups 

For blue/green, linear, and canary deployments with VPC Lattice, you need to create two target groups:  
A primary target group for the blue service revision (the version currently serving production traffic) 
An alternate target group for the green service revision (new version) 
 

Configure both target groups with the following settings:  
Target type: `IP` (required for Amazon ECS tasks) 
Protocol: `HTTP` (or the protocol your application uses) 
Port: The port your application listens on (typically `80` for HTTP) 
IP address type: `IPV4` or `IPV6` (match your tasks) 
VPC: The same VPC as your Amazon ECS tasks 
Health check settings: Configured to properly check your application's health 
 

The two target groups swap roles on every deployment. Amazon ECS registers the new service revision's tasks with whichever target group isn't serving production traffic. 

Both target groups must be in the `ACTIVE` state. Example Creating target groups for VPC Lattice

The following CLI commands create two target groups for a blue/green deployment:

```
aws vpc-lattice create-target-group \
    --name blue-target-group \
    --type IP \
    --config '{
        "port": 80,
        "protocol": "HTTP",
        "ipAddressType": "IPV4",
        "vpcIdentifier": "vpc-abcd1234",
        "healthCheck": {
            "enabled": true,
            "protocol": "HTTP",
            "path": "/",
            "healthCheckIntervalSeconds": 30,
            "healthCheckTimeoutSeconds": 5,
            "healthyThresholdCount": 2,
            "unhealthyThresholdCount": 2
        }
    }'

aws vpc-lattice create-target-group \
    --name green-target-group \
    --type IP \
    --config '{
        "port": 80,
        "protocol": "HTTP",
        "ipAddressType": "IPV4",
        "vpcIdentifier": "vpc-abcd1234",
        "healthCheck": {
            "enabled": true,
            "protocol": "HTTP",
            "path": "/",
            "healthCheckIntervalSeconds": 30,
            "healthCheckTimeoutSeconds": 5,
            "healthyThresholdCount": 2,
            "unhealthyThresholdCount": 2
        }
    }'
```
 

## VPC Lattice service 

You need a VPC Lattice service with a listener that carries the rules described in the next section. Clients reach the VPC Lattice service through a service network, or through a VPC association, in the same way as for an Amazon ECS service that doesn't use blue/green deployments. To learn more about these VPC Lattice resources, see the Amazon VPC Lattice User Guide. 

The security group attached to your Amazon ECS tasks must allow inbound traffic on the container port from the VPC Lattice managed prefix list (`com.amazonaws.region.vpc-lattice`, or `com.amazonaws.region.ipv6.vpc-lattice` for IPv6). A managed prefix list is an AWS-managed set of CIDR blocks for VPC Lattice that you reference in a security group rule. For more information, see Control traffic to your VPC Lattice services using security groups. Example Creating a VPC Lattice service and a listener

The following CLI commands create a VPC Lattice service and an HTTP listener. The listener's default action returns a fixed `404` response, so only the listener rules route traffic to the target groups:

```
aws vpc-lattice create-service \
    --name my-service

aws vpc-lattice create-listener \
    --service-identifier svc-0123456789abcdef0 \
    --name my-listener \
    --protocol HTTP \
    --port 80 \
    --default-action '{
        "fixedResponse": {
            "statusCode": 404
        }
    }'
```
 

Associate the VPC Lattice service with a service network so that your clients can reach it. The service network must already exist and be associated with the VPC that your clients run in. Example Associating the service with a service network

The following CLI command associates the VPC Lattice service with a service network:

```
aws vpc-lattice create-service-network-service-association \
    --service-identifier svc-0123456789abcdef0 \
    --service-network-identifier sn-0123456789abcdef0
```
 

## Listeners and rules 

You configure the following listener rules on your VPC Lattice service:  
Production listener rule (required): Routes production traffic.  
Initially forwards all traffic to one of the two target groups. 
After a successful deployment, forwards all traffic to the other target group. 
Test listener rule (optional): Routes test traffic, so you can validate the new service revision before production traffic moves to it.  
Must match a different set of requests than the production listener rule matches, and must be evaluated first. For example, match on a specific header or path, and give the test rule a lower priority number than the production rule, because VPC Lattice evaluates lower priority numbers first. 
Amazon ECS points the test listener rule at the new service revision during the `TEST_TRAFFIC_SHIFT` stage, before any production traffic moves. 
If you don't configure a test listener rule, Amazon ECS skips test traffic routing. 
 
 

Both rules must meet the following requirements:  
The action is `forward`. Amazon ECS rejects a rule with a `fixedResponse` action. 
The rule must forward to both target groups, with weight `100` on the target group that currently serves that traffic and weight `0` on the other. Both target groups are required. 
The test listener rule is on the same VPC Lattice service as the production listener rule, and it is a different rule. 
Each listener rule can be used by only one VPC Lattice configuration on the Amazon ECS service. 
 Note

The production listener rule can also be the listener's default rule. In that case, Amazon ECS updates the listener's default action instead of a named rule, so specify the listener ARN in place of a rule ARN. Use this approach for listeners that don't support rules, such as `TLS_PASSTHROUGH` listeners. For test traffic on such a service, use the default rule of a second listener on a different port. 

Amazon ECS shifts traffic by rewriting the forward action of these rules while a deployment is in progress. Example Creating a production listener rule

The following CLI command creates a production listener rule that matches all paths and forwards all traffic to the blue target group:

```
aws vpc-lattice create-rule \
    --service-identifier svc-0123456789abcdef0 \
    --listener-identifier listener-0123456789abcdef0 \
    --name production \
    --priority 100 \
    --match '{
        "httpMatch": {
            "pathMatch": {
                "match": {
                    "prefix": "/"
                }
            }
        }
    }' \
    --action '{
        "forward": {
            "targetGroups": [
                {
                    "targetGroupIdentifier": "tg-0123456789abcdef0",
                    "weight": 100
                },
                {
                    "targetGroupIdentifier": "tg-0fedcba9876543210",
                    "weight": 0
                }
            ]
        }
    }'
```
 Example Creating a test listener rule for header-based routing

The following CLI command creates a test listener rule that matches requests with an `X-Environment: test` header. It has a lower priority number than the production listener rule, so VPC Lattice evaluates it first:

```
aws vpc-lattice create-rule \
    --service-identifier svc-0123456789abcdef0 \
    --listener-identifier listener-0123456789abcdef0 \
    --name test \
    --priority 10 \
    --match '{
        "httpMatch": {
            "headerMatches": [
                {
                    "name": "X-Environment",
                    "match": {
                        "exact": "test"
                    }
                }
            ]
        }
    }' \
    --action '{
        "forward": {
            "targetGroups": [
                {
                    "targetGroupIdentifier": "tg-0123456789abcdef0",
                    "weight": 100
                },
                {
                    "targetGroupIdentifier": "tg-0fedcba9876543210",
                    "weight": 0
                }
            ]
        }
    }'
```
 

## Service configuration 

You must have permissions to allow Amazon ECS to manage VPC Lattice resources on your behalf. For more information, see Amazon ECS infrastructure IAM role. 

When you create or update an Amazon ECS service for blue/green, linear, or canary deployments with VPC Lattice, specify the following configuration. 

Replace the `user-input` with your values. 

The key components in this configuration are:  
`roleArn`: The ARN of the infrastructure role that allows Amazon ECS to manage VPC Lattice resources. 
`targetGroupArn`: The ARN of one target group of the pair. 
`portName`: The name of the port mapping in your task definition that receives the traffic. 
`alternateTargetGroupArn`: The ARN of the other target group of the pair. 
`productionListenerRule`: The ARN of the listener rule for production traffic. 
`testListenerRule`: The ARN of the listener rule for test traffic. This is an optional parameter. 
`strategy`: Set to `BLUE_GREEN`, `LINEAR`, or `CANARY`. 
`bakeTimeInMinutes`: The duration when both service revisions are running simultaneously after production traffic has shifted. 
 

```
{
    "vpcLatticeConfigurations": [
        {
            "roleArn": "arn:aws:iam::111122223333:role/ecsInfrastructureRoleVpcLattice",
            "targetGroupArn": "arn:aws:vpc-lattice:region:111122223333:targetgroup/tg-0123456789abcdef0",
            "portName": "web",
            "advancedConfiguration": {
                "alternateTargetGroupArn": "arn:aws:vpc-lattice:region:111122223333:targetgroup/tg-0fedcba9876543210",
                "productionListenerRule": "arn:aws:vpc-lattice:region:111122223333:service/svc-0123456789abcdef0/listener/listener-0123456789abcdef0/rule/rule-0123456789abcdef0",
                "testListenerRule": "arn:aws:vpc-lattice:region:111122223333:service/svc-0123456789abcdef0/listener/listener-0123456789abcdef0/rule/rule-0fedcba9876543210"
            }
        }
    ],
    "deploymentController": {
        "type": "ECS"
    },
    "deploymentConfiguration": {
        "strategy": "BLUE_GREEN",
        "maximumPercent": 200,
        "minimumHealthyPercent": 100,
        "bakeTimeInMinutes": 5
    }
}
```
 

For more information about creating an Amazon ECS service that uses VPC Lattice, see Create a service that uses VPC Lattice. 

## Traffic flow during deployment 

During a deployment with VPC Lattice, traffic flows through the system as follows:  
Initial state: The production listener rule forwards all production traffic to the target group of the current (blue) service revision. 
Green service revision deployment: Amazon ECS registers the new tasks with the target group that isn't serving production traffic (the green target group), at weight `0`. 
Target propagation: Amazon ECS waits for the new targets to become healthy. 
Test traffic: If a test listener rule is configured, test traffic is routed to the green target group to validate the green service revision. 
Production traffic shift: Amazon ECS updates the production listener rule's weights. A blue/green deployment moves all traffic at once. A linear or canary deployment moves traffic incrementally. 
Bake time: The duration when both service revisions are running simultaneously after production traffic has shifted. 
Completion: After a successful deployment, Amazon ECS deregisters and stops the blue tasks. Both target groups remain attached to the listener rules, with the blue target group at weight `0`, ready for the next deployment. 
 

## Considerations  
Don't modify forward actions: After the initial setup, don't modify the forward actions of the production and test listener rules outside of Amazon ECS. If a listener rule is modified externally, for example if a rule forwards to both target groups or to neither of them when a deployment starts, the deployment would fail. 
Rollback behavior: When a deployment rolls back, whether triggered by Amazon CloudWatch alarms, the deployment circuit breaker, or a manual rollback, Amazon ECS reverts the listener rule weights to route all traffic back to the previous service revision and stops the new tasks. 
Switching from a rolling deployment: To switch an Amazon ECS service that uses VPC Lattice from a rolling deployment to a blue/green, linear, or canary deployment, add the `advancedConfiguration` block to provide the alternate target group and listener rules. You can do this in the same update that changes the strategy, or in an earlier update. The first progressive deployment shifts traffic to the other target group. 
Multiple configurations: Each VPC Lattice configuration on the service needs its own pair of target groups and its own production listener rule. Amazon ECS shifts each configuration's rules independently. 
Accounts: The VPC Lattice target groups, service, and listener rules must be in the same account as the Amazon ECS service.
