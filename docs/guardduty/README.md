
## Amazon GuardDuty Runtime Monitoring - Local Documentation Snapshot

Offline copies of the AWS docs used to build [guardduty/guardduty-runtime-monitoring](../../guardduty/guardduty-runtime-monitoring/), converted from HTML to Markdown.
Downloaded 2026-10-28. Each file starts with its source URL. Check the live page if something looks off.

### Runtime Monitoring - concepts

| File | Topic |
|---|---|
| [ug-runtime-monitoring.md](ug-runtime-monitoring.md) | Overview: what the security agent sees, supported resource types (EC2, ECS on Fargate, EKS) |
| [ug-how-does-runtime-monitoring-work.md](ug-how-does-runtime-monitoring-work.md) | How it works |
| [ug-runtime-monitoring-enablement.md](ug-runtime-monitoring-enablement.md) | **Two-step enablement** (turn on the feature, then manage the agent) and the **VPC flow log billing waiver** |
| [ug-how-runtime-monitoring-works-ec2.md](ug-how-runtime-monitoring-works-ec2.md) | **Deploy to EC2**: automated vs manual agent, `GuardDutyManaged` tag behaviour |
| [ug-runtime-monitoring-agent-connectivity.md](ug-runtime-monitoring-agent-connectivity.md) | **Connectivity**: link-local (`169.254.170.248/29`) vs `guardduty-data` VPC endpoint |
| [ug-runtime-monitoring-collected-events.md](ug-runtime-monitoring-collected-events.md) | The runtime event types the agent collects (process, file, network, DNS) |
| [ug-guardduty-pricing.md](ug-guardduty-pricing.md) | Pricing dimensions |

### Prerequisites and agent management

| File | Topic |
|---|---|
| [ug-runtime-monitoring-prerequisites.md](ug-runtime-monitoring-prerequisites.md) | Prerequisites index |
| [ug-prereq-runtime-monitoring-ec2-support.md](ug-prereq-runtime-monitoring-ec2-support.md) | **EC2 prerequisites**: SSM managed, instance identity role, `guardduty:SendSecurityTelemetry` in SCPs, **CPU 10% / memory limits**, `RLIMIT_MEMLOCK`, IMDS tags for exclusion tags |
| [ug-prereq-runtime-monitoring-cpu-os-kernel-support.md](ug-prereq-runtime-monitoring-cpu-os-kernel-support.md) | Supported CPU architectures (no Graviton1/A1), OS distributions, kernel versions, `CONFIG_DEBUG_INFO_BTF` |
| [ug-runtime-monitoring-configuration.md](ug-runtime-monitoring-configuration.md) | Enabling Runtime Monitoring |
| [ug-runtime-monitoring-managing-agents.md](ug-runtime-monitoring-managing-agents.md) | Managing security agents index |
| [ug-managing-gdu-agent-ec2-automated.md](ug-managing-gdu-agent-ec2-automated.md) | Automated agent on EC2 |
| [ug-manage-agent-ec2-standalone-account.md](ug-manage-agent-ec2-standalone-account.md) | **Inclusion / exclusion tags** and the `GuardDutyRuntimeMonitoring-do-not-delete` SSM association |
| [ug-managing-gdu-agent-ec2-manually.md](ug-managing-gdu-agent-ec2-manually.md) | Manual agent management |
| [ug-migrate-from-ec2-manual-to-automated-agent.md](ug-migrate-from-ec2-manual-to-automated-agent.md) | Migrating from manual to automated agent |
| [ug-runtime-monitoring-agent-resource-clean-up.md](ug-runtime-monitoring-agent-resource-clean-up.md) | **Disabling and cleanup**: what GuardDuty deletes (resources tagged `GuardDutyManaged: true`) and what it leaves |

### Networking

| File | Topic |
|---|---|
| [ug-using-iac-with-gdu-automated-agents.md](ug-using-iac-with-gdu-automated-agents.md) | **IaC + automated agents**: `DependencyViolation` on subnet delete, and the fix - pre-create the endpoint so GuardDuty reuses it |
| [ug-creating-vpc-endpoint-ec2-agent-manually.md](ug-creating-vpc-endpoint-ec2-agent-manually.md) | Creating the `com.amazonaws.<region>.guardduty-data` endpoint, endpoint policy, account / org restriction |
| [ug-validate-vpc-endpoint-config.md](ug-validate-vpc-endpoint-config.md) | Validating the endpoint: inbound 443 from the VPC IPv4 CIDR |
| [ug-runtime-monitoring-shared-vpc.md](ug-runtime-monitoring-shared-vpc.md) | Shared VPC (owner / participant accounts) |

### Coverage and findings

| File | Topic |
|---|---|
| [ug-runtime-monitoring-after-configuration.md](ug-runtime-monitoring-after-configuration.md) | Tracking coverage, Healthy / Unhealthy |
| [ug-runtime-monitoring-assessing-coverage.md](ug-runtime-monitoring-assessing-coverage.md) | Coverage statistics index |
| [ug-gdu-assess-coverage-ec2.md](ug-gdu-assess-coverage-ec2.md) | **EC2 coverage troubleshooting table** and the `GuardDuty Runtime Protection Unhealthy` / `Healthy` EventBridge events |
| [ug-findings-runtime-monitoring.md](ug-findings-runtime-monitoring.md) | **All Runtime Monitoring finding types** (`*:Runtime/*`) with remediation |
| [ug-guardduty-findings-severity.md](ug-guardduty-findings-severity.md) | Severity bands: Critical 9.0-10.0, High 7.0-8.9, Medium 4.0-6.9, Low 1.0-3.9 |
| [ug-guardduty-findings-eventbridge.md](ug-guardduty-findings-eventbridge.md) | `aws.guardduty` / `GuardDuty Finding` event format, notification frequency, multi-account rules |

### CloudFormation and API reference

| File | Topic |
|---|---|
| [cfn-aws-resource-guardduty-detector.md](cfn-aws-resource-guardduty-detector.md) | `AWS::GuardDuty::Detector` - `Features` **or** `DataSources`, not both |
| [cfn-guardduty-detector-cfnfeatureconfiguration.md](cfn-guardduty-detector-cfnfeatureconfiguration.md) | `CFNFeatureConfiguration` (`Name`, `Status`, `AdditionalConfiguration`) |
| [cfn-guardduty-detector-cfnfeatureadditionalconfiguration.md](cfn-guardduty-detector-cfnfeatureadditionalconfiguration.md) | `CFNFeatureAdditionalConfiguration` (`Name`, `Status`) |
| [api-DetectorFeatureConfiguration.md](api-DetectorFeatureConfiguration.md) | Feature names: `RUNTIME_MONITORING`, and why it conflicts with `EKS_RUNTIME_MONITORING` |
| [api-DetectorAdditionalConfiguration.md](api-DetectorAdditionalConfiguration.md) | Additional configuration names: `EC2_AGENT_MANAGEMENT`, `ECS_FARGATE_AGENT_MANAGEMENT`, `EKS_ADDON_MANAGEMENT` |
