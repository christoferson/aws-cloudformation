> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gateway-connect-service.html
> Downloaded: 2026-10-21

# Connect Amazon ECS services to a gateway

You can connect an Amazon ECS service to a gateway by configuring a gateway connector when you create or update the service. A gateway connector identifies the named container port that receives traffic. You can also configure health checks and specify which gateway access types the service can use.

Amazon ECS connects the service to compatible gateways associated with its cluster. For each connection, Amazon ECS creates a gateway route and provides a unique HTTPS hostname. 

## Prerequisites 

Before you add a gateway connector to a service, make sure you have the following:  
A gateway is associated with your service's ECS cluster, and the association is ACTIVE. If no gateway is associated, Amazon ECS rejects the request, so you find out immediately instead of waiting for a service that deploys without a URL.
Your service has a task definition that uses `awsvpc` network mode and defines a named port on the container that should receive traffic. For more information, see Amazon ECS task networking options.
At least one gateway on the cluster is compatible with your service. A gateway is compatible when it is in the same VPC as your service's subnets, matches your access type filter, and covers every Availability Zone your service runs in.
 

## Connect a service to a gateway 

Add a gateway connector to the service and set `portName` to the container port in your task definition that should receive traffic. 

To connect a service to a gateway 

```
aws ecs update-service \
    --cluster my-cluster \
    --service my-service \
    --gateway-connectors '[{"portName": "web"}]'
```
 

During deployment, Amazon ECS selects the compatible gateways, provisions or reuses the required ingress infrastructure, creates the certificate, hostname, listener rules, and target groups, and creates a gateway route for each connection. Each route has its own HTTPS hostname. If more than one gateway is compatible, the service connects to all of them. A service has at most one gateway connector. 

## Customize a gateway connector 

The `portName` is required. It refers to a named port in your task definition. Amazon ECS uses that port's number, protocol, and protocol version to configure the target group. If the name does not match a port in the task definition your service uses, the request fails. Health check settings and an access type filter are optional. 

### Access type filter 

The `filters.accessTypes` narrows the gateways your service connects to. Set it to `PUBLIC`, `PRIVATE`, or both, and omit it to accept either. A `PUBLIC` gateway is reachable from the internet. A `PRIVATE` gateway is reachable only from a network that can reach its internal load balancer, so a request from the internet does not arrive. The filter controls gateway selection only. It does not configure traffic rules or security rules. 

To connect only to private gateways 

```
aws ecs update-service \
    --cluster my-cluster \
    --service my-service \
    --gateway-connectors '[{
        "portName": "web",
        "filters": { "accessTypes": ["PRIVATE"] }
    }]'
```
 

Narrowing the filter takes effect on the deployment it starts. Your service drops its connections to the gateways that no longer match, and their URLs stop working. Important

A service that should never be reachable from the internet must filter on `PRIVATE`. Without the filter, associating an internet-facing gateway with the cluster later exposes the service on its next deployment. 

### Health checks 

Amazon ECS configures health checks on the target group it creates for each gateway route, and forwards traffic only to targets that pass. By default, a gateway sends an HTTP request to `/` on the port that `portName` names, every 30 seconds, and expects a `200` response within 5 seconds. A service that answers `200` at `/` needs no health check configuration. 

Set a different path if `/` is slow or does real work, such as querying a database or rendering a full page. A health check repeats that work every 30 seconds for each target, and a slow response can exceed the health check timeout and mark a healthy target unhealthy. A lightweight endpoint such as `/health` avoids both. 

To set a health check path 

```
aws ecs update-service \
    --cluster my-cluster \
    --service my-service \
    --gateway-connectors '[{
        "portName": "web",
        "healthCheck": { "healthCheckPath": "/health" }
    }]'
```
 

For what each setting controls, see Health checks for Application Load Balancer target groups in the Application Load Balancers User Guide. Important

A health check change replaces the target group, so you cannot make one on a service that uses the `ROLLING` deployment strategy. The request fails with `Target group properties cannot be changed with ROLLING deployment strategy`. Use a `BLUE_GREEN` or `CANARY` deployment strategy on the service, or set the health check configuration when you first connect the service. 

## How Amazon ECS selects compatible gateways 

During a service deployment, Amazon ECS evaluates the gateways associated with the service's cluster, up to 5 per cluster, and narrows those candidates. It ignores the gateways that do not match rather than failing your deployment. 

Amazon ECS matches on three dimensions:  
|  Dimension |  How Amazon ECS determines eligibility |    
|  Access type |  The gateway matches the gateway connector's `filters.accessTypes`. If you omit the filter, both `PUBLIC` and `PRIVATE` gateways are eligible. |   
|  VPC |  The gateway is in the same VPC as your service's subnets. A gateway in another VPC is not eligible. |   
|  Availability Zone |  The gateway must have configured subnets in every Availability Zone used by the service's configured subnets. A gateway that overlaps with only some of the Availability Zones is not eligible. |    

Amazon ECS connects the service to every eligible gateway. An incompatible gateway does not by itself fail the deployment, if another associated gateway is eligible. If no eligible gateway remains, the request fails because the service cannot establish a gateway connection. 

Availability Zone coverage must be complete, not partial. A gateway reaches only the Availability Zones where it has subnets. A task that launches in an Availability Zone the gateway does not cover never passes its health checks, and Amazon ECS replaces it. Full Availability Zone coverage ensures tasks launched in any of the service's configured Availability Zones can register with healthy targets behind the connected gateway. 

For example, consider two gateways, Gateway 1 (GW1) and Gateway 2 (GW2), and a service (S1) in the same VPC:  
|  Resource |  Configured Availability Zones |  Eligible for service |    
|  GW1 |  `us-west-2a`, `us-west-2b`, `us-west-2c` |  Yes. It covers both of the service's Availability Zones. |   
|  GW2 |  `us-west-2a`, `us-west-2b` |  No. It does not cover `us-west-2c`. |   
|  S1 |  `us-west-2b`, `us-west-2c` |   |    

Assuming the access type filter also matches, Amazon ECS connects the service to Gateway 1 only. Gateway 1 covers both `us-west-2b` and `us-west-2c`, while Gateway 2 does not cover `us-west-2c`. Connecting the service to Gateway 2 can cause tasks launched in `us-west-2c` to fail load balancer health checks and be replaced. Important

A gateway connector does not select an individual gateway by name or ARN. The service connects to every gateway on the cluster that passes the three checks. A gateway spanning more Availability Zones than your service needs is the safer configuration. To connect a service to a particular gateway, configure that gateway to cover every Availability Zone where the service's tasks run. Coordinate changes to cluster associations with your platform team, because they can affect multiple services. 

## Understand service deployment 

Creating or updating a service with a gateway connector starts a deployment. Amazon ECS creates the gateway route and its service-specific resources during that deployment. The first connection to a gateway can take longer, because Amazon ECS might need to create a shared Application Load Balancer before it can create your service's resources. Later services reuse that load balancer, its listener, and its security group. 

When you update a gateway connector, or deploy the service after a cluster association changes, Amazon ECS reevaluates which gateways are eligible. The deployment establishes routes to newly eligible gateways and removes connections that no longer match. 

### How test traffic reaches a new revision 

During a progressive deployment, requests carrying the gateway's test traffic header and value reach the new service revision while everything else continues to reach the current one. The platform team sets that header on the gateway, not on your service, so every service behind the gateway uses the same one. Ask them what it is. 

A change to the header reaches your service only on its next deployment, so your service can still be matching a previous header. For more information, see Configure test traffic rules. 

## Verify the connection and find the service URL 

Each eligible gateway produces a separate connection and its own HTTPS hostname. These connections belong to a service revision, so one call returns every connection on the revision you name, along with each connection's URL, access type, and status. During a deployment, more than one revision exists, and each one carries its own connections. 

You get a revision ARN from the service's deployment. `describe-service-deployments` returns the ARN of the revision that a deployment is moving to, under `targetServiceRevision.arn`. For more information, see Viewing Amazon ECS service revision details. 

To verify a connection and get the service URL 

```
aws ecs describe-service-revisions \
    --service-revision-arns arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1234567890123456789 \
    --query 'serviceRevisions[0].ecsManagedResources.gatewayConnections'
```
 

Each connection carries `serviceUrl`, the HTTPS hostname to send traffic to, alongside `accessType`, which tells you how far that hostname reaches, and `status`. A hostname takes the form `https://<unique-id>.ecs.<region>.on.aws`. The domain varies by AWS partition. The hostname's identifier is random. It is not derived from your service name, so a service that you delete and recreate under the same name gets a different URL. 

Read `status` on every connection, and wait until a connection reports `ACTIVE` before you direct client traffic to its URL. `status` reports `CREATE_IN_PROGRESS` while Amazon ECS provisions and `ACTIVE` once that connection is ready, so run the command again until the connections you need report `ACTIVE`. A service connected to two gateways has two connections to check. A connection that reports `CREATE_FAILED` means provisioning failed rather than that it is still running, and waiting longer will not change it. For more information, see The service hostname does not respond. 

Gateway settings appear in `DescribeServiceRevisions`, because connectors change between deployments and a revision records what was configured when it deployed. For route status, resource inspection, and walking a route through every resource in its path, see Monitor gateway routes. 

## Migrate a service 

To migrate a service that already has its own load balancer, add a gateway connector to it. Amazon ECS provisions a gateway route and a new hostname, and it neither removes nor modifies your existing load balancer configuration. Both ingress paths serve traffic at once, so you can validate the gateway URL before you remove your own load balancer in a later update. 

To move a service from one gateway to another, coordinate with your platform team. Because the connector does not specify a gateway ARN, a migration is controlled through cluster associations and access type filters. That is also why a setting that is fixed on a gateway, such as its scheme, subnets, listener port, or protocol, cannot be changed in place, and creating a replacement gateway and moving services to it is the only way to get a different value.  
Create and associate the destination gateway. Confirm that its access type and VPC match the service, and that its subnets cover every Availability Zone the service's tasks run in. A gateway that covers only some of them is not eligible and the service will not connect to it.
Redeploy the service so that it connects to the destination gateway. If the original gateway remains eligible, both routes can coexist during the transition.
Confirm that the service's connection to the destination gateway reports `ACTIVE`, then update the clients that address the old hostname.
Have the platform team disassociate the old gateway when it is no longer needed. Redeploy affected services to remove the old routes.
 Important

Disassociating a gateway affects all services using that cluster association. Plan the change with other application teams. The old generated hostname stops working after its gateway route is removed. 

## Disconnect a service from gateways 

To disconnect a service from all gateways 

```
aws ecs update-service \
    --cluster my-cluster \
    --service my-service \
    --gateway-connectors '[]'
```
 

To keep only certain gateway access types, update `filters.accessTypes` instead. During the next deployment, Amazon ECS removes the routes for gateways that no longer match. You cannot use an access type filter to remove one specific gateway while retaining another eligible gateway of the same access type. 

When a service disconnects, Amazon ECS removes its gateway routes and service-specific ingress resources. The gateway and its cluster associations remain available to other services. Deleting a connected Amazon ECS service also removes its gateway connections. If no services remain on a managed load balancer, Amazon ECS removes that load balancer. A cluster association remains in the `DISASSOCIATING` state until every gateway route on that cluster is removed, and Amazon ECS then removes the association. For more information, see Disassociate a gateway from a cluster. 

Disconnecting takes effect on the deployment it starts, so the service keeps serving traffic through the gateway until that deployment finishes. Important

Removing the gateway connector makes the service inaccessible through its gateway hostnames after the corresponding routes are removed. Ensure that the service has another ingress path if it must remain accessible.
