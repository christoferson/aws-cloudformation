## RDS Cloudformation

### RDS - MySQL

Provision RDS for MySQL

[rds-mysql](rds-mysql.yaml)

### RDS - MySQL - With Secrets

Provision RDS for MySQL. Also provisions a SecretsManager Secret with Auto Rotation enabled for the Database Password.

First the Secret is created using AWS::SecretsManager::Secret

Next, the Secret is associated with the Database via AWS::SecretsManager::SecretTargetAttachment

After the Secret is attached to the database, we enable rotation using AWS::SecretsManager::RotationSchedule

[rds-mysql-with-secrets](rds-mysql-with-secrets.yaml)

### RDS - MySQL - Proxy

[troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.troubleshooting.html)

[rds-mysql-proxy](rds-mysql-proxy.yaml)

### RDS - Event

Provision RDS Event Subscription

[rds-event](rds-event.yaml)

### Resources

- [Cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html)

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html

- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.troubleshooting.html

### TODO

- RDS Proxy

### Errors

- Resource handler returned message: "Cannot find version 8.0.20 for mysql


#### Connect to MySQL Database using EC2 in Public Subnet

sudo yum install mysql

mysql -h xxxx.us-east-1.rds.amazonaws.com -P 3306 -u admin -p

