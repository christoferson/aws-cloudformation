## Cloudwatch Cloudformation Templates

### Cloudwatch - Alarm

Basic Cloudwatch Alarm example. Sends notification when breached.

[cloudwatch-alarm](cloudwatch-alarm.yaml)

### Cloudwatch - Alarm - EC2 Action

Cloudwatch Alarm which monitors EC2 CPUUtilization. Invoke EC2 Action when Breached.

[cloudwatch-alarm-ec2-action](cloudwatch-alarm-ec2-action.yaml)

### References

https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Logs.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html

### TODO

- Alarm View EventBridge rule

- Alarm Notification Action, AutoScaling Action, EC2 Action, System's Manager Action

-- EC2 Action (arn:aws:automate:region:ec2:stop | arn:aws:automate:region:ec2:terminate | arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot)
-- arn:aws:autoscaling:region:account-id:scalingPolicy:policy-id:autoScalingGroupName/group-friendly-name:policyName/policy-friendly-name
-- arn:aws:ssm:region:account-id:opsitem:severity | arn:aws:ssm-incidents::account-id:response-plan:response-plan-name

- CloudwatchAgent