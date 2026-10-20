> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-instancelaunchtemplate.html
> Downloaded: 2026-10-20

# AWS::ECS::CapacityProvider InstanceLaunchTemplate

The launch template configuration for Amazon ECS Managed Instances. This defines how Amazon ECS launches Amazon EC2 instances, including the instance profile for your tasks, network and storage configuration, capacity options, and instance requirements for flexible instance type selection.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CapacityOptionType" : String,
  "CapacityReservations" : CapacityReservationRequest,
  "Ec2InstanceProfileArn" : String,
  "FipsEnabled" : Boolean,
  "InstanceMetadataTagsPropagation" : Boolean,
  "InstanceRequirements" : InstanceRequirementsRequest,
  "LocalStorageConfiguration" : ManagedInstancesLocalStorageConfiguration,
  "Monitoring" : String,
  "NetworkConfiguration" : ManagedInstancesNetworkConfiguration,
  "StorageConfiguration" : ManagedInstancesStorageConfiguration
}

```

### YAML

```
  CapacityOptionType: String
  CapacityReservations: 
    CapacityReservationRequest
  Ec2InstanceProfileArn: String
  FipsEnabled: Boolean
  InstanceMetadataTagsPropagation: Boolean
  InstanceRequirements: 
    InstanceRequirementsRequest
  LocalStorageConfiguration: 
    ManagedInstancesLocalStorageConfiguration
  Monitoring: String
  NetworkConfiguration: 
    ManagedInstancesNetworkConfiguration
  StorageConfiguration: 
    ManagedInstancesStorageConfiguration

```

## Properties

**`CapacityOptionType`** 

The capacity option type. This determines whether Amazon ECS launches On-Demand, Spot or Capacity Reservation Instances for your managed instance capacity provider. 

Valid values are:  
`ON_DEMAND` - Launches standard On-Demand Instances. On-Demand Instances provide predictable pricing and availability. 
`SPOT` - Launches Spot Instances that use spare Amazon EC2 capacity at reduced cost. Spot Instances can be interrupted by Amazon EC2 with a two-minute notification when the capacity is needed back. 
`RESERVED` - Launches Instances using Amazon EC2 Capacity Reservations. Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone. 
 

The default is On-Demand 

For more information about Amazon EC2 capacity options, see Instance purchasing options in the Amazon EC2 User Guide. 

Required: No

Type: String

Allowed values: `ON_DEMAND | SPOT | RESERVED`

Update requires: Some interruptions

**`CapacityReservations`** 

Capacity reservation specifications. You can specify:  
Capacity reservation preference 
Reservation resource group to be used for targeted capacity reservations 
 

Amazon ECS will launch instances according to the specified criteria. 

Required: No

Type: CapacityReservationRequest

Update requires: No interruption

**`Ec2InstanceProfileArn`** 

The Amazon Resource Name (ARN) of the instance profile that Amazon ECS applies to Amazon ECS Managed Instances. This instance profile must include the necessary permissions for your tasks to access AWS services and resources. 

For more information, see Amazon ECS instance profile for Managed Instances in the Amazon ECS Developer Guide.  

Required: Yes

Type: String

Update requires: No interruption

**`FipsEnabled`** 

Determines whether to enable FIPS 140-2 validated cryptographic modules on EC2 instances launched by the capacity provider. If `true`, instances use FIPS-compliant cryptographic algorithms and modules for enhanced security compliance. If `false`, instances use standard cryptographic implementations. 

If not specified, instances are launched with FIPS enabled in AWS GovCloud (US) regions and FIPS disabled in other regions. 

Required: No

Type: Boolean

Update requires: Replacement

**`InstanceMetadataTagsPropagation`** 

Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS. 

Disable this setting if your tags contain characters that are not compatible with IMDS, such as `/`. IMDS requires tag keys to match the pattern `[0-9a-zA-Z\-_+=,.@:]{1,255}`. 

The default value is `true`. 

For more information, see Work with instance tags in instance metadata in the Amazon EC2 User Guide. 

Required: No

Type: Boolean

Update requires: No interruption

**`InstanceRequirements`** 

The instance requirements. You can specify:  
The instance types 
Instance requirements such as vCPU count, memory, network performance, and accelerator specifications 
 

Amazon ECS automatically selects the instances that match the specified criteria. 

Required: No

Type: InstanceRequirementsRequest

Update requires: No interruption

**`LocalStorageConfiguration`** 

The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses instance store volumes available on the container instance. 

Required: No

Type: ManagedInstancesLocalStorageConfiguration

Update requires: No interruption

**`Monitoring`** 

CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see Detailed monitoring for Amazon ECS Managed Instances in the Amazon ECS Developer Guide. 

Required: No

Type: String

Allowed values: `BASIC | DETAILED`

Update requires: No interruption

**`NetworkConfiguration`** 

The network configuration for Amazon ECS Managed Instances. This specifies the subnets and security groups that instances use for network connectivity. 

Required: Yes

Type: ManagedInstancesNetworkConfiguration

Update requires: No interruption

**`StorageConfiguration`** 

The storage configuration for Amazon ECS Managed Instances. This defines the data volume properties for the instances. 

Required: No

Type: ManagedInstancesStorageConfiguration

Update requires: No interruption
