## SES Cloudformation Templates

### SES - Configuration Set

[ses-configuration-set](ses-configuration-set.yaml)

### SES - Identity - Email

Provision and SES Identity (Email)

[ses-identity-email](ses-identity-email.yaml)

### SES - Identity - Domain

Provision and SES Identity (Domain). DKIM and MailFrom Enabled.

[ses-identity-domain](ses-identity-domain.yaml)

### Errors

```
Error: Could not publish message to SNS topic <arn:aws:sns:xxx>. (Service: SesV2, Status Code: 400, Request ID: zzz)
Cause: SNS topic has encryption enabled but SES has no permission for the KMS key
```

### Links

- [cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SES.html)