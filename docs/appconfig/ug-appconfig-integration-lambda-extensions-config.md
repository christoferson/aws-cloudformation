> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-config.html
> Downloaded: 2026-10-21

# Configuring the AWS AppConfig Agent Lambda extension

You can configure the extension by changing the following AWS Lambda environment variables. For more information, see Using AWS Lambda environment variables in the AWS Lambda Developer Guide. 

Prefetching configuration data

The environment variable `AWS_APPCONFIG_EXTENSION_PREFETCH_LIST` can improve the start-up time of your function. When the AWS AppConfig Agent Lambda extension is initialized, it retrieves the specified configuration from AWS AppConfig before Lambda starts to initialize your function and invoke your handler. In some cases, the configuration data is already available in the local cache before your function requests it. 

To use the prefetch capability, set the value of the environment variable to the path corresponding to your configuration data. For example, if your configuration corresponds to an application, environment, and configuration profile respectively named "my_application", "my_environment", and "my_configuration_data", the path would be `/applications/my_application/environments/my_environment/configurations/my_configuration_data`. You can specify multiple configuration items by listing them as a comma-separated list (If you have a resource name that includes a comma, use the resource's ID value instead of its name). 

Accessing configuration data from another account

The AWS AppConfig Agent Lambda extension can retrieve configuration data from another account by specifying an IAM role that grants permissions to the data. To set this up, follow these steps:  
In the account where AWS AppConfig is used to manage the configuration data, create a role with a trust policy that grants the account running the Lambda function access to the `appconfig:StartConfigurationSession` and `appconfig:GetLatestConfiguration` actions, along with the partial or complete ARNs corresponding to the AWS AppConfig configuration resources. 
In the account running the Lambda function, add the `AWS_APPCONFIG_EXTENSION_ROLE_ARN` environment variable to the Lambda function with the ARN of the role created in step 1. 
(Optional) If needed, an external ID can be specified using the `AWS_APPCONFIG_EXTENSION_ROLE_EXTERNAL_ID` environment variable. Similarly, a session name can be configured using the `AWS_APPCONFIG_EXTENSION_ROLE_SESSION_NAME` environment variable. 
Note

Note the following information. 
The AWS AppConfig Agent Lambda extension can only retrieve data from one account. If you specify an IAM role, the extension will not be able to retrieve configuration data from the account in which the Lambda function is running. 
AWS Lambda logs information about the AWS AppConfig Agent Lambda extension and the Lambda function by using Amazon CloudWatch Logs.  
The following table includes a Sample values column. Depending on your monitor resolution, you might need to scroll to the bottom of the table and then scroll to the right to view the column. 
 
|  Environment variable |  Details |  Default value |  Sample values |    
|   

`AWS_APPCONFIG_EXTENSION_EXPERIMENT_ASSIGNMENT_LOG_DESTINATION`  |   

This environment variable enables AWS AppConfig Agent to log experiment assignment records, which capture each occurrence of an experiment treatment being assigned to a given entity at a given time. Possible values: `file:<path>/` indicates a base directory under which assignment records are written to disk; `stderr` indicates that assignment records are emitted to stderr. This feature requires AWS AppConfig Agent Lambda extension version 2.0.20159 or later.  |  None |   

`file:/tmp/aws-appconfig/assignments/` 

`stderr`  |   
|   

`AWS_APPCONFIG_EXTENSION_HTTP_PORT`  |   

This environment variable specifies the port on which the local HTTP server that hosts the extension runs.  |  2772 |  2772 |   
|   

`AWS_APPCONFIG_EXTENSION_LOG_LEVEL`  |   

This environment variable specifies the level of detail that the agent logs. Each level includes the current level and all higher levels. The value is case insensitive. From most to least detailed, the log levels are: `trace`, `debug`, `info`, `warn`, `error`, `fatal`, and `none`. The `trace` log includes detailed information, including timing information, about the agent.  |   

info  |  

trace 

debug 

info 

warn 

error 

fatal 

none |   
|   

`AWS_APPCONFIG_EXTENSION_MAX_CONNECTIONS`  |   

This environment variable configures the maximum number of connections the extension uses to retrieve configurations from AWS AppConfig.   |  3 |  3 |   
|   

`AWS_APPCONFIG_EXTENSION_POLL_INTERVAL_SECONDS`  |   

This environment variable controls how often the agent polls AWS AppConfig for updated configuration data. You can specify a number of seconds for the interval. You can also specify a number with a time unit: s for seconds, m for minutes, and h for hours. If a unit isn't specified, the agent defaults to seconds. For example, 60, 60s, and 1m result in the same poll interval.   |  45 |  

45

45s

5m

1h |   
|   

`AWS_APPCONFIG_EXTENSION_POLL_TIMEOUT_MILLIS`  |   

This environment variable controls the maximum amount of time, in milliseconds, the extension waits for a response from AWS AppConfig when refreshing data in the cache. If AWS AppConfig does not respond in the specified amount of time, the extension skips this poll interval and returns the previously updated cached data.  |  3000ms |  

3000

300ms

5s |   
|   

`AWS_APPCONFIG_EXTENSION_PREFETCH_LIST`  |   

This environment variable specifies the configuration data the agent requests from AWS AppConfig as soon as it starts. Multiple configuration identifiers may be provided in a comma-separated list. Prefetching configuration data from AWS AppConfig can reduce the cold start time of your function significantly.  |  None |  

MyApp:MyEnv:MyConfig

abcd123:efgh456:ijkl789

MyApp:MyEnv:Config1,MyApp:MyEnv:Config2 |   
|  `AWS_APPCONFIG_EXTENSION_PROXY_HEADERS` |  This environment variable specifies headers required by the proxy referenced in the `AWS_APPCONFIG_EXTENSION_PROXY_URL` environment variable. The value is a comma-separated list of headers. |  None |  

header: value

h1: v1, h2: v2 |   
|  `AWS_APPCONFIG_EXTENSION_PROXY_URL` |  This environment variable specifies the proxy URL to use for connections from the AWS AppConfig extension to AWS services. `HTTPS` and `HTTP` URLs are supported. |  None |  

http://localhost:7474

https://my-proxy.example.com |   
|  `AWS_APPCONFIG_EXTENSION_ROLE_ARN` |  This environment variable specifies the IAM role ARN corresponding to a role that should be assumed by the AWS AppConfig extension to retrieve configuration. |  None |  arn:aws:iam::123456789012:role/MyRole |   
|  `AWS_APPCONFIG_EXTENSION_ROLE_EXTERNAL_ID` |  This environment variable specifies the external id to use in conjunction with the assumed role ARN. |  None |  MyExternalId |   
|  `AWS_APPCONFIG_EXTENSION_ROLE_SESSION_NAME` |  This environment variable specifies the session name to be associated with the credentials for the assumed IAM role. |  None |  AWSAppConfigAgentSession |   
|  `AWS_APPCONFIG_EXTENSION_SERVICE_REGION` |  This environment variable specifies an alternative Region the extension should use to call the AWS AppConfig service. When undefined, the extension uses the endpoint in the current Region. |  None |  

us-east-1

eu-west-1 |   
|   

`AWS_APPCONFIG_EXTENSION_MANIFEST`  |   

This environment variable configures AWS AppConfig Agent to take advantage of additional per-configuration features like multi-account retrievals and save configuration to disk. For more information about these features, see Using a manifest to enable additional retrieval features.   |  None |  

When using AWS AppConfig configuration as manifest: `MyApp:MyEnv:MyManifestConfig`.

When loading manifest from disk: `file:/path/to/manifest.json` |   
|   

`AWS_APPCONFIG_EXTENSION_WAIT_ON_MANIFEST`  |   

This environment variable configures AWS AppConfig Agent to wait until the manifest is processed before completing startup.  |  true |  

true

false |
