> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html
> Downloaded: 2026-10-24

# Zonal autoshift in ARC

With zonal autoshift, you authorize AWS to shift away resource traffic for an application from an Availability Zone (AZ) during events, on your behalf, to help reduce time to recovery. AWS starts an autoshift when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers. When AWS starts an autoshift, application traffic to resources that you've configured for zonal autoshift starts shifting away from the Availability Zone.

Be aware that ARC does not inspect the health of individual resources. AWS starts an autoshift when AWS telemetry detects that there is an Availability Zone impairment that could potentially impact customers. In some cases, traffic might be shifted away for resources that are not experiencing impact.

With zonal autoshift, you also authorize AWS to shift away resource traffic for an application from an Availability Zone, on your behalf, for regular practice runs. Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application. Practice runs regularly test that your application can operate normally without one Availability Zone by starting zonal shifts that shift traffic for a resource away from an Availability Zone. Practice runs take place weekly, and provide an outcome—such as `SUCCEEDED` or `FAILED`—to help you understand if the application operates as expected.Important

Before you configure practice runs or enable zonal autoshift, we strongly recommend that you pre-scale your application resource capacity in all Availability Zones in the Region where your application resources are deployed. You should not rely on scaling on demand when an autoshift or practice run starts. Zonal autoshift, including practice runs, works independently, and does not wait for auto scaling actions to complete. Relying on auto scaling, instead of pre-scaling, can result in it taking longer for your application to recover.

If you use auto scaling to handle regular cycles of traffic, we strongly recommend that you configure the minimum capacity of your auto scaling to continue operating normally with the loss of an Availability Zone. 

If you plan to enable zonal autoshift or configure practice runs, after you pre-scale your application resource capacity, test that your application can operate normally without one Availability Zone. To test this, start a zonal shift to move traffic for a resource away from an Availability Zone.

After you enable zonal autoshift, we recommend that you verify, by starting and evaluating an on-demand practice run zonal shift, that your application can continue operating normally with traffic shifted away from an Availability Zone. Then, the regular practice runs that ARC performs help you to confirm, on an ongoing basis, that you have enough capacity for an autoshift.

To ensure that your tests with zonal shift are effective, it's important to validate that traffic drains as expected from the AZ you shift away from. For example, both Application Load Balancers and Network Load Balancers provide per AZ metrics in Amazon CloudWatch that you can use to monitor this. Depending on how long a service and clients reuse connections, traffic might continue to the AZ that you have shifted away from for longer than you expect. To learn more, see Limit the time that clients stay connected to your endpoints.

You can enable zonal autoshift, for a supported resource, in the ARC console. Or, in the Amazon EC2 console, you have the option to enable zonal autoshift for a specific load balancer resource. To learn more about enabling zonal autoshift with Elastic Load Balancing, see Zonal shift in the Elastic Load Balancing User Guide.

Autoshifts and practice run zonal shifts are temporary. With autoshifts, when the affected Availability Zone recovers, AWS stops shifting traffic for resources away from the Availability Zone. Application traffic for customers returns to all Availability Zones in the Region. With a practice run, traffic is shifted away from an Availability Zone for a single resource for about 30 minutes, and then shifted back to all Availability Zones in the Region.

You can configure Amazon EventBridge notifications to alert you about autoshifts and practice runs. For more information, see Using zonal autoshift with Amazon EventBridge.
