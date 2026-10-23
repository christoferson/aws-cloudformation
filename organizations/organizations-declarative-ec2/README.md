
## Declarative Policies for EC2

Declarative policies (added December 2024) **declare a service configuration** for every account in scope, rather than denying API calls. Once attached, the configuration is always maintained, even as the service adds new features or APIs, and for every new account that joins the OU. Account administrators can't change it locally.

| | SCP | Declarative policy (EC2) |
|---|---|---|
| Mechanism | Deny or allow **API actions** for principals | Set **account attributes** (EC2, VPC, EBS) |
| Example | Deny `ec2:EnableSerialConsoleAccess` | `serial_console_access.status = disabled` |
| New APIs | You must add each one | Covered automatically |
| Regions | Per statement (`aws:RequestedRegion`) | Every Region of the account |
| `Type` | `SERVICE_CONTROL_POLICY` | `DECLARATIVE_POLICY_EC2` |

| Template | Scenario |
|---|---|
| [organizations-declarative-ec2.yaml](organizations-declarative-ec2.yaml) | Baseline for every account: IMDSv2 enforced, serial console off, no new public AMI or snapshot sharing |
| [organizations-declarative-ec2-allowed-amis.yaml](organizations-declarative-ec2-allowed-amis.yaml) | **Only approved AMIs**: golden AMIs from the image pipeline account (at most 90 days old), current Amazon AMIs, and Backup vault restores. Sandbox OU audits only |
| [organizations-declarative-ec2-vpc-block-public-access.yaml](organizations-declarative-ec2-vpc-block-public-access.yaml) | **No direct internet in workload accounts**: hub-and-spoke, where workloads are fully blocked and the network account is ingress-blocked with exclusions |

`TargetIds` / the `...TargetId` / `...OuId` parameters say **where in the organization tree** a policy is attached: root (`r-...`), OU (`ou-...-...`) or account ID. See the tree diagram in [../organizations-rcp/README.md](../organizations-rcp/README.md#what-attachtotargetid-targetids-is).

Offline docs: [../../docs/organizations/README.md](../../docs/organizations/README.md)

----------------------------------------------------------------------------------

## Baseline

| Attribute | Value | Effect |
|---|---|---|
| `image_block_public_access.state` | `block_new_sharing` | No new public AMI sharing (AMIs that are already public stay public) |
| `snapshot_block_public_access.state` | `block_new_sharing` | No new public EBS snapshot sharing (`block_all_sharing` would also make existing public snapshots private) |
| `serial_console_access.status` | `disabled` | EC2 serial console blocked |
| `instance_metadata_defaults.http_tokens` | `required` | IMDSv2 is the default for new launches |
| `instance_metadata_defaults.http_tokens_enforced` | `enabled` | Launching or switching an instance to IMDSv1 fails |
| `instance_metadata_defaults.http_put_response_hop_limit` | `2` | The docs recommend at least 2 when tokens are required |
| `exception_message` | `ExceptionMessage` parameter | Error text for calls that conflict with the policy |

## Allowed AMIs

**Problem:** anyone can launch any public AMI. That includes community AMIs with malware, abandoned AMIs that are years out of date, and lookalikes of popular images. Golden AMI programs are often bypassed this way.

**With Allowed AMIs**, only matching AMIs are **visible** (console, `DescribeImages`, AMI catalog) and **launchable**. AMIs that the account owns itself are always allowed.

```
 allowed = criteria_1 OR criteria_2 OR criteria_3          (up to 10 criteria)
           criteria_1 = provider 111122223333 AND name "golden-*" AND created <= 90 days ago
           criteria_2 = provider amazon AND not deprecated
           criteria_3 = provider aws_backup_vault
```

| Launch attempt in a Workloads account | `enabled` | `audit_mode` |
|---|---|---|
| `golden-al2023-2026-10-01` shared from the pipeline account | Allowed | Allowed |
| The same golden AMI, built 120 days ago | **Blocked** (too old, re-bake it) | Allowed, flagged `ImageAllowed: false` |
| Amazon Linux 2023 / ECS-optimized / EKS-optimized AMI | Allowed | Allowed |
| A deprecated Amazon AMI | **Blocked** | Allowed, flagged |
| A community AMI `ubuntu-cheap-miner` | **Blocked**, and not even listed | Allowed, flagged |
| A Marketplace AMI | **Blocked** (add `aws_marketplace` or `marketplace_product_codes` to allow) | Allowed, flagged |
| An AMI the account created itself | Allowed | Allowed |

**Inheritance:** `SandboxAllowedAmisPolicy`, attached to the Sandbox OU below Workloads, contains only `state: {"@@assign": audit_mode}`. The effective policy for sandbox accounts is the Workloads criteria merged with that override. Developers can try anything, and it all shows up as non-compliant.

```bash
# Rollout: audit first
aws ec2 describe-images --image-ids ami-xxxx --query "Images[].[ImageId,Name,ImageAllowed]"
aws ec2 describe-instance-image-metadata --filters "Name=image-allowed,Values=false" \
  --query "InstanceImageMetadata[*].[InstanceId,ImageMetadata.ImageId]" --output table
# Then redeploy the stack with AllowedAmisState=enabled
```

AWS Config rule `ec2-instance-launched-with-allowed-ami` reports instances that are already running from non-allowed AMIs. Those instances keep running.

## VPC Block Public Access

**Problem:** one route `0.0.0.0/0 → igw-...` plus a public IP or an internet-facing load balancer, and a database or admin port is on the internet. Route tables, security groups and NACLs are owned by every team in every account.

**VPC BPA** cuts the internet gateway path account-wide, whatever the routes or security groups say:

| Mode | Blocks | Still works |
|---|---|---|
| `block_bidirectional` | All IGW and egress-only IGW traffic: public IPs, internet-facing ALB / NLB, **NAT gateways** | Transit Gateway, Site-to-Site VPN, Client VPN, Cloud WAN, Verified Access, VPC endpoints |
| `block_ingress` | Inbound internet traffic | Outbound through NAT and egress-only gateways |
| `off` | Nothing | |

The template uses hub-and-spoke: workloads have no internet path of their own, and all north-south traffic goes through the network account.

```
 Workloads OU  (block_bidirectional, exclusions disabled, locked with @@operators_allowed_for_child_policies: @@none)
   app VPC ── Transit Gateway ──┐
                                ▼
 Network OU    (block_ingress, exclusions enabled)
   egress VPC:  NAT gateway ──► IGW ──► internet            outbound OK (ingress-only mode)
   ingress VPC: public ALB subnets ── exclusion (bidirectional) ◄── internet
```

| In a Workloads account | Result |
|---|---|
| EC2 instance with a public IP, SSH from home | **Blocked** |
| Internet-facing ALB in the workload VPC | **Blocked** |
| NAT gateway in the workload VPC | **Blocked**. Use central egress through the Transit Gateway |
| Account admin: `create-vpc-block-public-access-exclusion` or `modify-vpc-block-public-access-options` | **Fails**, because the policy owns these settings |
| A child OU policy that tries `"mode": {"@@assign": "off"}` | Not applied, because the parent locks `mode` with `@@none` |

In the network account, the network team excludes only the public entry subnets:

```bash
aws ec2 create-vpc-block-public-access-exclusion --subnet-id subnet-public-alb-a \
  --internet-gateway-exclusion-mode allow-bidirectional
```

Excluding only **some** of a public load balancer's subnets still lets the internet in through the excluded subnet. Exclude all of them or none.

----------------------------------------------------------------------------------

## Syntax and inheritance

Declarative policies use a fixed top-level key (`ec2_attributes`) and **inheritance operators**:

| Operator | Meaning |
|---|---|
| `@@assign` | Set the value, replacing the inherited value (for lists, replacing the whole list) |
| `@@append` | Add to an inherited list |
| `@@remove` | Remove from an inherited list |
| `@@operators_allowed_for_child_policies` | What child OU and account policies may do with this setting: `["@@all"]` (default), `["@@assign", ...]`, or `["@@none"]` (locked) |

```yaml
Content:
  ec2_attributes:
    vpc_block_public_access:
      internet_gateway_block:
        mode:
          "@@operators_allowed_for_child_policies": ["@@none"]   # children can't change it
          "@@assign": block_bidirectional
```

- **Effective policy:** the merge of the root, OU and account policies. Check it before and after a change: `aws organizations describe-effective-policy --policy-type DECLARATIVE_POLICY_EC2 --target-id <account-id>`.
- **YAML:** the `"@@..."` keys must be quoted.
- **Size:** a policy can be up to 10,000 characters.

Other EC2 attributes not used here: `vpc_encryption_control` (`attempt_monitor` / `attempt_enforce` with exclusions), `image_watermarks` in Allowed AMIs criteria, and `instance_metadata_tags` / `http_endpoint`. See the syntax page.

## Deploy

One-time, from the management account. Trusted access is needed for the account status report:

```bash
aws organizations enable-policy-type --root-id r-xxxx --policy-type DECLARATIVE_POLICY_EC2
aws organizations enable-aws-service-access --service-principal ec2.amazonaws.com
```

**Before attaching**, run the **account status report**. It shows the current value of every attribute per account and Region, and it can take hours:

```bash
aws ec2 start-declarative-policies-report --s3-bucket <bucket-in-this-region> --target-id r-xxxx
aws ec2 describe-declarative-policies-reports
aws ec2 get-declarative-policies-report-summary --report-id <id>
```

```bash
aws cloudformation create-stack --stack-name myapp-dev-ec2-allowed-amis \
  --template-body file://organizations-declarative-ec2-allowed-amis.yaml \
  --parameters ParameterKey=WorkloadsTargetId,ParameterValue=ou-ab12-11111111 \
               ParameterKey=SandboxOuId,ParameterValue=ou-ab12-33333333 \
               ParameterKey=GoldenAmiAccountId,ParameterValue=111122223333

aws cloudformation create-stack --stack-name myapp-dev-ec2-vpc-bpa \
  --template-body file://organizations-declarative-ec2-vpc-block-public-access.yaml \
  --parameters ParameterKey=WorkloadsOuId,ParameterValue=ou-ab12-11111111 \
               ParameterKey=NetworkOuId,ParameterValue=ou-ab12-44444444
```

## Before attaching broadly

- **Start small:** attach to one test account first, then move up to OUs. Validate each change with `describe-effective-policy`.
- **VPC BPA:** anything in a Workloads account that uses an IGW stops working immediately. That includes public ALBs, NAT gateways and instances with public IPs. Find these first with the status report and Network Access Analyzer.
- **Allowed AMIs:** stay in `audit_mode` until no workload launches a non-allowed AMI.
  - **Auto Scaling:** Auto Scaling groups and launch templates that point to old AMIs fail to scale out when the policy is `enabled`.
  - **AMI age:** a short `maximum_days_since_created` breaks launches whenever re-baking slips.
- **IMDSv1:** with `http_tokens_enforced: enabled`, launches that need IMDSv1 fail.
- **Locked operations:** each attribute's own APIs (for example `ModifyVpcBlockPublicAccessOptions` and `ReplaceImageCriteriaInAllowedImagesSettings`) stop working in member accounts.
- **Error text:** don't put personal or sensitive information in `ExceptionMessage`.

## Docs

- [../../docs/organizations/ug-orgs_manage_policies_ec2_syntax.md](../../docs/organizations/ug-orgs_manage_policies_ec2_syntax.md) (all attributes and values)
- [../../docs/organizations/ug-policy-operators.md](../../docs/organizations/ug-policy-operators.md) and [../../docs/organizations/ug-inheritance-examples.md](../../docs/organizations/ug-inheritance-examples.md) (inheritance)
- [../../docs/organizations/ug-orgs_manage_policies_ec2_status-report.md](../../docs/organizations/ug-orgs_manage_policies_ec2_status-report.md) and [../../docs/organizations/ug-orgs_manage_policies_ec2_best-practices.md](../../docs/organizations/ug-orgs_manage_policies_ec2_best-practices.md)
- [../../docs/organizations/ec2-allowed-amis.md](../../docs/organizations/ec2-allowed-amis.md) (criteria evaluation, audit mode, limits)
- [../../docs/organizations/vpc-security-vpc-bpa-basics.md](../../docs/organizations/vpc-security-vpc-bpa-basics.md) (what is and isn't blocked, exclusions)
