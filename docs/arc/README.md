
## Amazon Application Recovery Controller (ARC) - Zonal shift and zonal autoshift - Local Documentation Snapshot

Offline copies of the AWS docs used to build [arc-zonal-shift](../../arc-zonal-shift/), converted from HTML to Markdown.
Downloaded 2026-10-24. Each file starts with its source URL. Check the live page if something looks off.

### Developer Guide — What's new

| File | Topic |
|---|---|
| [ug-doc-history.md](ug-doc-history.md) | ARC document history (Auto Scaling groups 2024-11-18, NLB target group configurations 2026-09-24, ...) |

### Developer Guide — Zonal shift

| File | Topic |
|---|---|
| [ug-arc-zonal-shift.md](ug-arc-zonal-shift.md) | Overview |
| [ug-arc-zonal-shift.how-it-works.md](ug-arc-zonal-shift.how-it-works.md) | How a zonal shift works |
| [ug-introduction-components-zonal.md](ug-introduction-components-zonal.md) | Components: managed resource, zonal shift, expiry |
| [ug-route53-arc-best-practices.zonal-shifts.md](ug-route53-arc-best-practices.zonal-shifts.md) | Best practices |
| [ug-arc-zonal-shift.resource-types.md](ug-arc-zonal-shift.resource-types.md) | Supported resources, fail open, shared targets |
| [ug-arc-zonal-shift.resource-types.app-load-balancers.md](ug-arc-zonal-shift.resource-types.app-load-balancers.md) | ALB: `zonal_shift.config.enabled`, cross-zone behavior, keep-alive |
| [ug-arc-zonal-shift.resource-types.network-load-balancers.md](ug-arc-zonal-shift.resource-types.network-load-balancers.md) | NLB |
| [ug-arc-zonal-shift.resource-types.ec2-auto-scaling-groups.md](ug-arc-zonal-shift.resource-types.ec2-auto-scaling-groups.md) | Auto Scaling groups: impairment policy, behavior during a shift, best practices |
| [ug-arc-zonal-shift.start-cancel.md](ug-arc-zonal-shift.start-cancel.md) | Start, update, cancel (expiry up to 72 hours) |
| [ug-getting-started-cli-zonalshift.md](ug-getting-started-cli-zonalshift.md) | CLI examples |
| [ug-security_iam_service-with-iam-zonal-shift.md](ug-security_iam_service-with-iam-zonal-shift.md) | IAM permissions |

### Developer Guide — Zonal autoshift

| File | Topic |
|---|---|
| [ug-arc-zonal-autoshift.md](ug-arc-zonal-autoshift.md) | Overview |
| [ug-arc-zonal-autoshift.how-it-works.about.md](ug-arc-zonal-autoshift.how-it-works.about.md) | About zonal autoshift |
| [ug-arc-zonal-autoshift.how-it-works.start-stop-auto.md](ug-arc-zonal-autoshift.how-it-works.start-stop-auto.md) | When AWS starts and stops autoshifts |
| [ug-arc-zonal-autoshift.how-it-works.scheduled-practice-runs.md](ug-arc-zonal-autoshift.how-it-works.scheduled-practice-runs.md) | Practice run schedule, blocking constraints |
| [ug-arc-zonal-autoshift.how-it-works.capacity-check.md](ug-arc-zonal-autoshift.how-it-works.capacity-check.md) | Capacity checks (load balancers, Auto Scaling groups) |
| [ug-arc-zonal-autoshift.how-it-works.alarms.md](ug-arc-zonal-autoshift.how-it-works.alarms.md) | Outcome and blocking alarms |
| [ug-arc-zonal-autoshift.how-it-works.blocked-windows.md](ug-arc-zonal-autoshift.how-it-works.blocked-windows.md) | Blocked / allowed windows and dates |
| [ug-arc-zonal-autoshift.how-it-works.precedence.md](ug-arc-zonal-autoshift.how-it-works.precedence.md) | Precedence: customer shift, autoshift, practice run, FIS |
| [ug-arc-zonal-autoshift.how-it-works.how-traffic-shifted.md](ug-arc-zonal-autoshift.how-it-works.how-traffic-shifted.md) | How traffic is shifted |
| [ug-arc-zonal-autoshift.how-it-works.notifications.md](ug-arc-zonal-autoshift.how-it-works.notifications.md) | Notifications, autoshift observer |
| [ug-arc-zonal-autoshift.considerations.md](ug-arc-zonal-autoshift.considerations.md) | Best practices: keep-alive, pre-scaling, alarms, outcomes |
| [ug-getting-started-cli-zonal-autoshift.start-practice-run.md](ug-getting-started-cli-zonal-autoshift.start-practice-run.md) | On-demand practice run (CLI) |
| [ug-eventbridge-zonal-autoshift.md](ug-eventbridge-zonal-autoshift.md) | EventBridge events |
| [ug-testing-zonal-autoshift-fis.md](ug-testing-zonal-autoshift-fis.md) | Testing with AWS FIS (AZ power interruption) |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-arczonalshift-zonalautoshiftconfiguration.md](cfn-aws-resource-arczonalshift-zonalautoshiftconfiguration.md) | `AWS::ARCZonalShift::ZonalAutoshiftConfiguration` |
| [cfn-aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.md](cfn-aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.md) | PracticeRunConfiguration |
| [cfn-aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.md](cfn-aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.md) | ControlCondition (alarm) |
| [cfn-aws-resource-autoscaling-autoscalinggroup.md](cfn-aws-resource-autoscaling-autoscalinggroup.md) | `AWS::AutoScaling::AutoScalingGroup` (`SkipZonalShiftValidation`, `InstanceMaintenancePolicy`) |
| [cfn-aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy.md](cfn-aws-properties-autoscaling-autoscalinggroup-availabilityzoneimpairmentpolicy.md) | AvailabilityZoneImpairmentPolicy |
| [cfn-aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.md](cfn-aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.md) | Load balancer attributes (`zonal_shift.config.enabled`, `client_keep_alive.seconds`) |
| [cfn-aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.md](cfn-aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.md) | Target group attributes (cross-zone, DNS failover) |
