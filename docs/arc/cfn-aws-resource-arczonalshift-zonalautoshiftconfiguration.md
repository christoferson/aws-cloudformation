> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-arczonalshift-zonalautoshiftconfiguration.html
> Downloaded: 2026-10-24

# AWS::ARCZonalShift::ZonalAutoshiftConfiguration

The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuation, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

You can update the zonal autoshift autoshift status to enable or disable zonal autoshift. When zonal autoshift is `ENABLED`, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
  "Properties" : {
      "PracticeRunConfiguration" : PracticeRunConfiguration,
      "ResourceIdentifier" : String,
      "ZonalAutoshiftStatus" : String
    }
}

```

### YAML

```
Type: AWS::ARCZonalShift::ZonalAutoshiftConfiguration
Properties:
  PracticeRunConfiguration: 
    PracticeRunConfiguration
  ResourceIdentifier: String
  ZonalAutoshiftStatus: String

```

## Properties

**`PracticeRunConfiguration`** 

A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run. When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs. 

Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application. 

You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled. 

Required: No

Type: PracticeRunConfiguration

Update requires: No interruption

**`ResourceIdentifier`** 

The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource. 

At this time, supported resources are Network Load Balancers and Application Load Balancers. 

Required: No

Type: String

Minimum: `8`

Maximum: `1024`

Update requires: Replacement

**`ZonalAutoshiftStatus`** 

When zonal autoshift is `ENABLED`, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs. 

Required: No

Type: String

Allowed values: `ENABLED`

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the resource.

For more information about using the `Ref` function, see `Ref`.
