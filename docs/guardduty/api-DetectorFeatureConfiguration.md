<!-- Source: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfiguration.html -->
<!-- Downloaded: 2026-10-28 -->

# DetectorFeatureConfiguration

Contains information about a GuardDuty feature.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

## Contents

** ** additionalConfiguration ** **

Additional configuration for a resource.

Type: Array of [DetectorAdditionalConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorAdditionalConfiguration.html) objects

Required: No

** ** name ** **

The name of the feature.

Type: String

Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION | AI_ANALYST`

Required: No

** ** status ** **

The status of the feature.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

-

[AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectorFeatureConfiguration)
-

[AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectorFeatureConfiguration)
-

[AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectorFeatureConfiguration)
