<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-managing-agents.html -->
<!-- Downloaded: 2026-10-28 -->

# Managing GuardDuty security agents

You can manage the GuardDuty security agent for the resource that you want to monitor. If you want to monitor more than one resource type, make sure to manage the GuardDuty agent for that resource.

The following topics will help you with the next steps to manage the security agent.

###### Contents

-

[Enabling automated security agent for Amazon EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-automated.html)
-

[Managing security agent manually for Amazon EC2 resource](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html)
-

[Managing GuardDuty security agent on Bottlerocket (Amazon ECS on Amazon EC2)](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-bottlerocket-ecs-ec2.html)
-

[Managing automated security agent for Fargate (Amazon ECS only)](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ecs-automated.html)
-

[Managing security agent automatically for Amazon EKS resources](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-automatically.html)
-

[Managing security agent manually for Amazon EKS cluster](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-eks-manually.html)
-

[Configure GuardDuty security agent (add-on) parameters for Amazon EKS](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-configure-security-agent-eks-addon.html)
-

[Validating VPC endpoint configuration](https://docs.aws.amazon.com/guardduty/latest/ug/validate-vpc-endpoint-config-runtime-monitoring.html)

The following list includes good to know items after you install or update the security agent.

****Assess runtime coverage****

The next step after installing or updating your security agent is to assess runtime coverage of your resources. If the runtime coverage status is **Unhealthy**, then you must troubleshoot the issue. For more information, see [Runtime coverage issues and troubleshooting](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-assessing-coverage.html).

If the status of the runtime coverage shows as **Healthy**, it indicates that Runtime Monitoring is able to collect and receive runtime events. For a list of these events, see [Collected runtime event types](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-collected-events.html).

****Private DNS name for endpoint****

After you install the GuardDuty security agent for your resources, by default, it will resolve and connect to the private DNS name of the VPC endpoint. For a non-FIPS endpoint, the private DNS will appear in the following format:

`guardduty-data.`us-east-1`.amazonaws.com`

The AWS Region, `us-east-1`, will change based on your Region.

****A host may get installed with two security agents****

When working with GuardDuty security agent for an Amazon EC2 instance, you might install and use the agent on the underlying host within an Amazon EKS cluster. If you had already deployed a security agent on that EKS cluster, the same host could have two security agents running on it at the same time. For information about how GuardDuty works in this scenario, see [Security agents on same host](https://docs.aws.amazon.com/guardduty/latest/ug/two-security-agents-installed-on-ec2-node.html).
