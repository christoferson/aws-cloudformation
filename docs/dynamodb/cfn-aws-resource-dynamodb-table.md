> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table

The `AWS::DynamoDB::Table` resource creates a DynamoDB table. For more information, see CreateTable in the Amazon DynamoDB API Reference.

You should be aware of the following behaviors when working with DynamoDB tables: 
AWS CloudFormation typically creates DynamoDB tables in parallel. However, if your template includes multiple DynamoDB tables with indexes, you must declare dependencies so that the tables are created sequentially. Amazon DynamoDB limits the number of tables with secondary indexes that are in the creating state. If you create multiple tables with indexes at the same time, DynamoDB returns an error and the stack operation fails. For an example, see DynamoDB Table with a DependsOn Attribute. 
Important

 Our guidance is to use the latest schema documented for your AWS CloudFormation templates. This schema supports the provisioning of all table settings below. When using this schema in your AWS CloudFormation templates, please ensure that your Identity and Access Management (IAM) policies are updated with appropriate permissions to allow for the authorization of these setting changes.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::DynamoDB::Table",
  "Properties" : {
      "AttributeDefinitions" : [ AttributeDefinition, ... ],
      "BillingMode" : String,
      "ContributorInsightsSpecification" : ContributorInsightsSpecification,
      "DeletionProtectionEnabled" : Boolean,
      "GlobalSecondaryIndexes" : [ GlobalSecondaryIndex, ... ],
      "ImportSourceSpecification" : ImportSourceSpecification,
      "KeySchema" : [ KeySchema, ... ],
      "KinesisStreamSpecification" : KinesisStreamSpecification,
      "LocalSecondaryIndexes" : [ LocalSecondaryIndex, ... ],
      "OnDemandThroughput" : OnDemandThroughput,
      "PointInTimeRecoverySpecification" : PointInTimeRecoverySpecification,
      "ProvisionedThroughput" : ProvisionedThroughput,
      "ResourcePolicy" : ResourcePolicy,
      "SSESpecification" : SSESpecification,
      "StreamSpecification" : StreamSpecification,
      "TableClass" : String,
      "TableName" : String,
      "Tags" : [ Tag, ... ],
      "TimeToLiveSpecification" : TimeToLiveSpecification,
      "VectorIndexes" : [ VectorIndex, ... ],
      "WarmThroughput" : WarmThroughput
    }
}

```

### YAML

```
Type: AWS::DynamoDB::Table
Properties:
  AttributeDefinitions: 
    - AttributeDefinition
  BillingMode: String
  ContributorInsightsSpecification: 
    ContributorInsightsSpecification
  DeletionProtectionEnabled: Boolean
  GlobalSecondaryIndexes: 
    - GlobalSecondaryIndex
  ImportSourceSpecification: 
    ImportSourceSpecification
  KeySchema: 
    - KeySchema
  KinesisStreamSpecification: 
    KinesisStreamSpecification
  LocalSecondaryIndexes: 
    - LocalSecondaryIndex
  OnDemandThroughput: 
    OnDemandThroughput
  PointInTimeRecoverySpecification: 
    PointInTimeRecoverySpecification
  ProvisionedThroughput: 
    ProvisionedThroughput
  ResourcePolicy: 
    ResourcePolicy
  SSESpecification: 
    SSESpecification
  StreamSpecification: 
    StreamSpecification
  TableClass: String
  TableName: String
  Tags: 
    - Tag
  TimeToLiveSpecification: 
    TimeToLiveSpecification
  VectorIndexes: 
    - VectorIndex
  WarmThroughput: 
    WarmThroughput

```

## Properties

**`AttributeDefinitions`** 

A list of attributes that describe the key schema for the table and indexes. 

This property is required to create a DynamoDB table. 

You can add an `AttributeDefinition` without interruption. Changing the type of an existing `AttributeDefinition` requires replacement of the table. 

Required: Conditional

Type: Array of AttributeDefinition

Update requires: No interruption

**`BillingMode`** 

Specify how you are charged for read and write throughput and how you manage capacity. 

Valid values include:  
`PAY_PER_REQUEST` - We recommend using `PAY_PER_REQUEST` for most DynamoDB workloads. `PAY_PER_REQUEST` sets the billing mode to On-demand capacity mode.  
`PROVISIONED` - We recommend using `PROVISIONED` for steady workloads with predictable growth where capacity requirements can be reliably forecasted. `PROVISIONED` sets the billing mode to Provisioned capacity mode. 
 

If not specified, the default is `PROVISIONED`. 

Required: No

Type: String

Allowed values: `PROVISIONED | PAY_PER_REQUEST`

Update requires: No interruption

**`ContributorInsightsSpecification`** 

The settings used to specify whether to enable CloudWatch Contributor Insights for the table and define which events to monitor. 

Required: No

Type: ContributorInsightsSpecification

Update requires: No interruption

**`DeletionProtectionEnabled`** 

Determines if a table is protected from deletion. When enabled, the table cannot be deleted by any user or process. This setting is disabled by default. For more information, see Using deletion protection in the Amazon DynamoDBDeveloper Guide. 

Required: No

Type: Boolean

Update requires: No interruption

**`GlobalSecondaryIndexes`** 

Global secondary indexes to be created on the table. You can create up to 20 global secondary indexes. Important

If you update a table to include a new global secondary index, AWS CloudFormation initiates the index creation and then proceeds with the stack update. AWS CloudFormation doesn't wait for the index to complete creation because the backfilling phase can take a long time, depending on the size of the table. You can't use the index or update the table until the index's status is `ACTIVE`. You can track its status by using the DynamoDB DescribeTable command.

If you add or delete an index during an update, we recommend that you don't update any other resources. If your stack fails to update and is rolled back while adding a new index, you must manually delete the index. 

Updates are not supported. The following are exceptions: 
If you update either the contributor insights specification or the provisioned throughput values of global secondary indexes, you can update the table without interruption. 
You can create or delete one index without interruption. This index can be a global secondary index or a vector index, but not one of each. If you change more than one index in the same update, the update fails. 
 

Required: No

Type: Array of GlobalSecondaryIndex

Update requires: No interruption

**`ImportSourceSpecification`** 

Specifies the properties of data being imported from the S3 bucket source to the" table. Important

If you specify the `ImportSourceSpecification` property, and also specify either the `StreamSpecification`, the `TableClass` property, the `DeletionProtectionEnabled` property, or the `WarmThroughput` property, the IAM entity creating/updating stack must have `UpdateTable` permission. 

Required: No

Type: ImportSourceSpecification

Update requires: Replacement

**`KeySchema`** 

Specifies the attributes that make up the primary key for the table. The attributes in the `KeySchema` property must also be defined in the `AttributeDefinitions` property. 

Required: Yes

Type: Array of KeySchema

Update requires: Some interruptions

**`KinesisStreamSpecification`** 

The Kinesis Data Streams configuration for the specified table. 

Required: No

Type: KinesisStreamSpecification

Update requires: No interruption

**`LocalSecondaryIndexes`** 

Local secondary indexes to be created on the table. You can create up to 5 local secondary indexes. Each index is scoped to a given hash key value. The size of each hash key can be up to 10 gigabytes. 

Required: No

Type: Array of LocalSecondaryIndex

Update requires: No interruption

**`OnDemandThroughput`** 

Sets the maximum number of read and write units for the specified on-demand table. If you use this property, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both. 

Required: No

Type: OnDemandThroughput

Update requires: No interruption

**`PointInTimeRecoverySpecification`** 

The settings used to enable point in time recovery. 

Required: No

Type: PointInTimeRecoverySpecification

Update requires: No interruption

**`ProvisionedThroughput`** 

Throughput for the specified table, which consists of values for `ReadCapacityUnits` and `WriteCapacityUnits`. For more information about the contents of a provisioned throughput structure, see Amazon DynamoDB Table ProvisionedThroughput.  

If you set `BillingMode` as `PROVISIONED`, you must specify this property. If you set `BillingMode` as `PAY_PER_REQUEST`, you cannot specify this property. 

Required: Conditional

Type: ProvisionedThroughput

Update requires: No interruption

**`ResourcePolicy`** 

An AWS resource-based policy document in JSON format that will be attached to the table. 

When you attach a resource-based policy while creating a table, the policy application is strongly consistent. 

The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit. For a full list of all considerations that apply for resource-based policies, see Resource-based policy considerations. Note

You need to specify the `CreateTable` and `PutResourcePolicy` IAM actions for authorizing a user to create a table with a resource-based policy. 

Required: No

Type: ResourcePolicy

Update requires: No interruption

**`SSESpecification`** 

Specifies the settings to enable server-side encryption. 

Required: No

Type: SSESpecification

Update requires: Some interruptions

**`StreamSpecification`** 

The settings for the DynamoDB table stream, which captures changes to items stored in the table. Including this property in your AWS CloudFormation template automatically enables streaming. 

Required: No

Type: StreamSpecification

Update requires: No interruption

**`TableClass`** 

The table class of the new table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`. 

Required: No

Type: String

Allowed values: `STANDARD | STANDARD_INFREQUENT_ACCESS`

Update requires: No interruption

**`TableName`** 

A name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name. For more information, see Name Type. Important

If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. 

Required: No

Type: String

Minimum: `1`

Maximum: `1024`

Update requires: Replacement

**`Tags`** 

An array of key-value pairs to apply to this resource. 

For more information, see Tag. 

Required: No

Type: Array of Tag

Update requires: No interruption

**`TimeToLiveSpecification`** 

Specifies the Time to Live (TTL) settings for the table. Note

For detailed information about the limits in DynamoDB, see Limits in Amazon DynamoDB in the Amazon DynamoDB Developer Guide.  

Required: No

Type: TimeToLiveSpecification

Update requires: No interruption

**`VectorIndexes`** 

The vector indexes to create on the table. Each vector index enables similarity search on a vector attribute. Important

Vector indexes are supported only on tables that use on-demand capacity mode. To use vector indexes, you must set `BillingMode` to `PAY_PER_REQUEST`.

In a single stack operation, you can create or delete one index. This index can be a global secondary index or a vector index, but not one of each. To change more indexes, use a separate stack operation for each. 

Required: No

Type: Array of VectorIndex

Minimum: `1`

Update requires: No interruption

**`WarmThroughput`** 

Represents the warm throughput (in read units per second and write units per second) for creating a table. 

Required: No

Type: WarmThroughput

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myDynamoDBTable" }` 

For the resource with the logical ID `myDynamoDBTable`, `Ref` will return the DynamoDB table name.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The Amazon Resource Name (ARN) of the DynamoDB table, such as `arn:aws:dynamodb:us-east-2:123456789012:table/myDynamoDBTable`. 

**`StreamArn`** 

The ARN of the DynamoDB stream, such as `arn:aws:dynamodb:us-east-1:123456789012:table/testddbstack-myDynamoDBTable-012A1SL7SMP5Q/stream/2015-11-30T20:10:00.000`.  Note

You must specify the `StreamSpecification` property to use this attribute. 

## Examples 
DynamoDB Table with Local and Secondary Indexes
DynamoDB Table with a DependsOn Attribute
DynamoDB Table with Application Auto Scaling
 

### DynamoDB Table with Local and Secondary Indexes

The following sample creates a DynamoDB table with `Album`, `Artist`, `Sales`, `NumberOfSongs` as attributes. The primary key includes the `Album` attribute as the hash key and `Artist` attribute as the range key. The table also includes two global and one secondary index. For querying the number of sales for a given artist, the global secondary index uses the `Sales` attribute as the hash key and the `Artist` attribute as the range key.

For querying the sales based on the number of songs, the global secondary index uses the `NumberOfSongs` attribute as the hash key and the `Sales` attribute as the range key.

For querying the sales of an album, the local secondary index uses the same hash key as the table but uses the `Sales` attribute as the range key.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "myDynamoDBTable": {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "AttributeDefinitions": [
                    {
                        "AttributeName": "Album",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "Artist",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "Sales",
                        "AttributeType": "N"
                    },
                    {
                        "AttributeName": "NumberOfSongs",
                        "AttributeType": "N"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "Album",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "Artist",
                        "KeyType": "RANGE"
                    }
                ],
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": "5",
                    "WriteCapacityUnits": "5"
                },
                "TableName": "myTableName",
                "GlobalSecondaryIndexes": [
                    {
                        "IndexName": "myGSI",
                        "KeySchema": [
                            {
                                "AttributeName": "Sales",
                                "KeyType": "HASH"
                            },
                            {
                                "AttributeName": "Artist",
                                "KeyType": "RANGE"
                            }
                        ],
                        "Projection": {
                            "NonKeyAttributes": [
                                "Album",
                                "NumberOfSongs"
                            ],
                            "ProjectionType": "INCLUDE"
                        },
                        "ProvisionedThroughput": {
                            "ReadCapacityUnits": "5",
                            "WriteCapacityUnits": "5"
                        }
                    },
                    {
                        "IndexName": "myGSI2",
                        "KeySchema": [
                            {
                                "AttributeName": "NumberOfSongs",
                                "KeyType": "HASH"
                            },
                            {
                                "AttributeName": "Sales",
                                "KeyType": "RANGE"
                            }
                        ],
                        "Projection": {
                            "NonKeyAttributes": [
                                "Album",
                                "Artist"
                            ],
                            "ProjectionType": "INCLUDE"
                        },
                        "ProvisionedThroughput": {
                            "ReadCapacityUnits": "5",
                            "WriteCapacityUnits": "5"
                        }
                    }
                ],
                "LocalSecondaryIndexes": [
                    {
                        "IndexName": "myLSI",
                        "KeySchema": [
                            {
                                "AttributeName": "Album",
                                "KeyType": "HASH"
                            },
                            {
                                "AttributeName": "Sales",
                                "KeyType": "RANGE"
                            }
                        ],
                        "Projection": {
                            "NonKeyAttributes": [
                                "Artist",
                                "NumberOfSongs"
                            ],
                            "ProjectionType": "INCLUDE"
                        }
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: Album
          AttributeType: S
        - AttributeName: Artist
          AttributeType: S
        - AttributeName: Sales
          AttributeType: 'N'
        - AttributeName: NumberOfSongs
          AttributeType: 'N'
      KeySchema:
        - AttributeName: Album
          KeyType: HASH
        - AttributeName: Artist
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: '5'
        WriteCapacityUnits: '5'
      TableName: myTableName
      GlobalSecondaryIndexes:
        - IndexName: myGSI
          KeySchema:
            - AttributeName: Sales
              KeyType: HASH
            - AttributeName: Artist
              KeyType: RANGE
          Projection:
            NonKeyAttributes:
              - Album
              - NumberOfSongs
            ProjectionType: INCLUDE
          ProvisionedThroughput:
            ReadCapacityUnits: '5'
            WriteCapacityUnits: '5'
        - IndexName: myGSI2
          KeySchema:
            - AttributeName: NumberOfSongs
              KeyType: HASH
            - AttributeName: Sales
              KeyType: RANGE
          Projection:
            NonKeyAttributes:
              - Album
              - Artist
            ProjectionType: INCLUDE
          ProvisionedThroughput:
            ReadCapacityUnits: '5'
            WriteCapacityUnits: '5'
      LocalSecondaryIndexes:
        - IndexName: myLSI
          KeySchema:
            - AttributeName: Album
              KeyType: HASH
            - AttributeName: Sales
              KeyType: RANGE
          Projection:
            NonKeyAttributes:
              - Artist
              - NumberOfSongs
            ProjectionType: INCLUDE
```
 

### DynamoDB Table with a DependsOn Attribute

If you include multiple DynamoDB tables with indexes in a single template, you must include dependencies so that the tables are created sequentially. DynamoDB limits the number of tables with secondary indexes that are in the creating state. If you create multiple tables with indexes at the same time, DynamoDB returns an error and the stack operation fails.

The following sample assumes that the `myFirstDDBTable` table is declared in the same template as the `mySecondDDBTable` table, and both tables include a secondary index. The `mySecondDDBTable` table includes a dependency on the `myFirstDDBTable` table so that AWS CloudFormation creates the tables one at a time.

#### JSON

```
{
    "mySecondDDBTable": {
        "Type": "AWS::DynamoDB::Table",
        "DependsOn": "myFirstDDBTable",
        "Properties": {
            "AttributeDefinitions": [
                {
                    "AttributeName": "ArtistId",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "Concert",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "TicketSales",
                    "AttributeType": "S"
                }
            ],
            "KeySchema": [
                {
                    "AttributeName": "ArtistId",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "Concert",
                    "KeyType": "RANGE"
                }
            ],
            "ProvisionedThroughput": {
                "ReadCapacityUnits": {
                    "Ref": "ReadCapacityUnits"
                },
                "WriteCapacityUnits": {
                    "Ref": "WriteCapacityUnits"
                }
            },
            "GlobalSecondaryIndexes": [
                {
                    "IndexName": "myGSI",
                    "KeySchema": [
                        {
                            "AttributeName": "TicketSales",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "KEYS_ONLY"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": {
                            "Ref": "ReadCapacityUnits"
                        },
                        "WriteCapacityUnits": {
                            "Ref": "WriteCapacityUnits"
                        }
                    }
                }
            ],
            "Tags": [
                {
                    "Key": "foo",
                    "Value": "bar"
                }
            ]
        }
    }
}
```

#### YAML

```
mySecondDDBTable:
  Type: AWS::DynamoDB::Table
  DependsOn: myFirstDDBTable
  Properties:
    AttributeDefinitions:
      - AttributeName: ArtistId
        AttributeType: S
      - AttributeName: Concert
        AttributeType: S
      - AttributeName: TicketSales
        AttributeType: S
    KeySchema:
      - AttributeName: ArtistId
        KeyType: HASH
      - AttributeName: Concert
        KeyType: RANGE
    ProvisionedThroughput:
      ReadCapacityUnits: !Ref ReadCapacityUnits
      WriteCapacityUnits: !Ref WriteCapacityUnits
    GlobalSecondaryIndexes:
      - IndexName: myGSI
        KeySchema:
          - AttributeName: TicketSales
            KeyType: HASH
        Projection:
          ProjectionType: KEYS_ONLY
        ProvisionedThroughput:
          ReadCapacityUnits: !Ref ReadCapacityUnits
          WriteCapacityUnits: !Ref WriteCapacityUnits
    Tags:
      - Key: foo
        Value: bar
```
 

### DynamoDB Table with Application Auto Scaling

This example sets up Application Auto Scaling for a `AWS::DynamoDB::Table` resource. The template defines a `TargetTrackingScaling` scaling policy that scales up the `WriteCapacityUnits` throughput for the table. 

#### JSON

```
{
  "Resources": {
    "DDBTable": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "AttributeDefinitions": [
          {
            "AttributeName": "ArtistId",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Concert",
            "AttributeType": "S"
          },
          {
            "AttributeName": "TicketSales",
            "AttributeType": "S"
          }
        ],
        "KeySchema": [
          {
            "AttributeName": "ArtistId",
            "KeyType": "HASH"
          },
          {
            "AttributeName": "Concert",
            "KeyType": "RANGE"
          }
        ],
        "GlobalSecondaryIndexes": [
          {
            "IndexName": "GSI",
            "KeySchema": [
              {
                "AttributeName": "TicketSales",
                "KeyType": "HASH"
              }
            ],
            "Projection": {
              "ProjectionType": "KEYS_ONLY"
            },
            "ProvisionedThroughput": {
              "ReadCapacityUnits": 5,
              "WriteCapacityUnits": 5
            }
          }
        ],
        "ProvisionedThroughput": {
          "ReadCapacityUnits": 5,
          "WriteCapacityUnits": 5
        }
      }
    },
    "WriteCapacityScalableTarget": {
      "Type": "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties": {
        "MaxCapacity": 15,
        "MinCapacity": 5,
        "ResourceId": { "Fn::Join": [
          "/",
          [
            "table",
            { "Ref": "DDBTable" }
          ]
        ] },
        "RoleARN": {
          "Fn::GetAtt": ["ScalingRole", "Arn"]
        },
        "ScalableDimension": "dynamodb:table:WriteCapacityUnits",
        "ServiceNamespace": "dynamodb"
      }
    },
    "ScalingRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "application-autoscaling.amazonaws.com"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "Path": "/",
        "Policies": [
          {
            "PolicyName": "root",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "dynamodb:DescribeTable",
                    "dynamodb:UpdateTable",
                    "cloudwatch:PutMetricAlarm",
                    "cloudwatch:DescribeAlarms",
                    "cloudwatch:GetMetricStatistics",
                    "cloudwatch:SetAlarmState",
                    "cloudwatch:DeleteAlarms"
                  ],
                  "Resource": "*"
                }
              ]
            }
          }
        ]
      }
    },
    "WriteScalingPolicy": {
      "Type": "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties": {
        "PolicyName": "WriteAutoScalingPolicy",
        "PolicyType": "TargetTrackingScaling",
        "ScalingTargetId": {
          "Ref": "WriteCapacityScalableTarget"
        },
        "TargetTrackingScalingPolicyConfiguration": {
          "TargetValue": 50.0,
          "ScaleInCooldown": 60,
          "ScaleOutCooldown": 60,
          "PredefinedMetricSpecification": {
            "PredefinedMetricType": "DynamoDBWriteCapacityUtilization"
          }
        }
      }
    }
  }
}
```

#### YAML

```
Resources:
  DDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
          AttributeName: "ArtistId"
          AttributeType: "S"
          AttributeName: "Concert"
          AttributeType: "S"
          AttributeName: "TicketSales"
          AttributeType: "S"
      KeySchema:
          AttributeName: "ArtistId"
          KeyType: "HASH"
          AttributeName: "Concert"
          KeyType: "RANGE"
      GlobalSecondaryIndexes:
          IndexName: "GSI"
          KeySchema:
              AttributeName: "TicketSales"
              KeyType: "HASH"
          Projection:
            ProjectionType: "KEYS_ONLY"
          ProvisionedThroughput:
            ReadCapacityUnits: 5
            WriteCapacityUnits: 5
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
  WriteCapacityScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 15
      MinCapacity: 5
      ResourceId: !Join
        - /
        - - table
          - !Ref DDBTable
      RoleARN: !GetAtt ScalingRole.Arn
      ScalableDimension: dynamodb:table:WriteCapacityUnits
      ServiceNamespace: dynamodb
  ScalingRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
            Effect: "Allow"
            Principal:
              Service:
                - application-autoscaling.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: "/"
      Policies:
          PolicyName: "root"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
                Effect: "Allow"
                Action:
                  - "dynamodb:DescribeTable"
                  - "dynamodb:UpdateTable"
                  - "cloudwatch:PutMetricAlarm"
                  - "cloudwatch:DescribeAlarms"
                  - "cloudwatch:GetMetricStatistics"
                  - "cloudwatch:SetAlarmState"
                  - "cloudwatch:DeleteAlarms"
                Resource: "*"
  WriteScalingPolicy:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: WriteAutoScalingPolicy
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref WriteCapacityScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 50.0
        ScaleInCooldown: 60
        ScaleOutCooldown: 60
        PredefinedMetricSpecification:
          PredefinedMetricType: DynamoDBWriteCapacityUtilization
```
