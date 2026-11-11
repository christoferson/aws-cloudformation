<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_eventbridge.html -->
<!-- Downloaded: 2026-10-28 -->

# Processing GuardDuty findings with Amazon EventBridge

GuardDuty automatically publishes (sends) findings as events to Amazon EventBridge (formerly Amazon CloudWatch Events), a serverless event bus service. EventBridge delivers a stream of near real-time data from applications and services to targets such as Amazon Simple Notification Service (Amazon SNS) topics, AWS Lambda functions, and Amazon Kinesis streams. For more information, see [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

EventBridge enables automated monitoring and processing of GuardDuty findings by receiving [events](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html). EventBridge receives events for both newly generated findings and aggregated findings, where subsequent occurrences of an existing finding are combined with the original. Every GuardDuty finding is assigned a finding ID, and GuardDuty creates an EventBridge event for every finding with a unique finding ID. For information on how aggregation works in GuardDuty, see [GuardDuty finding aggregation](https://docs.aws.amazon.com/guardduty/latest/ug/finding-aggregation.html).

In addition to automated monitoring and processing, use of EventBridge enables longer-term retention of your findings data. GuardDuty stores findings for 90 days. With EventBridge, you can send findings data to your preferred storage platform and store the data for as long as you like. To retain findings for a longer duration, GuardDuty supports [Exporting generated findings to Amazon S3](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html).

###### Topics

-

[EventBridge notification frequency in GuardDuty](#eventbridge-freq-notifications-gdu)
-

[Set up an Amazon SNS topic and endpoint](#guardduty-eventbridge-set-up-sns-and-endpoint)
-

[Using EventBridge with GuardDuty](#eventbridge_events)
-

[Creating an EventBridge rule](#guardduty_eventbridge_severity_notification)
-

[EventBridge rule for multi-account environments](#guardduty_findings_eventbridge_multiaccount)

## Understanding EventBridge notification frequency in GuardDuty

This section explains how often you receive finding notifications through EventBridge and how to update the frequency for subsequent finding occurrences.

****Notifications for newly generated findings with a unique finding ID****

GuardDuty sends these notifications in near real-time when it generates a finding with a unique finding ID. The notification includes all subsequent occurrences of this finding ID during the notification generation process.

The notification frequency for newly generated findings is in near real-time. By default, you can not modify this frequency.

****Notifications for subsequent finding occurrences****

GuardDuty aggregates all subsequent occurrences of a particular finding type that take place within the 6-hour intervals into one single event. Only an administrator account can update the EventBridge notification frequency for subsequent finding occurrences. A member account can't update this frequency for their own account. For example, if the delegated GuardDuty administrator account updates the frequency to one hour, all member accounts will also have one hour notification frequency about the subsequent finding occurrences sent to EventBridge. For more information, see [Managing multiple accounts in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

As an administrator account, you can customize the default frequency of notifications about the subsequent finding occurrences. Possible values are 15 minutes, 1 hour, or the default 6 hours. For information about setting the frequency for these notifications, see [Step 5 – Setting frequency to export updated active findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html#guardduty_exportfindings-frequency).

For more details about administrator account receiving EventBridge notifications for member accounts, see [EventBridge rule for multi-account environments](#guardduty_findings_eventbridge_multiaccount).

## Set up an Amazon SNS topic and endpoint (Email, Slack, and Amazon Chime)

Amazon Simple Notification Service (Amazon SNS) is a fully managed service that provides message delivery from publishers to subscribers. Publishers communicate asynchronously with subscribers by sending messages to a *topic*. A topic is a logical access point and communication channel that lets you group multiple endpoints such as AWS Lambda, Amazon Simple Queue Service (Amazon SQS), HTTP/S, and an email address.

###### Note

You can add an Amazon SNS topic to your preferred EventBridge event rule during or after the creation of the rule.

** **Create an Amazon SNS topic****

To begin, you must first set up a topic in Amazon SNS and add an endpoint. To create a topic, perform the steps in [Step 1: Creating a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the *Amazon Simple Notification Service Developer Guide*. After the topic gets created, copy the topic ARN to the clipboard. You will use this topic ARN to continue with one of the preferred setups.

Choose a preferred method to establish where you want to send GuardDuty finding data.

**Email setup**

**To set up an email endpoint**

After you [Create an Amazon SNS topic](#guardduty-set-up-sns-topic-eventbridge), the next step is to create a subscription to this topic. Perform the steps under [Step 2: Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the *Amazon Simple Notification Service Developer Guide*.

1.

For **Topic ARN**, use the topic ARN created in the [Create an Amazon SNS topic](#guardduty-set-up-sns-topic-eventbridge) step. The topic ARN looks similar to the following:

```
arn:aws:sns:us-east-2:123456789012:your_topic
```

2.

For **Protocol**, select **Email**.
3.

For **Endpoint**, enter an email address where you want to receive the notifications from Amazon SNS.

After the subscription gets created, you will need to confirm it through your email client.

**Slack setup**

**To configure an Amazon Q Developer in chat applications client - Slack**

After you [Create an Amazon SNS topic](#guardduty-set-up-sns-topic-eventbridge), the next step is to configure the client for Slack.

Perform the steps under [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

**Chime setup**

**To configure an Amazon Q Developer in chat applications client - Chime**

After you [Create an Amazon SNS topic](#guardduty-set-up-sns-topic-eventbridge), the next step is to configure Amazon Q Developer for Chime.

Perform the steps under [Tutorial: Get started with Amazon Chime](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

## Using Amazon EventBridge for GuardDuty findings

With EventBridge, you create rules to specify the events that you want to monitor. These rules also specify the target services and applications that can perform automated actions if these events occur. A [target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) is a destination (a resource or an endpoint) that EventBridge sends an event to when the event matches the event pattern defined in the rule. Each event is a JSON object that conforms to the EventBridge schema for AWS events and contains a JSON representation of a finding. You can tailor the rule to send only those events that meet a certain criteria. For more information, see [Event schema](#guardduty_findings_eventbridge_format). Because the findings data is structured as an [EventBridge event](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html), you can monitor, process, and act upon findings by using other applications, services, and tools.

In order to receive notifications about GuardDuty findings based on events, you must create an EventBridge rule and a target for GuardDuty. This rule enables EventBridge to send notifications for findings that GuardDuty generates to the target that is specified in the rule.

###### Note

EventBridge and CloudWatch Events are the same underlying service and API. However, EventBridge includes additional features that help you receive events from software as a service (SaaS) applications and your own applications. Because the underlying service and API are the same, the event schema for GuardDuty findings is also the same.

**How archived and non-archived findings in GuardDuty work with EventBridge**

For findings that you manually archive, the initial and all subsequent occurrences of these findings (generated after the archiving is complete) are sent to EventBridge based on a specific notification frequency. For more information, see [Understanding EventBridge notification frequency in GuardDuty](#eventbridge-freq-notifications-gdu).

For the findings that are automatically archived with [Suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rule.html), the initial and all subsequent occurrences of these findings (generated after the archiving is complete) are *not* sent to EventBridge. You can view these automatically archived findings in the GuardDuty console.

### Event schema

An [event pattern](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) defines the data EventBridge uses to determine whether to send the event to the target. The EventBridge event for GuardDuty has the following format:

```
{
         "version": "0",
         "id": "cd2d702e-ab31-411b-9344-793ce56b1bc7",
         "detail-type": "GuardDuty Finding",
         "source": "aws.guardduty",
         "account": "111122223333",
         "time": "1970-01-01T00:00:00Z",
         "region": "us-east-1",
         "resources": [],
         "detail": {GUARDDUTY_FINDING_JSON_OBJECT}
        }
```

The `detail` value returns the JSON details of a single finding as an object, as opposed to returning the entire *findings* response syntax which supports multiple findings within an array.

For a complete list of all the parameters included in `GUARDDUTY_FINDING_JSON_OBJECT`, see [GetFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindings.html#API_GetFindings_ResponseSyntax). The `id` parameter that appears in `GUARDDUTY_FINDING_JSON_OBJECT` is the finding ID previously described.

## Creating an EventBridge rule for GuardDuty findings

The following procedures explain how to use the Amazon EventBridge console and the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) to create an EventBridge rule for GuardDuty findings. The rule detects EventBridge events that use the event schema and pattern for GuardDuty findings, and it sends those events to an AWS Lambda function for processing.

AWS Lambda is a compute service that you can use to run code without provisioning or managing servers. You package your code and upload it to AWS Lambda as a *Lambda function*. AWS Lambda then runs the function when the function is invoked. A function can be invoked manually by you, automatically in response to events, or in response to requests from applications or services. For information about creating and invoking Lambda functions, see the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

Choose your preferred method to create an EventBridge rule that sends your GuardDuty finding to a target.

**Console**

Follow these steps to use the Amazon EventBridge console to create a rule that automatically sends all GuardDuty finding events to a Lambda function for processing. The rule uses default settings for rules that run when specific events are received. For details about rule settings or to learn how to create a rule that uses custom settings, see [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *Amazon EventBridge User Guide*.

Before you create this rule, create the Lambda function that you want the rule to use as a target. When you create the rule, you'll need to specify this function as the target for the rule. Your target can also be the SNS topic that you created earlier. For more information, see [Set up an Amazon SNS topic and endpoint (Email, Slack, and Amazon Chime)](#guardduty-eventbridge-set-up-sns-and-endpoint).

###### To create an event rule by using console

1.

Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).
2.

In the navigation pane, under **Buses**, choose **Rules**.
3.

In the **Rules** section, choose **Create rule**.
4.

On the **Define rule detail** page, do the following:

  1.

For **Name**, enter a name for the rule.
  2.

(Optional) For **Description**, enter a brief description of the rule.
  3.

For **Event bus**, ensure that **default** is selected and **Enable the rule on the selected event bus** is turned on.
  4.

For **Rule type**, choose **Rule with an event pattern**.
  5.

When you finish, choose **Next**.

5.

On the **Build event pattern** page, do the following:

  1.

For **Event source**, choose **AWS events or EventBridge partner events**.
  2.

(Optional) For **Sample event**, review a sample finding event for GuardDuty to learn what an event might contain. To do this, choose **AWS events**. Then, for **Sample events**, choose **GuardDuty Finding**.
  3.

###### Option 1 - Using pattern form, a template that EventBridge provides

In the **Event pattern** section, you can do the following:

    1.

For **Creation method**, select **Use pattern form**.
    2.

For **Event source**, choose **AWS services**.
    3.

For **AWS service**, choose **GuardDuty**.
    4.

For **Event type**, choose **GuardDuty Finding**.

When you finish, choose **Next**.
  4.

###### Option 2 - Using custom event pattern in JSON

In the **Event pattern** section, you can do the following:

    1.

For **Creation method**, select **Custom pattern (JSON editor)**.
    2.

For **Event pattern**, paste the following custom JSON that will create an alert for medium, high, and critical findings. For more information, see [Findings severity levels](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html).

```
{
  "source": [
    "aws.guardduty"
  ],
  "detail-type": [
    "GuardDuty Finding"
  ],
  "detail": {
    "severity": [
      4,
      4.0,
      4.1,
      4.2,
      4.3,
      4.4,
      4.5,
      4.6,
      4.7,
      4.8,
      4.9,
      5,
      5.0,
      5.1,
      5.2,
      5.3,
      5.4,
      5.5,
      5.6,
      5.7,
      5.8,
      5.9,
      6,
      6.0,
      6.1,
      6.2,
      6.3,
      6.4,
      6.5,
      6.6,
      6.7,
      6.8,
      6.9,
      7,
      7.0,
      7.1,
      7.2,
      7.3,
      7.4,
      7.5,
      7.6,
      7.7,
      7.8,
      7.9,
      8,
      8.0,
      8.1,
      8.2,
      8.3,
      8.4,
      8.5,
      8.6,
      8.7,
      8.8,
      8.9,
      9,
      9.0,
      9.1,
      9.2,
      9.3,
      9.4,
      9.5,
      9.6,
      9.7,
      9.8,
      9.9,
      10,
      10.0
    ]
  }
}
```

When you finish, choose **Next**.

6.

###### Option A - Selecting AWS service - AWS Lambda as target

On the **Select target(s)** page, do the following:

  1.

For **Target types**, select **AWS service**.
  2.

For **Select a target**, choose **Lambda function**. Then, for **Function**, choose the Lambda function that you want to send finding events to.
  3.

For **Configure version/alias**, enter version or alias settings for the target Lambda function.
  4.

(Optional) For **Additional settings**, enter custom settings to specify which event data you want to send to the Lambda function. You can also specify how to handle events that aren't delivered to the function successfully.
  5.

When you finish, choose **Next**.

7.

###### Option B - Selecting SNS topic as target

On the **Select target(s)** page, do the following:

  1.

For **Target types**, select **AWS service**.
  2.

For **Select a target**, choose **SNS topic**. Then, for **Target location**, select the suitable option based on your target location. For **Topic**, choose the name of the SNS topic that you created.
  3.

Expand **Additional settings**. For **Configure target input**, choose **Input transformer**.
  4.

Choose **Configure input transformer**.
  5.

Copy the following code and paste it in the **Input Path** field under the **Target input transformer** section.

```
{
    "severity": "$.detail.severity",
    "Account_ID": "$.detail.accountId",
    "Finding_ID": "$.detail.id",
    "Finding_Type": "$.detail.type",
    "region": "$.region",
    "Finding_Description": "$.detail.description"
}
```

  6.

Copy the following code and paste it into the **Template** field to format the email.

```

{"message":"You have a severity <severity> GuardDuty finding type <Finding_Type> in the <region> Region.\n\nFinding Description:\n<Finding_Description>\n\nFor more details open the GuardDuty console at https://console.aws.amazon.com/guardduty/home?region=<region>#/findings?search=id%3D<Finding_ID>"}

```

###### Important

Provide the template as a single-line JSON object, with the message wrapped in a key such as `message`, as shown in the preceding example. Use `\n` to add line breaks.

GuardDuty finding fields such as `description` can contain unescaped control characters, including newlines. Don't use either of the following template formats:

    -

A bare quoted string
    -

A multi-line template that uses separate quoted strings on separate lines

With these formats, the substituted value can produce invalid JSON. EventBridge then rejects the event and doesn't deliver the notification.

###### Note

Email subscriptions receive the template output as is, so the email shows the `message` JSON object, and line breaks appear as `\n`. For formatted notifications, deliver the Amazon SNS topic to Amazon Q Developer in chat applications (Slack or Amazon Chime), or use an Lambda function as the target.

8.

On the **Configure tags** page, optionally enter one or more tags to assign to the rule. Then choose **Next**.
9.

On the **Review and create** page, review the rule’s settings and verify that they're correct.

To change a setting, choose **Edit** in the section that contains the setting, and then enter the correct setting. You can also use the navigation tabs to go to the page that contains a setting.
10.

When you finish verifying the settings, choose **Create rule**.

**API**

The following procedure shows how to use AWS CLI commands to create a EventBridge rule and target for GuardDuty. Specifically, the procedure shows you how to create a rule that enables EventBridge to send events for all findings that GuardDuty generates to an AWS Lambda function as a target for the rule.

###### Note

In this example, we're using a Lambda function as the target for the rule that triggers EventBridge. You can also configure other AWS resources as targets to trigger EventBridge. GuardDuty and EventBridge support the following target types - Amazon EC2 instances, Amazon Kinesis streams, Amazon ECS tasks, AWS Step Functions state machines, the `run` command, and built-in targets. For more information, see [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html) in the *Amazon EventBridge API Reference*.

###### To create a rule and target

1.

To create a rule that enables EventBridge to send events for all findings that GuardDuty generates, run the following EventBridge CLI command.

```
aws events put-rule --name your-rule-name --event-pattern "{\"source\":[\"aws.guardduty\"]}"
```

You can further customize your rule so that it instructs EventBridge to send events only for a subset of the GuardDuty-generated findings. This subset is based on the finding attribute or attributes that are specified in the rule. For example, use the following CLI command to create a rule that enables EventBridge to only send events for the GuardDuty findings with the severity of either 5 or 8:

```
aws events put-rule --name your-rule-name --event-pattern "{\"source\":[\"aws.guardduty\"],\"detail-type\":[\"GuardDuty Finding\"],\"detail\":{\"severity\":[5,8]}}"
```

For this purpose, you can use any of the property values that are available in the JSON for GuardDuty findings.
2.

To attach a Lambda function as a target for the rule that you created in step 1, run the following EventBridge CLI command.

```
aws events put-targets --rule your-rule-name --targets Id=1,Arn=arn:aws:lambda:us-east-1:111122223333:function:your-function
```

Make sure to replace `your-rule-name` with the name of the rule that you created in step 1, and `your-function` with your actual Lambda function for the GuardDuty events.
3.

To add the permissions required to invoke the target, run the following Lambda CLI command.

```
aws lambda add-permission --function-name your-function --statement-id 1 --action 'lambda:InvokeFunction' --principal events.amazonaws.com --source-arn arn:aws:events:us-east-1:111122223333:rule/your-rule-name
```

Make sure to replace `your-function` with your actual Lambda function for the GuardDuty events, and `your-rule-name` with the name of the rule that you created in step 1. The `--source-arn` condition allows only this rule to invoke the function.

## EventBridge rule for GuardDuty multi-account environments

When using a delegated GuardDuty administrator account, you can view the events generated in the member accounts and take action using other applications and services. EventBridge rules in your administrator account will trigger based on applicable findings from your member accounts. If you set up finding notifications through EventBridge in your administrator account, you will receive notifications of findings from both your account and member accounts. For example, you can use EventBridge to send specific types of findings to a Lambda function that processes and sends the data to your security incident and event management (SIEM) system.

You can identify the member account where the GuardDuty finding originated using the `accountId` field of the finding's JSON details. To create a custom event rule for specific member accounts, create a new rule and use the following template in **Event pattern**. Replace `123456789012` with the `accountId`of the member account for which you want to trigger the event.

```
{
  "source": [
    "aws.guardduty"
  ],
  "detail-type": [
    "GuardDuty Finding"
  ],
  "detail": {
    "accountId": [
      "123456789012"
    ]
  }
}

```

###### Note

This example creates a rule that matches all findings from the specified account ID. You can include multiple account IDs by separating them with commas, following JSON syntax.
