> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.how-traffic-shifted.html
> Downloaded: 2026-10-24

# How traffic is shifted away

For autoshifts and for practice run zonal shifts, traffic is shifted away from an Availability Zone using the same mechanism that ARC uses for customer-initiated zonal shifts. An unhealthy health check results in Amazon Route 53 withdrawing the corresponding IP addresses for the resource from DNS, so that traffic is redirected from the Availability Zone. New connections are now routed to other Availability Zones in the AWS Region instead.

With an autoshift, when an Availability Zone recovers and AWS decides to end the autoshift, ARC reverses the health check process, requesting the Route 53 health checks to be reverted. Then, the original zonal IP addresses are restored and, if the health checks continue to be healthy, the Availability Zone is included in the application's routing again.

It's important to be aware that autoshifts are not based on health checks that monitor the underlying health of load balancers or applications. ARC uses health checks to move traffic away from Availability Zones, by requesting health checks to be set to unhealthy, and then restores health checks to normal again when it ends an autoshift or zonal shift.
