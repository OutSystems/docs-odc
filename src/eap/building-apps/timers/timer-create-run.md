---
summary: Learn how to create and manage timers in OutSystems Developer Cloud (ODC) to execute application logic periodically.
tags: scheduler, process automation, application lifecycle management, periodic tasks, cloud development
locale: en-us
guid: 8468A775-BC5C-489C-8A44-D15F7C0B5BF1
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
topic:
  - process-data-timers
---

# Create and run Timers

A timer is a tool that lets you execute application logic periodically at a scheduled time. Using  ODC (OutSystems Developer Cloud) Studio you can create timers and then using ODC Portal you can modify the timer schedule. You associate timers with apps.

Follow the instructions below in ODC Studio learn how to create **Timers** at design time.

For more information about how timers work, see  [Use Timers](intro.md).

## Create the Timer

To create a Timer in your app:

1. On the right side of the screen, select the **Events** tab, right-click the **Timers** folder and select **Add Timer**.

1. In the **Name** field, enter a name for your timer.

1. From the **Action** dropdown, select an existing action or click **Select Action...** to open the **Select Action** dialog box.

1. Choose an action to execute when the timer runs or select  **New Server Action** to create a new action.

If the Action you specify has input parameters, then when you create the Timer you need to specify values that are passed as parameters when the Timer wakes. However, if the action has output parameters, you can't access the parameters until the action finishes executing.

You can set a schedule to run the Timer automatically or you can force the Timer to run without waiting at a specific time.

## Set the Timer Schedule

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

### Use the WakeTimer built-in Action

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
