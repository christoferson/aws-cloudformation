

In order for CodeDeploy to work, you need to install the CodeDeploy agent on each EC2 instance on which youÅfre running CodeDeploy.  CodeDeploy communicates with the agents via HTTPS over port 443. The agent contains code that has CodeDeploy domain-specific knowledge and uses the defined configuration to run through its lifecycle events. 

file_exists_behavior: OVERWRITE
https://github.com/aws/aws-codedeploy-agent/issues/14
Codedeploy Overwrite the content with auto deploy. : r/aws