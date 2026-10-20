> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-ulimit.html
> Downloaded: 2026-10-20

# AWS::ECS::DaemonTaskDefinition Ulimit

The `ulimit` settings to pass to the container.

Amazon ECS tasks hosted on AWS Fargate use the default resource limit values set by the operating system with the exception of the `nofile` resource limit parameter which AWS Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is ` 65535` and the default hard limit is `65535`.

You can specify the `ulimit` settings for a container in a task definition.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "HardLimit" : Integer,
  "Name" : String,
  "SoftLimit" : Integer
}

```

### YAML

```
  HardLimit: Integer
  Name: String
  SoftLimit: Integer

```

## Properties

**`HardLimit`** 

The hard limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`. 

Required: Yes

Type: Integer

Update requires: Replacement

**`Name`** 

The `type` of the `ulimit`. 

Required: Yes

Type: String

Allowed values: `core | cpu | data | fsize | locks | memlock | msgqueue | nice | nofile | nproc | rss | rtprio | rttime | sigpending | stack`

Update requires: Replacement

**`SoftLimit`** 

The soft limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`. 

Required: Yes

Type: Integer

Update requires: Replacement
