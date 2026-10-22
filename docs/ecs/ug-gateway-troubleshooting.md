> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gateway-troubleshooting.html
> Downloaded: 2026-10-21

# Troubleshoot a gateway

Use this topic to troubleshoot issues with Amazon ECS Gateway, including service connection failures, gateway route provisioning failures, gateway configuration updates, and connectivity issues.

Amazon ECS gateways, gateway routes, and application targets report their status independently. A gateway can remain `ACTIVE` even when a gateway route fails to provision, and a gateway route can be `ACTIVE` even when its application targets are unhealthy. To identify the cause of a failure, review the error returned by the API operation or inspect the status and failure details of the affected gateway or gateway route.

Before investigating further, verify that you are using the correct resource name or ARN, AWS account, and Region. Ensure that Amazon ECS Gateway is supported in your Region and that you have the required permissions. For service connection issues, verify that the service's task definition uses the `awsvpc` network mode.

If the issue persists, use the following troubleshooting procedures to identify and resolve the failure. 

## Service connection and deployment failures 

### No gateways are associated with the cluster 

A `CreateService` or `UpdateService` request that includes a gateway connector fails when no gateways are associated with the service's cluster. Amazon ECS reports `gatewayConnectors were specified but no gateways are associated with cluster` and rejects the request rather than deploying a service it cannot give a URL. Check the cluster's gateway associations to verify that at least one gateway is associated with the service's cluster. 

```
aws ecs list-gateway-cluster-associations \
    --cluster my-cluster
```
 

If no association is available, contact your platform team to associate a gateway before you deploy the service with a connector. A gateway whose association has entered `DISASSOCIATING` is not available for new connections. You also see this error after the platform team deletes the last gateway on your cluster. Remove the connector from your service, or wait for a replacement gateway, before your next update. 

### No compatible gateway matches the service 

Amazon ECS evaluates the gateways associated with the cluster and connects the service to every gateway that meets all of the following conditions:  
Access type. The gateway's access type matches the `filters.accessTypes` setting in the service's gateway connector. If you omit this filter, both `PUBLIC` and `PRIVATE` gateways are eligible. 
VPC. The gateway and the service are in the same VPC. 
Availability Zones. The gateway covers all Availability Zones used by the service's configured subnets. The subnet IDs themselves do not need to match, but the gateway must have subnet coverage in every Availability Zone the service uses. 
 

A gateway that does not meet these conditions is excluded. If at least one compatible gateway is available, the service connects to it. If no compatible gateways are available, the request fails. Amazon ECS reports `has associated gateways but none are in the service's VPC` when no associated gateway is in the service's VPC, and `none of the gateways associated with cluster match` when the access type filter excludes every remaining gateway. 

To identify and resolve a compatibility mismatch  
Check the service's access type filter. Verify that `filters.accessTypes` matches the access type of the gateway you want to connect to. 
Retrieve the service's configured subnets. Use `list-service-deployments` to identify the relevant service revision ARN. 

```
aws ecs list-service-deployments \
    --cluster my-cluster \
    --service my-service \
    --query 'serviceDeployments[].targetServiceRevisionArn'
```
 

Then use `describe-service-revisions` to retrieve its configured subnets. 

```
aws ecs describe-service-revisions \
    --service-revision-arns <service-revision-arn> \
    --query 'serviceRevisions[0].networkConfiguration.awsvpcConfiguration.subnets'
```
Retrieve the gateway's configured subnets. Use `describe-gateway` to view the gateway's networking configuration. 

```
aws ecs describe-gateway \
    --gateway my-gateway
```
Compare the VPCs and Availability Zones. Use `describe-subnets` to retrieve the VPC ID and Availability Zone for the service and gateway subnets. 

```
aws ec2 describe-subnets \
    --subnet-ids <subnet-ids> \
    --query 'Subnets[].{SubnetId:SubnetId,VpcId:VpcId,AvailabilityZone:AvailabilityZone}'
```
 

Verify that the service and gateway are in the same VPC and that the gateway covers all Availability Zones used by the service. 
Resolve the mismatch. Update the service's access type filter or subnet configuration as appropriate. If no compatible gateway is available, contact your platform team to configure or associate a gateway that matches the service's access type, VPC, and Availability Zone requirements. 
 

After resolving the mismatch, retry the service creation or update. Note

For greater flexibility when connecting ECS services, configure gateways with subnets that cover all Availability Zones where your services might run. Broader Availability Zone coverage allows a gateway to support more services and reduces the need to create additional gateways. Gateway subnets cannot be changed after creation. 

### Gateway connector references an invalid container port 

A gateway connector's `portName` must match the name of a port mapping in the service's task definition. It is the name of the port, not the numeric container port. When no container in the task definition has a port mapping with that name, Amazon ECS reports `InvalidConfiguration: "portName not found in task definition portMappings"`. To inspect the named port mappings, run: 

```
aws ecs describe-task-definition \
    --task-definition my-task-definition:1 \
    --query 'taskDefinition.containerDefinitions[].portMappings[].name'
```
 

Correct the connector or the task definition so the names match, and then retry the service operation. Check this again after you update a task definition, because a previously valid port name might no longer exist. 

### Updating health checks fails with the ROLLING deployment strategy 

Updating a gateway connector's health check settings returns an error stating that target group properties cannot be changed with the `ROLLING` deployment strategy. Changing those settings requires a replacement target group, and a service that uses the `ROLLING` deployment strategy does not support that replacement during an update. 

Keep the existing health check settings, or use a blue/green or canary deployment strategy for the change. If you must disconnect and reconnect the service to replace the target group, plan for the removal and recreation of its gateway route and hostname. For connector configuration, see Connect Amazon ECS services to a gateway. 

## Gateway route provisioning failures 

A service connection can have a gateway route in `CREATE_FAILED` or `UPDATE_FAILED` state, or a service deployment can fail to finish provisioning ingress. A route level failure does not necessarily change the gateway's overall status or affect another service's existing route.  
Find the failed gateway routes. 

```
aws ecs list-gateway-routes \
    --gateway my-gateway \
    --status CREATE_FAILED UPDATE_FAILED
```
Identify the service that each failed route belongs to, and the resources the gateway created for it. 

```
aws ecs describe-gateway-route \
    --gateway-route-arn arn:aws:ecs:us-west-2:123456789012:gateway-route/my-gateway/a1b2c3d4/9f8e7d6c
```
Check the service's deployment status and service events for the failure reason. Determine from the reason whether certificate issuance, a listener rule, a target group, a security group, or another resource failed. 
Correct the underlying issue and retry the affected service deployment. A gateway configuration change does not necessarily restart a service deployment that already failed. 
 Note

A gateway route reports a failure status but not the reason for it. Amazon ECS records the reason on the service deployment that triggered the provisioning, and in the service's events. 

Common causes include insufficient infrastructure role permissions, load balancer capacity or service quotas, subnet IP exhaustion, and resources deleted or changed outside Amazon ECS. Two reasons you may see are `InsufficientAvailabilityZones`, which means the gateway's subnets are in fewer than two Availability Zones, the minimum for an Application Load Balancer, and `InvalidSubnet`, which means a configured subnet does not exist, belongs to a different VPC, or has no free IP addresses left. The sections that follow describe how to investigate the permission, capacity, and out-of-band conditions. For the monitoring procedures, see Monitor a gateway. 

For the permissions the `hostSharedAlb` gateway type requires, see AmazonECSInfrastructureRoleForGatewayHostSharedALB in the AWS Managed Policy Reference. 

## Capacity and quota issues 

For the quota values, see Gateway Service Limits. 

### The cluster has reached its gateway association limit 

A cluster can associate with at most 5 gateways. When it reaches that limit, Amazon ECS reports `Cluster has reached the maximum number of gateway associations (5)`. Disassociate a gateway the cluster no longer needs, which requires disconnecting the services still using it first. 

### The gateway has reached its maximum number of load balancers 

When a gateway's existing load balancers cannot accept another service connection, Amazon ECS provisions another load balancer until it reaches the gateway's `maxAlbCount` setting, which defaults to 10. A load balancer can serve up to 25 ECS services. When every load balancer is full and the gateway is at `maxAlbCount`, a new service's deployment fails. Check the `currentAlbCount` against `maxAlbCount` and inspect the managed resources: 

```
aws ecs describe-gateway --gateway my-gateway
aws ecs describe-gateway-resources --gateway my-gateway
```
 

If `maxAlbCount` is the limiting factor, increase it within the supported limit. For example: 

```
aws ecs update-gateway \
    --gateway my-gateway \
    --configuration '{"hostSharedAlb":{"maxAlbCount":25}}'
```
 

Wait for the gateway update to complete, and then redeploy the affected service. Increasing `maxAlbCount` does not automatically retry a failed service deployment. 

### An underlying AWS resource quota was reached 

The resources provisioned by ECS Gateway are subject to their owning services' quotas, including load balancers, target groups, listener rules, certificates, and security group rules. Provisioning can also fail if the configured subnets do not have enough available IP addresses. You may see the following reasons:  
`LoadBalancerQuotaExceeded` and `TargetGroupQuotaExceeded`, for the account's limits in the Region. 
`ResourceQuotaExceeded`, for a per load balancer limit such as listener rules or certificates. 
`CertificateQuotaExceeded`, for the account's certificate limit. 
`CertificateAnnualLimitExceeded`, for certificates requested in the last 365 days. Deleting certificates does not reduce this count, so this one needs a quota increase through AWS Support. 
`SecurityGroupCapacityExceeded` and `SecurityGroupRuleCapacityExceeded`, for security groups per VPC and rules per security group. 
`TestRuleLimitExceeded`, for test traffic rules on one service. 
`TagLimitExceeded`, for a combination of gateway tags and service tags that exceeds what a resource allows, or for tags an account tag policy rejects. Amazon ECS also applies its own `AmazonECSManaged` tag, which uses one slot. 
 

Use the failure reason to identify the constrained resource and then check the applicable service quota. Request a quota increase, release unused capacity, or use a supported alternative configuration, and then retry the service deployment. For Elastic Load Balancing limits, see Quotas for your Application Load Balancers. 

## IAM and permissions issues 

Gateway operations involve two different identities: the IAM principal that makes the API request, and the infrastructure IAM role that Amazon ECS assumes to manage AWS resources. A permission problem on one is not fixed by changing the other. 

### The caller cannot pass the infrastructure role 

`CreateGateway` and `UpdateGateway` fail with a permissions error that involves `iam:PassRole` when the caller cannot pass the role provided in `infrastructureRoleArn`. This is the most common first-run failure, because the call fails even when the caller is allowed to create gateways. Confirm that the caller has `iam:PassRole` permission on the exact role ARN in `infrastructureRoleArn`, and check permissions boundaries, service control policies, and explicit denies. Adding permissions to the infrastructure role does not resolve a missing permission on the calling identity. For IAM role setup, see Infrastructure IAM role for Amazon ECS Gateway. 

### Amazon ECS cannot assume the infrastructure role 

Amazon ECS could reach the role but could not assume it. Verify that the IAM role exists and that its trust policy permits `ecs.amazonaws.com` to call `sts:AssumeRole`. 

```
aws iam get-role --role-name ecsInfrastructureRoleForGateways
```
 

The role's trust policy must match the following. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAccessInfrastructureForECSGateways",
            "Effect": "Allow",
            "Principal": {
                "Service": "ecs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
 

If the role was just created or modified, allow time for the IAM change to propagate before you retry. A missing or incorrect trust relationship is not fixed by granting the caller `iam:PassRole` alone. Confirm as well that the role is in the same account and partition as the gateway. A related failure, `AWS STS is not activated for this account in a Region`, means AWS Security Token Service is not enabled for that Region. Activate it, and then retry. 

### The infrastructure role cannot manage a resource 

A gateway route or a gateway update reports an access denied error for an Elastic Load Balancing, Amazon EC2, or AWS Certificate Manager operation when the infrastructure role is missing a permission. Verify that the role has the permissions required by the gateway configuration. For the `hostSharedAlb` gateway type, check the attached AWS managed policy. 

```
aws iam list-attached-role-policies --role-name ecsInfrastructureRoleForGateways
```
 

Attach the `AmazonECSInfrastructureRoleForGatewayHostSharedALB` managed policy, or, if you replaced it with a policy of your own, compare that policy against the IAM action named in the failure. You can see the permissions that this policy grants in the AWS Managed Policy Reference. Check also whether a permissions boundary or another account restriction prevents the action. The exact failed operation and resource ARN are more useful than an undifferentiated `AccessDenied` message. 

## Service connectivity and target health 

### The service hostname does not respond 

When requests to a gateway-generated HTTPS hostname time out or fail, check the connection from the gateway route to the application.  
Check the gateway route status. Find the route for the service and confirm that it is `ACTIVE`. A route in `CREATE_IN_PROGRESS` has not finished provisioning, and a route in a `*_FAILED` state has a provisioning failure. Inspect the route failure before troubleshooting the application: 

```
aws ecs list-gateway-routes --cluster my-cluster --service my-service
```
Check gateway access. An internal gateway requires network connectivity to the internal load balancer. Verify that you are testing from a network that can reach it. 
Check target health. Get the target group ARN from the service's gateway connection, which `describe-service-revisions` returns, then inspect its registered targets. 

```
aws elbv2 describe-target-health \
    --target-group-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-service/0123456789abcdef
```
 

A target group can report unhealthy targets when the application returns an unexpected status code, times out, listens on a different port, or cannot be reached by the load balancer. The response includes each target's health state and, when relevant, a reason and description. For example, a reason of `Target.ResponseCodeMismatch` indicates that the response did not match the configured success code range. Check the health check path, the application response, and the target port before you modify any gateway infrastructure. For the health check reason codes, see Health checks for Application Load Balancer target groups. 

An `ACTIVE` gateway route means that ingress provisioning succeeded. It does not mean that the application targets are healthy. 
Check the security groups. Confirm that the load balancer's inbound security group allows traffic from the intended clients, and that the task security group allows traffic from the load balancer on the container port. When the platform team supplies the gateway's inbound security group, Amazon ECS does not manage its inbound rules. 
Check the application and traffic controls. Verify the container's listening port and health endpoint. If an AWS WAF web ACL is configured, check whether a rule is blocking the request. Use load balancer access logs and CloudWatch metrics to tell load balancer errors apart from application responses. 
 

## Gateway update failures 

`DescribeGateway` reports `UPDATE_FAILED` after a gateway configuration update that Amazon ECS could not apply to every load balancer. Amazon ECS applies an update to each managed load balancer in turn and makes a best effort to update them all rather than stopping at the first failure, so some load balancers might accept the change while others fail. Do not assume the update was rolled back across the gateway. Retrieve the status and the failure information. 

```
aws ecs describe-gateway --gateway my-gateway
```
 

Inspect `statusReason` and `failures` for the resources and operations that could not be updated. For example, an error for an invalid security group identifier points to the gateway's configured inbound security group, and an access denied error points to the permissions available to the infrastructure role. For how to read the `failures` list, see Locate failure details. Correct the reported cause and retry the requested update. Wait until the gateway reports a successful update before you assume every managed load balancer has the new configuration, and wait for the update to complete before retrying. Important

A partial gateway update can leave different load balancers with different configurations, which can change traffic or policy behavior for the services behind them. Treat the update as partially applied until the gateway reports `UPDATE_COMPLETE`, and validate the affected resources after recovery. 

## Disassociation and deletion issues 

### A cluster association remains DISASSOCIATING 

A gateway cluster association remains in `DISASSOCIATING` until all gateway routes associated with that cluster are removed. Amazon ECS does not automatically redeploy connected services or remove their existing routes when you disassociate a gateway. 

To identify the services that are still connected, use the following command: 

```
aws ecs list-gateway-routes --gateway my-gateway --cluster my-cluster
```
 

Coordinate with the application teams to update or redeploy the affected services so they disconnect from the gateway. When the last route is removed, the disassociation completes. 

### The gateway cannot be deleted 

A gateway cannot be deleted while deletion protection is enabled or while it has cluster associations in the `ACTIVE` or `DISASSOCIATING` state. Check the gateway's cluster associations and ensure that all remaining gateway routes are removed so disassociation can complete. After all associations are removed, make sure that deletion protection is disabled, and then retry deleting the gateway. For the complete procedure, see Delete a gateway. 

```
aws ecs update-gateway --gateway my-gateway --no-deletion-protection
aws ecs delete-gateway --gateway my-gateway
```
 

## Changes made outside Amazon ECS 

Amazon ECS does not automatically repair or recreate gateway-managed resources that are modified or deleted outside Amazon ECS. Modifying or deleting managed resources such as load balancers, listeners, listener rules, target groups, certificates, or security groups outside Amazon ECS can interrupt traffic or cause subsequent service deployments, gateway updates, or cleanup operations to fail. 

If a gateway-managed resource was modified or deleted outside Amazon ECS, take the following steps:  
Identify the affected resource: Use `describe-gateway-resources` or `describe-gateway-route` to identify the managed resources. Inspect their current configuration in the corresponding AWS service to identify missing or modified resources. A change made outside Amazon ECS can surface as one of the following failure reasons:  
`ManagedResourceDeleted`, when a resource Amazon ECS created for the service was deleted outside Amazon ECS. 
`ConflictingListener`, when a listener on the gateway's port exists on the load balancer and Amazon ECS did not create it. 
`SecurityGroupNameInUse`, when a security group with the name Amazon ECS wants exists and is not managed by Amazon ECS. Amazon ECS does not reconfigure or delete it. 
`InvalidSecurityGroup`, when the gateway's inbound security group no longer exists. 
Recover the affected service: If a resource was modified, restore its original configuration and redeploy the service. If a resource was deleted, remove the gateway connector from the service and deploy, then add the connector back and deploy again. The second deployment provisions fresh resources and a new gateway route. Because the service receives a new generated hostname, update any clients or DNS records that point at the old one. 
Verify connectivity: Confirm that the service's gateway route is `ACTIVE` and its targets are healthy before you redirect traffic to it. 
 Important

Do not modify or remove the `AmazonECSManaged` tag from gateway-managed resources. Amazon ECS uses it to identify the resources it manages, and without it Amazon ECS can no longer update or clean up that resource. Make supported configuration changes through Amazon ECS Gateway operations rather than modifying the underlying resources directly.
