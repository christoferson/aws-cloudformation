> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-experimentrun.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExperimentRun

Describes an experiment run, including its status, exposure settings, and treatment overrides.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AppConfig::ExperimentRun",
  "Properties" : {
      "ApplicationIdentifier" : String,
      "Description" : String,
      "ExperimentDefinitionIdentifier" : String,
      "ExposurePercentage" : Number,
      "Tags" : [ Tag, ... ],
      "TreatmentOverrides" : TreatmentOverrides
    }
}

```

### YAML

```
Type: AWS::AppConfig::ExperimentRun
Properties:
  ApplicationIdentifier: String
  Description: String
  ExperimentDefinitionIdentifier: String
  ExposurePercentage: Number
  Tags: 
    - Tag
  TreatmentOverrides: 
    TreatmentOverrides

```

## Properties

**`ApplicationIdentifier`**

Property description not available.

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`Description`** 

A description of the experiment run. 

Required: No

Type: String

Maximum: `1024`

Update requires: No interruption

**`ExperimentDefinitionIdentifier`**

Property description not available.

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`ExposurePercentage`** 

The percentage of the target audience exposed to treatments. 

Required: Yes

Type: Number

Minimum: `0`

Maximum: `100`

Update requires: No interruption

**`Tags`**

Property description not available.

Required: No

Type: Array of Tag

Update requires: No interruption

**`TreatmentOverrides`** 

Treatment assignment overrides that assign specific entity IDs to treatments. 

Required: No

Type: TreatmentOverrides

Update requires: No interruption

## Return values

### Ref

### Fn::GetAtt

#### 

**`ApplicationId`** 

The application ID. 

**`ExperimentDefinitionId`** 

The experiment definition ID. 

**`Run`** 

The experiment run number. 

**`StartedAt`** 

The date and time the experiment run started, in ISO 8601 format. 

**`Status`** 

The current status of the experiment run. Valid values: `RUNNING`, `DONE`. 

**`UpdatedAt`** 

The date and time the experiment run was last updated, in ISO 8601 format.
