## Elastic Beanstalk

### Elastic Beanstalk - Min

Provision Beanstalk using default VPC. 

- Provision error if no default VPC.

[eb-min](eb-min.yaml) 

### Elastic Beanstalk - Basic

Provision Beanstalk using specified VPC. 

- Provision error if no default VPC.

[eb-basic](eb-basic.yaml) 

### Errors

- Configuration validation exception: LoadBalancer type option cannot be changed. (Service: AWSElasticBeanstalk; Status Code: 400; Error Code: ConfigurationValidationException;


### References

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html