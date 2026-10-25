> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-vectorindex.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable VectorIndex

Contains the configuration settings for a vector index, including the index name, vector attribute, dimensions, distance function, search schema, and projection.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Dimensions" : Integer,
  "DistanceFunction" : String,
  "IndexName" : String,
  "Projection" : Projection,
  "SearchSchema" : [ SearchSchemaElement, ... ],
  "VectorAttribute" : VectorAttribute
}

```

### YAML

```
  Dimensions: Integer
  DistanceFunction: String
  IndexName: String
  Projection: 
    Projection
  SearchSchema: 
    - SearchSchemaElement
  VectorAttribute: 
    VectorAttribute

```

## Properties

**`Dimensions`** 

The number of dimensions in each vector. 

Required: Yes

Type: Integer

Minimum: `1`

Maximum: `4096`

Update requires: Updates are not supported.

**`DistanceFunction`** 

The distance function used to calculate similarity between vectors. Valid values: `COSINE`, `EUCLIDEAN`, `DOT_PRODUCT`. 

Required: Yes

Type: String

Allowed values: `COSINE | DOT_PRODUCT | EUCLIDEAN`

Update requires: Updates are not supported.

**`IndexName`** 

The name of the vector index. 

Required: Yes

Type: String

Pattern: `[a-zA-Z0-9_.-]+`

Minimum: `3`

Maximum: `255`

Update requires: Updates are not supported.

**`Projection`** 

Specifies attributes that are copied (projected) from the table into the vector index. 

Required: Yes

Type: Projection

Update requires: Updates are not supported.

**`SearchSchema`** 

The search schema that defines partition key and inline filter attributes for the vector index. 

Every attribute that you reference in `SearchSchema` must also be declared in the table's `AttributeDefinitions`, the same way key attributes are declared for a global secondary index. Otherwise, the request fails with a `ValidationException`. 

Required: No

Type: Array of SearchSchemaElement

Minimum: `1`

Update requires: Updates are not supported.

**`VectorAttribute`** 

The vector attribute configuration for the index. 

Required: Yes

Type: VectorAttribute

Update requires: Updates are not supported.
