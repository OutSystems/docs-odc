---
summary: Explore mobile plugin functionalities and their support in PWAs with OutSystems Developer Cloud (ODC).
tags: mobile plugins, progressive web apps, native mobile features, security, firebase
locale: en-us
guid: 55ef1d73-dac8-48e6-8b15-dc6990779660
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - forge
coverage-type:
  - understand
  - apply
topic:
  - using-cordova-plugins
---

# Mobile plugins

Plugins provide important functionalities to native mobile apps, letting you use many of the hardware capabilities of mobile devices. You can add notifications, use camera or global positioning services, read QR codes, and more.

## The list of supported mobile plugins

The table shows the OutSystems-supported mobile plugins that you can find in the Forge repository. Some of them are already supported when distributing your app as a Progressive Web App (PWA).

| Plugin                    | Description                                                  | Supported in PWA |
| ------------------------- | ------------------------------------------------------------ | ---------------- |
| Analytics | Firebase-based plugin that lets you gather information about app use.        | No               |
| AppShield | Protect your mobile apps from tampering. OutSystems AppShield hardens the native mobile build, enabling the app to detect attempts of modification and misuse. | No |
| Barcode            | Access the camera to scan barcodes and QR codes.                    | Yes              |
| Calendar           | Access the calendar of your device.                                 | No               |
| Camera             | Access the camera capabilities of the device.                       | Yes              |
| Ciphered Local Storage  | Keep your mobile application's sensitive data safe using a ciphered local storage database.    | No               |
| Cloud Messaging | Firebase-based plugin to give your app users a state-of-the-art notifications experience. | No |
| Contacts  | Access the contacts of your device.    | No               |
| Crash Reporting | Firebase-based plugin that provides realtime crash reporting to help you track, prioritize, and fix stability issues. | No |
| Dynamic Links | Firebase-based plugin that lets you manage links outside of your app. | No |
| File               | Manage files and folders within the app sandbox.             | No               |
| File Transfer      | Upload and download files in background.                     | Yes              |
| File Viewer        | View remote or app resource files.                           | No               |
| Health & Fitness   | Provides access to health and fitness data. Uses HealthKit API for iOS and Health Connect API for Android. | No          |
| InAppBrowser   | Open external URLs directly in your application. | No          |
| Key Store          | Store encrypted key-value pairs with optional authentication. | No               |
| Local Notifications          | Send app notifications to the device when the application isn't running in the foreground. | No               |
| Location           | Access the GPS capabilities the device.                      | Yes              |
| OneSignal Notifications      | Push notifications using OneSignal, with deep-linking and actions. | No               |
| Payments | Allows the addition of a payments experience using Apple Pay and Google Pay. | No |
| Performance Monitoring | Firebase-based plugin that lets you understand how you can improve the performance of your app. | No |
| SSL Pinning | Provide an extra layer of security to HTTPS communications by adding a verification of the server certificate against hashes of public keys. | No |
| Touch ID | Use authentication with biometrics in your application. | No |

### Notes

When working with the plugins:

* Use the plugin that supports iOS or Android, depending on your target platform. The app creation fails if you use a plugin that isn't supported on the target platform. For more information on app generation errors check the [list of MABS errors](https://success.outsystems.com/support/errors/mabs_errors/).
* Each time you add, remove, or modify the plugin in an app, OutSystems creates a mobile package which you then have to distribute to the users for installation.
* Include the plugin license in your app to respect the license agreements of that plugin. These license agreements are usually placed in the About page of the app that uses them.

## Installing a plugin and adding a public element to your app { #adding-plugins }

The plugins are available from the Forge repository. To use a plugin in your app, you first need to install the plugin to your organization and add the plugin elements to your app.

To install a supported plugin from Forge:

1. Find the plugin you want to use in the [list of supported mobile plugins](#the-list-of-supported-mobile-plugins).

1. In **ODC Portal** > **Forge** find the plugin and open the details page.

1. Click **Install** and follow the instructions to install the plugin. Optionally, install the demo app that comes with the plugin.

1. Once the installation finishes, add the actions you want to use as public elements in your mobile app.

## Built-in plugins

All mobile apps generated by OutSystems include a native shell with the following built-in plugins that are used internally, handling a variety of housekeeping and infrastructure tasks. While you may see the names of these built-in plugins in the native mobile shell logs they're not user-configurable.

| Plugin            | Description                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| OS Auth           | Handles OAuth flows and ensures compliance with the guidelines for SSO using the right WebView instances types for Android and iOS. |
| OS Cache          | Lets your application to run offline or with bad network conditions.                                                                |
| OS Cordova Loader | Loads the Cordova engine on your app.                                                                                               |
| OS Deeplinks      | Opens hyperlinks to specific screens of your app.                                                                                   |
| OS DB Upgrader    | Manages the local storage of your app.                                                                                              |
| OS Manifest       | Provides a parser for the app manifest.                                                                                             |
| OS Pre-Bundle     | Handles the content of the app pre-bundled resources.                                                                               |
| OS Security       | Provides the APIs for the security layer.                                                                                           |
| NetworkStatus     | Lets your app know when the device is online/offline and informs of the type of network available (for example, WiFi, 3G, 4G).      |
