
## Step Functions (Standard)


### Standard - Step Functions Basic

Example with a single step that invokes a lambda function

Input JSON:

```
{
  "foo": 1
}
```

[step-functions-std-basic](step-functions-std-basic.yaml)

### Standard - Step Functions Demo

Example using various State types

Input JSON:

```
TODO
```

- foo=3: Succeed State
- foo=4: Retry State

[step-functions-std-demo](step-functions-std-demo.yaml)

### Step Function Batch

Provision a StepFunction that calls Batch

Input JSON:

```
TODO
```

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

### Standard - Step Functions - Sequence of Lambda

Provision Step Function that calls several Lambda in sequence.

```
{
  "movies": [
    {
      "genre": "crime",
      "director": "Quentin Tarantino",
      "title": "Reservoir Dogs",
      "year": 1992
    },
    {
      "genre": "action",
      "director": "Brian De Palma",
      "title": "Mission: Impossible",
      "year": 1996,
      "staring": [
        "Tom Cruise"
      ]
    }
  ],
  "metadata": {
    "lastUpdated": "2020-05-27T08:00:00.000Z"
  },
  "stringJson": "{\"arr\": [1, 2, 3, 4, 5], \"bool\": true, \"null\": null, \"number\": 1}"
}
```

[step-functions-std-seq](step-functions-std-seq.yaml)

### Standard - Step Functions - XXX

[step-functions-std-task-choice](step-functions-std-task-choice.yaml)

----------

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

You can call AWS SDK services directly from the Amazon States Language in the Resource field of a task state. To do this, use the following syntax:

arn:aws:states:::aws-sdk:serviceName:apiAction.[serviceIntegrationPattern]

If an AWS SDK integration encounters an error, the resulting Error field will be composed of the service name and the error name, separated by a period character: ServiceName.ErrorName. Both the service name and error name are in Pascal case. You can also see the service name, in lowercase, in the Task state's Resource field.

[link](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html)

#### Step Functions Integration - Lambda

https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html
https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestParameters

##### Optimized Lambda integration

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

Parameters in Step Functions are expressed in PascalCase, even when the native service API is camelCase.

##### Lambda AWS SDK integration

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

- StateMachineExecutionRole-foo/bar is not authorized to perform: batch:TagResource on resource: arn:aws:batch:eu-west-1:9030984848:job-definition/BatchJobDefinition-foo

## References

- https://docs.aws.amazon.com/step-functions/latest/dg/service-integration-iam-templates.html
- https://docs.aws.amazon.com/step-functions/latest/dg/tutorials.html
- https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
- https://aws.amazon.com/about-aws/whats-new/2021/03/aws-step-functions-adds-tooling-support-for-yaml/?nc1=h_ls
- https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html



### TODO

- ContainerOverrides, Batch, Env Vars