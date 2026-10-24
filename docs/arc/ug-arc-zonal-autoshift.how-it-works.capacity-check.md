> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html
> Downloaded: 2026-10-24

# Capacity checks for practice runs

When a practice run starts, to temporarily move traffic away from an Availability Zone, ARC runs a check to verify that you have enough capacity in other Availability Zones to safely move traffic away from the AZ. If there isn't sufficient capacity available, the traffic shift for the practice run is not started and the practice run ends. 

In addition, ARC runs a capacity check for load balancer resources when a zonal autoshift completes, before ARC ends the traffic shift started by the autoshift. If the capacity check fails when the autoshift ends, traffic is not shifted back to the Availability Zone that it was moved away from.

Checks for balanced capacity are only completed for load balancers and Auto Scaling groups.

For a load balancer resource, capacity checks validate that healthy hosts associated with the load balancer are distributed across Availability Zones. Specifically, capacity checks make sure that the number of healthy hosts across all Availability Zones where the resource is registered are balanced. For capacity checks, balanced means that the healthy capacity for each Availability Zone is in parity with the other zones, within a small variance.

Note that capacity checks are not applied to load balancers with target groups of type Lambda nor to load balancers with target groups of type Application Load Balancer, because those targets are not configured zonally.

Capacity checks are also completed for Auto Scaling groups. For an Auto Scaling group, capacity checks validate that the total healthy zonal capacity of an Auto Scaling group–that is, the number of total healthy hosts across all the Availability Zones–meet the desired capacity set for that Auto Scaling group. 

When a capacity check fails

When a capacity check finds that available capacity isn't balanced for a resource, the outcome for the practice run is `CAPACITY_CHECK_FAILED`. To learn more about why a capacity check has failed, see the comment field for the `ZonalShiftSummary`. To find the comment field for your practice run zonal shift, do the following: 
Using the AWS CLI, list the zonal shifts for the resource that you specified in the practice run using the ListZonalShifts API operation.  

FOr example, to return the zonal shifts, you can run a command similar to the following: 

```
aws arc-zonal-shift start-practice-run 
    --resource-identifier="arn:aws:elasticloadbalancing:Region:111122223333:ExampleALB123456890"

```
Review the array of `ZonalShiftSummary` objects returned to find the zonal shift for the practice run that failed due to capacity checks.
For the applicable zonal shift, review the information in the `Comment` field.
