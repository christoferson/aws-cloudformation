> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-gitpushfilter.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline GitPushFilter

The event criteria that specify when a specified repository event will start the pipeline for the specified trigger configuration, such as the lists of Git tags to include and exclude.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Branches" : GitBranchFilterCriteria,
  "FilePaths" : GitFilePathFilterCriteria,
  "Tags" : GitTagFilterCriteria
}

```

### YAML

```
  Branches: 
    GitBranchFilterCriteria
  FilePaths: 
    GitFilePathFilterCriteria
  Tags: 
    GitTagFilterCriteria

```

## Properties

**`Branches`**
 

The field that specifies to filter on branches for the push trigger configuration. 

Required: No

Type: GitBranchFilterCriteria

Update requires: No interruption

**`FilePaths`**
 

The field that specifies to filter on file paths for the push trigger configuration. 

Required: No

Type: GitFilePathFilterCriteria

Update requires: No interruption

**`Tags`**
 

The field that contains the details for the Git tags trigger configuration. 

Required: No

Type: GitTagFilterCriteria

Update requires: No interruption

