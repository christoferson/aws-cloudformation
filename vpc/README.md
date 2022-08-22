
## CloudFormation VPC Examples

### Concepts

EnableDnsSupport - Enable Route53 Resolver. Otherwise we need Custom DNS Server.

### Vpc - 2 Public Subnets Only

VPC with Public Subnets only and spans 2 Availability Zones

[vpc-public](vpc-public.yaml)

### Vpc - 2 Public and Private Subnets + NAT Gateways

VPC with 2 Public and Private Subnets. Spans 2 Availability Zone. NAT Gateways in each AZ.

[vpc-public-private-nat](vpc-public-private-nat.yaml)

### TODO
3 Public Private Subnets
NAT or NOT
6 Private Subnets
S3 or Dynamo