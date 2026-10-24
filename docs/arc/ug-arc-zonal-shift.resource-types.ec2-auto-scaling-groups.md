> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html
> Downloaded: 2026-10-24

# Amazon EC2 Auto Scaling groups

An Amazon EC2 Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group also lets you use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies. Both maintaining the number of instances in an Auto Scaling group and automatic scaling are the core functionality of the Amazon EC2 Auto Scaling service. 

## Using zonal shift for Auto Scaling groups 

To enable zonal shift, use one of the following methods.  

**Console** To enable zonal shift on a new group (console)
Follow the instructions in Create an Auto Scaling group using a launch template and complete each step in the procedure, up to step 10. 
On the Integrate with other services page, for ARC zonal shift, select the checkbox to enable zonal shift. 
For Health check behavior, choose Ignore unhealthy or Replace unhealthy. If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift. 
Continue with the steps in Create an Auto Scaling group using a launch template. 
  

**AWS CLI** To enable zonal shift on a new group (AWS CLI) 

Add the `--availability-zone-impairment-policy` parameter to the create-auto-scaling-group command. 

The `--availability-zone-impairment-policy` parameter has two options:  
ZonalShiftEnabled – If set to `true`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can start, update, or cancel a zonal shift on the ARC console. If set to `false`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set to `false`. 
ImpairedZoneHealthCheckBehavior – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift. 
 

The following example enables zonal shift on a new Auto Scaling group named ``my-asg``. 

```
aws autoscaling create-auto-scaling-group \
  --launch-template LaunchTemplateName=my-launch-template,Version='1' \
  --auto-scaling-group-name my-asg \
  --min-size 1 \
  --max-size 10 \
  --desired-capacity 5 \
  --availability-zones us-east-1a us-east-1b us-east-1c \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": true,
      "ImpairedZoneHealthCheckBehavior": IgnoreUnhealthy       
    }' 
  
```
    

**Console** To enable zonal shift on an existing group (console)
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/, and choose Auto Scaling Groups from the navigation pane.
On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in. 
Select the checkbox next to the Auto Scaling group. 

A split pane opens up in the bottom of the page.  
On the Integrations tab, under ARC zonal shift, choose Edit. 
Select the checkbox to enable zonal shift. 
For Health check behavior, choose Ignore unhealthy or Replace unhealthy.   
If health check behavior is set to ignore unhealthy, unhealthy instances are not replaced in the Availability Zone with the active zonal shift.
If health check behavior is set to replace unhealthy, unhealthy instances are replaced in the Availability Zone with the active zonal shift.
Choose Update. 
  

**AWS CLI** To enable zonal shift on an existing group (AWS CLI) 

Add the `--availability-zone-impairment-policy` parameter to the update-auto-scaling-group command. 

The `--availability-zone-impairment-policy` parameter has two options:  
ZonalShiftEnabled – If set to `TRUE`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can start, update, or cancel a zonal shift on the ARC console. If set to `FALSE`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set it to `FALSE`. 
ImpairedZoneHealthCheckBehavior – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift. 
 

The following example enables zonal shift on the specified Auto Scaling group. 

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name my-asg \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": true,
      "ImpairedZoneHealthCheckBehavior": IgnoreUnhealthy       
    }' 
```
   

To start a zonal shift, see Starting, updating, or canceling a zonal shift. 

## How zonal shift works for Auto Scaling groups 

Suppose you have an Auto Scaling group with the following Availability Zones:   
`us-east-1a`
`us-east-1b`
`us-east-1c`
 

You notice failures in `us-east-1a` and start a zonal shift. The following behaviors occur when a zonal shift is started in `us-east-1a`.  
Scaling out – Auto Scaling launches all new capacity requests in the healthy Availability Zones (`us-east-1b` and `us-east-1c`).
Dynamic scaling – Auto Scaling blocks scaling policies from decreasing desired capacity. Auto Scaling does not block scaling policies from increasing desired capacity.
Instance refresh – Auto Scaling extends the timeout for any instance refresh process that is delayed during an active zonal shift.  
|  Impaired Availability Zone health check behavior selection |  Health check behavior |    
|  Replace unhealthy |  Instances that appear unhealthy will be replaced in all Availability Zones (`us-east-1a`, `us-east-1b`, and `us-east-1c`). |   
|  Ignore unhealthy |  Instances that appear unhealthy will be replaced in `us-east-1b` and `us-east-1c`. Instances are not replaced in the Availability Zone with the active zonal shift (`us-east-1a`). |   
|   |   |   
 

## Best practices for using zonal shift 

To maintain high availability for your applications when using zonal shift, we recommend the following best practices.  
Monitor EventBridge notifications to determine when there is an ongoing availability zone impairment event. For more information, see Automating Amazon EC2 Auto Scaling with EventBridge. 
Use scaling policies with appropriate thresholds to make sure that you have enough capacity to tolerate the loss of an availability zone. 
Set an instance maintenance policy with a minimum healthy percentage of 100. With this setting, Auto Scaling waits for a new instance to be ready to use before terminating an unhealthy instance. 
 

For prescaled customers, we also recommend the following:  
Select Ignore unhealthy as the health check behavior for the impaired availability zone because you don't need to replace the unhealthy instance during the impairment event. 
Use zonal autoshift in ARC for your Auto Scaling groups. The zonal autoshift capability in Amazon Application Recovery Controller (ARC) allows AWS to shift traffic for a resource away from an availability zone when AWS detects an impairment in an availability zone. For more information, see Zonal autoshift in ARC. 
 

For customers with cross-zone disabled load balancers, we also recommend:  
Use balanced only for your availability zone distribution. 
If you are using zonal shift on both your Auto Scaling group and your load balancers, make sure to cancel the zonal shift on your Auto Scaling group first. Then, wait until the capacity is balanced across all availability zones. before you cancel the zonal shift on the load balancer. 
Because of the possibility of imbalanced capacity when you enable zonal shift and you use a cross-zone disabled load balancer, Auto Scaling has an extra validation. If you are following the best practices, you can acknowledge this possibility by selecting the checkbox in the AWS Management Console or using the `skip-zonal-shift-validation` flag in `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, or `AttachTrafficSources`.
