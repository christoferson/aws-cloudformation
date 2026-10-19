> Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-DeploymentWindow.html
> Downloaded: 2026-10-19

# DeploymentWindow

When you create a condition, you can add the `DeploymentWindow` rule. This section provides a reference for the rule parameters. For more information about rules and conditions, see How do stage conditions work?.Topics
Rule type
Configuration parameters
Example rule configuration
See also
 

## Rule type  
Category: `Rule` 
Owner: `AWS` 
Provider: `DeploymentWindow` 
Version: `1` 
 

## Configuration parameters   

**Cron**  

Required: Yes 

The expression that defines the days and times when the deployment will be allowed. Cron expressions are comprised of 6 required fields and one optional field separated by white space. The cron expression fields allow you to specify a schedule pattern with a cron expression as follows.  
|  Field name |  Allowed values |  Allowed special characters |    
|  Seconds |  N/A |  * |   
|  Minutes |  0-59 |  , - * / |   
|  Hours |  0-23 |  , - * / |   
|  Day-of-month |  1-31 |  , - * ? / L W |   
|  Month |  1-12 or JAN-DEC |  , - * / |   
|  Day-of-Week |  1-7 or SUN-SAT |  , - * ? / L # |   
|  Year (Optional) |  empty, 1970-2199 |  , - * / |     
The '*' character is used to specify all values. For example, "*" in the minute field means "every minute". 
The '?' character is allowed for the day-of-month and day-of-week fields. It is used to specify 'no specific value'. This is useful when you need to specify something in one of the two fields, but not the other. 
The '-' character is used to specify ranges. For example, "10-12" in the hour field means "the hours 10, 11 and 12". 
The ',' character is used to specify additional values. For example "MON,WED,FRI" in the day-of-week field means "the days Monday, Wednesday, and Friday". 
The '/' character is used to specify increments. For example "0/15" in the seconds field means "the seconds 0, 15, 30, and 45". And "5/15" in the seconds field means "the seconds 5, 20, 35, and 50". Specifying '*' before the '/' is equivalent to specifying 0 is the value to start with.  
The 'L' character is allowed for the day-of-month and day-of-week fields. This character is short-hand for "last", but it has different meaning in each of the two fields. For example, the value "L" in the day-of-month field means "the last day of the month" - day 31 for January, day 28 for February on non-leap years. If used in the day-of-week field by itself, it simply means "7" or "SAT". But if used in the day-of-week field after another value, it means "the last <specified_day> day of the month" - for example "6L" means "the last friday of the month". You can also specify an offset from the last day of the month, such as "L-3" which would mean the third-to-last day of the calendar month. 
The 'W' character is allowed for the day-of-month field. This character is used to specify the weekday (Monday-Friday) nearest the given day. As an example, if you were to specify "15W" as the value for the day-of-month field, the meaning is: "the nearest weekday to the 15th of the month". So if the 15th is a Saturday, the trigger will fire on Friday the 14th. If the 15th is a Sunday, the trigger will fire on Monday the 16th. If the 15th is a Tuesday, then it will fire on Tuesday the 15th. 
The 'L' and 'W' characters can also be combined for the day-of-month expression to yield 'LW', which translates to "last weekday of the month". 
The '#' character is allowed for the day-of-week field. This character is used to specify "the nth" <specified_day> day of the month. For example, the value of "6#3" in the day-of-week field means the third Friday of the month (day 6 = Friday and "#3" = the 3rd one in the month). 
The legal characters and the names of months and days of the week are not case sensitive. 
  

**TimeZone**  

Required: No 

The time zone for the deployment window. The regular expression matches patterns in the following formats:  
Region/City format. The value matches a time zone in the format Region/City or Region/City_City. For example, `America/New_York` or `Europe/Berlin`. 
UTC format. The value matches the string UTC optionally followed by an offset in the format +HH:MM or -HH:MM. For example, `UTC`, `UTC+05:30`, or `UTC-03:00`. This is the default format if the parameter is not set otherwise. 
Abbreviation format. The value matches a 3 to 5 character abbreviation for a time zone. For example, `EST` or `IST`. 

For a table of valid TimeZoneID values, see https://docs.oracle.com/middleware/1221/wcs/tag-ref/MISC/TimeZones.html. Note that certain abbreviations are duplicated abbreviations, such as CST for Central Standard Time, China Standard Time, and Cuba Standard Time. 
   

## Example rule configuration  

**YAML** 

```
- name: MyDeploymentRule
  ruleTypeId:
    category: Rule
    owner: AWS
    provider: DeploymentWindow
    version: '1'
  configuration:
    Cron: 0 0 9-17 ? * MON-FRI *
    TimeZone: PST
  inputArtifacts: []
  region: us-east-1
```
  

**JSON** 

```
[
                    {
                        "name": "MyDeploymentRule",
                        "ruleTypeId": {
                            "category": "Rule",
                            "owner": "AWS",
                            "provider": "DeploymentWindow",
                            "version": "1"
                        },
                        "configuration": {
                            "Cron": "0 0 9-17 ? * MON-FRI *",
                            "TimeZone": "PST"
                        },
                        "inputArtifacts": [],
                        "region": "us-east-1"
                    }
                ]
```
   

## See also 

The following related resources can help you as you work with this rule.  
Creating On Success conditions – This section provides steps for creating an On Success condition with a deployment window rule. 
For more information about rules and conditions, see Condition, RuleTypeId, and RuleExecution in the CodePipeline API Guide.
