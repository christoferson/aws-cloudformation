<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html -->
<!-- Downloaded: 2026-10-28 -->

# GuardDuty Runtime Monitoring

###### Note

You can configure Runtime Monitoring along with all other protection plans from a single page in the GuardDuty console. For more information, see [Configuring protection plans](https://docs.aws.amazon.com/guardduty/latest/ug/protection-plans.html).

Runtime Monitoring observes and analyzes operating system-level, networking, and file events to help you detect potential threats in specific AWS workloads in your environment.

**Supported AWS resources in Runtime Monitoring** – Runtime Monitoring provides threat detection coverage for Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Container Service (Amazon ECS) on AWS Fargate, and Amazon Elastic Compute Cloud (Amazon EC2) resources.

GuardDuty doesn't support Amazon EKS clusters running on AWS Fargate.

In this document and other sections related to Runtime Monitoring, GuardDuty uses the terminology of **resource type** to refer to Amazon EKS, Fargate Amazon ECS, and Amazon EC2 resources.

Runtime Monitoring uses a GuardDuty security agent that adds visibility into runtime behavior, such as file access, process execution, command line arguments, and network connections. For each resource type that you want to monitor for potential threats, you can manage the security agent for that specific resource type either automatically or manually (with an exception to Fargate (Amazon ECS only)). Managing the security agent automatically means that you permit GuardDuty to install and update the security agent on your behalf. On the other hand, when you manage the security agent for your resources manually, you are responsible for installing and updating the security agent, as needed.

With this extended capability, GuardDuty can help you identify and respond to potential threats that may target applications and data running in your individual workloads and instances. For example, a threat can potentially start by compromising a single container that runs a vulnerable web application. This web application might have access permissions to the underlying containers and workloads. In this scenario, incorrectly configured credentials could potentially lead to a broader access to the account, and the data stored within it.

By analyzing the runtime events of the individual containers and workloads, GuardDuty can potentially identify compromise of a container and associated AWS credentials in an initial phase, and detect attempts to escalate privileges, suspicious API requests, and malicious access to the data in your environment.

###### Contents

-

[How it works](https://docs.aws.amazon.com/guardduty/latest/ug/how-does-runtime-monitoring-work.html)
-

[How does 30-day free trial work in Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-free-trial-works.html)
-

[Prerequisites to enabling Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-prerequisites.html)
-

[Enabling GuardDuty Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html)
-

[Managing GuardDuty security agents](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-managing-agents.html)
-

[Reviewing runtime coverage statistics and troubleshooting issues](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-assessing-coverage.html)
-

[Setting up CPU and memory monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-setting-cpu-mem-monitoring.html)
-

[Using shared VPC with Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-shared-vpc.html)
-

[Using Infrastructure as Code (IaC) with GuardDuty automated security agents](https://docs.aws.amazon.com/guardduty/latest/ug/using-iac-with-gdu-automated-agents-runtime-monitoring.html)
-

[Collected runtime event types that GuardDuty uses](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-collected-events.html)
-

[Amazon ECR repository hosting GuardDuty agent](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-ecr-repository-gdu-agent.html)
-

[Two security agents on same underlying host](https://docs.aws.amazon.com/guardduty/latest/ug/two-security-agents-installed-on-ec2-node.html)
-

[EKS Runtime Monitoring in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-guardduty.html)
-

[GuardDuty security agent release versions](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-release-history.html)
-

[Disabling, uninstalling, and cleaning up resources in Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-resource-clean-up.html)
