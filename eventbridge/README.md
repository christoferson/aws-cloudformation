## EventBridge Cloudformation

### EventBridge - EventBus

Provision a Custom Event Bus

[eventbridge-eventbus](eventbridge-eventbus.yaml)

### EventBridge - Rule - CloudWatch Alarm

[eventbridge-rule-cloudwatch-alarm](eventbridge-rule-cloudwatch-alarm.yaml)

### EventBridge - CodePipeline - Pipeline

Privision EventBride rule to detect 'CodePipeline Pipeline Execution State Change' and invoke lambda.

CodePipeline Pipeline Execution State Change: CANCELED | FAILED | RESUMED | STARTED | STOPPED | STOPPING | SUCCEEDED | SUPERSEDED 

[eventbridge-rule-codepipeline](eventbridge-rule-codepipeline.yaml) | [reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)

### EventBridge - Rule - Custom

[eventbridge-rule-custom](eventbridge-rule-custom.yaml)

### EventBridge - Periodic - Trigger Lambda

Provision an EventBridge rule that periodically triggers a Lambda Function.

[eventbridge-call-lambda-schedule](eventbridge-call-lambda-schedule.yaml)

### EventBridge - Rule - CodeCommit - Trigger Lambda

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

### EventBridge - Rule - S3 - Trigger Lambda

[s3/eventbridge-rule-s3](s3/eventbridge-rule-s3.yaml)

### Refernces

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Events.html


### TODO

Receiving events using AWS Lambda function URLs
https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-furls.html