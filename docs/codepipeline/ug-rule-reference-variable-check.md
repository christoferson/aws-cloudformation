> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-VariableCheck.html
> Downloaded: 2026-10-19

# VariableCheck

When you create a condition, you can add the `VariableCheck` rule. This section provides a reference for the rule parameters. For more information about rules and conditions, see How do stage conditions work?.

You can use the `VariableCheck` rule to create a condition where the output variable is checked against a provided expression. The rule passes the check when the variable value meets the rule criteria, such as the value being equal or greater than a specified output variable.Topics
Rule type
Configuration parameters
Example rule configuration
See also
 

## Rule type  
Category: `Rule` 
Owner: `AWS` 
Provider: `VariableCheck` 
Version: `1` 
 

## Configuration parameters   

**Operator**  

Required: Yes 

The operator that indicates which operation to perform for the variable check. 

In the following example, the output variable for the repository name will be checked for whether it is equal to `MyDemoRepo`. 

```
        "configuration": {
            "Variable": "#{SourceVariables.RepositoryName}",
            "Value": "MyDemoRepo",
            "Operator": "EQ"
        },
```
 

The following operators are available to create an expression as follows.  
Equals - Choose this operator to check whether the variable is equal to the string value. 

CLI parameter: `EQ` 
Contains - Choose this operator to check whether the variable contains the string value as a substring. 

CLI parameter: `CONTAINS` 
Matches - Choose this operator to check whether the variable matches a given regex expression as the string value.  

All regular expressions in CodePipeline conform to the Java regex syntax. For a comprehensive description of the Java regex syntax and its constructs, see java.util.regex.Pattern. 

CLI parameter: `MATCHES` 
Not equals - Choose this operator to check whether the variable is not equal to the string value. 

CLI parameter: `NE` 
  

**Variable**  

Required: Yes 

The pipeline variables to check.  

**Value**  

Required: Yes 

The value for the expression to check against. 

In the following example, the output variable for the repository name will be checked for whether it is equal to `MyDemoRepo`. 

```
        "configuration": {
            "Variable": "#{SourceVariables.RepositoryName}",
            "Value": "MyDemoRepo",
            "Operator": "EQ"
        },
```
   

In the following JSON example, two separate rules are defined, one for an `EQ` (equals) statement that checks the repository and branch name formatted as #{SourceVariables.RepositoryName} and one for `CONTAINS` that checks the commit message output variable formatted as #{SourceVariables.CommitMessage} against the provided value "update." 

```
  "beforeEntry": {
                    "conditions": [
                        {
                            "result": "FAIL",
                            "rules": [
                                {
                                    "name": "MyVarCheckRule",
                                    "ruleTypeId": {
                                        "category": "Rule",
                                        "owner": "AWS",
                                        "provider": "VariableCheck",
                                        "version": "1"
                                    },
                                    "configuration": {
                                        "Operator": "EQ",
                                        "Value": "MyDemoRepo",
                                        "Variable": "#{SourceVariables.RepositoryName}"
                                    },
                                    "inputArtifacts": [],
                                    "region": "us-east-1"
                                },
                                {
                                    "name": "MyVarCheckRuleContains",
                                    "ruleTypeId": {
                                        "category": "Rule",
                                        "owner": "AWS",
                                        "provider": "VariableCheck",
                                        "version": "1"
                                    },
                                    "configuration": {
                                        "Operator": "CONTAINS",
                                        "Value": "update",
                                        "Variable": "#{SourceVariables.CommitMessage}"
                                    },
                                    "inputArtifacts": [],
                                    "region": "us-east-1"
                                }
                            ]
                        }
                    ]
                }
            }
        ],
```
 

## Example rule configuration  

**YAML** 

```
- name: MyVariableCheck
  ruleTypeId:
    category: Rule
    owner: AWS
    provider: VariableCheck
    version: '1'
  configuration:
    Variable: "#{SourceVariables.RepositoryName}"
    Value: MyDemoRepo
    Operator: EQ
  inputArtifacts: []
  region: us-west-2
```
  

**JSON** 

```
"rules": [
    {
        "name": "MyVariableCheck",
        "ruleTypeId": {
            "category": "Rule",
            "owner": "AWS",
            "provider": "VariableCheck",
            "version": "1"
        },
        "configuration": {
            "Variable": "#{SourceVariables.RepositoryName}",
            "Value": "MyDemoRepo",
            "Operator": "EQ"
        },
        "inputArtifacts": [],
        "region": "us-west-2"
    }
]
```
   

## See also 

The following related resources can help you as you work with this rule.  
Tutorial: Create a variable check rule for a pipeline as an entry condition – This section provides a tutorial with steps for creating an On Entry condition with a variable check rule. 
Variables reference – This section provides reference information and examples for pipeline variables. 
For more information about rules and conditions, see Condition, RuleTypeId, and RuleExecution in the CodePipeline API Guide.
