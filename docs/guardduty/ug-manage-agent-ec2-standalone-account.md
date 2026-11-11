<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/manage-agent-ec2-standalone-account.html -->
<!-- Downloaded: 2026-10-28 -->

# Enabling GuardDuty automated agent for Amazon EC2 resources in a standalone account

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to your account. For more information, see [Enabling Runtime Monitoring for multiple-account environments](https://docs.aws.amazon.com/guardduty/latest/ug/enable-runtime-monitoring-multiple-acc-env.html).

After you enable Runtime Monitoring, ensure to install GuardDuty security agent through automated configuration or manual deployment. As a part of completing all the steps listed in the following procedure, make sure to install the security agent.

Based on your preference to monitor all or selective Amazon EC2 resources, choose a preferred method and follow the steps in the following table.

**Configure for all instances**

###### To configure Runtime Monitoring for all instances in your standalone account

1.

Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).
2.

In the navigation pane, choose **Runtime Monitoring**.
3.

Under the **Configuration** tab, choose **Edit**.
4.

In the **EC2** section, choose **Enable**.
5.

Choose **Save**.
6.

You can verify that the SSM association that GuardDuty creates will install and manage the security agent on all the EC2 resources belonging to your account.

  1.

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).
  2.

Open the **Targets** tab for the SSM association (`GuardDutyRuntimeMonitoring-do-not-delete`). Observe that the **Tag key** appears as **InstanceIds**.

**Using inclusion tag in selected instances**

###### To configure GuardDuty security agent for selected Amazon EC2 instances

1.

Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
2.

Add the `GuardDutyManaged`:`true` tag to the instances that you want GuardDuty to monitor and detect potential threats. For information about adding this tag, see [To add a tag to an individual resource](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#adding-or-deleting-tags).
3.

You can verify that the SSM association that GuardDuty creates will install and manage the security agent only on the EC2 resources that are tagged with the inclusion tags.

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

  1.

Open the **Targets** tab for the SSM association that gets created (`GuardDutyRuntimeMonitoring-do-not-delete`). The **Tag key** appears as **tag:GuardDutyManaged**.

**Using exclusion tag in selected instances**

###### Note

Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent configuration for Amazon EC2, any EC2 instance that launches without an exclusion tag will be covered under GuardDuty automated agent configuration.

###### To configure GuardDuty security agent for selected Amazon EC2 instances

1.

Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
2.

Add the `GuardDutyManaged`:`false` tag to the instances that you **don't** want GuardDuty to monitor and detect potential threats. For information about adding this tag, see [To add a tag to an individual resource](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#adding-or-deleting-tags).
3.

###### For the [exclusion tags to be available](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html#general-runtime-monitoring-prereq-ec2) in the instance metadata, perform the following steps:

  1.

Under the **Details** tab of your instance, view the status for **Allow tags in instance metadata**.

If it is currently **Disabled**, use the following steps to change the status to **Enabled**. Otherwise, skip this step.
  2.

Select the instance for which you want to allow tags.
  3.

Under the **Actions** menu, choose **Instance settings**.
  4.

Choose **Allow tags in instance metadata**.
  5.

Under **Access to tags in instance metadata**, select **Allow**.
  6.

Choose **Save**.

4.

After you have added the exclusion tag perform the same steps as sepcified in the **Configure for all instances** tab.

You can now assess runtime [Runtime coverage and troubleshooting for Amazon EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-ec2.html).
