
## Resource Control Policies (RCPs) - data perimeter

### The problem

Your data sits in S3 buckets, KMS keys, SQS queues and secrets. Each one can have a **resource policy**, written by whichever developer created it, and any of them can open the data to the world:

```json
{ "Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::customer-exports/*" }
```

An SCP doesn't help here. An SCP only limits **your own** roles and users, and the attacker in these cases isn't one of them:
- An anonymous user on the internet.
- A role in somebody else's AWS account.
- Your own access keys, leaked on GitHub and used from a laptop in another country.

### What a data perimeter is

A **data perimeter** is a small set of org-wide rules that answer three questions for **every** request, whatever the individual bucket, key or queue policies say:

| Question | Perimeter | "Allowed" means |
|---|---|---|
| **Who** is calling? | Identity perimeter | A principal in **our organization**, a named partner account, or an AWS service working **for us** |
| **From where?** | Network perimeter | **Our VPC endpoints** or **our office / VPN / NAT IP ranges** |
| **What** is it calling? | Resource perimeter | **Our** resources. This one is an SCP, because it limits our principals, so it's not in this folder |

An **RCP** is the tool for the first two on the resource side. It's attached to the organization root, an OU or an account, and caps what **anyone** can do to the resources there. It only denies, so a resource policy can still grant less, but never more.

```
                     request ─► S3 bucket in account 111111111111 (OU: Production)
                                │
   RCPs attached to root ─┐     │   1. RCP: is the caller in our org?          (identity perimeter)
   RCPs attached to OU   ─┼───► │   2. RCP: is it from our network?            (network perimeter)
   RCPs attached to acct ─┘     │   3. RCP: TLS 1.2+, no SSE-C, ...            (guardrails)
                                │   4. Bucket policy / IAM policy: is it allowed?
                                ▼
                     allowed only if no RCP denies AND a policy allows
```

### What `AttachToTargetId` (TargetIds) is

It is **where in the organization tree the policy is attached**, and therefore which accounts' resources it protects:

```
 Root  r-ab12                         ← attach here = every member account
 ├── OU Security    ou-ab12-22222222  ← attach here = only accounts in this OU (and child OUs)
 │     ├── 222222222222 (log archive)
 │     └── 333333333333 (audit)
 ├── OU Production  ou-ab12-11111111
 │     └── 444444444444               ← attach here = only this account
 └── OU Sandbox     ou-ab12-33333333
       └── 555555555555
```

```bash
aws organizations list-roots --query "Roots[].Id"                                     # r-...
aws organizations list-organizational-units-for-parent --parent-id r-ab12 \
  --query "OrganizationalUnits[].[Name,Id]" --output table                            # ou-...
aws organizations list-accounts --query "Accounts[].[Name,Id]" --output table          # 12 digits
```

Start with **one test account**, then a test OU, then wider. RCPs never affect resources in the **management account**.

----------------------------------------------------------------------------------

## Templates

Each one is a realistic scenario based on the AWS example policies (saved in [docs/organizations/github](../../docs/organizations/github/)). They are meant to be used **together**.

| Template | Stops | Still works |
|---|---|---|
| [organizations-rcp-identity-perimeter.yaml](organizations-rcp-identity-perimeter.yaml) | A bucket, key, queue, secret, table or ECR repo opened to `Principal: "*"` or a foreign account. Another AWS customer pointing **their** CloudTrail or SNS at **your** bucket or queue (confused deputy). **Any GitHub repo in the world** assuming a role whose trust policy forgot to pin `sub` | Your org's roles. Listed partner accounts. AWS services acting for your org. Resources tagged `dp:exclude:identity=true` (public website bucket). Only your GitHub org's repos |
| [organizations-rcp-network-perimeter.yaml](organizations-rcp-network-perimeter.yaml) | **Leaked or stolen credentials** used from outside your networks, even though they're valid | Calls via your org's VPC endpoints or corporate IPs. AWS services calling for you (S3 → KMS for SSE-KMS, Athena → S3). EBS decryption. Only principals tagged `dp:include:network=true` are restricted (phased rollout) |
| [organizations-rcp-s3-kms-guardrails.yaml](organizations-rcp-s3-kms-guardrails.yaml) | Plain HTTP and TLS < 1.2. **SSE-C ransomware**: an attacker re-encrypts your objects with a key only they hold. **Leaked presigned URLs** older than 1 hour. **KMS key deletion** by anyone but the KMS admin role, since a deleted key makes its data unreadable forever | Normal TLS 1.2+ traffic, SSE-S3 / SSE-KMS uploads, short-lived presigned URLs, the `KmsAdministrator` role |
| [organizations-rcp-ou-boundary.yaml](organizations-rcp-ou-boundary.yaml) | A **dev / sandbox** role reading **production** data, even though it's in the same org and the bucket policy lets it in | Principals in the Production and Security OUs. AWS service principals |

### Example: one bucket, five callers

Bucket `customer-exports` in a production account. Its bucket policy (mistakenly) allows `Principal: "*"`. All four RCPs are attached.

| Caller | Result | Stopped by |
|---|---|---|
| Anonymous `curl https://customer-exports.s3.amazonaws.com/file.csv` | Denied | `EnforceOrgIdentities` (no `aws:PrincipalOrgID`) |
| A role in a stranger's AWS account | Denied | `EnforceOrgIdentities` |
| Your sandbox developer role | Denied | `EnforceProductionOuBoundary` |
| Your prod app role, with keys leaked and used from home, tagged `dp:include:network=true` | Denied | `EnforceNetworkPerimeterVpceOrgID` |
| Your prod app role, from the VPC through an org-owned S3 VPC endpoint, TLS 1.2 | **Allowed** | — |

----------------------------------------------------------------------------------

## RCP rules (from the RCP syntax reference)

| Rule | Detail |
|---|---|
| `Effect` | `Deny` only (the AWS managed `RCPFullAWSAccess` is the only `Allow`) |
| `Principal` | Required, and must be `"*"`. Narrow it with `Condition` |
| `Action` | `"*"` alone isn't allowed. Name the service (`"s3:*"`) |
| `NotAction`, `NotPrincipal` | Not supported |
| Services | Only those on the **RCP supported list** (S3, KMS, SQS, Secrets Manager, STS, DynamoDB, CloudWatch Logs, ECR, Cognito, ...) |
| Size | 5,120 characters per policy (these templates are about 500 to 1,500) |
| Scope | Not the management account, not service-linked roles |

### How the conditions read

A Deny statement applies only if **every** condition block matches. Within one `StringNotEqualsIfExists` block, all keys must be "not equal", so **any single match is an exception**:

```yaml
StringNotEqualsIfExists:              # deny unless the caller is in our org
  aws:PrincipalOrgID: o-abc           #   OR is a trusted account
  aws:PrincipalAccount: [111, 222]    #   OR the resource is tagged as excluded
  aws:ResourceTag/dp:exclude:identity: "true"
BoolIfExists:
  aws:PrincipalIsAWSService: "false"  # AND the caller is not an AWS service principal
```

`...IfExists` matters when a key is missing from the request. For example, anonymous callers have no `aws:PrincipalOrgID`, so "not equal if exists" counts as true and they are denied.

### Tags used for exceptions (AWS data perimeter convention)

| Tag (`true`) | On | Effect |
|---|---|---|
| `dp:exclude:identity` | Resource | Exempt from the identity perimeter (public content) |
| `dp:include:network` | Principal | **Opt in** to the network perimeter |
| `dp:exclude:network` | Principal / resource | Exempt from the network perimeter |

Whoever can set these tags can bypass the perimeter, so restrict tagging with an SCP. AWS's `data_perimeter_governance_scp.json` and `_rcp.json` show how.

----------------------------------------------------------------------------------

## Deploy

One-time, from the management account. This also attaches `RCPFullAWSAccess` everywhere, which allows everything until you add Deny RCPs:

```bash
aws organizations enable-policy-type --root-id r-ab12 --policy-type RESOURCE_CONTROL_POLICY
```

```bash
ORG_ID=$(aws organizations describe-organization --query Organization.Id --output text)

aws cloudformation create-stack --stack-name myapp-dev-rcp-identity \
  --template-body file://organizations-rcp-identity-perimeter.yaml \
  --parameters ParameterKey=OrganizationId,ParameterValue=$ORG_ID \
               ParameterKey=AttachToTargetId,ParameterValue=444444444444 \
               ParameterKey=TrustedExternalAccountIds,ParameterValue='127311923021' \
               ParameterKey=GitHubOrganization,ParameterValue=my-github-org
```

In that example, `127311923021` is the ELB access-log account for us-east-1. It's only needed if load balancers there write access logs to S3. Check the ELB documentation for your Region.

**Org path** for the OU boundary, needed by `ProductionOrgPath` and `SecurityOrgPath`. It is `<org-id>/<root-id>/<ou-id>/`, with nested OUs appended, for example `o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/`.

## Before attaching broadly

- **Find legitimate external access first:** IAM Access Analyzer external access findings (public and cross-account resources), and CloudTrail for calls from outside the org or from unexpected IPs.
- **Known exceptions** (from AWS's guidance):
  - ELB access logs in older Regions use an AWS-owned account.
  - CloudFront **OAI** is blocked by the identity perimeter, so migrate to **OAC**.
  - SaaS vendors that read your buckets.
  - Cross-org `sts:AssumeRole`.
- **Watch for `AccessDenied` after attaching:** check CloudTrail for the denied calls and add exceptions as needed.

## Docs

- [../../docs/organizations/github/data-perimeter-policy-examples/README.md](../../docs/organizations/github/data-perimeter-policy-examples/README.md) (identity / resource / network perimeter, tag convention)
- [../../docs/organizations/github/data-perimeter-policy-examples/resource_control_policies/README.md](../../docs/organizations/github/data-perimeter-policy-examples/resource_control_policies/README.md) (why each statement, service access patterns)
- [../../docs/organizations/github/resource-control-policy-examples/README.md](../../docs/organizations/github/resource-control-policy-examples/README.md) (service-specific RCPs: S3, KMS, OIDC, OU boundaries)
- [../../docs/organizations/ug-orgs_manage_policies_rcps.md](../../docs/organizations/ug-orgs_manage_policies_rcps.md) (supported services)
- [../../docs/organizations/ug-orgs_manage_policies_rcps_syntax.md](../../docs/organizations/ug-orgs_manage_policies_rcps_syntax.md)
- [../../docs/organizations/iam-reference_policies_condition-keys.md](../../docs/organizations/iam-reference_policies_condition-keys.md) (`aws:PrincipalOrgID`, `aws:VpceOrgID`, `aws:SourceOrgID`, `aws:PrincipalOrgPaths`, ...)
