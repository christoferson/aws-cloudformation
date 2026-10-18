> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-ruledeclaration.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline RuleDeclaration

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see Stage conditions and How do stage conditions work?. For more information about rules, see the AWS CodePipeline rule reference.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Commands" : [ String, ... ],
  "Configuration" : Json,
  "InputArtifacts" : [ InputArtifact, ... ],
  "Name" : String,
  "Region" : String,
  "RoleArn" : String,
  "RuleTypeId" : RuleTypeId
}

```

### YAML

```
  Commands: 
    - String
  Configuration: Json
  InputArtifacts: 
    - InputArtifact
  Name: String
  Region: String
  RoleArn: String
  RuleTypeId: 
    RuleTypeId

```

## Properties

**`Commands`**
 

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild. Note

Using compute time for this action will incur separate charges in AWS CodeBuild. 

Required: No

Type: Array of String

Minimum: `1`

Maximum: `50`

Update requires: No interruption

**`Configuration`**
 

The action configuration fields for the rule. 

Required: No

Type: Json

Update requires: No interruption

**`InputArtifacts`**
 

The input artifacts fields for the rule, such as specifying an input file for the rule. 

Required: No

Type: Array of InputArtifact

Update requires: No interruption

**`Name`**
 

The name of the rule that is created for the condition, such as `VariableCheck`. 

Required: No

Type: String

Pattern: `[A-Za-z0-9.@\-_]+`

Minimum: `1`

Maximum: `100`

Update requires: No interruption

**`Region`**
 

The Region for the condition associated with the rule. 

Required: No

Type: String

Minimum: `4`

Maximum: `30`

Update requires: No interruption

**`RoleArn`**
 

The pipeline role ARN associated with the rule. 

Required: No

Type: String

Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`

Update requires: No interruption

**`RuleTypeId`**
 

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. 

Required: No

Type: RuleTypeId

Update requires: No interruption

