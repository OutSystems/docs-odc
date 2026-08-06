---
guid: fd941531-d146-4f4e-aa3b-58a9eb70832e
locale: en-us
summary: 'ODC push notifications best practices for OutSystems Developer Cloud: FCM setup, permission timing, token management, and foreground/background handling.'
figma:
coverage-type:
  - evaluate
  - apply
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Android
  - Best Practices
  - Caching
  - iOS
  - Mobile app
  - Plugins
  - Testing
outsystems-tools:
  - odc studio
  - odc portal
  - forge
helpids:
isautopublish: true
---

# Best practices for push notifications

Push notifications are a direct channel for re-engaging users and delivering time-sensitive content, but the margin for error is narrow: a poorly timed permission request locks you out permanently, a stale token means silent delivery failure, and ignoring foreground and background differences produces a broken user experience. Following these recommendations helps you build a notification system that is reliable, respectful of user preferences, and straightforward to maintain.

## Use the Firebase Cloud Messaging plugin {#use-fcm-plugin}

The Firebase Cloud Messaging (FCM) plugin is the recommended OutSystems-supported plugin for push notifications in ODC mobile apps. It provides a single API for both Android and iOS: Firebase handles Android delivery natively and routes iOS notifications through the Apple Push Notification service (APNs) on your behalf. You configure Firebase once and the plugin takes care of the platform-specific delivery. No direct APNs configuration is required.

### Recommendation

Install the Firebase Cloud Messaging plugin from Forge in ODC Portal and complete the Firebase project setup before implementing any notification logic. Create and register your Firebase project by following the [Firebase plugin prerequisites](../../../integration-with-systems/mobile-plugins/firebase-plugin/intro.md#prerequisites), [upload the configuration files as extensibility settings](../../../integration-with-systems/mobile-plugins/firebase-plugin/intro.md#adding-google-services-configuration-file), and [configure the service account credentials](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#set-up-a-back-end-notification-service).

After adding the plugin as a dependency in your app, call [**CheckCloudMessagingPlugin**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) before using any plugin action to verify it is available at runtime. If the plugin is unavailable, for example when running in a browser during development, display a clear error rather than letting the call fail silently.

To send push notifications from server-side logic, use the Firebase Cloud Messaging Server Actions library, available on Forge. For more information, refer to [Firebase Cloud Messaging plugin using server actions](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md).

Most recommendations in this article are specific to the Firebase Cloud Messaging plugin. If your project requires a different notification provider, refer to [Use alternative notification providers when Firebase doesn't meet your requirements](#alternative-providers).

### Benefits

Using the OutSystems-supported plugin means the notification infrastructure is tested and maintained alongside MABS releases. Firebase's unified API eliminates the need to manage separate APNs and FCM integrations, reducing configuration surface and the risk of platform-specific delivery failures.

## Request notification permissions at the right moment {#contextual-permission-request}

Apps running on iOS and Android 13 or higher require explicit user permission before your app displays push notifications. When the system permission dialog appears at app launch with no context, users deny it. On iOS, a denied permission requires the user to navigate to device settings to re-enable notifications manually. That rarely happens in practice.

### Recommendation

Notification permission is shown when you call the [**RegisterDevice**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) client action. Do not call **RegisterDevice** in the **On Application Ready** event. Call it only after the user has experienced something in the app that makes the value of notifications clear.

Effective moments to request permission include:

* After onboarding, when the user has seen the core value of the app.
* When the user reaches a feature that depends on notifications, such as order status alerts or appointment reminders.
* On a dedicated notification preferences screen where the user opts in deliberately.

Before calling **RegisterDevice**, add an explanation of what notifications the user will receive and why. This can be a sentence or two on an existing onboarding step, a feature introduction, a text next to a settings toggle, or even its own screen. Users who understand what they are granting are more likely to approve the prompt.

When **RegisterDevice** returns success, call [**GetToken**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) immediately and persist the returned token on the server associated with the user's ID. When it returns an error, check whether the user denied the permission. On Android, one denial still allows a retry; a second denial or "Don't ask again" blocks it permanently. On iOS, any denial is permanent from the app's perspective. In both cases, direct the user to **Settings** > **[App Name]** > **Notifications** to enable notifications manually.

### Benefits

Contextual permission requests produce higher opt-in rates than at-launch prompts. A larger pool of opted-in users is the prerequisite for reliable notification delivery.

## Store and refresh device tokens reliably {#token-management}

A Firebase device token identifies a specific app installation on a specific device. Tokens are not permanent: they change when the user reinstalls the app, clears app data, or when Firebase rotates the token automatically. Sending a notification to a stale token results in a silent delivery failure with no error surfaced to the user.

### Recommendation

After a successful **RegisterDevice** call, retrieve the token with **GetToken** and store it server-side, associated with the user's ID. At minimum, store the token, the user ID, the platform (iOS or Android), and the timestamp of the last update.

If your app supports users being logged in on multiple devices simultaneously, model token storage as one-to-many: keep a separate record per device rather than a single token per user. When sending a notification to a user, query all their active tokens and include the full list in the [**SendNotificationToUsers**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#sendnotificationtousers) server action call. On logout, remove only the token for the device being logged out, not all tokens for that user.

On every app launch where the user is authenticated, call **GetToken** again and compare the result to the stored value. If the token has changed, update the database record immediately.

When the user logs out, call [**UnregisterDevice**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) to deregister from FCM, then remove or invalidate the token record from your database. Sending notifications to a device that has been logged out wastes API calls and can expose content to unintended recipients.

When a **SendNotificationToUsers** call returns an error for a specific token, inspect the error to determine whether it indicates the token is no longer valid before removing it from your database.

For iOS, [**GetAPNsToken**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) retrieves the Apple Push Notification service (APNs) token alongside the FCM token. Store it if your backend requires direct APNs delivery.

### Benefits

Accurate, up-to-date token records are the prerequisite for reliable delivery. Removing stale tokens reduces unnecessary Firebase API calls and prevents errors from accumulating silently over time.

## Handle foreground and background notification states {#foreground-background}

A push notification behaves differently depending on whether the app is in the foreground or the background when it arrives. Understanding this distinction is essential for delivering a consistent experience.

When the app is in the background, the operating system displays the notification in the device notification center automatically. When the app is in the foreground, behavior depends on the **ShowIfAppOpen** parameter in the server action request. By default, **ShowIfAppOpen** is `false` and the notification is shown in the device notification center, even when the app is open. When set to `true`, the notification is delivered to the [**NotificationsHandler**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#manage-the-experience-of-in-app-notifications-using-the-notifications-block) block in your app instead, where you control how it is displayed in-app.

Silent notifications (data-only messages with no visible UI) add another layer: on Android, silent notifications received while the app is in the background are persisted to the local database and retrieved with [**GetPendingNotification**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) on the next foreground session. On iOS, silent notifications are not processed when the device battery is low.

### Recommendation

When sending a notification that should be visible while the app is in the foreground, set **ShowIfAppOpen** to `true` in the **SendNotificationToUsers** or [**SendNotificationToTopics**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#sendnotificationtotopics) server action request. Without this, the notification is shown in the notification center even when the app is open, instead of triggering in-app handling.

Add the **NotificationsHandler** block to every screen that needs to respond to notification content. Handle both the [**NotificationReceived**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#manage-the-experience-of-in-app-notifications-using-the-notifications-block) event (notification arrives while the app is open) and the [**NotificationClicked**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#manage-the-experience-of-notification-clicks) event (user taps a notification to open the app). To display an in-app notification dialog, use the [**NotificationDialog**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#manage-the-experience-of-in-app-notifications-using-the-notifications-block) block. For custom behavior, handle **NotificationReceived** directly in your logic.

For silent notifications, handle both delivery paths. When the app is in the foreground, handle the [**SilentNotificationReceived**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#manage-the-experience-of-in-app-notifications-using-the-notifications-block) event in the **NotificationsHandler** block to process silent notifications as they arrive. When the app is in the background, silent notifications are queued — call **GetPendingNotification** during the app's initialization flow to retrieve them on the next foreground session.

### Benefits

Understanding the role of **ShowIfAppOpen** prevents silent delivery failures where foreground users never see a notification. Explicitly handling both states produces a consistent experience regardless of whether the app is open when the notification arrives.

## Cache the Firebase access token {#access-token-caching}

The [**GetAccessToken**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#getacesstoken) server action generates a short-lived OAuth token that authenticates requests to the Firebase Cloud Messaging HTTP v1 API. This token expires after one hour. Calling **GetAccessToken** before every notification send introduces unnecessary latency and API round-trips to Firebase.

### Recommendation

Store the access token and its creation timestamp in a database table. Before calling any notification send server action, check whether the stored token is still valid:

1. Read the stored token and its creation timestamp from the database.
1. Check whether more than 55 minutes have elapsed since the token was created. Use 55 minutes rather than the full 60 as a safety margin to avoid edge cases where the token expires mid-request.
1. If the token is still valid, use it directly.
1. If the token has expired, call **GetAccessToken**, persist the new token with a fresh timestamp, then use the new token for the send request.

Wrap this caching check in a reusable server action so every notification-sending flow uses the same logic.

### Benefits

Caching the access token removes a Firebase API call from every notification send. This matters most for time-sensitive notifications and high-frequency sends, where the token generation latency would otherwise accumulate.

## Scale notification delivery for large audiences {#large-audience-delivery}

The **SendNotificationToUsers** server action has a hard limit of 100 tokens per call. For large audiences, iterating through all tokens in batches adds complexity and latency. FCM topics offer a simpler and more scalable alternative for broadcast-style delivery.

### Recommendation

For notifications targeting a large group of users who share a common characteristic, use FCM topics rather than token lists.

Subscribe devices to a topic using the [**Subscribe**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) client action after a successful **RegisterDevice** call. Choose topic names that reflect the audience characteristic, such as a region, subscription tier, or feature preference. Topic names cannot contain spaces. When a user's preferences change or they no longer belong to an audience, for example after a subscription downgrade or a region change, call [**Unsubscribe**](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md#enable-basic-notification-functions-in-your-app) to remove the device from the relevant topic.

To send a notification to the audience, call **SendNotificationToTopics** with the relevant topic name. FCM handles delivery to all subscribers without any batching or iteration required on your side, and there is no per-call recipient limit.

For notifications where the audience is a computed subset that doesn't map to a predefined topic, or where the content differs per user (such as order status updates or personalized alerts), use token-based delivery with timer batching:

1. Query your token database to retrieve the full list of target device tokens.
1. Iterate over the list in batches of up to 100 tokens.
1. Call **SendNotificationToUsers** once per batch.
1. Log the result of each batch using **LogMessage**. Remove tokens that return an invalid-token error from the database.

Wrap each batch call in error handling so a failure in one batch does not stop the remaining batches from sending.

### Benefits

Topics offload fan-out complexity to FCM, eliminating batching logic for broadcast notifications. Timer batching remains the right approach for targeted sends where the audience or content is user-specific.

## Test push notifications on physical devices {#physical-device-testing}

Push notifications rely on FCM for both Android and iOS. On iOS, FCM routes through APNs under the hood. Neither platform delivers push notifications in browser emulation or iOS simulators. iOS additionally requires a real device with a valid provisioning profile.

### Recommendation

Always test push notifications on real physical devices. To install a test build on a device:

1. In ODC Portal, generate a mobile package with the [**Debug** build type](../mobile-build-types.md#android-debug) for Android or the [**Development** build type](../mobile-build-types.md#ios-dev) for iOS. For detailed steps, refer to [Create mobile app package](../creating-mobile-package.md).
1. Scan the QR code displayed in ODC Portal with the device to download and install the app.
1. Test the full notification flow on the device: permission request, foreground receipt, background receipt, and notification tap.

Test on at least one Android device and one iOS device. On Android, test across more than one manufacturer when possible, as notification display behavior can vary between manufacturers.

When a notification flow fails on a physical device and the web layer provides no diagnostic information, inspect native-layer logs using Android Studio or Xcode, as described in [Use Xcode and Android Studio for native-layer debugging](best-practices-testing-debugging.md#native-tools).

### Benefits

Physical device testing surfaces notification-specific issues that simulators cannot reproduce, including FCM registration failures, permission dialog behavior on specific Android manufacturers, and notification display differences between iOS versions.

## Use alternative notification providers when Firebase doesn't meet your requirements {#alternative-providers}

Firebase Cloud Messaging is the primary notification infrastructure for ODC mobile apps, available through the OutSystems-supported plugin. Some projects have requirements that Firebase alone does not address, such as cross-platform audience management, built-in segmentation dashboards, or an existing notification vendor the organization has already standardized on.

### Use the OneSignal plugin

The [OneSignal plugin](https://www.outsystems.com/forge/component-overview/15923/onesignal-plugin-odc) is an OutSystems-supported plugin available on Forge. It abstracts platform-specific details behind a single API, handling both iOS (APNs) and Android from the same interface, and provides an audience management dashboard for managing user segments and sending campaigns.

To use OneSignal in an ODC mobile app:

1. Configure a OneSignal app for iOS and Android by following the [OneSignal setup documentation](https://documentation.onesignal.com/docs/mobile-sdk-setup).
1. Install the OneSignal plugin from Forge in ODC Portal.
1. If the app requires login, register the device after a successful login using **RegisterWithUser** to associate the device token with the authenticated user. If the app does not require login, register in the **On Application Ready** event using **Register**.

For more information, refer to [How to use push notifications with OneSignal](https://success.outsystems.com/documentation/how_to_guides/integrations/how_to_use_push_notifications_with_onesignal/).

### Unsupported providers

You can integrate notification providers not available on Forge, such as Pushwoosh or Airship, by wrapping their native SDKs in a [custom Capacitor plugin](../../../integration-with-systems/mobile-plugins/capacitor-plugins/build-capacitor-plugin.md). Before building a custom integration, follow the plugin decision flow in [Best practices for native integrations and plugins](best-practices-native-plugins.md) to confirm no supported alternative meets your requirements.

Plugins not supported by OutSystems require you to maintain compatibility with future MABS versions independently. Treat them as long-term maintenance items in your release plan.

### Benefits

Using an OutSystems-supported plugin such as OneSignal provides provider flexibility with a reduced maintenance burden compared to a custom integration.

## Related resources

Refer to the following resources for more information about the Firebase Cloud Messaging plugin and its server actions.

* [Firebase Cloud Messaging plugin using server actions](../../../integration-with-systems/mobile-plugins/firebase-plugin/firebase-cloud-messaging-plugin-server-action.md)
* [Firebase plugins](../../../integration-with-systems/mobile-plugins/firebase-plugin/intro.md)

Refer to the following resources for general guidance on evaluating and using mobile plugins.

* [Use mobile plugins](../../../integration-with-systems/mobile-plugins/intro.md)
* [OutSystems supported mobile plugins](../../../integration-with-systems/mobile-plugins/os-supported-plugins.md)

Refer to the following best practices for related mobile app topics.

* [Best practices for native integrations and plugins](best-practices-native-plugins.md)
* [Best practices for testing and debugging mobile apps](best-practices-testing-debugging.md)

Refer to the following resource for creating and distributing mobile app packages.

* [Create mobile app package](../creating-mobile-package.md)
