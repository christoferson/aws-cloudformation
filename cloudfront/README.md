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

[cloudfront-s3](cloudfront-s3.yaml)


### References
- managed cache policies
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html