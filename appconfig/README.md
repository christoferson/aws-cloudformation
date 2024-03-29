
## AppConfig CloudFormation Templates

AWS AppConfig requires that you create resources and deploy a configuration in the following order:
- Create an application
- Create an environment
- Create a configuration profile
- Create a deployment strategy
- Deploy the configuration

A configuration profile includes the following information.

- The Uri location of the configuration data.
- The AWS Identity and Access Management (IAM) role that provides access to the configuration data.
- A validator for the configuration data. Available validators include either a JSON Schema or the Amazon Resource Name (ARN) of an AWS Lambda function.

### Concepts

The AWS::AppConfig::Environment resource creates an environment, which is a logical deployment group of AWS AppConfig targets, such as applications in a Beta or Production environment.

AWS::AppConfig::Deployment resource starts a deployment

AWS::AppConfig::ConfigurationProfile resource creates a configuration profile that enables AWS AppConfig to access the configuration source. Valid configuration sources include AWS Systems Manager (SSM) documents, SSM Parameter Store parameters, and Amazon S3. 

AWS::AppConfig::DeploymentStrategy resource creates an AWS AppConfig deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.


### AppConfig - Basic

Provision a complete AppConfig Application, Environment, Config

[appconfig-basic](appconfig-basic.yaml)


### Links

- https://aws.amazon.com/about-aws/whats-new/2020/02/aws-appconfig-launches-support-aws-cloudformation/?nc1=h_ls

- https://aws.amazon.com/about-aws/whats-new/2020/02/aws-appconfig-launches-support-aws-cloudformation/?nc1=h_ls	

- https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html