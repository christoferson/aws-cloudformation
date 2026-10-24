> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/testing-zonal-autoshift-fis.html
> Downloaded: 2026-10-24

# Testing zonal autoshift with AWS FIS

You can use AWS Fault Injection Service to set up and run experiments that help you simulate real-world conditions, such as the AZ Availability: Power Interruption scenario, that will demonstrate what happens when AWS starts a zonal autoshift on your autoshift-enabled resources during a potentially widespread AZ impairment.

The start `aws:arc:start-zonal-autoshift` recovery action allows you to demonstrate how AWS will automatically shifts traffic, for zonal autoshift enabled resources, away from a potentially impaired AZ and reroute them to healthy AZs in the same AWS Region during the execution of the AZ availability scenario.

For example, you can use the AWS FIS scenario library to simulate an AZ impairment that was caused by a power interruption. In this experiment, five minutes after the AZ power interruption begins, the recovery action `aws:arc:start-zonal-autoshift` automatically shifts resource traffic away from the specified AZ. The traffic is shifted for the remaining 25 minutes of the power interruption, to demonstrate how autoshift would be triggered when there is potentially widespread AZ impairment. When the experiment completes, the traffic shift ends and traffic begins flowing to all AZs again. This process demonstrates a complete recovery from a power event that impacts an AZ.

## How experiments differ from zonal autoshift practice runs 

AWS FIS experiments differ from zonal autoshift practice runs in that, during practice runs, ARC shifts traffic for your resource away from one AZ as part of a normal process to ensure that your application can tolerate the loss of an AZ. However, during an AWS FIS experiment, AWS FIS demonstrates how an AZ impairment and an autoshift would be triggered for your autoshift-enabled resources on your behalf, and then cancels the autoshift when the impairment has been resolved.  

You cannot update an AWS FIS-initiated zonal shift while it is running. In addition, if you cancel a zonal shift outside of AWS FIS, the AWS FIS experiment ends.  

## AWS FIS expiration-based safety mechanism 

AWS FIS manages the zonal shift using the StartZonalShift, UpdateZonalShift, and CancelZonalShift API operations, with the `expiresIn` field for these requests set to 1 minute as a safety mechanism. This enables AWS FIS to quickly roll back the zonal shift if there are unexpected events, such as network outages or system issues. In the ARC console, the expiration time field will display AWS FIS-managed, and the actual expected expiration is determined by the duration specified in the zonal shift action. For more information on practice runs, see How zonal autoshift and practice runs work 

There can be no more than one applied zonal shift at a given time. That is, only one practice run zonal shift, customer-initiated zonal shift, autoshift, or AWS FIS experiment for the resource. When a second zonal shift is started, ARC follows a precedence to determine which zonal shift type is in effect for a resource. For more information on precedence for zonal shifts, see Precedence for zonal shifts.

For more information about AWS FIS recovery actions, refer to the AWS FIS recovery action in the AWS Fault Injection Service User Guide.
