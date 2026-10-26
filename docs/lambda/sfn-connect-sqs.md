> Source: https://docs.aws.amazon.com/step-functions/latest/dg/connect-sqs.html
> Downloaded: 2026-10-25

# Send messages to an Amazon SQS queue with Step Functions

You can to send messages to an Amazon SQS queue using the following Amazon SQS API actions and example `Task` state code for Step Functions workflows.

To learn about integrating with AWS services in Step Functions, see Integrating services and Passing parameters to a service API in Step Functions.

To learn more about receiving messages in Amazon SQS, see Receive and Delete Your Message in the Amazon Simple Queue Service Developer Guide.

The following sample includes a `Task` state (JSONata) that sends an Amazon Simple Queue Service (Amazon SQS) message with optional MessageAttributes:

```
{
 "StartAt": "Send to SQS",
 "States": {
   "Send to SQS": {
     "Type": "Task",
     "Resource": "arn:aws:states:::sqs:sendMessage",
     "Arguments": {
       "QueueUrl": "https://sqs.us-east-1.amazonaws.com/account-id/myQueue",
       "MessageBody": "{% $states.input.message %}",
       "MessageAttributes": {
         "my_attribute_no_1": {
           "DataType": "String",
           "StringValue": "attribute1"
         },
         "my_attribute_no_2": {
           "DataType": "String",
           "StringValue": "attribute2"
         }
       }
     },
     "End": true
    }
  }
}
```

The following state machine includes a `Task` state that publishes to an Amazon SQS queue, and then waits for the task token to be returned. See Wait for a Callback with Task Token.

```
{  
   "StartAt":"Send message to SQS",
   "States":{  
      "Send message to SQS":{  
         "Type":"Task",
         "Resource":"arn:aws:states:::sqs:sendMessage.waitForTaskToken",
         "Arguments":{  
            "QueueUrl":"https://sqs.us-east-1.amazonaws.com/account-id/myQueue",
            "MessageBody":{  
               "Input" : "{% $states.input.message %}",
               "MyTaskToken" : "{% $states.context.Task.Token %}"
            }
         },
         "End":true
      }
   }
}
```
 

## Optimized Amazon SQS APIs  
`SendMessage` 
 Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`. Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See Quotas related to state machine executions. 

## IAM policies for calling Amazon SQS 

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see How Step Functions generates IAM policies for integrated services and Discover service integration patterns in Step Functions. 

Static resources   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage"
            ],
            "Resource": [
                "arn:aws:sqs:us-east-1:123456789012:myQueueName"
            ]
        }
    ]
}
        

```
   

Dynamic resources   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage"
            ],
            "Resource": "*"
        }
    ]
}

```
