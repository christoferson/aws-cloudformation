## CloudFormation VPC Examples

### Concepts

- VPC EnableDnsSupport - Enable Route53 Resolver. Otherwise we need Custom DNS Server.

- VPC EnableDnsHostnames - Assign Public HostName to Instances if it has Public IP.

#### Concepts - Private IP Address
  
  - (10.0.0.0/8) 10.0.0.0 - 10.255.255.255 1 x Class A
  - (172.16.0.0/12) 172.16.0.0 - 172.31.255.255  16 x Class B
  - (192.168.0.0/16) 192.168.0.0 - 192.168.255.255 256 x Class C

### Vpc - 2 Public Subnets Only

VPC with Public Subnets only and spans 2 Availability Zones

[vpc-public](vpc-public.yaml)

### Vpc - 2 Public and Private Subnets + NAT Gateways

VPC with 2 Public and Private Subnets. Spans 2 Availability Zone. NAT Gateways in each AZ.

[vpc-public-private-nat](vpc-public-private-nat.yaml)

### Vpc - 3 Public Subnets Only

VPC with Public Subnets only and spans 3 Availability Zones

[vpc-3-public](3az/vpc-public.yaml)

### Vpc - 3 Public and Private Subnets

VPC with Public Subnets only and spans 3 Availability Zones

[vpc-3-public-private](3az/vpc-public-private.yaml)

### Vpc FlowLogs - CloudWatch

Provision a VPC FlowLog and send logs to Cloudwatch.

[vpc-flowlogs-cw](vpc-flowlogs-cw.yaml)

### VPC Prefix List

VPC Prefix List

[vpc-prefixlist](vpc-prefixlist.yaml)

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

- https://www.site24x7.com/tools/ipv4-subnetcalculator.html
