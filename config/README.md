## Config Cloudformation Templates

- To enable AWS Config, you must create a configuration recorder and a delivery channel.

- AWS Config uses the delivery channel to deliver the configuration changes to your Amazon S3 bucket or Amazon SNS topic.

- You can have only one delivery channel per region per AWS account

- The delivery channel is required to use AWS Config.	

- Auditing and recording compliance of your AWS resources

- Record configurations and changes over time

- Regionally scoped. Option to aggregate across regions and accounts

- Receive SNS alerts for changes

## Use Cases

- Audit IAM policies

- Detect if cloudtrail has been disabled

- Detect if unapproved AMI is used to launch EC2 instance

- Detect if security groups are too open

- Detect if Internet Gateway is added to unauthorized VPC

- Detect if EBS volumes are unencrypted

- Detect if RDS are public

- Expired IAM Keys (access-keys-rotated)

---------------------------------------------------------------------


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

- Create an Aggregator in the Aggregator Account. Aggregate rules, resources, across multiple accounts and regions. If using Organizations, no need to create Authorization in individual accounts. otherwise you need to create authorization in each account.

- Rules are created and managed in individual accounts

###### Advanced queries

Use one of the sample queries or write your own query by referring to the configuration schema of the AWS resource.

--------------------------------------------------------------

## Resource Types

- [ ] AWS::Config::AggregationAuthorization

- [ ] AWS::Config::ConfigRule

- [x] AWS::Config::ConfigurationAggregator

- [ ] AWS::Config::ConfigurationRecorder

- [ ] AWS::Config::ConformancePack

- [x] AWS::Config::DeliveryChannel

- [ ] AWS::Config::OrganizationConfigRule

- [ ] AWS::Config::OrganizationConformancePack

- [ ] AWS::Config::RemediationConfiguration

- [x] ::Config::StoredQuery

--------------------------------------------------------------

### Setup Config

Provision Bucket, DeliveryChannel and ConfigurationRecorder

[setup](setup/config-setup.yaml)

### Config - Service Linked Role

Provision the Config Service Linked Role

[1-config-service-linked-role](setup/1-config-service-linked-role.yaml)

### Config - Stored Query

Provision a StoredQuery

[config-stored-query](config-stored-query.yaml)

#### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html

