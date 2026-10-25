> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-projection.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable Projection

Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "NonKeyAttributes" : [ String, ... ],
  "ProjectionType" : String
}

```

### YAML

```
  NonKeyAttributes: 
    - String
  ProjectionType: String

```

## Properties

**`NonKeyAttributes`** 

Represents the non-key attribute names which will be projected into the index. 

For global and local secondary indexes, the total count of `NonKeyAttributes` summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes. 

Required: No

Type: Array of String

Maximum: `20`

Update requires: Updates are not supported.

**`ProjectionType`** 

The set of attributes that are projected into the index:  
`KEYS_ONLY` - Only the index and primary keys are projected into the index. 
`INCLUDE` - In addition to the attributes described in `KEYS_ONLY`, the secondary index will include other non-key attributes that you specify. 
`ALL` - All of the table attributes are projected into the index. 
 

When using the DynamoDB console, `ALL` is selected by default. 

Required: No

Type: String

Allowed values: `ALL | KEYS_ONLY | INCLUDE`

Update requires: Some interruptions
