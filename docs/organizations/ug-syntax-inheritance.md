> Source: https://docs.aws.amazon.com/organizations/latest/userguide/syntax-inheritance.html
> Downloaded: 2026-10-23

# Policy syntax and inheritance for declarative policy types

Exactly how policies affect the OUs and accounts that inherit them depends on the type of declarative policy you choose. Declarative policy types include: 
EC2 policies 
Backup policies 
Tag policies 
Chat applications policies 
AI services opt-out policies 
Security Hub policies 
Bedrock policies 
Inspector policies 
Upgrade rollout policies 
S3 policies 
AWS Shield Network Security Director policies 
Amazon GuardDuty policies 

The syntax for declarative policy types includes Inheritance operators, which enable you to specify with fine granularity what elements from the parent policies are applied and what elements can be overridden or modified when inherited by child OUs and accounts.

The effective policy is the set of rules that are inherited from the organization root and OUs along with those directly attached to the account. The effective policy specifies the final set of rules that apply to the account. You can view the effective policy for an account that includes the effect of all of the inheritance operators in the policies applied. For more information, see Viewing effective declarative policies.
