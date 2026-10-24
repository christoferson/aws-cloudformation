> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::AutoScalingGroup AvailabilityZoneImpairmentPolicy

 Describes an Availability Zone impairment policy. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ImpairedZoneHealthCheckBehavior" : String,
  "ZonalShiftEnabled" : Boolean
}

```

### YAML

```
  ImpairedZoneHealthCheckBehavior: String
  ZonalShiftEnabled: Boolean

```

## Properties

**`ImpairedZoneHealthCheckBehavior`** 

 Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select `Replace unhealthy`, instances that appear unhealthy will be replaced in all Availability Zones. If you select `Ignore unhealthy`, instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see Auto Scaling group zonal shift in the Amazon EC2 Auto Scaling User Guide.  

Required: Yes

Type: String

Allowed values: `IgnoreUnhealthy | ReplaceUnhealthy`

Update requires: No interruption

**`ZonalShiftEnabled`** 

 If `true`, enable zonal shift for your Auto Scaling group.  

Required: Yes

Type: Boolean

Update requires: No interruption
