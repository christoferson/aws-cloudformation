
## Cloudformation

## Pseudo parameters

- AWS::AccountId
- AWS::Partition
- AWS::Region
- AWS::StackId
- AWS::StackName
- AWS::URLSuffix
- AWS::NotificationARNs
- AWS::NoValue


## Sections

### Parameters

### Mappings

## Cloudformation - Intrinsic Functions

Demo Intrinsic Functions

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

[cfn-intrinsic-functions](cfn-intrinsic-functions.yaml)

## Cloudformation - Transform - Language Extensions

Demo Language extensions transform. Uses new intrinsic functions Fn::Length, Fn::ToJsonString

https://aws.amazon.com/jp/about-aws/whats-new/2022/09/aws-cloudformation-new-language-extensions-transform/

https://github.com/aws-cloudformation/cfn-language-discussion

[cfn-transform-language-ext](cfn-transform-language-ext.yaml)


### Errors

#### SSM Secure reference is not supported in: [AWS::IAM::Role/Properties/Tags,AWS::IAM::Role/Properties/Tags]
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

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

- https://github.com/aws-cloudformation/cfn-language-discussion

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks-event-bridge.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html

### TODO

- Stack Sets

- EventBridge Events