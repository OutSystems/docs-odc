---
summary: Explore the integration and management of notifications in OutSystems Developer Cloud (ODC) using the Firebase Cloud Messaging plugin.
tags: firebase, notifications, plugin integration, deprecation, migration
locale: en-us
guid: 22d6edad-3a83-44f8-abbf-81e0b2d02041
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4352%3A160&mode=design&t=qrb6BRX1TGRFDKu7-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - forge
  - odc portal
coverage-type:
  - understand
  - apply
---

# Firebase Cloud Messaging plugin using configurator APIs

<div class="info" markdown="1">

This article applies only to Firebase Cloud Messaging plugin version 0.1.2 and older. These old versions use Cloud Messaging Configurator REST APIs to manage the notifications. 

The Cloud Messaging Configurator REST APIs, version 0.1.2 and older, are deprecated. This means that the **v2** and **v1** endpoints are no longer functional. For more information, see [Firebase Cloud Messaging HTTP protocol](https://firebase.google.com/docs/cloud-messaging/http-server-ref). 

OutSystems recommends that you migrate to [Firebase Cloud Messaging plugin](firebase-cloud-messaging-plugin-server-action.md) version 1.0.0 and newer by June 2024.  

</div>

The Firebase Cloud Messaging plugin lets you set a notification experience that starts the Firebase cross-platform messaging solution. This plugin lets you send normal and silent notifications to your mobile app users. Normal notifications can include customizable actions and sounds.

<div class="info" markdown="1">

You can install the Firebase Cloud Messaging Plugin from the Forge in ODC Portal.

</div>

Normal notifications have a UI that displays visual and auditory cues. The cues either display in the notifications area of the app or in the scope of the app. Silent notifications don't display any visual cues. Notifications can deliver a data package to the app (called extra data) in the form of a key-value pairs list.

OutSystems also has notification features you can use to create custom actions and custom sounds.

Following is a high-level process describing how to implement and manage the notifications of your OutSystems app.

1. Use the **Cloud Messaging Configurator** app to consume REST API methods that let you set up a back-end notification service.

1. Use the **Firebase Cloud Messaging** plugin actions to implement basic notifications functions on your app.

    <div class="info" markdown="1">

    You can download the **Cloud Messaging Configurator** app from [Forge](https://www.outsystems.com/forge/).

    </div>

1. To prevent the app from crashing, verify the plugin is available during runtime in your app. To check the availability of your plugin, from ODC Studio use the **Logic** > **Client Actions** > **CloudMessagingPlugin** > **CheckCloudMessagingPlugin** action. If the plugin isn't available to your app, display an error to your end-users.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your OutSystems apps, and how to install a sample app, see [Installing a plugin and adding a public element to your app](../intro.md#installing-a-plugin-and-adding-a-public-element-to-your-app). To use this plugin, verify your app meets all the [Firebase prerequisites](intro.md#prerequisites).

</div>

## Sample app

OutSystems provides a sample app that contains logic for common use cases. Install the Firebase sample app from Forge and then open it in ODC Studio.

This sample app shows you how to do the following:

* Trigger a basic notification, leading to internal routes.

* Trigger a notification with custom actions that lead to internal routes.

* Trigger a notification with custom actions that lead to a given URL in the device’s browser.

* Trigger a notification with custom actions that lead to an external app.

* Trigger a notification with custom actions that open a text field.

* Trigger a notification with a custom sound.

## Compose and manage push notifications

The following steps describe how to create a back-end notification service and how to prepare a mobile app to respond with push notifications:

1. [Set up a back-end notification service using the send Notifications REST API methods](#setup-back-end).

1. [Enable basic notification functions in your app using the plugin's actions](#enable-notifications-plugins).

1. [Enable notifications with custom actions](#enable-custom-actions).

1. [Enable notifications with custom sounds](#enable-custom-sounds).

1. [Manage the experience of in-app notifications using the Notifications block](#manage-notification-ux).

1. [Manage the experience of custom actions using the Notifications block](#manage-custom-actions-ux).

### Set up a back-end notification service { #setup-back-end }

To set up a back-end notification service, do the following:

1. Install the **Cloud Messaging Configurator** app from [Forge](https://www.outsystems.com/forge/) to your environment. This component includes the REST API methods necessary to send notifications to a list of users or topics.

1. Open the **Cloud Messaging Configurator** Configurator page.

1. Within the **Settings** panel, set the **AppId** and **AppKey** properties using encrypted values. These values are used to authenticate your REST API, so make sure you keep the encrypted values secure.

   ![Screenshot showing where to input encrypted App ID and Key in the Cloud Messaging Configurator app](images/firebase-messaging-api-key-odcs.png "Encrypted App ID and Key in Cloud Messaging Configurator")

1. Create a new app to serve as your back-end notification. This app can be a Reactive Web or Mobile.

1. In the newly created app, consume the **Cloud Messaging Configurator** REST API methods. For more details on how to consume a REST API, see [Consume one or more REST API methods](../../consume_rest/consume-a-rest-api.md).

   After importing the REST API methods you may get an invalid URL error. If you get an error, then in the consumed REST API properties, change the **Base URL** to include your stage address, setting it as `https://<your-environment>/CloudMessagingConfigurator/rest/v1`. Replace `<your-environment>` with your environment address and `<rest-api-version>` with the version you want to use.

    <div class="info" markdown='1'>

    OutSystems offers two REST API versions based on the features you want to use. See the [reference page](../firebase-plugin/firebase-cm-plugin-api-v1-v2.md) to learn more about the versions.

    </div>

    ![Screenshot illustrating how to set the Base URL in the REST API properties for Cloud Messaging Configurator](images/set-base-url-in-rest-api-odcs.png "Setting the Base URL in REST API Properties")

1. Then use the AppId and AppKey you defined in step 3 to authenticate your REST calls. In the consumed REST API properties, add the following **HTTP headers**:

    * `X-Send-AppId` = `<your-appid>`, replacing `<your-appid>` with the **AppId** defined in step 3.

    * `X-Send-Key` = `<your-key>`,, replacing `<your-key>` with the **AppKey** defined in step 3.

<div class="info" markdown='1'>

To learn more about the v1 and v2 endpoints of OutSystems REST API, see the [reference page](../firebase-plugin/firebase-cm-plugin-api-v1-v2.md).

</div>

Now you can start to create the UI for your back-end notification service. For example, to send a notification to all users on the associated Firebase project (using an app with the Cloud Messaging plugin), associate a **SendNotifcationToUsers** method to a button. 

If you want to send the notification to specific users, note that these are identified by their Firebase Token, that can be obtained with the **GetToken** client action. You can find this ID on the Firebase Project Settings under the Cloud Messaging tab. 

To send a notification to all users, or to all Android or iOS users, you need to fill the **SenderID** structure attribute of the **SendRequest** parameter. You can find this ID on the Firebase Project Settings under the Cloud Messaging tab. 

Moreover, to send a notification specifically to all Android or iOS users, you should set the **SendToPlatform** structure attribute to one of the values in the **Platform** static entity that the plugin provides.

![Diagram depicting the logic to send a notification to all users in the associated Firebase project](images/firebase-messaging-send-offer-notification-logic-odcs.png "Send Notification Logic in OutSystems")

To access values for the parameters **FCMServerKey** and **SenderID**, in the ODC Studio, navigate to **Project Settings** > **Cloud Messaging** > Firebase Console.

![Screenshot showing the navigation path to retrieve FCM Server Key and Sender ID in ODC Studio](images/firebase-messaging-get-fcm-server-key-and-sender-id.png "Retrieving FCM Server Key and Sender ID")

Other available methods include **SendNotificationToTopics**, **SendSilentNotificationToUsers**, and **SendSilentNotificationToTopics**.

For silent notifications (**SendSilentNotificationToUsers** and **SendSilentNotificationToTopics**), the **TimeToLive** structure attribute sets the notifications' expiration time. More specifically, if the **TimeValue** for a specific **TimeUnit** is greater than 0, the message will persist in the local storage and be delivered at the first opportunity, until the expiration time has passed.

For topic notifications (**SendNotificationToTopics**, **SendSilentNotificationToTopics**), set the topics for which a notification will be delivered to in the **SendToTopics** structure attribute.

### Enable basic notification functions in your app { #enable-notifications-plugins }

This section describes some of the actions that you can use to leverage notification functions on your mobile app.

On first use, you might want to register your users to receive notifications. For that, you can use the **RegisterDevice** action when your app opens. For example, if the user isn’t already registered, you can call the **RegisterDevice** action on the **OnReady** event of the app’s home screen. On first use, this action displays a native permission request and, upon user acceptance, the device is registered on the Firebase Cloud Messaging service, ready to receive notifications.

Alternatively, you can provide an explicit way to register and unregister the device from the Firebase cloud Messaging service using the **RegisterDevice** / **UnregisterDevice** actions. Then associate the actions to a UI element such as a toggle.

To prevent errors, it's a good practice to first check if the plugin is available using the **CheckCloudMessagingPlugin** action.

This is the ManageNotifications view.

![User interface view for registering a device with Firebase Cloud Messaging service](images/firebase-messaging-register-device-odcs.png "Register Device View in Firebase Messaging")

This is the logical flow view.

![Flowchart showing the logic for registering a device with Firebase Cloud Messaging service](images/firebase-messaging-with-register-device-logic-odcs.png "Register Device Logic Flow")

After registering the device on the Firebase Cloud Messaging service, the active device's token becomes available and can be retrieved using the action **GetToken**. For iOS devices, the Apple Push Notification service token can also be retrieved, using the **GetAPNsToken** action.

To manage topic subscriptions you can use the **SubscribeTopic / UnsubscribeTopic** actions. Users to which the app subscribes (or unsubscribes). If the topic doesn't exist yet on the Firebase Cloud Messaging project, the Cloud Messaging Configurator app creates a new topic.

This is the ManageNotifications view.

![User interface view for adding a topic in Firebase Cloud Messaging service](images/firebase-messaging-with-add-topic-odcs.png "Add Topic to Firebase Messaging")

This is the logical flow view.

![Flowchart showing the logic for adding a topic in Firebase Cloud Messaging service](images/firebase-messaging-with-logic-of-add-topic-odcs.png "Logic of Adding Topic in Firebase Messaging")

To retrieve all pending silent notifications you can use the **GetPendingNotifications** action. This action outputs a silent notifications list with Timestamp, MessageID, TimeToLive, and an ExtraData list of key-value pairs. So, app users don't see any visual or sound cues.

<div class="info" markdown="1">

When receiving a silent notification without extra data, and your app is in the background, the notification is not saved in the database. For example, the notification won’t be returned in the **GetPendingNotifications** action.

</div>

As a part of the notification experience, the developers can control the badge number which is a value that displays on the top-right corner of the app icon. The way you control the badge number differs from the Operating System:

* For iOS you can use the **GetBadgeNumber** action to retrieve the current badge number and the **SetBadgeNumber** to specify the number to display on the app icon.

* For Android you can only specify a given badge number after receiving a notification. Thus, you can use the **SendLocalNotification** action and set the badge number through the action parameter *BadgeNumber*.

<div class="info" markdown="1">

Starting on Android 14, most devices do not show the badge number when long-pressing the app's icon.

</div>

![Screenshot of the logic flow for setting badge numbers on app icons for notifications](images/firebase-messaging-with-setting-badge-logic-odcs.png "Setting Badge Numbers Logic Flow")

Finally, you can give users the ability to clear all app's notifications remaining in the notification center. For this, you can associate the **ClearNotifications** action to a piece of UI such as a button.

![Diagram showing the logic to clear all notifications from the notification center in Firebase Messaging](images/firebase-messaging-with-clear-notifications-logic-odcs.png "Clear Notifications Logic Flow")

### Enable notifications with custom actions { #enable-custom-actions }

To enhance your notification with custom actions you must use the **v2 REST API**, with the **ActionList** parameter inside the Notification parameter on the **SendNotificationToTopics** or **SendNotificationToUsers** REST API methods.

<div class="info" markdown='1'>

To learn more about the v2 endpoint of OutSystems REST API, see the [reference page](../firebase-plugin/firebase-cm-plugin-api-v1-v2.md).

</div>

OutSystems offers the following types of custom actions:

* **Internal route** - Sends an event to be handled by the app, similar to a basic notification click.

    * For this action, you must check the **Manage the experience of custom actions**. 

* **Web route** - Opens a given URL in the device’s browser.

* **App route** - Opens a route in an external app.

* **Reply field** - Opens a text field that lets users send a text directly to the app.

### Enable notifications with custom sound { #enable-custom-sounds }

To enhance your notification with custom sounds, follow these steps:

1. Put the .wav files you want to use as notification sounds into a .zip file called **sounds.zip**. 

1. Upload the .zip file to the app’s Resources folder. 

1. Use the **v2 REST API**, using the *Sound* parameter inside the *Notification* parameter on the **SendNotificationToTopics** or **SendNotificationToUsers** methods.


It is important to note the following requirements for custom sounds:

* Only .wav files are supported.

* The name of the zip sound file (.wav) can only contain lowercase letters, numbers, and underscores. If you add any other characters, the android build won't work.

* The sounds.zip file should be included with the “Deploy Action” set to “Deploy to Target Directory”.

 ### Manage the experience of in-app notifications { #manage-notification-ux }

By default, a cloud messaging notification displays in the notification center. However, you can also display the notification in-app when the app is on the foreground. To enable this notification, you can use the **NotificationsHandler** block. This block triggers events that pass the parameters of both notifications and silent notifications to the context of the app.

You need to add this block to each screen that might handle the notification content.

Optionally, you can use the **NotificationDialog** block, which provides a notification dialog UI inside the app.

### Manage the experience of custom actions using the Notifications block. { #manage-custom-actions-ux }

By default, a cloud messaging notification displays in the notification center. However, you can also display the notification in-app when the app is in the foreground. To enable this you can use the **NotificationsHandler** block, using **InternalRouteActionClicked** for custom actions. This block triggers events that pass the parameters of both notifications and silent notifications to the context of the app.

Add this block to each screen that might handle the notification content.

## Manage the experience of notification clicks

When the end-user clicks on a notification in the notification center, the app opens by default. If you want your app to handle the notification click, you can use the **NotificationsHandler** block and define a handler for the **NotificationClicked** event.

If you want to navigate to a screen inside your app when the end-user clicks on a notification, you can use the **BuildInternalDeepLink** client action from the plugin. Our Sample App has this scenario implemented. If you want to do something else after the end-user clicks on a notification, simply implement your logic in the handler you create for the **NotificationClicked** event.

### Optional setup for notification Channel Name and Description - Android only

By default, the Cloud Messaging plugin defines values for the notification channel name and description on local notifications. But in some instances, you might want to define a different default value by adding the following name and value properties on the extensibility configurations of your app:

```JSON
{
    "preferences": {
        "android": [
            {
                "name": "NotificationChannelDefaultName",
                "value": "This is my channel Name"
            },
            {
                "name": "NotificationChannelDefaultDescription",
                "value": "This is my channel Description"
            }
        ],
    }
}
```

The following image illustrates how the notification channel's name and description will appear in the user device:

![Screenshot of notification channel name and description](images/fcm-notification-channel.png "Notification Channel")

## Limitations

### On silent notifications

For iOS.

When a device has a low battery, apps don't process silent notifications.

For more information, see [Apple documentation](https://developer.apple.com/documentation/).

### On subscribe to topic

For both iOS and Android.

Firebase SDKs for Android and iOS don't support subscribing to topics if the name contains spaces, like `TV Shows`.

### On Changes in Android 15

From Android 15 onwards, users can install an app in the [Private space](https://developer.android.com/about/versions/15/features#private-space). Users can lock their private space at any time, which means that push notifications are not shown until the user unlocks it.

It is not possible to detect if an app is installed in the private space. Therefore, if your app shows any critical notifications, inform your users to avoid installing the app in the private space.

For more information about the behavior changes of your app related to the private space, refer to [Android documentation](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-changes).


## On compatibility with Firebase Performance

For both iOS and Android.

Using the Firebase Cloud Messaging in combination with Firebase Performance requires v1.0.4 (or higher) of the latter.

