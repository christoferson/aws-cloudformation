> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html
> Downloaded: 2026-10-24

# Application Load Balancers 

## Using zonal shift for Application Load Balancers 

To use Application Load Balancers with zonal shift, you must enable ARC zonal shift integration in the Application Load Balancer attributes. Application Load Balancer supports zonal shift with cross-zone enabled or cross-zone disabled configurations. 

Before you enable the ARC integration and start using zonal shift, review the following information:  
You can start a zonal shift for a specific load balancer only for a single Availability Zone. You can't start a zonal shift for multiple Availability Zones.
AWS proactively removes zonal load balancer IP addresses from DNS when multiple infrastructure issues impact services. Always check current Availability Zone capacity before you start a zonal shift.
Zonal shift won't work for single-AZ target groups.
When an Application Load Balancer is a target of a Network Load Balancer, always start the zonal shift from the Network Load Balancer. If you start a zonal shift from the Application Load Balancer, the Network Load Balancer doesn't recognize the shift and continues to send traffic to the Application Load Balancer.
 

You can start a zonal shift for a load balancer in the Elastic Load Balancing console (in most AWS Regions) or in the ARC console.  

**Console** To enable zonal shift on a load balancer (Console)
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. 
On the Navigation page, under Load balancing, choose Load balancers. 
Select the Application Load Balancer name. 
On the Attributes tab, Edit. 
Under Availability Zone routing configuration, for >ARC zonal shift integration, choose Enable. 
Choose Save. 
  

**AWS CLI** To enable zonal shift on a load balancer (AWS CLI)
Enter the following command: 

```
aws elbv2 modify-load-balancer-attributes --load-balancer-arn my-alb-arn --attributes Key=zonal_shift.config.enabled,Value=true
```
 
   

For more information on starting a zonal shift, see Starting, updating, or canceling a zonal shift. 

You can use the `keepalive` option to configure how long connections continue. For more information, see  HTTP client keepalive duration in the Application Load Balancer User Guide. By default, Application Load Balancers set the HTTP client keepalive duration value to 3600 seconds, or 1 hour. We suggest that you lower the value to be inline with your recovery time goal for your application, for example, 300 seconds. When you choose an HTTP client keepalive duration time, consider that this value is a trade off between reconnecting more frequently in general, which can affect latency, and more quickly moving all clients away from an impaired AZ or Region. 

## How zonal shift works for Application Load Balancers 

When a zonal shift is started on an Application Load Balancer with cross-zone load balancing enabled, all traffic to targets is blocked in the Availability Zone that is impacted, and the zonal shift removes the zonal IP address from DNS. 

For more information, see Integrations for your Application Load Balancer in the Application Load Balancer User Guide.
