## EventBridge Cloudformation - S3

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

When target has encryption enabled, make sure EventBridge role has KMS permissions.
This is only for Customer Managed KMS. Set the KMS Key Policy to allow access.

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


### S3 Trigger SQS

[eventbridge-rule-s3-call-sqs](eventbridge-rule-s3-call-sqs.yaml)

### S3 Trigger SNS

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html

[eventbridge-rule-s3-call-sns](eventbridge-rule-s3-call-sns.yaml)


### Links

- [AWS::Events::Rule](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)

- https://aws.amazon.com/premiumsupport/knowledge-center/sns-not-getting-eventbridge-notification/

### Errors

#### S3 Call SQS

```
RoleArn is not supported for target arn:aws:sqs:us-east-1:foo:bar. (Service: AmazonCloudWatchEvents; Status Code: 400; Error Code: ValidationException; Request ID: zzz; Proxy: null)
```

#### S3 Call SNS

```
Policy statement action out of service scope!
```
SNS policy only supports limited actions

### TODO

- SNS 
- SQS
- Policy Permissions


