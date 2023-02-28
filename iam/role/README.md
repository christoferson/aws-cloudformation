## IAM Role Cloudformation

### IAM - Role - EC2 Cloudwatch Agent

##### Install Cloudwatch Agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm 
sudo rpm -U ./amazon-cloudwatch-agent.rpm

##### Apply Cloudwatch Configuration from SSM Parameter
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:AmazonCloudWatch-ec2-cloudwatch-agent-config -s

##### AWS Cloudwatch Console

https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#metricsV2:graph=~();namespace=~'CWAgent

##### Check cloudwatch agent process

ps -ef | grep cloudwatch

```
root      4096     1  0 14:38 ?        00:00:01 /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent -config /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.toml -envconfig /opt/aws/amazon-cloudwatch-agent/etc/env-config.json -pidfile /opt/aws/amazon-cloudwatch-agent/var/amazon-cloudwatch-agent.pid
```

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


### Links

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent-New-Instances-CloudFormation.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent-commandline.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html

- https://github.com/awslabs/aws-cloudformation-templates/tree/master/aws/solutions/AmazonCloudWatchAgent