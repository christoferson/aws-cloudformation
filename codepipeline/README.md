
## CI/CD Cloudformation Templates

## CodeCommit

### CodeCommit - Basic

Provision a CodeCommit repository

[code-codecommit](code-codecommit.yaml)

### CodeCommit - Triggers - SNS

[code-codecommit-sns](code-codecommit-sns.yaml)

### CodeCommit - Triggers - Lambda

[code-codecommit-triggers](code-codecommit-triggers.yaml)

### CodeCommit - Notification Rules

## CodeBuild

- Source - NoSource, CodeCommit, GitHub, Bitbucket, CODEPIPELINE, S3
- Operating System - Linux, Ubuntu, Docket
- Output: NoOutput, S3

### CodeBuild - Input:none Output:none

CodeBuild example with No Input Source and No Output Artifact

code-codebuild-nosource

### CodeBuild - Input:S3 Output:S3

CodeBuild example with S3 Input Source and S3 Output Artifact. 

- Template uses same Bucket as Input and Output.
- The zip file code-codebuild-s3.zip containing buildspec.yaml and the source codes must be placed in the source bucket.

code-codebuild-s3

```yaml
      Source: #buildspec.yaml in zip file
        Type: S3
        Location: !Sub "${CodeBuildSourceBucket}/code-codebuild-s3.zip"
```

```yaml
      Artifacts:
        Type: S3
        Location: !Sub "${CodeBuildSourceBucket}"
        Path: /output
        Name: build.zip
        NamespaceType: BUILD_ID # NONE | BUILD_ID
        Packaging: ZIP # NONE | ZIP
        OverrideArtifactName: true #Use Name in buildspec.yaml. Otherwise use Name'build.zip' defined here.
```

### CodeBuild - Input:CodeCommit Output:S3

CodeBuild example with CodeCommit Input Source and S3 Output Artifact

- CodeCommit source must contain buildspec.yaml at the root of the repository.

code-codebuild-codecommit

```yaml
      Source:
        Type: CODECOMMIT
        Location: !Sub "${CodeCommitRepository.CloneUrlHttp}"
```

```yaml
      Artifacts:
        Type: S3
        Location: !Sub "${CodeBuildOutputBucket}"
        Path: /output
        Name: build.zip
        NamespaceType: BUILD_ID # NONE | BUILD_ID
        Packaging: ZIP
        OverrideArtifactName: true #Use Name in buildspec.yaml. Otherwise use Name'build.zip' defined here.
```

### CodeBuild - Input:CodeCommit Output:S3 with Trigger on Commit

CodeBuild example with CodeCommit Input Source and S3 Output Artifact with Trigger on Commit

code-codebuild-codecommit-evt

## CodeDeploy

- Deploys application from S3 or GitHub to EC2, Lambda or ECS.
- CodeDeploy does not provision resources.
- EC2 must be running the CodeDeploy agent which will process the appsec.yaml
- EC2 Role must have permissions to pull from S3

## CodeDeploy - Install

Based on [documentation](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html)

```
sudo yum update -y
sudo yum install -y ruby wget
wget https://aws-codedeploy-eu-west-1.s3.eu-west-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status
```


## CodeDeploy - EC2

CodeDeploy example that deploys to EC2

- Must make sure that EC2 satisfying Ec2TagFilters is up and running before deploying the template. - CF will wait until the code is deployed to the EC2 in order to complete.

```
      Ec2TagFilters:
        - Type: KEY_AND_VALUE
          Key: "Environment"
          Value: "Development"
        - Type: KEY_AND_VALUE
          Key: "Name"
          Value: "Webserver"
```

[code-codedeploy-ec2](code-codedeploy-ec2.yaml)

## CodePipeline

Remove Deployment in CodeDeploy

Stage Action Category: Source Build Test Deploy Invoke Approval

### CodePipeline Input:CodeCommit Stage:Source,Deploy to EC2

CodePipeline example with CodeCommit as Source. Has Stages Source,Deploy

code-codepipeline-basic.yaml

### CodePipeline Input:CodeCommit Stage:Source,Build,Deploy to EC2

CodePipeline example with CodeCommit as Source. Has Stages Source,Build,Deploy

code-codepipeline-3step.yaml

### CodePipeline Input:CodeCommit Stage:Source,Build,Deploy to EC2 with Trigger on Push

CodePipeline example with CodeCommit as Source. Has Stages Source,Build,Deploy

- CodePipeline is triggered on CodeCommit push

code-codepipeline-evt

### CodePipeline Input:CodeCommit Stage:Source,Build,Deploy to ECS with Trigger on Push

CodePipeline example with CodeCommit as Source. Has Stages Source,Build,Deploy. Deploys to ECS

code-codepipeline-ecs


## Resources

https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html
https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeCommit.html
https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html

## Resources - CodeCommit

- https://docs.aws.amazon.com/codecommit/latest/APIReference/API_RepositoryTrigger.html
- https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-events.html
- https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html
TODO
EventBridgeEvents

## Errors

1. Insufficient permissions Unable to use Connection: arn:aws:codestar-connections:us-east-1:xxx

Solution: Add permission to CodePipeline Service Role.

```
{
        "Effect": "Allow",
        "Action": "codestar-connections:UseConnection",
        "Resource": "ARN of the CodeStar connection" 
}
* arn:aws:codestar-connections:region:account-id:connection/connection-id
```

2. Source - [GitHub] Upload to S3 failed with the following error: Access Denied

Change the OutputArtifactFormat to CODEBUILD_CLONE_REF from CODE_ZIP

```
ConnectionArn: !Ref GithubConnectionArn
FullRepositoryId: !Ref GithubRepositoryName
BranchName: !Ref GithubBranchName
OutputArtifactFormat: CODEBUILD_CLONE_REF #OutputArtifactFormat: 'CODE_ZIP'
RunOrder: 1
```


3. CodeBuild - authorization failed for primary source and source version

Solution: Add permission to CodeBuild Service Role.

```
{
        "Effect": "Allow",
        "Action": "codestar-connections:UseConnection",
        "Resource": "ARN of the CodeStar connection" 
}
* arn:aws:codestar-connections:region:account-id:connection/connection-id
```