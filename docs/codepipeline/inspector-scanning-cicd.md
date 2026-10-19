> Source: https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html
> Downloaded: 2026-10-19

# Integrating Amazon Inspector scans into your CI/CD pipeline

 The Amazon Inspector CI/CD integration utilizes the Amazon Inspector SBOM Generator and Amazon Inspector Scan API to produce vulnerability reports for container images. The Amazon Inspector SBOM Generator creates a software bill of materials (SBOM) for archives, container images, directories, local systems, and compiled Go and Rust binaries. The Amazon Inspector Scan API scans the SBOM to create a report with details about detected vulnerabilities. You can integrate Amazon Inspector container image scans with your CI/CD pipeline to scan for software vulnerabilities and produce vulnerability reports, which allow you to investigate and remediate risks before deployment. To set up your CI/CD integration, you can use plugins or create a custom CI/CD integration using the Amazon Inspector SBOM Generator and Amazon Inspector Scan API. Topics
Plugin integration
Custom integration
Setting up an AWS account to use the Amazon Inspector CI/CD integration
Amazon Inspector Dockerfile checks
Creating a custom CI/CD pipeline integration with Amazon Inspector Scan
Using Amazon Inspector with GitHub actions
Using the Amazon Inspector Jenkins plugin
Using CodeCatalyst actions with Amazon Inspector
Using Amazon Inspector Scan actions with CodePipeline
Using the Amazon Inspector TeamCity plugin
Using Amazon Inspector with GitLab components
 

## Plugin integration 

Amazon Inspector provides plugins for supported CI/CD solutions. You can install these plugins from their respective marketplaces and then use them to add Amazon Inspector Scans as a build step in your pipeline. The plugin build step runs the Amazon Inspector SBOM generator on the image you supply, and then runs the Amazon Inspector Scan API on the generated SBOM. 

The following is an overview of how an Amazon Inspector CI/CD integration works through plugins:  
You configure an AWS account to allow access to the Amazon Inspector Scan API. For instructions, see Setting up an AWS account to use the Amazon Inspector CI/CD integration. 
You install the Amazon Inspector plugin from the marketplace. 
You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see Amazon Inspector SBOM Generator. 
You add Amazon Inspector Scans as a build step in your CI/CD pipeline and configure the scan. 
When you run a build, the plugin takes your container image as input and then runs the Amazon Inspector SBOM Generator on the image to generate a CycloneDX compatible SBOM. 
From there, the plugin sends the generated SBOM to an Amazon Inspector Scan API endpoint which assesses each SBOM component for vulnerabilities. 
The Amazon Inspector Scan API response is transformed into a vulnerability report in CSV, SBOM JSON, and HTML formats. The report contains details about any vulnerabilities that Amazon Inspector found. 
 

### Supported CI/CD solutions 

Amazon Inspector currently supports the following CI/CD solutions. For complete instructions on setting up the CI/CD integration using a plugin, select the plugin for your CI/CD solution:  
GitHub actions 
Jenkins plugin 
TeamCity plugin 
 

## Custom integration 

If Amazon Inspector does not provide plugins for your CI/CD solution, you can create your own custom CI/CD integration using a combination of the Amazon Inspector SBOM Generator and the Amazon Inspector Scan API. You can also use a custom integration to fine-tune scans using the options available through Amazon Inspector SBOM Generator.  

The following is an overview of how a custom Amazon Inspector CI/CD integration works:  
You configure an AWS account to allow access to the Amazon Inspector Scan API. For instructions, see Setting up an AWS account to use the Amazon Inspector CI/CD integration. 
You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see Amazon Inspector SBOM Generator. 
You use the Amazon Inspector SBOM Generator to generate a CycloneDX compatible SBOM for your container image. 
You use the Amazon Inspector Scan API on the generated SBOM to produce a vulnerability report. 
 

For instructions on setting up a custom integration, see Creating a custom CI/CD pipeline integration with Amazon Inspector Scan.
