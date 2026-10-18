> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitpullrequestfilter.html
> Downloaded: 2026-10-18

# AWS::CodePipeline::Pipeline GitPullRequestFilter

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter: 
CLOSED 
OPEN 
UPDATED 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Branches" : GitBranchFilterCriteria,
  "Events" : [ String, ... ],
  "FilePaths" : GitFilePathFilterCriteria
}

```

### YAML

```
  Branches: 
    GitBranchFilterCriteria
  Events: 
    - String
  FilePaths: 
    GitFilePathFilterCriteria

```

## Properties

**`Branches`** 

The field that specifies to filter on branches for the pull request trigger configuration. 

Required: No

Type: GitBranchFilterCriteria

Update requires: No interruption

**`Events`** 

The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `3`

Update requires: No interruption

**`FilePaths`** 

The field that specifies to filter on file paths for the pull request trigger configuration. 

Required: No

Type: GitFilePathFilterCriteria

Update requires: No interruption
