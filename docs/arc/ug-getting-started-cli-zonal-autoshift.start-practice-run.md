> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/getting-started-cli-zonal-autoshift.start-practice-run.html
> Downloaded: 2026-10-24

# Start an on-demand practice run

You can start an on-demand practice run zonal shift with the CLI by using the `start-practice-run` command.

For example, to start a practice run for a resource, use a command like the following:

```
aws arc-zonal-shift start-practice-run 
    --resource-identifier="arn:aws:elasticloadbalancing:Region:111122223333:ExampleALB123456890" \
    "awayFrom": "usw2-az1",
			
```

```
{
    "awayFrom": "usw2-az1",
    "comment": "Practice run started. Shifting traffic away from Availability Zone usw2-az1.",
}
```
