> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-view-logs.html
> Downloaded: 2026-10-22

# View logs for the Lambda Hooks in your account

When using a Lambda Hook, your validation output report log file can be found in the Lambda console. 

## View Lambda Hook logs in the Lambda console To view the Lambda Hook output log file
Sign-in to the Lambda console. 
On the navigation bar at the top of the screen, choose your AWS Region. 
Choose Functions. 
Choose desired Lambda function. 
Choose the Test tab. 
Choose CloudWatch Logs Live Trail 
Choose the drop-down menu and select the log groups you want to view. 
Choose Start. The log will display in the CloudWatch Logs Live Trail window. Choose View in columns or View in plain text depending on your preference.  
You can add more filters to the results by adding them in the Add filter pattern field. This field allows you filter results to only include events that match the specified pattern.  
 
 

For more information on viewing logs for Lambda functions, see Viewing CloudWatch Logs for Lambda functions.
