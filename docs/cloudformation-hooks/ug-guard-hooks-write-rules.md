> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.html
> Downloaded: 2026-10-22

# Write Guard rules to evaluate resources for Guard Hooks

AWS CloudFormation Guard is an open-source and general purpose domain specific language (DSL) you can use to author policy-as-code. This topic explains how to use Guard to author example rules which can be run in the Guard Hook to automatically evaluate CloudFormation and AWS Cloud Control API operations. It will also focus on the different types of inputs available to your Guard rules depending on when your Guard Hook runs. A Guard Hook can be configured to run during the following types of operations: 
Resource operations 
Stack operations 
Change set operations 

For more information on writing Guard rules, see Writing AWS CloudFormation Guard rulesTopics
Resource operation Guard rules
Stack operation Guard rules
Change set operation Guard rules
 

## Resource operation Guard rules 

Any time you create, update, or delete a resource, that's considered a resource operation. As an example, if you run update a CloudFormation stack that creates a new resource, you have completed a resource operation. When you create, update or delete a resource using Cloud Control API, that is also considered a resource operation. You can configure your Guard Hook to target `RESOURCE` and `CLOUD_CONTROL` operations in the `TargetOperations` configuration for your Hook. When your Guard Hook evaluates a resource operation, the Guard engine evaluates a resource input. Topics
Guard resource input syntax
Example Guard resource operation input
Guard rules for resource changes
 

### Guard resource input syntax 

The Guard resource input is the data that's made available to your Guard rules to evaluate. 

The following is an example shape of a resource input: 

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: String
  TargetType: RESOURCE
  TargetLogicalId: String
  ChangeSetId: String
Resources:
  {ResourceLogicalID}:
    ResourceType: {ResourceType}
    ResourceProperties:
        {ResourceProperties}
Previous:
  ResourceLogicalID:
    ResourceType: {ResourceType}
    ResourceProperties:
        {PreviousResourceProperties}
```
   

**`HookContext`**    

**`AWSAccountID`**  

The ID of the AWS account containing the resource being evaluated.  

**`StackId`**  

The stack ID of the CloudFormation stack that is part of the resource operation. This is empty if the caller is Cloud Control API.  

**`HookTypeName`**  

The name of the Hook that's running.  

**`HookTypeVersion`**  

The version of the Hook that is running.  

**`InvocationPoint`**  

The exact point in the provisioning logic where the Hook runs. 

Valid values: (`CREATE_PRE_PROVISION` | `UPDATE_PRE_PROVISION` | `DELETE_PRE_PROVISION`)  

**`TargetName`**  

The target type being evaluated, for example, `AWS::S3::Bucket`.  

**`TargetType`**  

The target type being evaluated, for example `AWS::S3::Bucket`. For resources provisioned with Cloud Control API, this value will be `RESOURCE`.  

**`TargetLogicalId`**  

The `TargetLogicalId` of the resource being evaluated. If the origin of the Hook is CloudFormation, this will be the logical ID (also known as logical name) of the resource. If the origin of the Hook is Cloud Control API, this will be a constructed value.  

**`ChangeSetId`**  

The change set ID that was executed to cause the Hook invocation. This value is empty if the resource change was initiated by Cloud Control API, or the `create-stack`, `update-stack`, or `delete-stack` operations.    

**`Resources`**    

**`ResourceLogicalID`**  

When the operation is initiated by CloudFormation, the `ResourceLogicalID` is the logical ID of the resource in the CloudFormation template. 

When the operation's initiated by Cloud Control API, the `ResourceLogicalID` is a combination of the resource type, name, operation ID, and request ID.  

**`ResourceType`**  

The type name of the resource (example: `AWS::S3::Bucket`).  

**`ResourceProperties`**  

The proposed properties of the resource being modified. When the Guard Hook is running against the CloudFormation resource changes, any functions, parameters, and transforms will be fully resolved. If the resource is being deleted, this value will be empty.    

**`Previous`**    

**`ResourceLogicalID`**  

When the operation is initiated by CloudFormation, the `ResourceLogicalID` is the logical ID of the resource in the CloudFormation template. 

When the operation's initiated by Cloud Control API, the `ResourceLogicalID` is a combination of the resource type, name, operation ID, and request ID.  

**`ResourceType`**  

The type name of the resource (example: `AWS::S3::Bucket`).  

**`ResourceProperties`**  

The current properties associated with the resource being modified. If the resource is being deleted, this value will be empty.     

### Example Guard resource operation input 

The following example input shows a Guard Hook that will receive the definition of the `AWS::S3::Bucket` resource to update. This is the data available to Guard for evaluation. 

```
HookContext:
  AwsAccountId: "123456789012"
  StackId: "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000"
  HookTypeName: org::s3policy::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: AWS::S3::Bucket
  TargetType: RESOURCE
  TargetLogicalId: MyS3Bucket
  ChangeSetId: ""
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket
      ObjectLockEnabled: true
Previous:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket
      ObjectLockEnabled: false
```
 

To see all of the properties available for the resource type, see AWS::S3::Bucket. 

### Guard rules for resource changes 

When a Guard Hook evaluates resource changes, it starts by downloading all the rules configured with the Hook. These rules are then evaluated against the resource input. The Hook will fail if any rules fail their evaluation. If there are no failures, the Hook will pass. 

The following example is a Guard rule that evaluates if the `ObjectLockEnabled` property is `true` for any `AWS::S3::Bucket` resource types. 

```
let s3_buckets_default_lock_enabled = Resources.*[ Type == 'AWS::S3::Bucket']

rule S3_BUCKET_DEFAULT_LOCK_ENABLED when %s3_buckets_default_lock_enabled !empty {
  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled exists
  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled == true
  <<
    Violation: S3 Bucket ObjectLockEnabled must be set to true.
    Fix: Set the S3 property ObjectLockEnabled parameter to true.
  >>
}
```
 

When this rule runs against the following input, it will fail since the `ObjectLockEnabled` property isn't set to `true`. 

```
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket 
      ObjectLockEnabled: false
```
 

When this rule runs against the following input, it will pass since the `ObjectLockEnabled` is set to `true`. 

```
Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: amzn-s3-demo-bucket
      ObjectLockEnabled: true
```
 

When a Hook fails, the rules which failed will be propagated back to CloudFormation or Cloud Control API. If a logging bucket has been configured for the Guard Hook, additional rule feedback will be provided there. This additional feedback includes the `Violation` and `Fix` information. 

## Stack operation Guard rules 

When a CloudFormation stack is created, updated, or deleted, you can configure your Guard Hook to start by evaluating the new template and potentially block the stack operation from proceeding. You can configure your Guard Hook to target `STACK` operations in the `TargetOperations` configuration for your Hook. Topics
Guard stack input syntax
Example Guard stack operation input
Guard rules for stack changes
 

### Guard stack input syntax 

The input for Guard stack operations provides the whole CloudFormation template for your Guard rules to evaluate. 

The following is an example shape of a stack input: 

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: String
  TargetType:STACK
  ChangeSetId: String
{Proposed CloudFormation Template}
Previous:
    {CloudFormation Template}
```
   

**`HookContext`**    

**`AWSAccountID`**  

The ID of the AWS account containing the resource.  

**`StackId`**  

The stack ID of the CloudFormation stack that is part of the stack operation.  

**`HookTypeName`**  

The name of the Hook that's running.  

**`HookTypeVersion`**  

The version of the Hook that is running.  

**`InvocationPoint`**  

The exact point in the provisioning logic where the Hook runs. 

Valid values: (`CREATE_PRE_PROVISION` | `UPDATE_PRE_PROVISION` | `DELETE_PRE_PROVISION`)  

**`TargetName`**  

The name of the stack being evaluated.  

**`TargetType`**  

This value will be `STACK` when running as a stack-level Hook.  

**`ChangeSetId`**  

The change set ID that was executed to cause the Hook invocation. This value is empty if the stack operation was initiated by a `create-stack`, `update-stack`, or `delete-stack` operation.    

**`Proposed CloudFormation Template`**  

The full CloudFormation template value that was passed to CloudFormation `create-stack` or `update-stack` operations. This includes things like the `Resources`, `Outputs`, and `Properties`. It can be a JSON or YAML string depending on what was provided to CloudFormation. 

In `delete-stack` operations, this value will be empty.  

**`Previous`**  

The last successfully deployed CloudFormation template. This value is empty if the stack is being created or deleted. 

In `delete-stack` operations, this value will be empty.   Note

The templates provided are what is passed into `create` or `update` stack operations. When deleting a stack, no template values are provided. 

### Example Guard stack operation input 

The following example input shows a Guard Hook that will receive a full template and the previously deployed template. The template in this example is using the JSON format. 

```
HookContext:
  AwsAccountId: 123456789012
  StackId: "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000"
  HookTypeName: org::templatechecker::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: MyStack
  TargetType: CHANGE_SET
  TargetLogicalId: arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000
  ChangeSetId: arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000
Resources: {
   "S3Bucket": {
        "Type": "AWS::S3::Bucket",
        "Properties": {
           "BucketEncryption": {
               "ServerSideEncryptionConfiguration": [ 
                {"ServerSideEncryptionByDefault": 
                    {"SSEAlgorithm": "aws:kms", 
                      "KMSMasterKeyID": "KMS-KEY-ARN" }, 
                      "BucketKeyEnabled": true } 
                ] 
           }
        }
}
Previous: {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {}
        }
    }
}
```
 

### Guard rules for stack changes 

When a Guard Hook evaluates stack changes, it starts by downloading all the rules configured with the Hook. These rules are then evaluated against the resource input. The Hook will fail if any rules fail their evaluation. If there are no failures, the Hook will pass. 

The following example is a Guard rule that evaluates if there are any `AWS::S3::Bucket` resource types containing a property called `BucketEncryption`, with the `SSEAlgorithm` set to either `aws:kms` or `AES256`. 

```
let s3_buckets_s3_default_encryption = Resources.*[ Type == 'AWS::S3::Bucket']

rule S3_DEFAULT_ENCRYPTION_KMS when %s3_buckets_s3_default_encryption !empty {
  %s3_buckets_s3_default_encryption.Properties.BucketEncryption exists
  %s3_buckets_s3_default_encryption.Properties.BucketEncryption.ServerSideEncryptionConfiguration[*].ServerSideEncryptionByDefault.SSEAlgorithm in ["aws:kms","AES256"]
  <<
    Violation: S3 Bucket default encryption must be set.
    Fix: Set the S3 Bucket property BucketEncryption.ServerSideEncryptionConfiguration.ServerSideEncryptionByDefault.SSEAlgorithm to either "aws:kms" or "AES256"
  >>
}
```
 

When the rule runs against the following template, it will `fail`. 

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket without default encryption
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
```
 

When the rule runs against the following template, it will `pass`. 

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket with default encryption using SSE-KMS with an S3 Bucket Key
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: KMS-KEY-ARN
            BucketKeyEnabled: true
```
 

## Change set operation Guard rules 

When a CloudFormation change set is created, you can configure your Guard Hook to evaluate the template and changes proposed in the change set to block the change set execution. Topics
Guard change set input syntax
Example Guard change set operation input
Guard rule for change set operations
 

### Guard change set input syntax 

The Guard change set input is the data that's made available to your Guard rules to evaluate. 

The following is an example shape of a change set input: 

```
HookContext:
  AWSAccountID: String
  StackId: String
  HookTypeName: String
  HookTypeVersion: String
  InvocationPoint: [CREATE_PRE_PROVISION, UPDATE_PRE_PROVISION, DELETE_PRE_PROVISION]
  TargetName: CHANGE_SET
  TargetType:CHANGE_SET
  TargetLogicalId:ChangeSet ID
  ChangeSetId: String
{Proposed CloudFormation Template}
Previous:
  {CloudFormation Template}
Changes: [{ResourceChange}]
```
 

The `ResourceChange` model syntax is: 

```
logicalResourceId: String 
resourceType: String
action: CREATE, UPDATE, DELETE
lineNumber: Number
beforeContext: JSON String
afterContext: JSON String 
```
   

**`HookContext`**    

**`AWSAccountID`**  

The ID of the AWS account containing the resource.  

**`StackId`**  

The stack ID of the CloudFormation stack that is part of the stack operation.  

**`HookTypeName`**  

The name of the Hook that's running.  

**`HookTypeVersion`**  

The version of the Hook that is running.  

**`InvocationPoint`**  

The exact point in the provisioning logic where the Hook runs. 

Valid values: (`CREATE_PRE_PROVISION` | `UPDATE_PRE_PROVISION` | `DELETE_PRE_PROVISION`)  

**`TargetName`**  

The name of the stack being evaluated.  

**`TargetType`**  

This value will be `CHANGE_SET` when running as a change set-level Hook.  

**`TargetLogicalId`**  

This value will be the ARN of the change set.  

**`ChangeSetId`**  

The change set ID that was executed to cause the Hook invocation. This value is empty if the stack operation was initiated by a `create-stack`, `update-stack`, or `delete-stack` operation.    

**`Proposed CloudFormation Template`**  

The full CloudFormation template that was provided to a `create-change-set` operation. It can be a JSON or YAML string depending on what was provided to CloudFormation.  

**`Previous`**  

The last successfully deployed CloudFormation template. This value is empty if the stack is being created or deleted.  

**`Changes`**  

The `Changes` model. This lists the resource changes.     

**Changes**    

**logicalResourceId**  

The logical resource name of the changed resource.  

**resourceType**  

The resource type that will be changed.  

**action**  

The type of operation being performed on the resource. 

Valid values: (`CREATE` | `UPDATE` | `DELETE`)  

**lineNumber**  

The line number in the template associated with the change.  

**beforeContext**  

A JSON string of properties of the resource before the change: 

```
{"properties": {"property1": "value"}}
```
  

**afterContext**  

A JSON string of properties of the resource after the change: 

```
{"properties": {"property1": "new value"}}
```
     

### Example Guard change set operation input 

The following example input shows a Guard Hook that will receive a full template, the previously deployed template, and a list of resource changes. The template in this example is using the JSON format. 

```
HookContext:
  AwsAccountId: "00000000"
  StackId: MyStack
  HookTypeName: org::templatechecker::hook
  HookTypeVersion: "00001"
  InvocationPoint: UPDATE_PRE_PROVISION
  TargetName: my-example-stack
  TargetType:STACK
  TargetLogicalId: arn...:changeSet/change-set
  ChangeSetId: ""
Resources: {
    "S3Bucket": {
       "Type": "AWS::S3::Bucket",
       "Properties": {
           "BucketName": "amzn-s3-demo-bucket",
           "VersioningConfiguration":{
              "Status": "Enabled"
            }                
         }
    }
Previous: {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "amzn-s3-demo-bucket",
                "VersioningConfiguration":{
                  "Status": "Suspended"
                }
            }
        }
    }
}
Changes: [
  {
    "logicalResourceId": "S3Bucket",
    "resourceType": "AWS::S3::Bucket",
    "action": "UPDATE",
    "lineNumber": 5,
    "beforeContext": "{\"Properties\":{\"VersioningConfiguration\":{\"Status\":\"Suspended\"}}}",
    "afterContext": "{\"Properties\":{\"VersioningConfiguration\":{\"Status\":\"Enabled\"}}}"
  }
]

```
 

### Guard rule for change set operations 

The following example is a Guard rule that evaluates changes to Amazon S3 buckets, and ensures that `VersionConfiguration` is not disabled. 

```
let s3_buckets_changing = Changes[resourceType == 'AWS::S3::Bucket']

rule S3_VERSIONING_STAY_ENABLED when %s3_buckets_changing !empty {
    let afterContext = json_parse(%s3_buckets_changing.afterContext)
    when %afterContext.Properties.VersioningConfiguration.Status !empty {
        %afterContext.Properties.VersioningConfiguration.Status == 'Enabled'
    }
}
```
