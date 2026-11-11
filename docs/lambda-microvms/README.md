
## AWS Lambda MicroVMs - Local Documentation Snapshot

Offline copies of the AWS docs used to build [lambda/lambda-microvms](../../lambda/lambda-microvms/), converted from HTML to Markdown.
Downloaded 2026-11-12. Each file starts with its source URL. Check the live page if something looks off.

### Lambda Developer Guide - MicroVMs

| File | Topic |
|---|---|
| [dg-lambda-microvms-guide.md](dg-lambda-microvms-guide.md) | Overview, how it works, use cases, key features |
| [dg-microvms-how-it-works.md](dg-microvms-how-it-works.md) | Image, connectors, build process, **MicroVM states and transitions** |
| [dg-microvms-getting-started.md](dg-microvms-getting-started.md) | First image and MicroVM: build role, zip, `create-microvm-image`, `run-microvm`, token, `curl` |
| [dg-microvms-images.md](dg-microvms-images.md) | **Sizing (baseline / 4x peak)**, CPU architecture, base image lifecycle, `/ready` and `/validate`, versions, OS capabilities |
| [dg-microvms-images-snapshots.md](dg-microvms-images-snapshots.md) | What a snapshot captures, **uniqueness**, snapshot-safe OpenSSL |
| [dg-microvms-base-image-release-notes.md](dg-microvms-base-image-release-notes.md) | Base image versions 2 and 3 (X86_64) |
| [dg-microvms-launching.md](dg-microvms-launching.md) | `run-microvm` parameters, **idle policy**, `runHookPayload`, tokens, port routing, WebSockets, **lifecycle hooks**, suspend/resume, errors |
| [dg-microvms-networking.md](dg-microvms-networking.md) | Ingress, bandwidth, HTTP/2, **VPC egress connectors**, connector versions, **PrivateLink** and `lambda:ConnectMicrovm` endpoint policy |
| [dg-microvms-security.md](dg-microvms-security.md) | Build vs execution role, tokens, shell tokens, IAM actions |
| [dg-microvms-monitoring.md](dg-microvms-monitoring.md) | Build and runtime logs, CloudTrail management and data events |
| [dg-microvms-troubleshooting.md](dg-microvms-troubleshooting.md) | Shell access, symptom table, build and connector error codes |
| [dg-microvms-best-practices.md](dg-microvms-best-practices.md) | Hooks, snapshot size, token rotation, cost |
| [dg-microvms-integrations.md](dg-microvms-integrations.md) | Integrations index |
| [dg-microvms-integrations-claude-managed-agents.md](dg-microvms-integrations-claude-managed-agents.md) | Claude Managed Agents |
| [dg-microvms-integrations-cursor-self-hosted-machines.md](dg-microvms-integrations-cursor-self-hosted-machines.md) | Cursor Cloud Agents |
| [dg-microvms-integrations-openai-agents-api.md](dg-microvms-integrations-openai-agents-api.md) | OpenAI Agents API |
| [dg-web-functions-networking.md](dg-web-functions-networking.md) | Network connectors (shared with web functions): **operator role trust policy** (`lambda.amazonaws.com`) |
| [al2023-minimal-container.md](al2023-minimal-container.md) | AL2023 minimal container: `microdnf` provides `dnf` |

### CloudFormation

| File | Topic |
|---|---|
| [cfn-aws-resource-lambda-microvmimage.md](cfn-aws-resource-lambda-microvmimage.md) | `AWS::Lambda::MicrovmImage` |
| [cfn-lambda-microvmimage-codeartifact.md](cfn-lambda-microvmimage-codeartifact.md), [cpuconfiguration](cfn-lambda-microvmimage-cpuconfiguration.md), [environmentvariable](cfn-lambda-microvmimage-environmentvariable.md), [resources](cfn-lambda-microvmimage-resources.md) | Image subproperties |
| [cfn-lambda-microvmimage-hooks.md](cfn-lambda-microvmimage-hooks.md), [microvmhooks](cfn-lambda-microvmimage-microvmhooks.md), [microvmimagehooks](cfn-lambda-microvmimage-microvmimagehooks.md) | Hook port and hook states / timeouts |
| [cfn-lambda-microvmimage-logging.md](cfn-lambda-microvmimage-logging.md), [cloudwatchlogging](cfn-lambda-microvmimage-cloudwatchlogging.md) | Logging |
| [cfn-aws-resource-lambda-networkconnector.md](cfn-aws-resource-lambda-networkconnector.md), [config](cfn-lambda-networkconnector-config.md), [vpcegressconfiguration](cfn-lambda-networkconnector-vpcegressconfiguration.md) | `AWS::Lambda::NetworkConnector` |
| [cfn-registry-schema-aws-lambda-microvmimage.json](cfn-registry-schema-aws-lambda-microvmimage.json) | **Registry schema** (from `CloudformationSchema.zip`, us-east-1): all 13 properties required, write-only properties, handler permissions |
| [cfn-registry-schema-aws-lambda-networkconnector.json](cfn-registry-schema-aws-lambda-networkconnector.json) | Registry schema for the connector |

### IAM

| File | Topic |
|---|---|
| [sar-lambda-microvm-actions.md](sar-lambda-microvm-actions.md) | Service Authorization Reference extract: MicroVM actions are authorized on the **`microvmImage`** resource; `RunMicrovm` also needs `lambda:PassNetworkConnector` |

Not saved here: the `lambda-microvms` API shapes come from the botocore 1.44.0 service model (`botocore/data/lambda-microvms/2025-09-09/service-2.json`), because the API reference isn't published in the Lambda API guide.
