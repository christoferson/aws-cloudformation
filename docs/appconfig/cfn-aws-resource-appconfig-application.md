> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-application.html
> Downloaded: 2026-10-21

# AWS::AppConfig::Application

The `AWS::AppConfig::Application` resource creates an application. In AWS AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

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
  "Type" : "AWS::AppConfig::Application",
  "Properties" : {
      "Description" : String,
      "Name" : String,
      "Tags" : [ Tags, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::Application
Properties:
  Description: String
  Name: String
  Tags: 
    - Tags

```

## Properties

**`Description`** 

A description of the application. 

Required: No

Type: String

Minimum: `0`

Maximum: `1024`

Update requires: No interruption

**`Name`** 

A name for the application. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: No interruption

**`Tags`** 

Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. 

Required: No

Type: Array of Tags

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`ApplicationId`** 

The application ID. 

## Examples

 

### AWS AppConfig application example

The following example creates a simple AWS AppConfig application named MyTestApplication. An application in AWS AppConfig is a logical unit of code that provides capabilities for your customers. For example, an application can be a microservice that runs on Amazon EC2 instances, a mobile application installed by your users, a serverless application using Amazon API Gateway and AWS Lambda, or any system you run on behalf of others. 

#### JSON

```
BasicApplication": {
    "Type": "AWS::AppConfig::Application",
    "Properties": {
      "Name": "MyTestApplication",
      "Description": "A sample test application.",
      "Tags": [
        {
          "Key": "Env",
          "Value": "test"
        }
      ]
    }
  }
}

```

#### YAML

```
BasicApplication:
    Type: AWS::AppConfig::Application
    Properties:
      Name: "MyTestApplication"
      Description: "A sample test application."
      Tags:
        - Key: Env
          Value: test

```
 

## See also 
 AWS AppConfig  
 Creating an Application
