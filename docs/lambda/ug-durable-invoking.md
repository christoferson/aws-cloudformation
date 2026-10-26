> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking.html
> Downloaded: 2026-10-25

# Invoking Lambda durable functions

Durable Lambda functions support the same invocation methods as other Lambda functions. You can invoke durable functions synchronously, asynchronously, or through event source mappings. The invocation process is identical to other functions, but durable functions provide additional capabilities for long-running executions and automatic state management. 

## Invocation methods 

Synchronous invocation: Invoke a durable function and wait for the response. Synchronous invocations are limited to 15 minutes, or less if the function timeout or execution timeout is lower. Use synchronous invocation when you need immediate results or when integrating with APIs and services that expect a response. You can use wait operations for efficient computation without disrupting the caller—the invocation waits for the entire durable execution to complete. For idempotent execution starts, use the execution name parameter as described in Idempotency. 

```

aws lambda invoke \
  --function-name my-durable-function:1 \
  --cli-binary-format raw-in-base64-out \
  --payload '{"orderId": "12345"}' \
  response.json
    
```
 

Asynchronous invocation: Queue an event for processing without waiting for a response. Lambda places the event in a queue and returns immediately. Asynchronous invocations support execution durations up to 1 year. Use asynchronous invocation for fire-and-forget scenarios or when processing can happen in the background. For idempotent execution starts, use the execution name parameter as described in Idempotency. 

```

aws lambda invoke \
  --function-name my-durable-function:1 \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"orderId": "12345"}' \
  response.json
    
```
 

Event source mappings: Configure Lambda to automatically invoke your durable function when records are available from stream or queue-based services like Amazon SQS, Kinesis, or DynamoDB. Event source mappings poll the event source and invoke your function with batches of records. For details about using event source mappings with durable functions, including execution duration limits, see Event source mappings with durable functions. 

For complete details about each invocation method, see synchronous invocation and asynchronous invocation. Note

Durable functions support dead-letter queues (DLQs) for error handling, but don't support Lambda destinations. Configure a DLQ to capture records from failed invocations. 

## Qualified ARNs requirement 

Durable functions require qualified identifiers for invocation. You must invoke durable functions using a version number, alias, or `$LATEST`. You can use either a full qualified ARN or a function name with version/alias suffix. You cannot use an unqualified identifier (without a version or alias suffix). 

Valid invocations: 

```

# Using full ARN with version number
arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1

# Using full ARN with alias
arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:prod

# Using full ARN with $LATEST
arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:$LATEST

# Using function name with version number
my-durable-function:1

# Using function name with alias
my-durable-function:prod
    
```
 

Invalid invocations: 

```

# Unqualified ARN (not allowed)
arn:aws:lambda:us-east-1:123456789012:function:my-durable-function

# Unqualified function name (not allowed)
my-durable-function
    
```
 

This requirement ensures that durable executions remain consistent throughout their lifecycle. When a durable execution starts, it's pinned to the function version that started it. If your function pauses and resumes hours or days later, Lambda invokes that same version, so publishing a new version affects only new executions. Similarly, when you update an alias, new executions use the new version, and in-progress executions continue on the version they started on. $LATEST executions can resume on updated code

Executions started with the `$LATEST` qualifier are not pinned to a fixed copy of your code. If you update your function code while an execution is paused, the execution resumes on the new code rather than the version that it started on.

Your code might no longer process the saved execution state in the same way, leading to non-determinism errors or silent failures. For more information about writing functions that replay safely, see Function versions and aliases. Best practice 

Use numbered versions or aliases for production durable functions rather than `$LATEST`. Numbered versions are immutable and support deterministic replay. Optionally, aliases provide a stable reference that you can update to point to new versions without changing invocation code. Use `$LATEST` only for prototyping or to shorten deployment times during development, because executions might not replay correctly if the code changes while they run. 

## Understanding execution lifecycle 

When you invoke a durable function, Lambda creates a durable execution that can span multiple function invocations:  
Initial invocation: Your invocation request creates a new durable execution. Lambda assigns a unique execution ID and starts processing. 
Execution and checkpointing: As your function executes durable operations, the SDK creates checkpoints that track progress. 
Suspension (if needed): If your function uses durable waits, such as `wait` or `waitForCallback`, or automatic step retries, Lambda suspends the execution and stops charging for compute time. 
Resumption: When it's time to resume (including after retries), Lambda invokes your function again. The SDK replays the checkpoint log and continues from where execution paused. 
Completion: When your function returns a final result or throws an unhandled error, the durable execution completes. 
 

For synchronous invocations, the caller waits for the entire durable execution to complete, including any wait operations. If the execution exceeds the invocation timeout (15 minutes or less), the invocation times out. For asynchronous invocations, Lambda returns immediately and the execution continues independently. Use the durable execution APIs to track execution status and retrieve final results. 

## Invoking from application code 

Use the AWS SDKs to invoke durable functions from your application code, with the same `Invoke` API you use for any Lambda function. Include a version number, alias, or `$LATEST` in the function name:  

**TypeScript** 

```

import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';

const client = new LambdaClient({});

// Synchronous invocation
const response = await client.send(new InvokeCommand({
  FunctionName: 'arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
  Payload: JSON.stringify({ orderId: '12345' })
}));

const result = JSON.parse(Buffer.from(response.Payload!).toString());

// Asynchronous invocation
await client.send(new InvokeCommand({
  FunctionName: 'arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
  InvocationType: 'Event',
  Payload: JSON.stringify({ orderId: '12345' })
}));
          
```
  

**Python** 

```

import boto3
import json

client = boto3.client('lambda')

# Synchronous invocation
response = client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
    Payload=json.dumps({'orderId': '12345'})
)

result = json.loads(response['Payload'].read())

# Asynchronous invocation
client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
    InvocationType='Event',
    Payload=json.dumps({'orderId': '12345'})
)
          
```
   

## Chained invocations 

Durable functions can invoke any Lambda function, including another durable function, using the `invoke` operation from `DurableContext`. This creates a chained invocation where the calling function suspends until the invoked function completes:  

**TypeScript** 

```

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    // Invoke another durable function and wait for result
    const result = await context.invoke(
      'process-order',
      'arn:aws:lambda:us-east-1:123456789012:function:order-processor:1',
      { orderId: event.orderId }
    );
    
    return { statusCode: 200, body: JSON.stringify(result) };
  }
);
          
```
  

**Python** 

```

@durable_execution
def handler(event, context: DurableContext):
    # Invoke another durable function and wait for result
    result = context.invoke(
        'arn:aws:lambda:us-east-1:123456789012:function:order-processor:1',
        {'orderId': event['orderId']},
        name='process-order'
    )
    
    return {'statusCode': 200, 'body': json.dumps(result)}
          
```
   

Chained invocations create a checkpoint in the calling function. If the calling function is interrupted, it resumes from the checkpoint with the invoked function's result, without re-invoking the function. Note

Cross-account chained invocations are not supported. The invoked function must be in the same AWS account as the calling function.
