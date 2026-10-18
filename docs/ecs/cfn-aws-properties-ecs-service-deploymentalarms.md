> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentalarms.html
> Downloaded: 2026-10-18

# AWS::ECS::Service DeploymentAlarms

One of the methods which provide a way for you to quickly identify when a deployment has failed, and then to optionally roll back the failure to the last working deployment.

When the alarms are generated, Amazon ECS sets the service deployment to failed. Set the rollback parameter to have Amazon ECS to roll back your service to the last completed deployment after a failure.

You can only use the `DeploymentAlarms` method to detect failures when the `DeploymentController` is set to `ECS`.

For more information, see Rolling update in the  Amazon Elastic Container Service Developer Guide .

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlarmNames" : [ String, ... ],
  "Enable" : Boolean,
  "Rollback" : Boolean
}

```

### YAML

```
  AlarmNames: 
    - String
  Enable: Boolean
  Rollback: Boolean

```

## Properties

**`AlarmNames`** 

One or more CloudWatch alarm names. Use a "," to separate the alarms. 

Required: Yes

Type: Array of String

Update requires: No interruption

**`Enable`** 

Determines whether to use the CloudWatch alarm option in the service deployment process. 

Required: Yes

Type: Boolean

Update requires: No interruption

**`Rollback`** 

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully. 

Required: Yes

Type: Boolean

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service
