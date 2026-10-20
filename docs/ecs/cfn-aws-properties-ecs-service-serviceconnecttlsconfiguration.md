> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttlsconfiguration.html
> Downloaded: 2026-10-20

# AWS::ECS::Service ServiceConnectTlsConfiguration

The key that encrypts and decrypts your resources for Service Connect TLS.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "IssuerCertificateAuthority" : ServiceConnectTlsCertificateAuthority,
  "KmsKey" : String,
  "RoleArn" : String
}

```

### YAML

```
  IssuerCertificateAuthority: 
    ServiceConnectTlsCertificateAuthority
  KmsKey: String
  RoleArn: String

```

## Properties

**`IssuerCertificateAuthority`** 

The signer certificate authority. 

Required: Yes

Type: ServiceConnectTlsCertificateAuthority

Update requires: No interruption

**`KmsKey`** 

The AWS Key Management Service key. 

Required: No

Type: String

Update requires: No interruption

**`RoleArn`** 

The Amazon Resource Name (ARN) of the IAM role that's associated with the Service Connect TLS. 

Required: No

Type: String

Update requires: No interruption
