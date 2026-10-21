
## Service Control Policies (SCPs) - IAM policy language

[organizations-scp-iam-language.yaml](organizations-scp-iam-language.yaml)

SCPs set the **maximum permissions for IAM users and roles in member accounts**. They never grant access themselves. The SCP syntax reference now lists `Condition`, `NotAction` and `NotResource` as supported in **both `Allow` and `Deny`** statements. The template has one policy per pattern:

| Policy | Pattern | Attached |
|---|---|---|
| `scp-region-guardrail` | `Deny` + `NotAction` (global services exempt) + `Condition` `aws:RequestedRegion` + `ArnNotLike aws:PrincipalArn` (break-glass role exempt) | `TargetId` |
| `scp-protect-platform-role` | `Deny` on a **specific role ARN** + `Condition` exemption | `TargetId` |
| `scp-bedrock-model-allow-list` | `Deny` + **`NotResource`**: invoking any model except the listed ARNs is denied | `TargetId` |
| `scp-allow-list-example` | **`Allow` + `Condition`** (`aws:PrincipalArn`) | Not attached |

Offline docs: [../../docs/organizations/README.md](../../docs/organizations/README.md)

----------------------------------------------------------------------------------

## SCP syntax rules (from the SCP syntax reference)

| Rule | Detail |
|---|---|
| `Version` | Every SCP must include `"Version": "2012-10-17"` |
| `Resource` / `NotResource` | **Every statement must include one** (clarified in the docs, June 2026) |
| `Allow` + `Resource` | Only `"*"`. Specific ARNs can't be used in `Allow` statements |
| `Deny` + `Resource` | Specific ARNs, wildcards, or `NotResource` |
| `Condition`, `NotAction` | Supported in `Allow` and `Deny` |
| Wildcards | `*` and `?` in `Action` / `NotAction` / `Resource` |
| `Principal`, `NotPrincipal` | **Not supported.** Target principals with `aws:PrincipalArn` in a `Condition` |
| Size | 5,120 characters per SCP (whitespace counts) |

Scope:
- **Not affected:** users and roles in the **management account**, and **service-linked roles**.
- **Affected:** member accounts that are delegated administrators.

## Deny list vs allow list

| Strategy | `FullAWSAccess` SCP | How you restrict | This template |
|---|---|---|---|
| Deny list (default) | Stays attached | Add `Deny` SCPs | The three attached policies |
| Allow list | **Detached** | `Allow` only what's permitted; everything else is implicitly denied | `scp-allow-list-example` (created, **not attached**) |

An `Allow` SCP has **no effect** while `FullAWSAccess` is attached to the same root, OU or account. Detaching `FullAWSAccess` without a working allow list cuts access for every principal in scope. So the example is created unattached, for you to attach on purpose:

```bash
aws organizations attach-policy --policy-id <AllowListExampleServiceControlPolicyId> --target-id <test-ou>
aws organizations detach-policy --policy-id p-FullAWSAccess --target-id <test-ou>   # only once the allow list is complete
```

## Content as a JSON object

```yaml
Content:            # object: drift detection works
  Version: "2012-10-17"
  Statement:
    - Effect: Deny
      ...
# Content: >-      # JSON string: no drift detection
#   { "Version": "2012-10-17", ... }
```

The `AWS::Organizations::Policy` reference warns that a JSON string prevents drift detection. The older [../organizations.yaml](../organizations.yaml) has been converted to objects too.

----------------------------------------------------------------------------------

## Deploy

One-time, from the management account. CloudFormation can't enable policy types:

```bash
aws organizations enable-policy-type --root-id r-xxxx --policy-type SERVICE_CONTROL_POLICY
```

```bash
aws cloudformation create-stack --stack-name myapp-dev-scp \
  --template-body file://organizations-scp-iam-language.yaml \
  --parameters ParameterKey=TargetId,ParameterValue=ou-xxxx-xxxxxxxx \
               ParameterKey=AllowedRegionList,ParameterValue='us-east-1\,us-west-2'
```

Test from an account in the target OU:

```bash
aws ec2 describe-vpcs --region eu-west-1      # AccessDenied ... explicit deny in a service control policy
aws ec2 describe-vpcs --region us-east-1      # works
aws iam list-roles                            # works (iam:* exempt via NotAction)
```

## Notes

- **Global services list:** the `NotAction` list is the AWS doc example. Real organizations usually exempt more global or management services, so extend it after checking CloudTrail.
- **`BedrockAllowedModelArnList`:** the default only allows Amazon Titan text models. If you call models through inference profiles, the request's resource is the inference-profile ARN, so add those ARNs too.
- **Updates:** changing a policy's `Type` replaces it. Changing `Content` doesn't interrupt anything.

## Docs

- [../../docs/organizations/ug-orgs_manage_policies_scps_syntax.md](../../docs/organizations/ug-orgs_manage_policies_scps_syntax.md)
- [../../docs/organizations/ug-orgs_manage_policies_scps.md](../../docs/organizations/ug-orgs_manage_policies_scps.md)
- [../../docs/organizations/ug-orgs_manage_policies_scps_evaluation.md](../../docs/organizations/ug-orgs_manage_policies_scps_evaluation.md)
- [../../docs/organizations/cfn-aws-resource-organizations-policy.md](../../docs/organizations/cfn-aws-resource-organizations-policy.md)
