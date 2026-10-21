> Source: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_authorization_policies.html
> Downloaded: 2026-10-20

# Authorization policies in AWS Organizations

Authorization policies in AWS Organizations enable you to centrally configure and manage access for principals and resources in your member accounts. How those policies affect the organizational units (OUs) and accounts that you apply them to depends on the type of authorization policy that you apply.

There are two different types of authorization policies in AWS Organizations: service control policies (SCPs) and resource control policies (RCPs).Topics
Differences between SCPs and RCPs
Using SCPs and RCPs
Service control policies
Resource control policies
 

## Differences between SCPs and RCPs 

SCPs are principal-centric controls. SCPs create a permissions guardrail, or set limits, on the maximum permissions available to principals in your member accounts. You can use an SCP when you want to centrally enforce consistent access controls on principals in your organization. This can include specifying which services your IAM users and IAM roles can access, which resources they can access, or the conditions under which they can make requests (for example, from specific regions or networks). 

RCPs are resource-centric controls. RCPs create a permissions guardrail, or set limits, on the maximum permissions available for resources in your member accounts. You can use an RCP when you want to centrally enforce consistent access controls across resources in your organization. This can restrict access to your resources so that they can only be accessed by identities that belong to your organization, or specifying the conditions under which identities external to your organization can access your resources.  

Some controls can be applied in a similar way through SCPs and RCPs. For example, you might want to prevent your users from uploading unencrypted objects to S3 which can be written as an SCP to enforce a control on the actions that your principals can take on your S3 buckets. This control can also be written as an RCP to require encryption whenever any principal uploads objects to your S3 bucket. The second option might be preferred if your bucket allows principals outside of your organization, such as third-party vendors, to upload objects to your S3 bucket. However, some controls can only be implemented in an RCP, and some controls can only be implemented in an SCP. For more information, see General use cases for SCPs and RCPs. 

## Using SCPs and RCPs 

SCPs and RCPs are independent controls. You can choose to enable only SCPs or RCPs, or use both policy types together. By using both SCPs and RCPs, you can create a data perimeter around your identities and your resources.  

SCPs provide an ability to control which resources your identities can access. For example, you may want to allow your identities to access resources in your AWS organization. However, you may want to prevent your identities from accessing resources outside of your organization. You can enforce this control using SCPs. 

RCPs provide an ability to control which identities can access your resources. For example, you may want to allow identities in your organization to be able to access resources in your organization. However, you may want to prevent identities external to your organization from accessing your resources. You can enforce this control using RCPs. RCPs provide an ability to impact the effective permissions for principals external to your organization that are accessing your resources. SCPs can only impact the effective permissions for principals within your AWS organization.  

### General use cases for SCPs and RCPs 

The following table details general use cases for using an SCP and RCPs  
|   |  Impacts |    
|  Use case |  Policy type |  Your identities |  External identities |  Your Resources |  External resources (target of the request) |   
|  Restrict which services or actions your identities can use |  SCP |  Yes |  No |  Yes |  Yes |   
|  Restrict which resources your identities can access |  SCP |  Yes |  No |  Yes |  Yes |   
|  Enforce requirements on how your identities can access resources |  SCP |  Yes |  No |  Yes |  Yes |   
|  Restrict which identities can access your resources |  RCP |  Yes |  Yes |  Yes |  No |   
|  Protect sensitive resources in your organization |  RCP |  Yes |  Yes |  Yes |  No |   
|  Enforce requirements on how your resources can be accessed |  RCP |  Yes |  Yes |  Yes |  No |
