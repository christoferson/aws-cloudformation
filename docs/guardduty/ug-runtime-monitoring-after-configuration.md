<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-after-configuration.html -->
<!-- Downloaded: 2026-10-28 -->

# Tracking Runtime Monitoring coverage

After you enable Runtime Monitoring and install GuardDuty security agent in your standalone account or multiple member accounts, you can take the following steps to ensure that the protection plan setting is working as expected, and monitor how much memory and CPU does GuardDuty security agent uses.

****Assess runtime coverage****

GuardDuty recommends you to continuously assess the coverage status of the resource where you have deployed the security agent. The coverage status could be either **Healthy** or **Unhealthy**. A **Healthy** coverage status indicates that GuardDuty is receiving the runtime events from the corresponding resource when there is an operating system-level activity.

When the coverage status becomes **Healthy** for the resource, GuardDuty is able to receive the runtime events and analyze them for threat detection. When GuardDuty detects a potential security threat in the tasks or applications running in your container workloads and instances, GuardDuty generates [GuardDuty Runtime Monitoring finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html).

You can also configure an Amazon EventBridge (EventBridge) to receive a notification when the coverage status changes from **Unhealthy** to **Healthy** and otherwise. For more information, see [Reviewing runtime coverage statistics and troubleshooting issues](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-assessing-coverage.html).

****Set up CPU and memory monitoring for GuardDuty security agent****

After you have assessed that the coverage status shows as **Healthy**, you can evaluate the performance of the security agent for your resource type. For Amazon EKS clusters that have the security agent release v1.5 or above, GuardDuty supports configuring the parameters of the (add-on) security agent. For more information, see [Setting up CPU and memory monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-setting-cpu-mem-monitoring.html).
