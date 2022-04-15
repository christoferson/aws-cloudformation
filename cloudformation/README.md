
## Cloudformation

## Sections

### Parameters

### Mappings


### Errors

## SSM Secure reference is not supported in: [AWS::IAM::Role/Properties/Tags,AWS::IAM::Role/Properties/Tags]
        - Key: "DynamicSsmSecureLatest"
          Value: !Sub "{{resolve:ssm-secure:/demo/database/password}}"
        - Key: "DynamicSsmSecureVersion"
          Value: !Sub "{{resolve:ssm-secure:/demo/database/password:1}}"

SSM Parameters are supported only for selected resources.

[link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#template-parameters-dynamic-patterns-resources)

- AWS::DirectoryService::MicrosoftAD
- AWS::DirectoryService::SimpleAD
- AWS::ElastiCache::ReplicationGroup
- AWS::IAM::User
- AWS::KinesisFirehose::DeliveryStream
- AWS::OpsWorks::App
- AWS::OpsWorks::Stack
- AWS::OpsWorks::Stack
- AWS::RDS::DBCluster
- AWS::RDS::DBInstance
- AWS::Redshift::Cluster

## Template error: Unable to get mapping for RegionEnvironmentTypeAmiMap::eu-west-1::dev

Cause: FindInMap did not resolve any value. No defaulting.



## Links

- [Sample Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html)
