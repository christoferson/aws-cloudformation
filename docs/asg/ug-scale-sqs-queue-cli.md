> Source: https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-sqs-queue-cli.html
> Downloaded: 2026-10-24

# Configure scaling based on Amazon SQS

The following procedure describes how to configure automatic scaling based on Amazon SQS. You'll learn how to create a CloudWatch custom metric, how to set up a target tracking policy using the AWS CLI, and how to test your configuration. 

Before you begin, make sure that you have the AWS CLI installed and configured. Also, you must have an Amazon SQS queue to use. The following tasks assume that you already have a queue (standard or FIFO), an Auto Scaling group, and EC2 instances running the application that uses the queue. 

For more information about Amazon SQS, see the Amazon Simple Queue Service Developer Guide.Tasks
Step 1: Create a CloudWatch custom metric
Step 2: Create a target tracking scaling policy
Step 3: Test your scaling policy
 

## Step 1: Create a CloudWatch custom metric 

A custom metric is defined using a metric name and namespace of your choosing. Namespaces for custom metrics cannot start with `AWS/`. For more information about publishing custom metrics, see the Publish custom metrics topic in the Amazon CloudWatch User Guide. 

Follow this procedure to create the custom metric by first reading information from your AWS account. Then, calculate the backlog per instance metric, as recommended in an earlier section. Lastly, publish this number to CloudWatch at a 1-minute granularity. Whenever possible, we strongly recommend that you scale on metrics with a 1-minute granularity to ensure a faster response to changes in system load.  To create a CloudWatch custom metric (AWS CLI)
Use the SQS get-queue-attributes command to get the number of messages waiting in the queue (`ApproximateNumberOfMessages`).  

```
aws sqs get-queue-attributes --queue-url https://sqs.region.amazonaws.com/123456789/MyQueue \
  --attribute-names ApproximateNumberOfMessages
```
Use the describe-auto-scaling-groups command to get the running capacity of the group, which is the number of instances in the `InService` lifecycle state. This command returns the instances of an Auto Scaling group along with their lifecycle state.  

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names my-asg
```
Calculate the backlog per instance by dividing the approximate number of messages available for retrieval from the queue by the group's running capacity.  
Create a script that runs every minute to retrieve the backlog per instance value and publish it to a CloudWatch custom metric. When you publish a custom metric, you specify the metric's name, namespace, unit, value, and zero or more dimensions. A dimension consists of a dimension name and a dimension value. 

To publish your custom metric, replace placeholder values in `italics` with your preferred metric name, the metric's value, a namespace (as long as it doesn’t begin with "`AWS`"), and dimensions (optional), and then run the following put-metric-data command.  

```
aws cloudwatch put-metric-data --metric-name MyBacklogPerInstance --namespace MyNamespace \
  --unit None --value 20 --dimensions MyOptionalMetricDimensionName=MyOptionalMetricDimensionValue
```
 
 

After your application is emitting the desired metric, the data is sent to CloudWatch. The metric is visible in the CloudWatch console. You can access it by logging into the AWS Management Console and navigating to the CloudWatch page. Then, view the metric by navigating to the metrics page or by searching for it using the search box. For information about viewing metrics, see View available metrics in the Amazon CloudWatch User Guide. 

## Step 2: Create a target tracking scaling policy 

The metric you created can now be added to a target tracking scaling policy. To create a target tracking scaling policy (AWS CLI)
Use the following `cat` command to store a target value for your scaling policy and a customized metric specification in a JSON file named `config.json` in your home directory. Replace each `user input placeholder` with your own information. For the `TargetValue`, calculate the acceptable backlog per instance metric and enter it here. To calculate this number, decide on a normal latency value and divide it by the average time that it takes to process a message, as described in an earlier section.  

If you didn't specify any dimensions for the metric you created in step 1, don't include any dimensions in the customized metric specification. 

```
$ cat ~/config.json
{
   "TargetValue":100,
   "CustomizedMetricSpecification":{
      "MetricName":"MyBacklogPerInstance",
      "Namespace":"MyNamespace",
      "Dimensions":[
         {
            "Name":"MyOptionalMetricDimensionName",
            "Value":"MyOptionalMetricDimensionValue"
         }
      ],
      "Statistic":"Average",
      "Unit":"None"
   }
}
```
Use the put-scaling-policy command, along with the `config.json` file that you created in the previous step, to create your scaling policy. 

```
aws autoscaling put-scaling-policy --policy-name sqs100-target-tracking-scaling-policy \
  --auto-scaling-group-name my-asg --policy-type TargetTrackingScaling \
  --target-tracking-configuration file://~/config.json
```
 

This creates two alarms: one for scaling out and one for scaling in. It also returns the Amazon Resource Name (ARN) of the policy that is registered with CloudWatch, which CloudWatch uses to invoke scaling whenever the metric threshold is in breach.  
 

## Step 3: Test your scaling policy 

After your setup is complete, verify that your scaling policy is working. You can test it by increasing the number of messages in your SQS queue and then verifying that your Auto Scaling group has launched an additional EC2 instance. You can also test it by decreasing the number of messages in your SQS queue and then verifying that the Auto Scaling group has terminated an EC2 instance. To test the scale-out function
Follow the steps in Creating an Amazon SQS standard queue and sending a message or Creating an Amazon SQS FIFO queue and sending a message to add messages to your queue. Make sure that you have increased the number of messages in the queue so that the backlog per instance metric exceeds the target value. 

It can take a few minutes for your changes to invoke the alarm. 
Use the describe-auto-scaling-groups command to verify that the group has launched an instance. 

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name my-asg
```
 
 To test the scale in function
Follow the steps in Receive and delete a message (console) to delete messages from the queue. Make sure that you have decreased the number of messages in the queue so that the backlog per instance metric is below the target value. 

It can take a few minutes for your changes to invoke the alarm. 
Use the describe-auto-scaling-groups command to verify that the group has terminated an instance. 

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name my-asg
```
