---
summary: Learn how to create and manage timers in OutSystems Developer Cloud (ODC) to execute application logic periodically.
tags:
  - Timers
locale: en-us
guid: 8468A775-BC5C-489C-8A44-D15F7C0B5BF1
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - odc portal
  - mentor studio
coverage-type:
  - apply
  - evaluate
topic:
  - process-data-timers
isautopublish: true
---

# Create and run Timers

A timer is a tool that lets you execute application logic periodically at a scheduled time. Using  ODC (OutSystems Developer Cloud) Studio you can create timers and then using ODC Portal you can modify the timer schedule. You associate timers with apps.

You create Timers at design time by describing them to Mentor Studio and validating the result, or manually in ODC Studio.

For more information about how timers work, refer to [Use Timers](intro.md).

## Create a Timer with Mentor Studio

Create a Timer by describing it and the logic it runs in Mentor Studio, and validate the Timer and its action before you publish.

In your prompt, include the following:

* The Timer
* The action it runs
* The values for the action input parameters
* The schedule
* The timeout

For example, the following sentences form one prompt:

* "Create a Timer named ArchiveOldOrders that runs a new server action named ArchiveOrders every day at 2:00 AM, with a timeout of 30 minutes."
* "In ArchiveOrders, set IsArchived to True for the Order records that are older than 365 days."

### Validate the Timer

The platform guarantees that the model is valid, and you decide whether the Timer runs the logic you need at the time you need. In the **Events** tab of ODC Studio, select the Timer and check the following:

* The **Action** property selects the action that contains the logic you described. When the action has input parameters, the Timer has values for them.
* The **Schedule** property matches your requirement: a recurrent schedule, a run each time the app is published, or no schedule for an on-demand Timer. A Timer that runs when published also runs after an automatic patch.
* The **Timeout in Minutes** property fits the duration of the logic. The default is 20 minutes, and the platform limits the maximum value.
* The action logic tolerates running again, because a Timer that times out retries up to three times.
* No other logic expects the output parameters of the action while the Timer runs, because the output parameters are available only after the action finishes executing.
* After you publish the app, the Timer appears in ODC Portal, where you can change the schedule for a stage and run the Timer. Refer to [Run a Timer in the ODC Portal](#run-a-timer-in-the-odc-portal).

## Create a Timer manually in ODC Studio

To create a Timer in your app:

1. On the right side of the screen, select the **Events** tab, right-click the **Timers** folder and select **Add Timer**.

1. In the **Name** field, enter a name for your timer.

1. From the **Action** dropdown, select an existing action or click **Select Action...** to open the **Select Action** dialog box.

1. Choose an action to execute when the timer runs or select  **New Server Action** to create a new action.

If the Action you specify has input parameters, then when you create the Timer you need to specify values that are passed as parameters when the Timer wakes. However, if the action has output parameters, you can't access the parameters until the action finishes executing.

You can set a schedule to run the Timer automatically or you can force the Timer to run without waiting at a specific time.

## Set the Timer schedule

You can set the schedule of a Timer in one of the following ways:

* **Setting the Schedule for a property of the Timer at design time**: You can define a recurrent schedule, such as daily or weekly, or define the Timer to run each time the app is published, for example to execute configurations or to bootstrap data.

* **Setting the Timer schedule at runtime in ODC Portal**: You might want to customize the Timer schedule when deploying an app to another stage. In this case, the effective Timer schedule is set in ODC Portal, which uses the default settings in every stage unless specifically modified.

When you define a schedule for your Timer, the Timer runs at the predefined time.

## Force the Timer to run

You can force a Timer to run without waiting for the scheduled time by:

* Using the **Wake&lt;TimerName&gt;** built-in action
* Running the Timer from ODC Portal

Neither of these options changes the timer schedule, so the Timer continues to run normally. Also, since the same Timer doesn't run twice simultaneously, if you run a Timer that's already running, the second execution starts after the first one finishes.

<div class="info" markdown="1">

Forcing the execution of a deactivated Timer that has a schedule defined, sets the Timer to run as soon as possible and activates the Timer again.

</div>

### Use the WakeTimer built-in Action {#wake-timer}

When you create a new Timer, a built-in action is available to you to programmatically run the timer. This action is called **Wake(Timer Name)** and can be used in your app logic.

When the **Wake&lt;TimerName&gt;** action executes, the **NextRun** property of that Timer updates to the present time. The timer is then handled by the Scheduler and executes according to its priorities.

The **Wake&lt;TimerName&gt;** action doesn't receive any input parameters and doesn't return any output parameters.

To use the **Wake&lt;TimerName&gt;** built-in action in your logic:

1. From  the **Events** tab, expand the Timer element.

1. Drag the **Wake&lt;TimerName&gt;** action and use it in your logic.

### Run a Timer in the ODC Portal

To force the execution of a Timer in the ODC Portal:

1. From the ODC Portal > **App** tab, select your **App**.

1. From the left Nav menu, click **Configurations** and open the **Timers** section. A list of timers displays.

1. Click on the Timer you want to run. From the right side of your screen, the timer detail screen displays.

1. From the Schedule section, select when you want the timer to run and click **Apply**. The timer runs when scheduled.  

## Related resources

The following resources describe prompt examples and the steps to prompt Mentor Studio.

* For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#logic).
* For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).
