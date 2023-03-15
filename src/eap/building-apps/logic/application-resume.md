---
kinds: ServiceStudio.Model.SystemClientActions+OnApplicationResume+Kind
tags: 
locale: en-us
guid: 96c703ae-d97e-4ceb-b511-6524da0b7cf3
app_type: mobile apps
platform-version: odc
---

# On Application Resume

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Action to be executed when the application is returning from background to foreground. Can be used for validating application state when resuming (e.g. checking for network availability).  

To add this action to a Mobile, do the following:

1. In your app, open the **Logic** tab.

1. Right-click the "Client Actions" node in the tree and select **Add System Event** > **On Application Resume**.

    ![](images/ss-add-system-event-reactive.png)
