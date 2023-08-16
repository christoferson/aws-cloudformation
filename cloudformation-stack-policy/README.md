## Cloudformation - Stack Policy

- By default, anyone with stack update permissions can update all of the resources in the stack.

- A stack policy is a JSON document that defines the update actions that can be performed on designated resources.

- To allow updates on specific resources, you specify an explicit Allow statement for those resources in your stack policy. You can define only one stack policy per stack, but, you can protect multiple resources within a single policy.

- A stack policy applies only during stack updates. It doesn't provide access controls like an AWS Identity and Access Management (IAM) policy. Use a stack policy only as a fail-safe mechanism to prevent accidental updates to specific stack resources. 


- The Principal element is required, but supports only the wild card (*)

### Syntax

```
{
  "Statement" : [
    {
      "Effect" : "Deny_or_Allow",
      "Action" : "update_actions",
      "Principal" : "*",
      "Resource" : "LogicalResourceId/resource_logical_ID",
      "Condition" : {
        "StringEquals_or_StringLike" : {
          "ResourceType" : [resource_type, ...]
        }
      }
    }
  ]
}
```

- Action Update:Modify, Update:Replace, Update:Delete, Update:* e.g. "Action" : ["Update:Replace", "Update:Delete"]
- NotAction e.g. "NotAction" : "Update:Delete"

- Resource e.g. "Resource" : ["LogicalResourceId/CriticalResource*"]
- NotResource e.g. "NotResource" : "LogicalResourceId/ProductionDatabase"


```
{
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "*"
    },
    {
      "Effect" : "Deny",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "LogicalResourceId/ProductionDatabase"
    }
  ]
}
```

```
{
  "Statement" : [
  {
    "Effect" : "Deny",
    "Principal" : "*",
    "Action" : "Update:*",
    "Resource" : "*",
    "Condition" : {
      "StringEquals" : {
        "ResourceType" : ["AWS::EC2::Instance", "AWS::RDS::DBInstance"]
      }
    }
  }
}
```

## Resources

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html