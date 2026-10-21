> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-experimentrun-treatmentoverrides.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExperimentRun TreatmentOverrides

Treatment assignment overrides that assign specific entity IDs to treatments, bypassing random assignment.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Inline" : {Key: Value, ...}
}

```

### YAML

```
  Inline: 
    Key: Value

```

## Properties

**`Inline`** 

A map of entity IDs to treatment keys. Each entry assigns the specified entity to the specified treatment, bypassing random assignment. 

Required: No

Type: Object of String

Pattern: `^.+$`

Update requires: No interruption
