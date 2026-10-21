> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html
> Downloaded: 2026-10-21

# Using AWS AppConfig Agent with AWS Lambda

An AWS Lambda extension is a companion process that augments the capabilities of a Lambda function. An extension can start before a function is invoked, run in parallel with a function, and continue to run after a function invocation is processed. In essence, a Lambda extension is like a client that runs in parallel to a Lambda invocation. This parallel client can interface with your function at any point during its lifecycle.

If you use AWS AppConfig feature flags or other dynamic configuration data in a Lambda function, then we recommend that you add the AWS AppConfig Agent Lambda extension as a layer to your Lambda function. This makes calling feature flags simpler, and the extension itself includes best practices that simplify using AWS AppConfig while reducing costs. Reduced costs result from fewer API calls to the AWS AppConfig service and shorter Lambda function processing times. For more information about Lambda extensions, see Lambda extensions in the AWS Lambda Developer Guide.Note

AWS AppConfig is a capability of AWS Systems Manager. AWS AppConfig pricing is based on the number of times a configuration is called and received. Your costs increase if your Lambda performs multiple cold starts and retrieves new configuration data frequently. Topics
Understanding how the AWS AppConfig Agent Lambda extension works
Adding the AWS AppConfig Agent Lambda extension
Configuring the AWS AppConfig Agent Lambda extension
Understanding available versions of the AWS AppConfig Agent Lambda extension
