

https://aws.amazon.com/premiumsupport/knowledge-center/batch-parameters-trigger-eventbridge/?nc1=h_ls


AWSTemplateFormatVersion: '2010-09-09'
Description: >-
  CloudFormation template for EventBridge rule
  'eventbridge-rule-s3-call-EventBridgeRuleS3CallBat-1K991IMNSTZ6D'
Resources:
  EventRule0:
    Type: AWS::Events::Rule
    Properties:
      Description: Demo S3 Trigger Batch
      EventBusName: default
      EventPattern:
        detail-type:
          - Object Created
        source:
          - aws.s3
        detail:
          bucket:
            name:
              - b2b-dev-data
      Name: eventbridge-rule-s3-call-EventBridgeRuleS3CallBat-1K991IMNSTZ6D
      State: ENABLED
      Targets:
        - Id: TargetBatch
          Arn: >-
            arn:aws:batch:eu-west-1:916902469227:job-queue/BatchJobQueue-YF75D0jJcnsxSG9P
          RoleArn: >-
            arn:aws:iam::916902469227:role/eventbridge-rule-s3-call-batch-EvenBridgeRole-APMGRXDQ5K7Z
          InputTransformer:
            InputPathsMap:
              S3ObjectKey: $.detail.object.key
            InputTemplate: |-
              {
                "Parameters": {"S3Key" : "<S3ObjectKey>"},
                "ContainerOverrides": { 
                  "Command": ["sh", "-c", "echo s3rocks && java -jar batch.jar <S3ObjectKey>"] 
                }
              }
          BatchParameters:
            JobDefinition: >-
              arn:aws:batch:eu-west-1:916902469227:job-definition/BatchJobDefinition-10e963866c726db:11
            JobName: eventbridge-rule-s3-call-batch-job
            RetryStrategy:
              Attempts: 1
