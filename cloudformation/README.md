
## Cloudformation

## Pseudo parameters | [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)

- AWS::AccountId
- AWS::Partition
- AWS::Region
- AWS::StackId
- AWS::StackName
- AWS::URLSuffix
- AWS::NotificationARNs
- AWS::NoValue

## Dynamic References | [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)

For transforms, such as AWS::Include and AWS::Serverless, AWS CloudFormation doesn't resolve dynamic references before invoking any transforms. 

Do not create a dynamic reference that has a backslash (\) as the final value. AWS CloudFormation cannot resolve those references, which results in a resource failure.


- ssm, for plaintext values stored in AWS Systems Manager Parameter Store.

- ssm-secure, for secure strings stored in AWS Systems Manager Parameter Store.

- secretsmanager, for entire secrets or secret values stored in AWS Secrets Manager.

- {{resolve:ssm:parameter-name:version}}

- {{resolve:ssm-secure:parameter-name:version}}

- {{resolve:secretsmanager:secret-id:secret-string:json-key:version-stage:version-id}}
  e.g. {{resolve:secretsmanager:MyRDSSecret:SecretString:password}}


## Intrinsic Functions

### Condition intrinsic functions | [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html)


Fn::And

```
MyAndCondition: !And
  - !Equals ["sg-mysggroup", !Ref ASecurityGroup]
  - !Condition SomeOtherCondition
```

Fn::Equals

```
UseProdCondition:
  !Equals [!Ref EnvironmentType, prod]
```

Fn::If

```
  Type: 'AWS::EC2::Volume'
  Properties:
    Size:
      'Fn::If':
        - CreateLargeSize
        - '100'
        - '10'
```

Fn::Not

```
MyNotCondition:
  !Not [!Equals [!Ref EnvironmentType, prod]]
 ```

Fn::Or

```
MyOrCondition:
  !Or [!Equals [sg-mysggroup, !Ref ASecurityGroup], Condition: SomeOtherCondition]
```


## Sections

### Parameters

### Conditions

Within each condition, you can reference another condition, a parameter value, or a mapping.

CloudFormation evaluates all the conditions in your template before creating any resources. 

### Mappings

## Cloudformation - Pseudo parameters

[cfn-psuedo-parameters](cfn-psuedo-parameters.yaml)

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

- [Parameters] https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html

- [Anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

- [Sample Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html)

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

- https://github.com/aws-cloudformation/cfn-language-discussion

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks-event-bridge.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html

### TODO

- Stack Sets

- EventBridge Events