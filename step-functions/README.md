
## Step Functions (Standard)


### Step Functions Basic

Example with a single step that invokes a lambda function

Input JSON:

```
{
  "foo": 1
}
```

[step-functions-std-basic](step-functions-std-basic.yaml)

### Step Functions Demo

Example using various State types

- foo=3: Succeed State
- foo=4: Retry State

[step-functions-std-demo](step-functions-std-demo.yaml)

### Step Function Batch

Provision a StepFunction that calls Batch

Use ContainerOverrides to pass parameters to the Batch process. [link](https://docs.aws.amazon.com/ja_jp/batch/latest/APIReference/API_ContainerOverrides.html)

```
"States": {
  "Submit Batch Job": {
    "Type": "Task",
    "Resource": "arn:aws:states:::batch:submitJob.sync",
    "Parameters": {
      "JobName": "${BATCH_JOB_NAME}",
      "JobQueue": "${BATCH_JOB_QUEUE_NAME}",
      "JobDefinition": "${BATCH_JOB_DEFINITION_NAME}",
      "ContainerOverrides": {
        "Command.$": "States.Array('sh', '-c', States.Format('echo s3rocksv2 && java -jar batch.jar {}', $.detail.object.key))"
      }
    }
```

[step-functions-std-batch](step-functions-std-batch.yaml)

## Step Functions (Express)

### Step Functions Type=Express

Example of Express Step Functions

```yaml
  StateMachine:
    Type: "AWS::StepFunctions::StateMachine"
    Properties:
      ...
      StateMachineType: EXPRESS  # STANDARD |  EXPRESS 
      ...
```

[step-functions-express](step-functions-express.yaml)

### Step Functions Integration

#### Step Functions Integration - Lambda

https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html

Optimized Lambda integration

```
{  
   "StartAt":"CallLambda",
   "States":{  
      "CallLambda":{  
         "Type":"Task",
         "Resource":"arn:aws:states:::lambda:invoke",
         "Parameters":{  
            "FunctionName":"MyFunction"
         },
         "End":true
      }
   }
}
```

Lambda AWS SDK integration

```
{  
   "StartAt":"CallFunction",
   "States":{  
      "CallFunction": {  
         "Type":"Task",
         "Resource":"arn:aws:lambda:us-east-1:123456789012:function:HelloFunction",
         "End": true
      }
   }
}     
```

## Errors
- StateMachineExecutionRole-1K0YP4X5NK8ON' is not authorized to create managed-rule. (Service: AWSStepFunctions; Status Code: 400; Error Code: AccessDeniedException;

```yaml
              - Effect: Allow
                Action:
                  - 'events:PutTargets'
                  - 'events:PutRule'
                  - 'events:DescribeRule'
                Resource: !Sub "arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/StepFunctionsGetEventsForBatchJobsRule"
```

## References

- https://docs.aws.amazon.com/step-functions/latest/dg/service-integration-iam-templates.html
- https://docs.aws.amazon.com/step-functions/latest/dg/tutorials.html
- https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
- https://aws.amazon.com/about-aws/whats-new/2021/03/aws-step-functions-adds-tooling-support-for-yaml/?nc1=h_ls
- https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html



### TODO

- ContainerOverrides, Batch, Env Vars