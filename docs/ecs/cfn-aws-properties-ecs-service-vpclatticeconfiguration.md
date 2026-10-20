> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-vpclatticeconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service VpcLatticeConfiguration

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "AdvancedConfiguration" : VpcLatticeAdvancedConfiguration,
  "PortName" : String,
  "RoleArn" : String,
  "TargetGroupArn" : String
}

```

### YAML

```
  AdvancedConfiguration: 
    VpcLatticeAdvancedConfiguration
  PortName: String
  RoleArn: String
  TargetGroupArn: String

```

## Properties

**`AdvancedConfiguration`**

Property description not available.

Required: No

Type: VpcLatticeAdvancedConfiguration

Update requires: No interruption

**`PortName`** 

The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition. 

Required: Yes

Type: String

Update requires: No interruption

**`RoleArn`** 

The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure. 

Required: Yes

Type: String

Update requires: No interruption

**`TargetGroupArn`** 

The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to. 

Required: Yes

Type: String

Update requires: No interruption
