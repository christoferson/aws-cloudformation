
## AWS Organizations - Local Documentation Snapshot

Offline copies of the AWS docs used to build the templates in [organizations/organizations-scp](../../organizations/organizations-scp/), [organizations/organizations-rcp](../../organizations/organizations-rcp/) and [organizations/organizations-declarative-ec2](../../organizations/organizations-declarative-ec2/), converted from HTML to Markdown.
Downloaded 2026-10-20. Each file starts with its source URL. Check the live page if something looks off.

### User Guide — What's new

| File | Topic |
|---|---|
| [ug-document-history.md](ug-document-history.md) | Organizations document history: dated list of changes (used to pick what's new) |

### User Guide — Authorization policies (SCPs and RCPs)

| File | Topic |
|---|---|
| [ug-orgs_manage_policies_authorization_policies.md](ug-orgs_manage_policies_authorization_policies.md) | SCPs vs RCPs |
| [ug-orgs_manage_policies_scps.md](ug-orgs_manage_policies_scps.md) | SCP overview: scope, management account, service-linked roles |
| [ug-orgs_manage_policies_scps_syntax.md](ug-orgs_manage_policies_scps_syntax.md) | SCP syntax: elements per effect, Resource requirement, unsupported elements |
| [ug-orgs_manage_policies_scps_evaluation.md](ug-orgs_manage_policies_scps_evaluation.md) | SCP evaluation (deny list vs allow list) |
| [ug-orgs_manage_policies_scps_examples.md](ug-orgs_manage_policies_scps_examples.md) | SCP examples (points to the AWS GitHub repository) |
| [ug-orgs_manage_policies_rcps.md](ug-orgs_manage_policies_rcps.md) | RCP overview, **list of supported services**, scope |
| [ug-orgs_manage_policies_rcps_syntax.md](ug-orgs_manage_policies_rcps_syntax.md) | RCP syntax: Deny only, Principal "*", Action rules |
| [ug-orgs_manage_policies_rcps_evaluation.md](ug-orgs_manage_policies_rcps_evaluation.md) | RCP evaluation |
| [ug-orgs_manage_policies_rcps_examples.md](ug-orgs_manage_policies_rcps_examples.md) | RCP examples (points to the AWS GitHub repository) |
| [ug-orgs_manage_policies_types.md](ug-orgs_manage_policies_types.md) | All organization policy types |
| [ug-enable-policy-type.md](ug-enable-policy-type.md) | Enabling a policy type on the root (CLI) |

### User Guide — Declarative policies

| File | Topic |
|---|---|
| [ug-orgs_manage_policies_declarative.md](ug-orgs_manage_policies_declarative.md) | Management policy types overview |
| [ug-orgs_manage_policies_ec2.md](ug-orgs_manage_policies_ec2.md) | EC2 policies: custom error messages, account status report |
| [ug-orgs_manage_policies_ec2_syntax.md](ug-orgs_manage_policies_ec2_syntax.md) | EC2 policy syntax for each attribute (VPC BPA, serial console, AMI / snapshot BPA, Allowed AMIs, IMDS, VPC encryption) |
| [ug-orgs_manage_policies-ec2_getting-started.md](ug-orgs_manage_policies-ec2_getting-started.md) | Enable EC2 policies + trusted access (2026-10-23) |
| [ug-orgs_manage_policies_ec2_best-practices.md](ug-orgs_manage_policies_ec2_best-practices.md) | Status report first, start small, `DescribeEffectivePolicy` (2026-10-23) |
| [ug-orgs_manage_policies_ec2_status-report.md](ug-orgs_manage_policies_ec2_status-report.md) | Account status report: prerequisites, permissions, CLI (2026-10-23) |
| [ug-orgs_manage_policies_inheritance_mgmt.md](ug-orgs_manage_policies_inheritance_mgmt.md) | Understanding policy inheritance (2026-10-23) |
| [ug-syntax-inheritance.md](ug-syntax-inheritance.md) | Declarative policy types and effective policies (2026-10-23) |
| [ug-policy-operators.md](ug-policy-operators.md) | `@@assign`, `@@append`, `@@remove`, `@@operators_allowed_for_child_policies` (2026-10-23) |
| [ug-inheritance-examples.md](ug-inheritance-examples.md) | Merge examples: overwrite, append, remove, lock children (2026-10-23) |

### EC2 and VPC User Guides (downloaded 2026-10-23)

| File | Topic |
|---|---|
| [ec2-allowed-amis.md](ec2-allowed-amis.md) | Allowed AMIs: criteria (AND / OR), providers and aliases, audit mode, limits, best practices |
| [ec2-manage-settings-allowed-amis.md](ec2-manage-settings-allowed-amis.md) | Manage Allowed AMIs settings, find instances launched from non-allowed AMIs |
| [vpc-security-vpc-bpa.md](vpc-security-vpc-bpa.md) | VPC Block Public Access: modes, exclusions |
| [vpc-security-vpc-bpa-basics.md](vpc-security-vpc-bpa-basics.md) | What BPA blocks (IGW, NAT, internet-facing ELB, ...) and doesn't (TGW, VPN, ...), exclusions, CLI |
| [vpc-security-vpc-bpa-assess-impact-main.md](vpc-security-vpc-bpa-assess-impact-main.md) | Assess impact (Network Access Analyzer, flow logs) |
| [vpc-security-vpc-bpa-example.md](vpc-security-vpc-bpa-example.md) | Advanced example walkthrough |

### AWS example policies (GitHub, downloaded 2026-10-22)

Raw copies of the AWS sample repositories that the RCP and SCP examples pages point to. These are the basis for the RCP templates.

| Folder | Source | Contents |
|---|---|---|
| [github/data-perimeter-policy-examples](github/data-perimeter-policy-examples/README.md) | https://github.com/aws-samples/data-perimeter-policy-examples | Identity / resource / network perimeter concepts, `dp:*` tag convention, RCPs (`identity_perimeter_rcp.json`, `network_perimeter_*_rcp.json`, `data_perimeter_governance_rcp.json`) and their rationale, plus S3 / STS / KMS service guidance |
| [github/resource-control-policy-examples](github/resource-control-policy-examples/README.md) | https://github.com/aws-samples/resource-control-policy-examples | Service-specific RCPs (S3 TLS version, SSE-C, presigned URL age, KMS deletion, ...), OIDC providers (GitHub Actions), intra-organization (OU) boundaries |

### IAM User Guide

| File | Topic |
|---|---|
| [iam-reference_policies_condition-keys.md](iam-reference_policies_condition-keys.md) | Global condition keys (`aws:PrincipalOrgID`, `aws:PrincipalIsAWSService`, `aws:SecureTransport`, `aws:PrincipalArn`, ...) |

### CloudFormation Template Reference — `AWS::Organizations::*`

| File | Resource |
|---|---|
| [cfn-aws-resource-organizations-organization.md](cfn-aws-resource-organizations-organization.md) | `AWS::Organizations::Organization` (FeatureSet only; can't enable policy types) |
| [cfn-aws-resource-organizations-organizationalunit.md](cfn-aws-resource-organizations-organizationalunit.md) | `AWS::Organizations::OrganizationalUnit` |
| [cfn-aws-resource-organizations-account.md](cfn-aws-resource-organizations-account.md) | `AWS::Organizations::Account` |
| [cfn-aws-resource-organizations-policy.md](cfn-aws-resource-organizations-policy.md) | `AWS::Organizations::Policy` (13 policy types, size limits, Content as object vs string) |
| [cfn-aws-resource-organizations-resourcepolicy.md](cfn-aws-resource-organizations-resourcepolicy.md) | `AWS::Organizations::ResourcePolicy` (delegated policy management) |
| [cfn-aws-properties-organizations-policy-tag.md](cfn-aws-properties-organizations-policy-tag.md) | Policy Tag |
| [cfn-aws-properties-organizations-account-tag.md](cfn-aws-properties-organizations-account-tag.md) | Account Tag |
| [cfn-aws-properties-organizations-organizationalunit-tag.md](cfn-aws-properties-organizations-organizationalunit-tag.md) | OrganizationalUnit Tag |
| [cfn-aws-properties-organizations-resourcepolicy-tag.md](cfn-aws-properties-organizations-resourcepolicy-tag.md) | ResourcePolicy Tag |
