<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html -->
<!-- Downloaded: 2026-10-28 -->

# Managing security agent manually for Amazon EC2 resource

This section provides the steps to manually install and update the security agent for your Amazon EC2 resources.

After you enable Runtime Monitoring, you will need to install the GuardDuty security agent manually. To manage the GuardDuty security agent manually, you must first create an Amazon VPC endpoint manually. After this, you can install the security agent so that GuardDuty will start receiving the runtime events from the Amazon EC2 instances. When GuardDuty releases a new agent version for this resource, you can update the agent version in your account.

The following topics include the steps to continuously manage the security agent for your Amazon EC2 resources.

###### Topics

-

[Prerequisite – Creating Amazon VPC endpoint manually](https://docs.aws.amazon.com/guardduty/latest/ug/creating-vpc-endpoint-ec2-agent-manually.html)
-

[Installing the security agent manually](https://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html)
-

[Updating the GuardDuty security agent for Amazon EC2 instance manually](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-update-security-agent-ec2.html)
