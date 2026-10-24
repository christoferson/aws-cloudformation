> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.blocked-windows.html
> Downloaded: 2026-10-24

# Blocked windows and allowed windows (in UTC)

You have the option to block or allow practice runs for specific calendar dates, or for specific time windows, that is, days and times, specified in UTC. 

For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01`.

Or, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example, in UTC: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30`.

Alternatively, you might decide that Wednesdays and Fridays from noon to 5:00 are the best times for ARC to start practice runs, to test your setup. For this scenario, you could set the following recurring days and times as allowed windows, for example, in UTC: `WED-12:00-17:00 FRI-12:00-17:00`.
