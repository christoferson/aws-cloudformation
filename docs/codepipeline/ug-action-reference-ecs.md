> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECS.html
> Downloaded: 2026-10-19

# Amazon Elastic Container Service deploy action reference

You can use an Amazon ECS action to deploy an Amazon ECS service and task set. An Amazon ECS service is a container application that is deployed to an Amazon ECS cluster. An Amazon ECS cluster is a collection of instances that host your container application in the cloud. The deployment requires a task definition that you create in Amazon ECS and an image definitions file that CodePipeline uses to deploy the image.Important

The Amazon ECS standard deployment action for CodePipeline creates its own revision of the task definition based on the revision used by the Amazon ECS service. If you create new revisions for the task definition without updating the Amazon ECS service, the deployment action will ignore those revisions.

Before you create your pipeline, you must have already created the Amazon ECS resources, tagged and stored the image in your image repository, and uploaded the buildspec file to your file repository.Note

This reference topic describes the Amazon ECS standard deployment action for CodePipeline. For reference information about Amazon ECS to CodeDeploy blue/green deployment actions in CodePipeline, see Amazon Elastic Container Service and CodeDeploy blue-green deploy action reference.Topics
Action type
Configuration parameters
Input artifacts
Output artifacts
Service role permissions: Amazon ECS standard action
Action declaration
See also
 

## Action type  
Category: `Deploy` 
Owner: `AWS` 
Provider: `ECS` 
Version: `1` 
 

## Configuration parameters   

**ClusterName**  

Required: Yes 

The Amazon ECS cluster in Amazon ECS.  

**ServiceName**  

Required: Yes 

The Amazon ECS service that you created in Amazon ECS.  

**FileName**  

Required: No 

The name of your image definitions file, the JSON file that describes your service's container name and the image and tag. You use this file for ECS standard deployments. For more information, see Input artifacts and imagedefinitions.json file for Amazon ECS standard deployment actions.  

**DeploymentTimeout**  

Required: No 

The Amazon ECS deployment action timeout in minutes. The timeout is configurable up to the maximum default timeout for this action. For example:  

```
"DeploymentTimeout": "15"
```
   

## Input artifacts  
Number of artifacts: `1` 
Description: The action looks for an `imagedefinitions.json` file in the source file repository for the pipeline. An image definitions document is a JSON file that describes your Amazon ECS container name and the image and tag. CodePipeline uses the file to retrieve the image from your image repository such as Amazon ECR. You can manually add an `imagedefinitions.json` file for a pipeline where the action is not automated. For information about the `imagedefinitions.json` file, see imagedefinitions.json file for Amazon ECS standard deployment actions. 

The action requires an existing image that has already been pushed to your image repository. Because the image mapping is provided by the `imagedefinitions.json` file, the action does not require that the Amazon ECR source be included as a source action in the pipeline. 
 

## Output artifacts  
Number of artifacts: `0`  
Description: Output artifacts do not apply for this action type. 
 

## Service role permissions: Amazon ECS standard action 

For Amazon ECS, the following are the minimum permissions needed to create pipelines with an Amazon ECS deploy action.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "TaskDefinitionPermissions",
            "Effect": "Allow",
            "Action": [
                "ecs:DescribeTaskDefinition",
                "ecs:RegisterTaskDefinition"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "ECSServicePermissions",
            "Effect": "Allow",
            "Action": [
                "ecs:DescribeServices",
                "ecs:UpdateService"
            ],
            "Resource": [
                "arn:aws:ecs:*:111122223333:service/[[clusters]]/*"
            ]
        },
        {
            "Sid": "ECSTagResource",
            "Effect": "Allow",
            "Action": [
                "ecs:TagResource"
            ],
            "Resource": [
                "arn:aws:ecs:*:111122223333:task-definition/[[taskDefinitions]]:*"
            ],
            "Condition": {
                "StringEquals": {
                    "ecs:CreateAction": [
                        "RegisterTaskDefinition"
                    ]
                }
            }
        },
        {
            "Sid": "IamPassRolePermissions",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": [
                "arn:aws:iam::111122223333:role/[[passRoles]]"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "ecs.amazonaws.com",
                        "ecs-tasks.amazonaws.com"
                    ]
                }
            }
        }
    ]
}

```
     

You can opt in to using tagging authorization in Amazon ECS. By opting in, you must grant the following permissions: `ecs:TagResource`. For more information about how to opt in and to determine whether the permission is required and tag authorization is enforced, see Tagging authorization timeline in the Amazon Elastic Container Service Developer Guide. 

You must add the `iam:PassRole` permissions to use IAM roles for tasks. For more information, see Amazon ECS task execution IAM role and IAM Roles for Tasks. Use the following policy text. 

## Action declaration  

**YAML** 

```
Name: DeployECS
ActionTypeId:
  Category: Deploy
  Owner: AWS
  Provider: ECS
  Version: '1'
RunOrder: 2
Configuration:
  ClusterName: my-ecs-cluster
  ServiceName: sample-app-service
  FileName: imagedefinitions.json
  DeploymentTimeout: '15'
OutputArtifacts: []
InputArtifacts:
  - Name: my-image
```
  

**JSON** 

```
{
    "Name": "DeployECS",
    "ActionTypeId": {
        "Category": "Deploy",
        "Owner": "AWS",
        "Provider": "ECS",
        "Version": "1"
    },
    "RunOrder": 2,
    "Configuration": {
        "ClusterName": "my-ecs-cluster",
        "ServiceName": "sample-app-service",
        "FileName": "imagedefinitions.json",
        "DeploymentTimeout": "15"
    },
    "OutputArtifacts": [],
    "InputArtifacts": [
        {
            "Name": "my-image"
        }
    ]
},
```
   

## See also 

The following related resources can help you as you work with this action.  
See Tutorial: Build and push a Docker image to Amazon ECR with CodePipeline (V2 type) for a tutorial that shows you how to use the ECRBuildandPublish action to push an image and then use the ECS standard action to deploy to Amazon ECS. 
Tutorial: Continuous Deployment with CodePipeline – This tutorial shows you how to create a Dockerfile that you store in a source file repository such as CodeCommit. Next, the tutorial shows you how to incorporate a CodeBuild buildspec file that builds and pushes your Docker image to Amazon ECR and creates your imagedefinitions.json file. Finally, you create an Amazon ECS service and task definition, and then you create your pipeline with an Amazon ECS deployment action. Note

This topic and tutorial describe the Amazon ECS standard deployment action for CodePipeline. For information about Amazon ECS to CodeDeploy blue/green deployment actions in CodePipeline, see Tutorial: Create a pipeline with an Amazon ECR source and ECS-to-CodeDeploy deployment. 
Amazon Elastic Container Service Developer Guide – For information about working with Docker images and containers, Amazon ECS services and clusters, and Amazon ECS task sets, see What Is Amazon ECS?
