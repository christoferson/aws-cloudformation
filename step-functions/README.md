
## Step Functions


### Step Functions Basic

Example with a single step that invokes a lambda function

step-functions-basic.yaml


### Step Functions Demo

Example using various State types

- foo=3: Succeed State
- foo=4: Retry State

step-functions-demo

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

step-functions-express
