> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html
> Downloaded: 2026-10-18

# CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions

Source actions for connections are supported by AWS CodeConnections. AWS CodeConnections allows you to create and manage connections between AWS resources and third-party repositories such as GitHub. Starts a pipeline when a new commit is made on a third-party source code repository. The source action retrieves code changes when a pipeline is manually run or when a webhook event is sent from the source provider. 

You can configure actions in your pipeline to use a Git configuration that allows you to start your pipeline with triggers. To configure the pipeline trigger configuration to filter with triggers, see more details in Add trigger with code push or pull request event types.Note

This feature is not available in the Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Osaka), Africa (Cape Town), Middle East (Bahrain), Middle East (UAE), Europe (Spain), Europe (Zurich), Israel (Tel Aviv), or AWS GovCloud (US-West) Regions. To reference other available actions, see Product and service integrations with CodePipeline. For considerations with this action in the Europe (Milan) Region, see the note in CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions.

Connections can associate your AWS resources with the following third-party repositories: 
Bitbucket Cloud (through the Bitbucket provider option in the CodePipeline console or the `Bitbucket` provider in the CLI) Note

You can create connections to a Bitbucket Cloud repository. Installed Bitbucket provider types, such as Bitbucket Server, are not supported.  
-  Note

If you are using a Bitbucket workspace, you must have administrator access to create the connection. 
GitHub and GitHub Enterprise Cloud (through the GitHub (via GitHub App) provider option in the CodePipeline console or the `GitHub` provider in the CLI) Note

If your repository is in a GitHub organization, you must be the organization owner to create the connection. If you are using a repository that is not in an organization, you must be the repository owner. 
GitHub Enterprise Server (through the GitHub Enterprise Server provider option in the CodePipeline console or the `GitHub Enterprise Server` provider in the CLI) 
GitLab.com (through the GitLab provider option in the CodePipeline console or the `GitLab` provider in the CLI) Note

You can create connections to a repository where you have the Owner role in GitLab, and then the connection can be used with the repository with resources such as CodePipeline. For repositories in groups, you do not need to be the group owner. 
Self-managed installation for GitLab (Enterprise Edition or Community Edition) (through the GitLab self-managed provider option in the CodePipeline console or the `GitLabSelfManaged` provider in the CLI) 
Note

Each connection supports all of the repositories you have with that provider. You only need to create a new connection for each provider type.

Connections allow your pipeline to detect source changes through the third-party provider's installation app. For example, webhooks are used to subscribe to GitHub event types and can be installed on an organization, a repository, or a GitHub App. Your connection installs a repository webhook on your GitHub App that subscribes to GitHub push type events.

After a code change is detected, you have the following options for passing the code to subsequent actions: 
Default: Like other existing CodePipeline source actions, `CodeStarSourceConnection` can output a ZIP file with a shallow copy of your commit. 
Full clone: `CodeStarSourceConnection` can also be configured to output a URL reference to the repo for subsequent actions. 

Currently, the Git URL reference can only be used by downstream CodeBuild actions to clone the repo and associated Git metadata. Attempting to pass a Git URL reference to non-CodeBuild actions results in an error. 

CodePipeline prompts you to add the AWS Connector installation app to your third-party account when you create a connection. You must have already created your third-party provider account and repository before you can connect through the `CodeStarSourceConnection` action.Note

To create or attach a policy to your role with the permissions required to use AWS CodeStar connections, see Connections permissions reference. Depending on when your CodePipeline service role was created, you might need to update its permissions to support AWS CodeStar connections. For instructions, see Add permissions to the CodePipeline service role.Note

To use connections in the Europe (Milan) AWS Region, you must:  
Install a Region-specific app 
Enable the Region 

This Region-specific app supports connections in the Europe (Milan) Region. It is published on the third-party provider site, and it is separate from the existing app supporting connections for other Regions. By installing this app, you authorize third-party providers to share your data with the service for this Region only, and you can revoke the permissions at any time by uninstalling the app.

The service will not process or store your data unless you enable the Region. By enabling this Region, you grant our service permissions to process and store your data.

Even if the Region is not enabled, third-party providers can still share your data with our service if the Region-specific app remains installed, so make sure to uninstall the app once you disable the Region. For more information, see  Enabling a Region.Topics
Action type
Configuration parameters
Input artifacts
Output artifacts
Output variables
Service role permissions: AWS CodeConnections action
Action declaration
Installing the installation app and creating a connection
See also
 

## Action type  
Category: `Source` 
Owner: `AWS` 
Provider: `CodeStarSourceConnection` 
Version: `1` 
 

## Configuration parameters   

**ConnectionArn**  

Required: Yes 

The connection ARN that is configured and authenticated for the source provider.  

**FullRepositoryId**  

Required: Yes 

The owner and name of the repository where source changes are to be detected. 

Example: `some-user/my-repo` Important

You must maintain the correct case for the FullRepositoryId value. For example, if your user name is `some-user` and repo name is `My-Repo`, the recommended value of FullRepositoryId is `some-user/My-Repo`.  

**BranchName**  

Required: Yes 

The name of the branch where source changes are to be detected.  

**OutputArtifactFormat**  

Required: No 

Specifies the output artifact format. Can be either `CODEBUILD_CLONE_REF` or `CODE_ZIP`. If unspecified, the default is `CODE_ZIP`. Important

The `CODEBUILD_CLONE_REF` option can only be used by CodeBuild downstream actions.

If you choose this option, you will need to update the permissions for your CodeBuild project service role as shown in Add CodeBuild GitClone permissions for connections to Bitbucket, GitHub, GitHub Enterprise Server, or GitLab.com. For a tutorial that shows you how to use the Full clone option, see Tutorial: Use full clone with a GitHub pipeline source.  

**DetectChanges**  

 Required: No 

Controls automatically starting your pipeline when a new commit is made on the configured repository and branch. If unspecified, the default value is `true`, and the field does not display by default. Valid values for this parameter:  
`true`: CodePipeline automatically starts your pipeline on new commits. 
`false`: CodePipeline does not start your pipeline on new commits. 
   

## Input artifacts  
Number of artifacts: `0` 
Description: Input artifacts do not apply for this action type. 
 

## Output artifacts  
Number of artifacts: `1`  
Description: The artifacts generated from the repository are the output artifacts for the `CodeStarSourceConnection` action. The source code commit ID is displayed in CodePipeline as the source revision for the triggered pipeline execution. You can configure the output artifact of this action in:  
A ZIP file that contains the contents of the configured repository and branch at the commit specified as the source revision for the pipeline execution. 
A JSON file that contains a URL reference to the repository so that downstream actions can perform Git commands directly. Important

This option can only be used by CodeBuild downstream actions.

If you choose this option, you will need to update the permissions for your CodeBuild project service role as shown in Troubleshooting CodePipeline. For a tutorial that shows you how to use the Full clone option, see Tutorial: Use full clone with a GitHub pipeline source. 
 
 

## Output variables 

When configured, this action produces variables that can be referenced by the action configuration of a downstream action in the pipeline. This action produces variables which can be viewed as output variables, even if the action doesn't have a namespace. You configure an action with a namespace to make those variables available to the configuration of downstream actions. 

For more information, see Variables reference.   

**AuthorDate**  

The date when the commit was authored, in timestamp format.  

**BranchName**  

The name of the branch for the repository where the source change was made.  

**CommitId**  

The commit ID that triggered the pipeline execution.  

**CommitMessage**  

The description message, if any, associated with the commit that triggered the pipeline execution.  

**ConnectionArn**  

The connection ARN that is configured and authenticated for the source provider.  

**FullRepositoryName**  

The name of the repository where the commit that triggered the pipeline was made.   

## Service role permissions: AWS CodeConnections action 

For AWS CodeConnections, the following permission is required to create pipelines with a source that uses a connection, such as Bitbucket Cloud. 

```
{
    "Effect": "Allow",
    "Action": [
        "codeconnections:UseConnection",
        "codestar-connections:UseConnection"
    ],
    "Resource": "resource_ARN"
},
```
 Note

Both actions are required. Operations invoked through call `codestar-connections:UseConnection`, while operations invoked outside of call `codeconnections:UseConnection`. Granting both actions ensures the role works for both code paths, regardless of whether the connection's resource ARN uses the `codeconnections` or `codestar-connections` service prefix. 

For more information about the IAM permissions for connections, see Connections permissions reference. 

## Action declaration 

In the following example, the output artifact is set to the default ZIP format of `CODE_ZIP` for the connection with ARN `arn:aws:codestar-connections:region:`account-id`:connection/`connection-id``.  

**YAML** 

```
Name: Source
Actions:
  - InputArtifacts: []
    ActionTypeId:
      Version: '1'
      Owner: AWS
      Category: Source
      Provider: CodeStarSourceConnection
    OutputArtifacts:
      - Name: SourceArtifact
    RunOrder: 1
    Configuration:
      ConnectionArn: "arn:aws:codestar-connections:region:account-id:connection/connection-id"
      FullRepositoryId: "some-user/my-repo"
      BranchName: "main"
      OutputArtifactFormat: "CODE_ZIP"
    Name: ApplicationSource

```
  

**JSON** 

```
{
    "Name": "Source",
    "Actions": [
        {
            "InputArtifacts": [],
            "ActionTypeId": {
                "Version": "1",
                "Owner": "AWS",
                "Category": "Source",
                "Provider": "CodeStarSourceConnection"
            },
            "OutputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "RunOrder": 1,
            "Configuration": {
                "ConnectionArn": "arn:aws:codestar-connections:region:account-id:connection/connection-id",
                "FullRepositoryId": "some-user/my-repo",
                "BranchName": "main",
                "OutputArtifactFormat": "CODE_ZIP"
            },
            "Name": "ApplicationSource"
        }
    ]
},
```
   

## Installing the installation app and creating a connection 

The first time you use the console to add a new connection to a third-party repository, you must authorize CodePipeline access to your repositories. You choose or create an installation app that helps you connect to the account where you have created your third-party code repository. 

 When you use the AWS CLI or an CloudFormation template, you must provide the connection ARN of a connection that has already gone through the installation handshake. Otherwise, the pipeline is not triggered.  Note

For a `CodeStarSourceConnection` source action, you do not have to set up a webhook or default to polling. The connections action manages your source change detection for you. 

## See also 

The following related resources can help you as you work with this action.  
AWS::CodeStarConnections::Connection – The CloudFormation template reference for the AWS CodeStar Connections resource provides parameters and examples for connections in CloudFormation templates. 
AWS CodeStar Connections API Reference – The AWS CodeStar Connections API Reference provides reference information for the available connections actions. 
To view the steps for creating a pipeline with source actions supported by connections, see the following:  
For Bitbucket Cloud, use the Bitbucket option in the console or the `CodestarSourceConnection` action in the CLI. See Bitbucket Cloud connections. 
For GitHub and GitHub Enterprise Cloud, use the GitHub provider option in the console or the `CodestarSourceConnection` action in the CLI. See GitHub connections. 
For GitHub Enterprise Server, use the GitHub Enterprise Server provider option in the console or the `CodestarSourceConnection` action in the CLI. See GitHub Enterprise Server connections. 
For GitLab.com, use the GitLab provider option in the console or the `CodestarSourceConnection` action with the `GitLab` provider in the CLI. See GitLab.com connections. 
To view a Getting Started tutorial that creates a pipeline with a Bitbucket source and a CodeBuild action, see Getting started with connections. 
For a tutorial that shows you how to connect to a GitHub repository and use the Full clone option with a downstream CodeBuild action, see Tutorial: Use full clone with a GitHub pipeline source.
