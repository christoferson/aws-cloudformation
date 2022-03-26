## API Gateway - HTTP

### API Gateway - Quick Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda using Quick Create

[api-gateway-http-quick](api-gateway-http-quick.yaml)

### API Gateway - Integrate with existing Lambda

Provision HTTP API that integrates with specified Lambda.

[api-gateway-http](api-gateway-http.yaml)

### API Gateway - Integrate with Lambda

Provision HTTP API that integrates with newly provisioned Lambda.

[api-gateway-http-lambda](api-gateway-http-lambda.yaml)


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


## API Gateway - REST

Provision REST API that integrates with specified Lambda.

[api-gateway-rest](api-gateway-rest.yaml)

## Resources

- [Cloudformation API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
- [Cloudformation REST API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html)
- [JWT Authorizer] (https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)
- [Lambda Authorizer] (https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html)

## Errors

- Internal Server Error if no permission to Invoke Lambda