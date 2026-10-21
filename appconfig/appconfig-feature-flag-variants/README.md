
## AppConfig Multi-Variant Feature Flags (targets, variants, splits)

[appconfig-feature-flag-variants.yaml](appconfig-feature-flag-variants.yaml)

Since July 2024, one AppConfig feature flag can hold **several variants**, each with its own enabled status, attribute values and **rule**. The caller sends **context** (such as user ID or tier) when it reads the flag, and the AppConfig Agent evaluates the rules **client-side** and returns the first matching variant. This covers:

- **Targets / allow lists:** turn a feature on only for listed users, tiers or accounts.
- **Splits:** send a consistent percentage of users (for example 15%) to a variant for an experiment or gradual rollout.

Offline docs: [../../docs/appconfig/README.md](../../docs/appconfig/README.md)

----------------------------------------------------------------------------------

## What the template creates

```
 AppConfig application <app>-<env>-variants
   environment <env>
   configuration profile "features"  (Type AWS.AppConfig.FeatureFlags, hosted)
     premium_feature   1. AllowList   (in $userId ["user-1", "user-2"])   enabled, discount_percent 20
                       2. GoldTier    (eq $tier "gold")                   enabled, discount_percent 10
                       3. Default     no rule                             disabled
     new_checkout      1. Express15   (split by::$userId pct::15 seed::"new_checkout")  layout express
                       2. Default     no rule                             layout classic
   deployment strategy: all at once, no bake  -> deployment

 Lambda flag-reader + AppConfig Agent extension (layer)
   event {"userId": "...", "tier": "..."} -> GET localhost:2772/... with header Context: userId=...,tier=...
```

### Flag data format (`AWS.AppConfig.FeatureFlags`)

```yaml
version: "1"
flags:                      # definitions: name, description, attribute constraints
  premium_feature:
    attributes:
      discount_percent: { constraints: { type: number, minimum: 0, maximum: 50 } }
values:                     # values per flag
  premium_feature:
    _variants:              # ordered, max 32
      - name: AllowList
        enabled: true
        rule: '(in $userId ["user-1", "user-2"])'
        attributeValues: { discount_percent: 20 }
      - name: Default       # last, no rule
        enabled: false
```

The template writes this as YAML and turns it into JSON with `Fn::ToJsonString`, which needs the `AWS::LanguageExtensions` transform.

## Rules

A rule is an expression over **context values** (`$key`) that must evaluate to `true` or `false`.

| Kind | Operators |
|---|---|
| Comparison | `eq`, `gt`, `gte`, `lt`, `lte` |
| Logical | `and`, `or`, `not` |
| Custom | `begins_with`, `ends_with`, `contains`, `in`, `matches` (`in::` / `pattern::`), `exists` (`key::`), `split` (`by::`, `pct::`, optional `seed::`) |

Operands: strings (`"gold"`), integers, floats, timestamps, booleans, and context values (`$userId`). Examples:

```
(in $userId ["123", "456"])
(and (eq $tier "gold") (gte $age 18))
(ends_with $email "example.com")
(split by::$userId pct::15 seed::"new_checkout")
```

How rules are evaluated:
- **Order:** variants are evaluated **in order**, and the first match wins.
- **Default variant:** returned when nothing matches. It **must be last and has no rule**, otherwise you get `BadRequestException`.
- **Splits:** `split` uses a consistent hash of the `by` value, so the same user always gets the same answer.
  - Splits **don't add up**. `A: pct::20` followed by `B: pct::20` gives A 20% and B **0%**, because B's users were already taken by A. Use `B: pct::25` to get 5%, or give B a different `seed`.
  - Without `seed`, the split is consistent only within that flag. With `seed`, it's consistent across flags, profiles and accounts.

----------------------------------------------------------------------------------

## Deploy

```bash
aws cloudformation create-stack --stack-name myapp-dev-appconfig-variants \
  --template-body file://appconfig-feature-flag-variants.yaml \
  --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND   # AUTO_EXPAND for AWS::LanguageExtensions
```

The extension layer ARN is resolved from the AWS public SSM parameter `/aws/service/aws-appconfig/lambda-extension/x86/latest`, so it's always the latest version for your Region. For an arm64 function, use `.../arm64/latest` and change `Architectures`.

## Try it

```bash
FN=$(aws cloudformation describe-stacks --stack-name myapp-dev-appconfig-variants \
  --query "Stacks[0].Outputs[?OutputKey=='FlagReaderLambdaFunctionName'].OutputValue" --output text)

for p in '{"userId":"user-1"}' '{"userId":"user-9","tier":"gold"}' '{"userId":"user-9"}' '{}'; do
  aws lambda invoke --function-name $FN --payload "$p" --cli-binary-format raw-in-base64-out out.json >/dev/null
  cat out.json; echo
done
```

| Context | `premium_feature` | `new_checkout` |
|---|---|---|
| `userId=user-1` | `AllowList` (enabled, 20) | `Express15` or `Default`, depending on the hash of `user-1` |
| `userId=user-9`, `tier=gold` | `GoldTier` (enabled, 10) | Hash of `user-9` |
| `userId=user-9` | `Default` (disabled) | Hash of `user-9` |
| none | `Default` | `Default`: without the context key a rule uses, the docs say the default variant is returned |

Each returned flag includes `"_variant": "<name>"`. Run the loop with many user IDs to see about 15% get `Express15`.

The same call from your own code, through any AppConfig Agent (Lambda, EC2, ECS, EKS):

```bash
curl "http://localhost:2772/applications/<app>/environments/<env>/configurations/features?flag=premium_feature" \
  -H "Context: userId=user-1" -H "Context: tier=gold"     # or one header: Context: userId=user-1,tier=gold
```

## Notes

- **Agent version:** variants need a recent AppConfig Agent, and `?flag=` single-flag retrieval needs agent 2.0.45 or later. Read flags with `GetLatestConfiguration` (or the agent). The older `GetConfiguration` is deprecated and can't return feature flag data.
- **What the caller receives:** a simplified JSON with `enabled`, the attribute values and `_variant`. The definitions and rules aren't included.
- **IAM:** the Lambda role needs `appconfig:StartConfigurationSession` and `appconfig:GetLatestConfiguration`. The template uses `Resource: "*"`, so scope it to the configuration ARN for production.
- **Deletion protection:** this is an account setting (`aws appconfig update-account-settings --deletion-protection Enabled=true,ProtectionPeriodInMinutes=60`). It blocks deleting an environment or profile that was read in the last 15–1440 minutes.
  - **Fresh resources:** resources created in the past hour are normally excluded from the check, so a test stack you delete soon after creating is usually fine.
  - **Overrides:** `DeletionProtectionCheck` on the Environment or ConfigurationProfile accepts `ACCOUNT_DEFAULT` (the default), `BYPASS` (skip the check) or `APPLY` (always check, including new resources).
- **Rollout:** the deployment strategy is "all at once" for the demo. For real rollouts, use `DeploymentDurationInMinutes` > 0, a `GrowthFactor` below 100, and environment `Monitors` with CloudWatch alarms for automatic rollback.

## Docs

- [../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-concepts.md](../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-concepts.md)
- [../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-rules.md](../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-rules.md) (split operator)
- [../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-rules-operators.md](../../docs/appconfig/ug-appconfig-creating-multi-variant-feature-flags-rules-operators.md)
- [../../docs/appconfig/ug-appconfig-type-reference-feature-flags.md](../../docs/appconfig/ug-appconfig-type-reference-feature-flags.md)
- [../../docs/appconfig/ug-appconfig-integration-retrieving-feature-flags.md](../../docs/appconfig/ug-appconfig-integration-retrieving-feature-flags.md)
- [../../docs/appconfig/ug-appconfig-integration-lambda-extensions-versions.md](../../docs/appconfig/ug-appconfig-integration-lambda-extensions-versions.md) (public SSM parameter)
