
## ARC zonal shift and zonal autoshift - ALB and EC2 Auto Scaling group

[arc-zonal-autoshift-alb-asg.yaml](arc-zonal-autoshift-alb-asg.yaml)

### The problem

An Availability Zone has a partial failure: packet loss, slow EBS, a power event. Health checks often still **pass**, so the load balancer keeps sending a third of your traffic into the bad zone and users see errors and timeouts. You want to say "**stop using AZ-a**" for this application, quickly, and without redeploying anything.

### What ARC gives you

| Feature | Who starts it | What happens |
|---|---|---|
| **Zonal shift** | You (console / CLI / API), with an expiry of up to 3 days | Traffic for one resource is moved away from one AZ |
| **Zonal autoshift** | **AWS**, when its internal telemetry (network, EC2, ELB) detects an AZ impairment | Same shift, started for you. It ends when AWS sees the AZ recover |
| **Practice run** | ARC weekly (about 30 minutes), or you on demand | A real shift, to prove you can lose an AZ. **Required** for autoshift |

Supported resources: **ALB and NLB, with cross-zone load balancing enabled or disabled**, **EC2 Auto Scaling groups** (since November 2024), and EKS.

### What a shift away from AZ-a does

| Resource | During the shift |
|---|---|
| ALB with cross-zone enabled (always the case for ALBs) | The AZ-a load balancer IP is removed from DNS, **and** no load balancer node sends to AZ-a targets. With cross-zone on, the nodes in AZ-b and AZ-c also stop using AZ-a targets |
| Auto Scaling group | New instances launch only in AZ-b and AZ-c. Scale-**in** is blocked, and scale-out still works. `IgnoreUnhealthy` means unhealthy instances in AZ-a aren't replaced, which avoids churn in a broken zone |

```
           before                                   shift away from AZ-a
 DNS ─► [ALB a][ALB b][ALB c]              DNS ─► [  -  ][ALB b][ALB c]
          │ cross-zone │                             │ cross-zone │
        ┌─┴────┬───────┴─┐                    ┌──────┴─┬──────────┐
     [a:2]   [b:2]     [c:2]               [a:2 idle] [b:2]      [c:2]
     6 instances serve the load            4 instances must serve the load  ← pre-scale for this
```

Offline docs: [../docs/arc/README.md](../docs/arc/README.md)

----------------------------------------------------------------------------------

## What the template creates

| Resource | Zonal setting |
|---|---|
| ALB | `zonal_shift.config.enabled = true` registers it with ARC. `client_keep_alive.seconds = 300` (default 3600), because shifts are DNS-based and open connections stay in the old AZ until the client reconnects |
| Auto Scaling group, 3 AZs, `InstanceCount` = 6 | `AvailabilityZoneImpairmentPolicy: { ZonalShiftEnabled: true, ImpairedZoneHealthCheckBehavior: IgnoreUnhealthy }`. `InstanceMaintenancePolicy.MinHealthyPercentage: 100`. Min = max = desired, because it's pre-scaled |
| `PracticeRunOutcomeAlarm` (composite) | Target 5XX **OR** p99 latency. In `ALARM` it ends the practice run with outcome **FAILED**. Only one outcome alarm is allowed, so KPIs are combined |
| `PracticeRunBlockingAlarm` | Healthy targets < `InstanceCount`. A practice run doesn't start, or is stopped, while capacity isn't fully in service, for example during a deployment |
| 2 × `AWS::ARCZonalShift::ZonalAutoshiftConfiguration` | Autoshift `ENABLED` on the ALB **and** the Auto Scaling group, with the practice run configuration and `BlockedWindows` (`WED:01:00-WED:03:00` UTC release window) |

**Static stability** is the core requirement. Autoshift doesn't wait for scale-out, and the docs say not to rely on scaling during a shift. If 4 instances carry peak load, run 6 (2 per AZ), so that after losing one AZ, 4 remain.

### Practice runs

| Outcome | Meaning |
|---|---|
| `SUCCEEDED` | 30 minutes with traffic shifted away and the outcome alarm never fired. You can lose an AZ |
| `FAILED` | The outcome alarm fired, so the application can't take the loss of an AZ. Add capacity or fix the alarm |
| `CAPACITY_CHECK_FAILED` | Before shifting, ARC found healthy capacity not balanced across AZs (load balancer), or below desired capacity (Auto Scaling group) |
| `INTERRUPTED` | Ended by something else: a real autoshift, your own shift, a blocking alarm, or an FIS experiment |

Practice runs are skipped during blocked windows and dates, when a blocking alarm is in `ALARM`, during an AWS FIS experiment, and during an AWS event in the Region.

### Precedence

Only one shift is `APPLIED` at a time. **A shift you start beats everything.** For example, your shift + an autoshift → the autoshift is `ACTIVE` but `NOT_APPLIED`. A practice run is cancelled (`INTERRUPTED`) by your shift, an autoshift or an FIS experiment.

----------------------------------------------------------------------------------

## Deploy and try it

```bash
aws cloudformation create-stack --stack-name myapp-dev-zonal \
  --template-body file://arc-zonal-autoshift-alb-asg.yaml \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-xxxx \
               ParameterKey=VpcSubnetList,ParameterValue='subnet-a\,subnet-b\,subnet-c'

ALB=$(aws cloudformation describe-stacks --stack-name myapp-dev-zonal --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerArn'].OutputValue" --output text)
ASG=$(aws cloudformation describe-stacks --stack-name myapp-dev-zonal --query "Stacks[0].Outputs[?OutputKey=='WebAutoScalingGroupArn'].OutputValue" --output text)
DNS=$(aws cloudformation describe-stacks --stack-name myapp-dev-zonal --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerDnsName'].OutputValue" --output text)

aws arc-zonal-shift get-managed-resource --resource-identifier $ALB   # zonalAutoshiftStatus, practiceRunConfiguration, appliedWeights
for i in $(seq 20); do curl -s http://$DNS/; done | sort | uniq -c        # spread across 3 AZs
```

Manual zonal shift. `--away-from` takes an **AZ ID** (`use1-az1`), not a name (`us-east-1a`):

```bash
aws ec2 describe-availability-zones --query "AvailabilityZones[].[ZoneName,ZoneId]" --output table

aws arc-zonal-shift start-zonal-shift --resource-identifier $ALB --away-from use1-az1 --expires-in 30m --comment "AZ test"
aws arc-zonal-shift start-zonal-shift --resource-identifier $ASG --away-from use1-az1 --expires-in 30m --comment "AZ test"
for i in $(seq 20); do curl -s http://$DNS/; done | sort | uniq -c        # only 2 AZs now

aws arc-zonal-shift list-zonal-shifts --query "items[].[zonalShiftId,resourceIdentifier,awayFrom,status]" --output table
# End it: Auto Scaling group first, wait for balanced capacity, then the load balancer
aws arc-zonal-shift cancel-zonal-shift --zonal-shift-id <asg-shift-id>
aws arc-zonal-shift cancel-zonal-shift --zonal-shift-id <alb-shift-id>
```

On-demand practice run, which is a good first test after enabling autoshift:

```bash
aws arc-zonal-shift start-practice-run --resource-identifier $ALB --away-from use1-az1 --comment "on-demand practice"
```

## Notes

- **Fail open:** if all targets in all AZs are unhealthy, the load balancer fails open and a shift has no effect. A shift also does nothing for a single-AZ target group.
- **Several load balancers, same targets:** a shift on one cross-zone load balancer removes that AZ's targets from every load balancer that shares them.
- **ALB behind an NLB:** start the shift on the NLB, because the NLB doesn't see an ALB shift.
- **Cross-zone disabled load balancers** (NLB): use `AvailabilityZoneDistribution: balanced-only` on the Auto Scaling group. Auto Scaling then asks you to acknowledge the imbalance risk with `SkipZonalShiftValidation`.
- **Notifications:** EventBridge events for practice runs and autoshifts. The **autoshift observer notification** reports every autoshift AWS starts in the Region, even for resources without autoshift. Enable it per Region.
- **Testing a real AZ failure:** AWS FIS has an AZ power interruption scenario that triggers autoshift ([../docs/arc/ug-testing-zonal-autoshift-fis.md](../docs/arc/ug-testing-zonal-autoshift-fis.md)).
- **CloudFormation reference gap:** the reference for `ZonalAutoshiftConfiguration` still says only ALB and NLB are supported. The ARC Developer Guide lists Auto Scaling groups for zonal shift **and** zonal autoshift, and its Auto Scaling best practices recommend autoshift. If the Auto Scaling group configuration is rejected, remove `AutoScalingGroupZonalAutoshiftConfiguration`.
- **Disable autoshift:** delete the `ZonalAutoshiftConfiguration` resource. `ENABLED` is the only allowed value.

## Docs

- [../docs/arc/ug-arc-zonal-shift.resource-types.app-load-balancers.md](../docs/arc/ug-arc-zonal-shift.resource-types.app-load-balancers.md)
- [../docs/arc/ug-arc-zonal-shift.resource-types.ec2-auto-scaling-groups.md](../docs/arc/ug-arc-zonal-shift.resource-types.ec2-auto-scaling-groups.md) (behavior during a shift, best practices)
- [../docs/arc/ug-arc-zonal-autoshift.considerations.md](../docs/arc/ug-arc-zonal-autoshift.considerations.md) (pre-scaling, keep-alive, alarms, outcomes)
- [../docs/arc/ug-arc-zonal-autoshift.how-it-works.precedence.md](../docs/arc/ug-arc-zonal-autoshift.how-it-works.precedence.md)
- [../docs/arc/cfn-aws-resource-arczonalshift-zonalautoshiftconfiguration.md](../docs/arc/cfn-aws-resource-arczonalshift-zonalautoshiftconfiguration.md)
