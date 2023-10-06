## EventBridge Cloudformation

### EventBridge - EventBus

Provision a Custom Event Bus with Custom Policy.

[eventbridge-eventbus](eventbridge-eventbus.yaml)

### EventBridge - EventBus with Archive

Provision a Custom Event Bus with Custom Policy and Archive.

[eventbridge-eventbus-archive](eventbridge-eventbus-archive.yaml)

### EventBridge - EventBus Policy

EventBus Policy Examples

[eventbridge-eventbus-policy](eventbridge-eventbus-policy.yaml)

### EventBridge - Periodic - Trigger Lambda

Provision an EventBridge rule that periodically triggers a Lambda Function.

[eventbridge-call-lambda-schedule](eventbridge-call-lambda-schedule.yaml)

### EventBridge - Rule - CloudWatch Alarm

[eventbridge-rule-cloudwatch-alarm](eventbridge-rule-cloudwatch-alarm.yaml)

### EventBridge - CodePipeline - Pipeline

Privision EventBride rule to detect 'CodePipeline Pipeline Execution State Change' and invoke lambda.

CodePipeline Pipeline Execution State Change: CANCELED | FAILED | RESUMED | STARTED | STOPPED | STOPPING | SUCCEEDED | SUPERSEDED 

[eventbridge-rule-codepipeline](eventbridge-rule-codepipeline.yaml) | [reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)

### EventBrdige - Rule - Health

[eventbridge-rule-health](eventbridge-rule-health.yaml)

### EventBridge - Rule - Custom

[eventbridge-rule-custom](eventbridge-rule-custom.yaml)

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

[s3/eventbridge-rule-s3](s3/eventbridge-rule-s3-call-lambda.yaml)

### EventBridge - Rule - S3 - Trigger Batch

[eventbridge-rule-s3-call-batch](s3/eventbridge-rule-s3-call-batch.yaml)

### EventBridge - Rule - S3 - Trigger Step Functions

[eventbridge-rule-s3-call-batch](s3/eventbridge-rule-s3-call-batch.yaml)

------------------------------------------------------------------


### EventBridge - Rule - S3 - Trigger Step Functions

[eventbridge-rule-config-sns](eventbridge-rule-config-sns.yaml)


------------------------------------------------------------------

### EventBridge - Rule - Batch - Trigger SNS

Provision EventBridge rules that monitor Batch Jobs and Trigger SNS Notifications

[eventbridge-rule-batch-call-sns](batch/eventbridge-rule-batch-call-sns.yaml)

------------------------------------------------------------------

### EventBridge - Rule - StepFunction - Trigger SNS

Provision EventBridge rules that monitor Step Functions and Trigger SNS Notifications

[eventbridge-rule-stepfunctions-call-sns](batch/eventbridge-rule-stepfunctions-call-sns.yaml)

### Errors

##### Input Transformer: Invalid InputTemplate

CWE rule only allows users to use a String (with double quotes) or a JSON in the input template.

https://repost.aws/questions/QU-uwSGaM_S4GZ_wvF9FfJzQ/error-while-saving-rule-with-input-transformer-invalid-input-template

### References

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Events.html

- https://aws.amazon.com/blogs/aws/new-create-point-to-point-integrations-between-event-producers-and-consumers-with-amazon-eventbridge-pipes/?trk=d0c467f8-ee69-4b7d-8e81-bc02ae25d111&sc_channel=el

- https://github.com/aws-samples/amazon-s3-object-lambda-default-configuration/blob/main/template/s3objectlambda_defaultconfig.yaml

- [event-bus-policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html)

### TODO

Receiving events using AWS Lambda function URLs
https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-furls.html