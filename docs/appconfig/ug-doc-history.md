> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/doc-history.html
> Downloaded: 2026-10-21

# AWS AppConfig User Guide document history

The following table describes the important changes to the documentation since the last release of AWS AppConfig.

Current API version: 2019-10-09
| Change | Description | Date | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated with minor enhancements and bug fixes. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

August 24, 2026 | 
| 

AWS AppConfig experimentation assignment logging and treatment retrieval | 

AWS AppConfig Agent can now log experiment treatment assignment records to stderr or to disk, and emits aggregated treatment traffic as CloudWatch metrics. New documentation describes the `EXPERIMENT_ASSIGNMENT_LOG_DESTINATION` agent option, how to retrieve an assigned treatment by using the `Entity-Id` and `Context` headers, and the minimum agent versions that support experimentation. For more information, see About data collection. | 

August 21, 2026 | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated with minor enhancements and bug fixes. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

June 22, 2026 | 
| 

Launch of AWS AppConfig experimentation | 

Application experimentation is the systematic process of testing hypotheses on software applications using A/B testing, feature flags, and analytics to measure user behavior, optimize performance, and drive data-driven product decisions. Experimentation enables teams to validate changes, such as new features or UI changes, before a full rollout, thereby reducing risk and improving engagement.

Built with the expertise of more than 20 years of software experimentation on Amazon.com, AWS AppConfig experimentation integrates seamlessly with your existing AWS AppConfig workflows, providing a comprehensive solution for feature management and experimentation in cloud-native applications. AWS AppConfig experimentation offers the following features:  
Support for multiple feature and test types – A/B tests, multivariate tests, and gradual feature rollouts.
Easy experiment setup and management through the AWS Management Console.
Powerful and flexible segmentation options for experiment participants.
Data independence – use your existing data warehouses and analytics tools for experiments or use an AWS-native service like Amazon CloudWatch RUM.

Additionally, AWS AppConfig experimentation includes automatic rollback capabilities that can revert to a safe configuration if predefined thresholds are exceeded. For example, you can monitor key metrics like page load, conversion rate, or page errors during an experiment. If a threshold is breached, the experiment will be stopped. You can set these safety monitoring capabilities using Amazon CloudWatch, Datadog, New Relic, Dynatrace, and more. For more information, see AWS AppConfig experimentation. | 

June 12, 2026 | 
| 

Entity-based targeting | 

AWS AppConfig Agent (version 2.0.136060 or later) supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see Using AWS AppConfig Agent for user- or entity-based gradual deployments. | 

March 26, 2026 | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated with minor enhancements and bug fixes. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

February 20, 2026 | 
| 

Deprecated: AWS AppConfig extension for CloudWatch Evidently | 

The AWS AppConfig extension for CloudWatch Evidently is no longer supported. | 

February 20, 2026 | 
| 

IPv6 support | 

All AWS AppConfig APIs now fully support IPv4 and IPv6 calls. For more information, see Understanding IPv6 support. | 

April 23, 2025 | 
| 

New topic: Saving a previous feature flag version to a new version | 

When you update a feature flag, AWS AppConfig automatically saves your changes to a new version. If you want to use a previous feature flag version, you must copy it to a draft version and then save it. You can't edit and save changes to a previous flag version without saving it to a new version. For more information, see Saving a previous feature flag version to a new version. | 

April 15, 2025 | 
| 

New topic: Feature flag samples for AWS AppConfig Agent local development mode | 

AWS AppConfig Agent supports a local development mode. If you enable local development mode, the agent reads configuration data from a specified directory on disk. It doesn't retrieve configuration data from AWS AppConfig. To help you better understand how to use local development mode, this guide now contains a topic with feature flag samples. For more information, see Feature flag samples for AWS AppConfig Agent local development mode. | 

February 18, 2025 | 
| 

New topic: Creating a configuration profile for non-native data sources | 

The topic describes the high level process for using an AWS AppConfig extension to retrieve configuration data from sources that are not natively supported, including other AWS services like Amazon RDS and Amazon DynamoDB, as well as 3rd-party sources like GitHub, GitLab, or a local repo. For more information, see Creating a configuration profile for non-native data sources | 

December 19, 2024 | 
| 

Updated topic: Fixed regex in feature flags type reference | 

The json schema in the feature flag type reference previously showed the following regex pattern in various places: `"^[a-z][a-zA-Z\\d-_]{0,63}$"`. The correct regex pattern is `"^[a-z][a-zA-Z\\d_-]{0,63}$"`. The hyphen is listed after the underscore. For more information, see Understanding the type reference for AWS.AppConfig.FeatureFlags | 

December 18, 2024 | 
| 

Updated topics: Environment variable samples added | 

The tables describing environment variable in the following topics were updated to include samples: 
(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS 
(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon EC2 
Configuring the AWS AppConfig Agent Lambda extension 
 | 

December 12, 2024 | 
| 

New section: Understanding the split operator | 

A new section uses examples to explain how the `split` operator works for a multi-variant feature flag rule. For more information, see Understanding multi-variant feature flag rules. | 

November 22, 2024 | 
| 

New extension action point: AT_DEPLOYMENT_TICK | 

AWS AppConfig launched a new action point for users who create custom extensions. The `AT_DEPLOYMENT_TICK` action point supports third-party monitoring integration. `AT_DEPLOYMENT_TICK` is invoked during configuration deployment processing orchestration. If you use a third-party monitoring solution (for example, Datadog), you can create an AWS AppConfig extension that checks for alarms at the `AT_DEPLOYMENT_TICK` action point and, as a safety guardrail, rolls back the deployment if it triggered an alarm. For more information about AWS AppConfig extensions, see Extending AWS AppConfig workflows using extensions. For more information about custom extensions, see Walkthrough: Creating custom AWS AppConfig extensions. To view a code sample of an AWS AppConfig extension that uses the `AT_DEPLOYMENT_TICK` action point to integrate with Datadog, see aws-samples / aws-appconfig-tick-extn-for-datadog on GitHub. | 

November 22, 2024 | 
| 

New topic: AWS AppConfig mobile use considerations | 

A new topic in this guide describes important considerations for using AWS AppConfig feature flags with mobiles devices. For more information, see AWS AppConfig mobile use considerations. | 

November 21, 2024 | 
| 

New feature: AWS AppConfig Deletion Protection | 

AWS AppConfig now provides an account setting to help prevent users from unintentionally deleting actively-used environments and configuration profiles. For more information, see Configuring AWS AppConfig deletion protection. | 

August 28, 2024 | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated with minor enhancements and bug fixes. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

August 9, 2024 | 
| 

New code samples for retrieving flag variants | 

For more information, see Using AWS AppConfig Agent to retrieve a feature flag with variants. | 

August 9, 2024 | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated to support feature flag targets, variants, and splits. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

July 23, 2024 | 
| 

New feature: Multi-variant feature flags | 

Multi-variant feature flags enable you to define a set of possible flag values to return for a request. You can also configure different statuses (enabled or disabled) for multi-variant flags. When requesting a flag configured with variants, your application provides context that AWS AppConfig evaluates against a set of user-defined rules. Depending on the context specified in the request and the rules defined for the variant, AWS AppConfig returns different flag values to the application. For more information, see Creating multi-variant feature flags. | 

July 23, 2024 | 
| 

New version of AWS AppConfig Agent Lambda extension | 

The agent has been updated with minor enhancements and bug fixes. To view the new Amazon Resource Names (ARNs) for the extension, see Available versions of the AWS AppConfig Agent Lambda extension. | 

February 28, 2024 | 
| 

AWS AppConfig custom extension samples | 

The Walkthrough: Creating custom AWS AppConfig extensions topic now includes links to the following sample extensions on GitHub: 
Sample extension that prevents deployments with a `blocked day` moratorium calendar using Systems Manager Change Calendar 
Sample extension that prevents secrets from leaking into configuration data using git-secrets 
Sample extension that prevents personally identifiable information (PII) from leaking into configuration data using Amazon Comprehend 
 | 

February 28, 2024 | 
| 

New topic: Logging AWS AppConfig API calls using AWS CloudTrail | 

AWS AppConfig is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS AppConfig. CloudTrail captures all API calls for AWS AppConfig as events. This new topic provides AWS AppConfig-specific content rather than linking to the corresponding content in the AWS Systems Manager User Guide. For more information, see Logging AWS AppConfig API calls using AWS CloudTrail. | 

January 18, 2024 | 
| 

AWS AppConfig now supports AWS PrivateLink | 

You can use AWS PrivateLink to create a private connection between your VPC and AWS AppConfig. You can access AWS AppConfig as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access AWS AppConfig. For more information, see Access AWS AppConfig using an interface endpoint (AWS PrivateLink). | 

December 6, 2023 | 
| 

Additional AWS AppConfig Agent retrieval features and a new local development mode | 

AWS AppConfig Agent offers the following additional features to help you retrieve configurations for your applications. 

Additional retrieval features 
Multi-account retrieval: Use AWS AppConfig Agent from a primary or retrieval AWS account to retrieve configuration data from multiple vendor accounts.  
Write configuration copy to disk: Use AWS AppConfig Agent to write configuration data to disk. This feature enables customers with applications that read configuration data from disk to integrate with AWS AppConfig. 
Note

Write configuration to disk is not designed as a configuration backup feature. AWS AppConfig Agent doesn't read from the configuration files copied to disk. If you want to back up configurations to disk, see the `BACKUP_DIRECTORY` and `PRELOAD_BACKUP` environment variables for Using AWS AppConfig Agent with Amazon EC2 or Using AWS AppConfig Agent with Amazon ECS and Amazon EKS.

Local development mode

AWS AppConfig Agent supports a local development mode. If you enable local development mode, the agent reads configuration data from a specified directory on disk. It doesn't retrieve configuration data from AWS AppConfig. You can simulate configuration deployments by updating files in the specified directory. We recommend local development mode for the following use cases: 
Test different configuration versions before deploying them using AWS AppConfig. 
Test different configuration options for a new feature before commiting changes to your code repository. 
Test different configuration scenarios to verify they work as expected. 
 | 

December 1, 2023 | 
| 

New code samples topic | 

Added a new code samples topic to this guide. The topic includes examples in Java, Python, and JavaScript for programmatically performing six common AWS AppConfig actions. | 

November 17, 2023 | 
| 

Revised table of contents to better reflect AWS AppConfig workflow | 

Content in this user guide is now grouped under the headings Creating, Deploying, Retrieving, and Extending workflows. This organization better reflects the workflow for using AWS AppConfig and aims to help make content more discoverable. | 

November 7, 2023 | 
| 

Payload reference added | 

The Creating a Lambda function for a custom AWS AppConfig extension topic now includes a request and response payload reference. | 

November 7, 2023 | 
| 

New AWS predefined deployment strategy | 

AWS AppConfig now offers and recommends the `AppConfig.Linear20PercentEvery6Minutes` predefined deployment strategy. For more information, see Predefined deployment strategies. | 

August 11, 2023 | 
| 

AWS AppConfig integration with Amazon EC2 | 

You can integrate AWS AppConfig with applications running on your Amazon Elastic Compute Cloud (Amazon EC2) Linux instances by using AWS AppConfig Agent. The agent supports x86_64 and ARM64 architectures for Amazon EC2. For more information, see AWS AppConfig integration with Amazon EC2. | 

July 20, 2023 | 
| 

CloudFormation support for new AWS AppConfig resources and a feature flag example | 

AWS CloudFormation now supports the AWS::AppConfig::Extension and AWS::AppConfig::ExtensionAssociation resources to help you get started with AWS AppConfig extensions.

The AWS::AppConfig::ConfigurationProfile and AWS::AppConfig::HostedConfigurationVersion resources now include an example for creating a feature flag configuration profile in the AWS AppConfig hosted configuration store.  | 

April 12, 2023 | 
| 

AWS AppConfig integration with AWS Secrets Manager | 

AWS AppConfig integrates with AWS Secrets Manager. Secrets Manager helps you to securely encrypt, store, and retrieve credentials for your databases and other services. Instead of hardcoding credentials in your apps, you can make calls to Secrets Manager to retrieve your credentials whenever needed. Secrets Manager helps you protect access to your IT resources and data by enabling you to rotate and manage access to your secrets.

When you create a freeform configuration profile, you can choose Secrets Manager as the source of your configuration data. You must onboard with Secrets Manager and create a secret before you create the configuration profile. For more information about Secrets Manager, see What is AWS Secrets Manager? in the AWS Secrets Manager User Guide. For information about creating a configuration profile, see Creating a freeform configuration profile. | 

February 2, 2023 | 
| 

AWS AppConfig integration with Amazon ECS and Amazon EKS | 

You can integrate AWS AppConfig with Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) by using the AWS AppConfig agent. The agent functions as a sidecar container running alongside your Amazon ECS and Amazon EKS container applications. The agent enhances containerized application processing and management in the following ways: 
The agent calls AWS AppConfig on your behalf by using an AWS Identity and Access Management (IAM) role and managing a local cache of configuration data. By pulling configuration data from the local cache, your application requires fewer code updates to manage configuration data, retrieves configuration data in milliseconds, and isn't affected by network issues that can disrupt calls for such data. 
The agent offers a native experience for retrieving and resolving AWS AppConfig feature flags. 
Out of the box, the agent provides best practices for caching strategies, polling intervals, and local configuration data availability while tracking the configuration tokens needed for subsequent service calls. 
While running in the background, the agent periodically polls the AWS AppConfig data plane for configuration data updates. Your containerized application can retrieve the data by connecting to localhost on port 2772 (a customizable default port value) and calling HTTP GET to retrieve the data. 
The AWS AppConfig agent updates configuration data in your containers without having to restart or recycle those containers. 

For more information, see AWS AppConfig integration with Amazon ECS and Amazon EKS. | 

December 2, 2022 | 
| 

New extension: AWS AppConfig extension for CloudWatch Evidently | 

You can use Amazon CloudWatch Evidently to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can monitor the performance of the new feature to help you decide when to ramp up traffic to your users. This helps you reduce risk and identify unintended consequences before you fully launch the feature. You can also conduct A/B experiments to make feature design decisions based on evidence and data.

The AWS AppConfig extension for CloudWatch Evidently allows your application to assign variations to user sessions locally instead of by calling the EvaluateFeature operation. A local session mitigates the latency and availability risks that come with an API call. For information about how to configure and use the extension, see Perform launches and A/B experiments with CloudWatch Evidently in the Amazon CloudWatch User Guide. | 

September 13, 2022 | 
| 

Deprecation of the GetConfiguration API action | 

On Nov 18, 2021, AWS AppConfig released a new data plane service. This service replaces the previous process of retrieving configuration data by using the `GetConfiguration` API action. The data plane service uses two new API actions, StartConfigurationSession and GetLatestConfiguration. The data plane service also uses new endpoints.

For more information, see About the AWS AppConfig data plane service. | 

September 13, 2022 | 
| 

New version of the AWS AppConfig Agent Lambda extension | 

Version 2.0.122 of the AWS AppConfig Agent Lambda extension is now available. The new extension uses different Amazon Resource Names (ARNs). For more information, see AWS AppConfig Agent Lambda extension release notes. | 

August 23, 2022 | 
| 

Launch of AWS AppConfig extensions | 

An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration. You can use AWS-authored extensions or create your own. For more information, see Working with AWS AppConfig extensions. | 

July 12, 2022 | 
| 

New version of the AWS AppConfig Agent Lambda extension | 

Version 2.0.58 of the AWS AppConfig Agent Lambda extension is now available. The new extension uses different Amazon Resource Names (ARNs). For more information, see Available versions of the AWS AppConfig Lambda extension. | 

May 3, 2022 | 
| 

AWS AppConfig integration with Atlassian Jira | 

Integrating with Atlassian Jira allows AWS AppConfig to create and update issues in the Atlassian console whenever you make changes to a feature flag in your AWS account for the specified AWS Region. Each Jira issue includes the flag name, application ID, configuration profile ID, and flag values. After you update, save, and deploy your flag changes, Jira updates the existing issues with the details of the change. For more information, see AWS AppConfig integration with Atlassian Jira. | 

April 7, 2022 | 
| 

General availability of feature flags and Lambda extension support for ARM64 (Graviton2) processors | 

With AWS AppConfig feature flags, you can develop a new feature and deploy it to production while hiding the feature from users. You start by adding the flag to AWS AppConfig as configuration data. Once the feature is ready to be released, you can update the flag configuration data without deploying any code. This feature improves the safety of your dev-ops environment because you don't need to deploy new code to release the feature. For more information, see Creating a feature flag configuration profile.

General availability of feature flags in AWS AppConfig includes the following enhancements: 
The console includes an option to designate a flag as a short term flag. You can filter and sort the list of flags on short-term flags. 
For customers using feature flags in AWS Lambda, the new Lambda extension allows you to call individual feature flags by using an HTTP endpoint. For more information, see see Retrieving one or more flags from a feature flag configuration. 

This update also provides support for AWS Lambda extensions developed for ARM64 (Graviton2) processors. For more information, see see Available versions of the AWS AppConfig Lambda extension.  | 

March 15, 2022 | 
| 

The GetConfiguration API action is deprecated | 

The `GetConfiguration` API action is deprecated. Calls to receive configuration data should use the `StartConfigurationSession` and `GetLatestConfiguration` APIs instead. For more information about these APIs and how to use them, see Retrieving the configuration. | 

January 28, 2022 | 
| 

New region ARN for AWS AppConfig Lambda extension | 

AWS AppConfig Lambda extension is available in the new Asia Pacific (Osaka) region. The Amazon Resource Name (ARN) is required to create a Lambda in the region. For more information about the Asia Pacific (Osaka) region ARN, see Adding the AWS AppConfig Lambda extension. | 

March 4, 2021 | 
| 

AWS AppConfig Lambda extension | 

If you use AWS AppConfig to manage configurations for a Lambda function, then we recommend that you add the AWS AppConfig Lambda extension. This extension includes best practices that simplify using AWS AppConfig while reducing costs. Reduced costs result from fewer API calls to the AWS AppConfig service and, separately, reduced costs from shorter Lambda function processing times. For more information, see AWS AppConfig integration with Lambda extensions. | 

October 8, 2020 | 
| 

New section | 

Added a new section that provides instructions for setting up AWS AppConfig. For more information, see Setting up AWS AppConfig. | 

September 30, 2020 | 
| 

Added commandline procedures | 

Procedures in this user guide now include commandline steps for the AWS Command Line Interface (AWS CLI) and Tools for Windows PowerShell. For more information, see Working with AWS AppConfig. | 

September 30, 2020 | 
| 

Launch of AWS AppConfig user guide | 

Use AWS AppConfig, a tool in AWS Systems Manager, to create, manage, and quickly deploy application configurations. AWS AppConfig supports controlled deployments to applications of any size and includes built-in validation checks and monitoring. You can use AWS AppConfig with applications hosted on EC2 instances, AWS Lambda, containers, mobile applications, or IoT devices. | 

July 31, 2020 |
