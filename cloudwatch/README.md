## Cloudwatch Cloudformation Templates

### Cloudwatch - Alarm

Basic Cloudwatch Alarm example. Sends notification when breached.

[cloudwatch-alarm](cloudwatch-alarm.yaml)

### Cloudwatch - Alarm - EC2 Action

Cloudwatch Alarm which monitors EC2 CPUUtilization. Invoke EC2 Action when Breached.

[cloudwatch-alarm-ec2-action](cloudwatch-alarm-ec2-action.yaml)

---

## Cloudwatch Logs

- Supports querying your logs with a powerful query language
- Auditing and masking sensitive data in logs
- Generating metrics from logs using filters or an embedded log format

### Cloudwatch Log Insights
Interactively search and analyze your log data. [syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)

##### Top 20 Recent Logs

```
fields @timestamp, @message, @logStream, @log
| sort @timestamp desc
| limit 20
```

##### Query with Filter (@message like "Fail")

```
fields @timestamp, @message, @logStream
| filter @message like "Fail"
| sort @timestamp desc
| limit 20
```

- | filter @message like /Fail/ Regex
- | filter @message like /Fail./ Regex Begins With
- | filter @message like /Fail.*/ Regex Begins With Greedy
- | filter @message like /(?i)Fail.*/  Case Insensitive

##### Stats aggregation functions - Query with time series (Group by 15 minutes) 

```
fields @timestamp, @message
| filter @message like /Fail/ 
| stats count(*) as FailCount by bin(15m)
| sort FailCount desc
```

avg, sum, count, count_distinct, min, max
earliest, latest

##### String Function

```
fields @timestamp, @message, replace(@message, "Service: ", "") as foo
| filter @message like /(?i)Fail.*/
| sort @timestamp desc
| limit 20
```

isempty, isblank, concat, ltrim, rtrim, trim, strlen, toupper, tolower, substr, replace, strcontains



### Cloudwatch - Log Group

[cloudwatch-log-group](cloudwatch-log-group.yaml)

---

### References

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Logs.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-start.html
  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-dataprotectionpolicy

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html


### TODO

- Alarm View EventBridge rule

- Alarm Notification Action, AutoScaling Action, EC2 Action, System's Manager Action

-- EC2 Action (arn:aws:automate:region:ec2:stop | arn:aws:automate:region:ec2:terminate | arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot)
-- arn:aws:autoscaling:region:account-id:scalingPolicy:policy-id:autoScalingGroupName/group-friendly-name:policyName/policy-friendly-name
-- arn:aws:ssm:region:account-id:opsitem:severity | arn:aws:ssm-incidents::account-id:response-plan:response-plan-name

- CloudwatchAgent
