<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/using-iac-with-gdu-automated-agents-runtime-monitoring.html -->
<!-- Downloaded: 2026-10-28 -->

# Using Infrastructure as Code (IaC) with GuardDuty automated security agents

Use this section only if the following list applies to your use case:

-

You use Infrastructure as Code (IaC) tools, such as AWS Cloud Development Kit (AWS CDK) and Terraform, to manage your AWS resources, and
-

You need to enable GuardDuty automated agent configuration for one or more resource types - Amazon EKS, Amazon EC2, or Amazon ECS-Fargate.

## IaC resource dependency graph overview

When you enable GuardDuty automated agent configuration for a resource type, GuardDuty automatically creates a VPC endpoint and a security group associated with this VPC endpoint, and installs the security agent for this resource type. By default, GuardDuty will delete the VPC endpoint and the associated security group only after you disable Runtime Monitoring. For more information, see [Disabling, uninstalling, and cleaning up resources in Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-resource-clean-up.html).

When you use an IaC tool, it maintains a dependency graph of resources. At the time of deletion of resources using the IaC tool, it only deletes resources that can be tracked as a part of dependency graph of resources. IaC tools may not know about the resources that are created outside of their specified configuration. For example, you create a VPC with an IaC tool and then add a security group to this VPC by using AWS console or an API operation. In the resource dependency graph, the VPC resource that you create depends on the associated security group. If you delete this VPC resource by using the IaC tool, then you will get an error. The way to get around this error is to delete the associated security group manually or to update the IaC configuration to include this added resource.

## Common issue - Deleting resources in IaC

When using GuardDuty automated agent configuration, you may want to delete a resource (Amazon EKS, Amazon EC2, or Amazon ECS-Fargate) that you created by using an IaC tool. However, this resource is dependent on a VPC endpoint that GuardDuty created. This prevents the IaC tool to delete the resource by itself and requires you to disable Runtime Monitoring, that further deletes the VPC endpoint automatically.

For example, when you attempt to delete the VPC endpoint that GuardDuty created on your behalf, you will get an error similar to the following examples.

###### Example

**Error example when using CDK**

```
The following resource(s) failed to delete: [mycdkvpcapplicationpublicsubnet1Subnet1SubnetEXAMPLE1, mycdkvpcapplicationprivatesubnet1Subnet2SubnetEXAMPLE2].
Resource handler returned message: "The subnet 'subnet-APKAEIVFHP46CEXAMPLE' has dependencies and cannot be deleted. (Service: Ec2, Status Code: 400, Request ID: e071c3c5-7442-4489-838c-0dfc6EXAMPLE)" (RequestToken: 4381cff8-6240-208a-8357-5557b7EXAMPLE, HandlerErrorCode: InvalidRequest)
```
[Show moreShow less](#)

###### Example

**Error example when using Terraform**

```
module.vpc.aws_subnet.private[1]: Still destroying... [id=subnet-APKAEIVFHP46CEXAMPLE, 19m50s elapsed]
module.vpc.aws_subnet.private[1]: Still destroying... [id=subnet-APKAEIVFHP46CEXAMPLE, 20m0s elapsed]

Error: deleting EC2 Subnet (subnet-APKAEIBAERJR2EXAMPLE): DependencyViolation: The subnet 'subnet-APKAEIBAERJR2EXAMPLE' has dependencies and cannot be deleted.
       status code: 400, request id: e071c3c5-7442-4489-838c-0dfc6EXAMPLE
```
[Show moreShow less](#)

###### Note

The Terraform AWS provider version 6.43.0 and later resolves this issue automatically. The AWS provider detects and removes GuardDuty-managed VPC endpoints and security groups during `terraform destroy`. This fix applies to all resource types (Amazon EKS, Amazon EC2, and Amazon ECS-Fargate).

### Solution - Prevent resource deletion issue

This section helps you manage the VPC endpoint and security group independent of GuardDuty.

To gain complete ownership of the resources configured by using the IaC tool, perform the following steps in the listed order:

1.

Create a VPC. To allow ingress permission, associate a GuardDuty VPC endpoint with the security group, to this VPC.
2.

Enable GuardDuty automated agent configuration for your resource type

After you complete the preceding steps, GuardDuty will not create its own VPC endpoint and will reuse the one that you created by using the IaC tool.

For information about creating your own VPC, see [Create a VPC only](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-only) in the *Amazon VPC Transit Gateways*. For information about creating a VPC endpoint, see the following section for your resource type:

-

For Amazon EC2, see [Prerequisite – Creating Amazon VPC endpoint manually](https://docs.aws.amazon.com/guardduty/latest/ug/creating-vpc-endpoint-ec2-agent-manually.html).
-

For Amazon EKS, see [Prerequisite – Creating an Amazon VPC endpoint](https://docs.aws.amazon.com/guardduty/latest/ug/eksrunmon-prereq-deploy-security-agent.html).
