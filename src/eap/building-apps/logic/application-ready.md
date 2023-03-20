---
kinds: ServiceStudio.Model.SystemClientActions+OnApplicationReady+Kind
summary:
tags: 
locale: en-us
guid: 393ee8f0-dede-42fe-b5fb-ecd4ed0ec534
app_type: mobile apps, reactive web apps
platform-version: odc
---

# On Application Ready

Your app runs the **On Application Ready** during the loading of the app. Use **On Application Ready** to set up the app, for example, to initialize variables and mobile plugins.

The **On Application Ready** action runs asynchronously, and doesn't block the render of the screens.

To add the **On Application Ready** action to a Mobile or Web App do the following in ODC Studio:

1. In your app, open the **Logic** tab.

1. Right-click the **Client Actions** node in the tree and select **Add System Event** > **On Application Ready**.

    ![Systems Event in the context menu](images/ss-add-system-event-reactive.png)
