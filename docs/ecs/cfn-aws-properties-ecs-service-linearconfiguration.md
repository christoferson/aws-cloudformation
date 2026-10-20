> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-linearconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service LinearConfiguration

Configuration for a linear deployment strategy that shifts production traffic in equal percentage increments with configurable wait times between each step until 100 percent of traffic is shifted to the new service revision. 

The following validation applies only to Linear deployments created through CloudFormation. CloudFormation operations time out after 36 hours. Linear deployments can approach this limit because of their extended duration. This can cause CloudFormation to roll back the deployment. To prevent timeout-related rollbacks, CloudFormation rejects deployments when the calculated deployment time exceeds 33 hours based on your template configuration: 

 `BakeTimeInMinutes + (StepBakeTimeInMinutes × Number of deployment steps)` 

Where the number of deployment steps is calculated as follows: 
If `StepPercent` evenly divides by 100: The number of deployment steps equals `(100 ÷ StepPercent) - 1` 
Otherwise: The number of deployment steps equals the floor of `100 ÷ StepPercent`. For example, if `StepPercent` is 11, the number of deployment steps is 9 (not 9.1). 

This calculation reflects that CloudFormation doesn't apply the step bake time after the final traffic shift reaches 100%. For example, with a `StepPercent` of 50%, there are actually two traffic shifts, but only one deployment step is counted for validation purposes because the bake time is applied only after the first 50% shift, not after reaching 100%.

Additional backend processes (such as task scaling and running lifecycle hooks) can extend deployment time beyond these calculations. Even deployments under the 33-hour threshold might still time out if these processes cause the total duration to exceed 36 hours. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "StepBakeTimeInMinutes" : Integer,
  "StepPercent" : Number
}

```

### YAML

```
  StepBakeTimeInMinutes: Integer
  StepPercent: Number

```

## Properties

**`StepBakeTimeInMinutes`** 

The amount of time in minutes to wait between each traffic shifting step during a linear deployment. Valid values are 0 to 1440 minutes (24 hours). The default value is 6. This bake time is not applied after reaching 100 percent traffic. 

Required: No

Type: Integer

Minimum: `0`

Maximum: `1440`

Update requires: No interruption

**`StepPercent`** 

The percentage of production traffic to shift in each step during a linear deployment. Valid values are multiples of 0.1 from 3.0 to 100.0. The default value is 10.0. 

Required: No

Type: Number

Minimum: `3`

Maximum: `100`

Update requires: No interruption
