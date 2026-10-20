> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-clustersettings.html
> Downloaded: 2026-10-20

# AWS::ECS::Cluster ClusterSettings

The settings to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights with enhanced observability or CloudWatch Container Insights for a cluster.

Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up. 

For more information, see Monitor Amazon ECS containers using Container Insights with enhanced observability in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Name" : String,
  "Value" : String
}

```

### YAML

```
  Name: String
  Value: String

```

## Properties

**`Name`** 

The name of the cluster setting. The value is `containerInsights`. 

Required: No

Type: String

Allowed values: `containerInsights`

Update requires: No interruption

**`Value`** 

The value to set for the cluster setting. The supported values are `enhanced`, `enabled`, and `disabled`.  

To use Container Insights with enhanced observability, set the `containerInsights` account setting to `enhanced`. 

To use Container Insights, set the `containerInsights` account setting to `enabled`. 

If a cluster value is specified, it will override the `containerInsights` value set with PutAccountSetting or PutAccountSettingDefault. 

Required: No

Type: String

Update requires: No interruption

## See also 
 Define an empty cluster with CloudWatch Container Insights enabled and defined tags
