> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html
> Downloaded: 2026-10-24

# AWS::ARCZonalShift::ZonalAutoshiftConfiguration ControlCondition

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an outcome alarm, to monitor application health during practice runs and, optionally, a blocking alarm, to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see  Considerations when you configure zonal autoshift in the ARC Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AlarmIdentifier" : String,
  "Type" : String
}

```

### YAML

```
  AlarmIdentifier: String
  Type: String

```

## Properties

**`AlarmIdentifier`** 

The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run. 

Required: Yes

Type: String

Pattern: `^.*$`

Minimum: `8`

Maximum: `1024`

Update requires: No interruption

**`Type`** 

The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH`. 

Required: Yes

Type: String

Pattern: `^[a-zA-Z]*$`

Minimum: `8`

Maximum: `10`

Update requires: No interruption
