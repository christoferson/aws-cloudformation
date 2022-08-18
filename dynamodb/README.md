## DynamoDB Cloudformation

### DynamoDB - Basic

Provision a DynamoDB with HASH and RANGE key.

[dynamodb-basic](dynamodb-basic.yaml)

### DynamoDB - Local Secondary Index

Provision a DynamoDB with LSI

[dynamodb-index-local](dynamodb-index-local.yaml)

### DynamoDB - Stream

Provision a DynamoDB with Streams Enabled. Lambda Function called on Item insertion and modification.

[dynamodb-stream](dynamodb-stream.yaml)

### DynamoDB - Dax

Provision a DynamoDB DAX Cluster.

[dynamodb-dax](dynamodb-dax.yaml)

### Auto Scaling (RCU and WCU)

Provision a DynamoDB table with Auto-scaling configuration for both RCU and WCU.

Script: dynamodb-autoscale.yaml


### Service Link Role

-  https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html
-  arn:aws:iam::${AWS::AccountId}:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable






# Service Link Role
-  You can specify the ARN of a service-linked role for the RoleARN property of an AWS::ApplicationAutoScaling::ScalableTarget resource in your AWS CloudFormation stack templates, 
-  even if the specified service-linked role doesn't yet exist. Application Auto Scaling automatically creates the role for you.

# ScalableDimension
- dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
- dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
- dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
- dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.

# Errors - DAX
- "dax" No endpoints available 
  You can only connect to DAX from an EC2 machine in the same VPC as the DAX cluster.


### TODO

- DAX (Memory Caching) - Dax Endpoint, Read Heavy Application, Runs inside VPC, Encryption at REST