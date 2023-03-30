## ECR

### ECR - Repository

Provision an Elastic Container Repository

[ecr-repository](ecr-repository.yaml)


### ECR - Private Policy

TODO

[ecr-private-policy](ecr-private-policy.yaml)

### ECR - Pull Through Cache Rule

Define the prefix 'ecr-public' for 'public.ecr.aws'.

You can set the permissions on what repositories and who can use the pull through cache by defining RepositoryPolicy. see [ecr-policy-pull-through-cache](ecr-policy-pull-through-cache.yaml)

[ecr-svc-pull-through-cache-rule](ecr-svc-pull-through-cache-rule.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ECR.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html

- https://aws.amazon.com/blogs/compute/introducing-cross-account-amazon-ecr-access-for-aws-lambda/
