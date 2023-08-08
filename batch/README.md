## Batch

### Batch - Concepts

#### Jobs
A unit of work (such as a shell script, a Linux executable, or a Docker container image) that you submit

#### Job Definitions
A job definition specifies how jobs are to be run. 
- IAM role to provide access to other AWS resources
- Memory and CPU requirements
- Control container properties, environment variables, and mount points for persistent storage

#### Job Queues
Job resides until it's scheduled onto a compute environment
Associate one or more compute environments with a job queue
Assign priority values for these compute environments and even across job queues themselves

#### Compute Environment
Set of managed or unmanaged compute resources that are used to run jobs

Fargate or EC2 - Amazon EC2 if your jobs require any of the following:
- More than four vCPUs
- More than 30 gibibytes (GiB) of memory
- A GPU
- An Arm-based AWS Graviton CPU
- A custom Amazon Machine Image (AMI)
- Any of the linuxParameters parameters

-----------------------------------------------------------------------------------------------------------------------

### Batch - EC2

Provision a Compute Environment, Job Queue, Definition

[batch-ec2](batch-ec2.yaml)

### Batch - EC2 with EFS

Provision a Compute Environment, Job Queue, Definition

[batch-ec2-efs](batch-ec2-efs.yaml)

### Batch - Fargate

Provision a Compute Environment (Fargate), Job Queue, Definition

[batch-fargate](batch-fargate.yaml)

### Batch - Fargate - Multiple Compute Environment

Provision 2 Compute Environments, Fargate & Fargate Spot, Job Queue, Definition

Job Queue references the 2 compute environments prioritizing Spot

```
  BatchJobQueue:
    Type: "AWS::Batch::JobQueue"
    Properties:
      Priority: 1
      ComputeEnvironmentOrder:
        - Order: 1
          ComputeEnvironment: !Ref BatchComputeEnvironmentSpot
        - Order: 2
          ComputeEnvironment: !Ref BatchComputeEnvironment
      State: ENABLED
```

[batch-fargate-multi-ce](batch-fargate-multi-ce.yaml)

### Batch - Fargate - Extra Service

Provision additional Job Queue, Job Definition and assign to an existing Compute Environment

[batch-fargate-xtra-service](batch-fargate-xtra-service.yaml)

### Batch - Fargate with EFS

Provision a Compute Environment (Fargate), Job Queue, Definition with EFS

- Note: Your Amazon EFS file system, Amazon ECS cluster, and Fargate tasks must all be in the same VPC.

https://aws.amazon.com/premiumsupport/knowledge-center/ecs-fargate-mount-efs-containers-tasks/?nc1=h_ls

[batch-fargate-efs](batch-fargate-efs.yaml)

-----------------------------------------------------------------------------------------------------------------------

### Errors

#### ECS Instance Role should be an ECS Instance Profile ARN
Must use AWS::IAM::InstanceProfile instead of AWS::IAM::Role

#### CannotStartContainerError: Error response from daemon: failed to create shim task: OCI runtime create failed

#### Exception : Fargate resource requirements (2.00 vCPU, 1024 MiB) not valid.
Must match memory cpu [combination](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)


#### Fargate requires that the ?privileged? setting be ?false? at the container level.
Privileged: false # Must be false for Fargate

#### Exception : desiredvCpus is not applicable for Fargate.,
Compute environment  desiredvCpus minvCpus

#### Error executing request, Exception : tags is not applicable for Fargate.

#### Exception : EFS is supported for Fargate platform version 1.4.0

Set PlatformVersion: 1.4.0. Error occurs if set to LATEST

-----------------------------------------------------------------------------------------------------------------------

### Resources

[fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate.html#fargate-job-queues)

https://docs.aws.amazon.com/batch/latest/userguide/batch-cwe-target.html

https://aws.amazon.com/about-aws/whats-new/2022/10/aws-batch-increases-compute-memory-resource-configurations-fargate-type-jobs-4x/?nc1=h_ls

- https://pages.awscloud.com/Running-Cost-Effective-Batch-Workloads-with-AWS-Batch-and-Amazon-EC2-Spot-Instances_1022-CMP_OD.html

### TODO

- [ ] SNS notify when batch fails https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_tutorial.html
- [ ] Extra Job Definition