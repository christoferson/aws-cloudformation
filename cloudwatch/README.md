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


---

### Cloudwatch - Log Metric Filter

#### Using filter patterns to match terms in log events
Match a single term: ERROR
Match multiple terms: ERROR ARGUMENTS - Contain ERROR and ARGUMENTS
Match single and multiple terms: ?ERROR ?ARGUMENTS - Contains ERROR or ARGUMENTS
Match exact phrases: "INTERNAL SERVER ERROR"
Include and exclude terms: ERROR -ARGUMENTS - include the term ERROR and exclude the term ARGUMENTS
Match everything: " "

#### Using metric filters to match terms and extract values from JSON log events

{ PropertySelector EqualityOperator String }

Metric filters that match strings: { $.eventType = "UpdateTrail" }
Metric filters that match numeric values: { $.latency < 50 }

#### Matching terms in JSON log events

If you test the example metric filters with the example JSON log event, you must enter the example JSON log on a single line.

Metric filter that matches element in array: { $.arrayKey[0] = "value" }
Metric filter that matches an object in array: { $.objectList[1].id = 2 }
Metric filter that matches a JSON property with a period (.) in the key: { $.['cluster.name'] = "c" }
Metric filter that matches JSON logs using IS: { $.SomeObject IS NULL }
Metric filter that matches JSON logs using NOT EXISTS { $.SomeOtherObject NOT EXISTS }

#### Using compound expressions to match terms in JSON objects

Expression that matches using AND (&&): { ($.user.id = 1) && ($.users[0].email = "John.Doe@example.com") }
Expression that matches using OR (||): { $.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch" && $.actions[2] = "nonmatch" }
Expression that doesn't match using AND (&&): { ($.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch") && $.actions[2] = "nonmatch" }
Expression that doesn't match using OR (||): { ($.user.id = 2 && $.users[0].email = "nonmatch") || $.actions[2] = "GET" }

#### Using metric filters to extract values from space-delimited log events

##### Example Log

127.0.0.1 Prod frank [10/Oct/2000:13:25:15 -0700] "GET /index.html HTTP/1.0" 404 1534

##### Format
enclose the metric filter in brackets ("[]"), and specify fields with names that are separated by commas (",")

[ip, user, username, timestamp, request =*.html*, status_code = 4*, bytes]

use numeric operators ( >, <, =, !=, >=, or <=) and the asterisk (*) as a wild card

##### ellipsis

use ellipsis (...) to reference any unnamed field. Elipsis can reference as many fields as needed.

[..., request =*.html*, status_code = 4*, bytes]

##### logical operator

use the logical operators AND (&&) and OR (||) to create compound expressions.

[ip, user, username, timestamp, request =*.html*, status_code = 404 || status_code = 410, bytes]


#### Using values in log events to increment a metric's value

- publish a numeric value in a JSON log event to a metric: { $.latency = * } metricValue: $.latency

Publishing dimensions with metrics

- specify any of the properties in the metric filter as a dimension: "eventType" : $.eventType

- specify any of the fields in the metric filter as a dimension: "server" : $server


---

### Cloudwatch - Log Group

[cloudwatch-log-group](cloudwatch-log-group.yaml)

---

### References

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Logs.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-start.html
  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-dataprotectionpolicy

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html#matching-terms-events


### TODO

- Alarm View EventBridge rule

- Alarm Notification Action, AutoScaling Action, EC2 Action, System's Manager Action

-- EC2 Action (arn:aws:automate:region:ec2:stop | arn:aws:automate:region:ec2:terminate | arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot)
-- arn:aws:autoscaling:region:account-id:scalingPolicy:policy-id:autoScalingGroupName/group-friendly-name:policyName/policy-friendly-name
-- arn:aws:ssm:region:account-id:opsitem:severity | arn:aws:ssm-incidents::account-id:response-plan:response-plan-name

- CloudwatchAgent
