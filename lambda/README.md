## Lambda Cloudformation

### Lambda - Basic - Inline NodeJS

Provision a Lambda and Execution Role with Inline Code. Code in NodeJS.

[lambda-basic](lambda-basic.yaml)

### Lambda - Basic - Inline Python

Provision a Lambda and Execution Role with Inline Code. Code in Python.

[lambda-basic-python](lambda-basic-python.yaml)

### Lambda - Basic - Zip NodeJS

Provision a Lambda and Execution Role using Specified Code in S3. Code in NodeJS. basic-lambda-zip.zip

[lambda-basic-zip](lambda-basic-zip.yaml)

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

### Lambda - URL

Provision a Lambda with HTTPS URL (Public Access)

[lambda-url](lambda-url.yaml)


### LogGroup

  LambdaLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub "/aws/lambda/${LambdaFunction}"
      RetentionInDays: 1
      
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


### Resources

- [Lambda URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)
- [Lambda URL CFN](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html)


