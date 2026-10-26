> Source: https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html
> Downloaded: 2026-10-25

# ListDurableExecutionsByFunction

Returns a list of durable executions for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets. 

## Request Syntax 

```
GET /2025-12-01/functions/FunctionName/durable-executions?DurableExecutionName=DurableExecutionName&Marker=Marker&MaxItems=MaxItems&Qualifier=Qualifier&ReverseOrder=ReverseOrder&StartedAfter=StartedAfter&StartedBefore=StartedBefore&Statuses=Statuses HTTP/1.1

```
 

## URI Request Parameters 

The request uses the following URI parameters.   

**  DurableExecutionName  **  

Filter executions by name. Only executions with names that matches this string are returned. 

Length Constraints: Minimum length of 1. Maximum length of 64. 

Pattern: `[a-zA-Z0-9-_]+`   

**  FunctionName  **  

The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN. 

Length Constraints: Minimum length of 1. Maximum length of 256. 

Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`  

Required: Yes  

**  Marker  **  

Pagination token from a previous request to continue retrieving results.  

**  MaxItems  **  

Maximum number of executions to return (1-1000). Default is 100. 

Valid Range: Minimum value of 0. Maximum value of 1000.  

**  Qualifier  **  

The function version to filter executions by. If you don't specify a qualifier, this operation returns executions across all versions of the Lambda function. 

Length Constraints: Minimum length of 1. Maximum length of 128. 

Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`   

**  ReverseOrder  **  

Set to true to return results in chronological order (oldest first). Default is false.  

**  StartedAfter  **  

Filter executions that started after this timestamp (ISO 8601 format).  

**  StartedBefore  **  

Filter executions that started before this timestamp (ISO 8601 format).  

**  Statuses  **  

Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED. 

Array Members: Fixed number of 1 item. 

Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | STOPPED`    

## Request Body 

The request does not have a request body. 

## Response Syntax 

```
HTTP/1.1 200
Content-type: application/json

{
   "DurableExecutions": [ 
      { 
         "DurableExecutionArn": "string",
         "DurableExecutionName": "string",
         "EndTimestamp": number,
         "FunctionArn": "string",
         "KMSKeyArn": "string",
         "StartTimestamp": number,
         "Status": "string"
      }
   ],
   "NextMarker": "string"
}
```
 

## Response Elements 

If the action is successful, the service sends back an HTTP 200 response. 

The following data is returned in JSON format by the service.   

**  DurableExecutions  **  

List of durable execution summaries matching the filter criteria. 

Type: Array of Execution objects  

**  NextMarker  **  

Pagination token for retrieving additional results. Present only if there are more results available. 

Type: String   

## Errors 

For information about the errors that are common to all actions, see Common Error Types.   

**  InvalidParameterValueException  **  

One of the parameters in the request is not valid.   

**  message  **  

The exception message.  

**  Type  **  

The exception type.   

HTTP Status Code: 400  

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
