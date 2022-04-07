## Batch

### Batch - EC2 Basic

Provision a Compute Environment, Job Queue, Definition

[batch-ec2](batch-ec2.yaml)


### Batch - Fargate

### Batch - Fargate with EFS

- Note: Your Amazon EFS file system, Amazon ECS cluster, and Fargate tasks must all be in the same VPC.

https://aws.amazon.com/premiumsupport/knowledge-center/ecs-fargate-mount-efs-containers-tasks/?nc1=h_ls

### Errors

## ECS Instance Role should be an ECS Instance Profile ARN
Must use AWS::IAM::InstanceProfile instead of AWS::IAM::Role

## Exception : Fargate resource requirements (2.00 vCPU, 1024 MiB) not valid.
Must match memory cpu [combination](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)


## Fargate requires that the ?privileged? setting be ?false? at the container level.
Privileged: false # Must be false for Fargate

## Exception : desiredvCpus is not applicable for Fargate.,
Compute environment  desiredvCpus minvCpus

## Error executing request, Exception : tags is not applicable for Fargate.

## Exception : EFS is supported for Fargate platform version 1.4.0

Set PlatformVersion: 1.4.0. Error occurs if set to LATEST

### Resources

[fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate.html#fargate-job-queues)