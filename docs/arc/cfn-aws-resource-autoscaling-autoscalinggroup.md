> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html
> Downloaded: 2026-10-24

# AWS::AutoScaling::AutoScalingGroup

The `AWS::AutoScaling::AutoScalingGroup` resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. 

For more information about Amazon EC2 Auto Scaling, see the Amazon EC2 Auto Scaling User Guide. Note

Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a launch template or a launch configuration. We strongly recommend that you do not use launch configurations. For more information, see Launch configurations in the Amazon EC2 Auto Scaling User Guide.

For help migrating from launch configurations to launch templates, see Migrate AWS CloudFormation stacks from launch configurations to launch templates in the Amazon EC2 Auto Scaling User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AutoScaling::AutoScalingGroup",
  "Properties" : {
      "AutoScalingGroupName" : String,
      "AvailabilityZoneDistribution" : AvailabilityZoneDistribution,
      "AvailabilityZoneIds" : [ String, ... ],
      "AvailabilityZoneImpairmentPolicy" : AvailabilityZoneImpairmentPolicy,
      "AvailabilityZones" : [ String, ... ],
      "CapacityRebalance" : Boolean,
      "CapacityReservationSpecification" : CapacityReservationSpecification,
      "Context" : String,
      "Cooldown" : String,
      "DefaultInstanceWarmup" : Integer,
      "DeletionProtection" : String,
      "DesiredCapacity" : String,
      "DesiredCapacityType" : String,
      "HealthCheckGracePeriod" : Integer,
      "HealthCheckType" : String,
      "InstanceId" : String,
      "InstanceLifecyclePolicy" : InstanceLifecyclePolicy,
      "InstanceMaintenancePolicy" : InstanceMaintenancePolicy,
      "LaunchConfigurationName" : String,
      "LaunchTemplate" : LaunchTemplateSpecification,
      "LifecycleHookSpecificationList" : [ LifecycleHookSpecification, ... ],
      "LoadBalancerNames" : [ String, ... ],
      "MaxInstanceLifetime" : Integer,
      "MaxSize" : String,
      "MetricsCollection" : [ MetricsCollection, ... ],
      "MinSize" : String,
      "MixedInstancesPolicy" : MixedInstancesPolicy,
      "NewInstancesProtectedFromScaleIn" : Boolean,
      "NotificationConfigurations" : [ NotificationConfiguration, ... ],
      "PlacementGroup" : String,
      "ServiceLinkedRoleARN" : String,
      "SkipZonalShiftValidation" : Boolean,
      "Tags" : [ TagProperty, ... ],
      "TargetGroupARNs" : [ String, ... ],
      "TerminationPolicies" : [ String, ... ],
      "TrafficSources" : [ TrafficSourceIdentifier, ... ],
      "VPCZoneIdentifier" : [ String, ... ]
    }
}

```

### YAML

```
Type: AWS::AutoScaling::AutoScalingGroup
Properties:
  AutoScalingGroupName: String
  AvailabilityZoneDistribution: 
    AvailabilityZoneDistribution
  AvailabilityZoneIds: 
    - String
  AvailabilityZoneImpairmentPolicy: 
    AvailabilityZoneImpairmentPolicy
  AvailabilityZones: 
    - String
  CapacityRebalance: Boolean
  CapacityReservationSpecification: 
    CapacityReservationSpecification
  Context: String
  Cooldown: String
  DefaultInstanceWarmup: Integer
  DeletionProtection: String
  DesiredCapacity: String
  DesiredCapacityType: String
  HealthCheckGracePeriod: Integer
  HealthCheckType: String
  InstanceId: String
  InstanceLifecyclePolicy: 
    InstanceLifecyclePolicy
  InstanceMaintenancePolicy: 
    InstanceMaintenancePolicy
  LaunchConfigurationName: String
  LaunchTemplate: 
    LaunchTemplateSpecification
  LifecycleHookSpecificationList: 
    - LifecycleHookSpecification
  LoadBalancerNames: 
    - String
  MaxInstanceLifetime: Integer
  MaxSize: String
  MetricsCollection: 
    - MetricsCollection
  MinSize: String
  MixedInstancesPolicy: 
    MixedInstancesPolicy
  NewInstancesProtectedFromScaleIn: Boolean
  NotificationConfigurations: 
    - NotificationConfiguration
  PlacementGroup: String
  ServiceLinkedRoleARN: String
  SkipZonalShiftValidation: Boolean
  Tags: 
    - TagProperty
  TargetGroupARNs: 
    - String
  TerminationPolicies: 
    - String
  TrafficSources: 
    - TrafficSourceIdentifier
  VPCZoneIdentifier: 
    - String

```

## Properties

**`AutoScalingGroupName`** 

The name of the Auto Scaling group. This name must be unique per Region per account. 

The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters. Note

You cannot use a colon (:) in the name. 

Required: No

Type: String

Update requires: Replacement

**`AvailabilityZoneDistribution`** 

The EC2 instance capacity distribution across Availability Zones for the Auto Scaling group. 

Required: No

Type: AvailabilityZoneDistribution

Update requires: No interruption

**`AvailabilityZoneIds`** 

 The Availability Zone IDs where the Auto Scaling group can launch instances.  

Required: No

Type: Array of String

Update requires: No interruption

**`AvailabilityZoneImpairmentPolicy`** 

The Availability Zone impairment policy for the Auto Scaling group. 

Required: No

Type: AvailabilityZoneImpairmentPolicy

Update requires: No interruption

**`AvailabilityZones`** 

A list of Availability Zones where instances in the Auto Scaling group can be created. Used for launching into the default VPC subnet in each Availability Zone when not using the `VPCZoneIdentifier` property, or for attaching a network interface when an existing network interface ID is specified in a launch template. 

Required: No

Type: Array of String

Update requires: No interruption

**`CapacityRebalance`** 

Indicates whether Capacity Rebalancing is enabled. Otherwise, Capacity Rebalancing is disabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. For more information, see Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions in the in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Boolean

Update requires: No interruption

**`CapacityReservationSpecification`** 

The capacity reservation specification for the Auto Scaling group. 

Required: No

Type: CapacityReservationSpecification

Update requires: No interruption

**`Context`** 

Reserved. 

Required: No

Type: String

Update requires: No interruption

**`Cooldown`** 

 Only needed if you use simple scaling policies.  

The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see Scaling cooldowns for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. 

Default: `300` seconds 

Required: No

Type: String

Update requires: No interruption

**`DefaultInstanceWarmup`** 

The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the `InService` state.  

During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see Set the default instance warmup for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. Important

To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, even if it is set to 0 seconds. To remove a value that you previously set, include the property but specify `-1` for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of `0` or other nominal value. 

Default: None  

Required: No

Type: Integer

Update requires: No interruption

**`DeletionProtection`** 

The deletion protection setting for the Auto Scaling group. 

Required: No

Type: String

Allowed values: `none | prevent-force-deletion | prevent-all-deletion`

Update requires: No interruption

**`DesiredCapacity`** 

The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure automatic scaling. 

The number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity when creating the stack, the default is the minimum size of the group. 

CloudFormation marks the Auto Scaling group as successful (by setting its status to CREATE_COMPLETE) when the desired capacity is reached. However, if a maximum Spot price is set in the launch template or launch configuration that you specified, then desired capacity is not used as a criteria for success. Whether your request is fulfilled depends on Spot Instance capacity and your maximum price. 

Required: No

Type: String

Pattern: `^[0-9]+$`

Update requires: No interruption

**`DesiredCapacityType`** 

The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports `DesiredCapacityType` for attribute-based instance type selection only. For more information, see Create a mixed instances group using attribute-based instance type selection in the Amazon EC2 Auto Scaling User Guide. 

By default, Amazon EC2 Auto Scaling specifies `units`, which translates into number of instances. 

Valid values: `units` | `vcpu` | `memory-mib` 

Required: No

Type: String

Update requires: No interruption

**`HealthCheckGracePeriod`** 

The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the `InService` state. For more information, see Set the health check grace period for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. 

Default: `0` seconds 

Required: No

Type: Integer

Update requires: No interruption

**`HealthCheckType`** 

A comma-separated value string of one or more health check types. 

The valid values are `EC2`, `EBS`, `ELB`, and `VPC_LATTICE`. `EC2` is the default health check and cannot be disabled. For more information, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. 

Only specify `EC2` if you must clear a value that was previously set. 

Required: No

Type: String

Update requires: No interruption

**`InstanceId`** 

The ID of the instance used to base the launch configuration on. For more information, see Create an Auto Scaling group using an EC2 instance in the Amazon EC2 Auto Scaling User Guide. 

If you specify `LaunchTemplate`, `MixedInstancesPolicy`, or `LaunchConfigurationName`, don't specify `InstanceId`. 

Required: No

Type: String

Update requires: Replacement

**`InstanceLifecyclePolicy`** 

The instance lifecycle policy for the Auto Scaling group. 

Required: No

Type: InstanceLifecyclePolicy

Update requires: No interruption

**`InstanceMaintenancePolicy`** 

An instance maintenance policy. For more information, see Set instance maintenance policy in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: InstanceMaintenancePolicy

Update requires: No interruption

**`LaunchConfigurationName`** 

The name of the launch configuration to use to launch instances. 

Required only if you don't specify `LaunchTemplate`, `MixedInstancesPolicy`, or `InstanceId`. 

Required: No

Type: String

Update requires: Some interruptions

**`LaunchTemplate`** 

Information used to specify the launch template and version to use to launch instances. You can alternatively associate a launch template to the Auto Scaling group by specifying a `MixedInstancesPolicy`. For more information about creating launch templates, see Create a launch template for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. 

If you omit this property, you must specify `MixedInstancesPolicy`, `LaunchConfigurationName`, or `InstanceId`. 

Required: No

Type: LaunchTemplateSpecification

Update requires: Some interruptions

**`LifecycleHookSpecificationList`** 

One or more lifecycle hooks to add to the Auto Scaling group before instances are launched. 

Required: No

Type: Array of LifecycleHookSpecification

Update requires: No interruption

**`LoadBalancerNames`** 

A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers, specify the `TargetGroupARNs` property instead. 

Required: No

Type: Array of String

Update requires: No interruption

**`MaxInstanceLifetime`** 

The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). For more information, see Replace Auto Scaling instances based on maximum instance lifetime in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Integer

Update requires: No interruption

**`MaxSize`** 

The maximum size of the group. Note

With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above `MaxSize` to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above `MaxSize` by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group). 

Required: Yes

Type: String

Pattern: `^[0-9]+$`

Update requires: No interruption

**`MetricsCollection`** 

Enables the monitoring of group metrics of an Auto Scaling group. By default, these metrics are disabled.  

Required: No

Type: Array of MetricsCollection

Update requires: No interruption

**`MinSize`** 

The minimum size of the group. 

Required: Yes

Type: String

Pattern: `^[0-9]+$`

Update requires: No interruption

**`MixedInstancesPolicy`** 

An embedded object that specifies a mixed instances policy. 

The policy includes properties that not only define the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances (optional), and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacities, but also the properties that specify the instance configuration information—the launch template and instance types. The policy can also include a weight for each instance type and different launch templates for individual instance types. 

For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: MixedInstancesPolicy

Update requires: Some interruptions

**`NewInstancesProtectedFromScaleIn`** 

Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see Use instance scale-in protection in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Boolean

Update requires: No interruption

**`NotificationConfigurations`** 

Configures an Auto Scaling group to send notifications when specified events take place. 

Required: No

Type: Array of NotificationConfiguration

Update requires: No interruption

**`PlacementGroup`** 

The name of the placement group into which to launch your instances. For more information, see Placement groups in the Amazon EC2 User Guide. Note

A cluster placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group.  

Required: No

Type: String

Update requires: No interruption

**`ServiceLinkedRoleARN`** 

The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS service on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named `AWSServiceRoleForAutoScaling`, which it creates if it does not exist. For more information, see Service-linked roles in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: String

Update requires: No interruption

**`SkipZonalShiftValidation`**

Property description not available.

Required: No

Type: Boolean

Update requires: No interruption

**`Tags`** 

One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches. Tags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group. For more information, see Tag Auto Scaling groups and instances in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Array of TagProperty

Update requires: No interruption

**`TargetGroupARNs`** 

The Amazon Resource Names (ARN) of the Elastic Load Balancing target groups to associate with the Auto Scaling group. Instances are registered as targets with the target groups. The target groups receive incoming traffic and route requests to one or more registered targets. For more information, see Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group in the Amazon EC2 Auto Scaling User Guide. 

Required: No

Type: Array of String

Update requires: No interruption

**`TerminationPolicies`** 

A policy or a list of policies that are used to select the instance to terminate. These policies are executed in the order that you list them. For more information, see Configure termination policies for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide. 

Valid values: `Default` | `AllocationStrategy` | `ClosestToNextInstanceHour` | `NewestInstance` | `OldestInstance` | `OldestLaunchConfiguration` | `OldestLaunchTemplate` | `arn:aws:lambda:region:account-id:function:my-function:my-alias` 

Required: No

Type: Array of String

Update requires: No interruption

**`TrafficSources`** 

The traffic sources associated with this Auto Scaling group. 

Required: No

Type: Array of TrafficSourceIdentifier

Update requires: No interruption

**`VPCZoneIdentifier`** 

A list of subnet IDs for a virtual private cloud (VPC) where instances in the Auto Scaling group can be created. 

If this resource specifies public subnets and is also in a VPC that is defined in the same stack template, you must use the DependsOn attribute to declare a dependency on the VPC-gateway attachment. Note

When you update `VPCZoneIdentifier`, this retains the same Auto Scaling group and replaces old instances with new ones, according to the specified subnets. To control how CloudFormation replaces the instances, add an UpdatePolicy attribute to your stack. Set the update policy to `AutoScalingInstanceRefresh`. For more information, see the AutoScalingInstanceRefresh policy. 

Required to launch instances into a nondefault VPC. If you specify `VPCZoneIdentifier` with `AvailabilityZones`, the subnets that you specify for this property must reside in those Availability Zones.  

Required: Conditional

Type: Array of String

Update requires: Some interruptions

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example: `mystack-myasgroup-NT5EUXTNTXXD`.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`AutoScalingGroupARN`** 

The Amazon Resource Name (ARN) of the Auto Scaling group. 

## Remarks

When you update certain properties of an Auto Scaling group, such as the launch template, mixed instances policy, or Availability Zones, this update action does not deploy any change across the running Amazon EC2 instances in the Auto Scaling group. All new instances get the updated configuration, but existing instances continue to run with their original configuration. To also replace the existing instances during the stack update, add an UpdatePolicy attribute to your stack. Set the update policy to `AutoScalingInstanceRefresh`. AWS CloudFormation then replaces the instances by starting an instance refresh. For more information about the policy syntax, properties, and the property changes that trigger an instance refresh, see the AutoScalingInstanceRefresh policy. For more information about instance refresh, see Use an instance refresh to update instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.

You can use a CreationPolicy attribute with an Auto Scaling group to prevent its status from reaching create complete until CloudFormation receives a specified number of success signals. For more information, see Use a CreationPolicy to Wait for On-Instance Configurations on the AWS DevOps Blog. For an example template, see Configure Amazon EC2 Auto Scaling resources.

Note that Amazon EC2 Auto Scaling provides scaling activities to help you monitor the progress of your Auto Scaling group and to assist in troubleshooting any configuration issues when launching Amazon EC2 instances. For more information, see Verify a scaling activity for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.

## Examples

The following examples create or make changes to an Auto Scaling group.  
An Auto Scaling group and a launch template with a parameters section
Auto Scaling group with CloudWatch monitoring enabled and custom tags
 

### An Auto Scaling group and a launch template with a parameters section

The following example shows an Auto Scaling group. You specify values for the `MaxSize` and `MinSize` properties.

It also shows an AWS::EC2::LaunchTemplate resource that contains the instance configuration information for the group, which uses the `LaunchTemplate` property to specify the launch template. The Ref intrinsic function gets the ID of the `AWS::EC2::LaunchTemplate` resource `myLaunchTemplate`. The GetAtt function gets the latest version number (for example, `1`) of the launch template for the `Version` property.

This example references parameters to specify the `ImageId` and `InstanceType` properties for the launch template and the `VPCZoneIdentifier` property for the group. Parameters are variables that you can specify when you create or update the stack. By default, the `ImageId` property of the launch template references the latest Amazon Linux 2 AMI from the AWS Systems Manager Parameter Store. For more information, see AWS Systems Manager Parameter Store in the AWS Systems Manager User Guide and the blog post Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store on the AWS Compute Blog.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "LatestAmiId": {
            "Description": "Region specific image from the Parameter Store",
            "Type": "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
            "Default": "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
        },
        "InstanceType": {
            "Description": "Amazon EC2 instance type for the instances",
            "Type": "String",
            "AllowedValues": [
                "t3.micro",
                "t3.small",
                "t3.medium"
            ],
            "Default": "t3.micro"
        },
        "Subnets": {
            "Type": "List<AWS::EC2::Subnet::Id>",
            "Description": "A list of subnets for the Auto Scaling group"
        }
    },
    "Resources": {
        "myLaunchTemplate": {
            "Type": "AWS::EC2::LaunchTemplate",
            "Properties": {
                "LaunchTemplateName": { "Fn::Sub": "${AWS::StackName}-launch-template" },
                "LaunchTemplateData": {
                    "ImageId": { "Ref": "LatestAmiId" },
                    "InstanceType": { "Ref": "InstanceType" }
                }
            }
        },
        "myASG": {
            "Type": "AWS::AutoScaling::AutoScalingGroup",
            "Properties": {
                "LaunchTemplate": {
                    "LaunchTemplateId": { "Ref": "myLaunchTemplate" },
                    "Version": { "Fn::GetAtt": [ "myLaunchTemplate", "LatestVersionNumber" ] }
                },
                "MaxSize": "1",
                "MinSize": "1",
                "VPCZoneIdentifier": { "Ref": "Subnets" }
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  LatestAmiId:
    Description: Region specific image from the Parameter Store
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'
  InstanceType:
    Description: Amazon EC2 instance type for the instances
    Type: String
    AllowedValues:
      - t3.micro
      - t3.small
      - t3.medium
    Default: t3.micro
  Subnets:
    Type: 'List<AWS::EC2::Subnet::Id>'
    Description: A list of subnets for the Auto Scaling group
Resources:
  myLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties: 
      LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
      LaunchTemplateData:
        ImageId: !Ref LatestAmiId
        InstanceType: !Ref InstanceType
  myASG:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchTemplate:
        LaunchTemplateId: !Ref myLaunchTemplate
        Version: !GetAtt myLaunchTemplate.LatestVersionNumber
      MaxSize: '1'
      MinSize: '1'
      VPCZoneIdentifier: !Ref Subnets
```
 

### Auto Scaling group with CloudWatch monitoring enabled and custom tags

The following snippet shows an Auto Scaling group with CloudWatch monitoring enabled and custom tags. The `LaunchTemplate` property references an AWS::EC2::LaunchTemplate resource with the logical name `myLaunchTemplate` that is defined elsewhere in your template.

You specify the CloudWatch metrics to monitor using the `MetricsCollection` property. If you keep the metrics as they are, only `GroupMinSize` and `GroupMaxSize` metrics are enabled.

You specify the tag keys and tag key values for the `Tags` property. If you keep the provided tags, the first tag, `Environment`=`Production`, is assigned to the Auto Scaling group and to any EC2 instances launched as part of the Auto Scaling group. The second tag, `Purpose`=`WebServerGroup`, is assigned only to the Auto Scaling group itself.

You also specify values for the `MaxSize`, `MinSize`, and `VPCZoneIdentifier` properties.

#### JSON

```
{
    "Resources": {
        "myASG": {
            "Type": "AWS::AutoScaling::AutoScalingGroup",
            "Properties": {
                "LaunchTemplate": {
                    "LaunchTemplateId": { "Ref": "myLaunchTemplate" },
                    "Version": { "Fn::GetAtt": [ "myLaunchTemplate", "LatestVersionNumber" ] }
                },
                "MaxSize": "1",
                "MinSize": "1",
                "VPCZoneIdentifier": [
                    "subnetIdAz1",
                    "subnetIdAz2",
                    "subnetIdAz3"
                ],
                "MetricsCollection": [
                    {
                        "Granularity": "1Minute",
                        "Metrics": [
                            "GroupMinSize",
                            "GroupMaxSize"
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Key": "Environment",
                        "Value": "Production",
                        "PropagateAtLaunch": "true"
                    },
                    {
                        "Key": "Purpose",
                        "Value": "WebServerGroup",
                        "PropagateAtLaunch": "false"
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
---
Resources:
  myASG:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchTemplate:
        LaunchTemplateId: !Ref myLaunchTemplate
        Version: !GetAtt myLaunchTemplate.LatestVersionNumber
      MaxSize: '1'
      MinSize: '1'
      VPCZoneIdentifier:   
        - subnetIdAz1
        - subnetIdAz2
        - subnetIdAz3
      MetricsCollection: 
        - Granularity: 1Minute
          Metrics: 
            - GroupMinSize
            - GroupMaxSize
      Tags:
        - Key: Environment
          Value: Production
          PropagateAtLaunch: true
        - Key: Purpose
          Value: WebServerGroup
          PropagateAtLaunch: false
```
 

## See also 
You can find additional useful snippets in the following sections of the AWS CloudFormation User Guide:  
For examples of Auto Scaling groups, see Configure Amazon EC2 Auto Scaling resources. 
For examples of launch templates, see Create launch templates. 
Migrate AWS CloudFormation stacks from launch configurations to launch templates in the Amazon EC2 Auto Scaling User Guide 
CreateAutoScalingGroup and UpdateAutoScalingGroup in the Amazon EC2 Auto Scaling API Reference
