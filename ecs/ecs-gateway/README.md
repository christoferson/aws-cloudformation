
## Amazon ECS Gateway (managed shared ALB ingress)

[ecs-gateway-fargate.yaml](ecs-gateway-fargate.yaml)

Amazon ECS Gateway (October 2026) moves ingress networking into ECS. You define the ingress settings **once on a gateway**: scheme, subnets, WAF, access logs and the test traffic header. Each service then opts in with a **gateway connector**. For every connected service, ECS provisions and manages the Application Load Balancers, the HTTPS listener, target groups, security groups, ACM certificates and a generated **HTTPS hostname**.

| Who | Resource | Purpose |
|---|---|---|
| Platform team | `AWS::ECS::Gateway` (`HostSharedAlb`) | Shared ALBs with host-based routing, plus the ingress policy |
| Platform team | `AWS::ECS::GatewayClusterAssociations` | Makes the gateway available to one cluster's services |
| Application team | `AWS::ECS::Service` → `GatewayConnectors` | Opts in. It names the container port, and can set an access type filter and a health check |

Application teams need no Elastic Load Balancing permissions. They don't write any listener, target group or certificate resources.

Offline docs: [../../docs/ecs/README.md](../../docs/ecs/README.md#developer-guide--ecs-gateway)

----------------------------------------------------------------------------------

## What the template creates

```
 IAM role (ecs.amazonaws.com) + AmazonECSInfrastructureRoleForGatewayHostSharedALB
   │
 ECS Gateway  <app>-<env>-gateway   HostSharedAlb: internet-facing, ipv4, HTTPS:443
   │            test traffic header x-ecs-test-traffic: true, MaxAlbCount 2
   │
 GatewayClusterAssociations ──► ECS cluster <app>-<env>-gateway
                                   ├─ service <app>-<env>-web  GatewayConnectors: PortName web, custom health check
                                   └─ service <app>-<env>-api  GatewayConnectors: PortName web, Filters.AccessTypes [PUBLIC]

 Managed by ECS (created when the first service connects; not in the stack):
   shared ALB + HTTPS:443 listener + ALB security group
   per service: certificate, hostname https://<id>.ecs.<region>.on.aws, listener rule, target group, service security group
```

Both services share one ALB (up to 25 services per ALB). Each one gets its own hostname and certificate.

## Concepts

- **Nothing is provisioned up front.** Creating or associating a gateway costs nothing until the first service connects. That first connect can take longer, because ECS creates the ALB first. Later services reuse the ALB, its listener and its security group.
- **A connector has no gateway name.** It connects to **every compatible gateway** associated with the cluster. A gateway is compatible when it is in the same VPC, covers every AZ the service uses, and matches `Filters.AccessTypes`. With no filter, both PUBLIC and PRIVATE gateways match. Use `AccessTypes: [PRIVATE]` for services that must never be internet-reachable. Otherwise, a public gateway associated with the cluster later would expose them. A service with two gateways gets two connections and two URLs.
- **Access type** is derived from the scheme: `internet-facing` → `PUBLIC`, `internal` → `PRIVATE`. It's available as `!GetAtt Gateway.AccessType`.
- **Named port.** `PortName` refers to `PortMappings[].Name` in the task definition, and ECS takes the port and protocol from that mapping.
- **Test traffic rules.** With `BLUE_GREEN`, `LINEAR` or `CANARY` deployments, requests that carry the header reach the new revision before production traffic moves. A header change reaches a service only on that service's next deployment.

## Constraints

| Item | Limit |
|---|---|
| Listener | HTTPS on 443 only |
| Services | `awsvpc` network mode only. Gateway and cluster in the same account. Service and gateway in the same VPC |
| AZs | The gateway subnets must cover every AZ the service runs in |
| Immutable | Name, type, scheme, port, protocol, subnets, IP address type. To change them, create a new gateway and move the services |
| Mutable | `InboundSecurityGroup`, `WebACLArn`, `AccessLogs`, `HttpDesync`, `MaxAlbCount`, `TestTrafficRules`, deletion protection, tags |
| Connectors | At most 1 per service. The association must be `ACTIVE` first (the template uses `DependsOn`) |
| Counts | 25 services per ALB. `MaxAlbCount` defaults to 10. Up to 5 gateways per cluster |
| Express Mode | Not compatible with ECS Express Mode services |

----------------------------------------------------------------------------------

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-ecs-gateway \
  --template-body file://ecs-gateway-fargate.yaml \
  --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx \
               ParameterKey=VpcCidr,ParameterValue=10.0.0.0/16 \
               ParameterKey=VpcSubnetList,ParameterValue='subnet-aaaa\,subnet-bbbb'
```

## Find the service URL

The hostname is not a CloudFormation output. It belongs to the **service revision**:

```bash
CLUSTER=myapp-dev-gateway
SERVICE=myapp-dev-web

REV=$(aws ecs describe-service-deployments \
  --service-deployment-arns $(aws ecs list-service-deployments --cluster $CLUSTER --service $SERVICE \
      --query 'serviceDeployments[0].serviceDeploymentArn' --output text) \
  --query 'serviceDeployments[0].targetServiceRevision.arn' --output text)

aws ecs describe-service-revisions --service-revision-arns $REV \
  --query 'serviceRevisions[0].ecsManagedResources.gatewayConnections'
# [ { "serviceUrl": "https://<id>.ecs.<region>.on.aws", "accessType": "PUBLIC", "status": "ACTIVE", ... } ]

curl -i https://<id>.ecs.<region>.on.aws/
curl -i -H "x-ecs-test-traffic: true" https://<id>.ecs.<region>.on.aws/   # new revision during a blue/green, linear or canary deployment
```

- **Wait for ACTIVE:** `status` is `CREATE_IN_PROGRESS` while ECS provisions the resources. Use the URL only once it's `ACTIVE`.
- **CREATE_FAILED:** means provisioning failed. Waiting longer won't help, so check the service events.
- **Random hostname:** the ID isn't derived from the service name, so deleting and recreating a service changes its URL.

## Notes

- **Deletion protection:** ECS enables it **by default** on a gateway and also sets it on the managed ALBs. The template sets it from `GatewayDeletionProtection`, which defaults to `false` so the demo stack can be deleted. Use `true` for shared or production gateways.
- **Task security group:** it must allow the load balancer on the container port. The managed ALB security group doesn't exist until the first service connects, so the template allows `VpcCidr`.
  - **ALB inbound rules:** ECS opens 443 to `0.0.0.0/0` on the ALB. Supply your own `InboundSecurityGroup` to own the inbound rules. ECS then removes the rules it managed and stops managing them.
- **IP address type:** the ECS default is `dualstack`. The template uses `ipv4`, so the subnets don't need IPv6.
- **Health check:** changing a connector's health check replaces the target group, and that fails with the `ROLLING` strategy. Set the health check when the service first connects, or switch to `BLUE_GREEN`, `LINEAR` or `CANARY` first. The defaults are HTTP `GET /` every 30 s, a 5 s timeout and code 200.
- **Managed resources:** these carry the tags `AmazonECSManaged=true`, `aws:ecs:gateway-arn` and (per route) `aws:ecs:gateway-route-arn`. Don't modify them outside ECS, because ECS won't repair them and later deployments or cleanup can fail.
- **Disconnect:** remove `GatewayConnectors` from a service, or delete the service. ECS then removes that service's route and resources on that deployment. The shared ALB is removed when its last service leaves.
- **Stack delete:** a gateway can be deleted only when deletion protection is off and no association is `ACTIVE` or `DISASSOCIATING`. An association stays `DISASSOCIATING` until every route on the cluster is gone. The services `DependsOn` the association, so CloudFormation deletes them first, then the association, then the gateway.

## Docs

- [../../docs/ecs/ug-gateway-overview.md](../../docs/ecs/ug-gateway-overview.md)
- [../../docs/ecs/ug-gateway-managing.md](../../docs/ecs/ug-gateway-managing.md) (infrastructure role, network configuration, inbound security group, deletion protection)
- [../../docs/ecs/ug-gateway-connect-service.md](../../docs/ecs/ug-gateway-connect-service.md) (connector, filters, health checks, service URL)
- [../../docs/ecs/ug-gateway-troubleshooting.md](../../docs/ecs/ug-gateway-troubleshooting.md)
- [../../docs/ecs/cfn-aws-resource-ecs-gateway.md](../../docs/ecs/cfn-aws-resource-ecs-gateway.md)
- [../../docs/ecs/cfn-aws-resource-ecs-gatewayclusterassociations.md](../../docs/ecs/cfn-aws-resource-ecs-gatewayclusterassociations.md)
- [../../docs/ecs/cfn-aws-properties-ecs-service-gatewayconnector.md](../../docs/ecs/cfn-aws-properties-ecs-service-gatewayconnector.md)
