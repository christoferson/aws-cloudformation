> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html
> Downloaded: 2026-10-24

# Best practices when you configure zonal autoshift

Be aware of the following best practices and considerations when you enable zonal autoshift in Amazon Application Recovery Controller (ARC).

Zonal autoshift includes two types of traffic shifts: autoshifts and practice run zonal shifts.  
With an autoshift, AWS helps reduce your time to recovery by shifting away application resource traffic from an Availability Zone during events, on your behalf. 
With practice runs, ARC starts a zonal shift on your behalf or you start a zonal shift practice run. The AWS practice run zonal shift shifts traffic away from an Availability Zone for a resource, and back again, on a weekly cadence. Practice runs help you to make sure that you have scaled up sufficient capacity for Availability Zones in a Region for your application to tolerate the loss of one Availability Zone.

There are several best practices and considerations to keep in mind with autoshifts and practice runs. Review the following topics before you enable zonal autoshift or configure practice runs for a resource.

Topics 
Limit the time that clients stay connected to your endpoints
Prescale your resource capacity and test shifting traffic
Be aware of resource types and restrictions
Specify alarms for practice runs
Evaluate outcomes for practice runs
  

**Limit the time that clients stay connected to your endpoints**  

When Amazon Application Recovery Controller (ARC) shifts traffic away from an impairment, for example, by using zonal shift or zonal autoshift, the mechanism that ARC uses to move your application traffic is a DNS update. A DNS update causes all new connections to be directed away from the impaired location. However, clients with pre-existing open connections might continue to make requests against the impaired location until the clients reconnect. To ensure a quick recovery, we recommend that you limit the amount of time clients stay connected to your endpoints.  

If you use an Application Load Balancer, you can use the `keepalive` option to configure how long connections continue. We suggest that you lower the `keepalive` value to be inline with your recovery time goal for your application, for example, 300 seconds. When you choose a `keepalive` time, consider that this value is a trade off between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away from an impaired AZ or Region. 

For more information about setting the `keepalive` option for Application Load Balancer, see the  HTTP client keepalive duration in the Application Load Balancer User Guide.  

**Prescale your resource capacity and test shifting traffic**  

When AWS shifts traffic away from one Availability Zone for a zonal shift or an autoshift, it's important that the remaining Availability Zones can service the increased request rates for your resource. This pattern is known as static stability. For more information, see the  Static stability using Availability Zones whitepaper in the Amazon Builder’s Library. 

For example, if your application requires 30 instances to serve its clients, you should provision 15 instances across three Availability Zones, for a total of 45 instances. By doing this, when AWS shifts traffic away from one Availability Zone—with an autoshift or during a practice run—AWS can still serve your application’s clients with the remaining total of 30 instances, across two Availability Zones. 

The zonal autoshift capability in ARC helps you to quickly recover from AWS events in an Availability Zone when you have an application with resources that are pre-scaled to work normally with the loss of one Availability Zone. Before you enable zonal autoshift for a resource, scale your resource capacity in all configured Availability Zones in an AWS Region. Then, start zonal shifts for the resource, to test that your application still runs normally when traffic is shifted away from an Availability Zone.  

After you test with zonal shifts, then enable zonal autoshift and configure practice runs for application resources. Run your own on-demand practice runs to help ensure that your configuration is scaled properly. Regular practice runs with zonal autoshift help you to make sure—on an ongoing basis—that your capacity is still scaled appropriately. With sufficient capacity across Availability Zones, your application can continue to serve clients, without interruption, during an autoshift. 

For more information about starting a zonal shift for a resource, see Zonal shift in ARC. 

**Be aware of resource types and restrictions** 

Zonal autoshift supports shifting traffic out of an Availability Zone for all resources that are supported by zonal shift. In a few specific resource scenarios, zonal autoshift does not shift traffic from an Availability Zone for an autoshift. 

For example, if the load balancer target groups in the Availability Zones don't have any instances, or if all of the instances are unhealthy, then the load balancer is in a fail open state. If AWS starts an autoshift for a load balancer in this scenario, an autoshift does not change which Availability Zones the load balancer uses because the load balancer is already in a fail open state. This is expected behavior. Autoshift cannot cause one Availability Zone to be unhealthy and shift traffic to the other Availability Zones in an AWS Region if all Availability Zones are failing open (unhealthy). 

To see details about supported resources, including all of the requirements and exceptions to be aware of, see Supported resources. 

**Specify alarms for practice runs**  

You must configure at least one type of alarm (an outcome alarm) for practice runs with zonal autoshift. Optionally, you can also configure a second type of alarm (blocking alarms). 

When you consider the CloudWatch alarms that you configure for practice runs for your resource, keep in mind the following:  
You're required to configure at least one outcome alarm for a practice run configuration. For outcome alarms, we recommend that you configure CloudWatch alarms to go into an `ALARM` state when metrics for the resource, or your application, indicate that shifting traffic away from the Availability Zone adversely impacts performance. For example, you can determine a threshold for request rates for your resource, and then configure an alarm to go into an `ALARM` state when the threshold is exceeded. You are responsible for configuring appropriate alarms that cause AWS to end the practice run and return a `FAILED` outcome. 
We recommend that you follow the AWS Well Architected Framework, which advises you to implement key performance indicators (KPIs) as CloudWatch alarms. If you do so, you can use these alarms to create a composite alarm to use as a safety trigger, to prevent practice runs from starting if they might cause your application to miss a KPI. When the alarm is no longer in an `ALARM` state, ARC starts practice runs the next time a practice run is scheduled for the resource.
For practice run blocking alarms, if you choose to configure one (or more), you might choose to track specific metrics that you use to indicate that you don't want an AWS practice run to start—for example, when an alarm indicates that there is an ongoing incident.
For practice run alarms, you specify the Amazon Resource Name (ARN) for each alarm, so you must first configure the alarm in Amazon CloudWatch. The CloudWatch alarms that you specify can be composite alarms, to enable you to include several metrics and checks for your application and resource that can trigger the alarm to go into an `ALARM` state. Or, you can configure separate alarms, and then specify more than one alarm of each type for your practice run configuration. For more information, see Combining alarms in the Amazon CloudWatch User Guide.
Make sure that the CloudWatch alarms that you specify for practice runs are in the same Region as the resource that you're configuring a practice run for.
 

**Evaluate outcomes for practice runs** 

ARC reports an outcome for each practice run. After a practice run, evaluate the outcome, and determine if you need to take action. For example, you might need to scale capacity or adjust the configuration for an alarm. 

The following are the possible practice run outcomes:   
SUCCEEDED: No outcome alarms entered an `ALARM` state during the practice run, and the practice run completed the full 30 minute test period.
FAILED:  At least one outcome alarm entered an `ALARM` state during the practice run.
INTERRUPTED:  The practice run ended for a reason that was not the outcome alarm entering an `ALARM` state. A practice run can be interrupted for a variety of reasons, including the following:   
Practice run was ended because AWS started an autoshift in the AWS Region or there was an alarm condition in the Region.
Practice run was ended because the practice run configuration was deleted for the resource.
Practice run was ended because a customer-initiated zonal shift was started for the resource in the Availability Zone that the practice run zonal shift was shifting traffic away from.
Practice run was ended because a CloudWatch alarm that was specified for the practice run configuration could no longer be accessed.
Practice run was ended because a blocking alarm specified for the practice run entered an `ALARM` state.
Practice run was ended for an unknown reason.
Practice run was ended because a zonal autoshift with precedence was initiated. See Precedence for zonal shifts. 
CAPACITY_CHECK_FAILED: The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.
PENDING: The practice run is active (in progress). There's no outcome to return yet.
