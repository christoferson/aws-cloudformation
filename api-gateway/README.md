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

### API Gateway - HTTP - Quick Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda using Quick Create

Quick Integrate uses the Target and RouteKey property of the Api resource. [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)

> **Target:** This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.

> **RouteKey:** This property is part of quick create. If you don't specify a routeKey, a default route of $default is created. The $default route acts as a catch-all for any request made to your API, for a particular stage. The $default route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.

[api-gateway-http-quick](api-gateway-http-quick.yaml)

### API Gateway - HTTP - Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda.

[api-gateway-http](api-gateway-http.yaml)

### API Gateway - HTTP - Integrate with Lambda

Provision HTTP API that integrates with newly provisioned Lambda.

AWS::Lambda::Function

[api-gateway-http-lambda](api-gateway-http-lambda.yaml)

### API Gateway - HTTP - Integrate with Lambda Alias

Provision HTTP API that integrates with newly provisioned Lambda and Alias.

AWS::Lambda::Function
AWS::Lambda::Version
AWS::Lambda::Alias

[api-gateway-http-lambda-alias](api-gateway-http-lambda-alias.yaml)

### API Gateway - HTTP - Integrate with existing Lambda - Multiple Stages

Provision HTTP API that integrates with specified Lambda.
Exposes 2 stages staging and production.

[api-gateway-http-staged](api-gateway-http-staged.yaml)

### API Gateway - HTTP - Integrate with existing Lambda - Authorizer Cognito

Provision HTTP API that integrates with specified Lambda.
Secured by Authorizer using Cognito, requires JWT token.

[api-gateway-http-authorizer-cognito](api-gateway-http-authorizer-cognito.yaml)

### API Gateway - HTTP - Integrate with existing Lambda - Authorizer Lambda

Provision HTTP API that integrates with specified Lambda.
Secured by Lambda Authorizer. Uses Payload format version 2.0.
1.0 uses authorizationToken and methodArn
2.0 uses identitySource and routeArn

[api-gateway-http-authorizer-lambda](api-gateway-http-authorizer-lambda.yaml)

### API Gateway - HTTP - Integrate with SQS Standard Queue

Provision HTTP API that integrates with newly provisioned SQS Standard Queue.

Send HTTP Post to API Gateway

```
curl -X POST "https://ddd.execute-api.eu-west-1.amazonaws.com/stg/demo" -d "name=linuxize"
```

- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html

[api-gateway-http-sqs](api-gateway-http-sqs.yaml)

## API Gateway - REST

### CORS

```
  const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify(message),
  };
```

## API Gateway - REST - Basic

Provision REST API that integrates with specified Lambda.

Execution Logs

```
  ApiGatewayStage:
    Type: "AWS::ApiGateway::Stage"
    Properties:
      StageName: "stg"
      ...
      MethodSettings:
        - LoggingLevel: "ERROR"
          ResourcePath: "/*"
          HttpMethod: "*"
```

Invoke: curl -X POST https://rest-id.execute-api.region.amazonaws.com/stg/demo

[api-gateway-rest-basic](api-gateway-rest-basic.yaml)

## API Gateway - REST - UsagePlan

Provision REST API that integrates with specified Lambda. Access is controlled by UsagePlan and ApiKeys.

- AWS::ApiGateway::ApiKey

- AWS::ApiGateway::UsagePlan

- AWS::ApiGateway::UsagePlanKey

Invoke: curl -X POST --header "x-api-key:xxx" https://rest-id.execute-api.region.amazonaws.com/stg/demo

[api-gateway-rest-usageplan](api-gateway-rest-usageplan.yaml)

## API Gateway - REST - Cache

Provision REST API that integrates with specified Lambda. Cache is enabled on the Api Stage for GET requests.

```
  ApiGatewayStage:
    Type: "AWS::ApiGateway::Stage"
    Properties:
      StageName: "stg"
      ...
      MethodSettings:
        - HttpMethod: "*"
          ResourcePath: "/*"
          ...
        - HttpMethod: "GET"
          ResourcePath: "/"
          CachingEnabled: true
          CacheTtlInSeconds: 600
```

[api-gateway-rest-cache](api-gateway-rest-cache.yaml)

### API Gateway - REST - Validation

```
  ApiGatewayMethod:
    Type: "AWS::ApiGateway::Method"
    Properties:
      RestApiId: !Ref ApiGatewayRestApi
      ...
      RequestValidatorId: !Ref ApiGatewayRequestValidator
      RequestParameters:
        method.request.querystring.language: true
        method.request.header.clientid: true
```

[api-gateway-rest-validation](api-gateway-rest-validation.yaml)

### API Gateway - REST (NonProxy) - Mappings

Specify Integration.Type as AWS instead of AWS_PROXY

```
  ApiGatewayMethod:
    Type: "AWS::ApiGateway::Method"
    Properties:
      RestApiId: !Ref ApiGatewayRestApi
      ...
      Integration:
        Type: "AWS" #Set to AWS instead of AWS_PROXY
        Uri: !Sub "arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/...
        IntegrationHttpMethod: "POST"
```

Integration Response for HTTP 200

```
      Integration:
        Type: "AWS"
        Uri: !Sub "arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/...
        IntegrationHttpMethod: "POST"
        IntegrationResponses:
          - StatusCode: 200
            ResponseTemplates:
              application/json: |
                {
                  "body" : $input.json('$.body')
                }
```

[api-gateway-rest-mapping](api-gateway-rest-mapping.yaml)

## API Gateway - REST

Provision REST API that showcases the different features

Invoke: curl -X GET https://rest-id.execute-api.eu-west-1.amazonaws.com/stg/demo -H "x-api-key: <api-key>"

[api-gateway-rest](api-gateway-rest.yaml)

## API Gateway - REST - Lambda

Provision REST API that integrates with Lambda.

Invoke: curl -X POST https://rest-id.execute-api.region.amazonaws.com/stg/demo
Invoke: curl -X POST https://rest-id.execute-api.region.amazonaws.com/stg/demo/{name}

[api-gateway-rest-lambda](api-gateway-rest-lambda.yaml)

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
- Execution failed due to configuration error: Invalid permissions on Lambda function
  - ss