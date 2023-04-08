## SSM Cloudformation Template

### SSM - Document Run Command


### SSM - Automation

(ssm-automation)[ssm-automation.yaml]

### SSM Parameter

To create an SSM parameter, you must have the AWS Identity and Access Management (IAM) permissions ssm:PutParameter and ssm:AddTagsToResource. ssm:RemoveTagsFromResource



### SSM Parameter - Standard Tier - String

(ssm-parameter-std-string)[ssm-parameter-std-string.yaml]

### SSM Parameter - Reference

(ssm-parameter)[ssm-parameter.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html

- (ssm-document-schema)[https://docs.aws.amazon.com/systems-manager/latest/userguide/document-schemas-features.html]

### Links (SSM Parameter)

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html

### Errors (Parameter Registration)

- Parameter name: can't be prefixed with "ssm" (case-insensitive). If formed as a path, it can consist of sub-paths divided by slash symbol; each sub-path can be formed as a mix of letters, numbers and the following 3 symbols .-_ 

- Parameter value, cannot be validated against allowedPattern: ^[a-zA-Z]{1,10}$

### TODO

- [X] Create Parameter - Standard - String

- [ ] Create Parameter - Standard - List of Strings

- [ ] Create Parameter - Standard - Secret (Not Supported in CF)

- [ ] Create Parameter - Advanced - String

- [ ] Create Parameter - Advanced - List of Strings

- [ ] Create Parameter - Advanced - Secret (Not Supported in CF)

- [ ] ssm:StartSession Condition StringLike ssm:resourceTag/Environment : ["Dev"]