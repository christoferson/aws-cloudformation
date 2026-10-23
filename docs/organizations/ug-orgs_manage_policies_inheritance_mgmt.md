> Source: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html
> Downloaded: 2026-10-23

# Understanding declarative policy inheritanceImportant

The information in this section does not apply to authorization policies: service control policies (SCPs) and resource control policies (RCPs). For more information about how SCPs and RCPs work in an AWS Organizations hierarchy, see SCP evaluation and RCP evaluation.

You can attach declarative policies to organization entities (organization root, organizational unit (OU), or account) in your organization: 
When you attach a declarative policy to the organization root, all OUs and accounts in the organization inherit that policy.  
When you attach a declarative policy to a specific OU, accounts that are directly under that OU or any child OU inherit the policy. 
When you attach a declarative policy to a specific account, it affects only that account.  

Because you can attach declarative policies to multiple levels in the organization, accounts can inherit multiple policies.

This following topics explain how parent policies and child policies are processed into the effective policy for an account. Topics
Terminology
Declarative policy types
Inheritance operators
Inheritance examples
