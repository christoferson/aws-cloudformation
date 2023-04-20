## IAM Role Cloudformation

### IAM - Role - EC2 CloudWatch Agent

Provision a Role and a Profile for EC2 instance where Unified CloudWatch Agent will be installed.

Also, creates an SSM Parameter where the CloudWatch Agent Configuration will be stored.


----------

After provisioning the roles and SSM Parameter, login to the EC2 instance then install and apply CloudWatch configuration.

##### Install CloudWatch Agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm 
sudo rpm -U ./amazon-cloudwatch-agent.rpm

##### Apply CloudWatch Configuration from SSM Parameter
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:AmazonCloudWatch-ec2-cloudwatch-agent-config -s

##### Check CloudWatch Agent Process is Running

ps -ef | grep cloudwatch

```
root      4096     1  0 14:38 ?        00:00:01 /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent -config /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.toml -envconfig /opt/aws/amazon-cloudwatch-agent/etc/env-config.json -pidfile /opt/aws/amazon-cloudwatch-agent/var/amazon-cloudwatch-agent.pid
```


----------

After enabling the Agent, you should be able to see metrics under the CWAgent category

##### AWS CloudWatch Console

https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#metricsV2:graph=~();namespace=~'CWAgent

You should be able to check the available memory is consistent with the CWAgent/mem_used_percent metric.

##### Command to show available memory

cat /proc/meminfo or free -m

```
              total        used        free      shared  buff/cache   available
Mem:            964         104         260           0         599         722
Swap:             0           0           0
```

[iam-role-cloudwatch-agent](iam-role-cloudwatch-agent.yaml)



### Install HTTPD on EC2

- sudo su

- yum install httpd

- echo "unified cloudwatch agent" > /var/www/html/index.html

- sudo systemctl start httpd

- sudo systemctl enable httpd

### EC2 with CloudWatch Agent

[ec2-cloudwatch](ec2-cloudwatch.yaml)

### Troubleshooting CloudWatch Agent

##### Agent fails to start

/opt/aws/amazon-cloudwatch-agent/logs/configuration-validation.log

##### Metrics does not appear in the Board

Check the configuration file amazon-cloudwatch-agent.json

### Links

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent-New-Instances-CloudFormation.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent-commandline.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html

- https://github.com/awslabs/aws-cloudformation-templates/tree/master/aws/solutions/AmazonCloudWatchAgent

### TODO

- Configuration to push logs

- CF template to provision everything from scratch