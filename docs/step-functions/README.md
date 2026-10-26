
## AWS Step Functions - Local Documentation Snapshot

Offline copies of the AWS docs used to build [step-functions/step-functions-jsonata](../../step-functions/step-functions-jsonata/), converted from HTML to Markdown.
Downloaded 2026-10-26. Each file starts with its source URL. Check the live page if something looks off.

The Step Functions pages used for the durable functions comparison (`.waitForTaskToken`, Standard vs Express) are in [../lambda](../lambda/README.md).

| File | Topic |
|---|---|
| [ug-document-history.md](ug-document-history.md) | Document history (variables and JSONata: 2024-11-22) |
| [ug-workflow-variables.md](ug-workflow-variables.md) | Variables: `Assign`, `$states`, scope (Map / Parallel / Distributed Map), evaluation order, limits, variables in JSONPath |
| [ug-transforming-data.md](ug-transforming-data.md) | JSONata: `QueryLanguage`, `{% %}`, `Arguments` / `Output`, Choice `Condition`, errors (`States.QueryEvaluationError`), JSONPath → JSONata conversion, examples, Step Functions functions (`$partition`, `$range`, `$hash`, `$random`, `$uuid`, `$parse`) |
| [ug-concepts-input-output-filtering.md](ug-concepts-input-output-filtering.md) | Processing input and output |
| [ug-amazon-states-language-paths.md](ug-amazon-states-language-paths.md) | JSONPath paths (classic) |
| [ug-statemachine-structure.md](ug-statemachine-structure.md) | State machine structure (top-level `QueryLanguage`) |
| [ug-amazon-states-language-task-state.md](ug-amazon-states-language-task-state.md) | Task state fields per query language |
| [ug-amazon-states-language-choice-state.md](ug-amazon-states-language-choice-state.md) | Choice state (`Condition` vs `Variable` + comparison) |
| [ug-state-map.md](ug-state-map.md) | Map state (`Items` vs `ItemsPath`) |
