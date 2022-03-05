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

## API Gateway - REST

Provision REST API that integrates with specified Lambda.

[api-gateway-rest](api-gateway-rest.yaml)

## Resources

- [Cloudformation API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
- [Cloudformation REST API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html)

## Errors

- Internal Server Error if no permission to Invoke Lambda