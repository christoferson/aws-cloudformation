## API Gateway - HTTP

### API Gateway - Integration Types

- AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. 
- AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action.
    - This is the preferred integration type to call a Lambda function through API Gateway and is not applicable to any other AWS service actions, including Lambda actions other than the function-invoking action. 
- HTTP: for integrating the route or method request with an HTTP endpoint.
- HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. 
- MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend.

### API Gateway - Account Settings

Account Settings e.g. IAM role that Amazon API Gateway uses to write API logs to Amazon CloudWatch Logs.

[api-gateway-account](api-gateway-account.yaml)

### API Gateway - Quick Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda using Quick Create

[api-gateway-http-quick](api-gateway-http-quick.yaml)

### API Gateway - Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda.

[api-gateway-http](api-gateway-http.yaml)

### API Gateway - Integrate with Lambda

Provision HTTP API that integrates with newly provisioned Lambda.

[api-gateway-http-lambda](api-gateway-http-lambda.yaml)

### API Gateway - Integrate with Lambda Alias

Provision HTTP API that integrates with newly provisioned Lambda and Alias.

[api-gateway-http-lambda-alias](api-gateway-http-lambda-alias.yaml)

### API Gateway - Integrate with existing Lambda - Multiple Stages

Provision HTTP API that integrates with specified Lambda.
Exposes 2 stages staging and production.

[api-gateway-http-staged](api-gateway-http-staged.yaml)

### API Gateway - Integrate with existing Lambda - Authorizer Cognito

Provision HTTP API that integrates with specified Lambda.
Secured by Authorizer using Cognito, requires JWT token.

[api-gateway-http-authorizer-cognito](api-gateway-http-authorizer-cognito.yaml)

### API Gateway - Integrate with existing Lambda - Authorizer Lambda

Provision HTTP API that integrates with specified Lambda.
Secured by Lambda Authorizer. Uses Payload format version 2.0.
1.0 uses authorizationToken and methodArn
2.0 uses identitySource and routeArn

[api-gateway-http-authorizer-lambda](api-gateway-http-authorizer-lambda.yaml)

### API Gateway - Integrate with SQS Standard Queue

Provision HTTP API that integrates with newly provisioned SQS Standard Queue.

Send HTTP Post to API Gateway

```
curl -X POST "https://ddd.execute-api.eu-west-1.amazonaws.com/stg/demo" -d "name=linuxize"
```

- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html

[api-gateway-http-sqs](api-gateway-http-sqs.yaml)


## API Gateway - REST - Basic

Provision REST API that integrates with specified Lambda.

[api-gateway-rest-basic](api-gateway-rest-basic.yaml)

## API Gateway - REST - UsagePlan

Provision REST API that integrates with specified Lambda.
Also provisions UsagePlan and ApiKeys

[api-gateway-rest-usageplan](api-gateway-rest-usageplan.yaml)

## API Gateway - REST

Provision REST API that integrates with specified Lambda.
Also provisions UsagePlan and ApiKeys

[api-gateway-rest](api-gateway-rest.yaml)

curl -X POST https://zzz.execute-api.<region>.amazonaws.com/stg/demo -H "x-api-key: <api-key>"

## API Gateway - WebSocket

RouteSelectionExpression
In your WebSocket API, incoming JSON messages are directed to backend integrations based on routes that you configure. 
(Non-JSON messages are directed to a $default route that you configure.)


## API Gateway - WebSocket - Mock

Provision WebSocket Endpoint with Mock Backends.

wscat -c wss://zzz.execute-api.eu-west-1.amazonaws.com/LATEST
- Log: /aws/apigateway/zzz/LATEST
> {"action":"message", "data":"foobar", "message": "list"}  

[api-gateway-websocket-mock](api-gateway-websocket-mock.yaml)

## API Gateway - WebSocket - Lambda

Provision WebSocket Endpoint with Lambda Backends. State Managed in DynamoDB.

wscat -c wss://zzz.execute-api.eu-west-1.amazonaws.com/LATEST
> {"action":"message", "data":"foobar"} 
> {"action":"list", "data":"foobar"}  

[api-gateway-websocket-lambda](api-gateway-websocket-lambda.yaml)
[api-gateway-websocket-lambda-api](api-gateway-websocket-lambda-api.yaml)

## Resources

- [Cloudformation API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
- [Cloudformation REST API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html)
- [JWT Authorizer] (https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)
- [Lambda Authorizer] (https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html)
- [API Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html)

## Errors

- Internal Server Error if no permission to Invoke Lambda
- CloudWatch Logs role ARN must be set in account settings to enable logging
- Currently, an API with a protocol type of HTTP may only be associated with proxy integrations (AWS_PROXY, HTTP_PROXY) 