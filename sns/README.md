
## SNS CloudFormation Templates



### SNS Basic

Provisions an SNS Topic with Email Subscription

sns-basic

### SNS FIFO

Provisions an FIFO SNS Topic with SQS Subscription

- Both SNS Topic and SQS Queue must be of type FIFO

sns-fifo

### SNS - Trigger Lambda

Provisions an SNS Topic and trigger a Lambda on Message

sns-handler-lambda

### Notes

- The Amazon SNS subscription and Amazon SQS queue must be under the same AWS account and Region.
- For a FIFO topic, use an Amazon SQS FIFO queue as a dead-letter queue for the Amazon SNS subscrption.

### Resources
- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html