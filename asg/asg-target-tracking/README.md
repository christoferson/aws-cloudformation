
## EC2 Auto Scaling - target tracking (adaptive, high-resolution metrics, metric math)

### The problem

Classic scaling setups react slowly and need hand-tuning:
- **Slow metrics:** EC2 metrics arrive every 5 minutes (1 minute with detailed monitoring), and alarms need several data points. A traffic spike is often over, or has already caused errors, before the first new instance is serving.
- **Hand-tuned step policies:** thresholds, step sizes and cooldowns have to be tuned per application, and re-tuned whenever the traffic pattern changes.

### What target tracking does now

You pick **one metric and one target value**, like a thermostat ("keep CPU at 50%"). Auto Scaling creates and manages the CloudWatch alarms and calculates how many instances to add or remove.

| Capability | What it means |
|---|---|
| **Adapts to each workload** | Target tracking **tunes its own alarms** to the application's usage pattern. There's nothing to configure. Don't create, edit or delete the `TargetTracking-...` alarms |
| **High-resolution metrics** (November 2024) | `Period` **10 or 30 seconds** (default 60) on a metric that is published at least that often. Target tracking then sees and reacts to a spike in tens of seconds |
| **Metric math** | Build the metric in the policy (for example queue length ÷ instances) instead of publishing your own custom metric |
| **Multiple policies** | Scale **out** if **any** policy asks, and **in** only if **all** agree (availability first) |

The metric must fall when instances are added. CPU %, requests **per target**, and backlog **per instance** work. Total `RequestCount`, latency, and raw queue length don't.

| Template | Workload | Metric |
|---|---|---|
| [asg-target-tracking-high-resolution.yaml](asg-target-tracking-high-resolution.yaml) | Spiky **API behind an ALB** | CloudWatch agent CPU every **10 s**, Period 10, **plus** `ALBRequestCountPerTarget` |
| [asg-target-tracking-sqs-backlog.yaml](asg-target-tracking-sqs-backlog.yaml) | **SQS queue workers** | Metric math: `ApproximateNumberOfMessagesVisible / GroupInServiceInstances` |

Offline docs: [../../docs/asg/README.md](../../docs/asg/README.md)

----------------------------------------------------------------------------------

## High-resolution CPU (API tier)

```
 instances ─ CloudWatch agent ─ cpu_usage_active every 10 s, dimension AutoScalingGroupName (rolled up)
                                        │
 target tracking  Period 10, target 50% ┴─► alarm managed by Auto Scaling ─► desired capacity
 target tracking  ALBRequestCountPerTarget 1000/min  ─────────────────────┘   (out if ANY, in if ALL)
```

| Piece | Why |
|---|---|
| Agent `metrics_collection_interval: 10` | Below 60 seconds, the agent publishes **high-resolution** metrics |
| `append_dimensions: AutoScalingGroupName` + `aggregation_dimensions: [["AutoScalingGroupName"]]` | Creates one metric for the whole group, with exactly the dimension the policy names |
| `Period: 10` in `CustomizedMetricSpecification` | Accepted values are 10, 30 and 60. The metric must be published at that resolution **or finer**, otherwise there are gaps (`INSUFFICIENT_DATA`, so no scaling) |
| `DefaultInstanceWarmup: 60` | A booting instance isn't counted in the metric until it's warm. This avoids scaling out again because of startup CPU |
| SSM parameter `AmazonCloudWatch-...` | The name prefix is what `CloudWatchAgentServerPolicy` allows `ssm:GetParameter` on |

**Targets for count metrics** (requests, jobs) are always **per instance per minute**, even with a 10-second period.

## SQS backlog per instance (workers)

| | |
|---|---|
| `m1` | `AWS/SQS ApproximateNumberOfMessagesVisible`, Sum |
| `m2` | `AWS/AutoScaling GroupInServiceInstances`, Average. Needs **group metrics** (`MetricsCollection`) |
| `e1 = m1 / m2` | Backlog per instance. `ReturnData: true` on this one only |
| Target | Acceptable latency ÷ processing time per message. With the defaults that's 60 s ÷ 0.5 s = **120** |

SQS publishes 1-minute metrics, so the period stays at 60. For a sub-minute custom metric divided by capacity, the docs use `FILL(m2, REPEAT)` on the 1-minute capacity metric so both series have the same period.

----------------------------------------------------------------------------------

## Deploy and try it

```bash
aws cloudformation create-stack --stack-name myapp-dev-api-highres \
  --template-body file://asg-target-tracking-high-resolution.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx ParameterKey=VpcSubnetList,ParameterValue='subnet-a\,subnet-b'

# Burn CPU on all instances for 5 minutes (Run Command), then watch scaling
aws ssm send-command --document-name AWS-RunShellScript \
  --targets Key=tag:aws:autoscaling:groupName,Values=myapp-dev-api \
  --parameters '{"commands":["for i in $(seq $(nproc)); do timeout 300 yes > /dev/null & done"]}'

aws autoscaling describe-scaling-activities --auto-scaling-group-name myapp-dev-api --max-items 5 \
  --query "Activities[].[StartTime,StatusCode,Description]" --output table
aws autoscaling describe-policies --auto-scaling-group-name myapp-dev-api \
  --query "ScalingPolicies[].[PolicyName,Alarms[].AlarmName]"     # alarms owned by target tracking
```

```bash
aws cloudformation create-stack --stack-name myapp-dev-workers \
  --template-body file://asg-target-tracking-sqs-backlog.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx ParameterKey=VpcSubnetList,ParameterValue='subnet-a\,subnet-b'

Q=$(aws cloudformation describe-stacks --stack-name myapp-dev-workers --query "Stacks[0].Outputs[?OutputKey=='WorkQueueUrl'].OutputValue" --output text)
for i in $(seq 200); do
  aws sqs send-message-batch --queue-url $Q \
    --entries "$(python3 -c 'import json;print(json.dumps([{"Id":str(i),"MessageBody":"job"} for i in range(10)]))')" >/dev/null
done   # 2,000 messages / 1 worker = 2,000 per instance vs target 120 -> scale out (capped at MaxSize 10)
```

## Notes

- **Scale-in is gradual by design.** Target tracking removes capacity more slowly than it adds it. If you need exact control, use step scaling. `DisableScaleIn: true` turns off the scale-in half, for example during deployments.
- **Small groups:** results round up when adding and conservatively when removing, so a 2-instance group can sit well below the target.
- **Cost:** high-resolution custom metrics, and the high-resolution alarms that target tracking creates for them, are priced higher than standard ones.
- **Predefined EC2 metrics** (`ASGAverageCPUUtilization`) are 5-minute unless detailed monitoring is enabled. Use the agent at 10 seconds, as here, for sub-minute reaction.
- **Workers and scale-in:** an instance terminated mid-job leaves its message invisible until the visibility timeout ends, and then another worker picks it up. For long jobs, use instance scale-in protection while working.

## Docs

- [../../docs/asg/ug-as-scaling-target-tracking.md](../../docs/asg/ug-as-scaling-target-tracking.md) (choosing metrics, target values, warmup, considerations)
- [../../docs/asg/ug-policy-creating-high-resolution-metrics.md](../../docs/asg/ug-policy-creating-high-resolution-metrics.md)
- [../../docs/asg/ug-ec2-auto-scaling-target-tracking-metric-math.md](../../docs/asg/ug-ec2-auto-scaling-target-tracking-metric-math.md) (SQS backlog example)
- [../../docs/asg/ug-as-using-sqs-queue.md](../../docs/asg/ug-as-using-sqs-queue.md) (acceptable backlog per instance)
- [../../docs/asg/cloudwatch-agent-configuration-file-details.md](../../docs/asg/cloudwatch-agent-configuration-file-details.md) (`metrics_collection_interval`, `aggregation_dimensions`)
- [../../docs/asg/cfn-aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.md](../../docs/asg/cfn-aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.md) (`Period`)
