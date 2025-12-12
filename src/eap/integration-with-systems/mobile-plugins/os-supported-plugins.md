---
guid: 7b6cb77f-a789-48ae-8070-1631b51722d8
locale: en-us
summary: This article provides a list of OutSystems supported mobile plugins that are ODC libraries that wrap the plugin.
figma: 
coverage-type:
  - remember
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Plugins,mobile plugins,plugin integration
outsystems-tools:
  - none
helpids:
---
# OutSystems supported mobile plugins

The OutSystems-supported mobile plugins are mobile libraries that wrap the plugin so that the plugin can be used across apps. Some of them are supported when distributing your app as a progressive web app (PWA).

All supported plugins can be used in both Capacitor and Cordova apps.

The table lists the OutSystems-supported mobile plugins available in the [Forge](https://www.outsystems.com/forge/).

| Plugin | Description | Supported in PWA |
| ------------------------- | ------------------------------------------------------------ | ---------------- |
| Analytics | Firebase-based plugin that lets you gather information about app use. | No |
| AppShield | Protect your mobile apps from tampering. OutSystems AppShield hardens the native mobile build, enabling the app to detect attempts of modification and misuse. | No |
| [Barcode](barcode/intro.md) | Access the camera to scan barcodes and QR codes. | Yes |
| Calendar | Access the calendar of your device. | No |
| Camera | Access the camera capabilities of the device. | Yes |
| Ciphered Local Storage | Keep your mobile application's sensitive data safe using a ciphered local storage database. | No |
| [Cloud Messaging](firebase-plugin/intro.md) | Firebase-based plugin to give your app users a state-of-the-art notifications experience. | No |
| Contacts | Access the contacts of your device. | No |
| Crash Reporting | Firebase-based plugin that provides realtime crash reporting to help you track, prioritize, and fix stability issues. | No |
| [File](file-plugin/intro.md) | Manage files and folders within the app sandbox. | No |
| [File Transfer](file-transfer-plugin/intro.md) | Upload and download files in background. | Yes |
| [File Viewer](file-viewer/intro.md) | View remote or app resource files. | No |
| [Haptics](./haptics-plugin/intro.md) | Provides physical feedback to your app users through touch and vibration. | No |
| [Health & Fitness](health-fitness/intro.md) | Provides access to health and fitness data. Uses HealthKit API for iOS and Health Connect API for Android. | No |
| [InAppBrowser](inapp-browser/inapp-browser.md) | Open external URLs directly in your application. | No |
| [Keyboard](keyboard-plugin/intro.md) | Provides keyboard display, visibility control, and keyboard event tracking | No |
| [Key Store](keystore-plugin/intro.md) | Store encrypted key-value pairs with optional authentication. | No |
| Local Notifications | Send app notifications to the device when the application isn't running in the foreground. | No |
| [Location](location/intro.md) | Access the GPS capabilities the device. | Yes |
| OneSignal Notifications | Push notifications using OneSignal, with deep-linking and actions. | No |
| [Payments](payments-plugin/intro.md) | Allows the addition of a payments experience using Apple Pay and Google Pay. | No |
| Performance Monitoring | Firebase-based plugin that lets you understand how you can improve the performance of your app. | No |
| [SSL Pinning](ssl-pinning/intro.md) | Provides an extra layer of security to HTTPS communications by adding a verification of the server certificate against hashes of public keys. | No |
| Touch ID | Uses authentication with biometrics in your application. | No |

## Install a plugin and use it in your app

The plugins are available from the Forge repository. To use a plugin in your app, you first need to install the plugin to your organization and add the plugin elements to your app.

To install a supported plugin from Forge:

1. Go to ODC Portal.
  
1. Click **Forge** find the plugin and open the details page.
   The details page displays the mobile framework compatibility.

1. Click **Install** and follow the instructions to install the plugin. Optionally, install the demo app that comes with the plugin.

1. Once the installation finishes, add the actions you want to use as public elements in your mobile app.

## Related resources

* [Mobile plugins](intro.md)
