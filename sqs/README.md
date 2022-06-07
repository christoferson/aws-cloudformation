## SQS Cloudformation Template

## SQS Queue - Standard

Example Standard Queue

- Defines Queue Policy that allows owner account to send and receive message. By default send/recieve is enabled for owner. Edit policy if you need to allow different account.

sqs-queue-standard

## SQS Queue - FIFO

Example FIFO Queue

- High throughput for a FIFO queue enabled. 

sqs-queue-fifo

## SQS Queue - Synchronous Lambda Trigger

Example Standard Queue with Lambda Trigger

- Source Queue Encryption enabled with AWS Managed KMS
- Source Queue Dead Letter Queue Enabled
- X-ray Active Tracing Enabled
- Lambda Log Group Retention Configuration

sqs-queue-trigger-lambda

## SQS FIFO Queue - Synchronous Lambda Trigger

Example Standard Queue with Lambda Trigger

TODO: Work in progress

sqs-queue-fifo-trigger-lambda

## Resources

### AWS CLI Send Message to Queue

aws --region eu-west-1 sqs send-message --queue-url https://sqs.eu-west-1.amazonaws.com/0000000000/sqs-queue-trigger-lambda-StandardQueue-zzz --message-body "{\"foo\": \"bar\", \"type\":\"error\"}

aws --region eu-west-1 sqs send-message --queue-url https://sqs.eu-west-1.amazonaws.com/0000000000/sqs-queue-fifo-trigger-lambda-FifoQueue-zzz.fifo --message-group-id mgrp1 --message-body "{\"foo\": \"bar\", \"type\":\"error\"} 


### SQS Encryption | [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-encryption-what-does-sse-encrypt)

SSE protects the contents of messages in queues using:

- SQS-owned encryption keys (SSE-SQS) 
- Keys managed in the AWS Key Management Service (SSE-KMS)

Moving a message to a dead-letter queue doesn't affect its encryption:

  - When Amazon SQS moves a message from an encrypted source queue to an unencrypted dead-letter queue, the message remains encrypted.

  - When Amazon SQS moves a message from an unencrypted source queue to an encrypted dead-letter queue, the message remains unencrypted.

SQS-managed encryption keys (SSE-SQS) not yet supported in CFN
https://github.com/aws-cloudformation/cloudformation-coverage-roadmap/issues/989
  
### SQS Require HTTPS | [link](https://forums.aws.amazon.com/thread.jspa?threadID=285230&tstart=75)

Enforce encryption in transit using require TLS https connection
