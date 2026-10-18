> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AmazonECSInfrastructureRolePolicyForLoadBalancers.html
> Downloaded: 2026-10-18

# Amazon ECS infrastructure IAM role for load balancers

An Amazon ECS infrastructure IAM role for load balancers allows Amazon ECS to manage load balancer resources in your clusters on your behalf, and is used when: 
You want to use blue/green deployments with Amazon ECS. The infrastructure role allows Amazon ECS to manage load balancer resources for your deployments. 
You need Amazon ECS to create, modify, or delete load balancer resources such as target groups and listeners during deployment operations. 

When Amazon ECS assumes this role to take actions on your behalf, the events will be visible in AWS CloudTrail. If Amazon ECS uses the role to manage load balancer resources for your blue/green deployments, the CloudTrail log `roleSessionName` will be `ECSNetworkingWithELB` or `ecs-service-scheduler`. You can use this name to search events in the CloudTrail console by filtering for User name.

Amazon ECS provides a managed policy which contains the permissions required for load balancer management. For more information see, AmazonECSInfrastructureRolePolicyForLoadBalancers in the AWS Managed Policy Reference Guide. 

## Creating the Amazon ECS infrastructure role for load balancers 

Replace all `user input` with your own information.
Create a file named `ecs-infrastructure-trust-policy.json` that contains the trust policy to use for the IAM role. The file should contain the following:  

**JSON**   

****  

```
{
  "Version":"2012-10-17", 
  "Statement": [ 
    {
      "Sid": "AllowAccessToECSForInfrastructureManagement", 
      "Effect": "Allow", 
      "Principal": {
        "Service": "ecs.amazonaws.com" 
      }, 
      "Action": "sts:AssumeRole" 
    } 
  ] 
}

```
Use the following AWS CLI command to create a role named `ecsInfrastructureRoleForLoadBalancers` by using the trust policy that you created in the previous step. 

```
aws iam create-role \
      --role-name ecsInfrastructureRoleForLoadBalancers \
      --assume-role-policy-document file://ecs-infrastructure-trust-policy.json
```
Attach the AWS managed `AmazonECSInfrastructureRolePolicyForLoadBalancers` policy to the `ecsInfrastructureRoleForLoadBalancers` role. 

```
aws iam attach-role-policy \
      --role-name ecsInfrastructureRoleForLoadBalancers \
      --policy-arn arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForLoadBalancers
```
 
 

You can also use the IAM console's Custom trust policy workflow to create the role. For more information, see Creating a role using custom trust policies (console) in the IAM User Guide. Important

If the infrastructure role is being used by Amazon ECS to manage load balancer resources for your blue/green deployments, ensure the following before you delete or modify the role: 
The role isn't deleted while active deployments are in progress. 
The trust policy for the role isn't modified to remove Amazon ECS access (`ecs.amazonaws.com`). 
The managed policy `AmazonECSInfrastructureRolePolicyForLoadBalancers` isn't removed while active deployments are in progress. 

Deleting or modifying the role during active blue/green deployments may result in deployment failures and could leave your services in an inconsistent state. 

After you create the file, you must grant your user permission to pass the role to Amazon ECS. 

## Permission to pass the infrastructure role to Amazon ECS 

To use an ECS infrastructure IAM role for load balancers, you must grant your user permission to pass the role to Amazon ECS. Attach the following `iam:PassRole` permission to your user. Replace `ecsInfrastructureRoleForLoadBalancers` with the name of the infrastructure role that you created.  

**JSON**   

****  

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": "iam:PassRole",
            "Effect": "Allow",
            "Resource": ["arn:aws:iam::*:role/ecsInfrastructureRoleForLoadBalancers"],
            "Condition": {
                "StringEquals": {"iam:PassedToService": "ecs.amazonaws.com"}
            }
        }
    ]
}

```
     

For more information about `iam:Passrole` and updating permissions for your user, see Granting a user permissions to pass a role to an AWS service and Changing permissions for an IAM user in the AWS Identity and Access Management User Guide.
