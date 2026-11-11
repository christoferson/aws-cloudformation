<!-- Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html -->
<!-- Downloaded: 2026-11-12 -->

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::NetworkConnector VpcEgressConfiguration

The VPC egress configuration for the network connector. Specifies the subnets, security groups, and network protocol for routing outbound traffic through your VPC.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "[AssociatedComputeResourceTypes](#cfn-lambda-networkconnector-vpcegressconfiguration-associatedcomputeresourcetypes)" : [ String, ... ],
  "[NetworkProtocol](#cfn-lambda-networkconnector-vpcegressconfiguration-networkprotocol)" : String,
  "[SecurityGroupIds](#cfn-lambda-networkconnector-vpcegressconfiguration-securitygroupids)" : [ String, ... ],
  "[SubnetIds](#cfn-lambda-networkconnector-vpcegressconfiguration-subnetids)" : [ String, ... ]
}

```

### YAML

```
  [AssociatedComputeResourceTypes](#cfn-lambda-networkconnector-vpcegressconfiguration-associatedcomputeresourcetypes):
    - String
  [NetworkProtocol](#cfn-lambda-networkconnector-vpcegressconfiguration-networkprotocol): String
  [SecurityGroupIds](#cfn-lambda-networkconnector-vpcegressconfiguration-securitygroupids):
    - String
  [SubnetIds](#cfn-lambda-networkconnector-vpcegressconfiguration-subnetids):
    - String

```

## Properties

**`AssociatedComputeResourceTypes`**

The types of Lambda compute resources that can use this connector:

-

`MicroVm` – A Lambda function that runs on a MicroVM-based execution environment.
-

`WebFunction` – A Lambda web function with built-in HTTP endpoints.

*Required*: Yes

*Type*: Array of String

*Allowed values*: `MicroVm | WebFunction`

*Minimum*: `1`

*Maximum*: `1`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`NetworkProtocol`**

The network protocol for the connector. Specify `IPv4` for IPv4-only networking, or `DualStack` for both IPv4 and IPv6.

*Valid Values*: `IPv4` | `DualStack`

*Required*: Yes

*Type*: String

*Allowed values*: `IPv4 | DualStack`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`SecurityGroupIds`**

The IDs of the VPC security groups to attach to the ENIs. All security groups must be in the same VPC as the subnets.

*Required*: Yes

*Type*: Array of String

*Minimum*: `0 | 0`

*Maximum*: `1024 | 16`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

**`SubnetIds`**

The IDs of the VPC subnets where Lambda provisions elastic network interfaces (ENIs). Specify 1 to 16 subnets. All subnets must be in the same VPC.

*Required*: Yes

*Type*: Array of String

*Minimum*: `0 | 1`

*Maximum*: `1024 | 16`

*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
