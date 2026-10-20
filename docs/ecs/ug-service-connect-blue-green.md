> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-blue-green.html
> Downloaded: 2026-10-20

# Service Connect resources for Amazon ECS blue/green, linear, and canary deployments

When using Service Connect with blue/green deployments, you need to configure specific components to enable proper traffic routing between the blue and green service revisions. This section explains the required components and their configuration. 

## Architecture overview 

Service Connect builds both service discovery and service mesh capabilities through a managed sidecar proxy that's automatically injected into your Amazon ECS tasks. These proxies handle routing decisions, retries, and metrics collection, while AWS Cloud Map provides the service registry backend. When you deploy a service with Service Connect enabled, the service registers itself in AWS Cloud Map, and client services discover it through the namespace. 

In a standard Service Connect implementation, client services connect to logical service names, and the sidecar proxy handles routing to the actual service instances. With blue/green deployments, this model is extended to include test traffic routing through the `testTrafficRules` configuration. 

During a blue/green deployment, the following key components work together:  
Service Connect Proxy: All traffic between services passes through the Service Connect proxy, which makes routing decisions based on the configuration. 
AWS Cloud Map Registration: Both blue and green deployments register with AWS Cloud Map, but the green deployment initially registers as a "test" endpoint. 
Test Traffic Routing: The `testTrafficRules` in the Service Connect configuration determine how to identify and route test traffic to the green deployment. This is accomplished through header-based routing, where specific HTTP headers in the requests direct traffic to the test revision. By default, Service Connect recognizes the `x-amzn-ecs-blue-green-test` header for HTTP-based protocols when no custom rules are specified. 
Client Configuration: All clients in the namespace automatically receive both production and test routes, but only requests matching test rules will go to the green deployment. 
 

What makes this approach powerful is that it handles the complexity of service discovery during transitions. As traffic shifts from the blue to green deployment, all connectivity and discovery mechanisms update automatically. There's no need to update DNS records, reconfigure load balancers, or deploy service discovery changes separately since the service mesh handles it all. 

## Traffic routing and testing 

Service Connect provides advanced traffic routing capabilities for blue/green deployments, including header-based routing and client alias configuration for testing scenarios. 

### Test traffic header rules 

During blue/green deployments, you can configure test traffic header rules to route specific requests to the green (new) service revision for testing purposes. This allows you to validate the new version with controlled traffic before completing the deployment. 

Service Connect uses header-based routing to identify test traffic. By default, Service Connect recognizes the `x-amzn-ecs-blue-green-test` header for HTTP-based protocols when no custom rules are specified. When this header is present in a request, the Service Connect proxy automatically routes the request to the green deployment for testing. 

Test traffic header rules enable you to:  
Route requests with specific headers to the green service revision 
Test new functionality with a subset of traffic 
Validate service behavior before full traffic cutover 
Implement canary testing strategies 
Perform integration testing in a production-like environment 
 

The header-based routing mechanism works seamlessly with your existing application architecture. Client services don't need to be aware of the blue/green deployment process - they simply include the appropriate headers when sending test requests, and the Service Connect proxy handles the routing logic automatically. Important

Test traffic header rules require that the Service Connect service port mapping has `appProtocol` set to `http`, `http2`, or `grpc`. If your service uses plain TCP without an application-layer protocol (that is, `appProtocol` is not set), you cannot use header-based `testTrafficRules` for blue/green deployments. In this case, use port-based test traffic routing instead. 

For more information about configuring test traffic header rules, see ServiceConnectTestTrafficHeaderRules in the Amazon Elastic Container Service API Reference. 

### Header matching rules 

Header matching rules define the criteria for routing test traffic during blue/green deployments. You can configure multiple matching conditions to precisely control which requests are routed to the green service revision. 

Header matching supports:  
Exact header value matching 
Header presence checking 
Pattern-based matching 
Multiple header combinations 
 

Example use cases include routing requests with specific user agent strings, API versions, or feature flags to the green service for testing. 

For more information about header matching configuration, see ServiceConnectTestTrafficHeaderMatchRules in the Amazon Elastic Container Service API Reference. 

### Client aliases for blue/green deployments 

Client aliases provide stable DNS endpoints for services during blue/green deployments. They enable seamless traffic routing between blue and green service revisions without requiring client applications to change their connection endpoints. 

During a blue/green deployment, client aliases:  
Maintain consistent DNS names for client connections 
Enable automatic traffic switching between service revisions 
Support gradual traffic migration strategies 
Provide rollback capabilities by redirecting traffic to the blue revision 
 

You can configure multiple client aliases for different ports or protocols, allowing complex service architectures to maintain connectivity during deployments. 

For more information about client alias configuration, see ServiceConnectClientAlias in the Amazon Elastic Container Service API Reference. 

### Best practices for traffic routing 

When implementing traffic routing for blue/green deployments with Service Connect, consider the following best practices:  
Start with header-based testing: Use test traffic header rules to validate the green service with controlled traffic before switching all traffic. 
Configure health checks: Ensure both blue and green services have appropriate health checks configured to prevent routing traffic to unhealthy instances. 
Monitor service metrics: Track key performance indicators for both service revisions during the deployment to identify issues early. 
Plan rollback strategy: Configure client aliases and routing rules to enable quick rollback to the blue service if issues are detected. 
Test header matching logic: Validate your header matching rules in a non-production environment before applying them to production deployments. 
 

## Service Connect blue/green deployment workflow 

Understanding how Service Connect manages the blue/green deployment process helps you implement and troubleshoot your deployments effectively. The following workflow shows how the different components interact during each phase of the deployment. 

### Deployment phases 

A Service Connect blue/green deployment progresses through several distinct phases:  
Initial State: The blue service handles 100% of production traffic. All client services in the namespace connect to the blue service through the logical service name configured in Service Connect. 
Green Service Registration: When the green deployment starts, it registers with AWS Cloud Map as a "test" endpoint. The Service Connect proxy in client services automatically receives both production and test route configurations. 
Test Traffic Routing: Requests containing the test traffic headers (such as `x-amzn-ecs-blue-green-test`) are automatically routed to the green service by the Service Connect proxy. Production traffic continues to flow to the blue service. 
Traffic Shift Preparation: After successful testing, the deployment process prepares for production traffic shift. Both blue and green services remain registered and healthy. 
Production Traffic Shift: The Service Connect configuration updates to route production traffic to the green service. This happens automatically without requiring client service updates or DNS changes. 
Bake Time Period: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted. 
Blue Service Deregistration: After successful traffic shift and validation, the blue service is deregistered from AWS Cloud Map and terminated, completing the deployment. 
 

### Service Connect proxy behavior 

The Service Connect proxy plays a crucial role in managing traffic during blue/green deployments. Understanding its behavior helps you design effective testing and deployment strategies. 

Key proxy behaviors during blue/green deployments:  
Automatic Route Discovery: The proxy automatically discovers both production and test routes from AWS Cloud Map without requiring application restarts or configuration changes. 
Header-Based Routing: The proxy examines incoming request headers and routes traffic to the appropriate service revision based on the configured test traffic rules. 
Health Check Integration: The proxy only routes traffic to healthy service instances, automatically excluding unhealthy tasks from the routing pool. 
Retry and Circuit Breaking: The proxy provides built-in retry logic and circuit breaking capabilities, improving resilience during deployments. 
Metrics Collection: The proxy collects detailed metrics for both blue and green services, enabling comprehensive monitoring during deployments. 
 

### Service discovery updates 

One of the key advantages of using Service Connect for blue/green deployments is the automatic handling of service discovery updates. Traditional blue/green deployments often require complex DNS updates or load balancer reconfiguration, but Service Connect manages these changes transparently. 

During a deployment, Service Connect handles:  
Namespace Updates: The Service Connect namespace automatically includes both blue and green service endpoints, with appropriate routing rules. 
Client Configuration: All client services in the namespace automatically receive updated routing information without requiring restarts or redeployment. 
Gradual Transition: Service discovery updates happen gradually and safely, ensuring no disruption to ongoing requests. 
Rollback Support: If a rollback is needed, Service Connect can quickly revert service discovery configurations to route traffic back to the blue service.
