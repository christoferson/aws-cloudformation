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

[cloudfront-s3-bucket](cloudfront-s3-bucket.yaml)

### Cloudfront - S3 - Static Website

Provision a cloudfront for S3. 
No ACM Certificate/Alias. No OAI.

[cloudfront-s3-website-origin](cloudfront-s3-website-origin.yaml)
[cloudfront-s3-website](cloudfront-s3-website.yaml)


### References
- managed cache policies
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html

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
