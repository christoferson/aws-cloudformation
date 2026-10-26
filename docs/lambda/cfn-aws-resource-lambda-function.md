> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html
> Downloaded: 2026-10-25

# AWS::Lambda::Function

The `AWS::Lambda::Function` resource creates a Lambda function. To create a function, you need a deployment package and an execution role. The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.

Event Functions is the name for the original Lambda function type, and the Lambda console labels it Event function. The `AWS::Lambda::Function` resource type and its properties still use function, so you don't need to change your templates.

You set the package type to `Image` if the deployment package is a container image. For these functions, include the URI of the container image in the Amazon ECR registry in the `ImageUri` property of the `Code` property. You do not need to specify the handler and runtime properties. 

You set the package type to `Zip` if the deployment package is a .zip file archive. For these functions, specify the Amazon S3 location of your .zip file in the `Code` property. Alternatively, for Node.js and Python functions, you can define your function inline in the `ZipFile` property of the `Code` property. In both cases, you must also specify the handler and runtime properties.

You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with `UpdateFunctionCode`, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.

When you update a `AWS::Lambda::Function` resource, CloudFormation calls the UpdateFunctionConfiguration and UpdateFunctionCodeLambda APIs under the hood. Because these calls happen sequentially, and invocations can happen between these calls, your function may encounter errors in the time between the calls. For example, if you remove an environment variable, and the code that references that environment variable in the same CloudFormation update, you may see invocation errors related to a missing environment variable. To work around this, you can invoke your function against a version or alias by default, rather than the `$LATEST` version.

Note that you configure  provisioned concurrency on a `AWS::Lambda::Version` or a `AWS::Lambda::Alias`.

For a complete introduction to Lambda functions, see What is Lambda? in the Lambda developer guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Lambda::Function",
  "Properties" : {
      "Architectures" : [ String, ... ],
      "CapacityProviderConfig" : CapacityProviderConfig,
      "Code" : Code,
      "CodeSigningConfigArn" : String,
      "DeadLetterConfig" : DeadLetterConfig,
      "Description" : String,
      "DurableConfig" : DurableConfig,
      "Environment" : Environment,
      "EphemeralStorage" : EphemeralStorage,
      "FileSystemConfigs" : [ FileSystemConfig, ... ],
      "FunctionName" : String,
      "FunctionScalingConfig" : FunctionScalingConfig,
      "Handler" : String,
      "ImageConfig" : ImageConfig,
      "KmsKeyArn" : String,
      "Layers" : [ String, ... ],
      "LoggingConfig" : LoggingConfig,
      "MemorySize" : Integer,
      "PackageType" : String,
      "PublishToLatestPublished" : Boolean,
      "RecursiveLoop" : String,
      "ReservedConcurrentExecutions" : Integer,
      "Role" : String,
      "Runtime" : String,
      "RuntimeManagementConfig" : RuntimeManagementConfig,
      "SnapStart" : SnapStart,
      "Tags" : [ Tag, ... ],
      "TenancyConfig" : TenancyConfig,
      "Timeout" : Integer,
      "TracingConfig" : TracingConfig,
      "VpcConfig" : VpcConfig
    }
}

```

### YAML

```
Type: AWS::Lambda::Function
Properties:
  Architectures: 
    - String
  CapacityProviderConfig: 
    CapacityProviderConfig
  Code: 
    Code
  CodeSigningConfigArn: String
  DeadLetterConfig: 
    DeadLetterConfig
  Description: String
  DurableConfig: 
    DurableConfig
  Environment: 
    Environment
  EphemeralStorage: 
    EphemeralStorage
  FileSystemConfigs: 
    - FileSystemConfig
  FunctionName: String
  FunctionScalingConfig: 
    FunctionScalingConfig
  Handler: String
  ImageConfig: 
    ImageConfig
  KmsKeyArn: String
  Layers: 
    - String
  LoggingConfig: 
    LoggingConfig
  MemorySize: Integer
  PackageType: String
  PublishToLatestPublished: Boolean
  RecursiveLoop: String
  ReservedConcurrentExecutions: Integer
  Role: String
  Runtime: String
  RuntimeManagementConfig: 
    RuntimeManagementConfig
  SnapStart: 
    SnapStart
  Tags: 
    - Tag
  TenancyConfig: 
    TenancyConfig
  Timeout: Integer
  TracingConfig: 
    TracingConfig
  VpcConfig: 
    VpcConfig

```

## Properties

**`Architectures`** 

The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is `x86_64`. 

Required: No

Type: Array of String

Allowed values: `x86_64 | arm64`

Minimum: `1`

Maximum: `1`

Update requires: No interruption

**`CapacityProviderConfig`** 

Configuration for the capacity provider that manages compute resources for Lambda functions. 

Required: No

Type: CapacityProviderConfig

Update requires: No interruption

**`Code`** 

The code for the function. You can define your function code in multiple ways:  
For .zip deployment packages, you can specify the Amazon S3 location of the .zip file in the `S3Bucket`, `S3Key`, and `S3ObjectVersion` properties. 
For .zip deployment packages, you can alternatively define the function code inline in the `ZipFile` property. This method works only for Node.js and Python functions. 
For container images, specify the URI of your container image in the Amazon ECR registry in the `ImageUri` property. 
 

Required: Yes

Type: Code

Update requires: No interruption

**`CodeSigningConfigArn`** 

To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function. 

Required: No

Type: String

Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`

Update requires: No interruption

**`DeadLetterConfig`** 

A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead-letter queues. 

Required: No

Type: DeadLetterConfig

Update requires: No interruption

**`Description`** 

A description of the function. 

Required: No

Type: String

Maximum: `256`

Update requires: No interruption

**`DurableConfig`** 

Configuration settings for durable functions, including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads. 

Required: No

Type: DurableConfig

Update requires: Replacement

**`Environment`** 

Environment variables that are accessible from function code during execution. 

Required: No

Type: Environment

Update requires: No interruption

**`EphemeralStorage`** 

The size of the function's `/tmp` directory in MB. The default value is 512, but it can be any whole number between 512 and 10,240 MB. 

Required: No

Type: EphemeralStorage

Update requires: No interruption

**`FileSystemConfigs`** 

Connection settings for an Amazon EFS or Amazon S3 Files file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget or AWS::S3Files::MountTarget resource, you must also specify a `DependsOn` attribute to ensure that the mount target is created or updated before the function. 

For more information about using the `DependsOn` attribute, see DependsOn Attribute.  

Required: No

Type: Array of FileSystemConfig

Maximum: `1`

Update requires: No interruption

**`FunctionName`** 

The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CloudFormation generates one. 

If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. 

Required: No

Type: String

Minimum: `1`

Update requires: Replacement

**`FunctionScalingConfig`** 

Configuration that defines the scaling behavior for a Lambda Managed Instances function, including the minimum and maximum number of execution environments that can be provisioned. 

Required: No

Type: FunctionScalingConfig

Update requires: No interruption

**`Handler`** 

The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see Lambda programming model. 

Required: No

Type: String

Pattern: `^[^\s]+$`

Maximum: `128`

Update requires: No interruption

**`ImageConfig`** 

Configuration values that override the container image Dockerfile settings. For more information, see Container image settings. 

Required: No

Type: ImageConfig

Update requires: No interruption

**`KmsKeyArn`** 

The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:  
The function's environment variables. 
The function's Lambda SnapStart snapshots. 
When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see  Specifying a customer managed key for Lambda. 
The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see Function lifecycle. 
 

If you don't provide a customer managed key, Lambda uses an AWS owned key or an AWS managed key. 

Required: No

Type: String

Pattern: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`

Update requires: No interruption

**`Layers`** 

A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version. 

Required: No

Type: Array of String

Update requires: No interruption

**`LoggingConfig`** 

The function's Amazon CloudWatch Logs configuration settings. 

Required: No

Type: LoggingConfig

Update requires: No interruption

**`MemorySize`** 

The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB. Note that new AWS accounts have reduced concurrency and memory quotas. AWS raises these quotas automatically based on your usage. You can also request a quota increase. 

Required: No

Type: Integer

Minimum: `128`

Maximum: `32768`

Update requires: No interruption

**`PackageType`** 

The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive. 

Required: No

Type: String

Allowed values: `Image | Zip`

Update requires: Replacement

**`PublishToLatestPublished`**

Property description not available.

Required: No

Type: Boolean

Update requires: No interruption

**`RecursiveLoop`** 

The status of your function's recursive loop detection configuration. 

When this value is set to `Allow`and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action. 

When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.  

Required: No

Type: String

Allowed values: `Allow | Terminate`

Update requires: No interruption

**`ReservedConcurrentExecutions`** 

The number of simultaneous executions to reserve for the function. 

Required: No

Type: Integer

Minimum: `0`

Update requires: No interruption

**`Role`** 

The Amazon Resource Name (ARN) of the function's execution role. 

Required: Yes

Type: String

Pattern: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

Update requires: No interruption

**`Runtime`** 

The identifier of the function's  runtime. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image. 

The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see Runtime use after deprecation. 

For a list of all currently supported runtimes, see Supported runtimes. 

Required: No

Type: String

Allowed values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

Update requires: No interruption

**`RuntimeManagementConfig`** 

Sets the runtime management configuration for a function's version. For more information, see Runtime updates. 

Required: No

Type: RuntimeManagementConfig

Update requires: No interruption

**`SnapStart`** 

The function's AWS Lambda SnapStart setting. 

Required: No

Type: SnapStart

Update requires: No interruption

**`Tags`** 

A list of tags to apply to the function. Note

You must have the `lambda:TagResource`, `lambda:UntagResource`, and `lambda:ListTags` permissions for your IAM principal to manage the CloudFormation stack. If you don't have these permissions, there might be unexpected behavior with stack-level tags propagating to the resource during resource creation and update. 

Required: No

Type: Array of Tag

Update requires: No interruption

**`TenancyConfig`** 

The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant. 

Required: No

Type: TenancyConfig

Update requires: Replacement

**`Timeout`** 

The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds, and the maximum allowed value is 900 seconds. For functions using Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum allowed value of 5,400 seconds (90 minutes). For more information, see Lambda execution environment. 

Required: No

Type: Integer

Minimum: `1`

Update requires: No interruption

**`TracingConfig`** 

Set `Mode` to `Active` to sample and trace a subset of incoming requests with X-Ray. 

Required: No

Type: TracingConfig

Update requires: No interruption

**`VpcConfig`** 

For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see Configuring a Lambda function to access resources in a VPC. 

Required: No

Type: VpcConfig

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`Arn`** 

The Amazon Resource Name (ARN) of the function. 

**`SnapStartResponse.ApplyOn`**

Property description not available.

**`SnapStartResponse.OptimizationStatus`**

Property description not available.

## Examples
Function
Inline Function
VPC Function
 

### Function

Create a Node.js function.

#### JSON

```
"AMIIDLookup": {
    "Type": "AWS::Lambda::Function",
    "Properties": {
        "Handler": "index.handler",
        "Role": {
            "Fn::GetAtt": [
                "LambdaExecutionRole",
                "Arn"
            ]
        },
        "Code": {
            "S3Bucket": "amzn-s3-demo-bucket",
            "S3Key": "amilookup.zip"
        },
        "Runtime": "nodejs20.x",
        "Timeout": 25,
        "TracingConfig": {
            "Mode": "Active"
        }
    }
}
```
 

### Inline Function

Inline Node.js function that lists Amazon S3 buckets in ` us-east-1 `. Before using this example, make sure that your execution role has Amazon S3 read permissions.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Lambda function ListBucketsCommand.
Resources:
  primer:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: nodejs20.x
      Role: arn:aws:iam::111122223333:role/lambda-role
      Handler: index.handler
      Code:
        ZipFile: |
          const { S3Client, ListBucketsCommand } = require("@aws-sdk/client-s3");
          const s3 = new S3Client({ region: "us-east-1" }); // replace "us-east-1" with your AWS Region

          exports.handler = async function(event) {
            const command = new ListBucketsCommand({});
            const response = await s3.send(command);
            return response.Buckets;
          };
      Description: List Amazon S3 buckets in us-east-1.
      TracingConfig:
        Mode: Active
```
 

### VPC Function

Function connected to a VPC.

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC function.
Resources:
  Function:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Role: arn:aws:iam::111122223333:role/lambda-role
      Code:
        S3Bucket: amzn-s3-demo-bucket
        S3Key: function.zip
      Runtime: nodejs20.x
      Timeout: 5
      TracingConfig:
        Mode: Active
      VpcConfig:
        SecurityGroupIds:
          - sg-085912345678492fb
        SubnetIds:
          - subnet-071f712345678e7c8
          - subnet-07fd123456788a036
```
