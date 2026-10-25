> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-inputformatoptions.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::Table InputFormatOptions

 The format options for the data that was imported into the target table. There is one value, CsvOption.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Csv" : Csv
}

```

### YAML

```
  Csv: 
    Csv

```

## Properties

**`Csv`** 

 The options for imported source files in CSV format. The values are Delimiter and HeaderList.  

Required: No

Type: Csv

Update requires: Replacement
