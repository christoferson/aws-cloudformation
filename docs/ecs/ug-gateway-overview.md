> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gateway-overview.html
> Downloaded: 2026-10-21

# Amazon ECS Gateway

Amazon ECS Gateway simplifies ingress networking for containerized applications. It automatically provisions and manages the infrastructure that routes traffic to your Amazon Elastic Container Service (Amazon ECS) services. Instead of configuring Application Load Balancers, listeners, target groups, security groups, and certificates for each service, you define ingress settings once on a gateway and share that infrastructure across many services.

You create a gateway with your desired networking configuration and associate it with one or more Amazon ECS clusters. Each service then opts in by adding a gateway connector parameter. Amazon ECS then provisions and manages the ingress infrastructure in your AWS account, giving each connected service a unique HTTPS hostname.

To get started, see Create and manage a gateway. To connect a service to a gateway that already exists, see Connect services to a gateway. 

## How Amazon ECS Gateway works 

Amazon ECS Gateway separates infrastructure management from application deployment. It supports two primary personas:  
Platform teams own the gateway. They create and configure gateways, and associate them with Amazon ECS clusters. A gateway's configuration applies to every service connected to it and includes settings across networking, security, and operations:  
Networking, such as whether services are reachable from the internet or only from inside the VPC, and which subnets the load balancers use
Security, such as which security group controls inbound traffic, and which AWS WAF web ACL applies
Operations, such as where access logs go, how much load balancer capacity to allow, and which request header identifies test traffic during progressive deployments.
 

You cannot change several of these settings after you create the gateway. For more information, see Customizing a gateway. 
Application teams opt their services into a gateway by adding a gateway connector parameter when they create or update a service. The connector names the container port that receives traffic, and can also set an access type filter and health checks. 
 

Setting up ingress through a gateway takes three steps:  
Create a gateway. The platform team creates a gateway and defines its ingress configuration, including the networking and security settings. 
Associate the gateway with clusters. The platform team associates the gateway with one or more Amazon ECS clusters, which makes it available to the services in those clusters. 
Connect services. Each service opts in individually. An application team adds a gateway connector when it creates or updates a service, naming the container port that receives traffic. 
 

Amazon ECS provisions no infrastructure until the first service connects. It then creates or reuses the shared resources, creates the per-service resources, and creates a gateway route that directs traffic to the service at a unique HTTPS URL. 

## Benefits of Amazon ECS Gateway 

Gateways simplify setting up and managing Application Load Balancers for your applications. Amazon ECS Gateway provides the following benefits:  
Centralized configuration. Platform teams define networking, security, and traffic management settings once, and every service that connects to the gateway inherits them across clusters. Application teams get ingress for their services without configuring any resources themselves or needing networking expertise. 
Automated infrastructure management. Amazon ECS provisions and manages Application Load Balancers, listeners, target groups, security groups, certificates, and DNS hostnames as services opt in to a gateway. 
Cost optimization. Share Application Load Balancers across multiple services using the same networking configuration to reduce costs. 
Transparent infrastructure. Amazon ECS creates all resources in your AWS account, where you can view and manage them with the AWS Management Console and the AWS APIs. 
 

## Key concepts 

The following table describes the concepts you work with when you use Amazon ECS Gateway.  
|  Concept |  Description |    
|  Gateway |  An account-level resource, with its own ARN, that defines the ingress configuration and manages the underlying infrastructure for the services connected to it. Gateway names are unique within an account and Region. |   
|  Gateway-cluster association |  A link between a gateway and a cluster that makes the gateway available to the services in that cluster. Associations are many-to-many: one gateway can serve multiple clusters, and one cluster can use multiple gateways. For more information, see Gateway Service Limits. |   
|  Gateway connector |  An opt-in parameter on a service that connects it to all compatible gateways associated with its cluster. The connector specifies the name of the container port to expose and includes optional access type and health check settings. |   
|  Gateway route |  A resource with its own ARN that represents one connection between a service and a gateway. Amazon ECS creates a route when the service connects and deletes it when the service disconnects. The route reports the connection status, the service's URL, and the underlying service-specific resources. |    

## Infrastructure managed by Amazon ECS Gateway 

Amazon ECS provisions two categories of ingress infrastructure in your account.  
|  Resource type |  Managed resources |  Description |    
|  Shared infrastructure |  Application Load Balancer, load balancer listener, load balancer security group |  Resources that a gateway manages and shares across multiple Amazon ECS services. |   
|  Service-specific infrastructure |  AWS Certificate Manager certificate, DNS hostname, listener rule, target group, service security group |  Resources that Amazon ECS creates for each gateway route to direct traffic to the corresponding service. |    

Amazon ECS uses host-based routing to direct requests from a shared Application Load Balancer to the appropriate service. Each service gets a generated hostname in the form `https://<unique-id>.ecs.<region>.on.aws`. The domain varies by AWS partition. 

A gateway provisions nothing when you create it or associate it with a cluster. When the first service connects, Amazon ECS provisions the first load balancer, its listener, and its security group, then adds that service's own resources. As more services connect, Amazon ECS reuses a load balancer that has capacity, or provisions another one. Up to 25 services share one Application Load Balancer, and each service has its own hostname, certificate, and listener rules. 

Amazon ECS tags the resources it manages with `AmazonECSManaged=true` and with the system tag `aws:ecs:gateway-arn`, whose value is the gateway's ARN. The target group, listener rules, and service security group that Amazon ECS creates for each gateway route also carry `aws:ecs:gateway-route-arn`. Use these tags to find the resources in the Elastic Load Balancing, Amazon EC2, and AWS Certificate Manager consoles. 

## Pricing 

There is no additional charge for using Amazon ECS Gateway. You pay only for the underlying AWS resources provisioned in your account when services connect to a gateway, including applicable Application Load Balancer, Amazon CloudWatch logs and metrics, and data transfer charges. 

## Availability 

Amazon ECS Gateway is available in all commercial AWS Regions. It supports Amazon ECS services that use the `awsvpc` network mode, on all launch types: Amazon ECS EC2, Fargate, and Amazon ECS Managed Instances. You can create and manage gateways using the Amazon ECS console, the AWS CLI, the AWS SDKs, and CloudFormation. 

## Gateway Service Limits 

The following table lists the service quotas for Amazon ECS Gateway.  
|  Limit |  Value |    
|  Max Gateway-Cluster Associations Per Cluster |  5 |   
|  Max Clusters Per Gateway |  10,000 |   
|  Max Gateway Connectors Per Service |  1 |   
|  Max Services Per Application Load Balancer |  25 |   
|  Max Application Load Balancers Per Gateway |  200 |    

The underlying AWS resources are also subject to their own service quotas. Refer to Quotas for your Application Load Balancers. 

## Considerations 

Review the following before you adopt Amazon ECS Gateway. 

A gateway serves `HTTPS` traffic only. A gateway uses Application Load Balancers with host-based routing, so it serves web applications and APIs addressed by hostname. The listener uses only the `HTTPS` protocol on port 443. No other protocol is supported. 

A service must use the `awsvpc` network mode. A service that uses the `bridge`, `host`, or `none` network mode cannot connect to a gateway. 

A gateway works within a single account. A gateway and its clusters must be in the same AWS account. You cannot associate a gateway with a cluster in another account. 

A gateway does not work with Express Mode services. It serves only Amazon ECS services. 

A service has one gateway connector. You cannot add a second connector to a service. One connector can still connect the service to several gateways. 

A service cannot choose a gateway by name. A connector connects the service to every compatible gateway associated with its cluster. A gateway is compatible when it matches the access type filter if the service sets one, in the same VPC as the service, and covers every Availability Zone the service runs in. Amazon ECS excludes every gateway that does not match, and the request fails when there is no compatible gateway in the cluster that meets all three conditions. For more information, see How Amazon ECS selects compatible gateways. 

Some gateway settings are immutable after creation. You cannot change a gateway's name, type, scheme, listener port, listener protocol, subnets, or IP address type after you create it. To change any of these, create a new gateway and move services to it. For more information, see Update a gateway. 

Amazon ECS does not consolidate load balancers. A gateway adds load balancers when the existing ones are full and removes them when they become empty. It does not move services between load balancers, so several partly filled load balancers can remain after services leave. 

Amazon ECS does not repair changes made outside it. If you modify or delete a resource that a gateway manages, Amazon ECS does not restore it. Traffic to the affected services can stop, and later service deployments, gateway updates, and cleanup operations can fail. For more information, see Changes made outside Amazon ECS.
