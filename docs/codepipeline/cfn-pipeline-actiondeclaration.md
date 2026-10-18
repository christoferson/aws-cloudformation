> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-actiondeclaration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline ActionDeclaration

Represents information about an action declaration.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ActionTypeId" : ActionTypeId,
  "Commands" : [ String, ... ],
  "Configuration" : Json,
  "EnvironmentVariables" : [ EnvironmentVariable, ... ],
  "InputArtifacts" : [ InputArtifact, ... ],
  "Name" : String,
  "Namespace" : String,
  "OutputArtifacts" : [ OutputArtifact, ... ],
  "OutputVariables" : [ String, ... ],
  "Region" : String,
  "RoleArn" : String,
  "RunOrder" : Integer,
  "TimeoutInMinutes" : Integer
}

```

### YAML

```
  ActionTypeId: 
    ActionTypeId
  Commands: 
    - String
  Configuration: Json
  EnvironmentVariables: 
    - EnvironmentVariable
  InputArtifacts: 
    - InputArtifact
  Name: String
  Namespace: String
  OutputArtifacts: 
    - OutputArtifact
  OutputVariables: 
    - String
  Region: String
  RoleArn: String
  RunOrder: Integer
  TimeoutInMinutes: Integer

```

## Properties

**`ActionTypeId`**
 

Specifies the action type and the provider of the action. 

Required: Yes

Type: ActionTypeId

Update requires: No interruption

**`Commands`**
 

The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild. Note

Using compute time for this action will incur separate charges in AWS CodeBuild. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`Configuration`**
 

The action's configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide. For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide. 

The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows: 

 JSON:  

 `"Configuration" : { Key : Value },`  

Required: No

Type: Json

Update requires: No interruption

**`EnvironmentVariables`**
 

The environment variables for the action. 

Required: No

Type: Array of EnvironmentVariable

Minimum: `1`

Maximum: `10`

Update requires: No interruption

**`InputArtifacts`**
 

The name or ID of the artifact consumed by the action, such as a test or build artifact. While the field is not a required parameter, most actions have an action configuration that requires a specified quantity of input artifacts. To refer to the action configuration specification by action provider, see the Action structure reference in the AWS CodePipeline User Guide. Note

For a CodeBuild action with multiple input artifacts, one of your input sources must be designated the PrimarySource. For more information, see the CodeBuild action reference page in the AWS CodePipeline User Guide. 

Required: No

Type: Array of InputArtifact

Update requires: No interruption

**`Name`**
 

The action declaration's name. 

Required: Yes

Type: String

Pattern: `[A-Za-z0-9.@\-_]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

**`Namespace`**
 

The variable namespace associated with the action. All variables produced as output by this action fall under this namespace. 

Required: No

Type: String

Pattern: `[A-Za-z0-9@\-_]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

**`OutputArtifacts`**
 

The name or ID of the result of the action declaration, such as a test or build artifact. While the field is not a required parameter, most actions have an action configuration that requires a specified quantity of output artifacts. To refer to the action configuration specification by action provider, see the Action structure reference in the AWS CodePipeline User Guide. 

Required: No

Type: Array of OutputArtifact

Update requires: No interruption

**`OutputVariables`**
 

The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `15`

Update requires: No interruption

**`Region`**
 

The action declaration's AWS Region, such as us-east-1. 

Required: No

Type: String

Minimum: `4`

Maximum: `30`

Update requires: No interruption

**`RoleArn`**
 

The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline. 

Required: No

Type: String

Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`

Update requires: No interruption

**`RunOrder`**
 

The order in which actions are run. 

Required: No

Type: Integer

Minimum: `1`

Maximum: `999`

Update requires: No interruption

**`TimeoutInMinutes`**
 

A timeout duration in minutes that can be applied against the ActionType’s default timeout value specified in Quotas for AWS CodePipeline. This attribute is available only to the manual approval ActionType. 

Required: No

Type: Integer

Minimum: `5`

Maximum: `86400`

Update requires: No interruption

