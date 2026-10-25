> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-importsourcespecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table ImportSourceSpecification

Specifies the properties of data being imported from the S3 bucket source to the table.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "InputCompressionType" : String,
  "InputFormat" : String,
  "InputFormatOptions" : InputFormatOptions,
  "S3BucketSource" : S3BucketSource
}

```

### YAML

```
  InputCompressionType: String
  InputFormat: String
  InputFormatOptions: 
    InputFormatOptions
  S3BucketSource: 
    S3BucketSource

```

## Properties

**`InputCompressionType`** 

 Type of compression to be used on the input coming from the imported table.  

Required: No

Type: String

Allowed values: `GZIP | ZSTD | NONE`

Update requires: Replacement

**`InputFormat`** 

 The format of the source data. Valid values for `ImportFormat` are `CSV`, `DYNAMODB_JSON` or `ION`.  

Required: Yes

Type: String

Allowed values: `DYNAMODB_JSON | ION | CSV`

Update requires: Replacement

**`InputFormatOptions`** 

 Additional properties that specify how the input is formatted,  

Required: No

Type: InputFormatOptions

Update requires: Replacement

**`S3BucketSource`** 

 The S3 bucket that provides the source for the import.  

Required: Yes

Type: S3BucketSource

Update requires: Replacement
