
## Resource Control Policies (RCPs) - data perimeter

[organizations-rcp-data-perimeter.yaml](organizations-rcp-data-perimeter.yaml)

RCPs (added November 2024) set the **maximum permissions for resources** in member accounts, whoever the caller is. SCPs and RCPs complement each other:

| | SCP | RCP |
|---|---|---|
| Limits | What **your IAM principals** can do | What **anyone** (including external principals) can do **to your resources** |
| Typical guardrail | "Our roles can't leave these Regions" | "Our buckets and keys can't be used by other organizations or over plain HTTP" |
| `Effect` | `Allow` or `Deny` | **`Deny` only** for customer managed RCPs |
| `Principal` | Not supported | **Required**, and must be `"*"` |
| Services | All | **Only services on the RCP supported list** |

Neither grants access, and effective permissions are the intersection of SCPs, RCPs, and identity- and resource-based policies.

The template's single RCP has two statements:

| Statement | Denies |
|---|---|
| `EnforceSecureTransport` | Any request to S3, SQS, KMS, Secrets Manager or STS where `aws:SecureTransport` is `false` |
| `EnforceOrgIdentities` | Principals whose `aws:PrincipalOrgID` isn't this organization (anonymous callers included), **unless** `aws:PrincipalIsAWSService` is `true` |

Offline docs: [../../docs/organizations/README.md](../../docs/organizations/README.md)

----------------------------------------------------------------------------------

## RCP syntax rules (from the RCP syntax reference)

| Rule | Detail |
|---|---|
| `Version` | Every RCP must include `"Version": "2012-10-17"` |
| `Effect` | `Deny` (only the AWS managed `RCPFullAWSAccess` uses `Allow`) |
| `Principal` | Required in each statement, only `"*"`. Narrow it with `Condition` |
| `Action` | Required. `"*"` on its own isn't allowed; name the service (`"s3:*"`) |
| `Resource` / `NotResource` | One is required in each statement |
| `Condition` | Supported in deny statements |
| `NotAction`, `NotPrincipal` | **Not supported** |
| Size | 5,120 characters |

Scope: RCPs **don't affect resources in the management account**, and **don't apply to calls made by service-linked roles**.

## Why these conditions

From the IAM global condition key reference:
- **`aws:SecureTransport`:** always in the request context. `false` means the request didn't use TLS.
- **`aws:PrincipalOrgID`:** present only when the caller belongs to an organization, and **absent for anonymous requests**. `StringNotEqualsIfExists` therefore also denies anonymous callers.
- **`aws:PrincipalIsAWSService`:** `true` only when an AWS **service principal** (such as `cloudtrail.amazonaws.com`) calls directly. `BoolIfExists ... "false"` keeps those service-to-resource calls working, for example CloudTrail writing to a log bucket.

## Deploy

One-time, from the management account. This also attaches the AWS managed `RCPFullAWSAccess` everywhere, which can't be detached and lets everything through until you attach your own `Deny` RCPs:

```bash
aws organizations enable-policy-type --root-id r-xxxx --policy-type RESOURCE_CONTROL_POLICY
```

```bash
ORG_ID=$(aws organizations describe-organization --query Organization.Id --output text)
aws cloudformation create-stack --stack-name myapp-dev-rcp \
  --template-body file://organizations-rcp-data-perimeter.yaml \
  --parameters ParameterKey=OrganizationId,ParameterValue=$ORG_ID \
               ParameterKey=TargetId,ParameterValue=ou-xxxx-xxxxxxxx
```

## Before attaching broadly

`EnforceOrgIdentities` also blocks **legitimate** access from outside the organization: partners, SaaS tools, cross-org `sts:AssumeRole`, and public S3 content. The RCP examples page recommends reviewing **IAM Access Analyzer external access findings** and **CloudTrail** to find these first. Then either exclude those accounts with an extra condition, such as `aws:PrincipalAccount`, or keep them in an OU without this RCP.

## Docs

- [../../docs/organizations/ug-orgs_manage_policies_rcps.md](../../docs/organizations/ug-orgs_manage_policies_rcps.md) (incl. supported services list)
- [../../docs/organizations/ug-orgs_manage_policies_rcps_syntax.md](../../docs/organizations/ug-orgs_manage_policies_rcps_syntax.md)
- [../../docs/organizations/ug-orgs_manage_policies_rcps_evaluation.md](../../docs/organizations/ug-orgs_manage_policies_rcps_evaluation.md)
- [../../docs/organizations/ug-orgs_manage_policies_authorization_policies.md](../../docs/organizations/ug-orgs_manage_policies_authorization_policies.md) (SCPs and RCPs)
- [../../docs/organizations/iam-reference_policies_condition-keys.md](../../docs/organizations/iam-reference_policies_condition-keys.md)
