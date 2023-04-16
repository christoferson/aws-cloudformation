## RDS Cloudformation

### RDS - MySQL

Provision RDS for MySQL

[rds-mysql](rds-mysql.yaml)

### RDS - Event

Provision RDS Event Subscription

[rds-event](rds-event.yaml)

### Resources

- [Cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html)


### TODO

- RDS Proxy

### Errors

- Resource handler returned message: "Cannot find version 8.0.20 for mysql


#### Connect

sudo yum install mysql
mysql -h xxxx.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
