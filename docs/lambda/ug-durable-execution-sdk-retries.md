> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk-retries.html
> Downloaded: 2026-10-25

# Retries for Lambda durable functions

Durable functions provide automatic retry capabilities that make your applications resilient to transient failures. The SDK handles retries at two levels: step retries for business logic failures and backend retries for infrastructure failures. 

## Step retries 

When an uncaught exception occurs within a step, the SDK automatically retries the step based on the configured retry strategy. Step retries are checkpointed operations that allow the SDK to suspend execution and resume later without losing progress. 

### Step retry behavior 

The following table describes how the SDK handles exceptions within steps:  
|  Scenario |  What happens |  Metering impact |    
|  Exception in step with remaining retry attempts |  The SDK creates a checkpoint for the retry and suspends the function. On the next invocation, the step retries with the configured backoff delay. |  1 operation + error payload size |   
|  Exception in step with no remaining retry attempts |  The step fails and throws an exception. If your handler code doesn't catch this exception, the entire execution fails. |  1 operation + error payload size |    

When a step needs to retry, the SDK checkpoints the retry state and exits the Lambda invocation if no other work is running. This allows the SDK to implement backoff delays without consuming compute resources. The function resumes automatically after the backoff period. 

### Configuring step retry strategies 

Configure retry strategies to control how steps handle failures. You can specify maximum attempts, backoff intervals, and conditions for retrying. For a complete reference of retry strategy helpers, presets, and custom strategies, see Retries in the Durable Execution SDK documentation. 

## Exceptions outside steps 

When an uncaught exception occurs in your handler code but outside any step, the SDK marks the execution as failed. This ensures errors in your application logic are properly captured and reported.  
|  Scenario |  What happens |  Metering impact |    
|  Exception in handler code outside any step |  The SDK marks the execution as FAILED and returns the error. The exception is not automatically retried. |  Error payload size |    

To enable automatic retry for error-prone code, wrap it in a step with a retry strategy. Steps provide automatic retry with configurable backoff, while code outside steps fails immediately. 

## Invocation retries 

Invocation level retries are handled differently depending on how the Lambda durable function is attempted to be invoked. The following table describes how the different invocation types might influence the invocation level retries.  
|  Invocation type |  What happens |    
|  Synchronous invocation |   Lambda does not automatically retry the invocation on an error during durable function execution. Retries on invocation failures depend on the source of the synchronous invocation. For example, using the AWS SDK, InternalFailure and ThrottlingException are by default retried automatically.  |   
|  Asynchronous invocation |   If a durable function execution fails (for example, it enters a FAILED, STOPPED, or TIMED_OUT status), Lambda does not retry the execution. This is different from functions without durable execution, where Lambda retries the function on asynchronous invocation failures. The `MaximumRetryAttempts` setting for asynchronous invocations does not apply to durable executions. If you configure a dead-letter queue (DLQ) for the function, Lambda sends the triggering event to the DLQ.  |   
|  ESM (Event Source Mapping) |   Lambda by default retries the entire batch until it succeeds. For stream sources (DynamoDB and Kinesis), you can configure the maximum number of times that Lambda retries when your function returns an error. See event source mappings batching. For Amazon SQS ESM, you can configure max retries through a DLQ on the original Amazon SQS queue. See configure Amazon SQS ESM. As best practice, you might consider a DLQ at the function level and Lambda sends the failing triggering event to the DLQ. See function DLQ.  |   
|  Direct Trigger |   This depends on the "Trigger". For example, Lambda processes functions triggered by Amazon S3 event notifications asynchronously. See Process Amazon SQS event notifications with Lambda. Lambda processes functions triggered by Amazon SNS event notifications, asynchronously. See Invoking Lambda functions with Amazon SNS notifications. The asynchronous invocation retry behavior is above in the "Asynchronous invocation" table entry. If Amazon SNS can't reach Lambda or the message is rejected, Amazon SNS retries at increasing intervals over several hours. For details, see Reliability in the Amazon SNS FAQs. API Gateway synchronously invokes Lambda and returns the genuine error response back to the requester. See invocation retries. The synchronous invocation retry behavior is above in the "Synchronous invocation" table entry. See each direct trigger for more details.  |    

## Backend retries 

Backend retries occur when Lambda encounters infrastructure failures, runtime errors, or when the SDK cannot communicate with the durable execution service. Lambda automatically retries these failures to help your durable functions recover from transient infrastructure issues. 

### Backend retry scenarios 

Lambda automatically retries your function when it encounters the following scenarios:  
Internal service errors - When Lambda or the durable execution service returns a 5xx error, indicating a temporary service issue. 
Throttling - When your function is throttled due to concurrency limits or service quotas. 
Timeouts - When the SDK cannot reach the durable execution service within the timeout period. 
Sandbox initialization failures - When Lambda cannot initialize the execution environment. 
Runtime errors - When the Lambda runtime encounters errors outside your function code, such as out-of-memory errors or process crashes. 
Invalid checkpoint token errors - When the checkpoint token is no longer valid, typically due to service-side state changes. 
 

The following table describes how the SDK handles these scenarios:  
|  Scenario |  What happens |  Metering impact |    
|  Runtime error outside durable handler (OOM, timeout, crash) |  Lambda automatically retries the invocation. The SDK replays from the last checkpoint, skipping completed steps. |  Error payload size + 1 operation per retry |   
|  Service error (5xx) or timeout when calling `CheckpointDurableExecution` / `GetDurableExecutionState` APIs |  Lambda automatically retries the invocation. The SDK replays from the last checkpoint. |  Error payload size + 1 operation per retry |   
|  Throttling (429) or invalid checkpoint token when calling `CheckpointDurableExecution` / `GetDurableExecutionState` APIs |  Lambda automatically retries the invocation with exponential backoff. The SDK replays from the last checkpoint. |  Error payload size + 1 operation per retry |   
|  Client error (4xx, except 429 and invalid token) when `CheckpointDurableExecution` / `GetDurableExecutionState` APIs |  The SDK marks the execution as FAILED. No automatic retry occurs because the error indicates a permanent issue. |  Error payload size |    

Backend retries use exponential backoff and continue until the function succeeds or the execution timeout is reached. During replay, the SDK skips completed checkpoints and continues execution from the last successful operation, ensuring your function doesn't re-execute completed work. 

## Retry best practices 

Follow these best practices when configuring retry strategies:  
Configure explicit retry strategies - Don't rely on default retry behavior in production. Configure explicit retry strategies with appropriate max attempts and backoff intervals for your use case. 
Use conditional retries - Implement `shouldRetry` logic to retry only transient errors (rate limits, timeouts) and fail fast on permanent errors (validation failures, not found). 
Set appropriate max attempts - Balance between resilience and execution time. Too many retries can delay failure detection, while too few can cause unnecessary failures. 
Use exponential backoff - Exponential backoff reduces load on downstream services and increases the likelihood of recovery from transient failures. 
Wrap error-prone code in steps - Code outside steps cannot be automatically retried. Wrap external API calls, database queries, and other error-prone operations in steps with retry strategies. 
Monitor retry metrics - Track step retry operations and execution failures in Amazon CloudWatch to identify patterns and optimize retry strategies.
