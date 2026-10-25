> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-streamspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table StreamSpecification

Represents the DynamoDB Streams configuration for a table in DynamoDB.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ResourcePolicy" : ResourcePolicy,
  "StreamViewType" : String,
  "Tags" : [ Tag, ... ]
}

```

### YAML

```
  ResourcePolicy: 
    ResourcePolicy
  StreamViewType: String
  Tags: 
    - Tag

```

## Properties

**`ResourcePolicy`** 

Creates or updates a resource-based policy document that contains the permissions for DynamoDB resources, such as a table's streams. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource. Note

When you remove the `StreamSpecification` property from the template, DynamoDB disables the stream but retains any attached resource policy until the stream is deleted after 24 hours. When you modify the `StreamViewType` property, DynamoDB creates a new stream and retains the old stream's resource policy. The old stream and its resource policy are deleted after the 24-hour retention period. 

In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see Using resource-based policies for DynamoDB and Resource-based policy examples. 

Required: No

Type: ResourcePolicy

Update requires: No interruption

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

**`Tags`** 

Specifies the tags to apply to the DynamoDB stream. Stream tags are independent of table tags. 

For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide. 

Required: No

Type: Array of Tag

Update requires: No interruption
