> Source: https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-codepipeline-actions.html
> Downloaded: 2026-10-19

# Using Amazon Inspector Scan actions with CodePipeline

 You can use Amazon Inspector with AWS CodePipeline by adding vulnerability scans to your workflows. This integration leverages the Amazon Inspector SBOM Generator and Amazon Inspector Scan API to produce detailed reports at the end of your build. The integration helps you investigate and remediate risk before deployment. The `InspectorScan` action is a managed compute action in CodePipeline that automates detecting and fixing security vulnerabilities in your open source code. You can use this action with application source code in your third-party repository, such as GitHub or Bitbucket Cloud, or with images for container applications. For more information, see InspectorScan invoke action reference in the AWS CodePipeline User Guide.
