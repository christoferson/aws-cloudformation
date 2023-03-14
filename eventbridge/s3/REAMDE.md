## EventBridge Cloudformation - S3

### Event Source Configuration

In order to receive events, source Bucket must have event bridge notification enabled.

```
  Bucket:
    Type: "AWS::S3::Bucket"
    Properties:
      ...
      NotificationConfiguration:
         EventBridgeConfiguration:
            EventBridgeEnabled: true
```

### Event Target Configuration

When applicable, targets must also be configured to have correct resource policy to allow EventBridge to perform actions. [link](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html)

### KMS Encryption - Key Policy Configuration

When target e.g. SQS has encryption enabled, make sure EventBridge has KMS permissions.
This only applies to Customer Managed Keys and not AWS Manages Keys. 
Set the KMS Key Policy to allow EventBridge to Decrypt and Generate data keys. [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html)

```
{
	"Sid": "Allow EventBridge to use the key",
	"Effect": "Allow",
	"Principal": {
	  "Service": "events.amazonaws.com"
	},
	"Action": [
	  "kms:Decrypt",
	  "kms:GenerateDataKey"
	],
	"Resource": "*"
}
```

### DeadLetter

```
DeadLetterConfig:
  Arn: 'arn:aws:sqs:us-west-2:081035103721:demoDLQ'
```

[link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-deadletterconfig.html)

- Arn
    
    - The ARN of the SQS queue specified as the target for the dead-letter queue.

### Retry Policy


```
  EventBridgeRule: 
    Type: AWS::Events::Rule
    Properties: 
      Name: eventbridge-rule-s3-call-batch
      ...
      Targets:
        - 
          Arn: !Ref JobQueueArn
          Id: "TargetBatch"
          RoleArn : !GetAtt EvenBridgeRole.Arn
          RetryPolicy:
            MaximumEventAgeInSeconds: 3600 #86400
            MaximumRetryAttempts: 1 #185
```
       

[link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html)

- MaximumEventAgeInSeconds

    - The maximum amount of time, in seconds, to continue to make retry attempts.

- MaximumRetryAttempts

    - The maximum number of retry attempts to make before the request fails. 
    - Retry attempts continue until either the maximum number of attempts is made or until the duration of the MaximumEventAgeInSeconds is met.


---

### S3 Trigger Batch

Provision an EventBridge rule that will trigger Batch.

Container Overrides [link](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerOverrides.html)

```
InputTemplate: |
  {
    "Parameters": {"S3Key" : "<S3ObjectKey>", "S3Bucket" : "<S3BucketName>"},
    "ContainerOverrides": {
      "Command": ["sh", "-c", "echo s3rocksv5 && java -jar batch.jar '<S3BucketName>' '<S3ObjectKey>'"],
      "Environment": [
        {"Name": "AWS_KEY", "Value": "<S3ObjectKey>"},
        {"Name": "APP_S3_BUCKET_OBJECT_KEY", "Value": "<S3ObjectKey>"}
      ]
    }
  }
```

If ContainerOverrides with Environment does not seem to work. Error=Unknown SDK Error.
Make sure Case is correct. e.g. name should be Name



[eventbridge-rule-s3-call-batch](eventbridge-rule-s3-call-batch.yaml)

### S3 Trigger Lambda

Provision an EventBridge rule that will trigger Lambda

[eventbridge-rule-s3-call-lambda](eventbridge-rule-s3-call-lambda.yaml)

### S3 Trigger SNS

Provision an EventBridge rule that will trigger SNS

[sns-policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html)

[eventbridge-rule-s3-call-sns](eventbridge-rule-s3-call-sns.yaml)

### S3 Trigger SQS

Provision an EventBridge rule that will trigger SQS

[eventbridge-rule-s3-call-sqs](eventbridge-rule-s3-call-sqs.yaml)

### S3 Trigger StepFunctions

Provision an EventBridge rule that will trigger StepFunctions

[eventbridge-rule-s3-call-stepfunctions](eventbridge-rule-s3-call-stepfunctions.yaml)

---

### Links

- [AWS::Events::Rule](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)

- https://aws.amazon.com/premiumsupport/knowledge-center/sns-not-getting-eventbridge-notification/

- https://aws.amazon.com/premiumsupport/knowledge-center/batch-parameters-trigger-eventbridge/?nc1=h_ls

- https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html#eb-filtering-prefix-matching

- https://aws.amazon.com/blogs/compute/reducing-custom-code-by-using-advanced-rules-in-amazon-eventbridge/

### Errors

#### S3 Call SQS

```
RoleArn is not supported for target arn:aws:sqs:us-east-1:foo:bar. 
(Service: AmazonCloudWatchEvents; Status Code: 400; 
Error Code: ValidationException; Request ID: zzz; Proxy: null)
```

Resource policy should be used instead of IAM Role

#### S3 Call SNS

```
Policy statement action out of service scope!
```

Policy Statement (e.g. SNS policy) only supports limited actions. 
Specifying unsupported actions will result to this error.

### TODO

- [x] Batch https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html
- [x] SNS 
- [x] SQS https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html
- [ ] Policy Permissions
- [ ] ECS https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html
- [ ] HTTPS https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html
- [ ] Kinesis https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html
- [ ] Redshift https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html
- [ ] RunCommand https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html
- [ ] SageMaker https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html


