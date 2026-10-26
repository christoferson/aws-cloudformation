> Source: https://docs.aws.amazon.com/step-functions/latest/dg/connect-ddb.html
> Downloaded: 2026-10-25

# Perform DynamoDB CRUD operations with Step Functions

You can integrate Step Functions with DynamoDB to perform CRUD operations on a DynamoDB table. This page lists the supported DynamoDB APIs and provides an example `Task` state to retrieve an item from DynamoDB.

To learn about integrating with AWS services in Step Functions, see Integrating services and Passing parameters to a service API in Step Functions.Key features of optimized DynamoDB integration 
There is no specific optimization for the Request Response integration pattern. 
Wait for a Callback with Task Token integration pattern is not supported. 
Only `GetItem`, `PutItem`, `UpdateItem`, and `DeleteItem` API actions are available through optimized integration. Other API actions, such as `CreateTable` are available using the DynamoDB AWS SDK integration.  

The following is an example `Task` state that retrieves a message from DynamoDB.

```
"Read next Message from DynamoDB": {
    "Type": "Task",
    "Resource": "arn:aws:states:::dynamodb:getItem",
    "Arguments": {
        "TableName": "DYNAMO_DB_TABLE_NAME",
        "Key": {
            "MessageId": {"S": "{% $List[0] %}"}
        }
    }
```

To see this state in a working example, see the Transfer data records with Lambda, DynamoDB, and Amazon SQS starter template.Exception prefix differences

When standard DynamoDB connections experience an error, the exception prefix will be `DynamoDb` (mixed case).

For optimized integrations, the exception prefix will be `DynamoDB` (uppercase `DB`). Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See Quotas related to state machine executions. 

## Optimized DynamoDB APIs  
`GetItem` 
`PutItem` 
`DeleteItem` 
`UpdateItem` 
 Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`. 

## IAM policies for calling DynamoDB 

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
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-east-1:123456789012:table/myTableName"
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
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": "*"
        }
    ]
}

```
   

For more information about the IAM policies for all DynamoDB API actions, see IAM policies with DynamoDB in the Amazon DynamoDB Developer Guide. Additionally, for information about the IAM policies for PartiQL for DynamoDB, see IAM policies with PartiQL for DynamoDB in the Amazon DynamoDB Developer Guide.
