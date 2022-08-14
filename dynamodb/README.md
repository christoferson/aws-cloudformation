## DynamoDB Cloudformation

### DynamoDB - Basic

Provision a DynamoDB with HASH and RANGE key.

[dynamodb-basic](dynamodb-basic.yaml)

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