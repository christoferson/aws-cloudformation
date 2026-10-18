> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-condition.html
> Downloaded: 2026-10-18


# AWS::CodePipeline::Pipeline Condition

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see Stage conditions and How do stage conditions work?.. For more information about rules, see the AWS CodePipeline rule reference.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Result" : String,
  "Rules" : [ RuleDeclaration, ... ]
}

```

### YAML

```
  Result: String
  Rules: 
    - RuleDeclaration

```

## Properties

**`Result`**
 

The action to be done when the condition is met. For example, rolling back an execution for a failure condition. 

Required: No

Type: String

Allowed values: `ROLLBACK | FAIL | RETRY | SKIP`

Update requires: No interruption

**`Rules`**
 

The rules that make up the condition. 

Required: No

Type: Array of RuleDeclaration

Minimum: `1`

Maximum: `5`

Update requires: No interruption

