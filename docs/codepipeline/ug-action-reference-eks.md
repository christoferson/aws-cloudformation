> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-EKS.html
> Downloaded: 2026-10-18

# Amazon Elastic Kubernetes Service `EKS` deploy action reference

You can use the `EKSDeploy` action to deploy an Amazon EKS service. The deployment requires a Kubernetes manifest file that CodePipeline uses to deploy the image.

Before you create your pipeline, you must have already created the Amazon EKS resources and have stored the image in your image repository. Optionally, you can provide VPC information for your cluster.Important

This action uses CodePipeline managed CodeBuild compute to run commands in a build environment. Running the commands action will incur separate charges in AWS CodeBuild.Note

The `EKS` deploy action is only available for V2 type pipelines.

The EKS action supports both public and private EKS clusters. Private clusters are the type recommended by EKS; however, both types are supported.

The EKS action is supported for cross-account actions. To add a cross-account EKS action, add `actionRoleArn` from your target account in the action declaration.Topics
Action type
Configuration parameters
Input artifacts
Output artifacts
Environment variables
Output variables
Service role policy permissions
Action declaration
See also
 

## Action type  
Category: `Deploy` 
Owner: `AWS` 
Provider: `EKS` 
Version: `1` 
 

## Configuration parameters   

**ClusterName**  

Required: Yes 

The Amazon EKS cluster in Amazon EKS.  

**Options under Helm**  

The following are available options when Helm is the selected deployment tool.   

**HelmReleaseName **  

Required: Yes (Required only for Helm type) 

The release name for your deployment.  

**HelmChartLocation **  

Required: Yes (Required only for Helm type) 

The chart location for your deployment.  

**HelmValuesFiles **  

Required: No (Optional only for Helm type) 

To override for Helm values files, enter the comma-separated Helm values files in the Helm chart location.    

**Options under Kubectl**  

The following are available options when Kubectl is the selected deployment tool.   

**ManifestFiles**  

Required: Yes (Required only for Kubectl type) 

The name of your manifest file, the text file that describes your service's container name and the image and tag. You use this file to parameterize your image URI and other information. You can use an environment variable for this purpose. 

 You store this file in the source repository for your pipeline.    

**Namespace**  

Required: No 

The Kubernetes namespace to be used in `kubectl` or `helm` commands.  

**Subnets**  

Required: No 

The subnets for the VPC for your cluster. These are part of the same VPC that is attached to your cluster. You can also provide subnets that aren't already attached to your cluster and specify them here.  

**SecurityGroupIds**  

Required: No 

The security groups for the VPC for your cluster. These are part of the same VPC that is attached to your cluster. You can also provide security groups that aren't already attached to your cluster and specify them here.   

## Input artifacts  
Number of artifacts: `1` 
Description: The action looks for the Kubernetes manifest file or Helm chart in the source file repository for the pipeline. If you want to use Helm charts in .tgz format stored in an S3 bucket, you can do so by configuring the S3 Bucket/Key as your source action. For example, the object key provided would be `my-chart-0.1.0.tgz`. 
 

## Output artifacts  
Number of artifacts: `0`  
Description: Output artifacts do not apply for this action type. 
 

## Environment variables 

Used to replace variables such as image repositories or image tags in manifest files or Helm chart values files.   

**Key**  

The key in a key-value environment variable pair, such as `$IMAGE_TAG`.  

**Value**  

The value for the key-value pair, such as `v1.0`. The value can be parameterized with output variables from pipeline actions or pipeline variables. For example, pipeline can have an ECRBuildAndPublish action that creates an ECR image with `${codepipeline.PipelineExecutionId}`, and the EKS action can use this image using `${codepipeline.PipelineExecutionId}` as the value of the environment variable.    

## Output variables   

**EKSClusterName**  

The Amazon EKS cluster in Amazon EKS.   

## Service role policy permissions 

To run this action, the following permissions must be available in your pipeline's service role policy.  
EC2 actions: When CodePipeline runs the action EC2 instance permissions are required. Note that this is not the same as the EC2 instance role required when you create your EKS cluster. 

If you are using an existing service role, to use this action, you will need to add the following permissions for the service role.  
ec2:CreateNetworkInterface 
ec2:DescribeDhcpOptions 
ec2:DescribeNetworkInterfaces 
ec2:DeleteNetworkInterface 
ec2:DescribeSubnets 
ec2:DescribeSecurityGroups 
ec2:DescribeVpcs 
EKS actions: When CodePipeline runs the action, EKS cluster permissions are required. Note that this is not the same as the IAM EKS cluster role required when you create your EKS cluster. 

If you are using an existing service role, to use this action, you will need to add the following permission for the service role.  
eks:DescribeCluster 
Log stream actions: When CodePipeline runs the action, CodePipeline creates a log group using the name of the pipeline as follows. This enables you to scope down permissions to log resources using the pipeline name. 

```
/aws/codepipeline/MyPipelineName
```
 

If you are using an existing service role, to use this action, you will need to add the following permissions for the service role.  
logs:CreateLogGroup 
logs:CreateLogStream 
logs:PutLogEvents 
 
 

In the service role policy statement, scope down the permissions to the resource level as shown in the following example.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "eks:DescribeCluster"
            ],
            "Resource": "arn:aws:eks:*:111122223333:cluster/YOUR_CLUSTER_NAME"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:CreateNetworkInterfacePermission",
                "ec2:DescribeDhcpOptions",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:DescribeRouteTables"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:111122223333:log-group:/aws/codepipeline/YOUR_PIPELINE_NAME",
                "arn:aws:logs:*:111122223333:log-group:/aws/codepipeline/YOUR_PIPELINE_NAME:*"
            ]
        }
    ]
}

```
     

To view logs in the console using the action details dialog page, the permission to view logs must be added to the console role. For more information, see the console permissions policy example in Permissions required to view compute logs in the console. 

### Adding the service role as an access entry for your cluster 

After the permissions are available in your pipeline's service role policy, you configure your cluster permissions by adding the CodePipeline service role as an access entry for your cluster. 

You can also use an action role that has the updated permissions. For more information, see the tutorial example in Step 4: Create an access entry for the CodePipeline service role. 

## Action declaration  

**YAML** 

```
Name: DeployEKS
ActionTypeId:
  Category: Deploy
  Owner: AWS
  Provider: EKS
  Version: '1'
RunOrder: 2
Configuration:
  ClusterName: my-eks-cluster
  ManifestFiles: ManifestFile.json
OutputArtifacts: []
InputArtifacts:
  - Name: SourceArtifact
```
  

**JSON** 

```
{
    "Name": "DeployECS",
    "ActionTypeId": {
        "Category": "Deploy",
        "Owner": "AWS",
        "Provider": "EKS",
        "Version": "1"
    },
    "RunOrder": 2,
    "Configuration": {
        "ClusterName": "my-eks-cluster",
        "ManifestFiles": "ManifestFile.json"
    },
    "OutputArtifacts": [],
    "InputArtifacts": [
        {
            "Name": "SourceArtifact"
        }
    ]
},
```
   

## See also 

The following related resources can help you as you work with this action.  
See Tutorial: Deploy to Amazon EKS with CodePipeline for a tutorial that demonstrates how to create an EKS cluster and Kubernetes manifest file to add the action to your pipeline.
