> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-csv.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table Csv

 The options for imported source files in CSV format. The values are Delimiter and HeaderList. 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Delimiter" : String,
  "HeaderList" : [ String, ... ]
}

```

### YAML

```
  Delimiter: String
  HeaderList: 
    - String

```

## Properties

**`Delimiter`** 

 The delimiter used for separating items in the CSV file being imported.  

Required: No

Type: String

Pattern: `[,;:|\t ]`

Minimum: `1`

Maximum: `1`

Update requires: Replacement

**`HeaderList`** 

 List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header.  

Required: No

Type: Array of String

Minimum: `1`

Maximum: `255`

Update requires: Replacement
