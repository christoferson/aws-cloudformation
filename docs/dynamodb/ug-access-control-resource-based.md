> Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html
> Downloaded: 2026-10-24

# Using resource-based policies for DynamoDB

DynamoDB supports resource-based policies for tables, indexes, and streams. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource.

You can attach a resource-based policy to DynamoDB resources, such as a table or a stream. In this policy, you specify permissions for Identity and Access Management (IAM) principals that can perform speciﬁc actions on these DynamoDB resources. For example, the policy attached to a table will contain permissions for access to the table and its indexes. As a result, resource-based policies can help you simplify access control for your DynamoDB tables, indexes, and streams, by defining permissions at the resource level. The maximum size of a policy you can attach to a DynamoDB resource is 20 KB.

A significant benefit of using resource-based policies is to simplify cross-account access control for providing cross-account access to IAM principals in different AWS accounts. For more information, see Resource-based policy for cross-account access.

Resource-based policies also support integrations with IAM Access Analyzer external access analyzer and Block Public Access (BPA) capabilities. IAM Access Analyzer reports cross-account access to external entities specified in resource-based policies. It also provides visibility to help you refine permissions and conform to the least privilege principle. BPA helps you prevent public access to your DynamoDB tables, indexes, and streams, and is automatically enabled in the resource-based policies creation and modification workflows.  Topics
Create a table with a resource-based policy
Attach a policy to an DynamoDB existing table
Attach a resource-based policy to a DynamoDB stream
Remove a resource-based policy from a DynamoDB table
Cross-account access with resource-based policies in DynamoDB
Blocking public access with resource-based policies in DynamoDB
DynamoDB API operations supported by resource-based policies
Authorization with IAM identity-based policies and DynamoDB resource-based policies
DynamoDB resource-based policy examples
DynamoDB resource-based policy considerations
DynamoDB resource-based policy best practices
