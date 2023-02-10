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

### Links

- [AWS::Events::Rule](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)


### TODO

- SNS 
- SQS