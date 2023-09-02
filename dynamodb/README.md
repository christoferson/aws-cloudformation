## DynamoDB Cloudformation

### DynamoDB - Concepts



### DynamoDB - Full

Provision a DynamoDB with various features enabled.

[dynamodb](dynamodb.yaml)

### DynamoDB - Basic

Provision a DynamoDB with HASH and RANGE key.

[dynamodb-basic](dynamodb-basic.yaml)

### DynamoDB - Local Secondary Index

Provision a DynamoDB with LSI

[dynamodb-index-local](dynamodb-index-local.yaml)

### DynamoDB - Global Secondary Index

Provision a DynamoDB with GSI

[dynamodb-index-global](dynamodb-index-global.yaml)

### DynamoDB - Stream

Provision a DynamoDB with Streams Enabled. Lambda Function called on Item insertion and modification.

##### StreamViewType
- KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
- NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
- OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
- NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.

[dynamodb-stream](dynamodb-stream.yaml)

### DynamoDB - Stream - Lambda - S3 - Glue

Writes out DynamoDB modifications to S3 using streams lambda. Format is JSON.

Provisions Glue Database and Catalog to enable querying changes using Athena.

Lambda outputs data in s3://<bucket>/route53/evt/adria-xx.json

##### Athena Query Editor

```
SELECT * FROM "glue-table-dynamodb-streams-s3" limit 2
SELECT charactername, region, profession.s AS profession FROM "glue-table-dynamodb-streams-s3" limit 2
SELECT * FROM "glue-table-dynamodb-streams-s3" WHERE charactername LIKE '%ri%' limit 2
```

[dynamodb-stream-s3](dynamodb-stream-s3.yaml)


### DynamoDB - Stream - Lambda - S3 - Glue (Partitioned)

Writes out DynamoDB modifications to S3 using streams lambda. Format is JSON.

Provisions Glue Database and Catalog to enable querying changes using Athena.

Table is partitioned using region attribute. Lambda outputs data in s3://<bucket>/route53/evt-partitioned/region=xx/adria-xx.json

##### Athena Query Editor

```
# Update Partition Information
MSCK REPAIR TABLE `glue-table-dynamodb-streams-s3-partitioned`

# Select Data
SELECT * FROM "glue-table-dynamodb-streams-s3-partitioned"
SELECT * FROM "glue-table-dynamodb-streams-s3-partitioned" where charactername like '%world'
SELECT * FROM "glue-table-dynamodb-streams-s3-partitioned" WHERE region = 'us' AND charactername like 'A%'
```

##### Create table manualy in Athena Query Editior

```
CREATE EXTERNAL TABLE IF NOT EXISTS `glue-db-dynamodb-streams-s3-partitioned`.`glue-table-dynamodb-streams-s3-partitioned` (
  `charactername` string,
  `Profession` struct<S:string>
)
PARTITIONED BY (
  `region` string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://bucket/route53/evt-partitioned/'
```

[dynamodb-stream-s3-partitioned](dynamodb-stream-s3-partitioned.yaml)

### DynamoDB - Auto Scaling (RCU and WCU))

Provision a DynamoDB table with Auto-scaling configuration for both RCU and WCU.

Script: dynamodb-autoscale.yaml

### DynamoDB - Point in Time Recovery

- After you enable point-in-time recovery, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime. 
- LatestRestorableDateTime is typically 5 minutes before the current time.
- EarliestRestorableDateTime, you can restore your table to any point in time during the last 35 days.
- The point-in-time recovery process always restores to a new table.

### DynamoDB - Global Table

Provision a DynamoDB Global Table

[dynamodb-global](dynamodb-global.yaml)

### DynamoDB - Dax

Provision a DynamoDB DAX Cluster.

[dynamodb-dax](dynamodb-dax.yaml)


### DynamoDB - TTL

Provision a DynamoDB with TTL.

```
  DynamoTable: 
    Type: AWS::DynamoDB::Table
    Properties: 
      TableName: "mytable"
      ...
      TimeToLiveSpecification:
        AttributeName: !Ref TimeToLiveAttributeName
        Enabled: true
```

[dynamodb-ttl](dynamodb-ttl.yaml)

Note


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
- #/TimeToLiveSpecification: required key [Enabled] not found

### Resources

- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html

### TODO

- DAX (Memory Caching) - Dax Endpoint, Read Heavy Application, Runs inside VPC, Encryption at REST
- Point in Time Recovery
- Global Table