> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-simplified-methods.html
> Downloaded: 2026-10-21

# Retrieving feature flags and configuration data in AWS AppConfig

Your application retrieves feature flags and free form configuration data by establishing a configuration session using the AWS AppConfig Data service. We recommended you use AWS AppConfig Agent to retrieve configuration data. The agent (or the AWS AppConfig Agent Lambda extension for Lambda compute environments) manages a series of API calls and session tokens on your behalf. From a high level, the process works as follows: 
You configure AWS AppConfig Agent as a local host and have the agent poll AWS AppConfig for configuration updates. 
The agent calls the StartConfigurationSession and GetLatestConfiguration API actions and caches your configuration data locally. 
To retrieve the data, your application makes an HTTP call to the localhost server. AWS AppConfig Agent supports several use cases, as described in How to use AWS AppConfig Agent to retrieve configuration data. 

If you prefer, you can manually call these API actions to retrieve a configuration. The API process works as follows: 
Your application establishes a configuration session using the `StartConfigurationSession` API action. Your session's client then makes periodic calls to `GetLatestConfiguration` to check for and retrieve the latest data available. 
When calling `StartConfigurationSession`, your code sends identifiers (ID or name) of an AWS AppConfig application, environment, and configuration profile that the session tracks. 
In response, AWS AppConfig provides an `InitialConfigurationToken` to be given to the session's client and used the first time it calls `GetLatestConfiguration` for that session. 
When calling `GetLatestConfiguration`, your client code sends the most recent `ConfigurationToken` value it has and receives in response:  
`NextPollConfigurationToken`: the `ConfigurationToken` value to use on the next call to `GetLatestConfiguration`. 
The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration. 
 
Note

Retrieving configuration data from a separate AWS account isn't supported.Contents
What is AWS AppConfig Agent?
How to use AWS AppConfig Agent to retrieve configuration data
