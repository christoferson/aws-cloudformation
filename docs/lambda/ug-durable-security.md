> Source: https://docs.aws.amazon.com/lambda/latest/dg/durable-security.html
> Downloaded: 2026-10-25

# Security and permissions for Lambda durable functions

AWS Lambda durable functions require specific IAM permissions to run and manage durable executions. Follow the principle of least privilege by granting only the permissions each principal needs. 

## IAM permissions for durable functions 

For most durable execution API actions, Lambda authorizes the request against the durable execution ARN, not the function ARN. A durable execution is a sub-resource of a function version, and its ARN extends the function ARN: 

`arn:aws:lambda:`region`:`account-id`:function:`function-name`:`qualifier`/durable-execution/`execution-name`/`execution-id`` 

The qualifier in a durable execution ARN is always `$LATEST` or a version number. 

If your policy specifies an unqualified function ARN in the Resource element, Lambda denies the request because an unqualified ARN never matches a durable execution ARN. To grant access, append a qualifier pattern to the function ARN:  
`arn:aws:lambda:us-east-1:123456789012:function:my-function:*` – Matches durable executions of every version.
`arn:aws:lambda:us-east-1:123456789012:function:my-function:1/durable-execution/*` – Matches durable executions of version 1 only.
 

Most policies use the `:*` form because version numbers can change with each deployment. Aliases do not apply to durable execution permissions

You can invoke a durable function through an alias, but the resulting execution's ARN contains the resolved version number. 

### Execution role permissions 

Your durable function's execution role must have permissions to create checkpoints and retrieve execution state. The following policy shows the minimum required permissions: 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CheckpointDurableExecution",
                "lambda:GetDurableExecutionState"
            ],
            "Resource": "arn:aws:lambda:region:account-id:function:function-name:*"
        }
    ]
}
```
 

When you create a durable function using the console, Lambda automatically adds these permissions to the execution role. If you create the function using the AWS CLI or AWS CloudFormation, add these permissions to your execution role. 

For Lambda to assume your execution role, the role's trust policy must specify the Lambda service principal (`lambda.amazonaws.com`) as a trusted service. The following example shows a trust policy that grants Lambda permission to assume the role. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
 Least privilege principle 

Scope the `Resource` element to specific function ARNs instead of using wildcards. This limits the execution role to checkpoint operations for only the functions that need them. Example Scoped permissions for multiple functions

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CheckpointDurableExecution",
                "lambda:GetDurableExecutionState"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:function:orderProcessor:*",
                "arn:aws:lambda:us-east-1:123456789012:function:paymentHandler:*"
            ]
        }
    ]
}
```
 

Alternatively, you can use the AWS managed policy `AWSLambdaBasicDurableExecutionRolePolicy` which includes the required durable execution permissions along with basic Lambda execution permissions for Amazon CloudWatch Logs. 

### Permissions for managing durable executions 

Lambda authorizes the `lambda:GetDurableExecution`, `lambda:GetDurableExecutionHistory`, and `lambda:StopDurableExecution` actions against the durable execution ARN. 

To list the durable executions of a function, use `lambda:ListDurableExecutionsByFunction`. Lambda authorizes this action against the function ARN from the request. The following rules apply to ARN matching:  
A policy that grants the unqualified function ARN matches only requests that use the unqualified function name.
A policy that grants a qualified ARN matches only requests that use a qualified function name.
 

For more information, see Referencing functions in the Resource section of policies. 

To match requests made with either form of the function name, include both the unqualified and the qualified function ARN, as the following policy shows: 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ManageDurableExecutions",
            "Effect": "Allow",
            "Action": [
                "lambda:GetDurableExecution",
                "lambda:GetDurableExecutionHistory",
                "lambda:StopDurableExecution"
            ],
            "Resource": "arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:*"
        },
        {
            "Sid": "ListDurableExecutions",
            "Effect": "Allow",
            "Action": "lambda:ListDurableExecutionsByFunction",
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction",
                "arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:*"
            ]
        }
    ]
}
```
 

### Permissions for sending callbacks 

The external system that sends a callback result uses the `lambda:SendDurableExecutionCallbackSuccess`, `lambda:SendDurableExecutionCallbackFailure`, and `lambda:SendDurableExecutionCallbackHeartbeat` actions. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SendCallbacks",
            "Effect": "Allow",
            "Action": [
                "lambda:SendDurableExecutionCallbackSuccess",
                "lambda:SendDurableExecutionCallbackFailure",
                "lambda:SendDurableExecutionCallbackHeartbeat"
            ],
            "Resource": "arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:*"
        }
    ]
}
```
 

Lambda authorizes callback requests against the ARN of the durable execution that created the callback. 

## State encryption 

Lambda durable functions encrypt execution data at rest. Each function execution maintains isolated state that other executions cannot access. You can configure a customer managed key to encrypt durable execution data. For more information, see Encrypting AWS Lambda durable execution data. 

Checkpoint data includes:  
Step results and errors
Chained invoke inputs
 

For the complete list of durable execution data encrypted at rest, see What is encrypted. 

All data is encrypted in transit using TLS when Lambda reads or writes checkpoint data. 

### Custom encryption with custom serializers and deserializers 

For critical security requirements, you can implement your own encryption and decryption mechanism using custom serializers and deserializers (SerDer) using durable SDK. This approach gives you full control over the encryption keys and algorithms used to protect checkpoint data. Important

When you use custom encryption, you lose visibility of operation results in the Lambda console and API responses. Checkpoint data appears encrypted in execution history and cannot be inspected without decryption. 

Your function's execution role needs `kms:Encrypt` and `kms:Decrypt` permissions for the AWS KMS key used in the custom SerDer implementation. 

## CloudTrail logging 

Lambda logs checkpoint operations as data events in AWS CloudTrail. You can use CloudTrail to audit when checkpoints are created, track execution state changes, and monitor access to durable execution data. 

Checkpoint operations appear in CloudTrail logs with the following event names:  
`CheckpointDurableExecution` - Logged when a step completes and creates a checkpoint
`GetDurableExecutionState` - Logged when Lambda retrieves execution state during replay
 

To enable data event logging for durable functions, configure a CloudTrail trail to log Lambda data events. For more information, see Logging data events in the CloudTrail User Guide. 

Example: CloudTrail log entry for checkpoint operation 

```
{
    "eventVersion": "1.08",
    "eventTime": "2024-11-16T10:30:45Z",
    "eventName": "CheckpointDurableExecution",
    "eventSource": "lambda.amazonaws.com",
    "requestParameters": {
        "functionName": "myDurableFunction",
        "executionId": "exec-abc123",
        "stepId": "step-1"
    },
    "responseElements": null,
    "eventType": "AwsApiCall"
}
```
 

## Cross-account considerations 

If you invoke durable functions across AWS accounts, the calling account needs `lambda:InvokeFunction` permission, but checkpoint operations always use the execution role in the function's account. The calling account cannot access checkpoint data or execution state directly. 

This isolation ensures that checkpoint data remains secure within the function's account, even when invoked from external accounts. 

## Inherited Lambda security features 

Durable functions inherit all security, governance, and compliance features from Lambda. These include VPC connectivity, environment variable encryption, dead letter queues, reserved concurrency, function URLs, code signing, and compliance certifications such as SOC, PCI DSS, and HIPAA. 

For detailed information about Lambda security features, see Security in AWS Lambda in the Lambda Developer Guide. The only additional security considerations for durable functions are the IAM permissions documented in this guide.
