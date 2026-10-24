> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html
> Downloaded: 2026-10-24

# Starting, updating, or canceling a zonal shift

This section provides procedures for working with zonal shifts, including starting a zonal shift and canceling a zonal shift.

## Starting a zonal shift 

The steps in this section explain how to start a customer-initiated zonal shift on the Amazon Application Recovery Controller (ARC) console. To work with zonal shift programmatically, see the  Zonal Shift API Reference Guide. 

In addition to starting a zonal shift in ARC, you can also start a zonal shift for a load balancer in the Elastic Load Balancing console (in supported Regions). For more information, see Zonal shift in the Elastic Load Balancing User Guide. 

## To start a zonal shift
Open the ARC console at https://console.aws.amazon.com/route53recovery/home#/dashboard.  
Under Multi-AZ, choose Zonal shift. 
On the Zonal shift page, choose Start zonal shift. 
Select the Availability Zone that you want to shift traffic away from. 
Select a supported resource from the Resources table to shift traffic away for. 
For Set zonal shift expiration, choose or enter an expiration for the zonal shift. A zonal shift can set to be active initially for 1 minute or up to three days (72 hours).  

All zonal shifts are temporary. You must set an expiration, but you can update active shifts later to set a new expiration period of up to three days.  
Enter a comment. You can update the zonal shift later to edit the comment, if you like. 
Select the checkbox to acknowledge that starting a zonal shift will reduce available capacity for your application by shifting traffic away from the Availability Zone. 
Choose Start. 
 

## Updating or canceling a zonal shift 

The steps in this section explain how to update a zonal shift that you initiate, or cancel a zonal shift, on the Amazon Application Recovery Controller (ARC) console. To work with zonal shift programmatically, see the  Zonal Shift API Reference Guide. 

You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift. You can cancel a zonal shift any time before it expires. 

You can cancel zonal shifts that you initiate, or zonal shifts that AWS starts for a resource for a practice run for zonal autoshift. To learn more about practice shifts in zonal autoshift, see How zonal autoshift and practice runs work. 

## To update a zonal shift
Open the ARC console at https://console.aws.amazon.com/route53recovery/home#/dashboard.  
Under Multi-AZ, choose Zonal shift. 
Select a zonal shift that you want to update, and then choose Update zonal shift. 
For Set zonal shift expiration, optionally select or enter an expiration. 
For Comment, optionally edit the existing comment or enter a new comment. 
Choose Update. 
 

## To cancel a zonal shift
Open the ARC console at https://console.aws.amazon.com/route53recovery/home#/dashboard.  
Under Multi-AZ, choose Zonal shift. 
Select a zonal shift that you want to cancel, and then choose Cancel zonal shift. 
On the confirmation modal dialog, choose Confirm.
