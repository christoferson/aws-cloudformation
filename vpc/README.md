
## CloudFormation VPC Examples

### Concepts

- VPC EnableDnsSupport - Enable Route53 Resolver. Otherwise we need Custom DNS Server.

- VPC EnableDnsHostnames - Assign Public HostName to Instances if it has Public IP.

### Vpc - 2 Public Subnets Only

VPC with Public Subnets only and spans 2 Availability Zones

[vpc-public](vpc-public.yaml)

### Vpc - 2 Public and Private Subnets + NAT Gateways

VPC with 2 Public and Private Subnets. Spans 2 Availability Zone. NAT Gateways in each AZ.

[vpc-public-private-nat](vpc-public-private-nat.yaml)

### Vpc FlowLogs - CloudWatch

Provision a VPC FlowLog and send logs to Cloudwatch.

[vpc-flowlogs-cw](vpc-flowlogs-cw.yaml)

### TODO
3 Public Private Subnets
NAT or NOT
6 Private Subnets
S3 or Dynamo
FlowLogs S3

### Errors - FlowLogs

DestinationOptions is not supported when LogDestinationType is cloud-watch-logs


### References

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-destinationoptions
