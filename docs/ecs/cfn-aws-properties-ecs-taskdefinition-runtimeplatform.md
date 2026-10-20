> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-runtimeplatform.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskDefinition RuntimePlatform

Information about the platform for the Amazon ECS service or task.

For more information about `RuntimePlatform`, see RuntimePlatform in the Amazon Elastic Container Service Developer Guide.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "CpuArchitecture" : String,
  "OperatingSystemFamily" : String
}

```

### YAML

```
  CpuArchitecture: String
  OperatingSystemFamily: String

```

## Properties

**`CpuArchitecture`** 

The CPU architecture. 

You can run your Linux tasks on an ARM-based platform by setting the value to `ARM64`. This option is available for tasks that run on Linux Amazon EC2 instance, Amazon ECS Managed Instances, or Linux containers on Fargate. 

Required: No

Type: String

Allowed values: `X86_64 | ARM64`

Update requires: Replacement

**`OperatingSystemFamily`** 

The operating system. 

Required: No

Type: String

Allowed values: `WINDOWS_SERVER_2019_FULL | WINDOWS_SERVER_2019_CORE | WINDOWS_SERVER_2016_FULL | WINDOWS_SERVER_2004_CORE | WINDOWS_SERVER_2022_CORE | WINDOWS_SERVER_2022_FULL | WINDOWS_SERVER_2025_CORE | WINDOWS_SERVER_2025_FULL | WINDOWS_SERVER_20H2_CORE | LINUX`

Update requires: Replacement
