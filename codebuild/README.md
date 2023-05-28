
## CodeBuild Cloudformation Templates

## CodeBuild Environment Variables | [link](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html)

##### CODEBUILD_BUILD_NUMBER
The current build number for the project.

##### CODEBUILD_RESOLVED_SOURCE_VERSION
The version identifier of a build's source code. The contents depends on the source code repository:

CodeCommit, GitHub, GitHub Enterprise Server, and Bitbucket
This variable contains the commit ID.

CodePipeline
This variable contains the source revision provided by CodePipeline.

If CodePipeline is not able to resolve the source revision, such as when the source is an Amazon S3 bucket that does not have versioning enabled, this environment variable is not set.

CODEBUILD_RESOLVED_SOURCE_VERSION variable is only available after the DOWNLOAD_SOURCE phase.

##### CODEBUILD_SOURCE_VERSION
The value's format depends on the source repository.

For Amazon S3, it is the version ID associated with the input artifact.

For CodeCommit, it is the commit ID or branch name associated with the version of the source code to be built. e.g. refs/heads/dev

For GitHub, GitHub Enterprise Server, and Bitbucket it is the commit ID, branch name, or tag name associated with the version of the source code to be built.

## CodeBuild - Input:CodeCommit Output:ECR

Provision a CodeBuild project that pulls source from CodeCommit and pushes to ECR

- Provision EventBridge role and rule to detect changes in CodeCommit and trigger CodeBuild

[code-codebuild-codecommit-ecr](code-codebuild-codecommit-ecr.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.html
- https://aws.amazon.com/blogs/devops/how-to-enable-caching-for-aws-codebuild/
- https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replicate-filtered-amazon-ecr-container-images-across-accounts-or-regions.html

#### Errors

##### junit because no identity-based policy allows the codebuild:CreateReportGroup action


#### Java

##### Install Java Runtime

Make sure you are using the Environment Image that supports the runtime version

```
      Environment:
        PrivilegedMode: true
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/standard:7.0
```

In your buildspec, install the correct java runtime. e.g. corretto17

```
        BuildSpec: |
          ...
          phases:
            install:
              runtime-versions:
                java: corretto17
```

##### JUNIT Report

Ensure CodeBuild has required permissions

```
            Action:
              - codebuild:CreateReportGroup
              - codebuild:CreateReport
              - codebuild:UpdateReport
              - codebuild:BatchPutTestCases
              - codebuild:BatchPutCodeCoverages
            Resource:
              - !Sub "arn:aws:codebuild:${AWS::Region}:${AWS::AccountId}:report-group/*"
```

Create a report in your buildspec.

```
          reports:
            junit:
              files:
                - '**/*'
              base-directory: "build/test-results"
              file-format: 'JUnitXML'           
```

TODO:
BuildSpec - Push to Docker Hub

```
2023-05-17T23:57:29.366+09:00	[Container] 2023/05/17 14:57:28 Running command echo $CODEBUILD_BUILD_NUMBER
2023-05-17T23:57:29.366+09:00	18
2023-05-17T23:57:29.366+09:00	[Container] 2023/05/17 14:57:28 Running command echo $CODEBUILD_RESOLVED_SOURCE_VERSION
2023-05-17T23:57:29.366+09:00	9ce3e5715da11c43acc5ad973080b09beaddf251
2023-05-17T23:57:29.366+09:00	[Container] 2023/05/17 14:57:28 Running command echo $CODEBUILD_SOURCE_VERSION
2023-05-17T23:57:29.366+09:00	
```