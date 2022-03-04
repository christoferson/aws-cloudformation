## EC2 

Cloudformation templates for EC2

### EC2 Basic

Launch an ec2 instance inside a the specified public subnet. 

- Creates IAM Role and Instance Profile
- Creates a Security Group for SSH Access. 
    - Need to provide allowed IP Range
    - Need to provide SSH Key
- Creates a Security Group for HTTP Access
- Enables SSM to connect to instance

ec2-basic

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

### Load Balancer + Auto Scaling Group

Provision Application Load Balancer in the public subnets and delegates traffic to the fleet of instances in the private subnet. The fleet of instances is managed by the auto scaling group.

ec2-alb

### Cloudformation Documentation

- [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)





