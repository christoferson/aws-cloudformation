

### LogGroup

  LambdaLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub "/aws/lambda/${LambdaFunction}"
      RetentionInDays: 1
      
### Enable Xray

 ```
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
        - arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess
 ```
     
 ```
   LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName : "basic-lambda"
      Description: "Basic Lambda"
      ...
      TracingConfig:
        Mode: "Active" 
```       