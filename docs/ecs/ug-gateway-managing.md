> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gateway-managing.html
> Downloaded: 2026-10-21

# Create and manage an Amazon ECS Gateway

An Amazon ECS Gateway is an account-level resource that holds the ingress configuration and security standards that connected services inherit. The platform team creates gateways, configures networking policies, and associates them with target Amazon ECS clusters. Application teams then opt in their services and the services then connect to the compatible gateways on the cluster. For more information, see Connect Amazon ECS services to a gateway.

Creating a gateway does not immediately provision infrastructure. Amazon ECS provisions the first Application Load Balancer only when the first service connects to an associated gateway. 

## Prerequisites 

Before you create a gateway, ensure that you have the following:  
An infrastructure IAM role that Amazon ECS can assume to provision and manage ingress resources.
A default VPC in the AWS Region where you create the gateway. If you do not have a default VPC, you can specify your own subnets when creating the gateway.
 

### Infrastructure IAM role for Amazon ECS Gateway 

Amazon ECS requires an infrastructure role to create, configure, and manage load balancers, listeners, target groups, security groups, and AWS Certificate Manager certificates in your account. 

Create an IAM role with a trust policy that allows the `ecs.amazonaws.com` service principal to assume it, and attach the AWS managed policy `AmazonECSInfrastructureRoleForGatewayHostSharedALB`. You can see the permissions that this policy grants in the AWS Managed Policy Reference. 

```
aws iam create-role \
    --role-name ecsInfrastructureRoleForGateways \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ecs.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'

aws iam attach-role-policy \
    --role-name ecsInfrastructureRoleForGateways \
    --policy-arn arn:aws:iam::aws:policy/AmazonECSInfrastructureRoleForGatewayHostSharedALB
```
 

The IAM user or role that creates or updates a gateway must have permission to pass the infrastructure role to Amazon ECS. The following policy scopes `iam:PassRole` to that specific infrastructure role rather than granting it broadly. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForGateways"
        }
    ]
}
```
 

An application team needs neither `iam:PassRole` nor the gateway operations to give its service an HTTPS endpoint. The team does not need permission to create load balancers either, because those permissions live in the infrastructure role. Note

IAM roles are eventually consistent, so a newly created role might not be usable immediately. Right after you create these roles, your first `create-gateway` call can fail with an error such as `The infrastructureRoleArn could not be assumed. Verify the role exists and its trust policy allows ECS to assume it.` Wait a short time (about a minute) for the role to propagate, and then retry the command. Important

Amazon ECS tags all resources it creates with `AmazonECSManaged=true`. If you modify or remove this tag from a managed Application Load Balancer, security group, or listener rule, Amazon ECS can no longer update or clean up that resource. 

## Create a gateway 

When creating a gateway, you must specify a unique name, the infrastructure role ARN, and the `hostSharedAlb` configuration object. A `hostSharedAlb` gateway shares Application Load Balancers across services and uses host-based routing to direct incoming traffic to connected ECS services. Every setting inside the configuration is optional, so `--configuration '{"hostSharedAlb": {}}'` creates a gateway that uses default values. `CreateGateway` is a synchronous operation: it returns a status of `ACTIVE`, and Amazon ECS provisions no infrastructure until the first service connects. 

To create a gateway 

```
aws ecs create-gateway \
    --name my-gateway \
    --infrastructure-role-arn arn:aws:iam::123456789012:role/ecsInfrastructureRoleForGateways \
    --configuration '{
        "hostSharedAlb": {
            "scheme": "internet-facing",
            "networkConfiguration": {
                "subnets": ["subnet-abc123", "subnet-def456"]
            }
        }
    }'
```
 

Output: 

```
{
    "gatewayArn": "arn:aws:ecs:us-west-2:123456789012:gateway/my-gateway/a1b2c3d4",
    "name": "my-gateway",
    "status": "ACTIVE"
}
```
 

To confirm the gateway and read its configuration back, run `aws ecs describe-gateway --gateway my-gateway`. For more information, see View gateway status. 

### Customizing a gateway 

Amazon ECS selects a default for every setting you do not provide. To customize a gateway, set the optional fields inside the configuration. 

Where a setting has an equivalent in Elastic Load Balancing, the field names and values match the Elastic Load Balancing API. 

A gateway listener uses `HTTPS` on port 443. No other protocol or port is supported. 

The following settings are immutable once a gateway is created. To change an immutable setting, you must create a new gateway, update your services to connect to it, and delete the previous gateway.  
Name. The name must be unique in your account and can be up to 255 characters.
Subnets. Specify the subnets that the load balancers use. The default is the subnets of your default VPC. A gateway's subnets determine which VPC and which Availability Zones it covers. A service connects only to gateways that cover the VPC and Availability Zones it runs in, so your choice decides which services can use the gateway. If your service does not run in your default VPC, set subnets when you create the gateway.
IP address type. Choose `ipv4`, `dualstack`, or `dualstack-without-public-ipv4`. The default is `dualstack`.
Scheme. Choose `internet-facing` or `internal`. The default is `internet-facing`. Amazon ECS derives the gateway's access type from the scheme, so `internet-facing` gives an access type of `PUBLIC` and `internal` gives `PRIVATE`. A service connects only to gateways whose access type it accepts. For more information, see Connect Amazon ECS services to a gateway.
 

You can change the following settings at any time.  
Inbound security group. Supply a security group if you want to control inbound traffic to the load balancers yourself. Otherwise, Amazon ECS creates one and manages its inbound rules.
Maximum load balancer count. Enter the number of Application Load Balancers that the gateway can manage. The default is 10.
AWS WAF web ACL. Enter the ARN of a web ACL to associate with every load balancer that the gateway manages. There is no default.
HTTP desync mitigation mode. Choose `monitor`, `defensive`, or `strictest`. The default is `defensive`.
Access logs. Access logs are disabled by default. To enable them, supply an Amazon S3 bucket that you own.
Test traffic rules. Enter the header that routes test traffic to a new service revision. There is no default. A change applies to each service on that service's next deployment.
Deletion protection. Deletion protection is enabled by default, and the gateway propagates it to the load balancers that it manages. You cannot delete the gateway until you disable it.
Tag propagation. The gateway applies its tags to the infrastructure that it manages. To keep your tags on the gateway only, set tag propagation to `NONE`.
 

## Associate a gateway with Amazon ECS clusters 

A cluster's services can use a gateway only after you associate the gateway with their cluster. A gateway and the clusters it serves must be in the same AWS Region and account. Associating a gateway does not route any traffic on its own. It does not change how existing services receive traffic. Services in this cluster opt in separately, and start using the gateway on their next deployment. 

To associate a gateway with a cluster 

```
aws ecs associate-gateway-with-cluster \
    --gateway my-gateway \
    --cluster my-cluster
```
 

Associations are many-to-many. You can associate a gateway with up to 10,000 clusters, and a cluster with up to 5 gateways. You manage associations only through `AssociateGatewayWithCluster` and `DisassociateGatewayFromCluster`. 

When a service with a gateway connector is deployed, Amazon ECS evaluates the gateways associated with its cluster. The service connects to compatible gateways based on its access type, VPC, and Availability Zones. Plan subnet coverage carefully, because it decides a gateway's reach. A gateway serves only the services in the VPC and Availability Zones that its subnets cover. Narrow coverage leaves the rest of the services in the cluster unable to use it. For more information, see How Amazon ECS selects compatible gateways. Note

When you associate a gateway with a cluster, existing services are not affected until their next deployment. Adding another gateway to a cluster does not automatically connect services that are already running. 

To list a gateway's cluster associations 

```
aws ecs list-gateway-cluster-associations --gateway my-gateway
```
 

The response includes the gateway ARN, cluster ARN, and association status. An association can have the following statuses:  
`ACTIVE`: The gateway is associated with the cluster
`DISASSOCIATING`: The association is being removed. Existing gateway routes can continue serving traffic until they are removed.
 

These are association statuses, not gateway statuses. A gateway has its own set of statuses. You can filter this list by gateway, by cluster, or by status. Pass `--cluster` to see which gateways a cluster has, or filter by status to find every association that is still `DISASSOCIATING`. This is how you check whether a disassociation is pending before you delete a gateway. The results are paginated, 100 per page by default. 

## Update a gateway 

Updating a gateway changes the settings that every connected service inherits, including the services and infrastructure already behind it. Some settings cannot be changed after you create a gateway. Customizing a gateway describes the available settings and identifies those you cannot change. Important

`UpdateGateway` replaces the gateway's configuration with the one in your request. Omitting a setting clears it rather than leaving it unchanged. Before you update, run `describe-gateway` to retrieve the current configuration, and include every setting you want to keep in the request, not only the one you are changing. 

Step 1: Get the current configuration 

```
aws ecs describe-gateway --gateway my-gateway
```
 

```
{
    "gateway": {
        "gatewayArn": "arn:aws:ecs:us-west-2:123456789012:gateway/my-gateway/a1b2c3d4",
        "name": "my-gateway",
        "status": "ACTIVE",
        "accessType": "PUBLIC",
        "deletionProtection": true,
        "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForGateways",
        "propagateTags": "GATEWAY",
        "configuration": {
            "hostSharedAlb": {
                "scheme": "internet-facing",
                "protocol": "HTTPS",
                "port": 443,
                "maxAlbCount": 10,
                "currentAlbCount": 2,
                "httpDesync": "monitor",
                "networkConfiguration": {
                    "subnets": ["subnet-abc123", "subnet-def456"],
                    "ipAddressType": "dualstack"
                }
            }
        },
        "tags": [],
        "createdAt": 1760000000.0,
        "updatedAt": 1760400000.0
    }
}
```
 

Step 2: Choose the settings to include 

Specify the new value for the setting you are changing, and include every other setting with its current value. Amazon ECS does not preserve a setting you leave out. The following table shows where each setting goes and what happens if you leave it out.  
|  Setting |  Where to pass it |  If you omit it |    
|  `infrastructureRoleArn` |  Top level |  The request fails (required) |   
|  `configuration.hostSharedAlb` |  Top level |  The request fails (required) |   
|  `deletionProtection` |  Top level |  Reset to `true` |   
|  `propagateTags` |  Top level |  Reset to `GATEWAY` |   
|  `networkConfiguration.inboundSecurityGroup` |  `hostSharedAlb` |  Removed. Amazon ECS resumes managing inbound rules |   
|  `webACLArn` |  `hostSharedAlb` |  Removed. The web ACL is disassociated |   
|  `httpDesync` |  `hostSharedAlb` |  Reset to `defensive` |   
|  `accessLogs` |  `hostSharedAlb` |  Removed. Access logging is turned off |   
|  `testTrafficRules` |  `hostSharedAlb` |  Removed |   
|  `maxAlbCount` |  `hostSharedAlb` |  Reset to `10` |    

The gateway's `name`, `scheme`, `protocol`, `port`, `subnets`, and `ipAddressType` are fixed when you create a gateway and cannot be changed. `currentAlbCount` is a value Amazon ECS reports rather than a setting. Leave all of these out of the request. Note

The infrastructure role is required in every `UpdateGateway` request. A request without it returns a validation error. If you omit deletion protection or tag propagation, Amazon ECS resets them to their default values. 

Step 3: Update the gateway 

This example changes `maxAlbCount` from `10` to `25`. It also includes `httpDesync`, which is not changing. Omitting it would return the gateway to the default of `defensive`. 

```
aws ecs update-gateway \
    --gateway my-gateway \
    --infrastructure-role-arn arn:aws:iam::123456789012:role/ecsInfrastructureRoleForGateways \
    --configuration '{
        "hostSharedAlb": {
            "maxAlbCount": 25,
            "httpDesync": "monitor"
        }
    }'
```
 

Immutable settings describe infrastructure that Amazon ECS cannot rebuild without interrupting traffic. To change an immutable setting, create a new gateway with the configuration you want, associate it with the cluster, move services to it, and then disassociate and delete the old gateway. 

When you modify mutable parameters with `UpdateGateway`, Amazon ECS applies the changes across all load balancers managed by the gateway asynchronously. Changes to shared infrastructure take effect as the update runs. The gateway enters `UPDATE_IN_PROGRESS`. Amazon ECS performs rolling updates to all active ALBs. When updates complete, the status becomes `UPDATE_COMPLETE`. 

If an update cannot be applied to one or more load balancers (such as an invalid WAF ARN or missing IAM permissions), the gateway status changes to `UPDATE_FAILED`. Use `describe-gateway` to inspect the failure. 

To check the progress of an update 

```
aws ecs describe-gateway \
    --gateway my-gateway \
    --query 'gateway.{name:name,status:status}'
```
 Note

While a gateway is updating, its load balancers hold a mix of the old and the new configuration, because Amazon ECS has applied the change to some of them and not yet to others. Repeat the command until the status changes. 

An update can succeed for some load balancers and fail for others. Amazon ECS makes a best effort to update every resource rather than stopping at the first failure. A gateway that reports `UPDATE_FAILED` explains the status in `statusReason`. In `failures`, it records each resource it could not update, and why. Each entry names the resource that failed and the operations, error codes, and messages associated with each failure. A gateway records failures for up to 200 resources, with up to 5 errors each. Resolve the underlying issue, such as missing IAM permissions or an externally modified resource and retry the `update-gateway` operation. 

For a gateway's full description, including its configuration and the number of load balancers it currently has, see View gateway status. Important

Until an update reports `UPDATE_COMPLETE`, do not assume that all managed resources have the requested configuration. 

The following sections describe the settings you can change. Each shows only its own configuration. Add it to the configuration you retrieved in Step 1, and include the infrastructure role in the request. 

### Control inbound traffic 

By default, Amazon ECS creates a security group for the gateway's load balancers and allows inbound HTTPS traffic from all IP addresses on port 443. To control inbound traffic yourself, provide your own security group. Amazon ECS attaches the specified security group to the load balancers, removes the existing inbound rules it previously managed, and stops managing inbound rules. Important

Before specifying an inbound security group, ensure that it allows the required traffic for your services. Otherwise, existing services connected to the gateway might become unreachable. 

To provide your own inbound security group 

```
"networkConfiguration": {
    "inboundSecurityGroup": "sg-085c0f8be53138a08"
}
```
 

The load balancers are shared, so changes to inbound security group rules can affect every service using those load balancers. The inbound security group is the only network configuration setting you can change after you create a gateway. The subnets and IP address type cannot be changed. 

### Associate an AWS WAF web ACL 

Amazon ECS applies the web ACL to every load balancer the gateway manages. The web ACL then protects every service behind the gateway without each team configuring it. The web ACL must be a regional web ACL in the same AWS Region as the gateway. 

To associate a web ACL 

```
"webACLArn": "arn:aws:wafv2:us-west-2:123456789012:regional/webacl/my-waf/a1b2c3d4"
```
 

### Set the HTTP desync mitigation mode 

By default, load balancers use `defensive` mode, which protects against most request smuggling while allowing requests that do not strictly conform to HTTP. Use `strictest` to reject any non-conforming request, or `monitor` to allow all requests and record which ones it would have blocked. 

If you are considering `strictest`, start with `monitor` so that you can see what it would reject before it rejects anything. To review the results, enable access logs. 

To set the desync mitigation mode 

```
"httpDesync": "strictest"
```
 

### Enable access logs 

Access logs are disabled until you provide an Amazon S3 bucket. Amazon ECS does not create a bucket for you, and no separate setting turns logging on. Supplying a bucket enables access logs. 

To enable access logs 

```
"accessLogs": {
    "destination": {
        "s3": { "bucket": "my-gateway-logs", "prefix": "alb" }
    }
}
```
 

The bucket must be in the same AWS Region as the gateway, and its bucket policy must allow Elastic Load Balancing to write to it. The infrastructure role is not involved in these writes, so granting it Amazon S3 permissions has no effect. Because the load balancers are shared, one bucket receives logs for every service on the gateway. Use the hostname in each log record to identify which service a request went to. 

### Configure test traffic rules 

During a progressive deployment, a new service revision needs to receive traffic before production traffic shifts to it. Test traffic rules identify the requests that reach the new revision. 

You configure these rules on the gateway rather than on individual services, so every service behind the gateway uses the same rule. Amazon ECS matches requests by header, and you must provide both the header name and at least one value. 

To configure test traffic rules 

```
"testTrafficRules": {
    "header": { "name": "x-test-traffic", "values": ["canary"] }
}
```
 

A request carrying `x-test-traffic: canary` reaches the new revision during a deployment. All other requests reach the production revision. Header matching is the only mechanism. You cannot send a percentage of traffic to the new revision. 

Outside a deployment, no new revision exists, so a request carrying the test header reaches the production revision like any other request. Important

A change to test traffic rules does not apply to running services when you make it. It applies to each service on that service's next deployment. 

Amazon ECS does not rewrite an existing rule's match conditions. Changing the header creates a new rule for the new revision. A deployment that fails removes only the rule it created and leaves the rule serving the current revision unchanged. As a result, a gateway can have some services matching an old test header and others matching the new one until each service redeploys. Application teams must redeploy their services to pick up a new header. Amazon ECS does not redeploy those services, so coordinate a header change with the service owners. 

### Set the maximum load balancer count 

`maxAlbCount` limits how many Application Load Balancers the gateway can create. The default is 10. 

To raise the maximum load balancer count 

```
"maxAlbCount": 50
```
 

Two separate limits decide how many services a gateway can serve.  
Services per load balancer. A `hostSharedAlb` gateway places up to 25 services on one Application Load Balancer. This is a fixed property of the Application Load Balancer with host-based routing and you cannot change it.
Load balancers per gateway. `maxAlbCount` is the ceiling you set on how many load balancers the gateway can create. The default is 10.
 

Amazon ECS fills a load balancer to 25 services, then provisions another, up to `maxAlbCount`. When the last service leaves a load balancer, Amazon ECS removes it. Together, the two limits cap a gateway at 25 x `maxAlbCount` services, or 250 at the default. 

Raise the maximum before you need it. If a service opts in when every load balancer is full and the gateway is at its maximum, Amazon ECS cannot provision ingress for that service. The failure happens during that service's deployment. Raising the maximum afterward does not retry the deployment that failed, so the service owner must deploy the service again. 

To see how many load balancers a gateway has against its maximum, describe the gateway and compare `currentAlbCount` with `maxAlbCount`. To see the load balancers themselves and the gateway routes on each, see Inspect managed infrastructure (platform view). 

## Disassociate a gateway from a cluster 

Disassociate a gateway from a cluster when you no longer want services in that cluster to connect to the gateway. Disassociating prevents new service connections through that association. It does not remove existing service connections immediately. Important

Before you disassociate a gateway, verify that the affected services have an alternative ingress path if they must remain accessible. Removing gateway routes can make services unreachable through that gateway. 

To disassociate a gateway from a cluster 

```
aws ecs disassociate-gateway-from-cluster \
    --gateway my-gateway \
    --cluster my-cluster
```
 

The association enters the `DISASSOCIATING` state. While the association is in `DISASSOCIATING` state:  
New services cannot connect to the gateway through the cluster.
Existing services continue receiving traffic through their gateway routes.
Services disconnect from the gateway when they are updated or redeployed.
The association remains `DISASSOCIATING` until all gateway routes have been removed.
 

Amazon ECS does not automatically redeploy services when a gateway is disassociated from their cluster. Application teams must update or redeploy their services to disconnect from the disassociating gateway. If no other gateways are available on the cluster, remove the gateway connector before redeploying the service. When the last gateway route is removed, Amazon ECS removes the association. 

### View gateway routes that prevent disassociation 

Use the `list-gateway-routes` command to identify services that still have gateway routes associated with the cluster. 

To find the gateway routes blocking a disassociation 

```
aws ecs list-gateway-routes --gateway my-gateway --cluster my-cluster
```
 

The response identifies the gateway routes that are still connected. If routes remain, update or redeploy the affected services to disconnect them from the disassociating gateway. 

Besides gateway and cluster, you can filter routes by service, by container port name, and by status. Filtering by status finds routes that are stuck rather than still in use. A route ARN leads to `DescribeGatewayRoute`, which reports the hostname and the service-specific infrastructure for that one connection. For more information, see Monitor a gateway. Note

Filtering by a service name alone is not allowed, because service names are unique only within a cluster. Pass either a full service ARN or a service name together with its cluster. 

### Cancel a gateway disassociation 

While an association is in the `DISASSOCIATING` state, you can reactivate it. Associate the gateway with the same cluster again, and Amazon ECS returns the association to `ACTIVE`. 

To reactivate an association 

```
aws ecs associate-gateway-with-cluster \
    --gateway my-gateway \
    --cluster my-cluster
```
 

What a service keeps depends on whether it redeployed while the association was disassociating.  
Services that have not redeployed keep their existing gateway routes and DNS hostnames, and continue serving traffic without interruption.
Services that redeployed while the association was disassociating lost their gateway routes. Each one needs another deployment to receive a route again, and that route carries a new DNS hostname.
 

After a disassociation completes, the association is permanently gone and cannot be reactivated. If the original association has already been fully removed, to use the same gateway with that cluster again, create a new association. Previously connected services receive new gateway routes, with new DNS hostnames, on their next deployment. 

## Delete a gateway 

You can delete a gateway when it is no longer needed. Before you delete a gateway, the following conditions must be met:  
Deletion protection is disabled.
The gateway has no cluster associations in the `ACTIVE` or `DISASSOCIATING` state.
 

Step 1: Disable deletion protection 

Deletion protection is enabled by default, so make sure that it is disabled before you continue. 

```
aws ecs update-gateway --gateway my-gateway --no-deletion-protection
```
 

Step 2: Disassociate the gateway from each of its clusters 

Run the following command for each associated cluster. 

```
aws ecs disassociate-gateway-from-cluster \
    --gateway my-gateway \
    --cluster my-cluster
```
 

Each association stays in `DISASSOCIATING` until every gateway route for that gateway in the cluster is removed. Amazon ECS removes a route only when the service that owns it is redeployed or deleted, and it does not redeploy services for you. Coordinate with the service owners to redeploy each service. 

To find the routes that are holding an association open, run the following command. 

```
aws ecs list-gateway-routes --gateway my-gateway --cluster my-cluster
```
 

Step 3: Confirm that no associations remain 

Amazon ECS removes an association after its last route is gone. When the list is empty, you can delete the gateway. 

```
aws ecs list-gateway-cluster-associations --gateway my-gateway
```
 

Step 4: Delete the gateway 

```
aws ecs delete-gateway --gateway my-gateway
```
 

The `DeleteGateway` operation is synchronous. When the operation succeeds, Amazon ECS returns the gateway information with a status of `DELETED`, and subsequent requests for the gateway return a `GatewayNotFoundException`. If the prerequisites are not met, the operation fails. 

Nothing remains to clean up. Amazon ECS removes a service's gateway route and its resources when the service disconnects, and removes a load balancer when its last service leaves.
