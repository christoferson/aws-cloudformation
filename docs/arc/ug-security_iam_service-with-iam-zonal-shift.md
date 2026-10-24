> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam-zonal-shift.html
> Downloaded: 2026-10-24

# IAM and permissions for zonal shift

This section provides additional information about how permissions work for the zonal shift feature in Amazon Application Recovery Controller (ARC), especially if you work with the feature from another AWS service, such as Elastic Load Balancing. To learn about how ARC features works with IAM and permissions in general, review the information in the overview topic, Identity and Access Management for zonal shift in ARC.

Zonal shift supports Application Load Balancers, Network Load Balancers, Amazon EC2 Auto Scaling groups, and Amazon EKS. You can use IAM condition keys to scope an IAM permission policy to these resources. The following is an example policy using a condition key with multiple resources of different types:

```
{
    "Condition": {
        "StringLike": {
            "arc-zonal-shift:ResourceIdentifier": [
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/*",
                "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/*",
                "arn:aws:eks:us-east-1:123456789012:cluster/*"
            ]
        }
    },
    "Action": [
        "arc-zonal-shift:StartZonalShift"
    ],
    "Resource": "*",
    "Effect": "Allow"
}
```

For more information, see Supported resources.

In addition to the permissions outlined in the IAM overview topic, the following applies to zonal shift for IAM and permissions: 
Make sure that you have the required permissions for working with zonal shift in ARC. For more information, see zonal shift console access and zonal shift operations access.
You do not need to add additional Elastic Load Balancing permissions with IAM to work with zonal shifts for managed load balancer resources in your account in ARC.
An AWS managed policy that provides full access for Elastic Load Balancing includes permissions for working with zonal shifts. If you use AWS managed policies for Elastic Load Balancing access, you do not need additional permissions in IAM for zonal shift to start zonal shifts for load balancers or work with in the Elastic Load Balancing console. For more information, see AWS managed policies for Elastic Load Balancing.
