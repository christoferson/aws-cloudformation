> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-requirements.html
> Downloaded: 2026-10-18

# Pipeline declaration

The pipeline and metadata level of a pipeline has a basic structure that includes the following parameters and syntax. The pipeline parameter represents the structure of actions and stages to be performed in the pipeline. 

For more information, see the PipelineDeclaration object in the CodePipeline API Guide.

The following example shows the pipeline and metadata level of the pipeline structure in both JSON and YAML for a V2 type pipeline. 

**YAML** 

```
pipeline:
  name: MyPipeline
  roleArn: >-
    arn:aws:iam::ACCOUNT_ID:role/service-role/AWSCodePipelineServiceRole-us-west-2-MyPipeline
  artifactStore:
    type: S3
    location: amzn-s3-demo-bucket
  stages:
    ...
  version: 6
  executionMode: SUPERSEDED
  pipelineType: V2
  variables:
  - name: MyVariable
    defaultValue: '1'
  triggers:
  - providerType: CodeStarSourceConnection
    gitConfiguration:
      sourceActionName: Source
      push:
      - branches:
          includes:
          - main
          excludes:
          - feature-branch
      pullRequest:
      - events:
        - CLOSED
        branches:
          includes:
          - main*
metadata:
  pipelineArn: 'arn:aws:codepipeline:us-west-2:ACCOUNT_ID:MyPipeline'
  created: '2019-12-12T06:49:02.733000+00:00'
  updated: '2020-09-10T06:34:07.447000+00:00'
  pollingDisabledAt: '2020-09-10T06:34:07.447000+00:00'
```
  

**JSON** 

```
{
    "pipeline": {
        "name": "MyPipeline",
        "roleArn": "arn:aws:iam::ACCOUNT_ID:role/service-role/AWSCodePipelineServiceRole-us-west-2-MyPipeline",
        "artifactStore": {
            "type": "S3",
            "location": "amzn-s3-demo-bucket"
        },
        "stages": {
            ...   
    },
        "version": 6,
        "executionMode": "SUPERSEDED",
                "pipelineType": "V2",
        "variables": [
            {
                "name": "MyVariable",
                "defaultValue": "1"
            }
        ],
        "triggers": [
            {
                "providerType": "CodeStarSourceConnection",
                "gitConfiguration": {
                    "sourceActionName": "Source",
                    "push": [
                        {
                            "branches": {
                                "includes": [
                                    "main"
                                ],
                                "excludes": [
                                    "feature-branch"
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
                                    "main*"
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    },
    "metadata": {
        "pipelineArn": "arn:aws:codepipeline:us-west-2:ACCOUNT_ID:MyPipeline",
        "created": "2019-12-12T06:49:02.733000+00:00",
        "updated": "2020-09-10T06:34:07.447000+00:00",
        "pollingDisabledAt": "2020-09-10T06:34:07.447000+00:00"
    }
}
```
   

## `name` 

The name of the pipeline. When you edit or update a pipeline, the pipeline name cannot be changed. Note

If you want to rename an existing pipeline, you can use the CLI `get-pipeline` command to build a JSON file that contains your pipeline's structure. You can then use the CLI `create-pipeline` command to create a pipeline with that structure and give it a new name. 

## `roleArn` 

The IAM ARN for the CodePipeline service role, such as arn:aws:iam::80398EXAMPLE:role/CodePipeline_Service_Role. 

To use the console to view the pipeline service role ARN instead of the JSON structure, choose your pipeline in the console, and then choose Settings. Under the General tab, the Service role ARN field displays. 

## `artifactStore` OR `artifactStores` 

The `artifactStore` field contains the artifact bucket type and location for a pipeline with all actions in the same AWS Region. If you add actions in a Region different from your pipeline, the `artifactStores` mapping is used to list the artifact bucket for each AWS Region where actions are executed. When you create or edit a pipeline, you must have an artifact bucket in the pipeline Region and then you must have one artifact bucket per Region where you plan to execute an action.  Note

In the pipeline structure, you must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`. 

The following example shows the basic structure for a pipeline with cross-Region actions that uses the `artifactStores` parameter:  

```
    "pipeline": {
        "name": "YourPipelineName",
        "roleArn": "CodePipeline_Service_Role",
        "artifactStores": {
            "us-east-1": {
                "type": "S3",
                "location": "S3 artifact bucket name, such as amzn-s3-demo-bucket"
            },
            "us-west-2": {
                "type": "S3",
                "location": "S3 artifact bucket name, such as amzn-s3-demo-bucket"
            }
        },
        "stages": [
            {

...
```
 

### `type` 

The location type for the artifact bucket, specified as Amazon S3. 

### `location` 

The name of the Amazon S3 bucket automatically generated for you the first time you create a pipeline using the console, such as codepipeline-us-east-2-1234567890, or any Amazon S3 bucket you provision for this purpose 

## `stages` 

This parameter contains the name of each stage in the pipeline. For more information about the parameters and syntax at the stage level of the pipeline structure, see the StageDeclaration object in the  CodePipeline API Guide. 

The pipeline structure for stages has the following requirements:  
A pipeline must contain at least two stages. 
The first stage of a pipeline must contain at least one source action. It can contain source actions only. 
Only the first stage of a pipeline can contain source actions. 
At least one stage in each pipeline must contain an action that is not a source action. 
All stage names in a pipeline must be unique. 
Stage names cannot be edited in the CodePipeline console. If you edit a stage name by using the AWS CLI, and the stage contains an action with one or more secret parameters (such as an OAuth token), the value of those secret parameters is not preserved. You must manually enter the value of the parameters (which are masked by four asterisks in the JSON returned by the AWS CLI) and include them in the JSON structure. 
 Important

Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline. For more information, see pollingDisabledAt in the pipeline structure reference. For the steps to migrate your pipeline from polling to event-based change detection, see Change Detection Methods. 

## `version` 

The version number of a pipeline is automatically generated and updated every time you update the pipeline. 

## `executionMode` 

You can set the pipeline execution mode so that you can specify the pipeline behavior for consecutive runs, such as queueing, superseding, or running in parallel mode. For more information, see Set or change the pipeline execution mode. Important

For pipelines in PARALLEL mode, stage rollback is not available. Similarly, failure conditions with a rollback result type cannot be added to a PARALLEL mode pipeline. 

## `pipelineType` 

The pipeline type specifies the available structure and features in the pipeline, such as for a V2 type pipeline. For more information, see Pipeline types. 

## `variables` 

Variables at the pipeline level are defined when the pipeline is created and resolved at pipeline run time. For more information, see Variables reference. For a tutorial with a pipeline-level variable that is passed at the time of the pipeline execution, see Tutorial: Use pipeline-level variables. 

## `triggers` 

Triggers allow you to configure your pipeline to start on a particular event type or filtered event type, such as when a change on a particular branch or pull request is detected. Triggers are configurable for source actions with connections that use the `CodeStarSourceConnection` action in CodePipeline, such as GitHub, Bitbucket, and GitLab. For more information about source actions that use connections, see Add third-party source providers to pipelines using AWS CodeConnections. 

For more information and more detailed examples, see Automate starting pipelines using triggers and filtering. 

For filtering, regular expression patterns in glob format are supported as detailed in Working with glob patterns in syntax. Note

The CodeCommit and S3 source actions require either a configured change detection resource (an EventBridge rule) or use the option to poll the repository for source changes. For pipelines with a Bitbucket, GitHub, or GitHub Enterprise Server source action, you do not have to set up a webhook or default to polling. The connections action manages change detection for you.  Important

Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline. For more information, see pollingDisabledAt in the pipeline structure reference. For the steps to migrate your pipeline from polling to event-based change detection, see Change Detection Methods. 

### `gitConfiguration` fields 

The Git configuration for the trigger, including the event types and any parameters for filtering by branches, file paths, tags, or pull request events.  

The fields in the JSON structure are defined as follows:  
`sourceActionName`: The name of the pipeline source action with the Git configuration. 
`push`: Push events with filtering. These events use an OR operation between different push filters and an AND operation inside filters.  
`branches`: The branches to filter on. Branches use an AND operation between includes and excludes.   
`includes`: Patterns to filter on for branches that will be included. Includes use an OR operation. 
`excludes`: Patterns to filter on for branches that will be excluded. Excludes use an OR operation. 
`filePaths`: The file path names to filter on.   
`includes`: Patterns to filter on for file paths that will be included. Includes use an OR operation. 
`excludes`: Patterns to filter on for file paths that will be excluded. Excludes use an OR operation. 
`tags`: The tag names to filter on.  
`includes`: Patterns to filter on for tags that will be included. Includes use an OR operation. 
`excludes`: Patterns to filter on for tags that will be excluded. Excludes use an OR operation. 
`pullRequest`: Pull request events with filtering on pull request events and pull request filters.  
`events`: Filters on open, updated, or closed pull request events as specified. 
`branches`: The branches to filter on. Branches use an AND operation between includes and excludes.   
`includes`: Patterns to filter on for branches that will be included. Includes use an OR operation. 
`excludes`: Patterns to filter on for branches that will be excluded. Excludes use an OR operation. 
`filePaths`: The file path names to filter on.   
`includes`: Patterns to filter on for file paths that will be included. Includes use an OR operation. 
`excludes`: Patterns to filter on for file paths that will be excluded. Excludes use an OR operation. 
 
 
 

The following is an example of the trigger configuration for push and pull request event types. 

```
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
```
 

### Event type `push` fields for include and exclude 

Include and exclude behavior for levels of Git configuration fields for push event types are shown in the following list: 

```
push (OR operation is used between push and pullRequest or multiples)
    filePaths (AND operation is used between filePaths, branches, and tags)
        includes (AND operation is used between includes and excludes)
            **/FILE.md, **/FILE2 (OR operation is used between file path names)
        excludes (AND operation is used between includes and excludes)
            **/FILE.md, **/FILE2 (OR operation is used between file path names)
    branches (AND operation is used between filePaths, branches, and tags)
        includes (AND operation is used between includes and excludes)
            BRANCH/**", "BRANCH2/** (OR operation is used between branch names)
        excludes (AND operation is used between includes and excludes)
            BRANCH/**", "BRANCH2/** (OR operation is used between branch names)
    tags (AND operation is used between filePaths, branches, and tags)        
         includes (AND operation is used between includes and excludes)
            TAG/**", "TAG2/** (OR operation is used between tag names)
         excludes (AND operation is used between includes and excludes)
            TAG/**", "TAG2/** (OR operation is used between tag names)
```
 

### Event type `pull request` fields for include and exclude 

Include and exclude behavior for levels of Git configuration fields for pull request event types are shown in the following list: 

```
pullRequest (OR operation is used between push and pullRequest or multiples)
    events (AND operation is used between events, filePaths, and branches). Includes/excludes are N/A for pull request events.
    filePaths (AND operation is used between events, filePaths, and branches)
        includes (AND operation is used between includes and excludes)
            **/FILE.md, **/FILE2 (OR operation is used between file path names)
        excludes (AND operation is used between includes and excludes)
            **/FILE.md, **/FILE2 (OR operation is used between file path names)
    branches (AND operation is used between events, filePaths, and branches)
        includes (AND operation is used between includes and excludes)
            BRANCH/**", "BRANCH2/** (OR operation is used between branch names)
        excludes (AND operation is used between includes and excludes)
            BRANCH/**", "BRANCH2/** (OR operation is used between branch names)
```
 

## `metadata` 

The pipeline metadata fields are distinct from the pipeline structure and cannot be edited. When you update a pipeline, the date in the `updated` metadata field changes automatically. 

### `pipelineArn` 

The Amazon Resource Name (ARN) of the pipeline. 

To use the console to view the pipeline ARN instead of the JSON structure, choose your pipeline in the console, and then choose Settings. Under the General tab, the Pipeline ARN field displays. 

### `created` 

The date and time when the pipeline was created. 

### `updated` 

The date and time when the pipeline was last updated. 

### `pollingDisabledAt` 

The date and time when, for a pipeline that is configured for polling for change detection, when polling was disabled. 

Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline.  
Inactive pipelines will have polling disabled after 30 days of no executions. 
Pipelines using EventBridge, CodeStar Connections, or webhooks will not be affected. 
Active pipelines will not be affected. 
 

For more information, see the `pollingDisabledAt` parameter under PipelineMetadata object in the  CodePipeline API Guide. For the steps to migrate your pipeline from polling to event-based change detection, see Change Detection Methods.
