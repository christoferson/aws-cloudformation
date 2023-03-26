## CloudFormation VPC Endpoint Examples

### Vpc Endpoint

A VPC Endpoint is a virtual scalable networking component you create in a VPC and use as a private entry point to supported AWS services and third-party applications.

---

### Vpc Endpoint - Gateway Endpoints

- VPC DNS Resolution must be enabled

- Specify Private Subnet Route Table for the Gateway Endpoints

- You must specify the region when executing AWS S3 commands. i.e. AWS cli defaults to us region

### Vpc Endpoint - Gateway Endpoint - S3

Provision a VPC Gateway Endpoint for S3.

[vpc-endpoint-s3](vpc-endpoint-s3.yaml)
[vpc-endpoint-gateway-s3](vpc-endpoint-gateway-s3.yaml)

### Vpc Endpoint - Gateway Endpoint - DynamoDB

Provision a VPC Gateway Endpoint for DynamoDB.

[vpc-endpoint-gateway-dynamodb](vpc-endpoint-gateway-dynamodb.yaml)

---

### Vpc Endpoint Interface Endpoints

- Enable DNS Hostnames must be true

- Enable DNS Support must be true

- Uses Private DNS for AWS services

- Leverage Security Groups

[List of Interface Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

### Vpc Endpoint Interface Endpoint - xxx

[vpc-endpoint-interface](vpc-endpoint-interface.yaml)

---

### Links

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html
- https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html
- https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-transit-gateway-with-aws-privatelink-and-amazon-route-53-resolver/

### TODO

- [ ] Dynamo

- [ ] Privatelink

- [ ] aws:PrincipalOrgId condition


com.amazonaws.region.batch
com.amazonaws.region.events
com.amazonaws.region.logs
com.amazonaws.region.codebuild
com.amazonaws.region.codecommit
com.amazonaws.region.git-codecommit
com.amazonaws.region.codedeploy
com.amazonaws.region.codepipeline
com.amazonaws.region.codestar-connections.api

com.amazonaws.region.ecr.api
com.amazonaws.region.ecr.dkr

com.amazonaws.region.ecs
com.amazonaws.region.ecs-agent
com.amazonaws.region.ecs-telemetry

com.amazonaws.region.events
com.amazonaws.region.lambda

com.amazonaws.region.secretsmanager
com.amazonaws.region.sts
