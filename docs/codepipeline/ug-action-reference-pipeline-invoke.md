> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-PipelineInvoke.html
> Downloaded: 2026-10-18

# AWS CodePipeline invoke action reference

You use a CodePipeline invoke action to simplify triggering downstream pipeline executions and passing pipeline variables and source revisions between pipelines.Note

This action is only supported for V2 type pipelines.Topics
Action type
Configuration parameters
Input artifacts
Output artifacts
Service role policy permissions for the CodePipeline invoke action
Action declaration
See also
 

## Action type  
Category: `Invoke` 
Owner: `AWS` 
Provider: `CodePipeline` 
Version: `1` 
 

## Configuration parameters   

**PipelineName**  

Required: Yes 

The name of the pipeline that will, upon running, start the current target pipeline. You must have already created the invoking pipeline. The action will start the `s3-pipeline-test` (target) pipeline when the (invoking) pipeline named `my-s3-pipeline` starts an execution.  

**SourceRevisions**  

Required: No 

The source revisions that you want the target pipeline to use when it is started by the invoking pipeline. For example, an S3 source action provides output variables such as the S3 Version ID and Object Key. You can specify a revision value to be used when the pipeline is invoked.  

For the CLI, you specify source revisions as a serialized JSON string. For more information about using source revision overrides, see SourceRevisionOverride in the CodePipeline API Guide. 

The mapping uses a string format as shown in the following example: 

```
[{"actionName":"Source","revisionType":"S3_OBJECT_VERSION_ID","revision
Value":"zq8mjNEXAMPLE"}]
```
  

**Variables**  

Required: No 

The names and values of variables that you want the action to support. 

For the CLI, you specify variables as a serialized JSON string. For more information about using pipeline variables, see PipelineVariable in the CodePipeline API Guide. 

The mapping uses a string format as shown in the following example: 

```
[{"name":"VAR1","value":"VALUE1"}]
```
   

The following image shows an example of the action added to a pipeline in the console.     

The following image shows an example of the Edit page for the action. In the following example, the pipeline named `s3-pipeline-test` has a pipeline invoke action configured as shown for the console. The action will start the `s3-pipeline-test` pipeline when the pipeline named `my-s3-pipeline` completes an execution. The example shows that source revision override for the S3_OBJECT_VERSION_ID source override with specified revision value of `zq8mjNYEexample`.    

## Input artifacts  
Number of artifacts: `0` 
Description: Input artifacts do not apply for this action type. 
 

## Output artifacts  
Number of artifacts: `0`  
Description: Output artifacts do not apply for this action type. 
 

## Service role policy permissions for the CodePipeline invoke action 

When CodePipeline runs the action, the CodePipeline service role policy requires the `codepipeline:StartPipelineExecution` permission, appropriately scoped down to the pipeline resource ARN in order to maintain access with least privilege. 

```
 {
            "Sid": "StatementForPipelineInvokeAction",
            "Effect": "Allow",
            "Action": "codepipeline:StartPipelineExecution",
            "Resource": [
                "arn:aws:codepipeline:{{region}}:{{AccountId}}:{{pipelineName}}"
            ]
        }
```
 

## Action declaration  

**YAML** 

```
name: Invoke-pipeline
actionTypeId:
  category: Invoke
  owner: AWS
  provider: CodePipeline
  version: '1'
runOrder: 2
configuration:
  PipelineName: my-s3-pipeline
  SourceRevisions: '[{"actionName":"Source","revisionType":"S3_OBJECT_VERSION_ID","revision
Value":"zq8mjNEXAMPLE"}]'
  Variables: '[{"name":"VAR1","value":"VALUE1"}]'
```
  

**JSON** 

```
{
    "name": "Invoke-pipeline",
    "actionTypeId": {
        "category": "Invoke",
        "owner": "AWS",
        "provider": "CodePipeline",
        "version": "1"
    },
    "runOrder": 2,
    "configuration": {
        "PipelineName": "my-s3-pipeline",
        "SourceRevisions": "[{\"actionName\":\"Source\",\"revisionType\":\"S3_OBJECT_VERSION_ID\",\"revisionValue\":\"zq8mjNEXAMPLE\"}]",
        "Variables": "[{\"name\":\"VAR1\",\"value\":\"VALUE1\"}]"
    }
},
```
   

## See also 

The following related resources can help you as you work with this action.  
 Start a pipeline with a source revision override – This section describes starting a pipeline with source revisions manually or through the EventBridge event input transformer.
