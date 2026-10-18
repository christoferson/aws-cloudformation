> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-filter.html
> Downloaded: 2026-10-18

# Add trigger with code push or pull request event types

You can configure filters for pipeline triggers to have pipeline executions started for different Git events, such as tag or branch push, changes in specific file paths, a pull request opened into a specific branch, and so on. You can use the AWS CodePipeline console or the create-pipeline and update-pipeline commands in the AWS CLI to configure trigger filters.Note

The action configuration `BranchName` field defines a single branch, while triggers with filters can be used for any branch or branches that you specify. For a pipeline where triggers are used to filter branches by push or pull request, the pipeline won't use the default `BranchName` field branch in the action configuration. However, the branch in the `BranchName` field in the action configuration is the default when the pipeline is started manually. For an example, see 5: Trigger configured while default action configuration BranchName is used for a manual start.

You can specify filters for the following trigger types:  
-  

Push 

A push trigger starts a pipeline when a change is pushed to your source repository. The execution will use the commit from the branch that you're pushing to (that is, the destination branch). You can filter push triggers on branches, file paths, or Git tags. 
-  

Pull request 

A pull request trigger starts a pipeline when a pull request is opened, updated, or closed in your source repository. The execution will use the commit from the source branch that you're pulling from (that is, the source branch). You can filter pull request triggers on branches and file paths. 

The supported event types for pull requests are the following. All other pull request events are ignored.  
  -  

Opened 
  -  

Updated 
  -  

Closed (merged) 
 Note

Certain pull request event behavior can differ by provider. For details, see Pull request events for triggers by provider. 

The pipeline definition allows you to combine different filters within the same push trigger configuration. For details about the pipeline definition, see Add filters for push and pull request event types (CLI). For a list of field definitions, see triggers in the Pipeline structure reference in this guide.Topics
- 

Add filters for push and pull request event types (console)
- 

Add filters for push and pull request event types (CLI)
- 

Add filters for push and pull request event types (CloudFormation templates)
 

## Add filters for push and pull request event types (console) 

You can use the console to add filters for push events and include or exclude branches or file paths. Add filters (console)
- 

Sign in to the AWS Management Console and open the CodePipeline console at http://console.aws.amazon.com/codesuite/codepipeline/home. 

The names and status of all pipelines associated with your AWS account are displayed.  
-  

In Name, choose the name of the pipeline you want to edit. Otherwise, use these steps on the pipeline creation wizard. 
-  

On the pipeline details page, choose Edit.  
-  

On the Edit page, choose the source action you want to edit. Choose Edit triggers. Choose Specify filter. 
-  

In Event type, choose Push from the following options.  
  -  

Choose Push to start the pipeline when a change is pushed to your source repository. Choosing this enables the fields to specify filters for branches and file paths or Git tags. 
  -  

Choose Pull request to start the pipeline when a pull request is opened, updated, or closed in your source repository. Choosing this enables the fields to specify filters for destination branches and file paths. 
 
-  

Under Push, in Filter type, choose one of the following options.  
  -  

Choose Branch to specify the branches in your source repository that the trigger monitors in order to know when to start a workflow run. In Include, enter patterns for branch names in glob format that you want to specify for the trigger configuration to start your pipeline on changes in the specified branches. In Exclude, enter the regex patterns for branch names in glob format that you want to specify for the trigger configuration to ignore and to not start your pipeline on changes in the specified branches. See Working with glob patterns in syntax for more information. Note

If the include and exclude both have the same pattern, then the default is to exclude the pattern. 

You can use glob patterns to define your branch names. For example, use `main*` to match all branches beginning with `main`. See Working with glob patterns in syntax for more information. 

For a push trigger, specify the branches you're pushing to, that is, the destination branches. For a pull request trigger, specify destination branches you're opening a pull request to. 
  -  

(Optional) Under File paths, specify file paths for your trigger. Enter the names in Include and Exclude as appropriate. 

You can use glob patterns to define your file path names. For example, use `prod*` to match all file paths beginning with `prod`. See Working with glob patterns in syntax for more information. 
  -  

Choose Tags to configure the pipeline trigger configuration to start with Git tags. In Include, enter patterns for tag names in glob format that you want to specify for the trigger configuration to start your pipeline on release of the specified tag or tags. In Exclude, enter the regex patterns for tag names in glob format that you want to specify for the trigger configuration to ignore and to not start your pipeline on release of the specified tag or tags. If the include and exclude both have the same tag pattern, then the default is to exclude the tag pattern. 
 
-  

Under Push, in Filter type, choose one of the following options.  
  -  

Choose Branch to specify the branches in your source repository that the trigger monitors in order to know when to start a workflow run. In Include, enter patterns for branch names in glob format that you want to specify for the trigger configuration to start your pipeline on changes in the specified branches. In Exclude, enter the regex patterns for branch names in glob format that you want to specify for the trigger configuration to ignore and to not start your pipeline on changes in the specified branches. See Working with glob patterns in syntax for more information. Note

If the include and exclude both have the same pattern, then the default is to exclude the pattern. 

You can use glob patterns to define your branch names. For example, use `main*` to match all branches beginning with `main`. See Working with glob patterns in syntax for more information. 

For a push trigger, specify the branches you're pushing to, that is, the destination branches. For a pull request trigger, specify destination branches you're opening a pull request to. 
  -  

(Optional) Under File paths, specify file paths for your trigger. Enter the names in Include and Exclude as appropriate. 

You can use glob patterns to define your file path names. For example, use `prod*` to match all file paths beginning with `prod`. See Working with glob patterns in syntax for more information. 
  -  

Choose Pull request to configure the pipeline trigger configuration to start with pull request events that you specify. 
 
 

## Add filters for push and pull request event types (CLI) 

You can update the pipeline JSON to add filters for triggers. 

To use the AWS CLI to create or update your pipeline, use the `create-pipeline` or `update-pipeline` command. 

The following example JSON structure provides a reference for the field definitions under `create-pipeline`. 

For a list of field definitions, see triggers in the Pipeline structure reference in this guide. 

```
{
    "pipeline": {
        "name": "MyServicePipeline",
        "triggers": [
            {
                "provider": "Connection",
                "gitConfiguration": {
                    "sourceActionName": "ApplicationSource",
                    "push": [
                        {
                            "filePaths": {
                                "includes": [
                                    "projectA/**",
                                    "common/**/*.js"
                                ],
                                "excludes": [
                                    "**/README.md",
                                    "**/LICENSE",
                                    "**/CONTRIBUTING.md"
                                ]
                            },
                            "branches": {
                                "includes": [
                                    "feature/**",
                                    "release/**"
                                ],
                                "excludes": [
                                    "mainline"
                                ]
                            },
                            "tags": {
                                "includes": [
                                    "release-v0", "release-v1"
                                ],
                                "excludes": [
                                    "release-v2"
                                ]
                            }
                        }
                    ],
                    "pullRequest": [
                        {
                            "events": [
                                "CLOSED"
                            ],
                            "branches": {
                                "includes": [
                                    "feature/**",
                                    "release/**"
                                ],
                                "excludes": [
                                    "mainline"
                                ]
                            },
                            "filePaths": {
                                "includes": [
                                    "projectA/**",
                                    "common/**/*.js"
                                ],
                                "excludes": [
                                    "**/README.md",
                                    "**/LICENSE",
                                    "**/CONTRIBUTING.md"
                                ]
                            }
                        }
                    ]
                }
            }
        ],
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "ApplicationSource",
                        "configuration": {
                            "BranchName": "mainline",
                            "ConnectionArn": "arn:aws:codestar-connections:eu-central-1:111122223333:connection/fe9ff2e8-ee25-40c9-829e-65f8EXAMPLE",
                            "FullRepositoryId": "monorepo-example",
                            "OutputArtifactFormat": "CODE_ZIP"
                        }
                    }
                ]
            }
        ]
    }
}
```
 

## Add filters for push and pull request event types (CloudFormation templates) 

You can update the pipeline resource in CloudFormation to add trigger filtering. 

The following example template snippet provides a YAML reference for triggers field definitions. For a list of field definitions, see triggers in the Pipeline structure reference in this guide. 

For a full template example for a connection source and trigger filter configuration, see Pipeline with two stages and trigger configuration in the CloudFormation User Guide. 

```
pipeline:
  name: MyServicePipeline
  executionMode: PARALLEL
  triggers:
    - provider: CodeConnection
      gitConfiguration:
        sourceActionName: ApplicationSource
        push:
          - filePaths:
              includes:
                - projectA/**
                - common/**/*.js
              excludes:
                - '**/README.md'
                - '**/LICENSE'
                - '**/CONTRIBUTING.md'
            branches:
              includes:
                - feature/**
                - release/**
              excludes:
                - mainline
          - tags:
              includes:
                - release-v0
                - release-v1
              excludes:
                - release-v2
        pullRequest:
          - events:
              - CLOSED
            branches:
              includes:
                - feature/**
                - release/**
              excludes:
                - mainline
            filePaths:
              includes:
                - projectA/**
                - common/**/*.js
              excludes:
                - '**/README.md'
                - '**/LICENSE'
                - '**/CONTRIBUTING.md'
  stages:
    - name: Source
      actions:
        - name: ApplicationSource
          configuration:
            BranchName: mainline
            ConnectionArn: arn:aws:codestar-connections:eu-central-1:111122223333:connection/fe9ff2e8-ee25-40c9-829e-65f85EXAMPLE
            FullRepositoryId: monorepo-example
            OutputArtifactFormat: CODE_ZIP
```
 

