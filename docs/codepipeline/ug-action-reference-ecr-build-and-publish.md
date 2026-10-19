> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECRBuildAndPublish.html
> Downloaded: 2026-10-18

# `ECRBuildAndPublish` build action reference

This build action allows you to automate building and pushing a new image when a change occurs in your source. This action builds based on a specified Dockerfile location and pushes the image. This build action is not the same as the Amazon ECR source action in CodePipeline, which triggers pipeline when a change occurs in your Amazon ECR source repository. For information about that action, see Amazon ECR source action reference.

This is not a source action that will trigger the pipeline. This action builds an image and pushes it to your Amazon ECR image repository.

You must have already created an Amazon ECR repository and have added a Dockerfile to your source code repository, such as GitHub, before you add the action to your pipeline.Important

This action uses CodePipeline managed CodeBuild compute to run commands in a build environment. Running the commands action will incur separate charges in AWS CodeBuild.Note

This action is only available for V2 type pipelines.Topics
Action type
Configuration parameters
Input artifacts
Output artifacts
Output variables
Service role permissions: ECRBuildAndPublish action
Action declaration
See also
 

## Action type  
Category: `Build` 
Owner: `AWS` 
Provider: `ECRBuildAndPublish` 
Version: `1` 
 

## Configuration parameters   

**ECRRepositoryName**  

Required: Yes 

The name of the Amazon ECR repository where the image is pushed.  

**DockerFilePath**  

Required: No 

The location of the Dockerfile used to build the image. Optionally, you can provide an alternate Dockerfile location if not at the root level. Note

If a value for `DockerFilePath` is not specified, the value defaults to the source repository root level.  

**ImageTags**  

Required: No 

The tags used for the image. You can enter multiple tags as a comma-delimited list of strings. Note

If a value for `ImageTags` is not specified, the value defaults to `latest`.  

**RegistryType**  

Required: No 

Specifies whether the repository is public or private. Valid values are `private | public`. Note

If a value for `RegistryType` is not specified, the value defaults to `private`.   

## Input artifacts  
Number of artifacts: `1` 
Description: The artifact produced by the source action that contains the Dockerfile needed to build the image. 
 

## Output artifacts  
Number of artifacts: `0`  
 

## Output variables 

When configured, this action produces variables that can be referenced by the action configuration of a downstream action in the pipeline. This action produces variables which can be viewed as output variables, even if the action doesn't have a namespace. You configure an action with a namespace to make those variables available to the configuration of downstream actions.  

For more information, see Variables reference.   

**ECRImageDigestId **  

The `sha256` digest of the image manifest.  

**ECRRepositoryName **  

The name of the Amazon ECR repository where the image was pushed.   

## Service role permissions: `ECRBuildAndPublish` action 

For the `ECRBuildAndPublish` action support, add the following to your policy statement: 

```
{
    "Statement": [
         {
            "Sid": "ECRRepositoryAllResourcePolicy",
            "Effect": "Allow",
            "Action": [
                "ecr:DescribeRepositories",
                "ecr:GetAuthorizationToken",
                "ecr-public:DescribeRepositories",
                "ecr-public:GetAuthorizationToken"
            ],
        "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchCheckLayerAvailability"
            ],
            "Resource": "PrivateECR_Resource_ARN"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr-public:GetAuthorizationToken",
                "ecr-public:DescribeRepositories",
                "ecr-public:InitiateLayerUpload",
                "ecr-public:UploadLayerPart",
                "ecr-public:CompleteLayerUpload",
                "ecr-public:PutImage",
                "ecr-public:BatchCheckLayerAvailability",
                "sts:GetServiceBearerToken"
            ],
            "Resource": "PublicECR_Resource_ARN"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sts:GetServiceBearerToken"
            ],
            "Resource": "*"
        }
    ]
}
```
 

In addition, if not already added for the `Commands` action, add the following permissions to your service role in order to view CloudWatch logs. 

```
{
    "Effect": "Allow",
    "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream", 
        "logs:PutLogEvents"
    ],
    "Resource": "resource_ARN"
},
```
 Note

Scope down the permissions to the pipeline resource level by using resource-based permissions in the service role policy statement. 

For more information about this action, see ECRBuildAndPublish build action reference. 

## Action declaration  

**YAML** 

```
name: ECRBuild
actionTypeId:
  category: Build
  owner: AWS
  provider: ECRBuildAndPublish
  version: '1'
runOrder: 1
configuration:
  ECRRepositoryName: actions/my-imagerepo
outputArtifacts: []
inputArtifacts:
- name: SourceArtifact
region: us-east-1
namespace: BuildVariables
```
  

**JSON** 

```
{
    "name": "ECRBuild",
    "actionTypeId": {
        "category": "Build",
        "owner": "AWS",
        "provider": "ECRBuildAndPublish",
        "version": "1"
    },
    "runOrder": 1,
    "configuration": {
        "ECRRepositoryName": "actions/my-imagerepo"
    },
    "outputArtifacts": [],
    "inputArtifacts": [
        {
            "name": "SourceArtifact"
        }
    ],
    "region": "us-east-1",
    "namespace": "BuildVariables"
},

```
   

## See also 

The following related resources can help you as you work with this action.  
Tutorial: Build and push a Docker image to Amazon ECR with CodePipeline (V2 type) – This tutorial provides a sample Dockerfile and instructions to create a pipeline that pushes your image to ECR on a change to your source repository and then deploys to Amazon ECS.
