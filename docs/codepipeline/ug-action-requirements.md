> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html
> Downloaded: 2026-10-19

# Action declaration

The action level of a pipeline has a basic structure that includes the following parameters and syntax. For more information, see the ActionDeclaration object in the CodePipeline API Guide.

The following example shows the action level of the pipeline structure in both JSON and YAML. 

**YAML** 

```
 
. . . 

  stages:
    - name: Source
      actions:
        - name: Source
          actionTypeId:
            category: Source
            owner: AWS
            provider: S3
            version: '1'
          runOrder: 1
          configuration:
            PollForSourceChanges: 'false'
            S3Bucket: amzn-s3-demo-bucket
            S3ObjectKey: codedeploy_linux.zip
          outputArtifacts:
            - name: SourceArtifact
          inputArtifacts: []
          region: us-west-2
          namespace: SourceVariables
    - name: Build
      actions:
        - name: Build
          actionTypeId:
            category: Build
            owner: AWS
            provider: CodeBuild
            version: '1'
          runOrder: 1
          configuration:
            EnvironmentVariables: >-
              [{"name":"ETag","value":"#{SourceVariables.ETag}","type":"PLAINTEXT"}]
            ProjectName: my-project
          outputArtifacts:
            - name: BuildArtifact
          inputArtifacts:
            - name: SourceArtifact
          region: us-west-2
          namespace: BuildVariables
          runOrder: 1
          configuration:
            CustomData: >-
              Here are the exported variables from the build action: S3 ETAG:
              #{BuildVariables.ETag}
          outputArtifacts: []
          inputArtifacts: []
          region: us-west-2

```
  

**JSON** 

```
 
. . . 

        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "S3",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "PollForSourceChanges": "false",
                            "S3Bucket": "amzn-s3-demo-bucket",
                            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                        },
                        "outputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "inputArtifacts": [],
                        "region": "us-west-2",
                        "namespace": "SourceVariables"
                    }
                ]
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "Build",
                        "actionTypeId": {
                            "category": "Build",
                            "owner": "AWS",
                            "provider": "CodeBuild",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "EnvironmentVariables": "[{\"name\":\"ETag\",\"value\":\"#{SourceVariables.ETag}\",\"type\":\"PLAINTEXT\"}]",
                            "ProjectName": "my-build-project"
                        },
                        "outputArtifacts": [
                            {
                                "name": "BuildArtifact"
                            }
                        ],
                        "inputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "region": "us-west-2",
                        "namespace": "BuildVariables"
                    }
                ]
      
. . . 
```
  

For a list of example `configuration` details appropriate to the provider type, see Valid configuration parameters for each provider type.

The action structure has the following requirements: 
All action names within a stage must be unique. 
A source action is required for each pipeline. 
Source actions that do not use a connection can be configured for change detection or to turn off change detection. See Change Detection Methods. 
This is true for all actions, whether they are in the same stage or in following stages, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifact bundles, which are, in turn, consumed by different following actions. 
When you use an Amazon S3 bucket as a deployment location, you also specify an object key. An object key can be a file name (object) or a combination of a prefix (folder path) and file name. You can use variables to specify the location name you want the pipeline to use. Amazon S3 deployment actions support the use of the following variables in Amazon S3 object keys. Using variables in Amazon S3 
|  Variable |  Example of console input |  Output |    
|  datetime |  js-application/{datetime}.zip |  UTC timestamp in this format: <YYYY>-<MM>-DD>_<HH>-<MM>-<SS>

Example:

js-application/2019-01-10_07-39-57.zip |   
|  uuid |  js-application/{uuid}.zip |  The UUID is a globally unique identifier that is guaranteed to be different from any other identifier. The UUID is in this format (all digits in hexadecimal format): <8-digits>-<4-digits>-4-digits>-<4-digits>-<12-digits>

Example:

js-application/54a60075-b96a-4bf3-9013-db3a9EXAMPLE.zip |    
 

## `name` 

The name of the action. 

## `region` 

For actions where the provider is an AWS service, the AWS Region of the resource. 

Cross-Region actions use the `Region` field to designate the AWS Region where the actions are to be created. The AWS resources created for this action must be created in the same Region provided in the `region` field. You cannot create cross-Region actions for the following action types:  
Source actions 
Actions by third-party providers 
Actions by custom providers 
 

## `roleArn` 

The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn that is specified at the pipeline level. 

## `namespace` 

Actions can be configured with variables. You use the `namespace` field to set the namespace and variable information for execution variables. For reference information about execution variables and action output variables, see Variables reference. Note

For Amazon ECR, Amazon S3, or CodeCommit sources, you can also create a source override using input transform entry to use the `revisionValue` in EventBridge for your pipeline event, where the `revisionValue` is derived from the source event variable for your object key, commit, or image ID. For more information, see the optional step for input transform entry included in the procedures under Amazon ECR source actions and EventBridge resources, Connecting to Amazon S3 source actions with a source enabled for events, or CodeCommit source actions and EventBridge. 

## `actionTypeId` 

The action type ID is identified as a combination of the following four fields. 

### `category` 

The type of action, or step, in the pipeline, such as a source action. Each action type has a specific set of valid action providers. For a list of valid providers by action type, see the Action structure reference. 

These are the valid `actionTypeId` categories (action types) for CodePipeline:  
`Source` 
`Build` 
`Approval` 
`Deploy` 
`Test` 
`Invoke` 
`Compute` 
 

### `owner` 

For all currently supported action types, the only valid owner string is `AWS`, `ThirdParty`, or `Custom`. For the valid owner string for a specific action, see the Action structure reference. 

For more information, see the CodePipeline API Reference. 

### `version` 

The version of the action. 

### `provider` 

The action provider, such as CodeBuild.  
Valid provider types for an action category depend on the category. For example, for a source action category, a valid provider type is `S3`, `CodeStarSourceConnection`, `CodeCommit`, or `Amazon ECR`. This example shows the structure for a source action with an `S3` provider: 

```
"actionTypeId": {
  "category": "Source",
  "owner": "AWS",
  "version": "1",
  "provider": "S3"},
```
 
 

## `InputArtifacts` 

This field contains the input artifact structure, if supported for the action category. The input artifact of an action must exactly match the output artifact declared in a preceding action. For example, if a preceding action includes the following declaration:  

```
"outputArtifacts": [
    {
    "MyApp"
    }
],
```
 

 and there are no other output artifacts, then the input artifact of a following action must be:  

```
"inputArtifacts": [
    {
    "MyApp"
    }
],
```
 

For example, a source action cannot have input artifacts because it is the first action in the pipeline. However, a source action will always have output artifacts that are processed by the following action. The output artifacts for a source action are the application files from the source repository, zipped and provided through the artifact bucket, that are processed by the following action, such as a CodeBuild action that acts on the application files with build commands. 

As an example of actions that cannot have output artifacts, deploy actions do not have output artifacts because these actions are generally the last action in a pipeline. 

### `name` 

The artifact name for the action's input artifacts. 

## `outputArtifacts` 

Output artifact names must be unique in a pipeline. For example, a pipeline can include one action that has an output artifact named `"MyApp"` and another action that has an output artifact named `"MyBuiltApp"`. However, a pipeline cannot include two actions that both have an output artifact named `"MyApp"`. 

 This field contains the output artifact structure, if supported for the action category. The output artifact of an action must exactly match the output artifact declared in a preceding action. For example, if a preceding action includes the following declaration:  

```
"outputArtifacts": [
    {
    "MyApp"
    }
],
```
 

 and there are no other output artifacts, then the input artifact of a following action must be:  

```
"inputArtifacts": [
    {
    "MyApp"
    }
],
```
 

For example, a source action cannot have input artifacts because it is the first action in the pipeline. However, a source action will always have output artifacts that are processed by the following action. The output artifacts for a source action are the application files from the source repository, zipped and provided through the artifact bucket, that are processed by the following action, such as a CodeBuild action that acts on the application files with build commands. 

As an example of actions that cannot have output artifacts, deploy actions do not have output artifacts because these actions are generally the last action in a pipeline. 

### `name` 

The artifact name for the action's output artifacts. 

## `configuration` (by action provider) 

The action configuration contains details and parameters appropriate to the provider type. In the section below, the example action configuration parameters are specific to the S3 source action. 

The action configuration and input/output artifact limits can vary by action provider. For a list of action configuration examples by action provider, see Action structure reference and the table in Valid configuration parameters for each provider type. The table provides a link to the action reference for each provider type, which lists the configuration parameters for each action in detail. For a table with the input and output artifact limits for each action provider, see Valid input and output artifacts for each action type. 

The following considerations apply to working with actions:  
Source actions do not have input artifacts, and deploy actions do not have output artifacts. 
For source action providers that do not use a connection, such as S3, you must use the `PollForSourceChanges` parameter to specify whether you want your pipeline to start automatically when a change is detected. See Valid settings for the PollForSourceChanges parameter. 
To configure automated change detection to start your pipeline, or to disable change detection, see Source actions and change detection methods. 
To configure triggers with filtering, use the source action for connections, and then see Automate starting pipelines using triggers and filtering. 
For the output variables for each action, see Variables reference. Note

For Amazon ECR, Amazon S3, or CodeCommit sources, you can also create a source override using input transform entry to use the `revisionValue` in EventBridge for your pipeline event, where the `revisionValue` is derived from the source event variable for your object key, commit, or image ID. For more information, see the optional step for input transform entry included in the procedures under Amazon ECR source actions and EventBridge resources, Connecting to Amazon S3 source actions with a source enabled for events, or CodeCommit source actions and EventBridge. Important

Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline. For more information, see pollingDisabledAt in the pipeline structure reference. For the steps to migrate your pipeline from polling to event-based change detection, see Change Detection Methods. 
 Note

The CodeCommit and S3 source actions require either a configured change detection resource (an EventBridge rule) or use the option to poll the repository for source changes. For pipelines with a Bitbucket, GitHub, or GitHub Enterprise Server source action, you do not have to set up a webhook or default to polling. The connections action manages change detection for you.  

## `runOrder` 

A positive integer that indicates the run order of the action within the stage. Parallel actions in the stage are shown as having the same integer. For example, two actions with a run order of two will run in parallel after the first action in the stage runs. 

The default `runOrder` value for an action is 1. The value must be a positive integer (natural number). You cannot use fractions, decimals, negative numbers, or zero. To specify a serial sequence of actions, use the smallest number for the first action and larger numbers for each of the rest of the actions in sequence. To specify parallel actions, use the same integer for each action you want to run in parallel. In the console, you can specify a serial sequence for an action by choosing Add action group at the level in the stage where you want it to run, or you can specify a parallel sequence by choosing Add action. Action group refers to a run order of one or more actions at the same level. 

For example, if you want three actions to run in sequence in a stage, you would give the first action the `runOrder` value of 1, the second action the `runOrder` value of 2, and the third the `runOrder` value of 3. However, if you want the second and third actions to run in parallel, you would give the first action the `runOrder` value of 1 and both the second and third actions the `runOrder` value of 2. Note

The numbering of serial actions does not have to be in strict sequence. For example, if you have three actions in a sequence and decide to remove the second action, you do not need to renumber the `runOrder` value of the third action. Because the `runOrder` value of that action (3) is higher than the `runOrder` value of the first action (1), it runs serially after the first action in the stage.
