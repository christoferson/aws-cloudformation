> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-deploymentstrategy.html
> Downloaded: 2026-10-21

# AWS::AppConfig::DeploymentStrategy

The `AWS::AppConfig::DeploymentStrategy` resource creates an AWS AppConfig deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

AWS AppConfig requires that you create resources and deploy a configuration in the following order: 
Create an application 
Create an environment 
Create a configuration profile 
Choose a pre-defined deployment strategy or create your own 
Deploy the configuration 

For more information, see AWS AppConfig in the AWS AppConfig User Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AppConfig::DeploymentStrategy",
  "Properties" : {
      "DeploymentDurationInMinutes" : Number,
      "Description" : String,
      "FinalBakeTimeInMinutes" : Number,
      "GrowthFactor" : Number,
      "GrowthType" : String,
      "Name" : String,
      "ReplicateTo" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::DeploymentStrategy
Properties:
  DeploymentDurationInMinutes: Number
  Description: String
  FinalBakeTimeInMinutes: Number
  GrowthFactor: Number
  GrowthType: String
  Name: String
  ReplicateTo: String
  Tags: 
    - Tag

```

## Properties

**`DeploymentDurationInMinutes`** 

Total amount of time for a deployment to last. Note

AWS AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see Using AWS AppConfig Agent for user-based or entity-based gradual deployments 

Required: Yes

Type: Number

Minimum: `0`

Maximum: `1440`

Update requires: No interruption

**`Description`** 

A description of the deployment strategy. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`FinalBakeTimeInMinutes`** 

Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see Configuring permissions for rollback based on Amazon CloudWatch alarms in the AWS AppConfig User Guide. 

Required: No

Type: Number

Minimum: `0`

Maximum: `1440`

Update requires: No interruption

**`GrowthFactor`** 

The percentage of targets to receive a deployed configuration during each interval. 

Required: Yes

Type: Number

Update requires: No interruption

**`GrowthType`** 

The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types: 

Linear: For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for `Step percentage`. For example, a linear deployment that uses a `Step percentage` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration. 

Exponential: For this type, AWS AppConfig processes the deployment exponentially using the following formula: `G*(2^N)`. In this formula, `G` is the growth factor specified by the user and `N` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: 

 `2*(2^0)`  

 `2*(2^1)`  

 `2*(2^2)`  

Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets. 

Required: No

Type: String

Allowed values: `EXPONENTIAL | LINEAR`

Update requires: No interruption

**`Name`** 

A name for the deployment strategy. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`ReplicateTo`** 

Save the deployment strategy to a Systems Manager (SSM) document. 

Required: Yes

Type: String

Allowed values: `NONE | SSM_DOCUMENT`

Update requires: Replacement

**`Tags`** 

Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource. 

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the deployment strategy ID.

### Fn::GetAtt

#### 

**`Id`** 

The deployment strategy ID. 

## Examples

 

### AWS AppConfig deployment strategy example

The following example creates an AWS AppConfig deployment strategy called MyTestDeploymentStrategy. A deployment strategy defines how a configuration is deployed.

#### JSON

```
Resources": {
    "BasicDeploymentStrategy": {
      "Type": "AWS::AppConfig::DeploymentStrategy",
      "Properties": {
        "Name": "MyTestDeploymentStrategy",
        "Description": "A sample test deployment strategy.",
        "DeploymentDurationInMinutes": 3,
        "FinalBakeTimeInMinutes": 4,
        "GrowthFactor": 10,
        "GrowthType": "LINEAR",
        "ReplicateTo": "NONE",
        "Tags": [
          {
            "Key": "Env",
            "Value": "test"
          }
        ]
      }
    }
  }
}

```

#### YAML

```
Resources:
  BasicDeploymentStrategy:
    Type: AWS::AppConfig::DeploymentStrategy
    Properties:
      Name: "MyTestDeploymentStrategy"
      Description: "A sample test deployment strategy."
      DeploymentDurationInMinutes: 3
      FinalBakeTimeInMinutes: 4
      GrowthFactor: 10
      GrowthType: LINEAR
      ReplicateTo: NONE
      Tags:
        - Key: Env
          Value: test

```
 

## See also 
 AWS AppConfig  
 Creating a deployment strategy
