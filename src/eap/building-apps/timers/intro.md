---
summary: ODC timers use container-based cron jobs to run asynchronous logic, with configurable timeout and automatic retries on failure.
tags:
  - Asynchronous Processes
  - Infrastructure
  - Logic
  - Mentor Studio
  - Timers
  - Triggers
locale: en-us
guid: 94BE2885-0E48-4516-9CD1-6638F16E7F4E
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc portal
  - mentor studio
coverage-type:
  - understand
  - evaluate
topic:
  - process-data-timers
isautopublish: true
---

# Use Timers

You can use **Timers** to execute asynchronous logic in your OutSystems application. This is useful when running batch tasks like sending emails at a predetermined time, or when executing logic to configure an application after its deployment.

You create a Timer by describing it to Mentor Studio and validating the result, or manually in ODC Studio. For the steps, refer to [Create and run Timers](timer-create-run.md). For what a correct result looks like, refer to [Correct Timer output](#correct-timer-output).

## How Timers work

In OutSystems Developer Cloud (ODC), OutSystems implements timers using the underlying container infrastructure and its job scheduler features (cron jobs).

When you first publish an application, ODC creates a background job and the associated container resources for each timer. Container resources store the state and configure the triggering of the background job. The container stores the:

* Timers schedule
* Timer type (scheduled or on demand)
* Startup date
* Status of other control properties

The timer manager container service listens for the creation of the Timer resources which specifies the Timer's type and its schedule (either on-demand or scheduled). The timer manager also starts the job container that remotely calls the app business logic specified in the Timer. The timer manager also updates the status and control properties of the Timer resources along its lifecycle.

While distinct timers can run concurrently, the timer manager service ensures that only one instance of each timer runs at a time, preventing concurrency issues such as deadlocks.

The container infrastructure triggers the background jobs that have the schedule type of **scheduled**. The Timer manager service triggers jobs that have the schedule type of **on-demand**.

From ODC Portal, using **Run now**, you can launch on-demand timers asynchronously. This creates an event that the Timer manager uses to start the Timer job.

## Timers timeout

By default, a Timer has a timeout of 20 minutes, which you can change using its **Timeout in Minutes** property. The [maximum value](../../getting-started/system-requirements.md#platform-limits) that you can set for timer execution timeout is defined by the ODC platform limits.

If the Timer’s action doesn’t complete within the specified timeout, the action aborts, timer stops, and an error is logged. The timer then automatically retries up to three times. This timer retry count cannot be changed.

Each timer retry resets the timeout period, so the total timer execution time can exceed the original timeout. In the worst case, the timer could run up to four times the defined timeout  which includes the initial attempt and 3 retries.

For queries inside timer logic, the **Server Request Timeout** property has a [maximum value](../../getting-started/system-requirements.md#platform-limits).

## Correct Timer output

The platform guarantees that the model is valid, and you decide whether the Timer runs the logic you need. The following checks are examples, not a complete list.

* **Action.** The Timer runs the action that contains the logic, and the action has values for its input parameters. The output parameters of the action are available only after the action finishes executing.
* **Schedule type.** A **scheduled** Timer has a schedule, and an **on-demand** Timer runs when you launch it with **Run now** or the **Wake** action.
* **Timeout.** The **Timeout in Minutes** property fits the duration of the logic and doesn't exceed the [platform limit](../../getting-started/system-requirements.md#platform-limits). Because the platform retries a Timer that times out up to three times, the logic tolerates running again.
* **Single instance.** The logic doesn't require two instances of the same Timer to run at the same time, because the timer manager runs one instance of each Timer at a time.
* **Query timeouts.** Queries in the Timer logic stay within the **Server Request Timeout** limit.

## Related resources

The following resources describe how to create, run, and monitor Timers, and what the platform guarantees and what you check in a Mentor Studio proposal.

* [Create and run Timers](timer-create-run.md)
* [Monitor Timers](timer-monitor.md)
* [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md)
