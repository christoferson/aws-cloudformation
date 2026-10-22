> Source: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-view-logs.html
> Downloaded: 2026-10-22

# View logs for the Guard Hooks in your account

When you activate a Guard Hook, you can specify an Amazon S3 bucket as the destination for the Hook output report. Once activated, the Hook automatically stores the results of your Guard rule validations in the specified bucket. You can then view these results in the Amazon S3 console. 

## View Guard Hook logs in the Amazon S3 console To view the Guard Hook output log file
Sign-in to the https://console.aws.amazon.com/s3/. 
On the navigation bar at the top of the screen, choose your AWS Region. 
Choose Buckets. 
Choose the bucket you selected for your Guard output report. 
Choose the desired validation output report log file. 
Choose whether you want to Download the file or Open it to view.
