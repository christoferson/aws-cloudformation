<!-- Source: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorAdditionalConfiguration.html -->
<!-- Downloaded: 2026-10-28 -->

# DetectorAdditionalConfiguration

Information about the additional configuration for a feature in your GuardDuty account.

## Contents

** ** name ** **

Name of the additional configuration.

Type: String

Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT | RDS_DATA_RISK`

Required: No

** ** status ** **

Status of the additional configuration.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

-

[AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectorAdditionalConfiguration)
-

[AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectorAdditionalConfiguration)
-

[AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectorAdditionalConfiguration)
