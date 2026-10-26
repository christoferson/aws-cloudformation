> Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html
> Downloaded: 2026-10-27

# Amazon SQS standard queues

Amazon SQS provides standard queues as the default queue type, supporting a nearly unlimited number of API calls per second for actions like `SendMessage`, `ReceiveMessage`, and `DeleteMessage`. Standard queues ensure at-least-once message delivery, but due to the highly distributed architecture, more than one copy of a message might be delivered, and messages may occasionally arrive out of order. Despite this, standard queues make a best-effort attempt to maintain the order in which messages are sent.

When you send a message using `SendMessage`, Amazon SQS redundantly stores the message in multiple availability zones (AZs) before acknowledging it. This redundancy ensures that no single computer, network, or AZ failure can render the messages inaccessible.

You can create and configure queues using the Amazon SQS console. For detailed instructions, see Creating a standard queue using the Amazon SQS console. For Java-specific examples, see Amazon SQS Java SDK examples.

Use cases for standard queues

Standard message queues are suitable for various scenarios, as long as your application can handle messages that might arrive more than once or out of order. Examples include: 
Decoupling live user requests from intensive background work – Users can upload media while the system resizes or encodes it in the background. 
Allocating tasks to multiple worker nodes – For example, handling a high volume of credit card validation requests. 
Batching messages for future processing – Scheduling multiple entries to be added to a database at a later time. 

For information on quotas related to standard queues, see Amazon SQS standard queue quotas.

For best practices of working with standard queues, see Amazon SQS best practices.
