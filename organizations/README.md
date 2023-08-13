
## Organizations Cloudformation Templates

- Create, delete, or update an organizational unit (OU). An OU is a container for accounts that allows you to organize your accounts to apply policies according to your needs.

- Create accounts in your organization, add tags, and attach them to OUs.

- Add or remove a tag on an OU.

- Create, delete, or update a service control policy (SCP), backup policy, tag policy and artificial intelligence (AI) services opt-out policy.

- Add or remove a tag on an SCP, backup policy, tag policy, and AI services opt-out policy.

- Attach or detach an SCP, backup policy, tag policy, and AI services opt-out policy to a target (root, OU, or account).

## Documentation

- [AWS::Organizations::Account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html)

- [AWS::Organizations::OrganizationalUnit](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html)

- [AWS::Organizations::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html)

## Points to Note

- Need the tag policy and service control policy types enabled in your management account

- AWS Organizations supports the creation of a single account at a time. If you include multiple accounts in a single CloudFormation template, you should use the DependsOn attribute so that your accounts are created sequentially.

- Before you can create a policy of a given type, you must first enable that policy type in your organization.

- The number of levels deep that you can nest OUs depends on the policy types that you have enabled for the root. For SCPs, the limit is five.

- To modify the AccountName, Email, and RoleName for the account resource parameters, you must sign in to the AWS Management Console as the AWS account root user.

----------------------------------------------------------------------------------------------------------------

### Organization - Organization Unit

Provision OU Infrastructure and Security

[organizations-unit](organizations-unit.yaml)

------------------------------------------------------------------------------------------------------

## Links

- https://aws.amazon.com/jp/blogs/security/deploy-aws-organizations-resources-by-using-cloudformation/

- https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html

- https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreatePolicy.html

- https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html

- [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)

- [Operational Excellence Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)

## Errors

##### Error-1

- Properties validation failed for resource ServiceControlPolicyPreventLeavingOrganization with message: #/TargetIds: expected type: JSONArray, found: String

##### Error-2

- 	Resource handler returned message: "The provided policy document does not meet the requirements of the specified policy type.

##### Error-3

- This operation can be performed only for enabled policy types.
- Need to enable Organization Policy e.g. SCP

##### Error-4

- A policy with the specified name and type already exists. 

## Notes

Control Tower
- Guardrails
- Preventive
  - Disallow creation of access keys for the root user
- Detective 
  - AWS Config (Detect whether MFS for root is enabled)
  
 - Guardrail Levels
  - Mandatory (Disable public read access to the log archive account)
  - Strongly recommended (encrypt ebs volumes attached to ec2 instances)
- Elective (Delete bucket objects without MFA)
  