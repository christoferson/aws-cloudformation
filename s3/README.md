
## S3 Cloudformation Templates

### S3 Basic Minimum Example

s3-basic

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