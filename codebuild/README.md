
## CodeBuild Cloudformation Templates

## CodeBuild - Input:CodeCommit Output:ECR

Provision a CodeBuild project that pulls source from CodeCommit and pushes to ECR

- Provision EventBridge role and rule to detect changes in CodeCommit and trigger CodeBuild

[code-codebuild-codecommit-ecr](code-codebuild-codecommit-ecr.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.html
- https://aws.amazon.com/blogs/devops/how-to-enable-caching-for-aws-codebuild/
- https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html

TODO:
BuildSpec - Push to Docker Hub