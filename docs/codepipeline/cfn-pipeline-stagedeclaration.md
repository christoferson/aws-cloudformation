> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-stagedeclaration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline StageDeclaration

Represents information about a stage and its definition.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Actions" : [ ActionDeclaration, ... ],
  "BeforeEntry" : BeforeEntryConditions,
  "Blockers" : [ BlockerDeclaration, ... ],
  "Name" : String,
  "OnFailure" : FailureConditions,
  "OnSuccess" : SuccessConditions
}

```

### YAML

```
  Actions: 
    - ActionDeclaration
  BeforeEntry: 
    BeforeEntryConditions
  Blockers: 
    - BlockerDeclaration
  Name: String
  OnFailure: 
    FailureConditions
  OnSuccess: 
    SuccessConditions

```

## Properties

**`Actions`**
 

The actions included in a stage. 

Required: Yes

Type: Array of ActionDeclaration

Update requires: No interruption

**`BeforeEntry`**
 

The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met. 

Required: No

Type: BeforeEntryConditions

Update requires: No interruption

**`Blockers`**
 

Reserved for future use. 

Required: No

Type: Array of BlockerDeclaration

Update requires: No interruption

**`Name`**
 

The name of the stage. 

Required: Yes

Type: String

Pattern: `[A-Za-z0-9.@\-_]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

**`OnFailure`**
 

The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage. 

Required: No

Type: FailureConditions

Update requires: No interruption

**`OnSuccess`**
 

The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met. 

Required: No

Type: SuccessConditions

Update requires: No interruption

