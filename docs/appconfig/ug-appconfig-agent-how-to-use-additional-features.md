> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use-additional-features.html
> Downloaded: 2026-10-21

# Using a manifest to enable additional retrieval features

AWS AppConfig Agent offers the following additional features to help you retrieve configurations for your applications.  
Configuring AWS AppConfig Agent to retrieve configurations from multiple accounts: Use AWS AppConfig Agent from a primary or retrieval AWS account to retrieve configuration data from multiple vendor accounts.  
Configuring AWS AppConfig Agent to write configuration copies to disk: Use AWS AppConfig Agent to write configuration data to disk. This feature enables customers with applications that read configuration data from disk to integrate with AWS AppConfig. 
 

## Understanding agent manifests 

To enable these AWS AppConfig Agent features, you create a manifest. A manifest is a set of configuration data that you provide to control actions the agent can perform. A manifest is written in JSON. It contains a set of top-level keys that correspond to different configurations you've deployed using AWS AppConfig. 

A manifest can include multiple configurations. Furthermore, each configuration in the manifest can identify one or more agent features to use for the specified configuration. The content of the manifest uses the following format: 

```
{
    "application_name:environment_name:configuration_name": {
        "agent_feature_to_enable_1": {
            "feature-setting-key": "feature-setting-value"
        },
        "agent_feature_to_enable_2": {
            "feature-setting-key": "feature-setting-value"
        }
    }
}
```
 

Here is example JSON for a manifest with two configurations. The first configuration (`MyApp`) doesn't use any AWS AppConfig Agent features. The second configuration (`My2ndApp`) uses the write configuration copy to disk and the multi-account retrieval features: 

```
{
        "MyApp:Test:MyAllowListConfiguration": {},
        
        "My2ndApp:Beta:MyEnableMobilePaymentsFeatureFlagConfiguration": {
            "credentials": {
                "roleArn": "arn:aws:us-west-1:iam::123456789012:role/MyTestRole",
                "roleExternalId": "00b148e2-4ea4-46a1-ab0f-c422b54d0aac",
                "roleSessionName": "AwsAppConfigAgent",
                "credentialsDuration": "2h"
            },
            "writeTo": {
                "path": "/tmp/aws-appconfig/my-2nd-app/beta/my-enable-payments-feature-flag-configuration.json"
            }
        }
    }
```
 How to supply an agent manifest 

You can store the manifest as a file in a location where AWS AppConfig Agent can read it. Or, you can store the manifest as an AWS AppConfig configuration and point the agent to it. To supply an agent manifest, you must set a `MANIFEST` environment variable with one of the following values:  
|  Manifest location |  Environment variable value |  Use case |    
|   

File  |   

file:/path/to/agent-manifest.json  |   

Use this method if your manifest won't change often.  |   
|   

AWS AppConfig configuration  |   

`application-name`:`environment-name`:`configuration-name`  |   

Use this method for dynamic updates. You can update and deploy a manifest stored in AWS AppConfig as a configuration in the same ways you store other AWS AppConfig configurations.  |   
|   

Environment variable  |   

Manifest content (JSON)  |   

Use this method if your manifest won't change often. This method is useful in container environments where it's easier to set an environment variable than it is to expose a file.  |    

For more information about setting variables for AWS AppConfig Agent, see the relevant topic for your use case:  
Configuring the AWS AppConfig Agent Lambda extension 
Using AWS AppConfig Agent with Amazon EC2 
Using AWS AppConfig Agent with Amazon ECS and Amazon EKS
