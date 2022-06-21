
## S3 Cloudformation Templates

### S3 Basic Minimum Example

[s3-basic](s3-basic.yaml)

### S3 Standard Example

s3-bucket

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

#### Resources