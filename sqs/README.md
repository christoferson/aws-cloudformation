## SQS Cloudformation Template

## SQS Queue - Standard

Example Standard Queue

- Defines Queue Policy that allows owner account to send and receive message. By default send/recieve is enabled for owner. Edit policy if you need to allow different account.

sqs-queue-standard

## SQS Queue - FIFO

Example FIFO Queue

[sqs-queue-fifo](sqs-queue-fifo.yaml)

## SQS Queue - FIFO - High Throughput

High throughput FIFO Queue

[sqs-queue-fifo-ht](sqs-queue-fifo-ht.yaml)

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

### SQS FIFO - Message Deduplication | [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html)

- If a message with a particular MessageDeduplicationId is sent successfully, any messages sent with the same MessageDeduplicationId are accepted successfully but aren't delivered during the 5-minute deduplication interval.

- If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message). 

- If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error. 

### SQS FIFO - Message Group | [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html)

- Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use MessageGroupId values (for example, session data for multiple users).

- You must associate a non-empty MessageGroupId with a message. If you don't provide a MessageGroupId, the action fails. 

- ReceiveMessage might return messages with multiple MessageGroupId values. For each MessageGroupId, the messages are sorted by time sent. The caller can't specify a MessageGroupId. 

### SQS FIFO - High Throughput | [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html)

To enable high throughput for a FIFO queue
- Deduplication scope is set to Message group, the required setting for using high throughput for FIFO queues.
- FIFO throughput limit is set to Per message group ID, the required setting for using high throughput for FIFO queues.

Features
- Enable high throughput FIFO - Makes higher throughput available for messages in the current FIFO queue.
- Deduplication scope - Specifies whether deduplication occurs at the queue or message group level.
- FIFO throughput limit - Specifies whether the throughput quota on messages in the FIFO queue is set at the queue or message group level.

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
