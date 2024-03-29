
## S3 Cloudformation Templates

### S3 Basic

Provision a bucket with minimum configuration.

[s3-basic](s3-basic.yaml)

### S3 Standard Example

s3-bucket

[s3-bucket](s3-bucket.yaml)

### S3 Encryption

- SSEAlgorithm {AES256 | aws:kms | aws:kms:dsse}
- AES256 = S3-managed keys (SSE-S3)

- arn:aws:kms:<region>:<account>:alias/aws/s3

[s3-bucket-encryption](s3-bucket-encryption.yaml)

[doc](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingDSSEncryption.html) | [cf](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html)

### S3 Object Lambda 

s3-object-lambda

#### S3 Server Access Logging 

Activate Server Access Logging for a Bucket. Server Access Logs are saved in a separate Bucket. 
Server Access Log Bucket Settings:
1. Object Ownership set to Bucket Owner
2. Lifecycle rule to expire Log Objects in 7 days

s3-server-access-log.yaml

#### S3 WebSite

Provision an S3 bucket with WebSite Configuration.

[s3-website](s3-website.yaml)

#### S3 Replication

[s3-bucket-replication](s3-bucket-replication.yaml)


#### S3 Event

- s3:ObjectRemoved:* s3:ObjectRestore:* s3:ObjectCreated:*

#### S3 Event - SNS

- Need to create TopicPolicy to allow s3 to publish events

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "TopicPolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:us-west-1:84985938533:topicname"
    }
  ]
}
```

[s3-handler-sns](s3-handler-sns.yaml)

#### S3 EventBridge

  - "Object Created"
  - "Object Deleted"
  - "Object Tags Added"
  - "Object Tags Deleted"
          
#### S3 EventBridge - Lambda

Trigger Lambda via EventBridge

[s3-handler-eventbridge](s3-handler-eventbridge.yaml)

#### S3 Extra - Conditional Bucket 

Bucket and Bucket Policy Created per Condition

[s3-x-bucket-with-condition](s3-x-bucket-with-condition.yaml)

#### Resources
- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
- https://aws.amazon.com/jp/blogs/aws/new-use-amazon-s3-event-notifications-with-amazon-eventbridge/

##### Errors (S3)
- KMS key must be in the same region as the destination bucket.

#### TODO
- [ ] Learn more about S3 Object Lambda

- [ ] aws:SecureTransport

- [ ] Organization