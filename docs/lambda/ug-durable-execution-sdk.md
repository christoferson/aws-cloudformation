> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk.html
> Downloaded: 2026-10-25

# Durable execution SDK

The durable execution SDK is the foundation for building durable functions. It provides primitives to checkpoint progress, handle retries, and manage execution flow. The SDK abstracts the complexity of checkpoint management and replay, letting you write sequential code that automatically becomes fault-tolerant.

The SDK is available for JavaScript, TypeScript, Python, Java, Go, and C# (.NET). For complete API documentation, quickstart tutorials, and language-specific guides, see the AWS Durable Execution SDK Developer Guide. 

## What the SDK does 

Checkpoint management: The SDK automatically creates checkpoints as your function executes durable operations. Each checkpoint records the operation type, inputs, and results. When your function completes a step, the SDK persists the checkpoint before continuing. This ensures your function can resume from any completed operation if interrupted. 

Replay coordination: When your function resumes after a pause or interruption, the SDK performs replay. It runs your code from the beginning but skips completed operations, using stored checkpoint results instead of re-executing them. The SDK ensures replay is deterministic. Given the same inputs and checkpoint log, your function produces the same results. 

State isolation: The SDK maintains execution state separately from your business logic. Each durable execution has its own checkpoint log that other executions cannot access. The SDK encrypts checkpoint data at rest and ensures state remains consistent across replays. 

For a detailed explanation of how checkpointing works and replay behavior, see Key concepts in the AWS Durable Execution SDK Developer Guide. 

## Durable operations 

The SDK provides your function with a `DurableContext` object. This context replaces the standard Lambda context and provides methods for creating checkpoints, managing execution flow, and coordinating with external systems. 

The `DurableContext` provides the following operations for building durable workflows:  
|  Operation |  Description |    
|  Step |  Execute and checkpoint a unit of work with configurable retry strategies and execution semantics. |   
|  Wait |  Pause execution for a specified duration without consuming compute resources. |   
|  Wait for Condition |  Poll for a condition with automatic checkpointing between attempts. |   
|  Callback |  Pause execution and wait for an external system to provide input through the Lambda API. |   
|  Invoke |  Call another Lambda function and wait for its result, with automatic checkpointing. |   
|  Parallel |  Execute multiple operations concurrently with configurable completion policies. |   
|  Map |  Process each item in a collection concurrently with optional concurrency control. |   
|  Child Context |  Create an isolated execution context for grouping multiple operations. |    

Each durable operation creates checkpoints automatically, ensuring your function can resume from any point. For detailed API reference, code examples, and language-specific usage, see SDK Reference in the AWS Durable Execution SDK Developer Guide. 

## How durable operations are metered 

Each durable operation you call through `DurableContext` creates checkpoints to track execution progress and store state data. These operations incur charges based on their usage, and the checkpoints may contain data that contributes to your data write and retention costs. Stored data includes invocation event data, payloads returned from steps, and data passed when completing callbacks. Understanding how durable operations are metered helps you estimate execution costs and optimize your workflows. For details on pricing, see the Lambda pricing page. 

Payload size refers to the size of the serialized data that a durable operation persists. The data is measured in bytes and the size can vary depending on the serializer used by the operation. The payload of an operation could be the result itself for successful completions, or the serialized error object if the operation failed. 

### Basic operations 

Basic operations are the fundamental building blocks for durable functions:  
|  Operation |  Checkpoint timing |  Number of operations |  Data persisted |    
|  Execution |  Started |  1 |  Input payload size |   
|  Execution |  Completed (Succeeded/Failed/Stopped) |  0 |  Output payload size |   
|  Step |  Retry/Succeeded/Failed |  1 + N retries |  Returned payload size from each attempt |   
|  Wait |  Started |  1 |  N/A |   
|  WaitForCondition |  Each poll attempt |  1 + N polls |  Returned payload size from each poll attempt |   
|  Invocation-level Retry |  Started |  1 |  Payload for error object |    

### Callback operations 

Callback operations enable your function to pause and wait for external systems to provide input. These operations create checkpoints when the callback is created and when it's completed:  
|  Operation |  Checkpoint timing |  Number of operations |  Data persisted |    
|  CreateCallback |  Started |  1 |  N/A |   
|  Callback completion through API call |  Completed |  0 |  Callback payload |   
|  WaitForCallback |  Started |  3 + N retries (context + callback + step) |  Payloads returned by submitter step attempts, plus two copies of the callback payload |    

### Compound operations 

Compound operations combine multiple durable operations to handle complex coordination patterns like parallel execution, array processing, and nested contexts:  
|  Operation |  Checkpoint timing |  Number of operations |  Data persisted |    
|  Parallel |  Started |  1 + N branches (1 parent context + N child contexts) |  Up to two copies of the returned payload size from each branch, plus the statuses of each branch |   
|  Map |  Started |  1 + N branches (1 parent context + N child contexts) |  Up to two copies of the returned payload size from each iteration, plus the statuses of each iteration |   
|  Promise helpers |  Completed |  1 |  Returned payload size from the promise |   
|  RunInChildContext |  Succeeded/Failed |  1 |  Returned payload size from the child context |    

For contexts, such as from `runInChildContext` or used internally by compound operations, results smaller than 256 KB are checkpointed directly. Larger results aren't stored—instead, they're reconstructed during replay by re-processing the context's operations.
