---
summary: Learn how to use Timers to execute asynchronous logic. 
locale: en-us
guid: 94BE2885-0E48-4516-9CD1-6638F16E7F4E
app_type: web apps, mobile apps
---

# Use Timers

You can use **Timers** to execute asynchronous logic in your OutSystems application. This is useful when running batch tasks like sending emails at a predetermined time, or when executing logic to configure an application after its deployment.

## How Timers work 

In Project Neo, OutSystems implements timers using the underlying container infrastructure and its job scheduler features (cron jobs).

When you first publish an application, Project Neo creates a background job and the associated container resources for each timer. Container resources store the state and configure the triggering of the background job. The container stores the:

* Timers schedule
* Timer type (scheduled or on demand)
* Startup date
* Status of other control properties

The Timer manager container service listens for the creation of the Timer resources which specifies the Timer's type and its schedule (either on-demand or scheduled). The Timer manager also starts the job container that remotely calls the Application business logic specified in the OutSystems Timer. The Timer manager also updates the status and control properties of the Timer resources along its lifecycle.

The container infrastructure triggers the background jobs that have the schedule type of **scheduled**. The Timer manager service triggers jobs that have the schedule type of **on-demand**.

From the Portal, using the **Wake** function, you can launch on-demand timers asynchronously. The **Wake** function creates an event that the Timer manager uses to start the Timer job.

## Timers timeout

By default,the timeout of a Timer is set to 20 minutes. You can change the timeout setting in the **Timeout in Minutes** property of the Timer.

If the action associated with a Timer doesn't end within a predefined time, the action aborts and the Timer stops. This is an error. The timer tries to execute three more times. The number of retries isn't configurable.

