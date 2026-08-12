---
guid: f04447c0-bbbb-4b20-aa16-5f0291ebbc5e
locale: en-us
summary: Apply these recommendations to handle native app lifecycle, system back navigation, deep links, system bars, and device orientation in OutSystems Developer Cloud mobile apps.
figma:
coverage-type:
  - evaluate
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Best Practices
  - Capacitor
  - Cordova
  - Lifecycle
  - Mobile app
  - Native App
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Best practices for app lifecycle, navigation, and deep linking

The native shell sits between the mobile operating system and your app's screens, so it decides how lifecycle transitions, system back navigation, deep links, system bars, and orientation reach the code you build in ODC Studio. Configuring this native layer correctly keeps your app responsive to the platform and predictable for users. These recommendations cover what you control at the native shell; behavior that runs inside your app, such as reacting to a lifecycle event or navigating between screens, is handled in your app's logic and is cross-linked rather than repeated here.

## Handle native app lifecycle transitions {#handle-lifecycle-transitions}

The operating system moves your app through foreground, background, resume, and pause states. The native shell observes these transitions to keep its own work correct, while your app reacts to them through ODC application events. Knowing which layer does what keeps your lifecycle handling in the right place.

### Recommendation

The native shell handles operating-system lifecycle housekeeping automatically — for example, keeping your authenticated session current when the app returns to the foreground — so you don't wire it up.

Handle the transitions your app cares about with the matching ODC event:

* **Resume** — to run logic when the app returns to the foreground, such as re-checking session validity or triggering a data sync, use the **On Application Resume** system event. See [On Application Resume](../../logic/application-resume.md).
* **Pause and background** — there is no built-in low-code event for the app being sent to the background. If you need to react — for example, to pause background work — add a [JavaScript element](../../../integration-with-systems/javascript/javascript.md) that listens for the `pause` document event.

Lifecycle handling is the same whether your app uses the [Cordova or the Capacitor](../mabs-overview.md) shell: use the **On Application Resume** event rather than any shell-specific behavior.

### Benefits

Keeping lifecycle housekeeping in the native shell and lifecycle reactions in your app means your session checks and background-work pauses fire reliably on both iOS and Android, and on both the Cordova and Capacitor shells, without fragile native hooks that can break as [Mobile App Build Service (MABS)](../mabs-overview.md) or the frameworks evolve.

## Route system back navigation through the native shell {#route-system-navigation}

Mobile platforms provide a system back gesture that lives outside your screens: the back gesture on Android and the back-swipe on iOS. The native shell decides what these do before your screens react, so treat them as a native-layer concern that is distinct from in-app, screen-to-screen navigation.

### Recommendation

Let the native shell own the Android back gesture. When the user goes back, the shell navigates the WebView back through its history one entry at a time. When there is no history left, it hands control to the operating system so the app can close. You don't wire this up yourself.

On iOS, the native shell does not add a custom handler for the back-swipe gesture. Back navigation on iOS is driven by your app's in-app navigation running in the WebView.

Keep screen-to-screen navigation — the navigation stack, route-driven data loading, and in-app back behavior — in your app's logic, not the native shell. See [UI flows](../../ui/navigation/ui-flow.md) for in-app screen navigation.

The behavior is the same from your app's perspective on both the Cordova and Capacitor shells: back navigation is mediated by the native shell and the WebView history.

### Benefits

Because the native shell maps the back gesture to WebView history automatically, back navigation behaves the way users expect across your screens without per-screen wiring, and the app exits cleanly when the user is at the navigation root.

## Configure and handle deep links and custom URL schemes {#configure-deep-links}

Deep links let a browser, another app, or a notification open your app at a specific place. In ODC, MABS configures deep linking for you at build time from your app's identifier, so the native shell receives matching links on both iOS and Android. Your job is to decide what happens when a link arrives.

### Recommendation

You don't register URL schemes or edit the native project. When MABS builds your app, it configures a deep link URL scheme based on your app's identifier on both iOS and Android. For how the scheme is formed and how to trigger a deep link, see [How to define mobile app deep links](https://success.outsystems.com/documentation/how_to_guides/development/how_to_define_mobile_app_deep_links/).

The native shell receives a matching link and hands it to your app. Decide how the link is handled:

* In a Capacitor app, the default is to navigate to the link's URL. To route it yourself, define a `window.handleOpenURL(url)` function in a [JavaScript element](../../../integration-with-systems/javascript/javascript.md). See [Using universal extensibility configurations JSON schema](../extensibility-configurations-use-cases.md).
* In a Cordova app, set the `deeplinksHandler` property in the [app extensibility configuration](../extensibility-configurations/extensibility-app-reference.md) to `default`, `event`, or `function`. For a worked example, see [Cordova-based extensibility configurations use cases](../cordova-extensibility-configurations-use-cases.md).

Link handling works the same whether your app uses the Cordova or the Capacitor shell.

### Benefits

Because ODC configures deep linking from your app identifier, links open your app reliably from browsers, other apps, and notifications on both iOS and Android, and you handle them in one place instead of writing platform-specific glue code.

## Configure system bars, edge-to-edge display, and safe areas {#configure-system-bars}

The status and navigation bars, edge-to-edge layout, and safe-area or notch handling span two layers: what the native shell sets for the app window, and what your UI consumes as CSS inside the WebView. Configure each setting in the layer that owns it.

### Recommendation

Two system-bar settings belong to the native layer, and you set them in your [app extensibility configuration](../extensibility-configurations/extensibility-app-reference.md):

* `systemBars.style` — the text and icon style of the system bars: `default` (follows the device's light or dark appearance), `light`, or `dark`. You can override it per platform, for example, with a separate `android` value.
* `systemBars.statusBarBackgroundColor` — the status bar background color, as a hex value.

Edge-to-edge display and safe-area handling stay in your app's UI: your screens read the `env(safe-area-inset-*)` CSS variables to keep content clear of the status and navigation bars. This matters especially on notched devices and on Android 16 and later, where edge-to-edge display is enforced.

For the full configuration reference, the safe-area inset variables, and worked examples for both the Capacitor and Cordova shells, see [Customize system bars with edge-to-edge display](../extensibility-configurations/customize-system-bars-edge-to-edge.md).

### Benefits

Setting the system bars in your extensibility configuration while consuming safe-area insets in your UI keeps content clear of the system bars on notched and edge-to-edge devices, with each setting configured in one place.

## Lock and handle device orientation at the native layer {#handle-device-orientation}

Whether your app rotates or stays locked to one orientation is a native, build-time setting for the whole app, not something you toggle per screen at runtime. Decide the supported orientations up front and configure them in the native layer.

### Recommendation

Set the supported orientations in your [app extensibility configuration](../extensibility-configurations/extensibility-app-reference.md) with the `orientation` property: `portrait`, `landscape`, or `all`. Choosing `all` lets the device rotate freely. On iOS, you can also target a device family with `targetDevice` (`phone`, `tablet`, or `all`). The native shell applies your choice to both platforms when the package is built.

Orientation changes then reach your app through the standard resize and rotation, so your screens adjust in place. On Android, the app rotates without reloading your screens.

The `orientation` setting applies the same way whether your app uses the Cordova or the Capacitor shell.

### Benefits

Declaring supported orientations once at the native layer gives consistent rotation behavior across iOS, Android, and both shells, and lets Android rotate smoothly without reloading your screens, so users don't lose their place when they turn the device.

## Related resources

The following resources group related app lifecycle, navigation, and configuration topics by area.

### Lifecycle and JavaScript extensibility

These resources cover reacting to lifecycle events and extending your app's behavior with JavaScript.

* [On Application Resume](../../logic/application-resume.md)
* [Extend Your Apps Using JavaScript](../../../integration-with-systems/javascript/javascript.md)
* [Screen and block lifecycle events](../../ui/screen-block-lifecycle-events.md)

### Navigation

This resource covers in-app, screen-to-screen navigation.

* [UI flows](../../ui/navigation/ui-flow.md)

### Deep links and system bars configuration

These resources cover the extensibility configuration schema and the system bars configuration reference.

* [App extensibility configuration JSON schema](../extensibility-configurations/extensibility-app-reference.md)
* [Customize system bars with edge-to-edge display](../extensibility-configurations/customize-system-bars-edge-to-edge.md)

### Native shell and building mobile package

These resources cover switching native shells and building your app package.

* [Migrate a mobile app from Cordova to Capacitor](../migrate-cordova-to-capacitor.md)
* [Create mobile app package](../creating-mobile-package.md)
