> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking-esm.html
> Downloaded: 2026-10-25

# Event source mappings with durable functions

Durable functions work with all Lambda event source mappings. Configure event source mappings for durable functions the same way you configure them for other functions. Event source mappings automatically poll event sources like Amazon SQS, Kinesis, and DynamoDB Streams, and invoke your function with batches of records.

Event source mappings are useful for durable functions that process streams or queues with complex, multi-step workflows. For example, you can create a durable function that processes Amazon SQS messages with retries, external API calls, and human approvals. 

## How event source mappings invoke durable functions 

Event source mappings invoke durable functions synchronously, waiting for the complete durable execution to finish before processing the next batch or marking records as processed. If the total durable execution time exceeds the applicable timeout limit (15 minutes by default, or up to 90 minutes for functions running on Lambda Managed Instances), the execution times out and fails. The event source mapping receives a timeout exception and handles it according to its retry configuration. 

## Execution duration limit 

When durable functions are invoked by event source mappings, the total durable execution duration cannot exceed the maximum function timeout: 15 minutes for functions running on the default (on-demand) capacity mode, or up to 90 minutes for functions running on Lambda Managed Instances (except Amazon MQ and Amazon DocumentDB event source mappings, which remain limited to 15 minutes). This limit applies to the entire durable execution from start to completion, not just individual function invocations. 

The function timeout limits each invocation. The durable execution timeout limits the total time from execution start to completion. With event source mappings, both have the same maximum: 15 minutes by default, or 90 minutes on Lambda Managed Instances. 

Example scenarios:  
Valid (any capacity mode): A durable function processes an Amazon SQS message with three steps, each taking 2 minutes, then waits 5 minutes before completing a final step. Total execution time: 11 minutes. This works on both capacity modes because it is under the 15-minute default limit. 
Valid on Lambda Managed Instances only: A durable function processes an Amazon SQS message, completes initial processing in 2 minutes, then waits 20 minutes for an external callback before completing. Total execution time: 22 minutes. This exceeds the 15-minute default limit, but is within the 90-minute limit for functions running on Lambda Managed Instances. 
Invalid (any capacity mode): A durable function processes a Kinesis record with multiple wait operations totaling two hours between steps. This exceeds even the 90-minute Lambda Managed Instances limit, so the execution fails regardless of capacity mode. Use the intermediary function pattern for workflows this long. 
 Important

Configure your durable execution timeout within the applicable limit when using event source mappings, or creation of the event source mapping fails. The limit is 15 minutes by default, or up to 90 minutes on Lambda Managed Instances. If your workflow requires longer execution times, use the intermediary function pattern described below. 

## Configuring event source mappings 

Configure event source mappings for durable functions using the Lambda console, AWS CLI, or AWS SDKs. All event source mapping properties, such as batch size and batching window, apply to durable functions: 

```

aws lambda create-event-source-mapping \
  --function-name arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1 \
  --event-source-arn arn:aws:sqs:us-east-1:123456789012:my-queue \
  --batch-size 10 \
  --maximum-batching-window-in-seconds 5
    
```
 

Use a qualified ARN with a version number, alias, or `$LATEST` when you configure an event source mapping for a durable function. 

## Error handling with event source mappings 

Event source mappings provide built-in error handling that works with durable functions:  
Retry behavior: If the initial invocation fails, the event source mapping retries according to its retry configuration. Configure maximum retry attempts and retry intervals based on your requirements. 
Dead-letter queues: Configure a dead-letter queue to capture records that fail after all retries. This prevents message loss and enables manual inspection of failed records. 
Partial batch failures: For Amazon SQS and Kinesis, use partial batch failure reporting to process records individually and only retry failed records. 
Bisect on error: For Kinesis and DynamoDB Streams, enable bisect on error to split failed batches and isolate problematic records. 
 Note

Durable functions support dead-letter queues (DLQs) for error handling, but don't support Lambda destinations. Configure a DLQ to capture records from failed invocations. 

For complete information about event source mapping error handling, see event source mappings. 

## Using an intermediary function for long-running workflows 

If your workflow requires more than the applicable event source mapping limit (15 minutes by default, or 90 minutes on Lambda Managed Instances), use an intermediary standard Lambda function between the event source mapping and your durable function. The intermediary function receives events from the event source mapping and invokes the durable function asynchronously, removing the execution-duration limit. 

This pattern decouples the event source mapping's synchronous invocation model from the durable function's long-running execution model. The event source mapping invokes the intermediary function, which quickly returns after starting the durable execution. The durable function then runs independently for as long as needed (up to 1 year). 

### Architecture 

The intermediary function pattern uses three components:  
Event source mapping: Polls the event source (Amazon SQS, Kinesis, DynamoDB Streams) and invokes the intermediary function synchronously with batches of records. 
Intermediary function: A Lambda function without durable execution that receives events from the event source mapping, validates and transforms the data if needed, and invokes the durable function asynchronously. This function completes quickly (typically under 1 second) and returns control to the event source mapping. 
Durable function: Processes the event with complex, multi-step logic that can run for extended periods. Invoked asynchronously, so it's not constrained by the event source mapping execution-duration limit. 
 

### Implementation 

The intermediary function receives the entire event from the event source mapping and invokes the durable function asynchronously. Use the execution name parameter to ensure idempotent execution starts, preventing duplicate processing if the event source mapping retries:  

**TypeScript** 

```

import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';
import { SQSEvent } from 'aws-lambda';
import { createHash } from 'crypto';

const lambda = new LambdaClient({});

export const handler = async (event: SQSEvent) => {
  // Invoke durable function asynchronously with execution name
  await lambda.send(new InvokeCommand({
    FunctionName: 'arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
    InvocationType: 'Event',
    Payload: JSON.stringify({
      executionName: event.Name,
      event: event
    })
  }));
  
  return { statusCode: 200 };
};
            
```
  

**Python** 

```

import boto3
import json
import hashlib

lambda_client = boto3.client('lambda')

def handler(event, context):  
    # Invoke durable function asynchronously with execution name
    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:123456789012:function:my-durable-function:1',
        InvocationType='Event',
        Payload=json.dumps({
            'executionName': execution_name,
            'event': event["name"]
        })
    )
    
    return {'statusCode': 200}
            
```
   

For idempotency in the intermediary function itself, use Powertools for AWS Lambda to prevent duplicate invocations of the durable function if the event source mapping retries the intermediary function. 

The durable function receives the payload with the execution name and processes all records with long-running logic:  

**TypeScript** 

```

import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (payload: any, context: DurableContext) => {
    const sqsEvent = payload.event;
    
    // Process each record with complex, multi-step logic
    const results = await context.map(
      sqsEvent.Records,
      async (ctx, record) => {
        const validated = await ctx.step('validate', async () => {
          return validateOrder(JSON.parse(record.body));
        });
        
        // Wait for external approval (could take hours or days)
        const approval = await ctx.waitForCallback(
          'approval',
          async (callbackId) => {
            await requestApproval(callbackId, validated);
          },
          { timeout: { hours: 48 } }
        );
        
        // Complete processing
        return await ctx.step('complete', async () => {
          return completeOrder(validated, approval);
        });
      }
    );
    
    return { statusCode: 200, processed: results.getResults().length };
  }
);
            
```
  

**Python** 

```

from aws_durable_execution_sdk_python import durable_execution, DurableContext
from aws_durable_execution_sdk_python.config import Duration, WaitForCallbackConfig
from collections.abc import Sequence
import json

def validate_order(order_data: dict) -> dict:
    """Validate order data - always passes."""
    return order_data

def request_approval(callback_id: str, validated_order: dict) -> None:
    """Request approval for the order - always passes."""
    pass

def complete_order(validated_order: dict, approval_result: str) -> dict:
    """Complete the order processing - always passes."""
    return validated_order

@durable_execution
def lambda_handler(payload, context: DurableContext):
    sqs_event = payload['event']

    def process_record(
        ctx: DurableContext, 
        record: dict, 
        index: int, 
        items: Sequence[dict]
    ) -> dict:
        validated = ctx.step(
            lambda _: validate_order(json.loads(record['body'])),
            name=f'validate-{index}'
        )

        approval = ctx.wait_for_callback(
            submitter=lambda callback_id, wait_ctx: request_approval(callback_id, validated),
            name=f'approval-{index}',
            config=WaitForCallbackConfig(timeout=Duration.from_seconds(172800))
        )

        return ctx.step(
            lambda _: complete_order(validated, approval),
            name=f'complete-{index}'
        )

    results = context.map(
        inputs=sqs_event['Records'],
        func=process_record,
        name='process-records'
    )

    return {
        'statusCode': 200, 
        'started': results.started_count,
        'completed': results.success_count,
        'failed': results.failure_count,
        'total': results.total_count
    }
            
```
   

### Key considerations 

This pattern removes the event source mapping execution-duration limit by decoupling the event source mapping from the durable execution. The intermediary function returns immediately after starting the durable execution, allowing the event source mapping to continue processing. The durable function then runs independently for as long as needed. 

The intermediary function succeeds when it invokes the durable function, not when the durable execution completes. If the durable execution fails later, the event source mapping won't retry because it already processed the batch successfully. Implement error handling in the durable function and configure dead-letter queues for failed executions. 

Use the execution name parameter to ensure idempotent execution starts. If the event source mapping retries the intermediary function, the durable function won't start a duplicate execution because the execution name already exists. 

## Supported event sources 

Durable functions support all Lambda event sources that use event source mappings:  
Amazon SQS queues (standard and FIFO)
Kinesis streams
DynamoDB Streams
Amazon Managed Streaming for Apache Kafka (Amazon MSK)
Self-managed Apache Kafka
Amazon MQ (ActiveMQ and RabbitMQ)
Amazon DocumentDB change streams
 

All event source types are subject to the durable execution limit described earlier (15 minutes by default) when invoking durable functions. On Lambda Managed Instances, the limit increases to 90 minutes for these event sources, except Amazon MQ and Amazon DocumentDB, which remain limited to 15 minutes.
