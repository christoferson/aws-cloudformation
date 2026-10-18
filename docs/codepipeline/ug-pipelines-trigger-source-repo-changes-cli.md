> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-repo-changes-cli.html
> Downloaded: 2026-10-18

# Create an EventBridge rule for a CodeCommit source (CLI)

Call the put-rule command, specifying: 
A name that uniquely identifies the rule you are creating. This name must be unique across all of the pipelines you create with CodePipeline associated with your AWS account. 
The event pattern for the source and detail fields used by the rule. For more information, see Amazon EventBridge and Event Patterns. 
To create an EventBridge rule with CodeCommit as the event source and CodePipeline as the target
Add permissions for EventBridge to use CodePipeline to invoke the rule. For more information, see Using resource-based policies for Amazon EventBridge. 
Use the following sample to create the trust policy that allows EventBridge to assume the service role. Name the trust policy `trustpolicyforEB.json`.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "events.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```
Use the following command to create the `Role-for-MyRule` role and attach the trust policy. 

```
aws iam create-role --role-name Role-for-MyRule --assume-role-policy-document file://trustpolicyforEB.json
```
Create the permissions policy JSON, as shown in this sample, for the pipeline named `MyFirstPipeline`. Name the permissions policy `permissionspolicyforEB.json`.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "codepipeline:StartPipelineExecution"
            ],
            "Resource": [
                "arn:aws:codepipeline:us-west-2:111122223333:MyFirstPipeline"
            ]
        }
    ]
}

```
Use the following command to attach the `CodePipeline-Permissions-Policy-for-EB` permissions policy to the `Role-for-MyRule` role. 

Why am I making this change? Adding this policy to the role creates permissions for EventBridge. 

```
aws iam put-role-policy --role-name Role-for-MyRule --policy-name CodePipeline-Permissions-Policy-For-EB --policy-document file://permissionspolicyforEB.json
```
Call the put-rule command and include the `--name`, `--event-pattern` , and`--role-arn` parameters. 

Why am I making this change? This command enables CloudFormation to create the event. 

The following sample command creates a rule called `MyCodeCommitRepoRule`. 

```
aws events put-rule --name "MyCodeCommitRepoRule" --event-pattern "{\"source\":[\"aws.codecommit\"],\"detail-type\":[\"CodeCommit Repository State Change\"],\"resources\":[\"repository-ARN\"],\"detail\":{\"referenceType\":[\"branch\"],\"referenceName\":[\"main\"]}}" --role-arn "arn:aws:iam::ACCOUNT_ID:role/Role-for-MyRule"
```
To add CodePipeline as a target, call the put-targets command and include the following parameters:  
The `--rule` parameter is used with the `rule_name` you created by using put-rule.  
The `--targets` parameter is used with the list `Id` of the target in the list of targets and the `ARN` of the target pipeline. 
 

The following sample command specifies that for the rule called `MyCodeCommitRepoRule`, the target `Id` is composed of the number one, indicating that in a list of targets for the rule, this is target 1. The sample command also specifies an example `ARN` for the pipeline. The pipeline starts when something changes in the repository. 

```
aws events put-targets --rule MyCodeCommitRepoRule --targets Id=1,Arn=arn:aws:codepipeline:us-west-2:80398EXAMPLE:TestPipeline
```
(Optional) To configure an input transformer with source overrides for a specific image ID, use the following JSON in your CLI command. The following example configures an override where:  
The `actionName`, `Source` in this example, is the dynamic value, defined at pipeline creation, not derived from the source event. 
The `revisionType`, `COMMIT_ID` in this example, is the dynamic value, defined at pipeline creation, not derived from the source event. 
The `revisionValue`, <`revisionValue`> in this example, is derived from the source event variable. 
 

```
{
    "Rule": "my-rule",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "pipeline-ARN",
            "InputTransformer": {
                "sourceRevisions": {
                    "actionName": "Source",
                    "revisionType": "COMMIT_ID",
                    "revisionValue": "<revisionValue>"
                },
                "variables": [
                    {
                        "name": "Branch_Name",
                        "value": "value"
                    }
                ]
            }
        }
    ]
}
```
 
To edit your pipeline's PollForSourceChanges parameterImportant

When you create a pipeline with this method, the `PollForSourceChanges` parameter defaults to true if it is not explicitly set to false. When you add event-based change detection, you must add the parameter to your output and set it to false to disable polling. Otherwise, your pipeline starts twice for a single source change. For details, see Valid settings for the PollForSourceChanges parameter.
Run the get-pipeline command to copy the pipeline structure into a JSON file. For example, for a pipeline named `MyFirstPipeline`, run the following command:  

```
aws codepipeline get-pipeline --name MyFirstPipeline >pipeline.json
```
 

This command returns nothing, but the file you created should appear in the directory where you ran the command. 
Open the JSON file in any plain-text editor and edit the source stage by changing the `PollForSourceChanges` parameter to `false`, as shown in this example. 

Why am I making this change? Changing this parameter to `false` turns off periodic checks so you can use event-based change detection only. 

```
"configuration": {
    "PollForSourceChanges": "false",
    "BranchName": "main",
    "RepositoryName": "MyTestRepo"
},
```
If you are working with the pipeline structure retrieved using the get-pipeline command, remove the `metadata` lines from the JSON file. Otherwise, the update-pipeline command cannot use it. Remove the `"metadata": { }` lines and the `"created"`, `"pipelineARN"`, and `"updated"` fields. 

For example, remove the following lines from the structure:  

```
"metadata": {
    "pipelineArn": "arn:aws:codepipeline:region:account-ID:pipeline-name",
    "created": "date",
    "updated": "date"
},
```
 

Save the file. 
To apply your changes, run the update-pipeline command, specifying the pipeline JSON file: Important

Be sure to include `file://` before the file name. It is required in this command. 

```
aws codepipeline update-pipeline --cli-input-json file://pipeline.json
```
 

This command returns the entire structure of the edited pipeline. Note

The update-pipeline command stops the pipeline. If a revision is being run through the pipeline when you run the update-pipeline command, that run is stopped. You must manually start the pipeline to run that revision through the updated pipeline. Use the `start-pipeline-execution` command to manually start your pipeline.
