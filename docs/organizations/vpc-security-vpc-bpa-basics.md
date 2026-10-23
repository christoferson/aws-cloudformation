> Source: https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html
> Downloaded: 2026-10-23

# VPC BPA basics

This section covers important details about VPC BPA, including which services support it and how you can work with it.Contents
Regional availability
AWS service impact and support
VPC BPA limitations
Control access to VPC BPA with an IAM policy
Enable VPC BPA bidirectional mode for your account
Change VPC BPA mode to ingress-only
Create and delete exclusions
Enable VPC BPA at the Organization level
 

## Regional availability 

VPC BPA is available in all commercial AWS Regions including GovCloud and China Regions. 

In this guide, you'll also find information about using Network Access Analyzer and Reachability Analyzer with VPC BPA. Note that Network Access Analyzer and Reachability Analyzer are not available in all commercial Regions. For information about the regional availability of Network Access Analyzer and Reachability Analyzer, see Limitations in the Network Access Analyzer Guide and Considerations in the Reachability Analyzer Guide. 

## AWS service impact and support 

The following resources and services support VPC BPA and traffic to these services and resources is impacted by VPC BPA:  
Internet gateway: All inbound and outbound traffic is blocked.
Egress-only internet gateway: All outbound traffic is blocked. Egress-only internet gateways do not allow inbound traffic.
Gateway Load Balancer (GWLB): All inbound and outbound traffic is blocked unless the subnet containing GWLB endpoints is excluded. 
NAT gateway: All inbound and outbound traffic is blocked. NAT gateways require an internet gateway for internet connectivity.
Internet-facing Network Load Balancer: All inbound and outbound traffic is blocked. Internet-facing Network Load Balancers require an internet gateway for internet connectivity.
Internet-facing Application Load Balancer: All inbound and outbound traffic is blocked. Internet-facing Application Load Balancers require an internet gateway for internet connectivity.
Amazon CloudFront VPC Origins: All inbound and outbound traffic is blocked. 
Direct Connect: All inbound and outbound traffic that uses public virtual interfaces (public IPv4 or global unicast IPv6 addresses) is blocked. This traffic uses the internet gateway (or egress-only internet-gateway) for connectivity.  
AWS Global Accelerator: Inbound traffic to VPCs is blocked, whether or not the target is otherwise accessible from the internet. 
AWS Network Firewall: All inbound and outbound traffic is blocked unless the subnet containing firewall endpoints is excluded. 
AWS Wavelength carrier gateway: All inbound and outbound traffic is blocked.
 

Traffic related to private connectivity, such as traffic for the following services and resources, is not blocked or impacted by VPC BPA:  
AWS Client VPN
AWS CloudWAN
AWS Outposts local gateway 
AWS Site-to-Site VPN 
Transit gateway 
AWS Verified Access 

 
 Important 
If you route incoming and outgoing traffic through an appliance (such as a third-party security or monitoring tool) that runs on an EC2 instance in a subnet using VPC Ingress Routing, you must exclude the workload subnet from VPC Block Public Access. The workload subnet is the subnet that contains the instances whose traffic is routed through the appliance. The subnet containing the appliance does not need to be excluded.
Traffic sent privately from resources in your VPC to other services running in your VPC, such as the Route 53 Resolver, is allowed even when VPC BPA is turned on because it does not pass through an internet gateway in your VPC. It is possible that these services may make requests to resources outside of the VPC on your behalf, for example, to resolve a DNS query, and may expose information about the activity of resources within your VPC if not mitigated through other security controls.
If you have an internet-facing load balancer and you create a VPC BPA exclusion for only one of its subnets, the load balancer can still receive public traffic in the excluded subnet and route it privately to targets in subnets that are not excluded. To ensure VPC BPA fully blocks public access to your targets, make sure none of the load balancer subnets are excluded.
 

## VPC BPA limitations 

VPC BPA ingress-only mode is not supported in Local Zones (LZs) where NAT gateways and egress-only internet gateways are not allowed. 

## Control access to VPC BPA with an IAM policy 

For examples of IAM policies that allow/deny access to the VPC BPA feature, see Block public access to VPCs and subnets. 

## Enable VPC BPA bidirectional mode for your account 

VPC BPA bidirectional mode blocks all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets). For more information about exclusions, see Create and delete exclusions. Important

We strongly recommend that you thoroughly review the workloads that require Internet access before enabling VPC BPA in your production accounts. Note 
To enable VPC BPA on the VPCs and subnets in your account, you must own the VPCs and subnets. 
If you are currently sharing VPC subnets with other accounts, the VPC BPA mode enforced by the subnet owner applies to participant traffic as well, but participants can't control the VPC BPA settings that impact the shared subnet.
  

**AWS Management Console** 
Open the Amazon VPC console at https://console.aws.amazon.com/vpc/. 
On the left navigation pane, choose Settings. 
Choose Edit public access settings. 
Choose Turn on block public access and Bidirectional, then choose Save changes. 
Wait for the Status to change to On. It may take a few minutes for VPC BPA settings to take effect and the status to be updated. 
 

VPC BPA Bidirectional mode is now on.  

**AWS CLI** 
Turn on VPC BPA: 

```
aws ec2 --region us-east-2 modify-vpc-block-public-access-options --internet-gateway-block-mode block-bidirectional
```
 

It may take a few minutes for VPC BPA settings to take effect and the status to be updated. 
View the status of VPC BPA: 

```
aws ec2 --region us-east-2 describe-vpc-block-public-access-options
```
 
   

## Change VPC BPA mode to ingress-only 

VPC BPA ingress-only mode blocks all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.  

**AWS Management Console** 
Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
On the left navigation pane, choose Settings. 
Choose Edit public access settings. 
Change the direction to Ingress-only. 
Save the changes and wait for the status to be updated. It may take a few minutes for VPC BPA settings to take effect and the status to be updated. 
  

**AWS CLI** 
Modify the VPC BPA block direction: 

```
aws ec2 --region us-east-2 modify-vpc-block-public-access-options --internet-gateway-block-mode block-ingress
```
 

It may take a few minutes for VPC BPA settings to take effect and the status to be updated. 
View the status of VPC BPA: 

```
aws ec2 --region us-east-2 describe-vpc-block-public-access-options
```
 
   

## Create and delete exclusions 

A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account's VPC BPA mode and will allow bidirectional or egress-only access. You can create VPC BPA exclusions for VPCs and subnets even when VPC BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. An exclusion for a VPC automatically applies to all subnets in the VPC. 

You can create a maximum of 50 exclusions. For information about requesting a limit increase, see VPC BPA exclusions per account in Amazon VPC quotas.  

**AWS Management Console** 
Open the Amazon VPC console at https://console.aws.amazon.com/vpc/. 
On the left navigation pane, choose Settings. 
In the Block public access tab, under Exclusions, do one of the following:  
To delete an exclusion, select the exclusion and then choose Actions > Delete exclusions.
To create an exclusion, choose Create exclusions and continue with the next steps.
Choose a block direction:   
Bidirectional: Allows all internet traffic to and from the excluded VPCs and subnets. 
Egress-only: Allows outbound internet traffic from the excluded VPCs and subnets. Blocks inbound internet traffic to the excluded VPCs and subnets. This setting applies when VPC BPA is set to Bidirectional. 
Choose a VPC or subnet.
Choose Create exclusions. 
Wait for the Exclusion status to change to Active. You may need to refresh the exclusion table to see the change. 
 

The exclusion has been created.  

**AWS CLI** 
Modify the exclusion allow direction: 

```
aws ec2 --region us-east-2 create-vpc-block-public-access-exclusion --subnet-id subnet-id --internet-gateway-exclusion-mode allow-bidirectional
```
It can take time for the exclusion status to update. To view the status of the exclusion: 

```
aws ec2 --region us-east-2 describe-vpc-block-public-access-exclusions --exclusion-ids exclusion-id
```
 
   

## Enable VPC BPA at the Organization level 

If you are using AWS Organizations to manage accounts in your organization, you can use an AWS Organizations declarative policy to enforce VPC BPA on the accounts in the organization. For more information about the VPC BPA declarative policy, see Supported declarative policies  in the AWS Organizations User Guide. Note 
You can use the VPC BPA declarative policy to configure if exclusions are allowed, but you cannot create exclusions with the policy. To create exclusions, you still have to create them in the account that owns the VPC. For more information about creating VPC BPA exclusions, see Create and delete exclusions.
If the VPC BPA declarative policy is enabled, in Block public access settings, you'll see Managed by Declarative Policy and you won't be able to modify VPC BPA settings at the account level.
