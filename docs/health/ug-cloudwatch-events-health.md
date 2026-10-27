> Source: https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html
> Downloaded: 2026-10-27

# Monitoring events in AWS Health with Amazon EventBridge

You can use Amazon EventBridge to detect and react to AWS Health events. Then, based on rules that you create, EventBridge invokes one or more target actions when an event matches the values that you specify in a rule. Depending on the type of event, you can capture event information, initiate additional events, send notifications, take corrective action, or perform other actions. For example, you can use AWS Health to receive email notifications if you have AWS resources in your AWS account that are scheduled for updates, such as Amazon Elastic Compute Cloud (Amazon EC2) instances.Notes 
AWS Health delivers events on a durable basis and attempts to successfully deliver events to EventBridge at least once. 
Any EventBridge rules that you create can only receive notifications for your AWS account. To receive organizational events for other accounts within your AWS Organizations, see Aggregating AWS Health events using organizational view and delegated administrator access.
Public health events might take up to one hour to start sending after you create an EventBridge rule. 

You can choose between multiple target types for EventBridge as part of your AWS Health workflow, including: 
AWS Lambda functions 
Amazon Kinesis Data Streams 
Amazon Simple Queue Service (Amazon SQS) queues 
Built-in targets (such as CloudWatch alarm actions) 
Amazon Simple Notification Service (Amazon SNS) topics 

For example, you can use a Lambda function to pass a notification to a Slack channel when an AWS Health event occurs. Or, you can use Lambda and EventBridge to send custom text or SMS notifications with Amazon SNS when an AWS Health event occurs.

For samples of automation and customized alerts that you can create in response to AWS Health events, see the AWS Health Tools in GitHub.Topics
Creating EventBridge rules for AWS Region coverage
Monitoring account-specific and public events for AWS Health
Viewing paginated lists of AWS Health events on EventBridge
Aggregating AWS Health events using organizational view and delegated administrator access
Integrating AWS Health event monitoring and notifications with JIRA and ServiceNow
Configuring an EventBridge rule to send notifications about events in AWS Health
Configuring Amazon Q Developer in chat applications to send notifications about events in AWS Health
Running operations on EC2 instances automatically in response to events in AWS Health
Reference: AWS Health events Amazon EventBridge schema
