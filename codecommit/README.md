
## CodeCommit Cloudformation Templates

## CodeCommit [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html)


### CodeCommit - Basic

Provision a CodeCommit repository

[code-codecommit](code-codecommit.yaml)

### CodeCommit - Trigger

Provision a CodeCommit repository with Trigger definition that notifies SNS.

Trigger will be called for the following events:

- Push to Existing Branch
- Create Branch or Tag
- Delete Branch or Tag

##### Triggers vs Notification [link](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email.html)
- Repository notifications are different from repository triggers.
- Although you can configure a trigger to use Amazon SNS to send emails about some repository events, 
those events are limited to operational events, such as creating branches and pushing code to a branch. 
- Triggers do not use CloudWatch Events rules to evaluate repository events. They are more limited in scope. 

[code-codecommit-triggers](code-codecommit-triggers.yaml)


## Resources

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeCommit.html
