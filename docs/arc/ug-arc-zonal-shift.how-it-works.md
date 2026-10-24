> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.how-it-works.html
> Downloaded: 2026-10-24

# How a zonal shift works

When you start a zonal shift for a supported resource, traffic for the resource is moved away from the Availability Zone (AZ) that you've specified. ARC's supported resources provide integrations that mark the specified AZ as unhealthy, which results in a traffic shifting away from the impaired AZ. 

Traffic begins to shift - When you start a zonal shift in ARC, you might not see traffic move out of the Availability Zone immediately. It can take a short time for existing, in-progress connections in the Availability Zone to complete, depending on client behavior and connection reuse. DNS settings and other factors including existing connections can complete in just a few minutes, but they may take longer. For more information, see Ensuring that traffic shifts finish quickly.

Traffic shift ends - When a zonal shift expires or you cancel it, ARC takes steps to stop shifting traffic and reverses the process for starting a traffic shift. Now, the recovered AZ is recognized as available for the resource and traffic resumes flowing to the AZ.

You must set all zonal shifts to expire when you start the shifts. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time. You can also cancel a zonal shift before it expires, if you're ready to restore traffic to the Availability Zone.

When traffic does not shift away - In specific scenarios, a zonal shift does not shift traffic from the Availability Zone. For example, say you start a zonal shift for a load balancer when the load balancer target groups in the AZs don't have any instances, or if all of the instances are unhealthy. In this scenario, the load balancer is in a fail open state and starting a zonal shift does not shift away traffic.

Before you start a zonal shift for a resource, make sure that all the conditions for a successful zonal shift are met. AWS resources handle zonal shifts differently. For more information about zonal shift support, see Supported resources.
