
## Step Functions (Standard)


### Step Functions Basic

Example with a single step that invokes a lambda function

[step-functions-std-basic](step-functions-std-basic.yaml)

### Step Functions Demo

Example using various State types

- foo=3: Succeed State
- foo=4: Retry State

[step-functions-std-demo](step-functions-std-demo.yaml)

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



## Errors
- StateMachineExecutionRole-1K0YP4X5NK8ON' is not authorized to create managed-rule. (Service: AWSStepFunctions; Status Code: 400; Error Code: AccessDeniedException;
```yaml
              - Effect: Allow
                Action:
                  - 'events:PutTargets'
                  - 'events:PutRule'
                  - 'events:DescribeRule'
                Resource: !Sub "arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/StepFunctionsGetEventsForBatchJobsRule"
                
## References

- https://docs.aws.amazon.com/step-functions/latest/dg/service-integration-iam-templates.html
- https://docs.aws.amazon.com/step-functions/latest/dg/tutorials.html

```