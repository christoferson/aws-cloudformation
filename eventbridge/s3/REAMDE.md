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

When applicable, Targets must also be configured to have correct resource policy to allow EventBridge to perform actions. [link](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html)

When target has encryption enabled, make sure EventBridge role has KMS permissions.
This only applies to Customer Managed Keys and not AWS Manages Keys. 
Set the KMS Key Policy to allow EventBridge to decrypt and generage data keys.

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
### S3 Trigger Batch

Provision an EventBridge rule that will trigger Batch

[eventbridge-rule-s3-call-batch](eventbridge-rule-s3-call-batch.yaml)

### S3 Trigger Lambda

[eventbridge-rule-s3-call-lambda](eventbridge-rule-s3-call-lambda.yaml)

### S3 Trigger SNS

[sns-policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html)

[eventbridge-rule-s3-call-sns](eventbridge-rule-s3-call-sns.yaml)

### S3 Trigger SQS

[eventbridge-rule-s3-call-sqs](eventbridge-rule-s3-call-sqs.yaml)

### S3 Trigger StepFunctions

[eventbridge-rule-s3-call-stepfunctions](eventbridge-rule-s3-call-stepfunctions.yaml)

### Links

- [AWS::Events::Rule](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)

- https://aws.amazon.com/premiumsupport/knowledge-center/sns-not-getting-eventbridge-notification/

- https://aws.amazon.com/premiumsupport/knowledge-center/batch-parameters-trigger-eventbridge/?nc1=h_ls

### Errors

#### S3 Call SQS

```
RoleArn is not supported for target arn:aws:sqs:us-east-1:foo:bar. (Service: AmazonCloudWatchEvents; Status Code: 400; Error Code: ValidationException; Request ID: zzz; Proxy: null)
```

Resource policy should be used instead of IAM Role

#### S3 Call SNS

```
Policy statement action out of service scope!
```

Policy Statement (e.g. SNS policy) only supports limited actions. Specifying unsupported actions will result to this error.

### TODO

- [x] SNS 
- [x] SQS
- [ ] Policy Permissions
- [ ] ECS


