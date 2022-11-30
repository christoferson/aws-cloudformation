## Lambda Feature Updates

### 28 NOV 2022 - Lambda SnapStart 

**DESCRIPTION**
> After you enable Lambda SnapStart for a particular Lambda function, publishing a new version of the function will trigger an optimization process. The process launches your function and runs it through the entire Init phase. Then it takes an immutable, encrypted snapshot of the memory and disk state, and caches it for reuse. When the function is subsequently invoked, the state is retrieved from the cache in chunks on an as-needed basis and used to populate the execution environment. This optimization makes invocation time faster and more predictable, since creating a fresh execution environment no longer requires a dedicated Init phase.
[more](https://aws.amazon.com/jp/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart/)

**EXAMPLE SAM DEFINITION - Note New SnapStart Attribute**

```yaml
  PetStoreFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: com.amazonaws.serverless.sample.springboot2.StreamLambdaHandler::handleRequest
      Runtime: java11
      CodeUri: .
      MemorySize: 1512
      Policies: AWSLambdaBasicExecutionRole
      Timeout: 61
      SnapStart:
        ApplyOn: PublishedVersions
      Events:
        HttpApiEvent:
          Type: HttpApi
          Properties:
            TimeoutInMillis: 20000
            PayloadFormatVersion: '1.0'
```

**NOTES**

- Requires latest SAM CLI, version 1.66.0 for SNAPSTART



**TODO**

- [x] Test drive using Petstore
  
  Was not seeing improvement in performance. Still getting Init Time 6004.67 ms

>2022-11-30 16:20:56.790  INFO 8 --- [main] lambdainternal.AWSLambda : Started AWSLambda in 3.901 seconds (JVM running for 5.965)
  
![run duration](/assets/images/snap-lambda-duration.jpg)
  
- [ ] Retry test using Petstore
  

- [ ] Create project sample using java

- [ ] Create minimum cloudformation sample (lambda with Java runtime)
