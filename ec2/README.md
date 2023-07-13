## EC2 

Cloudformation templates for EC2

### EC2 Basic

Launch an ec2 instance inside a the specified public subnet. 

- Creates IAM Role and Instance Profile
- Creates a Security Group for HTTP Access
- Enables SSM to connect to instance
- Installs HTTPD on instance

[ec2-basic](./ec2-basic.yaml)



### EC2 Basic with Options

Launch an ec2 instance inside a the specified public subnet. 

- Creates IAM Role and Instance Profile
- Creates a Security Group for HTTP Access
- Enables SSM to connect to instance
- Installs HTTPD on instance
- Creates a Security Group for SSH Access. 
    - Need to provide allowed IP Range
    - Need to provide SSH Key

[ec2-basic-options](./ec2-basic-options.yaml)

### EC2 Basic - With Volume

Provision EC2 instance with Volume and Volume Attachment

[ec2-volume](ec2-volume.yaml)

### EC2 with Unified CloudWatch Agent

Launch an ec2 instance inside a the specified public subnet with Unified CloudWatch agent.
CloudWatch agent will send logs and additional metrics.

- Configure Unified CloudWatch Agent and send HTTP Logs (/var/log/httpd/access_log, /var/log/httpd/error_log) to CloudWatch

- Instance Role must have policy CloudWatchAgentServerPolicy.
- SSM Parameter Name must start with AmazonCloudWatch- to match policy in CloudWatchAgentServerPolicy.


Check the Agent Status

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
```

Initialize the Agent with the SSM Config if needed

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:AmazonCloudWatch-agent-config -s
```

Agent Log

```
/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log
```

[ec2-cloudwatch](ec2-cloudwatch.yaml)

### User Data

Launch instance with httpd initialized using user data

ec2-user-data

### CloudFormation Init

Cloudformation init signal and metadata example.

Also includes examples for cfn utilities to detect changes in the metadata.

```
/opt/aws/bin/cfn-hup || error_exit 'Failed to start cfn-hup'
/etc/cfn/cfn-hup.conf
/etc/cfn/hooks.d/cfn-auto-reloader.conf
```
Use the following command to get the latest metadata

```
/opt/aws/bin/cfn-get-metadata --stack <stack-name> --resource EC2Instance --region eu-west-1
```

ec2-cfn-signal

### Launch Template

Launch instance using launch template

ec2-template

### EC2 Load Balancer + Auto Scaling Group

Provision Application Load Balancer in the public subnets and delegates traffic to the fleet of instances in the private subnets. The fleet of instances is managed by the auto scaling group.

TODO: Add Dynamic Scaling

[ec2-alb](./ec2-alb.yaml)

### Cloudformation Documentation

- [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)


### Resources

- https://aws.amazon.com/jp/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-autoscaling.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.html

### TODO
GRPC





### Hekper Scripts

cfn-init
[ec2-helper-cfn-init](ec2-helper-cfn-init.yaml)

cfn-signal

cfn-get-metadata

cfn-hup
The cfn-hup helper is a daemon that detects changes in resource metadata and runs user-specified actions when a change is detected. This allows you to make configuration updates on your running Amazon EC2 instances through the UpdateStack API action.