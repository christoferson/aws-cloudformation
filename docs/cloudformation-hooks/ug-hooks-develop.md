> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-develop.html
> Downloaded: 2026-10-22

# Developing custom Hooks using the CloudFormation CLI

This section is for customers who want to develop custom Hooks and register them in the CloudFormation registry. It provides an overview of the structure of CloudFormation Hooks, and guides for developing, registering, testing, managing, and publishing your own Hooks with Python or Java.

There are three major steps in developing a custom Hook: 
Initiate 

To develop custom Hooks, you must configure and use the CloudFormation CLI. To initiate a Hook's project and its required files, use the CloudFormation CLI init command and specify that you want to create a Hook. For more information, see Initiating a custom CloudFormation Hooks project. 
Model 

To model, author, and validate your Hook schema, define the Hook, its properties, and their attributes. 

The CloudFormation CLI creates empty handler functions which correspond to a specific Hook invocation point. Add your own logic to these handlers to control what happens during your Hook invocation at each stage of its target lifecycle. For more information, see Modeling custom CloudFormation Hooks. 
Register 

To register a Hook, submit your Hook to be registered either as a private or a public third-party extension. Register your Hook with the `submit` operation. For more information, see Registering a custom Hook with CloudFormation.  

The following tasks are associated with registering your Hook: 
Publish – Hooks are published to the registry. 
Configure – Hooks are configured when the type configuration invokes against stacks. 
 Note

Hooks will time out after 30 seconds and retry up to 3 times. For more information, see Timeout and retry limits. 
Topics
Prerequisites
Initiating a Hooks project
Modeling Hooks
Registering Hooks
Testing Hooks
Updating Hooks
Deregistering Hooks
Publishing Hooks
Schema syntax
