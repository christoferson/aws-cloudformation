> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-globaltablewitness.html
> Downloaded: 2026-10-24

# AWS::DynamoDB::GlobalTable GlobalTableWitness

The witness Region for the MRSC global table. A MRSC global table can be configured with either three replicas, or with two replicas and one witness.

The witness must be in a different Region than the replicas and within the same Region set: 
US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon) 
EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt) 
AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka) 

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Region" : String
}

```

### YAML

```
  Region: String

```

## Properties

**`Region`** 

The name of the AWSRegion that serves as a witness for the MRSC global table. 

Required: No

Type: String

Update requires: No interruption
