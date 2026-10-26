> Source: https://docs.aws.amazon.com/lambda/latest/api/API_SendDurableExecutionCallbackSuccess.html
> Downloaded: 2026-10-25

# SendDurableExecutionCallbackSuccess

Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation. 

## Request Syntax 

```
POST /2025-12-01/durable-execution-callbacks/CallbackId/succeed HTTP/1.1

Result
```
 

## URI Request Parameters 

The request uses the following URI parameters.   

**  CallbackId  **  

The unique identifier for the callback operation. 

Length Constraints: Minimum length of 1. Maximum length of 1024. 

Pattern: `[A-Za-z0-9+/]+={0,2}`  

Required: Yes   

## Request Body 

The request accepts the following binary data.   

**  Result  **  

The result data from the successful callback operation. Maximum size is 1 MB. 

Length Constraints: Minimum length of 0. Maximum length of 1048576.   

## Response Syntax 

```
HTTP/1.1 200

```
 

## Response Elements 

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body. 

## Errors 

For information about the errors that are common to all actions, see Common Error Types.   

**  CallbackTimeoutException  **  

The callback ID token has either expired or the callback associated with the token has already been closed.   

**  Type  **  

The exception type.   

HTTP Status Code: 400  

**  InvalidParameterValueException  **  

One of the parameters in the request is not valid.   

**  message  **  

The exception message.  

**  Type  **  

The exception type.   

HTTP Status Code: 400  

**  KMSAccessDeniedException  **  

Lambda couldn't decrypt the environment variables because AWS KMS access was denied. Check the Lambda function's KMS permissions. 

HTTP Status Code: 502  

**  KMSDisabledException  **  

Lambda couldn't decrypt the environment variables because the AWS KMS key used is disabled. Check the Lambda function's KMS key settings. 

HTTP Status Code: 502  

**  KMSInvalidStateException  **  

Lambda couldn't decrypt the environment variables because the state of the AWS KMS key used is not valid for Decrypt. Check the function's KMS key settings. 

HTTP Status Code: 502  

**  KMSNotFoundException  **  

Lambda couldn't decrypt the environment variables because the AWS KMS key was not found. Check the function's KMS key settings. 

HTTP Status Code: 502  

**  ResourceNotFoundException  **  

The resource specified in the request does not exist. 

HTTP Status Code: 404  

**  ServiceException  **  

The AWS Lambda service encountered an internal error. 

HTTP Status Code: 500  

**  TooManyRequestsException  **  

The request throughput limit was exceeded. For more information, see Lambda quotas.   

**  retryAfterSeconds  **  

The number of seconds the caller should wait before retrying.   

HTTP Status Code: 429   

## See Also 

For more information about using this API in one of the language-specific AWS SDKs, see the following:  
 AWS Command Line Interface V2  
 AWS SDK for .NET V4  
 AWS SDK for C++  
 AWS SDK for Go v2  
 AWS SDK for Java V2  
 AWS SDK for JavaScript V3  
 AWS SDK for Kotlin  
 AWS SDK for PHP V3  
 AWS SDK for Python (Boto3)  
 AWS SDK for Ruby V3
