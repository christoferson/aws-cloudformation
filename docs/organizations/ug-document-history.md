> Source: https://docs.aws.amazon.com/organizations/latest/userguide/document-history.html
> Downloaded: 2026-10-20

# Document history for AWS Organizations

The following table describes major documentation updates for AWS Organizations. 
API version: 2016-11-28 
Latest documentation update: June 22, 2026 

| Change | Description | Date | 
| 

Added Amazon GuardDuty policies | 

You can use Amazon GuardDuty policies to centrally enable and manage GuardDuty configurations across your AWS Organizations. These policies help you enable protection plans and maintain consistent threat-detection coverage across multiple accounts in your organization. | 

September 25, 2026 | 
| 

Added Amazon Connect Talent to AI services opt-out policy | 

Added Amazon Connect Talent to the list of AWS services supported by the AI services opt-out policy. | 

September 15, 2026 | 
| 

Clarified Resource element requirement in SCPs | 

Clarified that each statement in an SCP must include a `Resource` or `NotResource` element. | 

June 23, 2026 | 
| 

Added AWS FinOps Agent to AI services opt-out policy | 

Added AWS FinOps Agent to the list of AWS services supported by the AI services opt-out policy. | 

June 22, 2026 | 
| 

Updated Backup policies | 

Added Amazon Redshift Serverless namespaces and Aurora DSQL clusters to the list of supported resource types for backup policies. | 

April 8, 2026 | 
| 

Added Path field to Account and OU objects | 

Account and organizational unit (OU) objects now include path information in API responses. Account APIs (such as `DescribeAccount` and `ListAccounts`) and OU APIs (such as `DescribeOrganizationalUnit`) return a path field showing where entities exist within an organization. | 

March 30, 2026 | 
| 

New services supported in RCPs | 

Added additional services supported by RCPs.  | 

January 23, 2026 | 
| 

New monitoring account states topic | 

Added guidance on using AWS Organizations to centrally monitor account states across all accounts in your organization, such as Active, Suspended, or Closed, from either the console, CLI, and SDKs.  | 

September 9, 2025 | 
| 

Added Security Hub policies | 

You can use Security Hub policies to centrally manage Security Hub configurations across your AWS Organizations. These policies help you enable features and maintain consistent security controls across multiple accounts in your organization. | 

June 17, 2025 | 
| 

Updated the AWSOrganizationsFullAccess managed policy | 

Added the `account:GetAccountInformation` action to enable access to view the account name of any account in an organization and the `account:PutAccountName` action to enable access to modify any account name in an organization. | 

April 22, 2025 | 
| 

Organizations integration with AWS User Notifications | 

You can integrate User Notifications with AWS Organizations to configure and view notifications centrally across accounts in your organization. | 

January 24, 2025 | 
| 

Organizations integration with AWS Managed Services (AMS) Self-Service Reporting (SSR) | 

You can integrate AMS SSR with AWS Organizations to enable Aggregated self-service reporting (SSR). This is an AMS feature that allows Advanced and Accelerate customers to view their existing Self-service reports aggregated at the organization level, cross-account. | 

January 21, 2025 | 
| 

Added declarative policies | 

You can use declarative policies to centrally declare and enforce desired configurations for a given AWS service at scale across an organization. Once attached, the configuration is always maintained when the service adds new features or APIs. | 

December 1, 2024 | 
| 

New AWS managed policy | 

Added the `DeclarativePoliciesEC2Report` policy to enable the functionality of the declarative-policies-ec2.amazonaws.com service-linked role. | 

November 22, 2024 | 
| 

Updated Backup policies | 

AWS Backup policies updated the `selections` policy key to include a `conditions` policy key and added a new `resources` policy key to the schema. With the new schema, you have more flexibility in resource selection for your backup policies. | 

November 14, 2024 | 
| 

Centrally manage root access for member accounts | 

You can now manage privileged root user credentials across member accounts in AWS Organizations with centralized root access. Centrally secure the root user credentials of your AWS accounts managed using AWS Organizations to remove and prevent root user credential recovery and access at scale. | 

November 14, 2024 | 
| 

Added resource control policies (RCPs) | 

You can use resource control policies (RCPs) to control the maximum available permissions for resources in an organization. | 

November 13, 2024 | 
| 

Added chat applications policies | 

You can use chat applications policies to control access to your organization's accounts from chat applications such as Slack and Microsoft Teams. | 

September 26, 2024 | 
| 

Scenario-driven content updates | 

The AWS Organizations documentation was updated to be more scenario-driven throughout the entire guide and content was reorganized to improve readability and discovery. If you have feedback on these changes, use the Provide feedback button at the bottom of a page. | 

September 4, 2024 | 
| 

New opt out from all AI services topic | 

Added documentation about how opt out from all supported AWS AI services. | 

August 16, 2024 | 
| 

Organizations now supports 10,000 accounts in an organization | 

You can now manage up to 10,000 member accounts in an organization, doubling the previous limit of 5,000 accounts. If you have a valid requirement and business need, you can request and be approved for a 10,000 account quota without service limit checks from Organizations or other integrated AWS services. | 

August 14, 2024 | 
| 

New account migration topic | 

Added documentation about how to migrate an account from one organization to another. | 

August 1, 2024 | 
| 

Updated Backup policies | 

AWS Backup policies now support Amazon Elastic Block Store (Amazon EBS) snapshot archives. For updated examples, see Updating a backup policy and Backup policy syntax and examples. | 

July 9, 2024 | 
| 

Updated the AWSOrganizationsReadOnlyAccess managed policy | 

Added the `account:GetPrimaryEmail` action to the AWSOrganizationsReadOnlyAccess policy which enables access to view the root user email address for any member account in an organization and added the `account:GetRegionOptStatus`action to enable access to view the enabled Regions for any member account in an organization. | 

June 6, 2024 | 
| 

New update root user email address topic | 

Organizations now provides the capability to centrally update the root user email address for any member account in an organization. | 

June 6, 2024 | 
| 

Updated policy statements | 

Added new `Sid` elements to the AWS Organizations managed policy statements. | 

February 6, 2024 | 
| 

New close management account topic | 

Added links to considerations and detailed steps that walk through how to close a management account. | 

February 1, 2024 | 
| 

Updated best practices | 

Added new information to the best practices section to help align with IAM best practices. | 

June 12, 2023 | 
| 

Updated the AWSOrganizationsFullAccess and AWSOrganizationsReadOnlyAccess managed policies | 

Both managed policies were updated to enable write or read access to contacts for accounts. | 

October 21, 2022 | 
| 

Updated the AWSOrganizationsFullAccess managed policy | 

The managed policy was updated to allow creating an organization by adding the permission required to create the service linked role needed by a new organization. | 

August 24, 2022 | 
| 

Organizations close account capability from the AWS Organizations console | 

Principals in the management account can close member accounts from the AWS Organizations console, and protect member accounts from accidental closure by using IAM policies. | 

March 29, 2022 | 
| 

Updated announcement to update alternate contacts with AWS Organizations console | 

Organizations now provides ability to update alternate contacts for accounts within your organization using the AWS Organizations console. Announce new capability and points to Account Management Reference for instructions.  | 

February 8, 2022 | 
| 

Organizations managed policy updates - Update to an existing policy | 

Updated the AWSOrganizationsFullAccess and AWSOrganizationsReadOnlyAccess managed policies to allow account API permissions required to update or view account alternate contacts via the AWS Organizations console.  | 

February 7, 2022 | 
| 

Organizations integration with Amazon DevOps Guru | 

You can integrate Amazon DevOps Guru with AWS Organizations to monitor application health holistically across all of your organization accounts and gain insights. | 

January 3, 2022 | 
| 

Organizations integration with Amazon Detective | 

You can integrate Amazon Detective with AWS Organizations to ensure that your Detective behavior graph provides visibility into the activity for all of your organization accounts. | 

December 16, 2021 | 
| 

Organizations integration with AWS Config now supports multi-account multi-region data aggregation. | 

You can use a delegated administrator account to aggregate resource configuration and compliance data from all of the member accounts your organization. For more information, see Multi-account multi-region data aggregationin the AWS Config Developer Guide. | 

June 16, 2021 | 
| 

Organizations integration with AWS Firewall Manager now includes support for a delegated administrator | 

You can now designate a member account in your organization to be the Firewall Manager administrator for the entire organization. This allows for better separation of permissions from the organization's management account. | 

April 30, 2021 | 
| 

Organizations backup policies now support continuous backup | 

You can use the AWS Backup continuous backups feature with your organization's backup policies. | 

March 10, 2021 | 
| 

Organizations integration with AWS CloudFormation StackSets now includes support for a delegated administrator | 

You can now designate a member account in your organization to be the CloudFormation StackSets administrator for the entire organization. This allows for better separation of permissions from the organization's management account. | 

February 18, 2021 | 
| 

Continue inviting accounts while you enable all features | 

AWS updated the process to enable all features in an organization. You can now continue to invite new accounts to join your organization while you wait for existing accounts to respond to their invitations. | 

February 3, 2021 | 
| 

Introduces version 2.0 of the AWS Organizations console | 

AWS introduced a new version of the AWS console. All of the documentation has been updated to reflect the new way of performing tasks. | 

January 21, 2021 | 
| 

Organizations now supports integration with AWS Marketplace | 

You can now enable AWS Marketplace to more easily share your software licenses across all of the accounts in your organization. | 

December 3, 2020 | 
| 

Organizations now supports integration with Amazon S3 Lens | 

Amazon S3 Lens supports both trusted access and delegated administrator with Organizations. For details, see Amazon S3 Storage Lens in the Amazon Simple Storage Service User Guide. | 

November 18, 2020 | 
| 

Cross-account backup copies | 

When you use backup policies to backup the resources in your organization, you can now store copies of your backup in other AWS accounts in the organization. | 

November 18, 2020 | 
| 

AWS Regions in China now support AWS Resource Access Manager as an Organizations trusted service | 

You can now use AWS RAM features that integrate with Organizations as a trusted service when you use Organizations and AWS RAM in China. | 

November 18, 2020 | 
| 

Organizations now supports integration with AWS Security Hub CSPM | 

You can enable Security Hub CSPM across all of the accounts in your organization, and designate one of your organization's member accounts as the delegated administrator account for Security Hub CSPM. | 

November 12, 2020 | 
| 

Renamed the master account | 

AWS Organizations changed the name of the “master account” to “management account”. This is a name change only, and there is no change in functionality. | 

October 20, 2020 | 
| 

New Best Practices section and topics | 

Added a new section for best practices for AWS Organizations. The new section includes topics that discuss best practices for the management account and member account root users and password management. | 

October 6, 2020 | 
| 

Added new best practices section and first two pages | 

There is a new section for topics that describe best practices for AWS Organizations. This update includes a topic for best practices for an organization's management account and a topic for best practices for member accounts. | 

October 2, 2020 | 
| 

Organizations backup policies now support application-consistent backups on Windows EC2 instances by using VSS (Volume Shadow Copy Service) | 

Backup policies support a new `advanced_backup_settings`" section. The first entry in this new section is an `ec2` setting called `WindowsVSS` that you can enable or disable. For details, see Creating a VSS-Enabled Windows Backup in the AWS Backup Developer Guide. | 

September 24, 2020 | 
| 

Organizations supports tag-on-create and tag-based access control | 

You can add tags to Organizations resources when you create them. You can use tag policies to standardize tag usage on Organizations resources. You can use IAM policies to restrict access to only resources that have specified tag keys and values. | 

September 15, 2020 | 
| 

Added AWS Health as a trusted service | 

You can aggregate AWS Health events across accounts in your organization. | 

August 4, 2020 | 
| 

Artificial Intelligence (AI) services opt-out policies | 

You can use AI services opt-out policies to control whether AWS AI services may store and use customer content processed by those services (AI content) for the development and continuous improvement of AWS AI services and technologies. | 

July 8, 2020 | 
| 

Added backup policies and integration with AWS Backup | 

You can use backup policies to create and enforce backup policies across all of the accounts in your organization. | 

June 24, 2020 | 
| 

Support delegated administration for IAM Access Analyzer | 

Enables you to delegate administrative access for Access Analyzer in your organization to a designated member account. | 

March 30, 2020 | 
| 

Integration with CloudFormation StackSets | 

You can create a service-managed stack set to deploy stack instances to accounts managed by AWS Organizations. | 

February 11, 2020 | 
| 

Integration with Compute Optimizer | 

Compute Optimizer was added as a service that can work with accounts in your organization. | 

February 4, 2020 | 
| 

Tag policies | 

You can use tag policies to help standardize tags across resources in your organization's accounts. | 

November 26, 2019 | 
| 

Integration with Systems Manager | 

You can synchronize operations data across all AWS accounts in your organization in Systems Manager Explorer. | 

November 26, 2019 | 
| 

aws:PrincipalOrgPaths | 

New global condition key checks the AWS Organizations path for the IAM user, IAM role, or AWS account root user who is making the request.  | 

November 20, 2019 | 
| 

Integration with AWS Config rules | 

You can use AWS Config API operations to manage AWS Config rules across all AWS accounts in your organization. | 

July 8, 2019 | 
| 

New service for trusted access | 

Service Quotas added as a service that can work with the accounts in your organization. | 

June 24, 2019 | 
| 

Integration with AWS Control Tower | 

AWS Control Tower added as a service that can work with the accounts in your organization. | 

June 24, 2019 | 
| 

Integration with AWS Identity and Access Management | 

IAM provides service last accessed data for your organization's entities (the organization root, OUs, and accounts). You can use this data to restrict access to only the AWS services that you need. | 

June 20, 2019 | 
| 

Tagging accounts | 

You can tag and untag accounts in your organization and view tags on an account in your organization. | 

June 6, 2019 | 
| 

Resources, conditions, and the `NotAction` element in service control policies (SCPs) | 

You can now specify resources, conditions, and the `NotAction` element in SCPs to deny access across accounts in your organization or organizational unit (OU).  | 

March 25, 2019 | 
| 

New services for trusted access | 

AWS License Manager and Service Catalog added as services that can work with the accounts in your organization.  | 

December 21, 2018 | 
| 

New services for trusted access | 

AWS CloudTrail and AWS RAM added as services that can work with the accounts in your organization. | 

December 4, 2018 | 
| 

New service for trusted access | 

Directory Service added as a service that can work with the accounts in your organization. | 

September 25, 2018 | 
| 

Email address verification | 

You must verify that you own the email address that is associated with the management account before you can invite existing accounts to your organization. | 

September 20, 2018 | 
| 

CreateAccount notifications | 

`CreateAccount` notifications are published to the management account's CloudTrail logs. | 

June 28, 2018 | 
| 

New service for trusted access | 

AWS Artifact added as a service that can work with the accounts in your organization. | 

June 20, 2018 | 
| 

New services for trusted access | 

AWS Config and AWS Firewall Manager added as services that can work with the accounts in your organization. | 

April 18, 2018 | 
| 

Trusted service access | 

You can now enable or disable access for select AWS services to work in the accounts in your organization. IAM Identity Center is the initial supported trusted service. | 

March 29, 2018 | 
| 

Account removal is now self-service | 

You can now remove accounts that were created from within AWS Organizations without contacting AWS Support. | 

December 19, 2017 | 
| 

Added support for new service AWS IAM Identity Center | 

AWS Organizations now supports integration with AWS IAM Identity Center (IAM Identity Center). | 

December 7, 2017 | 
| 

AWS added a service-linked role to all organization accounts | 

A service-linked role named `AWSServiceRoleForOrganizations` is added to all accounts in an organization to enable integration between AWS Organizations and other AWS services. | 

October 11, 2017 | 
| 

You can now remove created accounts | 

Customers can now remove created accounts from their organization, with help from AWS Support. | 

June 15, 2017 | 
| 

Service launch | 

Initial version of the AWS Organizations documentation that accompanied the launch of the new service. | 

February 17, 2017 |
