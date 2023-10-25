## Service Catalog Cloudformation Templates

[schema](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalog.html)

### Concept

#### Products
A product is an IT service that you want to make available for deployment on AWS. 
A product consists of one or more AWS resources, such as EC2 instances, storage volumes, databases, 
monitoring configurations, and networking components, or packaged AWS Marketplace products.

#### Portfolios
A portfolio is a collection of products that contains configuration information. Portfolios help manage who can use specific products and how they can use them. With Service Catalog, you can create a customized portfolio for each type of user in your organization and selectively grant access to the appropriate portfolio. 

#### Versioning
Service Catalog allows you to manage multiple versions of the products in your catalog. This approach allows you to add new versions of templates and associated resources based on software updates or configuration changes.

#### Permissions
Granting a user access to a portfolio enables that user to browse the portfolio and launch the products in it. You apply AWS Identity and Access Management (IAM) permissions to control who can view and modify your catalog. IAM permissions can be assigned to IAM users, groups, and roles.

#### Constraints
Constraints control the ways that you can deploy specific AWS resources for a product. You can use them to apply limits to products for governance or cost control. There are different types of AWS Service Catalog constraints: launch constraints, notification constraints, and template constraints.

With launch constraints, you specify a role for a product in a portfolio. Use this role to provision the resources at launch, so you can restrict user permissions without impacting users' ability to provision products from the catalog.

Notification constraints enable you to get notifications about stack events using an Amazon SNS topic.

Template constraints restrict the configuration parameters that are available for the user when launching the product (for example, EC2 instance types or IP address ranges). With template constraints, you reuse generic AWS CloudFormation templates for products and apply restrictions to the templates on a per-product or per-portfolio basis.


------


### Templates

#### Portfolio

[service-catalog-portfolio](service-catalog-portfolio.yaml)


#### Product - Cloudformation

Provision Product using Cloudformation Provider and associate with Portfolio.

- Product consists of AWS::EC2::Instance and Security Group

- Includes LaunchTemplateConstraint that restraints the instance type to ["t2.micro", "t2.small"]

- Includes LaunchRoleConstraint that restraints the role

[service-catalog-product-cf](service-catalog-product-cf.yaml)

### Errors

- Package properties validation failed: Could not read package properties from JSON. (Service: AWSServiceCatalog; Status Code: 400; Error Code: InvalidParametersException;

- The parameter groupName cannot be used with the parameter subnet

```
--security-groups (list)

[EC2-Classic, default VPC] The names of the security groups. For a nondefault VPC, you must use security group IDs instead.

If you specify a network interface, you must specify any security groups as part of the network interface.

Default: Amazon EC2 uses the default security group.
```

### Links

- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html

- https://docs.aws.amazon.com/servicecatalog/latest/userguide/end-user-console.html

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalog.html

- [blogs](https://aws.amazon.com/about-aws/whats-new/management-and-governance/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23aws-service-catalog)

- AWS AppRegistry

CodeCommit -> Lambda -> Service Catalog