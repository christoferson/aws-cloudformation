## Cloudfront

### Cloudfront - Demo

Provision a cloudfront showcasing multiple Origin Types

- bucket-ws/*  S3 Bucket Website Origin
- bucket/* S3 Bucket Origin
- oai/* S3 Origin OAI
- oac/* S3 Origin OAC
- lambda/* Lambda Origin
- elb/* Load Balancer Origin (http)

Lambda and ELB uses OriginCustomHeaders to limit access to clients via CloudFront

- [cloudfront-demo](cloudfront-demo.yaml)

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

### Cloudfront - Signed Cookie

Provision an S3 Bucket fronted by Cloudfront. Path /secure can only be accessed using Signed Url or Cookies.

Also Creates a lambda that can be used to generate the signed cookies available from path /sign/xx. Make sure to set the values in the Environment Variables.

#### Process:

1. Create Private and Public Key

openssl.exe genrsa -out private_key.pem 2048
openssl.exe rsa -pubout -in private_key.pem -out public_key.pem

2. Create the Public Key and Key Group via AWS Console (Alternative)

Cloudfront > Key Management > Public keys > Create Public Key. Take note of the ID 
Cloudfront > Key Management > Key groups > Create Key Group

This is equivalent to the below  definition in cloudfront-s3-signed-cookie

```(yaml)
  CloudFrontPublicKey:
    Type: AWS::CloudFront::PublicKey
    Properties:
      PublicKeyConfig:
        Name: "cfn-public-key"
        Comment: cfn-example signed public key
        CallerReference: "20230208000512.523756"
        EncodedKey: |
          -----BEGIN PUBLIC KEY-----
          MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0ZCz4OoFhfPm38JraZKT
          85GRaxS2mfZC2IWfatpzirsBb7vX1HIVyEhE7uiLAyftO6Y0xj9HzKQFkzuIl9iD
          oI69MovHGtb+BM5f4VnN4Srf2CkWgpF5jqwf8jRTpvKkoKyNGABWCTIYIbJrt0JM
          xIg5xt4UFa7ARGxiMejqOwvlf2dwtmwEaNvdZGxCpnDQ9cpKUvlxzs6sn+KclsR3
          WhRQPueY5nfy0C+ICyzwXSc+yUharjtuyFYbh5WKgrFcXRgixKzHVaIhAaaAkuA6
          z9cn/AbbTO4NzhP/pKwyw0dm1E0RkOkCprEVLWvWA9bgxYLQRoO1ii0khtUtBZ6Z
          PwIDAQAB
          -----END PUBLIC KEY-----

  CloudFrontKeyGroup:
    Type: AWS::CloudFront::KeyGroup
    DependsOn:
      - CloudFrontPublicKey
    Properties:
      KeyGroupConfig:
        Name: "cfn-public-key-group-config"
        Comment: cfn-example signed key group
        Items:
          - !Ref 'CloudFrontPublicKey'
```

3. 


[cloudfront-s3-signed-cookie](cloudfront-s3-signed-cookie)

### Errors

- Internal error reported from downstream service during operation 'null'

- Invalid request provided: Illegal configuration: The origin type and OAC origin type differ. 
  For S3 OAC, make sure you specify S3OriginConfig instead of CustomOriginConfig

- Exactly one of [AcmCertificateArn, CloudFrontDefaultCertificate, IamCertificateId] needs to be specified

### References
- [cloudformation](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_CloudFront.html)
- managed cache policies
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html
- https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-cloudfront-origin-access-control/?nc1=h_ls
- https://aws.amazon.com/jp/about-aws/whats-new/2023/11/amazon-cloudfront-keyvaluestore-globally-managed-key-value-datastore/
- https://repost.aws/questions/QU4VpxEkw_Q6yQotN5JhkBEA/lambda-function-url-not-returning-multiple-cookies

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
- Origin ALB
- Signed Cookies

Migrating from origin access identity (OAI) to origin access control (OAC)
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html


