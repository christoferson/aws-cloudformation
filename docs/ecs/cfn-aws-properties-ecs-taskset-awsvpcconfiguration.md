> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskset-awsvpcconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::TaskSet AwsVpcConfiguration

An object representing the networking details for a task or service. For example `awsVpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"]}`.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AssignPublicIp" : String,
  "SecurityGroups" : [ String, ... ],
  "Subnets" : [ String, ... ]
}

```

### YAML

```
  AssignPublicIp: String
  SecurityGroups: 
    - String
  Subnets: 
    - String

```

## Properties

**`AssignPublicIp`** 

Whether the task's elastic network interface receives a public IP address.  

Consider the following when you set this value:  
When you use `create-service` or `update-service`, the default is `DISABLED`.  
When the service `deploymentController` is `ECS`, the value must be `DISABLED`.  
 

Required: No

Type: String

Allowed values: `DISABLED | ENABLED`

Update requires: Replacement

**`SecurityGroups`** 

The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified. Note

All specified security groups must be from the same VPC. 

Required: No

Type: Array of String

Maximum: `5`

Update requires: Replacement

**`Subnets`** 

The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified. Note

All specified subnets must be from the same VPC. 

Required: Yes

Type: Array of String

Maximum: `16`

Update requires: Replacement
