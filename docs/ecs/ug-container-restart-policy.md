> Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy.html
> Downloaded: 2026-10-20

# Restart individual containers in Amazon ECS tasks with container restart policies

You can enable a restart policy for each essential and non-essential container defined in your task definition, to overcome transient failures faster and maintain task availability. When you enable a restart policy for a container, Amazon ECS can restart the container if it exits, without needing to replace the task.

Restart policies are not enabled for containers by default. When you enable a restart policy for a container, you can specify exit codes that the container will not be restarted on. These can be exit codes that indicate success, like exit code `0`, that don't require a restart. You can also specify how long a container must run succesfully before a restart can be attempted. For more information about these parameters, see Restart policy. For an example task definition that specifies these values, see Specifying a container restart policy in an Amazon ECS task definition.

You can use the Amazon ECS task metadata endpoint or CloudWatch Container Insights to monitor the number of times a container has restarted. For more information about the task metadata endpoint, see Amazon ECS task metadata endpoint version 4 and Amazon ECS task metadata endpoint version 4 for tasks on Fargate. For more information about Container Insights metrics for Amazon ECS, see Amazon ECS Container Insights metrics in the Amazon CloudWatch User Guide.

Container restart policies are supported by tasks hosted on Fargate, Amazon EC2 instances, and external instances using Amazon ECS Anywhere. 

## Considerations 

Consider the following before enabling a restart policy for your container:  
Restart policies aren't supported for Windows containers on Fargate. 
For tasks hosted on Amazon EC2 instances, this feature requires version `1.86.0` or later of the container agent. However, we recommend using the latest container agent version. For information about how to check your agent version and update to the latest version, see Updating the Amazon ECS container agent. 
If you're using EC2 with the `bridge` network mode, the `FLUENT_HOST` environment variable in your application container can become inaccurate after a restart of the FireLens log router container (the container with the `firelensConfiguration` object in its container definition). This is because `FLUENT_HOST` is a dynamic IP address and can change after a restart. Logging directly from the application container to the `FLUENT_HOST` IP address can start failing after the address changes. For more information about `FLUENT_HOST`, see Configuring Amazon ECS logs for high throughput. 
The Amazon ECS agent handles the container restart policies. If for some unexpected reason the Amazon ECS agent fails or is no longer running, the container won't be restarted. 
 The restart attempt period defined in your policy determines the period of time (in seconds) that the container must run for before Amazon ECS restarts a container.
