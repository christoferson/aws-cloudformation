<!-- Source: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html -->
<!-- Downloaded: 2026-10-28 -->

# Severity levels of GuardDuty findings

Each GuardDuty finding has an assigned severity level and value that reflects the potential risk the finding could have to your environment, as determined by our security engineers. The value of the severity can fall anywhere within the 1.0 to 10.0 range, with higher values indicating greater security risk. To help you determine a response to a potential security issue that is highlighted by a finding, GuardDuty breaks down this range into *Critical*, *High*, *Medium*, and *Low* severity levels.

A finding of a particular type may have a different severity depending on the context specific to the finding. To view a consolidated list of default severity levels for all GuardDuty finding types, see [GuardDuty active finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html#findings-table).

The following sections explain defined severity levels for the GuardDuty findings.

###### Topics

-

[Critical severity](#guardduty-finding-severity-level-critical)
-

[High severity](#guardduty-finding-severity-level-high)
-

[Medium severity](#guardduty-finding-severity-level-medium)
-

[Low severity](#guardduty-finding-severity-level-low)

## Critical severity

**Value range**: 9.0 - 10.0

**Description**: A critical severity level indicates that an attack sequence may be in progress or had recently happened. One or more AWS resources, such as IAM user sign-in credentials and Amazon S3 bucket, are potentially being compromised or may have already been compromised.

**Recommendation**: GuardDuty recommends that you prioritize triaging and remediating all critical severity findings because these issues can be a part of a ransomware attack and can escalate at any time. View details about the involved resources and start addressing the security issues. For more information, see [Remediating findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html).

## High severity

**Value range**: 7.0 - 8.9

**Description**: A High severity level indicates that the resource in question (an Amazon EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.

**Recommendation**: GuardDuty recommends that you treat any high severity finding security issue as a priority and take immediate remediation steps to prevent further unauthorized use of your resources. For example, clean up your Amazon EC2 instance or terminate it, or rotate the IAM credentials. Follow the steps in [Remediating findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html) to remediate the finding.

## Medium severity

**Value range**: 4.0 - 6.9

**Description**: A medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.

**Recommendation**: GuardDuty recommends investigating the potentially impacted resource at your earliest convenience. Remediation steps will vary by resource and finding family. An establish approach is for you to confirm that the activity is authorized and consistent with your use case. If you cannot identify the cause, or confirm the activity was authorized, you should consider the resource compromised. Follow the steps in [Remediating findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html) to remediate the finding.

Here are some things to consider when reviewing a medium level finding:

-

Check if an authorized user has installed new software that changed the behavior of a resource (for example, allowed higher than normal traffic, or enabled communication on a new port).
-

Check if an authorized user changed the control plane settings, for example, modified a security group setting.
-

Run an anti-virus scan on the implicated resource to detect unauthorized software.
-

Verify the permissions that are attached to the implicated IAM role, user, group, or set of credentials. These might have to be changed or rotated.

## Low severity

**Value range**: 1.0 - 3.9

**Description**: A low severity level indicates attempted suspicious activity that did not compromise your environment, for example, a port scan or a failed intrusion attempt.

**Recommendation**: There is no immediate recommended action, but it is worth taking a note of this information as it may indicate someone is looking for weak points in your environment.
