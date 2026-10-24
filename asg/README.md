

Auto Scaling to send a notification when it launches or terminates an EC2 instance. There are actually four separate notifications: EC2_INSTANCE_LAUNCH, EC2_INSTANCE_LAUNCH_ ERROR, EC2_INSTANCE_TERMINATE, and EC2_INSTANCE_TERMINATE_ERROR.

- https://aws.amazon.com/blogs/aws/auto-scaling-notifications-recurrence-and-more-control/

### Target tracking (adaptive, high-resolution metrics, metric math)

High-resolution (10-second) CPU target tracking for an API tier behind an ALB, and SQS backlog per instance with metric math for queue workers.

[asg-target-tracking/README.md](asg-target-tracking/README.md)
