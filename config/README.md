## Config Cloudformation Templates

- To enable AWS Config, you must create a configuration recorder and a delivery channel.

- AWS Config uses the delivery channel to deliver the configuration changes to your Amazon S3 bucket or Amazon SNS topic.

- You can have only one delivery channel per region per AWS account

- The delivery channel is required to use AWS Config.	

- Auditing and recording compliance of your AWS resources

- Record configurations and changes over time

- Regionally scoped. Option to aggregate across regions and accounts

- Receive SNS alerts for changes



###### Managed Rules

[link](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)

##### Resource management

- Specify the resource types you want AWS Config to record.
- Set up an Amazon S3 bucket to receive a configuration snapshot on request and configuration history.
- Set up Amazon SNS to send configuration stream notifications.
- Grant AWS Config the permissions it needs to access the Amazon S3 bucket and the Amazon SNS topic.

##### Rules and conformance packs

- Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types.

- Use conformance packs, or a collection of AWS Config rules and remediation actions that can be deployed and monitored as a single entity in your AWS account.

##### Aggregators

- Use an aggregator to get a centralized view of your resource inventory and compliance. An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from multiple AWS accounts and AWS Regions into a single account and Region.

###### Advanced queries

Use one of the sample queries or write your own query by referring to the configuration schema of the AWS resource.

--------------------------------------------------------------

### Setup Config

Provision a DynamoDB with various features enabled.

[setup](setup/config-setup.yaml)

### Setup Config - Service Linked Role

Provision a DynamoDB with various features enabled.

[1-config-service-linked-role](setup/1-config-service-linked-role.yaml)

#### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html