
## S3 Cloudformation Templates

### S3 Basic

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