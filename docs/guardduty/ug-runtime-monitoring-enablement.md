<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-enablement.html -->
<!-- Downloaded: 2026-10-28 -->

# Enabling Runtime Monitoring

Enabling Runtime Monitoring is a two-step process:

1.

**Turn on Runtime Monitoring** for your account. GuardDuty then accepts runtime events from your Amazon EC2 instances, Amazon ECS clusters, and Amazon EKS workloads.
2.

**Manage the GuardDuty security agent** for the resources you want to monitor. Based on the resource type, you can:

  -

Use automated agent configuration – GuardDuty deploys the agent and establishes its connectivity.
  -

Manage the agent manually – you create a VPC endpoint and manage the agent's installation and updates.

Managing the agent differs by resource type. For details, see:

-

[Deploying the security agent to Amazon EKS](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-eks.html)
-

[Deploying the security agent to Amazon EC2](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ec2.html)
-

[Deploying the security agent to Amazon ECS on Fargate](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ecs-fargate.html)

When the GuardDuty security agent is deployed on an Amazon EC2 instance and receives runtime events from it, GuardDuty does not charge your AWS account for analyzing VPC flow logs from that instance. This avoids double usage costs.
