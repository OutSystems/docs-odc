---
summary: On Application Resume ODC system event fires when a mobile app returns to foreground; add it in ODC Studio Logic tab to check network availability.
tags:
  - Events
  - Lifecycle
  - Logic
  - Mobile app
locale: en-us
guid: 96c703ae-d97e-4ceb-b511-6524da0b7cf3
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3214%3A21752&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - system-events
isautopublish: true
---

# On Application Resume

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Action to be executed when the application is returning from background to foreground. Can be used for validating application state when resuming (e.g. checking for network availability).  

To add this action to a Mobile, do the following:

1. In your app, open the **Logic** tab.

1. Right-click the "Client Actions" node in the tree and select **Add System Event** > **On Application Resume**.

    ![Screenshot showing how to add the On Application Resume system event in OutSystems Developer Cloud.](images/add-system-event-resume-odcs.png "Add On Application Resume System Event")

## Related resources

* [Best practices for app lifecycle, navigation, and deep linking](../mobile/best-practices/best-practices-app-lifecycle-navigation.md)
