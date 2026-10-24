> Source: https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy_creating.html
> Downloaded: 2026-10-24

# Create a target tracking scaling policy

To create a target tracking scaling policy for your Auto Scaling group, use one of the following methods. 

Before you begin, confirm that your preferred metric is available at 1-minute intervals (compared to the default 5-minute interval of Amazon EC2 metrics). 

**Console** To create a target tracking scaling policy for a new Auto Scaling group
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/, and choose Auto Scaling Groups from the navigation pane.
Choose Create Auto Scaling group. 
In Steps 1, 2, and 3, choose the options as desired and proceed to Step 4: Configure group size and scaling policies. 
Under Scaling, specify the range that you want to scale between by updating the Min desired capacity and Max desired capacity. These two settings allow your Auto Scaling group to scale dynamically. For more information, see Set scaling limits for your Auto Scaling group. 
Under Automatic scaling, choose Target tracking scaling policy. 
To define a policy, do the following: 
Specify a name for the policy. 
For Metric type, choose a metric.  

If you chose Application Load Balancer request count per target, choose a target group in Target group. 
Specify a Target value for the metric. 
(Optional) For Instance warmup, update the instance warmup value as needed. 
(Optional) Select Disable scale in to create only a scale-out policy. This allows you to create a separate scale-in policy of a different type if wanted. 
Proceed to create the Auto Scaling group. Your scaling policy will be created after the Auto Scaling group has been created.  
 To create a target tracking scaling policy for an existing Auto Scaling group
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/, and choose Auto Scaling Groups from the navigation pane.
Select the check box next to your Auto Scaling group. 

A split pane opens up in the bottom of the page.  
Verify that the scaling limits are appropriately set. For example, if your group's desired capacity is already at its maximum, you need to specify a new maximum in order to scale out. For more information, see Set scaling limits for your Auto Scaling group. 
On the Automatic scaling tab, in Dynamic scaling policies, choose Create dynamic scaling policy. 
To define a policy, do the following: 
For Policy type, keep the default of Target tracking scaling.  
Specify a name for the policy. 
For Metric type, choose a metric. You can choose only one metric type. To use more than one metric, create multiple policies. 

If you chose Application Load Balancer request count per target, choose a target group in Target group. 
Specify a Target value for the metric. 
(Optional) For Instance warmup, update the instance warmup value as needed. 
(Optional) Select Disable scale in to create only a scale-out policy. This allows you to create a separate scale-in policy of a different type if wanted. 
Choose Create. 
  

**AWS CLI** 

To create a target tracking scaling policy, you can use the following example to help you get started. Replace each `user input placeholder` with your own information. Note

For more examples, see Example scaling policies for the AWS CLI. To create a target tracking scaling policy (AWS CLI)
Use the following `cat` command to store a target value for your scaling policy and a predefined metric specification in a JSON file named `config.json` in your home directory. The following is an example target tracking configuration that keeps the average CPU utilization at 50 percent. 

```
$ cat ~/config.json
{
  "TargetValue": 50.0,
  "PredefinedMetricSpecification": 
    {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    }
}
```
 

For more information, see PredefinedMetricSpecification in the Amazon EC2 Auto Scaling API Reference. 
Use the put-scaling-policy command, along with the `config.json` file that you created in the previous step, to create your scaling policy. 

```
aws autoscaling put-scaling-policy --policy-name cpu50-target-tracking-scaling-policy \
  --auto-scaling-group-name my-asg --policy-type TargetTrackingScaling \
  --target-tracking-configuration file://config.json
```
 

If successful, this command returns the ARNs and names of the two CloudWatch alarms created on your behalf. 

```
{
    "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:228f02c2-c665-4bfd-aaac-8b04080bea3c:autoScalingGroupName/my-asg:policyName/cpu50-target-tracking-scaling-policy",
    "Alarms": [
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e",
            "AlarmName": "TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e"
        },
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2",
            "AlarmName": "TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2"
        }
    ]
}
```
