## Lambda Cloudformation

### Concepts

#### IAM Resource Policy / Function Policy 

- Defines what can invoke the function
- Defined using AWS::Lambda::Permission

```
  CodeCommitInvokeLambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !Sub "arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${LambdaFunction}"
      Action: lambda:InvokeFunction
      Principal: codecommit.amazonaws.com
      SourceArn: !Sub arn:aws:codecommit:${AWS::Region}:${AWS::AccountId}:${CodeCommitRepository}
      SourceAccount: !Sub ${AWS::AccountId}
```

- Policy associated with a "push" event source
- Created when you add a trigger to a Lambda function
- Allows the event source to take the lambda:InvokeFunction action

#### IAM Execution Role 

- Defines the resources that the Lambda can access or what it is permitted to do
- Defined using AWS::IAM::Role
- Selected or created when you create a Lambda function
- IAM policy includes actions that can be taken with the resource
- Trust policy that allows Lambda to AssumeRole
- Creator must have permission for iam:PassRole

#### Event Source Mapping

- Use event source mappings to process items from a stream or queue in services that don't invoke Lambda functions directly
    - Amazon DynamoDB
    - Amazon Kinesis
    - Amazon MQ
    - Amazon Managed Streaming for Apache Kafka (Amazon MSK)
    - Self-managed Apache Kafka
    - Amazon Simple Queue Service (Amazon SQS)

- Defined using AWS::Lambda::EventSourceMapping

```yaml
  LambdaEventSourceMapping:
    Type: AWS::Lambda::EventSourceMapping
    Properties:
      EventSourceArn: !GetAtt LambdaTriggerSqsQueue.Arn
      FunctionName: !GetAtt LambdaFunction.Arn
```

### Concurrency

- Concurrency is the number of requests that your function is serving at any given time. 
- Default regional concurrency quota starts at 1,000 instances
- throttling error (429 status code)
    - When requests come in faster than your function can scale
    - When your function is at maximum concurrency

### Reserved Concurrency

- Guarantees the maximum number of concurrent instances for the function. 

### Provisioned Concurrency

- Initializes a requested number of execution environments so that they are prepared to respond immediately to your function's invocations. 

### Managed Policy

- arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
- arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole
- arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole
- arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole
- arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole

### Lambda - Basic - Inline NodeJS

Provision a Lambda and Execution Role with Inline Code. Code in NodeJS.

[lambda-basic](lambda-basic.yaml)

### Lambda - Basic - Inline Python

Provision a Lambda and Execution Role with Inline Code. Code in Python.

[lambda-basic-py](lambda-basic-py.yaml)

### Lambda - Basic - Zip NodeJS

Provision a Lambda and Execution Role using Specified Code in S3. Code in NodeJS. basic-lambda-zip.zip

[lambda-basic-zip](lambda-basic-zip.yaml)

### Lambda - Basic - Zip Java

Provision a Lambda and Execution Role using Specified Code in S3. Code in Java. basic-lambda-zip-java.zip

[lambda-basic-zip-java](lambda-basic-zip-java.yaml)

### Lambda - Ephemeral Storage - /tmp

Provision a Lambda with specified Ephemeral Storage or /tmp storage size

[lambda-ephemeral-storage](lambda-ephemeral-storage.yaml)

### Lambda Layer

Provision a Lambda Version

[lambda-layer](lambda-layer.yaml)

### Lambda Layer - JS

Provision a Lambda Version with Javascript SDK

```
npm init
npm install aws-sdk
```

[lambda-layer-js](lambda-layer-js.yaml)

### Lambda Layer - Java

Provision a Lambda Version with Java SDK

```
<dependency>
	<groupId>com.amazonaws</groupId>
	<artifactId>aws-lambda-java-core</artifactId>
	<version>1.2.2</version>
</dependency>
```

[lambda-layer-java](lambda-layer-java.yaml)

### Lambda - Trigger - SQS

Provision a Lambda triggered by SQS

- Amazon SQS is used as a Lambda event source
- Lambda service manages polling the queue on your behalf
- Lambda service Retries until Message Retention Period expires or is sent to a dead-letter queue

```
  LambdaTriggerSqsQueue: 
    Type: AWS::SQS::Queue
    Properties: 
       MessageRetentionPeriod: 43200 #60 seconds (1 minute) to 1,209,600 seconds (14 days), default value is 345,600 seconds (4 days)
       RedrivePolicy: 
         deadLetterTargetArn: !GetAtt LambdaTriggerSqsQueueDeadLetter.Arn
         maxReceiveCount: 2
```

[lambda-trigger-sqs](lambda-trigger-sqs.yaml)

### Lambda - Trigger - DynamoDB

Provision a Lambda triggered by DynamoDB streams

- DynamoDB Streams is used as a Lambda event source
- Lambda service manages polling the queue on your behalf

[lambda-trigger-dynamodb](lambda-trigger-dynamodb.yaml)


### Lambda - URL

Provision a Lambda with HTTPS URL (Public Access)

[lambda-url](lambda-url.yaml)

### Lambda - Application Load Balancer

Provision a Lambda fronted by Application Load Balancer. 
Multi Value Header is enabled using Target Group Attribute.

```
TargetGroup MultiValue Headers:
curl http://xxx.elb.amazonaws.com/zzz?name=foo&name=bar&name=zig
true - multiValueQueryStringParameters: { name: [ 'foo', 'bar', 'zig' ] }
false - queryStringParameters: { name: 'bar' }
```

[lambda-alb](lambda-alb.yaml)


TODO: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html

### Lambda - Version and Alias

Provision a Lambda with Versions and Alias.

- Add 1 AWS::Lambda::Version at a time. Update the Alias to point to the correct Version.
- Remove AWS::Lambda::Version to delete the version.

[lambda-alias](lambda-alias.yaml)

### Lambda - Concurrency

Provision lambda with Reserved Concurrency & Provisioned Concurrency on Alias.

```
  LambdaAliasDev:
    Type: AWS::Lambda::Alias
    Properties:
      ...
      ProvisionedConcurrencyConfig:
        ProvisionedConcurrentExecutions: 5
```


[lambda-concurrency](lambda-concurrency.yaml)

### Lambda - Concurrency - AutoScale

Provision lambda with Provisioned Concurrency on Scheduled AutoScaling

aws application-autoscaling describe-scalable-targets --service-namespace lambda

[lambda-concurrency-scale](lambda-concurrency-scale.yaml)

### Lambda - VPC

- Provide additional VPC-specific configuration information, which includes VPC subnet IDs and security group IDs

- Execution role with permissions to create, describe, and delete elastic network interfaces. e.g. AWSLambdaVPCAccessExecutionRole

[lambda-vpc](lambda-vpc.yaml)


### LogGroup

 ```
  LambdaLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub "/aws/lambda/${LambdaFunction}"
      RetentionInDays: 1
 ```
   
### Enable Xray

 ```
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
        - arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess
 ```
     
 ```
   LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName : "basic-lambda"
      Description: "Basic Lambda"
      ...
      TracingConfig:
        Mode: "Active" 
```

### Errors

1. Alias can't be used for Provisioned Concurrency configuration on an already Provisioned version

Cannot configure provisioned concurrency on both alias and version

### Resources

- [Lambda Resource Policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)
- [Lambda VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- [Lambda URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)
- [Lambda URL CFN](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html)
- [AutoScale Concurrency](https://aws.amazon.com/jp/blogs/compute/scheduling-aws-lambda-provisioned-concurrency-for-recurring-peak-usage/)
- [MultiHeader](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.html)
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
- https://aws.amazon.com/blogs/compute/reducing-java-cold-starts-on-aws-lambda-functions-with-snapstart/

