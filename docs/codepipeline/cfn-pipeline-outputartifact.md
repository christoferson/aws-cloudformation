> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-outputartifact.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline OutputArtifact

Represents information about the output of an action.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Files" : [ String, ... ],
  "Name" : String
}

```

### YAML

```
  Files: 
    - String
  Name: String

```

## Properties

**`Files`**
 

The files that you want to associate with the output artifact that will be exported from the compute action. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `10`

Update requires: No interruption

**`Name`**
 

The name of the output of an artifact, such as "My App". 

The output artifact name must exactly match the input artifact declared for a downstream action. However, the downstream action's input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions. 

Output artifact names must be unique within a pipeline. 

Required: Yes

Type: String

Pattern: `[a-zA-Z0-9_\-]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

