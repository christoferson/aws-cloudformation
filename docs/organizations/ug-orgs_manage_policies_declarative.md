> Source: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html
> Downloaded: 2026-10-20

# Declarative policies in AWS Organizations

Declarative policies enable you to centrally configure and manage AWS services and their features. How those policies affect the OUs and accounts that inherit them depends on the type of declarative policy you apply in AWS Organizations. Review the topics in this section to understand relevant terms and concepts about declarative policies.

Declarative policies allow you to centrally declare and enforce your desired configuration for a given AWS service at scale across an organization. Once attached, the configuration is always maintained when the service adds new features or APIs. Use declarative policies to prevent noncompliant actions. For example, you can block public internet access to Amazon VPC resources, or enforce encryption in transit for VPC traffic, across your organization.

The key benefits of using declarative policies are: 
Ease of use: You can enforce the baseline configuration for an AWS service with a few selections in the AWS Organizations and AWS Control Tower consoles or with a few commands using the AWS CLI & AWS SDKs. 
Set once and forget: The baseline configuration for an AWS service is always maintained, even when the service introduces new features or APIs. The baseline configuration is also maintained when new accounts are added to an organization or when new principals and resources are created. 
Transparency: The account status report allows you to review the current status of all attributes supported by declarative policies for the accounts in scope. You can also create customizable error messages, which can help administrators redirect end users to internal wiki pages or provide a descriptive message that can help end users understand why an action failed.  
 

## How declarative policies work 

Declarative policies are enforced in the service's control plane, which is an important distinction from authorization policies such as service control policies (SCPs) and resource control policies (RCPs). While authorization policies regulate access to APIs, declarative policies are applied directly at the service level to enforce durable intent. This ensures that the baseline configuration is always enforced, even when new features or APIs are introduced by the service. 

The following table helps illustrate this distinction and provides some use cases.  
|   |  Service control policies |  Resource control policies |  Declarative policies |    
|  Why? |   

To centrally define and enforce consistent access controls on principals (such as IAM users and IAM roles) at scale.   |   

To centrally define and enforce consistent access controls on resources at scale  |   

To centrally define and enforce the baseline configuration for AWS services at scale.  |   
|  How? |   

By controlling the maximum available access permissions of principals at an API level.  |   

By controlling the maximum available access permissions for resources at an API level.  |   

By enforcing the desired configuration of an AWS service without using API actions.  |   
|  Governs service-linked roles? |  No |  No |  Yes |   
|  Example policy |  Deny member accounts from leaving the organization |  Restrict access to only HTTPS connections to your resources |  Allowed Images Settings |    

After you have created and attached a declarative policy, it is applied and enforced across your organization. Declarative policies can be applied to an entire organization, organizational units (OUs), or accounts. Accounts joining an organization will automatically inherit the declarative policy in the organization. For more information, see Understanding declarative policy inheritance. 

The effective policy is the set of rules that are inherited from the organization root and OUs along with those directly attached to the account. The effective policy specifies the final set of rules that apply to the account. For more information, see Viewing effective declarative policies. 

If a declarative policy is detached, the attribute state will roll back to its previous state before the declarative policy was attached. Topics
Prerequisites and permissions
Understanding policy inheritance
Viewing effective policies
Invalid policy alerts
EC2 policies
Backup policies
Tag policies
Chat applications policies
AI services opt-out policies
Security Hub policies
Amazon Bedrock policies
Amazon Inspector policies
Upgrade rollout policies
Amazon S3 policies
AWS Shield Network Security Director policies
Amazon GuardDuty policies
