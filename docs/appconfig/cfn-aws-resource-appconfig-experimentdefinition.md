> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-experimentdefinition.html
> Downloaded: 2026-10-21

# AWS::AppConfig::ExperimentDefinition

Describes an experiment definition, including the target audience, feature flag, treatments, and current status.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::AppConfig::ExperimentDefinition",
  "Properties" : {
      "ApplicationIdentifier" : String,
      "AudienceDescription" : String,
      "AudienceRule" : String,
      "ConfigurationProfileIdentifier" : String,
      "Control" : Treatment,
      "EnvironmentIdentifier" : String,
      "FlagKey" : String,
      "Hypothesis" : String,
      "LaunchCriteria" : String,
      "Name" : String,
      "Tags" : [ Tag, ... ],
      "Treatments" : [ Treatment, ... ]
    }
}

```

### YAML

```
Type: AWS::AppConfig::ExperimentDefinition
Properties:
  ApplicationIdentifier: String
  AudienceDescription: String
  AudienceRule: String
  ConfigurationProfileIdentifier: String
  Control: 
    Treatment
  EnvironmentIdentifier: String
  FlagKey: String
  Hypothesis: String
  LaunchCriteria: String
  Name: String
  Tags: 
    - Tag
  Treatments: 
    - Treatment

```

## Properties

**`ApplicationIdentifier`**

Property description not available.

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`AudienceDescription`** 

A description of the intended audience for the experiment. 

Required: No

Type: String

Maximum: `1024`

Update requires: No interruption

**`AudienceRule`** 

The rule that defines which users are eligible to be assigned to treatments. 

Required: Yes

Type: String

Maximum: `16384`

Update requires: No interruption

**`ConfigurationProfileIdentifier`**

Property description not available.

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`Control`** 

The control treatment used as the baseline for comparison. 

Required: Yes

Type: Treatment

Update requires: No interruption

**`EnvironmentIdentifier`**

Property description not available.

Required: Yes

Type: String

Minimum: `1`

Maximum: `2048`

Update requires: Replacement

**`FlagKey`** 

The key of the feature flag used by the experiment. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`Hypothesis`** 

The hypothesis that the experiment is designed to validate. 

Required: No

Type: String

Maximum: `1024`

Update requires: No interruption

**`LaunchCriteria`** 

The conditions under which the winning treatment should be launched. 

Required: No

Type: String

Maximum: `1024`

Update requires: No interruption

**`Name`** 

The name of the experiment definition. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `64`

Update requires: Replacement

**`Tags`**

Property description not available.

Required: No

Type: Array of Tag

Update requires: No interruption

**`Treatments`** 

The list of treatments defined for the experiment. 

Required: Yes

Type: Array of Treatment

Minimum: `1`

Maximum: `5`

Update requires: No interruption

## Return values

### Ref

### Fn::GetAtt

#### 

**`ApplicationId`** 

The application ID. 

**`Control.Key`**

Property description not available.

**`CreatedAt`** 

The date and time the experiment definition was created, in ISO 8601 format. 

**`Id`** 

The experiment definition ID. 

**`Status`** 

The current status of the experiment definition. Valid values: `ACTIVE`, `IDLE`, `ARCHIVED`. 

**`UpdatedAt`** 

The date and time the experiment definition was last updated, in ISO 8601 format.
