## Route53 Cloudformation

- Cloudformation does not support domain registration. Need to do via Console.

- Registering a domain will automatically Hosted Zone.

### Route 53 - Hosted Zone

Provision a Route53 Hosted Zone.

[route53-hostedzone](route53-hostedzone.yaml)

### Route 53 - Hosted Zone - HTTP - LoadBalancer

Points exiting Hosted Zone to a new LoadBalancer backed by Lambda

[route53-record-lb2](route53-record-lb2.yaml)

### Route 53 - Hosted Zone - HTTPS - Cognito Auth

Provision a Route53 Hosted Zone. Also provision ALB backed by Lambda to test Subdomain.
Finally Adds Cognito for Authentication.

Setup:

- [https-certificate](setup/route53-record-lb2-https-cognito/certificate-manager-public.yaml)

[route53-record-lb2-https-cognito](route53-record-lb2-https-cognito.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53.html
- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
- https://repost.aws/knowledge-center/cloudformation-ssl-tls-certificates-alb

### Errors

- The user pool client must have a client secret (Service: ElasticLoadBalancingV2

- "Invalid request provided: The function must be in region 'us-east-1'. ARN: arn:aws:lambda:eu-west-1:xxx:function:route53-record-cloudfront-LambdaFunctionEdgeCognit-u1VuMGseaUXC:1 

- "Invalid request provided: The function timeout is larger than the maximum allowed for functions that are triggered by a CloudFront event: 15 Max allowed: 5 Function: arn:aws:lambda:us-east-1:xxx:function:route53-record-cloudfront-LambdaFunctionEdgeCognit-cccc:1

TODO
- [ ] AWS::Route53::CidrCollection
AWS::Route53::DNSSEC
AWS::Route53::KeySigningKey
- [ ] AWS::Route53::HealthCheck
AWS::Route53::HostedZone Public vs Private
AWS::Route53::RecordSetGroup
AWS::Route53::RecordSet