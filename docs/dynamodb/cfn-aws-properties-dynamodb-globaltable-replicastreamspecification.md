> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicastreamspecification.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable ReplicaStreamSpecification

Represents the DynamoDB Streams configuration for a global table replica.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "ResourcePolicy" : ResourcePolicy,
  "Tags" : [ Tag, ... ]
}

```

### YAML

```
  ResourcePolicy: 
    ResourcePolicy
  Tags: 
    - Tag

```

## Properties

**`ResourcePolicy`** 

A resource-based policy document that contains the permissions for the specified stream of a DynamoDB global table replica. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource. 

In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see Using resource-based policies for DynamoDB and Resource-based policy examples. 

You can update the `ResourcePolicy` property if you've specified more than one table using the AWS::DynamoDB::GlobalTable resource. 

Required: No

Type: ResourcePolicy

Update requires: No interruption

**`Tags`** 

Specifies the tags to apply to the DynamoDB stream for this global table replica. Stream tags are independent of table and replica tags. 

For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide. 

Required: No

Type: Array of Tag

Update requires: No interruption
