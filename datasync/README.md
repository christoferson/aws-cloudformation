## DataSync Cloudformation Templates

### DataSync - CloudWatch Log Resource Policy

[datasync-log-resource-policy](datasync-log-resource-policy.yaml)

### DataSync - S3 to S3

Provision a DataSync task to copy from S3 to S3

[datasync-s3-to-s3](datasync-s3-to-s3.yaml)

### Errors - S3

- Invalid SyncOption value. Option: PosixPermissions, Value: PRESERVE invalid for non-POSIX transfer. please use NONE.

- Invalid SyncOption value. Option: Uid, Value: INT_VALUE invalid for non-POSIX transfer. please use NONE. 

- Invalid request provided: DataSync location access test failed: could not perform s3:ListObjectsV2 on bucket. Ensure bucket access role has s3:ListBucket permission.



### Links

- https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#cloudwatchlogs

### TODO

- AWS::DataSync::LocationEFS

