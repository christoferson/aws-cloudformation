## SES Cloudformation Templates

### SES - Configuration Set

Provision a Configuration Set plus SNS Event Destination.

[ses-configuration-set](ses-configuration-set.yaml)

### SES - Identity - Email

Provision and SES Identity (Email). 
When you verify an email address, SES sends an email to the address. 
Your email address is verified as soon as you follow the link in the verification email.

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

### SES SMTP Credentials

User is the IAM Access Key. Password is derived/calculated from the IAM Secret Key.
Make sure the IAM User have the required permissions to send emails.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ses:SendRawEmail",
            "Resource": "*"
        }
    ]
}
```

- [AWS Documentation](https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html#smtp-credentials-console)
- [Java Code to derive SMTP Password from IAM Secret Key](smtp/AwsSesSmtpPasswordCalculator.java)


