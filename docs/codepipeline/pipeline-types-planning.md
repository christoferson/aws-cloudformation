> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html
> Downloaded: 2026-10-18

# What type of pipeline is right for me?

The pipeline type is determined by the set of characteristics and features supported by each pipeline version.

The following is a summary of the use cases and characteristics available for each type of pipeline. 
|   |  V1 type |  V2 type |   
|  Characteristics |   |   |    
|  Use cases |    
-  

Standard deployments 
  |    
-  

Deployments with configuration from passing pipeline-level variables at runtime 
-  

Deployments where pipelines are configured to start on Git tags 
  |   
|  Action-level variables |  Supported |  Supported |   
|  PARALLEL execution mode |  Not supported |  Supported |   
|  Pipeline-level variables |  Not supported |  Supported |   
|  QUEUED execution mode |  Not supported |  Supported |   
|  Rollback for pipeline stages |  Not supported |  Supported |   
|  Source revision overrides |  Not supported |  Supported |   
|  Stage conditions |  Not supported |  Supported |   
|  Triggers and filtering Git tags, pull requests, branches, or file paths |  Not supported |  Supported |   
|  The Commands action |  Not supported |  Supported |   
|   Creating Entry conditions with Skip result |  Not supported |  Supported |   
|  Configure a stage for automatic retry on failure |  Not supported |  Supported |   

For information about pricing for CodePipeline, see Pricing.

You can create and run a Python script to help you analyze the potential cost of moving a V1 type pipeline to a V2 type pipeline.Note

The sample script below is intended for demonstration and evaluation purposes only. It is not a quote tool and does not guarantee the cost for your actual use of a V2 type pipeline, and it does not include any taxes that might apply. For information about pricing for CodePipeline, see Pricing.To create and run a script to help you evaluate the cost of moving a V1 type pipeline to a V2 type pipeline
-  

Download and install python. 
-  

Open a terminal window. Run the following command to create a new python script named PipelineCostAnalyzer.py. 

```
vi PipelineCostAnalyzer.py
```
 
-  

Copy and paste the following code into the PipelineCostAnalyzer.py script. 

```

import boto3
import sys
import math
from datetime import datetime, timedelta, timezone

if len(sys.argv) < 3:
    raise Exception("Please provide region name and pipeline name as arguments. Example usage: python PipelineCostAnalyzer.py us-east-1 MyPipeline")
session = boto3.Session(profile_name='default', region_name=sys.argv[1])
pipeline = sys.argv[2]
codepipeline = session.client('codepipeline')

def analyze_cost_in_v2(pipeline_name):
    if codepipeline.get_pipeline(name=pipeline)['pipeline']['pipelineType'] == 'V2':
        raise Exception("Provided pipeline is already of type V2.")
    total_action_executions = 0
    total_blling_action_executions = 0
    total_action_execution_minutes = 0
    cost = 0.0
    hasNextToken = True
    nextToken = ""

    while hasNextToken:
        if nextToken=="":
            response = codepipeline.list_action_executions(pipelineName=pipeline_name)
        else:
            response = codepipeline.list_action_executions(pipelineName=pipeline_name, nextToken=nextToken)
        if 'nextToken' in response:
            nextToken = response['nextToken']
        else:
            hasNextToken= False
        for action_execution in response['actionExecutionDetails']:
            start_time = action_execution['startTime']
            end_time = action_execution['lastUpdateTime']
            if (start_time < (datetime.now(timezone.utc) - timedelta(days=30))):
                hasNextToken= False
                continue
            total_action_executions += 1
            if (action_execution['status'] in ['Succeeded', 'Failed', 'Stopped']):
                action_owner = action_execution['input']['actionTypeId']['owner']
                action_category = action_execution['input']['actionTypeId']['category']
                if (action_owner == 'Custom' or (action_owner == 'AWS' and action_category == 'Approval')):
                    continue
                
                total_blling_action_executions += 1
                action_execution_minutes = (end_time - start_time).total_seconds()/60
                action_execution_cost = math.ceil(action_execution_minutes) * 0.002
                total_action_execution_minutes += action_execution_minutes
                cost = round(cost + action_execution_cost, 2)

    print ("{:<40}".format('Activity in last 30 days:'))
    print ("| {:<40} | {:<10}".format('___________________________________', '__________________'))
    print ("| {:<40} | {:<10}".format('Total action executions:', total_action_executions))
    print ("| {:<40} | {:<10}".format('Total billing action executions:', total_blling_action_executions))
    print ("| {:<40} | {:<10}".format('Total billing action execution minutes:', round(total_action_execution_minutes, 2)))
    print ("| {:<40} | {:<10}".format('Cost of moving to V2 in $:', cost - 1))

analyze_cost_in_v2(pipeline)
```
 
-  

From the terminal or command prompt, change directories to where you created the analyzer script. 

From that directory, run the following command, where region is the AWS Region where you created the V1 pipelines you want to analyze. You can also optionally evaluate a specific pipeline by providing its name: 

```
python3 PipelineCostAnalyzer.py region --pipelineName
```
 

For example, run the following command to run the python script named PipelineCostAnalyzer.py. In this example, the Region is `us-west-2`. 

```
python3 PipelineCostAnalyzer.py us-west-2
```
 Note

This script will analyze all V1 pipelines in the specified AWS Region unless you specify a specific pipeline name. 
-  

In the following sample output from the script, we can see the list of action executions, the list of action executions that were eligible for billing, the total runtime of these action executions, and the estimated cost of these actions as performed in a V2 pipeline. 

```
Activity in last 30 days: 
 | ___________________________________      | __________________
 | Total action executions:                 | 9         
 | Total billing action executions:         | 9         
 | Total billing action execution minutes:  | 5.59      
 | Cost of moving to V2 in $:               | -0.76 
```
 

In this example, the negative value in the last row represents the estimated amount that might be saved by moving to V2 type pipelines. Note

The script output and related examples that show costs and other information are estimates only. They are intended for demonstration and evaluation purposes only and do not guarantee any actual savings. For information about pricing for CodePipeline, see Pricing. 

