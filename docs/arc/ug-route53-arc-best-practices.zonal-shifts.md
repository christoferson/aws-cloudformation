> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.zonal-shifts.html
> Downloaded: 2026-10-24

# Best practices for zonal shifts in ARC

We recommend the following best practices for using zonal shifts for multi-AZ recovery in ARC. 

Topics 
Capacity planning and pre-scaling
Limit the time that clients stay connected to your endpoints
Test starting zonal shifts, in advance
Ensure that all Availability Zones are healthy and taking traffic
Use data plane API operations for disaster recovery
Move traffic with a zonal shift only temporarily
  

**Capacity planning and pre-scaling** 

Ensure that you have planned for, and either pre-scaled or can auto-scale, sufficient capacity to accommodate the extra load imposed on Availability Zones when you start a zonal shift. With a recovery-oriented architecture, a typical recommendation is to pre-scale compute capacity to include enough headroom to serve your peak traffic when one of your (typically) three replicas is offline. 

When you start a zonal shift for a supported resource and traffic is shifted away from an AZ, the capacity that your application was using to service requests is removed. You must ensure that you have planned for a shift of traffic away from an AZ and can continue to service requests in the remaining AZs.   

**Limit the time that clients stay connected to your endpoints**  

When Amazon Application Recovery Controller (ARC) shifts traffic away from an impairment, for example, by using zonal shift or zonal autoshift, the mechanism that ARC uses to move your application traffic is a DNS update. A DNS update causes all new connections to be directed away from the impaired location. 

However, clients with pre-existing open connections might continue to make requests against the impaired location until the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients stay connected to your endpoints.   

**Test starting zonal shifts, in advance** 

Regularly test moving traffic away from Availability Zones for your application by starting zonal shifts. Plan for and execute starting zonal shifts, preferably in both test and production environments, as part of regular failover testing for recovering your applications in the event of a disaster. Regular testing is a critical part of ensuring that you're ready for and have the confidence to mitigate issues when an operational event occurs.  

**Ensure that all Availability Zones are healthy and taking traffic** 

Zonal shifts work by marking a resource, that is, an application replica, as unhealthy in an Availability Zone. This means that it's critical to ensure that the resources in your applications are generally healthy and actively taking traffic in the Availability Zones in a Region. We recommend that you have dashboards to track this, including, for example, Elastic Load Balancing metrics for unhealthy targets and bytesProcessed per Availability Zone.  

Consider monitoring the health of your resources from a second, adjacent Region. Advantages of this approach are that it can be more representative of your end users' experience, and it also reduces the risk of both your application and your monitoring being impacted by the same disaster at the same time.  

**Use data plane API operations for disaster recovery** 

For starting a zonal shift when you need to recover an application quickly, with few dependencies, we recommend using the AWS Command Line Interface or API with zonal shift actions, with pre-stored credentials, if possible. You can also start zonal shifts in the AWS Management Console, for ease of use. But when fast, reliable recovery is critical, data plane operations are a better choice. For more information, see  Zonal Shift API Reference Guide.  

**Move traffic with a zonal shift only temporarily** 

A zonal shift moves traffic away from an Availability Zone on a temporary basis, to mitigate an impairment. You should restore the resource for the application to service as soon as you've taken action to correct a problem. This ensures that your overall application is restored to its original fully redundant, resilient state.
