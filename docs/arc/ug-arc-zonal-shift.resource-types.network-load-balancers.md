> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html
> Downloaded: 2026-10-24

# Network Load Balancers 

## Using zonal shift for Network Load Balancers 

To use Network Load Balancers with zonal shift, you must enable ARC zonal shift integration in the Network Load Balancer attributes. Network Load Balancer supports zonal shift with cross-zone enabled or cross-zone disabled configurations.  

You can choose which resources to opt-in to use zonal shift and zonal autoshift, and when you would like to fail away from an impaired Availability Zone. Both internet-facing and internal Network Load Balancers are supported.  

To enable zonal shift for your cross-zone enabled Network Load Balancer, all target groups attached to the load balancer must have cross-zone load balancing enabled, or set to `use_load_balancer_configuration`. For more information on target group cross-zone load balancing, see Cross-zone load balancing for target groups. 

You can start a zonal shift for a Network Load Balancer by using the AWS CLI, the AWS Management Console, or the Elastic Load Balancing widget. When an Application Load Balancer is the target of a Network Load Balancer, you must start the zonal shift from the Network Load Balancer. If you start the zonal shift from the Application Load Balancer, the Network Load Balancer will not stop sending traffic to the Application Load Balancer and its targets.  

**Console** To enable zonal shift on a load balancer (Console)
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. 
On the Navigation page, under Load balancing, choose Load balancers. 
Select the Network Load Balancer name. 
On the Attributes tab, choose Edit. 
Under Availability Zone routing configuration, for ARC zonal shift integration, choose Enable. 
Choose Save. 
  

**AWS CLI** To enable zonal shift on a load balancer (AWS CLI)
Enter the following command: 

```
aws elbv2 modify-load-balancer-attributes --load-balancer-arn my-nlb-arn --attributes Key=zonal_shift.config.enabled,Value=true
```
 
   

For more information about starting a zonal shift, see Starting, updating, or canceling a zonal shift. 

## How zonal shift works for Network Load Balancers 

ARC creates a health check failure for the registered Network Load Balancer so that the Network Load Balancer node in the impaired AZ is removed from the DNS when you start a zonal shift. The Network Load Balancer disables the targets in the impacted zone so that they stop receiving traffic, and Elastic Load Balancing treats these targets as disabled targets for zonal shift. Targets in the disabled state continue receiving health checks. When the targets are healthy and the zonal shift expires (or is canceled), routing to targets in the previously impaired zone resumes. 

During zonal shift on Network Load Balancers with cross-zone load balancing enabled, the zonal load balancer IP addresses are removed from DNS. Existing connections to targets in the impaired Availability Zone persist until they organically close, while new connections are no longer routed to targets in the impaired Availability Zone. 

 For more information see Zonal Shift for your Network Load Balancer in the Network Load Balancer User Guide.
