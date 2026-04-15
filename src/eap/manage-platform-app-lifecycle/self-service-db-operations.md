---
summary: Manage and reschedule updates for the OutSystems Developer Cloud (ODC) infrastructure using the ODC Portal, ensuring flexibility and preparation for infrastructure managers.
tags: infrastructure management, platform updates, scheduling updates, odc portal, outsystems developer cloud
guid: b34fef09-2fa8-4b16-ad5c-b7d032d7032f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4977-217
outsystems-tools:
  - odc portal
coverage-type:
  - apply
  - understand
audience:
  - infrastructure managers
  - platform administrators
topic:
helpids: 30745
---
# Managing platform infrastructure updates

Whenever OutSystems updates the ODC platform infrastructure, it's done within a set time window. Within that time, you have the flexibility to reschedule these updates for each stage of your tenant. This allows you to pick the most convenient time to prepare for the changes and ensure a smooth update process.

## Where to find the upcoming updates

In your ODC Portal you can find a list of all scheduled updates on your infrastructure, see there details and reschedule any of the operations. To do this:

1. On the ODC Portal, click **Maintain** -> **Platform updates**. This opens the Platform updates screen.

1. On the Platform updates screen select the **Infrastructure** tab.

1. Here, you'll find a list of all upcoming updates, with information on:

    * The update scope/short description.
    * The time-frame in which the update occurs.
    * The affected stages, the status of the update and the scheduled date for the update to run.

Here you can also get to the details page, by clicking in **View details**. This allows you to get more detail on the update, re-scheduled it, and check the documentation for any breaking changes.

![ODC Portal showing the Platform updates screen with a list of scheduled updates and their statuses.](images/platform-updates-pl.png "Platform Updates Screen")

## Rescheduling an update

When you open a details screen, you can see detailed information on the update. Namely, a more detailed description, its impact, the available time-frame, access to the update documentation, and options to re-schedule for any of your stages.

![Detailed view of a database major version upgrade update in the ODC Portal, with options to reschedule.](images/update-details-pl.png "Update Details Screen")

To rescheduled, do the following:

1. Click on the rescheduled button for the desired stage. This opens a pop up.
1. In the pop up select the desired date for the update, and click **Reschedule update**.

![Popup window in the ODC Portal for rescheduling an update, showing a calendar to select a new date and time.](images/reschedule-update-pl.png "Reschedule Update Popup")

The schedule table changes the scheduled date for your selection and the status changes to **User-scheduled**.

## Updates life cycle

Updates have a life cycle and within that life cycle the process goes through several different states:

* Before the update starts:
    * **Checking update**. This is a process that runs on your tenant before the update to ensure your tenant is ready for the update.
    * **System scheduled.** When the Checking update ends and the update is possible on your tenant, the system defines a date for the update. If you don't reschedule it, the update runs on that defined date.
    * **User scheduled.** Whenever you decide to reschedule an update the update changes the date when it runs and changes the state.
    * **Skipped.** This update is not necessary for your tenant and won't be applied.
    * **Canceled**. Whenever an update is canceled by OutSystems, this state becomes visible.

* During the update:
    * **In progress**. During the update this status indicates that the update is running.
    * **Pending update.** This indicates that the update is still going but something is preventing the update to finish.

* After the update:
    * **Updated**. The update finished with success, if there are breaking changes you should test for them to ensure they're fixed.
    * **Error**. There was an error during the update. You get notified of this error and an automatic reschedule happens.

## Other considerations on the updates

1. Updates are mandatory and you can't reschedule them outside of the defined time-frame.

1. Always make sure to check the documentation page for the update to check for breaking changes and guidance on what to do in case of any.

1. It's recommended that you do the update on dev first, test the update and then do the remainder stages. This is especially important if the update introduces breaking changes.
