<!-- Source: https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations.html -->
<!-- Downloaded: 2026-11-12 -->

# Integrations

AWS Lambda MicroVMs provides isolated, snapshot-based compute environments that AI agent frameworks and development tools can use as sandboxes. Each integration follows the same pattern: you build a reusable MicroVM image, and the framework launches one MicroVM per session or job through the Lambda API.

The following integrations are available:

-

**[Using Lambda MicroVMs as a sandbox for Claude Managed Agents](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html)** – Use Lambda MicroVMs as a self-hosted sandbox for Anthropic's Claude Managed Agents. The agent loop runs on Anthropic's infrastructure; the MicroVM runs your tool calls. A webhook-driven controller launches one MicroVM per session.
-

**[Using Lambda MicroVMs as a sandbox for Cursor Cloud Agents](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-cursor-self-hosted-machines.html)** – Use Lambda MicroVMs as self-hosted machines for Cursor Cloud Agents. A scheduled controller polls for pending pool requests and launches a MicroVM for each worker session.
-

**[Using Lambda MicroVMs as a sandbox for OpenAI Agents API](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-openai-agents-api.html)** – Use Lambda MicroVMs as a self-hosted environment for agents built with the OpenAI Agents API. Your application or a webhook launcher starts a MicroVM for each turn, with optional suspend and resume between turns.
