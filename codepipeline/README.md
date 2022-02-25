
## CodeCommit

CodeCommit example

code-codecommit

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

code-codedeploy-ec2

## CodePipeline
