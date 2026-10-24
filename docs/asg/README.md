
## EC2 Auto Scaling - Local Documentation Snapshot

Offline copies of the AWS docs used to build [asg/asg-target-tracking](../../asg/asg-target-tracking/), converted from HTML to Markdown.
Downloaded 2026-10-24. Each file starts with its source URL. Check the live page if something looks off.

### User Guide — What's new

| File | Topic |
|---|---|
| [ug-DocumentHistory.md](ug-DocumentHistory.md) | EC2 Auto Scaling document history (high-resolution metrics for target tracking: 2024-11-22) |

### User Guide — Target tracking

| File | Topic |
|---|---|
| [ug-as-scaling-target-tracking.md](ug-as-scaling-target-tracking.md) | Overview: adapts to usage patterns, multiple policies, choosing metrics, target value, warmup, considerations |
| [ug-policy_creating.md](ug-policy_creating.md) | Create a target tracking policy |
| [ug-policy-creating-high-resolution-metrics.md](ug-policy-creating-high-resolution-metrics.md) | High-resolution metrics: Period 10 / 30, FILL with 1-minute capacity, pricing |
| [ug-ec2-auto-scaling-target-tracking-metric-math.md](ug-ec2-auto-scaling-target-tracking-metric-math.md) | Metric math, SQS backlog per instance example |
| [ug-as-using-sqs-queue.md](ug-as-using-sqs-queue.md) | Scaling on SQS: acceptable backlog per instance, scale-in protection |
| [ug-scale-sqs-queue-cli.md](ug-scale-sqs-queue-cli.md) | SQS scaling with the CLI (custom metric approach) |
| [ug-examples-scaling-policies.md](ug-examples-scaling-policies.md) | CLI examples for scaling policies |
| [ug-ec2-auto-scaling-default-instance-warmup.md](ug-ec2-auto-scaling-default-instance-warmup.md) | Default instance warmup |

### CloudWatch

| File | Topic |
|---|---|
| [cloudwatch-agent-configuration-file-details.md](cloudwatch-agent-configuration-file-details.md) | CloudWatch agent config: `metrics_collection_interval` < 60 = high-resolution, `append_dimensions`, `aggregation_dimensions` |

### CloudFormation Template Reference

| File | Type |
|---|---|
| [cfn-aws-resource-autoscaling-scalingpolicy.md](cfn-aws-resource-autoscaling-scalingpolicy.md) | `AWS::AutoScaling::ScalingPolicy` |
| [cfn-aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.md](cfn-aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.md) | TargetTrackingConfiguration |
| [cfn-aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.md](cfn-aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.md) | CustomizedMetricSpecification (`Period`, `Metrics`) |
| [cfn-aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery.md](cfn-aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery.md) | TargetTrackingMetricDataQuery (metric math) |
| [cfn-aws-properties-autoscaling-scalingpolicy-targettrackingmetricstat.md](cfn-aws-properties-autoscaling-scalingpolicy-targettrackingmetricstat.md) | TargetTrackingMetricStat (`Period`) |
| [cfn-aws-properties-autoscaling-scalingpolicy-metric.md](cfn-aws-properties-autoscaling-scalingpolicy-metric.md) | Metric |
| [cfn-aws-properties-autoscaling-scalingpolicy-metricdimension.md](cfn-aws-properties-autoscaling-scalingpolicy-metricdimension.md) | MetricDimension |
| [cfn-aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.md](cfn-aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.md) | PredefinedMetricSpecification (`ALBRequestCountPerTarget`, `ResourceLabel`) |
| [cfn-aws-properties-autoscaling-autoscalinggroup-metricscollection.md](cfn-aws-properties-autoscaling-autoscalinggroup-metricscollection.md) | Auto Scaling group MetricsCollection (group metrics) |
