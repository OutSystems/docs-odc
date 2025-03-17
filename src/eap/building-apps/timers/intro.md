---
summary: OutSystems Developer Cloud (ODC) leverages container infrastructure to manage and execute timers for asynchronous tasks in applications.
tags: timers, asynchronous tasks, container infrastructure, job scheduler, cron jobs
locale: en-us
guid: 94BE2885-0E48-4516-9CD1-6638F16E7F4E
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc portal
coverage-type:
  - understand
topic:
  - process-data-timers
---

# Use Timers

You can use **Timers** to execute asynchronous logic in your OutSystems application. This is useful when running batch tasks like sending emails at a predetermined time, or when executing logic to configure an application after its deployment.

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

From ODC Portal, using the **Wake** function, you can launch on-demand timers asynchronously. The **Wake** function creates an event that the Timer manager uses to start the Timer job.

## Timers timeout

By default, the timeout of a Timer is set to 20 minutes. You can change the timeout using the **Timeout in Minutes** property of the Timer. There is a [maximum value](../../getting-started/system-requirements.md#timers-timeout).

If the action associated with a Timer doesn't end within a predefined time, the action aborts and the Timer stops. This is an error. The timer tries to execute three more times. The number of retries isn't configurable.

For queries inside timer logic, the **Server Request Timeout** property has a [maximum value](../../getting-started/system-requirements.md#timers-timeout).
