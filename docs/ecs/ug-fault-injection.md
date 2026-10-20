> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection.html
> Downloaded: 2026-10-20

# Use fault injection with your Amazon ECS and Fargate workloads

Customers can utilize fault injection with Amazon ECS on both Amazon EC2 and Fargate to test how their application responds to certain impairment scenarios. These tests provide information you can use to optimize your application's performance and resiliency.

When fault injection is enabled, the Amazon ECS container agent allows tasks access to new fault injection endpoints. You need to opt-in in order to use fault injection by setting the `enableFaultInjection` task definition parameter value to `true`. The default value is `false`. 

```
{
    ...
   "enableFaultInjection": true
}
```
Note

Fault injection only works with tasks using the `awsvpc` or `host` network modes.

Fault injection isn't available on Windows.

For information on how to enable fault injection in the AWS Management Console, see Creating an Amazon ECS task definition using the console.

You'll need to enable the feature for testing in the AWS Fault Injection Service. For more information, see Use the AWS FIS aws:ecs:task actions.Note

If you don't use thenew Amazon ECS optimized AMIs, or have a custom AMI, install the following dependencies: 
`tc` 
`sch_netem` kernel module
