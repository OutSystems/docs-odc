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

[Mobile Apps Build Service (MABS 12)](../../building-apps/mobile/mabs-overview.md) introduces support for the Capacitor framework alongside Cordova, providing you a modern, flexible way to build mobile apps. When building your mobile apps with MABS 12, you can choose between the Cordova and Capacitor frameworks.

For new mobile apps, to leverage Capacitor, consider building Capacitor plugins for use in your mobile apps. For detailed information about building Capacitor plugins, refer to [How to build a Capacitor plugin](https://docs.google.com/document/d/1OtPcZy19-XqsTfNuCKtpg-G4I_XEmp-2uhHhcbpE7Cg/edit?tab=t.0#heading=h.oebpf6wacdvm). 

For existing apps, to leverage the modern capabilities, consider migrating your existing mobile apps to the Capacitor framework by adapting your existing custom Cordova plugins for Capacitor or developing native Capacitor plugins. For detailed information about migrating the plugins, refer to [Migrate plugins to Capacitor](migrate-cordova-plugin.md).

## Using custom Cordova plugins with Capacitor

Capacitor provides a compatibility layer that allows Cordova plugins to run within Capacitor. However, not all Cordova plugins are fully compatible, especially those that rely on Cordova-specific APIs or lifecycle events.

Here are some guidelines for using a Cordova plugin with Capacitor:

* Test your Cordova plugin with Capacitor first.
  
* If issues arise, check for a Capacitor equivalent plugin or update the plugin to support Capacitor APIs.
  
* To leverage the latest mobile app capabilities, consider migrating custom Cordova plugins to Capacitor. For detailed information about migrating the plugins, refer to [Migrate plugins to Capacitor](https://docs.google.com/document/d/10qjRTGV8nGrwZwxyBxCvTVX0Y1qxaG1mlvXVlpNCblg/edit?usp=sharing).
  
* If your plugin is used in both Cordova and Capacitor apps, consider building a dual-stack plugin. For detailed information, refer to section [Two Plugins: Cordova and Capacitor](https://docs.google.com/document/d/10qjRTGV8nGrwZwxyBxCvTVX0Y1qxaG1mlvXVlpNCblg/edit?usp=sharing).

## Supported mobile plugins

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
| Payments | Allows the addition of a payments experience using Apple Pay and Google Pay.	| No |
| Performance Monitoring | Firebase-based plugin that lets you understand how you can improve the performance of your app. | No |
| SSL Pinning | Provide an extra layer of security to HTTPS communications by adding a verification of the server certificate against hashes of public keys. | No |
| Touch ID | Use authentication with biometrics in your application. | No |

### Important considerations when using plugins

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

