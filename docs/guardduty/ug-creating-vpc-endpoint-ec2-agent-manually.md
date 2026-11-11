<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/creating-vpc-endpoint-ec2-agent-manually.html -->
<!-- Downloaded: 2026-10-28 -->

# Prerequisite – Creating Amazon VPC endpoint manually

Before you can install the GuardDuty security agent, you must create an Amazon Virtual Private Cloud (Amazon VPC) endpoint. This will help GuardDuty receive the runtime events of your Amazon EC2 instances.

###### Note

There is no additional cost for the usage of the VPC endpoint.

###### To create a Amazon VPC endpoint

1.

Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).
2.

In the navigation pane, under **VPC private cloud**, choose **Endpoints**.
3.

Choose **Create Endpoint**.
4.

On the **Create endpoint** page, for **Service category**, choose **Other endpoint services**.
5.

For **Service name**, enter `com.amazonaws.`us-east-1`.guardduty-data`.

Make sure to replace `us-east-1` with your AWS Region. This must be the same Region as the Amazon EC2 instance that belongs to your AWS account ID.
6.

Choose **Verify service**.
7.

After the service name is successfully verified, choose the **VPC** where your instance resides. Add the following policy to restrict Amazon VPC endpoint usage to the specified account only. With the organization `Condition` provided below this policy, you can update the following policy to restrict access to your endpoint. To provide the Amazon VPC endpoint support to specific account IDs in your organization, see [Organization condition to restrict access to your endpoint](#gdu-runtime-ec2-organization-restrict-access-vpc-endpoint).

**JSON**

********

```
{
	"Version":"2012-10-17",
	"Statement": [
		{
			"Action": "*",
			"Resource": "*",
			"Effect": "Allow",
			"Principal": "*"
		},
		{
			"Condition": {
				"StringNotEquals": {
					"aws:PrincipalAccount": "111122223333"
				}
			},
			"Action": "*",
			"Resource": "*",
			"Effect": "Deny",
			"Principal": "*"
		}
	]
}

```

The `aws:PrincipalAccount` account ID must match the account containing the VPC and VPC endpoint. The following list shows how to share the VPC endpoint with other AWS account IDs:

  -

To specify multiple accounts to access the VPC endpoint, replace `"aws:PrincipalAccount: "`111122223333`"` with the following block:

```
"aws:PrincipalAccount": [
          "666666666666",
          "555555555555"
      ]
```

Make sure to replace the AWS account IDs with the account IDs of those accounts that need to access the VPC endpoint.
  -

To allow all the members from an organization to access the VPC endpoint, replace `"aws:PrincipalAccount: "`111122223333`"` with the following line:

```
"aws:PrincipalOrgID": "o-abcdef0123"
```

Make sure to replace the organization `o-abcdef0123` with your organization ID.
  -

To restrict accessing a resource by an organization ID, add your `ResourceOrgID` to the policy. For more information, see [`aws:ResourceOrgID`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgid) in the *IAM User Guide*.

```
"aws:ResourceOrgID": "o-abcdef0123"
```

8.

Under **Additional settings**, choose **Enable DNS name**.
9.

Under **Subnets**, choose the subnets in which your instance resides.
10.

Under **Security groups**, choose a security group that has the in-bound port 443 enabled from your VPC (or your Amazon EC2 instance). If you don't already have a security group that has an in-bound port 443 enabled, see [Create a security group for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html) in the *Amazon VPC User Guide*.

If there is an issue while restricting the in-bound permissions to your VPC (or instance), you can the in-bound 443 port from any IP address `(0.0.0.0/0)`. However, GuardDuty recommends using IP addresses that matches the CIDR block for your VPC. For more information, see [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) in the *Amazon VPC User Guide*.

After you have followed the steps, see [Validating VPC endpoint configuration](https://docs.aws.amazon.com/guardduty/latest/ug/validate-vpc-endpoint-config-runtime-monitoring.html) to ensure that the VPC endpoint was set up correctly.
