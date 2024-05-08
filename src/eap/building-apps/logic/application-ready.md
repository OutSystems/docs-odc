---
summary: Explore how the OutSystems Developer Cloud (ODC) utilizes the "On Application Ready" event to initialize apps and manage screen rendering.
tags: 
locale: en-us
guid: 393ee8f0-dede-42fe-b5fb-ecd4ed0ec534
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21674&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# On Application Ready

Your app runs the **On Application Ready** during the loading of the app. Use **On Application Ready** to set up the app, for example, to initialize variables and mobile plugins.

**On Application Ready** action runs synchronously and blocks the screen render. When navigating to an app for the first time, the accessed screen renders only after **On Application Ready** completes.

After the first execution, navigations between screens from the same app don't trigger **On Application Ready**. This includes navigating to other screens using External Site or Destination or navigating back to a previous screen. However, if you navigate to a screen of a different app, the **On Application Ready** of that app is executed.

Note that if the user types or refreshes the URL of a screen directly in the browser address bar, **On Application Ready** is executed. This causes the corresponding app to reload.

To add the **On Application Ready** action to a Mobile or Web App do the following in ODC Studio:

1. In your app, open the **Logic** tab.

1. Right-click the **Client Actions** node in the tree and select **Add System Event** > **On Application Ready**.

    ![Screenshot showing the 'Add System Event' option in the context menu with 'On Application Ready' highlighted.](images/ss-add-system-event-reactive.png "Add System Event Option")
