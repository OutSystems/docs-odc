---
guid: fca52f4d-822f-4375-9081-285d2c43b9d4
locale: en-us
summary: Apply these recommendations when testing and debugging mobile apps in OutSystems Developer Cloud to catch issues early and diagnose problems efficiently.
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
  - Best Practices
  - Debugging
  - Logging
  - Mobile app
  - Native App
  - Testing
  - Troubleshooting
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Best practices for testing and debugging mobile apps

Testing and debugging mobile apps is more complex than testing web apps because issues arise at the web layer, the native layer, or the interaction between the two. Following these recommendations helps you choose the right tool for each type of problem and build confidence in your app before each release.

## Test on real physical devices { #real-devices }

Simulators and emulators are useful for rapid iteration but do not accurately reproduce the hardware diversity, performance characteristics, memory constraints, and OS behavior of real devices. Android devices from different manufacturers vary in hardware capabilities, system configurations, and OS customizations, which affects how your app renders, handles permissions, and accesses hardware across the devices your users carry. Some native capabilities also require a physical device: camera integration, for example, cannot be tested in an iOS simulator.

### Recommendation

Test across devices from multiple Android manufacturers whenever native integrations or extensibility configurations change, and periodically for regression testing, as hardware capabilities and OS customizations directly affect native behavior. For the same reason, test on devices running the latest iOS version and the oldest your app supports, which is iOS 15 by default for MABS 12.

To install a build on a device for testing, generate a mobile package with the **Debug** build type for Android or the **Development** build type for iOS, then scan the QR code displayed in ODC Portal with your device to download and install the app. ODC authentication may be required. For detailed steps, refer to [Create mobile app package](../creating-mobile-package.md). iOS Development builds require additional steps; for details, refer to [Mobile app build types](../mobile-build-types.md#iOS-dev).

Test all flows that exercise native capabilities, such as plugins, system bars, device sensors, and offline behavior, on a physical device.

Do not rely on the **Emulate using Google Chrome** target in ODC Studio as your only testing environment. Use it for rapid logic iteration, then validate on a real device before releasing.

### Benefits

Testing on real hardware surfaces issues that simulators cannot reproduce: memory pressure, manufacturer-specific UI differences, and platform-specific permission dialogs. A diverse device matrix reflects the real spread of hardware your users carry and reduces the risk of shipping issues that only appear on specific manufacturers or hardware tiers.

## Use browser fallbacks to enable non-native testing { #browser-testing }

Native plugins are unavailable when running your app in the browser, in the ODC Studio debugger with the Chrome emulation target, or when distributing your app as a [Progressive Web App (PWA)](../pwa.md). Without fallbacks, any flow that calls a plugin fails in the browser, which forces you to use a physical device even when native behavior is not what you are testing.

### Recommendation

Implement a browser fallback for every plugin call in your ODC library client actions. For guidance on implementing browser fallbacks and PWA-specific alternatives, refer to [Best practices for native integrations and plugins](best-practices-native-plugins.md).

### Benefits

Browser fallbacks let you test the non-native portions of your app, such as logic flows, data actions, screen navigation, and error handling, without a physical device for every iteration. This shortens the feedback loop for logic-level issues and reduces time spent on test setup.

## Test under real-world network conditions { #network-conditions }

Mobile apps operate across a wide range of network conditions, from fast Wi-Fi to 3G, intermittent connectivity, and full offline. Many bugs only surface under poor or absent connectivity, and these are often the issues that matter most to field users.

### Recommendation

When you add or modify functionality that depends on network requests, such as offline sync, data fetching, or timeout handling, test under degraded and offline conditions. The simplest approaches require no additional tools:

* **Full offline:** Enable airplane mode on your test device and verify that offline-first features work correctly and the app does not crash or display unhandled errors.
* **Degraded connectivity:** On Android, switch the device to 3G mode in mobile data settings to simulate a slow network. Verify that the app stays responsive and that loading states, timeouts, and error messages behave as expected.

For finer-grained simulation, such as packet loss or request inspection, refer to [Inspect network traffic](../../../debugging-apps/inspect-network-traffic.md).

### Benefits

Catching network-related issues before release prevents failures in the field. Mobile users routinely experience poor connectivity, and an app that degrades gracefully in those conditions builds user trust and improves retention.

## Use browser DevTools to debug the web layer on real devices { #remote-devtools }

The [ODC Studio debugger](../../../debugging-apps/intro.md) is the first tool to reach for when diagnosing logic errors, but it only works in the Development stage and only exposes the OutSystems logic layer. Remote browser DevTools give you direct access to the full web layer, letting you inspect raw network requests and response payloads and view JavaScript errors in the console. They are also useful when a bug only reproduces on a specific device or OS version: you install a Debug (Android) or Development (iOS) build on that device, connect it via USB, and inspect it from your desktop browser without needing ODC Studio. For production issues where you cannot install a debug build, refer to the [client-side logging recommendation](#client-side-logging) instead.

### Recommendation

#### On Android using Chrome DevTools

Enable **USB debugging** on the device, install a **Debug** build, and connect the device to your computer via USB. For detailed steps, refer to [Install the mobile app on a device](../../../debugging-apps/intro.md#install-the-mobile-app-on-a-device).

1. Open the mobile app you previously installed.
1. On your computer, open Chrome and navigate to `chrome://inspect/#devices`.
1. Select the WebView for your app and click **Inspect** to open DevTools.

Once connected, you can:

* Step through generated JavaScript execution in the **Sources** tab.
* Inspect network requests and response payloads in the **Network** tab.
* View JavaScript errors in the **Console** tab. Enable **Preserve log** to retain console output across screen navigations.
* Inspect local entity data in the **Application** tab.
* Identify long wait times in the **Performance** tab. Extended gaps with no CPU or network activity typically indicate the app is waiting for a server response or a plugin operation.

#### On iOS using Safari Web Inspector

Enable **Web Inspector** on the device, install a **Development** build, and connect the device to your Mac via USB. For detailed steps, refer to [Install the mobile app on a device](../../../debugging-apps/intro.md#install-the-mobile-app-on-a-device).

1. Open the mobile app you previously installed.
1. On your Mac, open Safari. In the **Develop** menu, select your device, then select the WebView for your app.

Safari Web Inspector provides equivalent capabilities to Chrome DevTools for the web layer of your iOS app, including console inspection, script debugging, network monitoring, and storage inspection.

### Benefits

Remote browser DevTools give you visibility into the web layer that the ODC Studio debugger does not expose, including storage data, all running on real hardware. Connecting the specific device with the problem to your desktop means you inspect exactly what that environment produces, without modifying the app or adding diagnostic code.

## Use Xcode and Android Studio for native-layer debugging { #native-tools }

Chrome DevTools and Safari Web Inspector cover the web layer of your app, including JavaScript logic, screen rendering, and network requests. They do not surface native-layer issues such as plugin errors, native exceptions, failed build configurations, or hardware access errors. For these, native IDE tooling provides the visibility you need.

### Recommendation

Use the native IDE for your platform when the issue involves a plugin crash, a native exception or crash report, a build configuration problem in `AndroidManifest.xml`, `Info.plist`, or a build action, or a hardware issue that does not surface in the web layer.

* **Android:** Generate a **Debug** build and install it on the device. Open Android Studio, connect your device via USB, and use **Logcat** to view native logs and crash reports filtered by your app's package name.
* **iOS:** Generate a **Development** build and install it on the device. Open Xcode, go to **Window** > **Devices and Simulators**, and select your device. Use **Open Recent Logs** to inspect crash reports and **Open Console** for live log streaming. If you do not have signing credentials set up, use the **Simulator** build type instead to run the app in Xcode Simulator and inspect logs there, keeping in mind its [architectural limitations](../mobile-build-types.md#iOS-simulator).

Before using the native IDE, ensure you generate the package with the correct build type. Debug and Development builds enable additional native logging that is reduced or absent in release builds. For detailed steps, refer to [Create mobile app package](../creating-mobile-package.md).

### Benefits

Native IDEs surface crashes, internal plugin errors, and build configuration issues that are invisible to browser DevTools. Some plugin failures produce no error in the web layer and are only diagnosable from native logs, making native-layer tooling essential for any app that uses native capabilities.

## Implement client-side logging for production diagnostics {#client-side-logging}

All the debugging tools covered in this article require a debug build and are unavailable in production environments. When a user reports a production issue, particularly on a specific device, OS version, or network condition, you have no direct visibility into what is happening on their device. Without a logging mechanism, diagnosing production issues requires guesswork or lengthy interaction with the user to reproduce the problem.

### Recommendation

Use the built-in **LogMessage** system action to log diagnostic messages from client actions at **Error**, **Warning**, or **Information** level. Logs appear in ODC Portal under **Monitoring** > **Logs** and are retained for up to four weeks. The action supports offline scenarios: if the device has no connectivity, log entries are queued and sent when connectivity is restored.

Call `LogMessage` at meaningful diagnostic points and avoid logging sensitive personal or financial information. For more information about viewing and filtering logs, refer to [Monitoring and troubleshooting apps](../../../monitor-and-troubleshoot/monitor-apps.md#logs).

For native crash reporting, integrate the supported Firebase Crashlytics Plugin from the [Firebase plugins](../../../integration-with-systems/mobile-plugins/firebase-plugin/intro.md) to capture crash reports from the native layer and diagnose crashes that do not surface in ODC logs.

### Benefits

Client-side logging gives you visibility into production issues that cannot be reproduced in a development environment. By capturing the exact sequence of events on the affected device, you reduce the time needed to diagnose and resolve production issues and validate the fix before deploying it broadly.

## Related resources

Refer to the following resources for further guidance on debugging and monitoring and native integrations.

* [Debugging apps](../../../debugging-apps/intro.md)
* [Inspect network traffic](../../../debugging-apps/inspect-network-traffic.md)
* [Monitoring and troubleshooting apps](../../../monitor-and-troubleshoot/monitor-apps.md)

* [Best practices for native integrations and plugins](best-practices-native-plugins.md)
* [Use mobile plugins](../../../integration-with-systems/mobile-plugins/intro.md)
