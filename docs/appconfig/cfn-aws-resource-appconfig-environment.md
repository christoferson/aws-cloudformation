> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-environment.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Environment

The `AWS::AppConfig::Environment` resource creates an environment, which is a logical deployment group of AWS AppConfig targets, such as applications in a `Beta` or `Production` environment. You define one or more environments for each AWS AppConfig application. You can also define environments for application subcomponents such as the `Web`, `Mobile` and `Back-end` components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

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
  "Type" : "AWS::AppConfig::Environment",
  "Properties" : {
      "ApplicationId" : String,
      "DeletionProtectionCheck" : String,
      "Description" : String,
      "Monitors" : [ Monitor, ... ],
      "Name" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::Environment
Properties:
  ApplicationId: String
  DeletionProtectionCheck: String
  Description: String
  Monitors: 
    - Monitor
  Name: String
  Tags: 
    - Tag

```

## Properties

**`ApplicationId`** 

The ID or name of the application. 

Required: Yes

Type: String

Pattern: `[a-z0-9]{4,7}`

Update requires: Replacement

**`DeletionProtectionCheck`** 

A parameter to configure deletion protection. Deletion protection prevents a user from deleting an environment if your application called either GetLatestConfiguration or GetConfiguration in the environment during the specified interval.  

This parameter supports the following values:  
`BYPASS`: Instructs AWS AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it.  
`APPLY`: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. `APPLY` also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks. 
`ACCOUNT_DEFAULT`: The default setting, which instructs AWS AppConfig to implement the deletion protection value specified in the `UpdateAccountSettings` API. 
 

Required: No

Type: String

Allowed values: `ACCOUNT_DEFAULT | APPLY | BYPASS`

Update requires: No interruption

**`Description`** 

A description of the environment. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`Monitors`** 

Amazon CloudWatch alarms to monitor during the deployment process. 

Required: No

Type: Array of Monitor

Minimum: `0`

Maximum: `5`

Update requires: No interruption

**`Name`** 

A name for the environment. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: No interruption

**`Tags`** 

Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. 

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the environment ID.

### Fn::GetAtt

#### 

**`EnvironmentId`** 

The environment ID. 

## Examples

 

### AWS AppConfig environment example

The following example creates an AWS AppConfig environment named MyTestEnvironment. An environment is a logical deployment group of AWS AppConfig targets, such as applications in a Beta or Production environment. You can also define environments for application subcomponents such as the Web, Mobile, and Back-end components for your application. 

#### JSON

```
Resources": {
    "BasicEnvironment": {
      "Type": "AWS::AppConfig::Environment",
      "DependsOn": "DependentApplication",
      "Properties": {
        "ApplicationId": null,
        "Name": "MyTestEnvironment",
        "Description": "My test environment",
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
  BasicEnvironment:
    Type: AWS::AppConfig::Environment
    Properties:
      ApplicationId: !Ref DependentApplication
      Name: "MyTestEnvironment"
      Description: "My test environment"
      Tags:
        - Key: Env
          Value: test

```
 

## See also 
 AWS AppConfig  
 Creating an environment
