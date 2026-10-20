> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-tag.html
> Downloaded: 2026-10-20

# AWS::ECS::Service Tag

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags: 
Maximum number of tags per resource - 50 
For each resource, each tag key must be unique, and each tag key can have only one value. 
Maximum key length - 128 Unicode characters in UTF-8 
Maximum value length - 256 Unicode characters in UTF-8 
If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @. 
Tag keys and values are case-sensitive. 
Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit. 

In order to tag a service that has the following ARN format, you need to migrate the service to the long ARN. You must use the API, CLI or console to migrate the service ARN. For more information, see Migrate an Amazon ECS short service ARN to a long ARN in the Amazon Elastic Container Service Developer Guide.

 `arn:aws:ecs:region:aws_account_id:service/service-name` 

After the migration is complete, the following are true: 
 The service ARN is: `arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name` 
You can use CloudFormation to tag the service as you would a service with a long ARN format. 
When the `PhysicalResourceId` in the CloudFormation stack represents a service, the value does not change and will be the short service ARN.  

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Key" : String,
  "Value" : String
}

```

### YAML

```
  Key: String
  Value: String

```

## Properties

**`Key`** 

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values. 

Required: No

Type: String

Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Minimum: `1`

Maximum: `128`

Update requires: No interruption

**`Value`** 

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key). 

Required: No

Type: String

Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Minimum: `0`

Maximum: `256`

Update requires: No interruption

## See also 
 Associate an Application Load Balancer with a service  
 Migrate an Amazon ECS short service ARN to a long ARN
