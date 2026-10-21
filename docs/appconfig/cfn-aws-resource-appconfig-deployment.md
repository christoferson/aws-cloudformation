> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-deployment.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Deployment

The `AWS::AppConfig::Deployment` resource starts a deployment. Starting a deployment in AWS AppConfig calls the `StartDeployment` API action. This call includes the IDs of the AWS AppConfig application, the environment, the configuration profile, and (optionally) the configuration data version to deploy. The call also includes the ID of the deployment strategy to use, which determines how the configuration data is deployed.

AWS AppConfig monitors the distribution to all hosts and reports status. If a distribution fails, then AWS AppConfig rolls back the configuration. 

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
  "Type" : "AWS::AppConfig::Deployment",
  "Properties" : {
      "ApplicationId" : String,
      "ConfigurationProfileId" : String,
      "ConfigurationVersion" : String,
      "DeploymentStrategyId" : String,
      "Description" : String,
      "DynamicExtensionParameters" : [ DynamicExtensionParameters, ... ],
      "EnvironmentId" : String,
      "KmsKeyIdentifier" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::Deployment
Properties:
  ApplicationId: String
  ConfigurationProfileId: String
  ConfigurationVersion: String
  DeploymentStrategyId: String
  Description: String
  DynamicExtensionParameters: 
    - DynamicExtensionParameters
  EnvironmentId: String
  KmsKeyIdentifier: String
  Tags: 
    - Tag

```

## Properties

**`ApplicationId`** 

The ID or name of the application. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`ConfigurationProfileId`** 

The ID or name of the configuration profile. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `128`

Update requires: Replacement

**`ConfigurationVersion`** 

The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `1024`

Update requires: Replacement

**`DeploymentStrategyId`** 

The deployment strategy ID. 

Required: Yes

Type: String

Pattern: `[a-z0-9]{4,7}`

Update requires: Replacement

**`Description`** 

A description of the deployment. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: Replacement

**`DynamicExtensionParameters`** 

A map of dynamic extension parameter names to values to pass to associated extensions with `PRE_START_DEPLOYMENT` actions. 

Required: No

Type: Array of DynamicExtensionParameters

Update requires: Replacement

**`EnvironmentId`** 

The ID or name of the environment. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`KmsKeyIdentifier`** 

The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated. 

Required: No

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`Tags`** 

Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. 

Required: No

Type: Array of Tag

Update requires: Replacement

## Return values

### Ref

### Fn::GetAtt

#### 

**`DeploymentNumber`** 

The sequence number of the deployment. 

**`State`** 

The state of the deployment. 

## Examples

 

### AWS AppConfig deployment example

The following example creates an AWS AppConfig deployment. Starting a deployment in AWS AppConfig calls the StartDeployment API action. This call includes the IDs of the AWS AppConfig application, the environment, the configuration profile, and (optionally) the configuration data version to deploy. The call also includes the ID of the deployment strategy to use, which determines how the configuration data is deployed.

AWS AppConfig monitors the distribution to all hosts and reports status. If a distribution fails, then AWS AppConfig rolls back the configuration. 

#### JSON

```
Resources": {
    "BasicDeployment": {
      "Type": "AWS::AppConfig::Deployment",
      "DependsOn": [
        "MyTestApplication",
        "MyTestConfigurationProfile",
        "MyTestEnvironment",
        "MyTestDeploymentStrategy"
      ],
      "Properties": {
        "ApplicationId": MyTestApplication,
        "EnvironmentId": MyTestEnvironment,
        "DeploymentStrategyId": MyTestDeploymentStrategy,
        "ConfigurationProfileId": MyTestConfigurationProfile,
        "ConfigurationVersion": "1",
        "Description": "My test deployment",
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
  BasicDeployment:
    Type: AWS::AppConfig::Deployment
    Properties:
      ApplicationId: !Ref MyTestApplication
      EnvironmentId: !Ref MyTestEnvironment
      DeploymentStrategyId: !Ref MyTestDeploymentStrategy
      ConfigurationProfileId: !Ref MyTestConfigurationProfile
      ConfigurationVersion: '1'
      Description: 'My test deployment'
      Tags:
        - Key: Env
          Value: test

```
 

## See also 
 AWS AppConfig  
 Deploying a configuration
