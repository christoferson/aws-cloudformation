## CloudFormation CodeArtifact Examples

### CodeArtifact - Domain

Provision a CodeArtifact Domain

[codeartifact-domain](codeartifact-domain.yaml)

### CodeArtifact - Repository - Maven

Provision a CodeArtifact Repository Maven

[codeartifact-repository-mvn](codeartifact-repository-mvn.yaml)

### Permissions


Policy needs to be applied to both the Repository AND Domain.


##### [Domain](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html)

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Sid": "DomainPolicyForOrganization",
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
             "codeartifact:GetDomainPermissionsPolicy",
             "codeartifact:ListRepositoriesInDomain",
             "codeartifact:GetAuthorizationToken",
             "codeartifact:DescribeDomain",
             "codeartifact:CreateRepository"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": { "aws:PrincipalOrgID":["o-xxxxxxxxxxx"]}
        }
    }
}
```


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "codeartifact:DescribePackageVersion",
                "codeartifact:DescribeRepository",
                "codeartifact:GetPackageVersionReadme",
                "codeartifact:GetRepositoryEndpoint",
                "codeartifact:ListPackages",
                "codeartifact:ListPackageVersions",
                "codeartifact:ListPackageVersionAssets",
                "codeartifact:ListPackageVersionDependencies",
                "codeartifact:ReadFromRepository"
            ],
            "Effect": "Allow",
            "Principal": {
                 "AWS": "arn:aws:iam::123456789012:root"
            },
            "Resource": "*"
        }
    ]
}
```


```
{
  "Version": "2012-10-17",
  "Statement": [
      {
          "Effect": "Allow",
          "Action": [ "codeartifact:*" ],
          "Resource": "*",
          "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-xxxxxxxxxx"
                }
          }
      },
      {       
          "Effect": "Allow",
          "Action": "sts:GetServiceBearerToken",
          "Resource": "*",
          "Condition": {
              "StringEquals": {
                  "sts:AWSServiceName": "codeartifact.amazonaws.com"
              }
          }
      }
  ]
}
```

### Errors

- Resource handler returned message: "KMS key not found: aws/codeartifact (Service: Codeartifact, Status Code: 400, Request ID: 15c3171b-e68e-4d79-affa-7bd3f019c94f)" (RequestToken: 1115d97f-628c-98cf-5fc5-3394292158b1, HandlerErrorCode: InvalidRequest)

### References

- https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html

- https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html