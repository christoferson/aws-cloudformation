<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/how-does-runtime-monitoring-work.html -->
<!-- Downloaded: 2026-10-28 -->

# How it works

Runtime Monitoring uses a lightweight security agent to observe the runtime behavior of your Amazon EC2, Amazon EKS, and Amazon ECS on Fargate workloads and detect threats. It works end to end as follows:

1.

**The agent is deployed to your resources.** GuardDuty can deploy and update the agent for you (automated agent configuration), or you can deploy and manage it yourself (manual agent configuration). The steps depend on the resource type.
2.

**The agent collects runtime events.** On each monitored resource, the agent observes operating system-level activity, such as process execution, file access, and network connections.
3.

**The agent sends events to GuardDuty.** The agent delivers the events to the GuardDuty backend. The data remains within the AWS network, and GuardDuty doesn't charge for the events transmitted from your compute resources to GuardDuty. For details, see [How the security agent connects to GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-connectivity.html).
4.

**GuardDuty analyzes the events and generates findings.** When it detects suspicious behavior, such as privilege escalation or communication with a known malicious host, GuardDuty generates a finding. To see the up-to-date list of findings that GuardDuty generates, see [GuardDuty Runtime Monitoring finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html).

The agent runs within defined CPU and memory limits, so its resource consumption stays predictable and doesn't degrade the performance or availability of the workloads running on the same host. For these limits, see [Prerequisites to enabling Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-prerequisites.html).

###### Contents

-

[Enabling Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-enablement.html)
-

[Deploying the security agent to Amazon EKS](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-eks.html)
-

[Deploying the security agent to Amazon EC2](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ec2.html)
-

[Deploying the security agent to Amazon ECS on Fargate](https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ecs-fargate.html)
-

[How the security agent connects to GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-connectivity.html)
-

[Tracking Runtime Monitoring coverage](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-after-configuration.html)
