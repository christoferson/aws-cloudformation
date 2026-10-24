> Source: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.scheduled-practice-runs.html
> Downloaded: 2026-10-24

# When ARC schedules, starts, and ends practice runs

ARC schedules a practice run for a resource weekly, for about 30 minutes. ARC schedules, starts, and manages practice runs for each resource independently. ARC does not batch together practice runs for resources in the same account. You can also start on-demand practice runs yourself, to help verify that your setup is safe for a zonal autoshift event.

When a practice run continues for the expected duration, without interruption, it is marked with an outcome of `SUCCESSFUL`. There are several other possible outcomes: `FAILED`, `INTERRUPTED`, `CAPACITY_CHECK_FAILED` and `PENDING`. Outcome values and descriptions are included in the Outcomes for practice runs section.

There are some scenarios when ARC interrupts a practice run and ends it. For example, if an autoshift starts during a practice run, ARC interrupts the practice run and ends it. As another example, say that the resource has an adverse response to a practice run and causes an alarm that you've specified to monitor the practice run to go into an `ALARM` state. In this scenario, ARC also interrupts the practice run and ends it.

In addition, there are several scenarios when ARC does not start a schedule practice run for a resource.

In response to interrupted and blocked practice runs for a resource, ARC does the following: 
If a practice run for a resource is interrupted while it's in progress, ARC considers the weekly practice run to be over, and schedules a new practice run for the resource for the next week. The weekly practice outcome is `INTERRUPTED` in this scenario, not `FAILED`. The practice run outcome set to `FAILED` only when the outcome alarm that monitors the practice run goes into an `ALARM` state during the practice run. 
If there is a blocking constraint when a practice run for a resource is scheduled to be started, ARC does not start the practice run. ARC continues regular monitoring, to determine if there are still one or more blocking constraints. When there aren't any blocking constraints, ARC starts the practice run for the resource.

The following are examples of blocking constraints that stop ARC from starting, or continuing, a practice run for a resource: 
ARC does not start or continue practice runs when there is an AWS Fault Injection Service experiment in progress. If an AWS FIS event is active when ARC has scheduled a practice run to start, ARC does not start the practice run. ARC monitors throughout practice runs for blocking constraints, including an AWS FIS event. If an AWS FIS event starts while a practice run is active, ARC ends the practice run and doesn't attempt to start another one until the next regularly scheduled practice run for the resource.
If there is a current AWS event in a Region, ARC does not start practice runs for resources, and ends active practice runs, in the Region.

When the practice run finishes without being interrupted, ARC schedules the next practice run in a week, as usual. If a practice run isn't started because of a blocking constraint, such as a AWS FIS experiment or a blocked time window that you've specified, ARC continues to attempt to start a practice run until the practice run can be started.
