> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttesttrafficrules.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceConnectTestTrafficRules

The test traffic routing configuration for Amazon ECS blue/green deployments. This configuration allows you to define rules for routing specific traffic to the new service revision during the deployment process, allowing for safe testing before full production traffic shift.

For more information, see Service Connect for Amazon ECS blue/green deployments in the  Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Header" : ServiceConnectTestTrafficRulesHeader
}

```

### YAML

```
  Header: 
    ServiceConnectTestTrafficRulesHeader

```

## Properties

**`Header`** 

The HTTP header-based routing rules that determine which requests should be routed to the new service version during blue/green deployment testing. These rules provide fine-grained control over test traffic routing based on request headers. 

Required: Yes

Type: ServiceConnectTestTrafficRulesHeader

Update requires: No interruption
