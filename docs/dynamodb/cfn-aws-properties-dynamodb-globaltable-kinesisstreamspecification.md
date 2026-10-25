> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-kinesisstreamspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable KinesisStreamSpecification

The Kinesis Data Streams configuration for the specified global table replica.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ApproximateCreationDateTimePrecision" : String,
  "StreamArn" : String
}

```

### YAML

```
  ApproximateCreationDateTimePrecision: String
  StreamArn: String

```

## Properties

**`ApproximateCreationDateTimePrecision`** 

The precision for the time and date that the stream was created. 

Required: No

Type: String

Allowed values: `MICROSECOND | MILLISECOND`

Update requires: No interruption

**`StreamArn`** 

The ARN for a specific Kinesis data stream. 

Required: Yes

Type: String

Minimum: `37`

Maximum: `1024`

Update requires: No interruption
