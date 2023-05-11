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

### ECR - Cross Account Replication

#### Configure the replication settings in the Source Account

```
  EcrReplicationConfiguration:
    Type: "AWS::ECR::ReplicationConfiguration"
    Properties:
      ReplicationConfiguration: 
          Rules:
            - 
              Destinations:
                - 
                  Region: !Ref RepositoryStgRegionID
                  RegistryId: !Ref RepositoryStgAccountID
              RepositoryFilters:
                - 
                  FilterType: "PREFIX_MATCH" 
                  Filter: !Ref RepositoryFilterPrefix   
```

[ecr-svc-replication-rule](ecr-svc-replication-rule.yaml)


#### Next, configure the permissions in the Destination Account

```
  PrivateRegistryPolicy:
    Type: "AWS::ECR::RegistryPolicy"
    Properties:
      PolicyText:
        Version: 2012-10-17
        Statement:
          - Sid: replicate-repository
            Effect: Allow
            Principal:
              AWS: !Sub "arn:aws:iam::${RepositoryReplicationSourceAccountID}:root" #Source
            Action:
              - "ecr:CreateRepository"
              - "ecr:ReplicateImage"
            Resource: !Sub "arn:aws:ecr:${AWS::Region}:${AWS::AccountId}:repository/*" #Destination
```

[ecr-policy-replicate-repository](ecr-policy-replicate-repository.yaml)

### Links

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ECR.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html

- https://aws.amazon.com/blogs/compute/introducing-cross-account-amazon-ecr-access-for-aws-lambda/
