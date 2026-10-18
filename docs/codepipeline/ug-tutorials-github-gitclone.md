> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-github-gitclone.html
> Downloaded: 2026-10-18

# Tutorial: Use full clone with a GitHub pipeline source

You can choose the full clone option for your GitHub source action in CodePipeline. Use this option to run CodeBuild commands for Git metadata in your pipeline build action.Note

The full clone option described here refers to specifying whether CodePipeline should clone repository metadata, which can only be used by CodeBuild commands. To use a GitHub  user access token for use with CodeBuild projects, follow the steps here to install the AWS Connector for GitHub app and then leave the App installation field empty. AWS CodeConnections will use the user access token for the connection.

Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.) If the S3 artifact bucket is in a different account from the account for your pipeline, make sure that the S3 artifact bucket is owned by AWS accounts that are safe and will be dependable.

In this tutorial, you will create a pipeline that connects to your GitHub repository, uses the full clone option for source data, and runs a CodeBuild build that clones your repository and performs Git commands for the repository.Note

This feature is not available in the Asia Pacific (Hong Kong), Africa (Cape Town), Middle East (Bahrain), Europe (Zurich), or AWS GovCloud (US-West) Regions. To reference other available actions, see Product and service integrations with CodePipeline. For considerations with this action in the Europe (Milan) Region, see the note in CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions.Topics
Prerequisites
Step 1: Create a README file
Step 2: Create your pipeline and build project
Step 3: Update the CodeBuild service role policy to use connections
Step 4: View repository commands in build output
 

## Prerequisites 

Before you begin, you must do the following:  
Create a GitHub repository with your GitHub account. 
Have your GitHub credentials ready. When you use the AWS Management Console to set up a connection, you are asked to sign in with your GitHub credentials.  
 

## Step 1: Create a README file 

After you create your GitHub repository, use these steps to add a README file. 
Log in to your GitHub repository and choose your repository. 
To create a new file, choose Add file > Create new file. Name the file `README.md` and add the following text. 

```
This is a GitHub repository!
```
Choose Commit changes. 

Make sure the `README.md` file is at the root level of your repository. 
 

## Step 2: Create your pipeline and build project 

In this section, you create a pipeline with the following actions:  
A source stage with a connection to your GitHub repository and action. 
A build stage with an AWS CodeBuild build action. 
 To create a pipeline with the wizard
Sign in to the CodePipeline console at https://console.aws.amazon.com/codepipeline/. 
On the Welcome page, Getting started page, or Pipelines page, choose Create pipeline. 
On the Step 1: Choose creation option page, under Creation options, choose the Build custom pipeline option. Choose Next. 
In Step 2: Choose pipeline settings, in Pipeline name, enter `MyGitHubPipeline`. 
In Pipeline type, choose V1 for the purposes of this tutorial. You can also choose V2; however, note that pipeline types differ in characteristics and price. For more information, see Pipeline types. 
In Service role, choose New service role. Note

If you choose instead to use your existing CodePipeline service role, make sure that you have added the `codestar-connections:UseConnection` IAM permission to your service role policy. For instructions for the CodePipeline service role, see Add permissions to the CodePipeline service role. 
Under Advanced settings, leave the defaults. In Artifact store, choose Default location to use the default artifact store, such as the Amazon S3 artifact bucket designated as the default, for your pipeline in the Region you selected for your pipeline. Note

This is not the source bucket for your source code. This is the artifact store for your pipeline. A separate artifact store, such as an S3 bucket, is required for each pipeline. 

Choose Next. 
On the Step 3: Add source stage page, add a source stage: 
In Source provider, choose GitHub (via GitHub App). 
Under Connection, choose an existing connection or create a new one. To create or manage a connection for your GitHub source action, see GitHub connections.  

You install one app for all of your connections to a particular provider. If you have already installed the AWS Connector for GitHub app, choose it and skip this step. Note

If you want to create a  user access token, make sure that you've already installed the AWS Connector for GitHub app and then leave the App installation field empty. AWS CodeConnections will use the user access token for the connection. For more information, see Access your source provider in CodeBuild. 
In Repository name, choose the name of your GitHub repository. 
In Branch name, choose the repository branch you want to use. 
Make sure the Start the pipeline on source code change option is selected. 
Under Output artifact format, choose Full clone to enable the Git clone option for the source repository. Only actions provided by CodeBuild can use the Git clone option. You will use Step 3: Update the CodeBuild service role policy to use connections in this tutorial to update the permissions for your CodeBuild project service role to use this option. 
 

Choose Next. 
In Step 4: Add build stage, add a build stage: 
In Build provider, choose AWS CodeBuild. Allow Region to default to the pipeline Region. 
Choose Create project. 
In Project name, enter a name for this build project. 
In Environment image, choose Managed image. For Operating system, choose Ubuntu. 
For Runtime, choose Standard. For Image, choose aws/codebuild/standard:5.0. 
For Service role, choose New service role. Note

Note the name of your CodeBuild service role. You will need the role name for the final step in this tutorial. 
Under Buildspec, for Build specifications, choose Insert build commands. Choose Switch to editor, and paste the following under Build commands. Note

In the `env` section of the build spec, make sure the credential helper for git commands is enabled as shown in this example. 

```
version: 0.2

env:
  git-credential-helper: yes
phases:
  install:
    #If you use the Ubuntu standard image 2.0 or later, you must specify runtime-versions.
    #If you specify runtime-versions and use an image other than Ubuntu standard image 2.0, the build fails.
    runtime-versions:
      nodejs: 12
      # name: version
    #commands:
      # - command
      # - command
  pre_build:
    commands:
      - ls -lt
      - cat README.md
  build:
    commands:
      - git log | head -100
      - git status
      - ls
      - git archive --format=zip HEAD > application.zip
  #post_build:
    #commands:
      # - command
      # - command
artifacts:
  files:
    - application.zip
    # - location
  #name: $(date +%Y-%m-%d)
  #discard-paths: yes
  #base-directory: location
#cache:
  #paths:
    # - paths
```
Choose Continue to CodePipeline. This returns to the CodePipeline console and creates a CodeBuild project that uses your build commands for configuration. The build project uses a service role to manage AWS service permissions. This step might take a couple of minutes. 
Choose Next. 
In Step 5: Add test stage, choose Skip test stage, and then accept the warning message by choosing Skip again.  

Choose Next. 
On the Step 6: Add deploy stage page, choose Skip deploy stage, and then accept the warning message by choosing Skip again. Choose Next. 
On Step 7: Review, choose Create pipeline. 
 

## Step 3: Update the CodeBuild service role policy to use connections 

The initial pipeline run will fail because the CodeBuild service role must be updated with permissions to use connections. Add the `codestar-connections:UseConnection` IAM permission to your service role policy. For instructions to update the policy in the IAM console, see Add CodeBuild GitClone permissions for connections to Bitbucket, GitHub, GitHub Enterprise Server, or GitLab.com. 

## Step 4: View repository commands in build output 
When your service role is successfully updated, choose Retry on the failed CodeBuild stage. 
After the pipeline runs successfully, on your successful build stage, choose View details. 

On the details page, choose the Logs tab. View the CodeBuild build output. The commands output the value of the entered variable. 

The commands output the `README.md` file contents, list the files in the directory, clone the repository, view the log, and archive the repository as a ZIP file.
