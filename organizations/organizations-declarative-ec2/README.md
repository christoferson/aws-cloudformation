
## Declarative Policies for EC2

[organizations-declarative-ec2.yaml](organizations-declarative-ec2.yaml)

Declarative policies (added December 2024) **declare a service configuration** for every account in scope, rather than denying API calls. Once attached, the configuration is always maintained, even as the service adds new features or APIs. Account administrators can't change it locally.

| | SCP | Declarative policy (EC2) |
|---|---|---|
| Mechanism | Deny or allow **API actions** for principals | Set **account attributes** (EC2, VPC, EBS) |
| Example | Deny `ec2:EnableSerialConsoleAccess` | `serial_console_access.status = disabled` |
| New APIs | You must add each one | Covered automatically |
| `Type` | `SERVICE_CONTROL_POLICY` | `DECLARATIVE_POLICY_EC2` |

What the template sets:

| Attribute | Value | Effect |
|---|---|---|
| `image_block_public_access.state` | `block_new_sharing` | No new public AMI sharing (AMIs that are already public stay public) |
| `snapshot_block_public_access.state` | `block_new_sharing` | No new public EBS snapshot sharing (`block_all_sharing` would also make existing public snapshots private) |
| `serial_console_access.status` | `disabled` | EC2 serial console blocked |
| `instance_metadata_defaults.http_tokens` | `required` | IMDSv2 is the default for new launches |
| `instance_metadata_defaults.http_tokens_enforced` | `enabled` | Launching or switching an instance to IMDSv1 fails |
| `instance_metadata_defaults.http_put_response_hop_limit` | `2` | The docs recommend at least 2 when tokens are required |
| `exception_message` | `ExceptionMessage` parameter | Error text for calls that conflict with the policy |

Not included: **VPC Block Public Access** (`block_ingress` / `block_bidirectional`), because it would cut internet access for existing VPCs. **VPC Encryption Controls** are also supported by EC2 policies. See the syntax page.

Offline docs: [../../docs/organizations/README.md](../../docs/organizations/README.md)

----------------------------------------------------------------------------------

## Syntax

Declarative policies use the management-policy syntax: a fixed top-level key (`ec2_attributes`), with values set through `@@assign`:

```yaml
Content:
  ec2_attributes:
    serial_console_access:
      status:
        "@@assign": disabled
```

In YAML the `"@@assign"` keys must be quoted, because `@` can't start a plain scalar. Maximum size is 10,000 characters.

## Deploy

One-time, from the management account:

```bash
aws organizations enable-policy-type --root-id r-xxxx --policy-type DECLARATIVE_POLICY_EC2
```

Recommended before attaching: generate the **account status report** (see "Generating the account status report" in [../../docs/organizations/ug-orgs_manage_policies_ec2.md](../../docs/organizations/ug-orgs_manage_policies_ec2.md)). It shows each attribute's current value across accounts and Regions.

```bash
aws cloudformation create-stack --stack-name myapp-dev-declarative-ec2 \
  --template-body file://organizations-declarative-ec2.yaml \
  --parameters ParameterKey=TargetId,ParameterValue=ou-xxxx-xxxxxxxx
```

## Before attaching broadly

- **IMDSv1:** check that no instances or launch templates still depend on IMDSv1. With `http_tokens_enforced: enabled`, those launches fail.
- **Locked operations:** the operations each attribute controls stop working in member accounts. Examples are `EnableSerialConsoleAccess` and `DisableImageBlockPublicAccess`, and the syntax page lists more per attribute.
- **Error text:** don't put personal or sensitive information in `ExceptionMessage`.

## Docs

- [../../docs/organizations/ug-orgs_manage_policies_ec2.md](../../docs/organizations/ug-orgs_manage_policies_ec2.md)
- [../../docs/organizations/ug-orgs_manage_policies_ec2_syntax.md](../../docs/organizations/ug-orgs_manage_policies_ec2_syntax.md)
- [../../docs/organizations/ug-orgs_manage_policies_declarative.md](../../docs/organizations/ug-orgs_manage_policies_declarative.md)
