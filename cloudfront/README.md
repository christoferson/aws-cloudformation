## Cloudfront

### Cloudfront - Lambda

Provision a cloudfront for Lambda Backend

- [cloudfront-lambda-origin](cloudfront-lambda-origin.yaml)
- [cloudfront-lambda](cloudfront-lambda.yaml)

### Cloudfront - S3 - Bucket

Bucket must allow public access and appropriate bucket policy.

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}
```
[cloudfront-s3-bucket-origin](cloudfront-s3-bucket-origin.yaml)
[cloudfront-s3-bucket](cloudfront-s3-bucket.yaml)

### Cloudfront - S3 - Static Website

Provision a cloudfront for S3 Static WebSite. 
No ACM Certificate/Alias. No OAI.

[cloudfront-s3-website-origin](cloudfront-s3-website-origin.yaml)
[cloudfront-s3-website](cloudfront-s3-website.yaml)

### Cloudfront - S3 - Origin Access Identifier

Provision a cloudfront for S3. Access files using Origin Access Identifier (OAI)

[cloudfront-s3-oai-origin](cloudfront-s3-oai-origin.yaml)
[cloudfront-s3-oai](cloudfront-s3-oai.yaml)

### Cloudfront - S3 - Origin Access Control

[cloudfront-s3-oac-origin](cloudfront-s3-oac-origin.yaml)

### Errors

- Internal error reported from downstream service during operation 'null'

- Invalid request provided: Illegal configuration: The origin type and OAC origin type differ. 
  For S3 OAC, make sure you specify S3OriginConfig instead of CustomOriginConfig

### References
- [cloudformation](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_CloudFront.html)
- managed cache policies
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html
- https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-cloudfront-origin-access-control/?nc1=h_ls


### TODO
- Origin
- OAI
- Create Origin Group
- AWS WAF
- Alternate domain name (CNAME) 
- Custom SSL certificate - optional
- Standard logging
- Error Response
- Multi Path

Migrating from origin access identity (OAI) to origin access control (OAC)
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
