> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/creating-hooks-with-cloudformation.html
> Downloaded: 2026-10-22

# Create Hooks using CloudFormation templates

This page provides links to sample CloudFormation templates and technical reference topics for Hooks.

By using CloudFormation templates to create Hooks, you can reuse your template to set up your Hooks consistently and repeatedly. This approach allows you to define your Hooks once, and then provision the same Hooks over and over in multiple AWS accounts and Regions. 

CloudFormation offers the following specialized resource types for Guard and Lambda Hook creation.  
|  Task |  Solution |  Links |    
|   

Create a Guard Hook  |   

Use the `AWS::CloudFormation::GuardHook` resource type to create and activate a Guard Hook.  |   

Sample template 

Technical reference  |   
|   

Create a Lambda Hook  |   

Use the `AWS::CloudFormation::LambdaHook` resource type to create and activate a Lambda Hook.  |   

Sample template 

Technical reference  |   

CloudFormation also offers the following resource types that you can use in your stack templates for custom Hook creation.  
|  Task |  Solution |  Links |    
|   

Register a Hook   |   

Use the `AWS::CloudFormation::HookVersion` resource type to publish a new or first version of a custom Hook to the CloudFormation registry.  |   

Sample templates 

Technical reference  |   
|   

Set the Hook's configuration  |   

Use the `AWS::CloudFormation::HookTypeConfig` resource type to specify the configuration of a custom Hook.  |   

Sample templates 

Technical reference  |   
|   

Set the Hook's default version  |   

Use the `AWS::CloudFormation::HookDefaultVersion` resource type to specify the default version of a custom Hook.  |   

Sample templates 

Technical reference  |   
|   

Register your account as a publisher  |   

Use the `AWS::CloudFormation::Publisher` resource type to register your account as a publisher of public extensions (Hooks, modules, and resource types) in the CloudFormation registry.  |   

Technical reference  |   
|   

Publish a Hook publicly  |   

Use the `AWS::CloudFormation::PublicTypeVersion` resource type to test and publish a registered custom Hook as a public, third-party Hook.  |   

Technical reference  |   
|   

Activate public, third-party Hooks  |   

The `AWS::CloudFormation::TypeActivation` resource type works together with the `AWS::CloudFormation::HookTypeConfig` resource type to activate a public, third-party custom Hook in your account.  |   

Technical reference  |
