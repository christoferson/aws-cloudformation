> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-capacityreservationrequest.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider CapacityReservationRequest

The Capacity Reservation configurations to be used when using the `RESERVED` capacity option type.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ReservationGroupArn" : String,
  "ReservationPreference" : String
}

```

### YAML

```
  ReservationGroupArn: String
  ReservationPreference: String

```

## Properties

**`ReservationGroupArn`** 

The ARN of the Capacity Reservation resource group in which to run the instance. 

Required: No

Type: String

Update requires: No interruption

**`ReservationPreference`** 

The preference on when capacity reservations should be used. 

Valid values are:  
`RESERVATIONS_ONLY` - Exclusively launch instances into capacity reservations that match the instance requirements configured for the capacity provider. If none exist, instances will fail to provision. 
`RESERVATIONS_FIRST` - Prefer to launch instances into a capacity reservation if any exist that match the instance requirements configured for the capacity provider. If none exist, fall back to launching instances On-Demand. 
`RESERVATIONS_EXCLUDED` - Avoid using capacity reservations and launch exclusively On-Demand. 
 

Required: No

Type: String

Allowed values: `RESERVATIONS_ONLY | RESERVATIONS_FIRST | RESERVATIONS_EXCLUDED`

Update requires: No interruption
