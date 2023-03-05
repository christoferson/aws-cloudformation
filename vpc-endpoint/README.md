## CloudFormation VPC Endpoint Examples

### Vpc Endpoint

A VPC endpoint is a virtual scalable networking component you create in a VPC and use as a private entry point to supported AWS services and third-party applications.

### Vpc Endpoint - Gateway Endpoints

- VPC DNS Resolution must be enabled

### Vpc Endpoint - Gateway Endpoint - S3

Provision a VPC Gateway Endpoint for S3.

[vpc-endpoint-s3](vpc-endpoint-s3.yaml)
[vpc-endpoint-gateway-s3](vpc-endpoint-gateway-s3.yaml)

### Vpc Endpoint - Gateway Endpoint - DynamoDB

[vpc-endpoint-gateway-dynamodb](vpc-endpoint-gateway-dynamodb.yaml)

### Vpc Endpoint Interface Endpoints

- Enable DNS Hostnames must be true

- Enable DNS Support must be true

- Uses Private DNS for AWS services

- Leverage Security Groups

[List of Interface Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

### Vpc Endpoint Interface Endpoint - xxx

### Links

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html
- https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html

### TODO
Dynamo
Privatelink