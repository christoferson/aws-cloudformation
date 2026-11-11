<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-resource-clean-up.html -->
<!-- Downloaded: 2026-10-28 -->

# Disabling, uninstalling, and cleaning up resources in Runtime Monitoring

This section applies to your AWS account if you choose to disable Runtime Monitoring, or only GuardDuty automated agent configuration for a resource type.

****Disabling GuardDuty automated agent configuration****

GuardDuty doesn't remove the security agent that is deployed on your resource. However, GuardDuty will stop managing the updates to the security agent.

GuardDuty continues to receive the runtime events from your resource type. To prevent an impact on your usage statistics, make sure to remove the GuardDuty security agent from your resource.

Whether or not an AWS account uses a shared VPC endpoint, GuardDuty doesn't delete the VPC endpoint. If required, you will need to delete the VPC endpoint manually.

****Disabling Runtime Monitoring **and** EKS Runtime Monitoring****

This section applies to you in the following scenarios:

-

You never enabled EKS Runtime Monitoring separately and now you disabled Runtime Monitoring.
-

You are disabling both Runtime Monitoring and EKS Runtime Monitoring. If you're unsure about the configuration status of EKS Runtime Monitoring, see [Checking EKS Runtime Monitoring configuration status](https://docs.aws.amazon.com/guardduty/latest/ug/checking-eks-runtime-monitoring-enable-status.html).

###### Disabling Runtime Monitoring without disabling EKS Runtime Monitoring

In this scenario, at some point in time, you enabled EKS Runtime Monitoring, and later, also enabled Runtime Monitoring without disabling EKS Runtime Monitoring.

Now, when you disable Runtime Monitoring, you will also need to disable EKS Runtime Monitoring; otherwise, you will continue incurring usage cost for EKS Runtime Monitoring.

If the previously listed scenarios apply to you, then GuardDuty will take the following actions in your account:

-

GuardDuty deletes the VPC endpoint that has the `GuardDutyManaged`:`true` tag. This is the VPC that GuardDuty had created to manage the automated security agent.
-

GuardDuty deletes the security group that was tagged as `GuardDutyManaged`:`true`.
-

For a shared VPC that has been used by at least one participant account, GuardDuty neither deletes the VPC endpoint nor the security group associated with the shared VPC resource.
-

For an Amazon EKS resource, GuardDuty deletes the security agent. This is independent of whether it was managed manually or through GuardDuty.

For an Amazon ECS resource, because an ECS task is immutable, GuardDuty can't uninstall the security agent from that resource. This is independent of how you manage the security agent – manually or automatically through GuardDuty. After you disable Runtime Monitoring, GuardDuty will not attach a sidecar container when a new ECS task starts running. For information about working with Fargate-ECS tasks, see [Deploying the security agent to Amazon ECS on Fargate](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ecs-fargate.html).

For an Amazon EC2 resource, GuardDuty uninstalls the security agent from all the Systems Manager (SSM) managed Amazon EC2 instances only when it meets the following conditions:

  -

Your resource is **not** tagged with `GuardDutyManaged`:`false` exclusion tag.
  -

GuardDuty must have permissions to access the tags in instance metadata. For this EC2 resource, the **Access to tags in instance metadata** is set to **Allow**.

****When you stop managing the security agent manually****

Regardless of which approach you use to deploy and manage the GuardDuty security agent, to stop monitoring the runtime events in your resource, you must remove the GuardDuty security agent. When you want to stop monitoring the runtime events from a resource type in an account, you may also delete the Amazon VPC endpoint.
