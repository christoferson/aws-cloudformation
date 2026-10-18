> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-pipelinetriggerdeclaration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline PipelineTriggerDeclaration

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.Note

This is only supported for the `CodeStarSourceConnection` action type.Note

When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "GitConfiguration" : GitConfiguration,
  "ProviderType" : String
}

```

### YAML

```
  GitConfiguration: 
    GitConfiguration
  ProviderType: String

```

## Properties

**`GitConfiguration`**
 

Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags. 

Required: No

Type: GitConfiguration

Update requires: No interruption

**`ProviderType`**
 

The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration. 

Required: Yes

Type: String

Allowed values: `CodeStarSourceConnection`

Update requires: No interruption

