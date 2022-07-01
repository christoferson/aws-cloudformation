## EventBridge Cloudformation

### EventBridge - Periodic - Trigger Lambda

Provision an EventBridge rule that periodically triggers a Lambda Function.

[eventbridge-trigger-lambda](eventbridge-trigger-lambda.yaml)

### EventBridge - CodeCommit - Trigger Lambda

Provision an EventBridge rule that triggers a Lambda Function on CodeCommit events.

- Branch is Created or Updated
- PullRequest is Merged

Also includes settings to transform the input Event into a custom output format.

```yaml
          InputTransformer: 
            InputPathsMap:
              "CallerUserArn" : "$.detail.callerUserArn"
              "ReferenceName" : "$.detail.referenceName"
              "RepositoryName" : "$.detail.repositoryName"
              "CommitId" : "$.detail.commitId"
            InputTemplate: |
              {
                "CallerUserArn" : "\"<CallerUserArn>\"",
                "ReferenceName" : "\"<ReferenceName>\"",
                "RepositoryName": "\"<RepositoryName>\"",
                "CommitId": "\"<CommitId>\""
              }
```

[eventbridge-rule-codecommit](eventbridge-rule-codecommit.yaml)

