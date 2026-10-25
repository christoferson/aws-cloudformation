> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-streamspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable StreamSpecification

Represents the DynamoDB Streams configuration for a table in DynamoDB.

You can only modify this value for a `AWS::DynamoDB::GlobalTable` resource configured for multi-Region eventual consistency (MREC, the default) if that resource contains only one entry in `Replicas`. You must specify a value for this property for a `AWS::DynamoDB::GlobalTable` resource configured for MREC with more than one entry in `Replicas`. For Multi-Region Strong Consistency (MRSC), Streams are not required and can be changed for existing tables.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "StreamViewType" : String
}

```

### YAML

```
  StreamViewType: String

```

## Properties

**`StreamViewType`** 

 When an item in the table is modified, `StreamViewType` determines what information is written to the stream for this table. Valid values for `StreamViewType` are:  
`KEYS_ONLY` - Only the key attributes of the modified item are written to the stream. 
`NEW_IMAGE` - The entire item, as it appears after it was modified, is written to the stream. 
`OLD_IMAGE` - The entire item, as it appeared before it was modified, is written to the stream. 
`NEW_AND_OLD_IMAGES` - Both the new and the old item images of the item are written to the stream. 
 

Required: Yes

Type: String

Allowed values: `NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES | KEYS_ONLY`

Update requires: No interruption
