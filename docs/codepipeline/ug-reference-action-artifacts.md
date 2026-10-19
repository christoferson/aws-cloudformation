> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-action-artifacts.html
> Downloaded: 2026-10-19

# Valid input and output artifacts for each action type

Depending on the action type and provider, you can have the following number of input and output artifacts.Action type constraints for artifacts 
|  Owner |  Type of action |  Provider |  Valid number of input artifacts |  Valid number of output artifacts |    
|  `AWS` |  Source |  `S3` |  0 |  1 |   
|  `AWS` |  Source |  `CodeCommit` |  0 |  1 |   
|  `AWS` |  Source |  `ECR` |  0 |  1 |   
|  `ThirdParty` |  Source |  `CodeStarSourceConnection` |  0 |  1 |   
|  `AWS` |  Build |  `CodeBuild` |  1 to 5 |  0 to 5 |   
|  `AWS` |  Test |  `CodeBuild` |  1 to 5 |  0 to 5 |   
|  `AWS` |  Test |  `DeviceFarm` |  1 |  0 |   
|  `AWS` |  Approval |  `ThirdParty` |  0 |  0 |   
|  `AWS` |  Deploy |  `S3` |  1 |  0 |   
|  `AWS` |  Deploy |  `CloudFormation` |  0 to 10 |  0 to 1 |   
|  `AWS` |  Deploy |  `CodeDeploy` |  1 |  0 |   
|  `AWS` |  Deploy |  `ElasticBeanstalk` |  1 |  0 |   
|  `AWS` |  Deploy |  `OpsWorks` |  1 |  0 |   
|  `AWS` |  Deploy |  `ECS` |  1 |  0 |   
|  `AWS` |  Deploy |  `ServiceCatalog` |  1 |  0 |   
|  `AWS` |  Invoke |  `Lambda` |  0 to 5 |  0 to 5 |   
|  `ThirdParty` |  Deploy |  `AlexaSkillsKit` |  1 to 2 |  0 |   
|  `Custom` |  Build |  `Jenkins` |  0 to 5 |  0 to 5 |   
|  `Custom` |  Test |  `Jenkins` |  0 to 5 |  0 to 5 |   
|  `Custom` |  Any supported category |  As specified in the custom action |  0 to 5 |  0 to 5 |
