## SQS Cloudformation Template

## SQS Queue - Standard

Example Standard Queue

- Defines Queue Policy that allows owner account to send and receive message. By default send/recieve is enabled for owner. Edit policy if you need to allow different account.

sqs-queue-standard

## SQS Queue - FIFO

Example FIFO Queue

- High throughput for a FIFO queue enabled. 

sqs-queue-fifo


## SQS Encryption | [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-encryption-what-does-sse-encrypt)

Moving a message to a dead-letter queue doesn't affect its encryption:

  - When Amazon SQS moves a message from an encrypted source queue to an unencrypted dead-letter queue, the message remains encrypted.

  - When Amazon SQS moves a message from an unencrypted source queue to an encrypted dead-letter queue, the message remains unencrypted.
  
## SQS Require HTTPS | [link] (https://forums.aws.amazon.com/thread.jspa?threadID=285230&tstart=75)

